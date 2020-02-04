import nuke
import DML_Tools
import DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Generic_Widgets_Nodes
DML_Nuke = DML_Tools.DML_Nuke

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
				write_node.knob("file").setValue("[value parent.dml_folder_destination]/Layers_Frames/%0[value parent.dml_frame_padding]d/[value input0.in].png")
				write_node.knob("views").setValue('{{parent.dml_output_views}}')
				write_node.knob("disable").setExpression('parent.disable')
				if "ICC_knob" in write_node.knobs():
					write_node.knob("ICC_knob").setValue('sRGB.icc')
				write_nodes.append(write_node)
		self._shuffle_nodes = shuffle_nodes
		self._write_nodes   = write_nodes
		return shuffle_nodes,write_nodes
	
	
################################################################################
class DML_Layers_To_Gimped_PSD(DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Generic_Widgets_Nodes.Layer_Order_Views_Selector_Output_Builder_Node):
	NODE_TYPE_RELATION  = "DML_Layers_To_Gimped_PSD"
	
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		""""""
		DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Generic_Widgets_Nodes.Layer_Order_Views_Selector_Output_Builder_Node.__init__(self,*args,**kwargs)
		self._raw_folder_destination_knob = self.knob("dml_raw_folder_destination")
		#self._folder_destination_knob = self.knob("dml_folder_destination")
		#self._frame_padding_knob = self.knob("dml_frame_padding", nuke.Int_Knob)
		#self._file_name_knob = self.knob("dml_file_name", nuke.String_Knob)
		#self._enable_views_knob = self.knob("dml_enable_views", nuke.Boolean_Knob)
		#self._imbeded_data_layer_Order_knob = self.knob("DML_Layer_Order_layers","layer Order")
		#self._imbeded_data_layer_Icons_knob = self.knob("DML_Layer_Order_Layer_Icons")
		if False:
			isinstance(self._raw_folder_destination_knob, nuke.String_Knob)
			#isinstance(self._folder_destination_knob, nuke.File_Knob)
			#isinstance(self._frame_padding_knob, nuke.Int_Knob)
			#isinstance(self._file_name_knob , nuke.String_Knob)
			#isinstance(self._enable_views_knob, nuke.Boolean_Knob)
			#isinstance(self._imbeded_data_layer_Order_knob , nuke.String_Knob)
			#isinstance(self._imbeded_data_layer_Icons_knob , nuke.String_Knob)
		self.Initialize_build_Layers()

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
				grp = nuke.createNode("Group","tile_color 0x7f0000ff name Layers_To_PSD")
				self._psd_build_group = DML_Gimped_PSD_Group(nuke_node=grp)
				self._psd_build_group.x = self.x
				self._psd_build_group.y = self.y + 100
				self._psd_build_group.setInput(0,self)
			self._psd_build_group.assign_knob_links(self._folder_path_knob, self._file_name_knob, self._frame_padding_knob, self._imbeded_data_View_Selection_knob)
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