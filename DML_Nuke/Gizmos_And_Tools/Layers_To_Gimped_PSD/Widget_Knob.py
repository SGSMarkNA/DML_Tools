
import nuke
import os

import DML_Tools

DML_PYQT = DML_Tools.DML_PYQT
DML_Nuke = DML_Tools.DML_Nuke
import Layers_To_Gimped_PSD_Nodes
import Layers_To_Gimped_PSD_Utils
import DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.View_Selection
import threading


########################################################################
class Collect_Nodes_QTimer(DML_PYQT.QTimer):
	""""""
	def __init__(self,scaner,parent=None):
		"""Constructor"""
		super(Collect_Nodes_QTimer, self).__init__(parent)
		self.scaner = scaner
		self.timeout.connect(self.do_check)
		self.start(50000)
	
	#----------------------------------------------------------------------
	def do_check(self):
		""""""		
		self.scaner._nodes = Layers_To_Gimped_PSD_Utils.find_All_DML_Layers_To_Gimped_PSD()
		print "did Collection"

########################################################################
class Check_For_Errors_QTimer(DML_PYQT.QTimer):
	""""""
	def __init__(self,parent=None):
		"""Constructor"""
		super(Check_For_Errors_QTimer, self).__init__(parent)
		self._nodes = Layers_To_Gimped_PSD_Utils.find_All_DML_Layers_To_Gimped_PSD()
		self.timeout.connect(self.do_check)
		self.start(5000)

	#----------------------------------------------------------------------
	def do_check(self):
		""""""
		threading.Thread( None, self.checker,None).start()
	#----------------------------------------------------------------------
	def _do_check(self):
		""""""
		nuke.executeInMain.executeInMainThread(self.checker)
	#----------------------------------------------------------------------
	def checker(self):
		""""""
		for psd_node in self._nodes:
			psd_node.do_Error_Check()
		print "did check"
		
	
#DML_Layers_To_Gimped_PSD_Error_Check_Timmer = Check_For_Errors_QTimer()
#DML_Collect_Nodes_QTimer =  Collect_Nodes_QTimer(DML_Layers_To_Gimped_PSD_Error_Check_Timmer)

#----------------------------------------------------------------------
def get_Folder_Dialog(label="Output Folder", UseNativeDialog=False, folder="", parent=None):
	""""""
	options = DML_PYQT.QFileDialog.DontResolveSymlinks | DML_PYQT.QFileDialog.ShowDirsOnly
	if UseNativeDialog:
		options |= DML_PYQT.QFileDialog.DontUseNativeDialog
	if folder == "":
		folder = nuke.script_directory()
		
	folder = folder.replace("/", "\\")
	if not os.path.exists(folder):
		temp_path = folder
		while not os.path.exists(temp_path):
			new_path = os.path.dirname(temp_path)
			if new_path == temp_path:
				temp_path = nuke.script_directory()
				break
			else:
				temp_path = new_path
		folder = temp_path
	folder_name = DML_PYQT.QFileDialog.getExistingDirectory(parent,label,folder, options)
	if folder_name:
		return folder_name.replace("\\","/")
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
		
		#self._create_PSD_Group()
		#self._rebuild()
		
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
		return self._nuke_node._create_PSD_Group()
		
	#----------------------------------------------------------------------
	def _rebuild(self):
		""""""
		self._create_PSD_Group()
		self.Layers_Order_Widget._rebuild()
		self.input_folder_path.setText(self._nuke_node._raw_folder_destination_knob.getText())
		self.input_frame_padding.setValue(self._nuke_node._frame_padding_knob.value())
		self.input_file_name.setText(self._nuke_node._file_name_knob.getText())
		DML_PYQT.QMetaObject.connectSlotsByName(self)
		#self._update_Folder_Path()
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def _update_Folder_Path(self):
		folder  = self.input_folder_path.text()
		if folder != self._nuke_node._raw_folder_destination_knob.getText():
			self._nuke_node._raw_folder_destination_knob.setText(folder)
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_input_folder_path_textChanged(self):
		self._nuke_node._raw_folder_destination_knob.setText(self.input_folder_path.text())
	
	#----------------------------------------------------------------------
	@DML_PYQT.Slot(int)
	def on_input_frame_padding_valueChanged(self,value):
		self._nuke_node._frame_padding_knob.setValue(value)
	
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_input_file_name_textChanged(self):
		self._nuke_node._file_name_knob.setValue(self.input_file_name.text())
	#----------------------------------------------------------------------
	def _get_ui_file(self):
		""""""
		return os.path.join(os.path.dirname(__file__),"Layers_To_Gimped_PSD.ui")
	##----------------------------------------------------------------------
	#@DML_PYQT.Slot()
	#def on_browse_Button_clicked(self):
		#""""""
		#folder = self.input_folder_path.text()
		#res = get_Folder_Dialog(folder=folder)
		#if res:
			#self.input_folder_path.setText(res)
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_browse_Button_clicked(self):
		""""""
		folder = self._nuke_node._raw_folder_destination_knob.value()
		folder = folder.replace("%V", nuke.thisView())
		if folder == None or folder == "":
			folder = nuke.script_directory()			
		res = get_Folder_Dialog(folder=folder)
		if res:
			self.input_folder_path.setText(res)
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_build_button_clicked(self):
		""""""
		self.channel_layers_list._update_Imbeded_Data_Layer_Order()
		self._nuke_node.create_Layers_To_Render()
		self._nuke_node.do_Error_Check()
	#----------------------------------------------------------------------
	def showEvent(self,event):
		""""""
		super(Nuke_To_Gimped_PSD_Builder_UI, self).showEvent(event)
		self._rebuild()
		self._nuke_node.do_Error_Check()