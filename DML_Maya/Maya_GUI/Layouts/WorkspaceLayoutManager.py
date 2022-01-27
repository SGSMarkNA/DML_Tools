

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class WorkspaceLayoutManager(UI_Object.UI):
	"""
	The Workspace Layout Manager loads and saves the layout of the various toolbars and windows in the user interface.
	This command allows listing and managing their properties.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.workspaceLayoutManager(**kwargs)
			super(WorkspaceLayoutManager, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.workspaceLayoutManager(name, exists=True):
				super(WorkspaceLayoutManager, self).__init__(name)
			else:
				name = cmds.workspaceLayoutManager(name, **kwargs)
				super(WorkspaceLayoutManager, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def current(self):
		"""
		
				Get the name of the current layout.
				
		"""
		return self.query(current=True)