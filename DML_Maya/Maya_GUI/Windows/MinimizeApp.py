

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class MinimizeApp(UI_Object.UI):
	"""
	This command minimizes (iconifies) all of the application's windows
	into a single desktop icon.  To restore the application click on the
	desktop icon.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.minimizeApp(**kwargs)
			super(MinimizeApp, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.minimizeApp(name, exists=True):
				super(MinimizeApp, self).__init__(name)
			else:
				name = cmds.minimizeApp(name, **kwargs)
				super(MinimizeApp, self).__init__(name, **dict(qtParent=parent))