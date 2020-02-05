import nuke,os
import DML_Tools
import DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Generic_Widgets_Nodes
DML_Nuke = DML_Tools.DML_Nuke


def get_DML_Gimped_PSD_Group_Last_Layer_Build_Order(node):
	return eval(node.knob("dml_last_layer_build_order").getText())

################################################################################
class DML_Gimped_PSD_Group(DML_Nuke.Nuke_Nodes.Standered_Nodes.Group):
	#NODE_TYPE_RELATION        = None
	RETURN_OVERIDE_CHECK_TYPE = "Group"
	#----------------------------------------------------------------------
	@classmethod
	def _overide_Return_Check(cls,node):
		""""""
		try:
			return node.knob("DML_NODE_CLASS").value() == "DML_Gimped_PSD_Group"
		except:
			return False
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		""""""
		if not self.hasKnob("DML_NODE_CLASS"):
			knob = nuke.String_Knob("DML_NODE_CLASS","DML Node Class")
			knob.setVisible(False)
			knob.setText("DML_Gimped_PSD_Group")
			self.addKnob(knob)
		
		if not self.hasKnob("dml_folder_destination"):
			self._folder_destination_knob = nuke.Link_Knob("dml_folder_destination")
			self.addKnob(self._folder_destination_knob)
		else:
			self._folder_destination_knob = self.nuke_object.knobs()["dml_folder_destination"]
		self._folder_destination_knob.setVisible(False)
		
		if not self.hasKnob("dml_file_name"):
			self._file_name_knob = nuke.Link_Knob("dml_file_name")
			self.addKnob(self._file_name_knob)
		else:
			self._file_name_knob = self.nuke_object.knobs()["dml_file_name"]
		self._file_name_knob.setVisible(False)
		
		if not self.hasKnob("dml_frame_padding"):
			self._frame_padding_knob = nuke.Link_Knob("dml_frame_padding")
			self.addKnob(self._frame_padding_knob)
		else:
			self._frame_padding_knob = self.nuke_object.knobs()["dml_frame_padding"]
		self._frame_padding_knob.setVisible(False)
		
		if not self.hasKnob("dml_output_views"):
			self._output_views_knob = nuke.MultiView_Knob("dml_output_views")
			self.addKnob(self._output_views_knob)
		else:
			self._output_views_knob = self.nuke_object.knobs()["dml_output_views"]
		#self._output_views_knob.setVisible(False)
		
		if not self.hasKnob("dml_last_layer_build_order"):
			self._last_layer_build_order_knob = nuke.String_Knob("dml_last_layer_build_order")
			self.addKnob(self._last_layer_build_order_knob)
			self._last_layer_build_order_knob.setText(repr([]))
		else:
			self._last_layer_build_order_knob = self.nuke_object.knobs()["dml_last_layer_build_order"]
		self._last_layer_build_order_knob.setVisible(False)
		
		if not len(nuke.allNodes("Input",self.nuke_object)):
			with self.nuke_object:
				nuke.nodes.Input(xpos=0,ypos=0)
		
		self.input_node = DML_Nuke.dml.to_DML_Node(nuke.allNodes("Input",self.nuke_object)[0])
		
		if not len(nuke.allNodes("Output",self.nuke_object)):
			with self.nuke_object:
				output_node = nuke.nodes.Output(xpos=0,ypos=500)
				output_node.setInput(0,self.input_node.nuke_object)
		self.output_node = DML_Nuke.dml.to_DML_Node(nuke.allNodes("Output",self.nuke_object)[0])
		
		self._noop_node = self.nuke_object.node("PSD_LAYER_SHUFFLE_SECTION")
		if self._noop_node == None:
			with self.nuke_object:
				if self._noop_node == None:
					self._noop_node = DML_Nuke.Nuke_Nodes.Nodes.NoOp(xpos=0,ypos=250,name="PSD_LAYER_SHUFFLE_SECTION")
					self._noop_node.setInput(0, self.input_node)
					self.output_node.setInput(0, self._noop_node)
		else:
			self._noop_node = DML_Nuke.dml.to_DML_Node(self._noop_node)
	#----------------------------------------------------------------------
	def assign_knob_links(self,folder_destination,file_name,frame_padding,output_views):
		""""""
		self._file_name_knob.setLink(file_name.fullyQualifiedName())
		self._folder_destination_knob.setLink(folder_destination.fullyQualifiedName())
		self._frame_padding_knob.setLink(frame_padding.fullyQualifiedName())
		self._output_views_knob.setValue("{{" + output_views.fullyQualifiedName() + "}}")
	#----------------------------------------------------------------------
	def create_Layers_To_Render(self, layers, xOffset=200, xSpaceing=150, yOffset=100):
		# set the node to be the only thing selected
		self._noop_node.selectOnly()
		new_layer_build_order = []
		[nuke.delete(node) for node in nuke.allNodes(group=self.nuke_object) if not node in [self.input_node.nuke_object,self.output_node.nuke_object,self._noop_node.nuke_object]]
		
		# collect only the layers that exist in the noop node's layers
		createion_layers = [layer for layer in layers if layer in self.layers]
	
		# caculate the start pos of the shuffles
		master_xpos = self._noop_node.x + xOffset
		master_ypos = self._noop_node.y
	
		# keeps track of the last shuffle node created and used to connet the current shuffle node 
		last_created_shuffle = None
		
		shuffle_nodes = DML_Nuke.Nuke_Nodes.Node_List()
		write_nodes   = DML_Nuke.Nuke_Nodes.Node_List()
		# scan over each layer and create the nodes
		with self.nuke_object:
			
			for index,layer in enumerate(createion_layers):
				# create the shuffle node
				new_layer_build_order.append(layer)
				shuffle_node = DML_Nuke.Nuke_Nodes.Standered_Nodes.Shuffle(**{"in":layer, "out":"rgba", "xpos":master_xpos + (xSpaceing * index), "ypos":master_ypos,"label":"[value in ]"})
				shuffle_nodes.append(shuffle_node)
		
				# check for a last created shuffle node
				if last_created_shuffle == None:
					# if not set the current shuffle nodes input to the input start node
					shuffle_node.setInput(0,self._noop_node)
				else:
					# otherwise set the current shuffle nodes input to the shuffle node that was created just before this one
					shuffle_node.setInput(0,last_created_shuffle)
				# assign the current shuffle node to the last crated input for the next loop
				last_created_shuffle = shuffle_node
				# check if write nodes should be crated for the shuffles
				write_node=DML_Nuke.Nuke_Nodes.Standered_Nodes.Write(xpos=shuffle_node.x,
																	 ypos=shuffle_node.y + yOffset,
																	file_type="png",
																	create_directories=True,
																	channels="rgba")
				# connect the write nodes input to the current shuffle node
				write_node.setInput(0,shuffle_node)
				#write_node.knob("render_order").setValue(index+1)
				write_node.knob("file").setValue("[value parent.dml_folder_destination]/PNGS/%0[value parent.dml_frame_padding]d/[value input0.in].png")
				write_node.knob("views").setValue('{{parent.dml_output_views}}')
				write_node.knob("disable").setExpression('parent.disable')
				if "ICC_knob" in write_node.knobs():
					write_node.knob("ICC_knob").setValue('sRGB.icc')
				write_nodes.append(write_node)
		new_layer_build_order.reverse()
		self._shuffle_nodes = shuffle_nodes
		self._write_nodes   = write_nodes
		self._last_layer_build_order_knob.setText(repr(new_layer_build_order))
		return shuffle_nodes,write_nodes
	#----------------------------------------------------------------------
	@property
	def last_layer_build_order(self):
		""""""
		return eval(self._last_layer_build_order_knob.getText())
	#----------------------------------------------------------------------
	def get_Shuffle_Nodes(self):
		""""""
		shuffles = DML_Nuke.dml.to_DML_Nodes(nuke.allNodes("Shuffle",self.nuke_object))
		shuffles.reorder_By_X_Value()
		return shuffles
	#----------------------------------------------------------------------
	def get_Write_Nodes(self):
		""""""
		writes = DML_Nuke.dml.to_DML_Nodes(nuke.allNodes("Write",self.nuke_object))
		writes.reorder_By_X_Value()
		return writes

def _update_DML_Layers_To_Gimped_PSD_Folder_Path(node):
	if False:
		isinstance(node,DML_Layers_To_Gimped_PSD)
	folder = node.knob("dml_raw_folder_destination").getText()
	if node.metadata(key="version") != None:
		folder = os.path.join(folder, "[metadata version]").replace("\\","/")
	
	folder = os.path.join(folder, "PNGS").replace("\\","/")

	if node.knob("dml_enable_views").value():
		folder = os.path.join(folder, "%V").replace("\\","/")
	else:
		folder = os.path.join(folder, node.knob("dml_file_name").getText()).replace("\\","/")
	
	node.knob("dml_folder_destination").setText(folder)

#----------------------------------------------------------------------
def does_DML_Layers_To_Gimped_PSD_Need_Rebuild(psd_node):
	""""""
	if not isinstance(psd_node,DML_Layers_To_Gimped_PSD):
		psd_node = DML_Layers_To_Gimped_PSD(nuke_node=psd_node)
	layer_order      = psd_node.imbeded_data_layer_order
	last_build_order = psd_node._psd_build_group.last_layer_build_order
	
	if not layer_order == last_build_order and len(last_build_order):
		return True
	
	if len(psd_node.layers) != len(last_build_order):
		return True
	
	return False

#----------------------------------------------------------------------
def on_DML_Layers_To_Gimped_PSD_Knob_Changed():
	""""""
	try:
		knob = nuke.thisKnob()
		node = nuke.thisNode()
		if knob.name() in ["dml_raw_folder_destination","dml_enable_views","dml_file_name","dml_frame_padding"]:
			_update_DML_Layers_To_Gimped_PSD_Folder_Path(node)
		
		#elif knob.name() == "dml_needs_rebuild":
			#psd_node = DML_Layers_To_Gimped_PSD(nuke_node=node)
			#if knob.value():
				#psd_node.psd_build_group.knob("tile_color").setValue(16711935)
				
		elif not knob.name() in ["selected","ypos","xpos","name"]:
			if knob.name() == "DML_Layer_Order_layers":
				psd_node = DML_Layers_To_Gimped_PSD(nuke_node=node)
				psd_node.do_Error_Check()
				#has_error = does_DML_Layers_To_Gimped_PSD_Need_Rebuild(psd_node)
				#if has_error:
					#if not node.error():
						#psd_node._needs_rebuild.setValue(False)
						#psd_node.psd_build_group.knob("tile_color").setValue(4278190335L)	
				#elif node.error():
					#psd_node._needs_rebuild.setValue(True)
					#psd_node.psd_build_group.knob("tile_color").setValue(16711935)
	except:
		pass

################################################################################
class DML_Layers_To_Gimped_PSD(DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Generic_Widgets_Nodes.Layer_Order_Views_Selector_Output_Builder_Node):
	NODE_TYPE_RELATION  = "DML_Layers_To_Gimped_PSD"
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		""""""
		DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Generic_Widgets_Nodes.Layer_Order_Views_Selector_Output_Builder_Node.__init__(self,*args,**kwargs)
		self._raw_folder_destination_knob = self.knob("dml_raw_folder_destination")
		self._needs_rebuild = self.knob("dml_needs_rebuild")
		self._raw_folder_destination_knob.setVisible(False)
		self._psd_build_group = None#self._find_Psd_Build_Group()
		self._create_PSD_Group()
		
		if False:
			isinstance(self._raw_folder_destination_knob, nuke.String_Knob)
			isinstance(self._needs_rebuild, nuke.Boolean_Knob)
	#----------------------------------------------------------------------
	def do_Error_Check(self):
		""""""
		has_error = does_DML_Layers_To_Gimped_PSD_Need_Rebuild(self)
		if has_error:
			self._needs_rebuild.setValue(False)
			self.psd_build_group.knob("tile_color").setValue(4278190335L)
			try:
				wig_knob = self.knob("dml_gimped_psd_builder")
				wig_object = wig_knob.getObject()
				wig_object.channel_layers_list.rebuild_Items()
			except:
				pass
		else:
			self._needs_rebuild.setValue(True)
			self.psd_build_group.knob("tile_color").setValue(16711935)
			
	#----------------------------------------------------------------------
	def _update_Folder_Path(self):
		_update_DML_Layers_To_Gimped_PSD_Folder_Path(self.nuke_object)
	#----------------------------------------------------------------------
	def _find_Psd_Build_Group(self):
		""""""
		# get all the nodes connected to this nuke node that are of type Group
		dependent =  DML_Nuke.dml.to_DML_Nodes([n for n in self.dependent(nuke.INPUTS, forceEvaluate=True) if n.nuke_object.Class() == "Group"])
		for node in DML_Nuke.dml.to_DML_Nodes(dependent):
			if isinstance(node,DML_Gimped_PSD_Group):
				return node
		return None
	#----------------------------------------------------------------------
	@property
	def psd_build_group(self):
		""""""
		if self._psd_build_group == None:
			self._create_PSD_Group()
		return self._psd_build_group
	#----------------------------------------------------------------------
	def _create_PSD_Group(self):
		""""""
		#----------------------------------------------------------------------
		def create_group():
			this_parent = nuke.thisParent()
			if this_parent == None:
				this_parent = nuke.root()
				
			with this_parent:
				self.selectOnly()
				self.selected = False
				grp = nuke.createNode("Group","tile_color 0xff00ff name Layers_To_PSD")
				self._psd_build_group = DML_Gimped_PSD_Group(nuke_node=grp)
				self._psd_build_group.x = self.x
				self._psd_build_group.y = self.y + 100
				self._psd_build_group.setInput(0,self)
			self._psd_build_group.assign_knob_links(self._folder_path_knob, self._file_name_knob, self._frame_padding_knob, self._imbeded_data_View_Selection_knob)
			self.Initialize_build_Layers()
			self.create_Layers_To_Render()
			return self._psd_build_group
		
		# get all the nodes connected to this nuke node that are of type Group
		dependent =  [n for n in self.dependent(nuke.INPUTS, forceEvaluate=True) if n.nuke_object.Class() == "Group"]
		
		self._psd_build_group = None
		
		if not len(dependent):
			return create_group()
		else:
			for node in DML_Nuke.dml.to_DML_Nodes(dependent):
				if node.__class__.__name__ == 'DML_Gimped_PSD_Group':
					self._psd_build_group = node
					self._psd_build_group.assign_knob_links(self._folder_path_knob, self._file_name_knob, self._frame_padding_knob, self._imbeded_data_View_Selection_knob)
					return self._psd_build_group
			return create_group()
		raise LookupError("Cound Not Find PSD Build Node Connected to this node")
	#----------------------------------------------------------------------
	def create_Layers_To_Render(self):
		""""""
		layer_order = list(reversed(self.imbeded_data_layer_order))
		self.psd_build_group.create_Layers_To_Render(layer_order, xOffset=200, xSpaceing=150, yOffset=100)
		self._needs_rebuild.setValue(True)
				
	#----------------------------------------------------------------------
	def generate_Json_Data(self,frame,multi_frame=True):
		""""""
		psd_node  = self
		writeNode = self.psd_build_group.get_Write_Nodes()[0]
		res = []
		# can a list of all the nuke views
		all_view_names                = nuke.views()
		# store the options that determans if views are to be used or not
		dml_enable_views              = psd_node._enable_views_knob.value()
		# get the views that are going to be rended out
		view_selection                = psd_node.active_views
		# get the layer order that the psd builder will use when assemblying the psd file
		layer_order_names             = psd_node.imbeded_data_layer_order
		# get the frame padding
		frame_padding                 = int(psd_node._frame_padding_knob.value())
	
		# using the current frame and the padding create a padded_frame for use in file path image createion
		padded_frame  = str(frame).zfill(frame_padding)
	
		# get the folder path that this write node will render the image to
		layers_folder                 = os.path.dirname(nuke.filename(writeNode.nuke_object,nuke.REPLACE))
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
