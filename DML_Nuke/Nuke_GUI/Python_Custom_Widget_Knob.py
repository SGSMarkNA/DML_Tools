import nuke
import os
import DML_Tools
from DML_Tools import DML_General_Utilities
DML_PYQT = DML_Tools.DML_PYQT
from .. import dml
from .Utils import remove_Tab

########################################################################
class Registered_Knob_Widgets(dict):
	""""""
	__metaclass__ = DML_General_Utilities.Generic_Classes.Singleton


registered_knob_widgets = Registered_Knob_Widgets()

Default_Ui_Loader = DML_PYQT.QT.QUiLoader()


def load_Widget_command(clsName,modual):
	if not clsName in registered_knob_widgets.keys():		
		if modual not in os.sys.modules.keys():
			nuke.executeInMainThread(__import__,modual)
		modual = os.sys.modules[modual]
		registered_knob_widgets[clsName] = getattr(modual,clsName)
	
	cls = registered_knob_widgets[clsName]
	return cls(  nuke.thisNode()  )

def add_Widget_Knob(clsName, modual, node, name, label='',tab="Widget"):
	
	cmd = __name__+'.load_Widget_command("{}","{}")'.format(clsName,modual)
	
	if tab in node.knobs().keys():
		remove_Tab(node,tab)
	tab_knb = nuke.Tab_Knob(tab)
	node.addKnob(tab_knb)
	knb = nuke.PyCustom_Knob(name, "", cmd)
	knb.setLabel(label)
	node.addKnob(knb)
	return knb

########################################################################
class _CallBack_Singles(DML_PYQT.QObject):
	"""A Signal That Is A emited whatever a knob has changed on any node that has a Python Widget Knob Attached To It"""
	Knob_Changed_Signal = DML_PYQT.Signal(object,object)

CallBack_Singles = _CallBack_Singles()
#----------------------------------------------------------------------
def _on_nuke_node_knob_changed():
	""""""
	knb = nuke.thisKnob()
	nod = nuke.thisNode()
	CallBack_Singles.Knob_Changed_Signal.emit(nod,knb)


########################################################################
class Python_Widget_Knob(DML_PYQT.QWidget):
	Knob_Changed_Signal = DML_PYQT.Signal(object,object)
	Knob_Changed = DML_PYQT.Signal(nuke.Knob)
	_class_knob_name = "dml_default_widget_knob"
	_class_label_name = ""
	_class_tab_name  = "Widget"
	
	def __init__(self, node, parent=None):
		DML_PYQT.QWidget.__init__(self, parent)
		self._nuke_node = dml.to_DML_Node(node)
		if __name__ == '__main__':
			cmd = "_on_nuke_node_knob_changed()"
		else:
			cmd = __name__+"._on_nuke_node_knob_changed()"
		#self._nuke_node.nuke_object.knob('knobChanged').setValue(cmd)
		#CallBack_Singles.Knob_Changed_Signal.connect(self._on_knob_changed)
		#self.Knob_Changed.connect(self.on_knob_changed)
	#----------------------------------------------------------------------
	def _rebuild(self):
		""""""
		
	#----------------------------------------------------------------------
	@classmethod
	def add_Widget_Knob(cls, node):
		knb  = add_Widget_Knob(cls.__name__, cls.__module__, node, cls._class_knob_name, label=cls._class_label_name, tab=cls._class_tab_name)
		return knb
	#----------------------------------------------------------------------
	def _on_knob_changed(self,nod,knb):
		""""""
		knb = nuke.thisKnob()
		nod = nuke.thisNode()
		if nod == self._nuke_node.nuke_object:
			self.Knob_Changed.emit(knb)
	#----------------------------------------------------------------------
	def on_knob_changed(self,knb):
		""""""
		pass
	#----------------------------------------------------------------------
	def makeUI(self):
		return self
	#----------------------------------------------------------------------
	def updateValue(self):
		return None
	
	#----------------------------------------------------------------------
	def _get_imbeded_data(self):
		""""""
		try:
			return eval(self.imbeded_data_knob.getText())
		except:
			return ""
	#----------------------------------------------------------------------
	def _set_imbeded_data(self,data):
		""""""
		self.imbeded_data_knob.setText(repr(data))
	#----------------------------------------------------------------------
	def _add_imbeded_data_knob(self):
		""""""
		name = "DML_EMBEDED_WIDGET_DATA"
		if not name in self._nuke_node.knobs().keys():
			knb = nuke.String_Knob(name)
			#knb.setVisible(False)
			knb.setTooltip("No Touchy")
			self._nuke_node.addKnob(knb)
		else:
			knb = self._nuke_node.knob(name)
		return knb
	#----------------------------------------------------------------------
	def add_data_knob(self,name,knbtype):
		""""""
		if not name in self._nuke_node.knobs().keys():
			knb = knbtype(name)
			#knb.setVisible(False)
			knb.setTooltip("No Touchy")
			self._nuke_node.addKnob(knb)
		else:
			knb = self._nuke_node.knob(name)
		return knb
	#----------------------------------------------------------------------
	def _get_imbeded_data_knob(self):
		""""""
		return self._add_imbeded_data_knob()
	

	imbeded_data_knob = property(fget=_get_imbeded_data_knob, fdel=None, doc="The Nuke Knob That Holds The Data For This Widget To Rebuild Itself")
	imbeded_data_value = property(fget=_get_imbeded_data, fset=_set_imbeded_data, doc="The Data Used By This Widget To Rebuild Itself")
		
########################################################################
class External_UI_Base_Widget_Knob(Python_Widget_Knob):
	def __init__(self, node, parent=None):
		Python_Widget_Knob.__init__(self, node,parent=parent)
		master_Layout = DML_PYQT.QVBoxLayout(self)
		master_Layout.setSpacing(0)
		master_Layout.setContentsMargins(0, 0, 0, 0)
		self.file_wig = self._load_ui()
		master_Layout.addWidget(self.file_wig)
		
		for child in self.file_wig.findChildren(DML_PYQT.QObject):
			objectName = child.objectName()
			if len(objectName):
				if not hasattr(self,objectName):
					self.__dict__[objectName]=child
	#----------------------------------------------------------------------
	def _load_ui(self):
		""""""
		wig = Default_Ui_Loader.load(self._get_ui_file(), parent_widget=self)
		isinstance(wig,DML_PYQT.QWidget)
		return wig

	#----------------------------------------------------------------------
	def _get_ui_file(self):
		""""""
		return os.path.join(os.path.dirname(__file__), "default.ui")
	#----------------------------------------------------------------------
	ui_file = property(fget=_get_ui_file)
