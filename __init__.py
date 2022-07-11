import os
#from . import DML_General_Utilities



if os.environ.get("DML_TOOLS_USE_WING_DEBUG","0") == "1":
	try:
		from . import wingdbstub
		try:
			wingdbstub.Ensure()
		except ValueError:
			pass
	except (ImportError,ValueError):
		pass

#----------------------------------------------------------------------
def test_For_Maya():
	""""""
	try:
		import maya.cmds
		maya.cmds.about(version=True)
		return True
	except:
		return False

#----------------------------------------------------------------------
def test_For_Nuke():
	""""""
	try:
		import nuke
		return True
	except:
		return False

try:
	#from . import DML_PYQT
	import DML_PYQT
except ImportError:
	pass

if test_For_Maya():
	try:
		from . import DML_Maya
	except ImportError:
		pass
if test_For_Nuke():
	#from . import DML_Nuke
	import DML_Tools.DML_Nuke
	DML_Nuke = DML_Tools.DML_Nuke
	
#if False:
	#import DML_Nuke
	#import DML_PYQT