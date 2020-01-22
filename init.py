import nuke
try:
	import DML_Tools
	DML_Nuke = DML_Tools.DML_Nuke
	DML_PYQT = DML_Tools.DML_PYQT
except ImportError:
	import inspect,os
	filename = inspect.getframeinfo(inspect.currentframe()).filename
	path = os.path.dirname(os.path.abspath(filename))
	if path.endswith("DML_Tools"):
		dml_tools_parent_dir = os.path.realpath(path+'/..')
		os.sys.path.append(dml_tools_parent_dir)
		import DML_Tools
		DML_Nuke = DML_Tools.DML_Nuke
		DML_PYQT = DML_Tools.DML_PYQT

if nuke.GUI:
	nuke.addOnScriptLoad(DML_Tools.DML_Nuke.Nuke_GUI.Utils.get_Nuke_QMainWindow_Widget)