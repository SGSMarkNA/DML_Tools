
import json
import nuke
import DML_Tools
DML_Nuke = DML_Tools.DML_Nuke
import os
import subprocess

#----------------------------------------------------------------------
def get_Enabled_DML_Gimped_PSD_Group_Nodes():
	""""""
	res = []
	for node in nuke.allNodes("Group",nuke.root(),recurseGroups=True):
		if not node.knob("disable") == None:
			if not node.knob("disable").value():
				knb = node.knob("DML_NODE_CLASS")
				if not knb == None:
					if knb.getText()== "DML_Gimped_PSD_Group":
						res.append(node)
	return res

#----------------------------------------------------------------------
def get_Enabled_DML_Layers_To_Gimped_PSD_Dict():
	""""""
	res = []
	gimped_psd_nodes = get_Enabled_DML_Gimped_PSD_Group_Nodes()
	for group in gimped_psd_nodes:
		psd_node = DML_Nuke.Nuke_Scripts.find_upstream_node(group,"DML_Layers_To_Gimped_PSD")
		if psd_node is not None:
			write_nodes = nuke.allNodes("Write",group)
			write_nodes.sort(key=lambda n:n.knob("render_order").value())
			write_node = write_nodes[-1]
			data = dict(psd=psd_node,grp=group,wn=write_node,allwrns=write_nodes)
			res.append(data)
	return res

#----------------------------------------------------------------------
def get_Json_File_Path():
	""""""
	json_folder    = nuke.script_directory()
	json_file_name = os.path.splitext(os.path.split(nuke.root().name())[1])[0]+"_psd_build_info.json"
	json_file_path = os.path.join(json_folder,json_file_name).replace("\\","/")
	return json_file_path

#----------------------------------------------------------------------
def create_PSD_Build_Info(frames,gimped_psd_data=None):
	""""""
	if gimped_psd_data is None:
		gimped_psd_data = get_Enabled_DML_Layers_To_Gimped_PSD_Dict()

	image_formate                 = nuke.root().format()
	# store the width and height in a list
	Image_Size                    = [image_formate.width(),image_formate.height()]

	baked_data = dict(builds=[],image_size=Image_Size)

	for data_item in gimped_psd_data:
		psd = data_item['psd']
		wn  = data_item['wn']
		for frame in frames:
			frame_build_data = _generate_Json_Data(psd, wn, frame)
			for build in frame_build_data:
				baked_data["builds"].append(build)
	return baked_data

#----------------------------------------------------------------------
def Bake_PSD_Build_Info(gimped_psd_data):
	""""""
	json_file_path = get_Json_File_Path()
	with file(json_file_path,"w") as fp:
		json.dump(gimped_psd_data, fp)

#----------------------------------------------------------------------
def _generate_Json_Data(psd_node,writeNode,frame):
	""""""
	res = []
	# can a list of all the nuke views
	all_view_names                = nuke.views()
	# store the options that determans if views are to be used or not
	dml_enable_views              = psd_node.knob("dml_enable_views").value()
	# get the views that are going to be rended out
	view_selection                = psd_node.knob("DML_Nuke_View_Selection").value().split()
	# get the layer order that the psd builder will use when assemblying the psd file
	layer_order_names             = eval(psd_node.knob("DML_Layer_Order_layers").getText())
	# get the frame padding
	frame_padding                 = int(psd_node.knob("dml_frame_padding").value())

	# using the current frame and the padding create a padded_frame for use in file path image createion
	padded_frame  = str(frame).zfill(frame_padding)

	psd_padded_frame_sufix = "_" + padded_frame + ".psd"

	# get the folder path that this write node will render the image to
	layers_folder                 = os.path.dirname(nuke.filename(writeNode,nuke.REPLACE))
	layers_folder                 = layers_folder.replace(layers_folder.split("/")[-1],padded_frame)
	# check if the view are enabled
	# if so then things get a little tricky
	# at no point in the render process is there view context so nuke.thisView() will never work.
	# so to do anykind of actions that are relative to a view you have to manuly figure it out
	# by diceting the folder path and the views that this write node is going to render
	if dml_enable_views:
		# create and list that will be used to store the folder paths for each view
		view_layer_folders = []
		# this will be a prebuilt forder path with built in formating that will replaced with view names  
		layers_folder_exp = None

		# check the root node to determan if view names or image names are to be used
		if nuke.root().knob("DML_nuke_views_system_use_image_name").value():
			# get a list of the image name for each view
			all_image_names  = [nuke.DML_Nuke_View_System.get_Image_Name_From_View_Name(v) for v in all_view_names]

			# first we need to replace the view section of the folder path with {} for formating later
			# because we don't know what view is the active view we have to find it useing the layers_folder
			for image_name in all_image_names:
				# check if the image_name is in the layers_folder path
				if image_name in layers_folder.split("/"):
					# if so replace it and we are done searching
					layers_folder_exp = layers_folder.replace(image_name,"{}")
					break

			# this is to make sure that we found the view to replace
			if layers_folder_exp is not None:
				# get the image names for the views this write node is using 
				view_image_names = [nuke.DML_Nuke_View_System.get_Image_Name_From_View_Name(v) for v in view_selection]
				# iterate over each image name and build a folder path for the image name
				for image_name in view_image_names:
					view_layer_folders.append(layers_folder_exp.format(image_name))
		else:
			# first we need to replace the view section of the folder path with {} for formating later
			# because we don't know what view is the active view we have to find it using the layers_folder
			for view_name in all_view_names:
				# check if the view is in the layers_folder path
				if view_name in layers_folder.split("/"):
					# if so replace it and we are done searching
					layers_folder_exp = layers_folder.replace(view_name,"{}")
					break

			# this is to make sure that we found the view to replace
			if layers_folder_exp is not None:
				# iterate over each view and build a folder path for the view name
				for view_name in view_selection:
					view_layer_folders.append(layers_folder_exp.format(view_name))

		# iterate over each view folder
		for view_layer_folder in view_layer_folders:
			# stores the path for each image to be used in the psd build in the older that it should be added
			Layer_Order_Paths = []

			# iterate over each layer name
			for layer_name in layer_order_names:
				# build the path to the image using the current view folder and layer name
				layer_path = os.path.join(view_layer_folder,layer_name+".png")
				# normalize the path 
				layer_path = os.path.normpath(layer_path)
				# force consistent pathings
				layer_path = layer_path.replace("\\","/")
				# add it to the collection
				Layer_Order_Paths.append(layer_path)

			# get the folder that the psd files should be created in
			psd_folder_path               = os.path.dirname(view_layer_folder.split("Layers_Frames",1)[0])
			# this gets the folder that contains the frame folders witch is also the view name and combines it with the frame padding
			psd_file_name                 = psd_folder_path.split("/")[-1] + psd_padded_frame_sufix
			# last combine the psd folder path with the psd file name for this view
			PSD_File_Path                 = os.path.join(psd_folder_path,psd_file_name).replace("\\","/")
			# create the data to be writen to json
			data = dict(PSD_File_Path     = PSD_File_Path,
						Layer_Order_Paths = Layer_Order_Paths)
			res.append(data)

	else:
		# stores the path for each image to be used in the psd build in the older that it should be added
		Layer_Order_Paths = []
		# iterate over each layer name
		for layer_name in layer_order_names:
			# build the layer file name
			layer_file_name = layer_name + ".png"
			# build file path to the image using the layers folder and the layer file name
			layer_file_path = os.path.join(layers_folder,layer_file_name)
			# normalize the path 
			layer_file_path = os.path.normpath(layer_file_path)
			# force consistent pathings
			layer_file_path = layer_file_path.replace("\\","/")
			# add it to the collection
			Layer_Order_Paths.append(layer_file_path)

		# get the folder that the psd files should be created in
		psd_folder_path               = os.path.dirname(layers_folder.split("Layers_Frames",1)[0])
		## this gets the folder that contains the images witch is also the frame with its frame padding exp '001.psd'
		#psd_file_frame_padding        = padded_frame + ".psd"
		# this gets the folder that contains the frame folders witch is also the view name and combines it with the frame padding
		psd_file_name                 = psd_folder_path.split("/")[-1] + psd_padded_frame_sufix
		# last combine the psd folder path with the psd file name for this view
		PSD_File_Path                 = os.path.join(psd_folder_path,psd_file_name).replace("\\","/")

		# create the data to be writen to json
		data = dict(PSD_File_Path     = PSD_File_Path,
					Layer_Order_Paths = Layer_Order_Paths)
		res.append(data)
	return res

#----------------------------------------------------------------------
def process_Gimp_PSD_Build(psd_file,image_files,image_width,image_height):
	""""""
	python_script_path = os.path.join(os.path.dirname(__file__),"Files_To_PSD_Layers.py").replace("\\","/")
	#python_script_path = r"//isln-smb/aw_config/Pipeline/Deadline/DeadlineRepository10/custom/plugins/GimpPSD/Files_To_PSD_Layers.py"
	cmd = "\\\\isln-smb\\aw_config\\Apps\\GIMP\\bin\\gimp-2.10.exe -idf --batch-interpreter python-fu-eval -b "
	cmd += '''"execfile('{}', dict(psd_file='{}',image_files={},image_width={},image_height={}),dict())"'''.format(python_script_path,psd_file,image_files,image_width,image_height)
	#pip = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	pip = subprocess.Popen(cmd)
	return pip

#----------------------------------------------------------------------
def run_Json_Build_Data(arg):
	""""""
	all_procs = []
	if isinstance(arg,str):
		with file(arg,"r") as fp:
			build_data = json.load(fp)
	elif isinstance(arg,dict):
		build_data = arg
	else:
		raise ValueError("arg must be a json file or a dict")

	image_width,image_height    = build_data["image_size"]
	builds = build_data["builds"]
	build_count = len(builds) * 2

	task = nuke.ProgressTask("Build PSD Files")
	task.setMessage("Doing Cool Stuff")

	max_sub_process_count = 5

	compleated = 0
	stoped = False
	for build in builds:
		if len(all_procs) == max_sub_process_count:
			while len(all_procs) >= max_sub_process_count:
				for proc in all_procs:
					if not proc.poll() == None:
						all_procs.remove(proc)
						compleated+=1
						task.setProgress( int( float(compleated)/build_count * 100 ) )
				if task.isCancelled():
					stoped = True
					for proc in all_procs:
						proc.kill()
					all_procs = []
					break
		image_files = list(reversed(build["Layer_Order_Paths"]))
		psd_file    = build["PSD_File_Path"]
		proc = process_Gimp_PSD_Build(psd_file,image_files,image_width,image_height)
		all_procs.append(proc)
		compleated+=1
		task.setProgress( int( float(compleated)/build_count * 100 ) )


	if not stoped:
		while len(all_procs):
			if task.isCancelled():
				for proc in all_procs:
					proc.kill()
				all_procs = []
				break				
			for proc in all_procs:
				if not proc.poll() == None:
					all_procs.remove(proc)
					compleated+=1
					task.setProgress( int( float(compleated)/build_count * 100 ) )
	del task