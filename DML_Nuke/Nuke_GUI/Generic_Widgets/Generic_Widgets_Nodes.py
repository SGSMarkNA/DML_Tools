import nuke
import DML_Tools
DML_Nuke = DML_Tools.DML_Nuke


########################################################################
class Output_Path_Builder_Node(DML_Nuke.Nuke_Nodes.Standered_Nodes.Gizmo):
	NODE_TYPE_RELATION  = None
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		""""""
		self._folder_path_knob   = self.knob("dml_folder_destination")
		self._frame_padding_knob = self.knob("dml_frame_padding")
		self._file_name_knob     = self.knob("dml_file_name") 
		self._enable_views_knob  = self.knob("dml_enable_views")
		
		self._folder_path_knob.setVisible(False)
		self._frame_padding_knob.setVisible(False)
		self._file_name_knob.setVisible(False)
		self._enable_views_knob.setVisible(False)
		if False:
			isinstance(self._folder_path_knob,nuke.String_Knob)
			isinstance(self._frame_padding_knob,nuke.Int_Knob)
			isinstance(self._file_name_knob ,nuke.String_Knob)
			isinstance(self._enable_views_knob,nuke.Boolean_Knob)
	

################################################################################
class Layer_Order_Node(DML_Nuke.Nuke_Nodes.Standered_Nodes.Gizmo):
	NODE_TYPE_RELATION  = None
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		""""""
		self._imbeded_data_layer_Order_knob = self.knob("DML_Layer_Order_layers")
		self._imbeded_data_layer_Icons_knob = self.knob("DML_Layer_Order_Layer_Icons")
		self._imbeded_data_layer_Icons_knob.setVisible(False)
		self._imbeded_data_layer_Icons_knob.setVisible(False)
		if False:
			isinstance(self._imbeded_data_layer_Order_knob , nuke.String_Knob)
			isinstance(self._imbeded_data_layer_Icons_knob , nuke.String_Knob)
		self.Initialize_build_Layers()
	#----------------------------------------------------------------------
	def Initialize_build_Layers(self):
		""""""
		# get the imbeded layer order data
		layers = self.imbeded_data_layer_order
		# get the imbeded layer icon data
		icons  = self.imbeded_data_layer_icons
		# check if both imbeded data items are empty
		if len(layers) == 0:
			# if so set it to a master layer order and check if it was set
			check = self.set_Layer_Data_From_Master_Layer_Order()
			# if so reaquire the imbeded information
			if not check:
				self.imbeded_data_layer_order = self.layers
	#----------------------------------------------------------------------
	def get_Imbeded_Data_Layer_Icons(self):
		""""""
		try:
			return eval(self._imbeded_data_layer_Icons_knob.getText())
		except:
			return {}
	#----------------------------------------------------------------------
	def set_Imbeded_Data_Layer_Icons(self,data):
		""""""
		self._imbeded_data_layer_Icons_knob.setText(repr(data))
	#----------------------------------------------------------------------
	imbeded_data_layer_icons = property(get_Imbeded_Data_Layer_Icons,set_Imbeded_Data_Layer_Icons)
	#----------------------------------------------------------------------
	def get_Imbeded_Data_Layer_Order(self):
		""""""
		try:
			return eval(self._imbeded_data_layer_Order_knob.getText())
		except:
			return []
	#----------------------------------------------------------------------
	def set_Imbeded_Data_Layer_Order(self,data):
		""""""
		self._imbeded_data_layer_Order_knob.setText(repr(data))
	#----------------------------------------------------------------------
	imbeded_data_layer_order = property(get_Imbeded_Data_Layer_Order,set_Imbeded_Data_Layer_Order)
	#----------------------------------------------------------------------
	def set_Layer_Data_From_Master_Layer_Order(self):
		""""""
		match = self.find_Upstream_Node("DML_Master_Layer_Order")
		if match is not None:
			if not match.name == self.name:
				knob = match.knob("dml_master_layer_order")
				if not knob == None:
					layer_order_knob = match.knob("DML_Layer_Order_layers")
					layer_icons_knob = match.knob("DML_Layer_Order_Layer_Icons")
					if layer_order_knob != None and layer_icons_knob != None:
						layers = eval(layer_order_knob.getText())
						icons  = eval(layer_icons_knob.getText())
						
						nuke_node_layers = self.layers
						nuke_node_icons  = self.imbeded_data_layer_icons
						
						for icon in nuke_node_icons:
							if not icon in icons:
								icons[icon] = nuke_node_icons[icon]
								
						for layer in nuke_node_layers:
							if not layer in layers:
								layers.insert(0, layer)
								
						for layer in layers:
							if not layer in nuke_node_layers:
								layers.remove(layer)
						
						self.imbeded_data_layer_order = layers
						self.imbeded_data_layer_icons = icons
						return True
		return False
	
########################################################################
class Views_Selector_Node(DML_Nuke.Nuke_Nodes.Standered_Nodes.Gizmo):
	NODE_TYPE_RELATION  = None
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		""""""
		self._imbeded_data_View_Selection_knob = self.knob("DML_Nuke_View_Selection")
		
		if False:
			isinstance(self._imbeded_data_View_Selection_knob, nuke.MultiView_Knob)
	#----------------------------------------------------------------------
	@property
	def nuke_views(self):
		""""""
		return nuke.DML_Nuke_View_System.views

	#----------------------------------------------------------------------
	def get_Active_Views(self,active_views=[]):
		""""""
		return self._imbeded_data_View_Selection_knob.value().split()
	#----------------------------------------------------------------------
	def set_Active_Views(self,active_views=[]):
		""""""
		if not len(active_views):
			self._imbeded_data_View_Selection_knob.setValue(" ")
		else:
			self._imbeded_data_View_Selection_knob.setValue(" ".join(active_views))
			
	active_views = property(get_Active_Views,set_Active_Views)
	
########################################################################
class Layer_Order_Views_Selector_Node(Layer_Order_Node,Views_Selector_Node):
	NODE_TYPE_RELATION  = None
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		""""""
		Layer_Order_Node.__init__(self,*args,**kwargs)
		Views_Selector_Node.__init__(self,*args,**kwargs)
		
########################################################################
class Layer_Order_Output_Builder_Node(Layer_Order_Node,Output_Path_Builder_Node):
	NODE_TYPE_RELATION  = None
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		""""""
		Layer_Order_Node.__init__(self,*args,**kwargs)
		Output_Path_Builder_Node.__init__(self,*args,**kwargs)
		
########################################################################
class Layer_Order_Views_Selector_Output_Builder_Node(Layer_Order_Node,Views_Selector_Node,Output_Path_Builder_Node):
	NODE_TYPE_RELATION  = None
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		""""""
		Layer_Order_Node.__init__(self,*args,**kwargs)
		Views_Selector_Node.__init__(self,*args,**kwargs)
		Output_Path_Builder_Node.__init__(self,*args,**kwargs)