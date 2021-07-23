from __future__ import print_function
import os
import sys

try:
	import DML_Tools.DML_PYQT as PYQT
except:
	os.sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../../.."))
	try:
		import DML_Tools.DML_PYQT as PYQT
	except Exception as e:
		sys.exit()
		
try:
	import maya.cmds as cmds
	cmds.about( version=True)
	_in_maya = True
except:
	_in_maya = False

GUI_Loader = PYQT.GUI.UI_Loader.GUI_Loader

import Main_Window

GUI_Loader.registerCustomWidget(Main_Window.Custom_TableWidget)

if _in_maya:
	import Maya_Main_Window
	GUI_Loader.registerCustomWidget(Maya_Main_Window.Name_Associations_Main_Window)
else:
	GUI_Loader.registerCustomWidget(Main_Window.Name_Associations_Main_Window)
	
	
#----------------------------------------------------------------------
def show_Main_Window():
	""""""
	main_window_ui_file = os.path.join(os.path.dirname(__file__),"UI","Main_Window.ui")
	try:
		wig = GUI_Loader.load_file(main_window_ui_file)
	except Exception:
		sys.exit()
	
	isinstance(wig,Main_Window.Name_Associations_Main_Window)
	if _in_maya:
		isinstance(wig,Maya_Main_Window.Name_Associations_Main_Window)
	wig._run_init()
	wig.show()
	return wig
	
	
if __name__ == '__main__':
	import sys
	app = PYQT.QApplication(sys.argv)
	show_Main_Window()
	sys.exit(app.exec_())