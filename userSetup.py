
try:
	import DML_Tools.DML_Maya as DML_Maya
	import DML_Tools.DML_PYQT as DML_PYQT
except ImportError:
	import inspect,os
	filename = inspect.getframeinfo(inspect.currentframe()).filename
	path = os.path.dirname(os.path.abspath(filename))
	if path.endswith("DML_Tools"):
		dml_tools_parent_dir = os.path.realpath(path+'/..')
		os.sys.path.append(dml_tools_parent_dir)
		import DML_Tools.DML_Maya as DML_Maya
		import DML_Tools.DML_PYQT as DML_PYQT