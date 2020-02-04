
import nuke
import os

import DML_Tools

DML_PYQT = DML_Tools.DML_PYQT
DML_Nuke = DML_Tools.DML_Nuke
import Layers_To_Gimped_PSD_Nodes
import DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.View_Selection

#----------------------------------------------------------------------
def get_Folder_Dialog(label="Output Folder", UseNativeDialog=True, folder="", parent=None):
	""""""
	options = DML_PYQT.QFileDialog.Options()
	# options |= PYQT.QFileDialog.Option.
	if not UseNativeDialog:
		options |= DML_PYQT.QFileDialog.DontUseNativeDialog
	if folder == "":
		folder = nuke.script_directory()
	folder_name = DML_PYQT.QFileDialog.getExistingDirectory(parent,label,folder, options)
	if folder_name:
		return folder_name
	else:
		return False

#----------------------------------------------------------------------
def channel_Layers_To_Shuffles(start_node, layer_order=[], include_missing=True, xOffset=200, xSpaceing=150,createWrites=False, yOffset=100):
	# convert the input node into a DML Nuke Node
	start_node = DML_Nuke.dml.to_DML_Node(start_node)
	# set the node to be the only thing selected
	start_node.selectOnly()
	# get the layers for this node
	node_layers      = start_node.layers
	# Check if a layer order was given
	if len(layer_order):
		# if so using the layer order that was requested
		# collect only the layers that exist in the start nodes layers
		createion_layers = [layer for layer in layer_order if layer in node_layers]
		# check if layers that were not included in layer order should also be added
		if include_missing:
			createion_layers.extend( [layer for layer in node_layers if layer not in createion_layers] )
	# if not then just set the createion_layers to the start nodes layers
	else:
		createion_layers = node_layers

	# caculate the start pos of the shuffles
	master_xpos = start_node.x + xOffset
	master_ypos = start_node.y

	# keeps track of the last shuffle node created and used to connet the current shuffle node 
	last_created_shuffle = None

	shuffle_nodes = DML_Nuke.Nuke_Nodes.Node_List()
	write_nodes   = DML_Nuke.Nuke_Nodes.Node_List()
	# scan over each layer and create the nodes
	for index,layer in enumerate(createion_layers):
		# create the shuffle node
		shuffle_node = DML_Nuke.Nuke_Nodes.Standered_Nodes.Shuffle(**{"in":layer, "out":"rgba", "xpos":master_xpos + (xSpaceing * index), "ypos":master_ypos,"label":"[value in ]"})
		shuffle_nodes.append(shuffle_node)

		# check for a last created shuffle node
		if last_created_shuffle == None:
			# if not set the current shuffle nodes input to the input start node
			shuffle_node.setInput(0,start_node)
		else:
			# otherwise set the current shuffle nodes input to the shuffle node that was created just before this one
			shuffle_node.setInput(0,last_created_shuffle)
		# assign the current shuffle node to the last crated input for the next loop
		last_created_shuffle = shuffle_node
		# check if write nodes should be crated for the shuffles
		if createWrites:
			write_node=DML_Nuke.Nuke_Nodes.Standered_Nodes.Write(xpos=shuffle_node.x,
			                                                     ypos=shuffle_node.y + yOffset,
			                                                    colorspace="sRGB_ICC(sRGB)",
			                                                    file_type="png",
			                                                    create_directories=True,
			                                                    channels="rgba")
			if "ICC_knob" in write_node.knobs():
				write_node.knob("ICC_knob").setValue('sRGB.icc')
			# connect the write nodes input to the current shuffle node
			write_node.setInput(0,shuffle_node)
			write_nodes.append(write_node)
	if not createWrites:
		return shuffle_nodes
	else:
		return shuffle_nodes,write_nodes


########################################################################
class Nuke_To_Gimped_PSD_Builder_UI(DML_Nuke.Nuke_GUI.Python_Custom_Widget_Knob.External_UI_Base_Widget_Knob):
	_class_knob_name = "dml_gimped_psd_builder"
	_class_label_name = ""
	_class_tab_name = "Gimped PSD Builder"
	def __init__(self,node,parent=None):
		DML_Nuke.Nuke_GUI.Python_Custom_Widget_Knob.External_UI_Base_Widget_Knob.__init__(self,node,parent)
		self._nuke_node = DML_Nuke.dml.to_DML_Node(nuke.thisNode())
		self._psd_build_group = None
		isinstance(self._nuke_node,Layers_To_Gimped_PSD_Nodes.DML_Layers_To_Gimped_PSD)
		if False:
			self._nuke_node = DML_Nuke.Nuke_Nodes.Nodes.Group()
			self.channel_layers_list    = DML_Nuke.Nuke_GUI.Generic_Widgets.Layer_Order.DML_Nuke_Layer_Order_List_Widget()
			self.build_button           = DML_PYQT.QPushButton()
			self.input_folder_path      = DML_PYQT.QLineEdit()
			self.input_file_name        = DML_PYQT.QLineEdit()
			self.input_frame_padding    = DML_PYQT.QSpinBox()
			self.browse_Button          = DML_PYQT.QPushButton()
			self.enable_Views_CheckBox    = DML_PYQT.QCheckBox()
			self.Layers_Order_Widget    = DML_Nuke.Nuke_GUI.Generic_Widgets.Layer_Order.Layer_Order_UI()
			self.Nuke_Views_Selector    = DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.View_Selection.Nuke_Views_Selector_UI()
			self.tabWidget              = DML_PYQT.QTabWidget()
			self.psd_build_group        = Layers_To_Gimped_PSD_Nodes.DML_Gimped_PSD_Group()
			self.group_folder_destination_knob = nuke.String_Knob()
			
		#self._raw_folder_destination_knob = self._nuke_node._raw_folder_destination_knob #self.add_data_knob("dml_raw_folder_destination", nuke.String_Knob)
		#self._folder_destination_knob = self._nuke_node._folder_path_knob #self.add_data_knob("dml_folder_destination", nuke.File_Knob)
		#self._frame_padding_knob = self._nuke_node._frame_padding_knob
		self._file_name_knob = self._nuke_node._file_name_knob
		#self._enable_views_knob = self._nuke_node._enable_views_knob
		
		self._create_PSD_Group()
		#self._raw_folder_destination_knob.setVisible(False)
		#self._enable_views_knob.setVisible(False)
		#self._folder_destination_knob.setVisible(False)
		#self._frame_padding_knob.setVisible(False)
		self._file_name_knob.setVisible(False)
		self._rebuild()
		
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
		##----------------------------------------------------------------------
		#def create_group():
			#this_parent = nuke.thisParent()
			#with this_parent:
				#self._nuke_node.selectOnly()
				#self._nuke_node.selected = False
				#grp = nuke.createNode("Group","tile_color 0x7f0000ff name Layers_To_PSD")
				#self._psd_build_group = Layers_To_Gimped_PSD_Nodes.DML_Gimped_PSD_Group(nuke_node=grp)
				#self._psd_build_group.x = self._nuke_node.x
				#self._psd_build_group.y = self._nuke_node.y + 100
				#self._psd_build_group.setInput(0,self._nuke_node)
			#self._psd_build_group.assign_knob_links(self._folder_destination_knob, self._file_name_knob, self._frame_padding_knob, self.Nuke_Views_Selector._imbeded_data_View_Selection_knob)
			#return self._psd_build_group
		
		## get all the nodes connected to this nuke node that are of type Group
		#dependent =  [n for n in self._nuke_node.dependent(nuke.INPUTS, forceEvaluate=True) if n.nuke_object.Class() == "Group"]
		
		#self._psd_build_group = None
		
		#if not len(dependent):
			#return create_group()
		#else:
			#for node in DML_Nuke.dml.to_DML_Nodes(dependent):
				#if node.__class__.__name__ == 'DML_Gimped_PSD_Group':
					#self._psd_build_group = node
					#self._psd_build_group.assign_knob_links(self._folder_destination_knob, self._file_name_knob, self._frame_padding_knob, self.Nuke_Views_Selector._imbeded_data_View_Selection_knob)
					#return self._psd_build_group
			#return create_group()
		#raise LookupError("Cound Not Find PSD Build Node Connected to this node")
		return self._nuke_node._create_PSD_Group()
		
	#----------------------------------------------------------------------
	def _rebuild(self):
		""""""
		self.Layers_Order_Widget._rebuild()
		#self.Nuke_Views_Selector._rebuild()
		
		if self._nuke_node._raw_folder_destination_knob.value() == "":
			self._nuke_node._raw_folder_destination_knob.setValue(nuke.script_directory())
			
		if self._nuke_node._file_name_knob.value() == "":
			self._nuke_node._file_name_knob.setValue("Drew_Is_Awsome")

		self.input_folder_path.setText(self._nuke_node._raw_folder_destination_knob.value())
		
		if self._nuke_node._frame_padding_knob.value() == 0:
			self.input_frame_padding.setValue(3)
			self._nuke_node._frame_padding_knob.setValue(3)
		else:
			self.input_frame_padding.setValue(self._nuke_node._frame_padding_knob.value())

		self.input_file_name.setText(self._nuke_node._file_name_knob.value())
		
		self.enable_Views_CheckBox.setChecked(self._nuke_node._enable_views_knob.value())
		
		self.fileNameLabel.setHidden(self.enable_Views_CheckBox.isChecked())
		self.input_file_name.setHidden(self.enable_Views_CheckBox.isChecked())
		
		DML_PYQT.QMetaObject.connectSlotsByName(self)
		self._update_Folder_Path()
	#----------------------------------------------------------------------
	@DML_PYQT.Slot(bool)
	def on_enable_Views_CheckBox_clicked(self,value):
		self._nuke_node._enable_views_knob.setValue(value)
		self._update_Folder_Path()
		
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def _update_Folder_Path(self):
		folder  = self.input_folder_path.text()
		self._nuke_node._raw_folder_destination_knob.setText(folder)

		if self._nuke_node.metadata(key="version") != None:
			folder = os.path.join(folder, "[metadata version]").replace("\\","/")

		folder = os.path.join(folder, "PNGS").replace("\\","/")

		if self.enable_Views_CheckBox.isChecked():
			folder = os.path.join(folder, "%V").replace("\\","/")
		else:
			folder = os.path.join(folder, self.input_file_name.text()).replace("\\","/")

		self._nuke_node._folder_path_knob.setValue(folder)
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_input_folder_path_textChanged(self):
		self._update_Folder_Path()
	
	#----------------------------------------------------------------------
	@DML_PYQT.Slot(int)
	def on_input_frame_padding_valueChanged(self,value):
		self._nuke_node._frame_padding_knob.setValue(value)
	
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_input_file_name_textChanged(self):
		self._nuke_node._file_name_knob.setValue(self.input_file_name.text())
		self._update_Folder_Path()
	#----------------------------------------------------------------------
	def _get_ui_file(self):
		""""""
		return os.path.join(os.path.dirname(__file__),"Layers_To_Gimped_PSD.ui")
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_browse_Button_clicked(self):
		""""""
		folder = self.input_folder_path.text()
		res = get_Folder_Dialog(folder=folder)
		if res:
			self.input_folder_path.setText(res)
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_build_button_clicked(self):
		""""""
		#layer_order = list(reversed(self.Layers_Order_Widget.channel_layers_list.imbeded_data_layer_order))
		#self.psd_build_group.create_Layers_To_Render(layer_order, xOffset=200, xSpaceing=150, yOffset=100)
		self._nuke_node.create_Layers_To_Render()
