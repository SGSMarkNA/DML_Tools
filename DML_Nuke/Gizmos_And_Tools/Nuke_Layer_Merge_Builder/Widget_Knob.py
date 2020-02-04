import os
import nuke
import nuke
import DML_Tools
import Nuke_Layer_Merge_Builder_Nodes
DML_PYQT = DML_Tools.DML_PYQT
DML_Nuke = DML_Tools.DML_Nuke


#----------------------------------------------------------------------
def get_Folder_Dialog(label="Output Folder", UseNativeDialog=False, folder="", parent=None):
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

def create_Client_Approval_Setup(start_node, layer_order=[], file_path_value=""):
	res = None
	with nuke.Undo():
		try:
			# convert the input node into a DML Nuke Node
			start_node = DML_Nuke.Decorators.Node_Wraper_Manager.to_DML_Node(start_node)
			# set the node to be the only thing selected
			start_node.selectOnly()
			# get the layers for this node
			node_layers      = start_node.layers
			# Check if a layer order was given
			# if so collect only the layers that exist in the input nodes layers
			# using the layer order that was requested
			# if not then just set the node layers to the createion_layers
			createion_layers = [layer for layer in layer_order if layer in node_layers] if len(layer_order) else node_layers
			
			# get the name of the backdrop node that will be created
			backdrop_name = start_node.name + "_Client_Approval_BKDRP"
			
			# get the write node name that will be created
			write_node_name = start_node.name+"_Client_Approval_Write"
			
			master_xpos = start_node.x + 200
			master_ypos = start_node.y
			
			# Check If The backdrop node exists if so then delete it along with all the nodes in it
			if nuke.exists(backdrop_name):
				bd=DML_Nuke.Nuke_Nodes.Standered_Nodes.BackdropNode(backdrop_name)
				if bd.nuke_object.Class()=="BackdropNode":
					bd.delete(includeContents=True)
			
			shuffle_nodes = DML_Nuke.Nuke_Nodes.Node_List()
			# this will collect all the node that the backdrow will be created around 
			nodes_for_backdrop_createion = DML_Nuke.Nuke_Nodes.Node_List()
			
			last_created_shuffle = None
			last_created_merge   = None
			
			# scan over each layer and create the nodes
			for index,layer in enumerate(createion_layers):
				# create the shuffle node
				shuffle_node = DML_Nuke.Nuke_Nodes.Standered_Nodes.Shuffle(**{"in":layer, "out":"rgba", "xpos":master_xpos + (150 * index), "ypos":master_ypos,"label":"[value in ]"})
				nodes_for_backdrop_createion.append(shuffle_node)
				
				if index == 0 :
					shuffle_node.setInput(0,start_node)
				else:
					shuffle_node.setInput(0,last_created_shuffle)
					merge_node = DML_Nuke.dml.to_DML_Node( nuke.nodes.PSDMerge(xpos=master_xpos, ypos=master_ypos + (100 * index),label="[value input1.in]") )
					
					if index == 1 :
						merge_node.setInput(1,shuffle_node)
						merge_node.setInput(0,last_created_shuffle)
					else:
						merge_node.setInput(1,shuffle_node)
						merge_node.setInput(0,last_created_merge)
						
					last_created_merge = merge_node
					nodes_for_backdrop_createion.append(merge_node)
				
				shuffle_nodes.append(shuffle_node)
				last_created_shuffle = shuffle_node
		
	
			w=DML_Nuke.Nuke_Nodes.Standered_Nodes.Write(xpos=master_xpos,
														ypos=master_ypos + ( 100 * len(shuffle_nodes)),
														name=start_node.name+"_Client_Approval_Write",
														file=file_path_value,
														colorspace="sRGB",
														file_type="png",
														create_directories=True,
														channels="rgb")
			w.setInput(0,last_created_merge)
			nodes_for_backdrop_createion.append(w)
			w.selectOnly()
			text_node = DML_Nuke.dml.to_DML_Node(nuke.createNode("Text",'message "[value [value input.name].file]" xjustify left yjustify baseline size 20 box "0 0 0 0" translate "10 50" Transform 1',False))
			text_node.y = text_node.y + 50
			nodes_for_backdrop_createion.append(text_node)
			DML_Nuke.Nuke_Nodes.Standered_Nodes.BackdropNode(name=backdrop_name,
															 label="PNG Sequence out to Client Approval",
															 note_font_size=25,
															 note_font_color=255,
															 note_font='Verdana Bold',
															 post_kwargs=dict(nodes=nodes_for_backdrop_createion))
			res = w
		except:
			nuke.message("Something went wrong")
	return res
########################################################################
class Layer_Merge_Builder_Widget_Knob(DML_Nuke.Nuke_GUI.Python_Custom_Widget_Knob.External_UI_Base_Widget_Knob):
	_class_knob_name = "dml_layer_merge_build"
	_class_label_name = ""
	_class_tab_name = "Layer Merge Builder"
	def __init__(self,node,parent=None):
		DML_Nuke.Nuke_GUI.Python_Custom_Widget_Knob.External_UI_Base_Widget_Knob.__init__(self,node,parent)
		if False:
			self.channel_layers_list    = DML_Nuke.Nuke_GUI.Generic_Widgets.Layer_Order.DML_Nuke_Layer_Order_List_Widget()
			self.move_layer_up_button   = DML_PYQT.QPushButton()
			self.move_layer_down_button = DML_PYQT.QPushButton()
			self.build_button           = DML_PYQT.QPushButton()
			self.active_view_checkBox   = DML_PYQT.QCheckBox()
			self.input_folder_path      = DML_PYQT.QLineEdit()
			self.input_file_name        = DML_PYQT.QLineEdit()
			self.input_frame_padding    = DML_PYQT.QSpinBox()
			self.browse_Button          = DML_PYQT.QPushButton()
			self.input_channels         = DML_PYQT.QComboBox()
			self.fileTypeComboBox       = DML_PYQT.QComboBox()
			self.enableViewsCheckBox    = DML_PYQT.QCheckBox()
			self.Layers_Order_Widget    = DML_Nuke.Nuke_GUI.Generic_Widgets.Layer_Order.Layer_Order_UI()
			
		#self.Layers_Order_Widget.imbeded_data_knob = self.imbeded_data_knob
		#self.Layers_Order_Widget._set_nuke_node(self._nuke_node)
		self.build_button.clicked.connect(self.build_Layer_Merge_Output)
		
		self._folder_path_knob = self._nuke_node._folder_path_knob #self.add_data_knob("dml_folder_destination", nuke.String_Knob)
		self._frame_padding_knob = self._nuke_node._frame_padding_knob #self.add_data_knob("dml_frame_padding", nuke.Int_Knob)
		self._file_name_knob = self._nuke_node._file_name_knob #self.add_data_knob("dml_file_name", nuke.String_Knob)
		self._enable_views_knob = self._nuke_node._enable_views_knob #self.add_data_knob("dml_enable_views", nuke.Boolean_Knob)
		
		self._enable_views_knob.setVisible(False)
		self._folder_path_knob.setVisible(False)
		self._frame_padding_knob.setVisible(False)
		self._file_name_knob.setVisible(False)
		self.imbeded_data_knob.setVisible(False)
		self._rebuild()
	
	#----------------------------------------------------------------------
	def _rebuild(self):
		""""""
		self.Layers_Order_Widget._rebuild()
		if self._folder_path_knob.value() == "":
			self._folder_path_knob.setValue(nuke.script_directory())
		if self._file_name_knob.value() == "":
			self._file_name_knob.setValue("Drew_Is_Awsome")
			
		self.input_folder_path.setText(self._folder_path_knob.value())
		if self._frame_padding_knob.value() == 0:
			self.input_frame_padding.setValue(3)
			self._frame_padding_knob.setValue(3)
		else:
			self.input_frame_padding.setValue(self._frame_padding_knob.value())
			
		self.input_file_name.setText(self._file_name_knob.value())
		
		self.enableViewsCheckBox.setChecked(self._enable_views_knob.value())
		
		self.input_file_name.textChanged.connect(self.on_input_file_name_textChanged)
		self.input_folder_path.textChanged.connect(self.on_input_folder_path_textChanged)
		self.input_frame_padding.valueChanged.connect(self.on_input_frame_padding_changed)
		self.input_channels.currentIndexChanged.connect(self.on_input_channels_currentIndexChanged)
		self.fileTypeComboBox.currentIndexChanged.connect(self.on_fileTypeComboBox_currentIndexChanged)
		self.browse_Button.clicked.connect(self.on_Browse_Button_Clicked)
		self.enableViewsCheckBox.clicked.connect(self.on_enable_views_valueChanged)
		write_node_name = self._nuke_node.name+"_Client_Approval_Write"
		self._nuke_write_node = None
		if nuke.exists(write_node_name):
			self._nuke_write_node = DML_Nuke.dml.to_DML_Node(nuke.toNode(write_node_name))
			self.input_channels.setCurrentIndex(["rgb","rgba"].index(self._nuke_write_node.knob("channels").value()))
			try:
				self.fileTypeComboBox.setCurrentIndex(["png","jpeg","tiff"].index(self._nuke_write_node.knob("file_type").value()))
			except ValueError:
				self.fileTypeComboBox.setCurrentIndex(0)
	 
	def _update_Write_Node_File_Path(self):
		if not self._nuke_write_node == None:
			folder  = "[value {}.dml_folder_destination]".format(self._nuke_node.name)
			name    = "[value {}.dml_file_name]".format(self._nuke_node.name)
			padding = "%0[value {}.dml_frame_padding]".format(self._nuke_node.name)
			version = "[metadata version]/" if self._nuke_write_node.metadata(key="version") != None  else ""
			views   = "%V/" if self.enableViewsCheckBox.isChecked() else ""
			file_type = self._nuke_write_node.knob("file_type").value()
			value = '{}/{}{}{}_{}d.{}'.format(folder,version,views,name,padding,file_type)
			self._nuke_write_node.knob("file").setValue(value)
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_enable_views_valueChanged(self):
		self._enable_views_knob.setValue(self.enableViewsCheckBox.isChecked())
		self._update_Write_Node_File_Path()
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_input_folder_path_textChanged(self):
		#self._update_Write_Node_File_Path()
		self._folder_path_knob.setValue(self.input_folder_path.text())

	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_fileTypeComboBox_currentIndexChanged(self):
		if self._nuke_write_node != None:
			self._nuke_write_node.knob("file_type").setValue(str(self.fileTypeComboBox.currentText()))
		self._update_Write_Node_File_Path()
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_input_channels_currentIndexChanged(self):
		if self._nuke_write_node != None:
			self._nuke_write_node.knob("channels").setValue(self.input_channels.currentText())
	#----------------------------------------------------------------------
	@DML_PYQT.Slot(int)
	def on_input_frame_padding_changed(self,value):
		#self._update_Write_Node_File_Path()
		self._frame_padding_knob.setValue(value)
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_input_file_name_textChanged(self):
		#self._update_Write_Node_File_Path()
		self._file_name_knob.setValue(self.input_file_name.text())
		
	#----------------------------------------------------------------------
	def _get_ui_file(self):
		""""""
		return os.path.join(os.path.dirname(__file__),"Nuke_Layer_Merge_Builder.ui")
	#----------------------------------------------------------------------
	def on_Browse_Button_Clicked(self):
		""""""
		if self._folder_path_knob.value() == None:
			folder = nuke.script_directory()
		else:
			folder = self._folder_path_knob.value()
			
		res = get_Folder_Dialog(folder=folder)
		if res:
			self.input_folder_path.setText(res)
			self._update_Write_Node_File_Path()
	#----------------------------------------------------------------------
	def build_Layer_Merge_Output(self):
		""""""
		layer_order = list(reversed(self.Layers_Order_Widget.channel_layers_list.imbeded_data_layer_order))
		self._nuke_write_node = create_Client_Approval_Setup(self._nuke_node,layer_order=layer_order)
		if self.active_view_checkBox.isChecked():
			self._nuke_write_node.dependent()[0].view_In_Active_Viewer()
		self._update_Write_Node_File_Path()