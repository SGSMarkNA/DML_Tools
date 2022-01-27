
import os
import nuke
import DML_Tools
DML_PYQT = DML_Tools.DML_PYQT
from DML_Tools.DML_Nuke.Nuke_GUI import Python_Custom_Widget_Knob
from . import Master_Layer_Order_Nodes

	
########################################################################
class Master_Layer_Order_Widget_Knob(Python_Custom_Widget_Knob.External_UI_Base_Widget_Knob):
	_class_knob_name = "dml_master_layer_order"
	_class_label_name = ""
	_class_tab_name = "Master Layer Order"
	def __init__(self,node,parent=None):
		Python_Custom_Widget_Knob.External_UI_Base_Widget_Knob.__init__(self,node,parent)
		if False:
			from DML_Tools.DML_Nuke.Nuke_GUI import Generic_Widgets
			self.channel_layers_list    = Generic_Widgets.Layer_Order.DML_Nuke_Layer_Order_List_Widget()
			self.move_layer_up_button   = DML_PYQT.QPushButton()
			self.move_layer_down_button = DML_PYQT.QPushButton()
			self.build_button           = DML_PYQT.QPushButton()
			self.Layers_Order_Widget    = Generic_Widgets.Layer_Order.Layer_Order_UI()
		self._rebuild()
	#----------------------------------------------------------------------
	def _rebuild(self):
		""""""
		self.Layers_Order_Widget._rebuild()
		#self.Layers_Order_Widget.channel_layers_list._update_Imbeded_Data_Layer_Order()
	#----------------------------------------------------------------------
	def _get_ui_file(self):
		""""""
		return os.path.join(os.path.dirname(__file__),"Master_Layer_Order.ui")