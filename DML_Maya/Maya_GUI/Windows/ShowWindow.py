

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class ShowWindow(UI_Object.UI):
	"""
	Make a window visible. If no window is specified then the current
	window (most recently created) is used. See also the 
	command's  flag.
	
	If the specified window is iconified, it will be opened.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.showWindow(**kwargs)
			super(ShowWindow, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.showWindow(name, exists=True):
				super(ShowWindow, self).__init__(name)
			else:
				name = cmds.showWindow(name, **kwargs)
				super(ShowWindow, self).__init__(name, **dict(qtParent=parent))