

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class WorkspacePanel(UI_Object.UI):
	"""
	Workspace panel.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.workspacePanel(**kwargs)
			super(WorkspacePanel, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.workspacePanel(name, exists=True):
				super(WorkspacePanel, self).__init__(name)
			else:
				name = cmds.workspacePanel(name, **kwargs)
				super(WorkspacePanel, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def get_mainWindow(self):
		"""
		
				Main window for the application.  The main window
				has an 'Exit' item in the Window Manager menu.  By default, the
				first created window becomes the main window.
				
		"""
		return self.query(mainWindow=True)
	#----------------------------------------------------------------------
	def set_mainWindow(self, value):
		"""
		
				Main window for the application.  The main window
				has an 'Exit' item in the Window Manager menu.  By default, the
				first created window becomes the main window.
				
		"""
		self.edit(mainWindow=value)
	#----------------------------------------------------------------------
	mainWindow = property(get_mainWindow, set_mainWindow)