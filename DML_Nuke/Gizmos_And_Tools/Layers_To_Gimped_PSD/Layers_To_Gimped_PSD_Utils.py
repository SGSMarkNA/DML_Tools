import json
import nuke
import DML_Tools
DML_Nuke = DML_Tools.DML_Nuke
DML_PYQT = DML_Tools.DML_PYQT
import os
import subprocess
import Layers_To_Gimped_PSD_Nodes

#----------------------------------------------------------------------
def is_Single_Frame_Comp():
	""""""
	root = nuke.root()
	first_frame,last_frame = root.knob("first_frame").value(),root.knob("last_frame").value()
	if first_frame == last_frame:
		return True
	else:
		return False

#----------------------------------------------------------------------
def find_All_DML_Layers_To_Gimped_PSD():
	""""""
	return DML_Nuke.dml.to_DML_Nodes(nuke.allNodes("DML_Layers_To_Gimped_PSD",nuke.root(),recurseGroups=True))
#----------------------------------------------------------------------
def find_All_DML_Gimped_PSD_Groups():
	""""""
	res = [node for node in nuke.allNodes("Group",nuke.root(),recurseGroups=True) if "DML_NODE_CLASS" in node.knobs() and node.knob("DML_NODE_CLASS").getText() == "DML_Gimped_PSD_Group"]
	res = DML_Nuke.dml.to_DML_Nodes(res)
	return res
#----------------------------------------------------------------------
def rebuild_Errored_DML_Layers_To_Gimped_PSD():
	""""""
	for node in find_All_DML_Layers_To_Gimped_PSD():
		if node.error():
			node.create_Layers_To_Render()
#----------------------------------------------------------------------
def get_Enabled_DML_Layers_To_Gimped_PSD_Nodes():
	""""""
	res = []
	for node in find_All_DML_Layers_To_Gimped_PSD():		
		if False:
			isinstance(node,Layers_To_Gimped_PSD_Nodes.DML_Layers_To_Gimped_PSD)
			
		if not node.psd_build_group.knob("disable").value():
			res.append(node)
	return res
#----------------------------------------------------------------------
def get_Enabled_DML_Layers_To_Gimped_PSD_Dict():
	""""""
	res = []
	psd_nodes = get_Enabled_DML_Layers_To_Gimped_PSD_Nodes()
	for psd_node in psd_nodes:
		if False:
			isinstance(psd_node,Layers_To_Gimped_PSD_Nodes.DML_Layers_To_Gimped_PSD)			
		
		write_nodes = psd_node.psd_build_group.get_Write_Nodes()
		write_node = write_nodes[-1]
		data = dict(psd=psd_node,grp=psd_node.psd_build_group,wn=write_node,allwrns=write_nodes)
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
def create_PSD_Build_Info_V2(frames):
	""""""
	rebuild_Errored_DML_Layers_To_Gimped_PSD()
	psd_nodes = get_Enabled_DML_Layers_To_Gimped_PSD_Nodes()
	multi = not is_Single_Frame_Comp()
	image_formate                 = nuke.root().format()
	# store the width and height in a list
	baked_data = dict(builds=[], image_size=[image_formate.width(),image_formate.height()])

	for psd_node in psd_nodes:
		isinstance(psd_node,Layers_To_Gimped_PSD_Nodes.DML_Layers_To_Gimped_PSD)
		
		for frame in frames:
			for build in psd_node.generate_Json_Data(frame,multi):
				baked_data["builds"].append(build)
	return baked_data

#----------------------------------------------------------------------
def Bake_PSD_Build_Info(gimped_psd_data):
	""""""
	json_file_path = get_Json_File_Path()
	with file(json_file_path,"w") as fp:
		json.dump(gimped_psd_data, fp,indent=4)

#----------------------------------------------------------------------
def _generate_Json_Data(psd_node,writeNode,frame,multi_frame=True):
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

		if nuke.root().knob("DML_nuke_views_system_use_image_name")==None:
			nuke.showSettings()

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
			# exam : C:/User_Input_Folder/verions/PNGS/view_folder/frame_folder
			# exam : C:/Psd_Local_output/v06/PNGS/Background/001

			# stores the path for each image to be used in the psd build in the older that it should be added
			Layer_Order_Paths = []

			# iterate over each layer name
			for layer_name in layer_order_names:
				# exam : Background

				# build the path to the image using the current view folder and layer name
				# exam : C:/User_Input_Folder/verions/PNGS/view_folder/frame_folder
				# exam : C:/Psd_Local_output/v06/PNGS/Background/001
				layer_path = os.path.join(view_layer_folder,layer_name+".png")
				# exam : C:/User_Input_Folder/verions/PNGS/view_folder/frame_folder/layer_name.png
				# exam : C:/Psd_Local_output/v06/PNGS/Background/001/Background.png

				# normalize the path 
				layer_path = os.path.normpath(layer_path)
				# force consistent pathings
				layer_path = layer_path.replace("\\","/")
				# add it to the collection
				Layer_Order_Paths.append(layer_path)
			# exam : C:/Psd_Local_output/v06/PNGS/Background/001/Background.png
			# exam : C:/Psd_Local_output/v06
			# exam : folder_end: Blurred_Oval_Bloo/001
			folder_start,folder_end = view_layer_folder.split("/PNGS/",1)
			# exam : Blurred_Oval_Bloo/001
			# exam : Blurred_Oval_Bloo
			image_name              = folder_end.split("/")[0]

			if multi_frame:
				# exam : C:/Psd_Local_output/v06/Blurred_Oval_Bloo
				psd_folder_path         = os.path.join(folder_start,image_name).replace("\\","/")
				# exam : Blurred_Oval_Bloo_001.psd
				psd_file_name                 = psd_folder_path.split("/")[-1] + "_" + padded_frame + ".psd"
			else:
				# exam : C:/Psd_Local_output/v06/Blurred_Oval_Bloo
				psd_folder_path         = os.path.join(folder_start).replace("\\","/")
				# exam : Blurred_Oval_Bloo_001.psd
				psd_file_name                 = image_name+".psd"
			# last combine the psd folder path with the psd file name for this view
			# exam : C:/Psd_Local_output/v06/Blurred_Oval_Bloo/Blurred_Oval_Bloo_001.psd
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

		folder_start,folder_end = layers_folder.split("/PNGS/",1)
		# exam : Blurred_Oval_Bloo/001
		# exam : Blurred_Oval_Bloo
		image_name              = folder_end.split("/")[0]

		psd_folder_path         = os.path.join(folder_start).replace("\\","/")

		if multi_frame:
			psd_file_name                 = image_name + "_" + padded_frame + ".psd"
			#psd_file_name                 = psd_folder_path.split("/")[-1] + "_" + padded_frame + ".psd"
		else:
			# exam : C:/Psd_Local_output/v06/Blurred_Oval_Bloo
			#psd_folder_path         = os.path.join(folder_start).replace("\\","/")
			# exam : Blurred_Oval_Bloo_001.psd
			psd_file_name                 = image_name+".psd"

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
	pip = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	#pip = subprocess.Popen(cmd)
	return pip

#----------------------------------------------------------------------
def run_Json_Build_Data(arg):
	"""This Runs The Gimp Psd Builder For Local Renders"""
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
				print proc.stdout.read()
				print proc.returncode
				if not proc.poll() == None:
					print proc.returncode
					all_procs.remove(proc)
					compleated+=1
					task.setProgress( int( float(compleated)/build_count * 100 ) )