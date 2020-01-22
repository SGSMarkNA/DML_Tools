import os
import nuke
import nuke
import DML_Tools
DML_PYQT = DML_Tools.DML_PYQT
DML_Nuke = DML_Tools.DML_Nuke
import View_Selection
import Utils
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
class Output_Path_Builder_Widget_UI(DML_PYQT.QWidget):
	def __init__(self,parent=None):
		DML_PYQT.QWidget.__init__(self,parent=parent)
		self._nuke_node = nuke.thisNode()
		if False:
			self.input_folder_path      = DML_PYQT.QLineEdit()
			self.input_file_name        = DML_PYQT.QLineEdit()
			self.input_frame_padding    = DML_PYQT.QSpinBox()
			self.browse_Button          = DML_PYQT.QPushButton()
			self.channel_input         = DML_PYQT.QComboBox()
			self.fileTypeComboBox       = DML_PYQT.QComboBox()
			self.enableViewsCheckBox    = DML_PYQT.QCheckBox()
			self.Nuke_Views_Selector    = View_Selection.Nuke_Views_Selector_UI()

		#self.Layers_Order_Widget.imbeded_data_knob = self.imbeded_data_knob
		#self.Layers_Order_Widget._set_nuke_node(self._nuke_node)
		self.build_button.clicked.connect(self.build_Layer_Merge_Output)

		self._folder_path_knob = Utils.add_data_knob(self._nuke_node, "dml_folder_path", nuke.String_Knob, visable=False, defalutValue=nuke.script_directory())
		self._frame_padding_knob = Utils.add_data_knob(self._nuke_node, "dml_frame_padding", nuke.Int_Knob, visable=False, defalutValue=3)
		self._file_name_knob = Utils.add_data_knob(self._nuke_node, "dml_file_name", nuke.String_Knob, visable=False, defalutValue="Drew_Is_Awsome") 
		self._enable_views_knob = Utils.add_data_knob(self._nuke_node, "dml_enable_views", nuke.Boolean_Knob, visable=False, defalutValue=False)
		self._enable_views_knob = Utils.add_data_knob(self._nuke_node, "dml_enable_views", nuke.Boolean_Knob, visable=False, defalutValue=False)
		self._channel_input_knob = Utils.add_data_knob(self._nuke_node, "dml_enable_views", nuke.Boolean_Knob, visable=False, defalutValue=False)
		self._file_type_knob
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
			folder  = "[value {}.dml_folder_path]".format(self._nuke_node.name)
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