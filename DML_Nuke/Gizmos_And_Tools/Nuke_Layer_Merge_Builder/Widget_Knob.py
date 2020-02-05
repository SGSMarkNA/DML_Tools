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
		
		self.build_button.clicked.connect(self.build_Layer_Merge_Output)
		self.imbeded_data_knob.setVisible(False)
		self._nuke_node = Nuke_Layer_Merge_Builder_Nodes.DML_Layer_Order_Builder(nuke_node=self._nuke_node.nuke_object)
		self._rebuild()
	#----------------------------------------------------------------------
	def _rebuild(self):
		""""""
		self.Layers_Order_Widget._rebuild()
		
		if self._nuke_node._folder_path_knob.value() == "":
			self._nuke_node._folder_path_knob.setValue(nuke.script_directory())
		if self._nuke_node._file_name_knob.value() == "":
			self._nuke_node._file_name_knob.setValue("Drew_Is_Awsome")
			
		#self.input_folder_path.setText(self._nuke_node._folder_path_knob.value())
		#if self._nuke_node._frame_padding_knob.value() == 0:
			#self.input_frame_padding.setValue(3)
			#self._nuke_node._frame_padding_knob.setValue(3)
		#else:
			#self.input_frame_padding.setValue(self._nuke_node._frame_padding_knob.value())
		
		self.input_folder_path.setText(self._nuke_node._folder_path_knob.getText())	
		self.input_frame_padding.setValue(self._nuke_node._frame_padding_knob.value())
		self.input_file_name.setText(self._nuke_node._file_name_knob.getText())
		self.enableViewsCheckBox.setChecked(self._nuke_node._enable_views_knob.value())
		
		self.input_file_name.textChanged.connect(self.on_input_file_name_textChanged)
		self.input_folder_path.textChanged.connect(self.on_input_folder_path_textChanged)
		self.input_frame_padding.valueChanged.connect(self.on_input_frame_padding_changed)
		self.input_channels.currentIndexChanged.connect(self.on_input_channels_currentIndexChanged)
		self.fileTypeComboBox.currentIndexChanged.connect(self.on_fileTypeComboBox_currentIndexChanged)
		self.browse_Button.clicked.connect(self.on_Browse_Button_Clicked)
		self.enableViewsCheckBox.clicked.connect(self.on_enable_views_valueChanged)
		
		if self._nuke_node.write_node != None:
			self.input_channels.setCurrentIndex(["rgb","rgba"].index(self._nuke_node.write_node.knob("channels").value()))
			try:
				self.fileTypeComboBox.setCurrentIndex(["png","jpeg","tiff"].index(self._nuke_node.write_node.knob("file_type").value()))
			except ValueError:
				self.fileTypeComboBox.setCurrentIndex(0)
	
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_enable_views_valueChanged(self):
		self._nuke_node._enable_views_knob.setValue(self.enableViewsCheckBox.isChecked())
		self._nuke_node._update_Write_Node_File_Path()
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_input_folder_path_textChanged(self):
		self._nuke_node._folder_path_knob.setText(self.input_folder_path.text())

	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_fileTypeComboBox_currentIndexChanged(self):
		if self._nuke_node.write_node != None:
			self._nuke_node.write_node.knob("file_type").setValue(str(self.fileTypeComboBox.currentText()))
			self._nuke_node._update_Write_Node_File_Path()
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_input_channels_currentIndexChanged(self):
		if self._nuke_node.write_node != None:
			self._nuke_node.write_node.knob("channels").setValue(self.input_channels.currentText())
	#----------------------------------------------------------------------
	@DML_PYQT.Slot(int)
	def on_input_frame_padding_changed(self,value):
		self._nuke_node._frame_padding_knob.setValue(value)
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_input_file_name_textChanged(self):
		self._nuke_node._file_name_knob.setText(self.input_file_name.text())
		
	#----------------------------------------------------------------------
	def _get_ui_file(self):
		""""""
		return os.path.join(os.path.dirname(__file__),"Nuke_Layer_Merge_Builder.ui")
	#----------------------------------------------------------------------
	def on_Browse_Button_Clicked(self):
		""""""
		if self._nuke_node._folder_path_knob.value() == None:
			folder = nuke.script_directory()
		else:
			folder = self._nuke_node._folder_path_knob.value()
			
		res = get_Folder_Dialog(folder=folder)
		if res:
			self.input_folder_path.setText(res)
			self._nuke_node._update_Write_Node_File_Path()
	#----------------------------------------------------------------------
	def build_Layer_Merge_Output(self):
		""""""
		self._nuke_node.create_Client_Approval_Setup()
		if self.active_view_checkBox.isChecked():
			self._nuke_node.write_node.dependent()[0].view_In_Active_Viewer()