

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class AutoPlace(UI_Object.UI):
	"""
	This command takes a point in the centre of the current
	modeling pane and projects it onto the live surface.
	This produces a point in 3 space which is returned.
	If the  flag is set the current mouse position
	is used rather than the centre of the modeling pane.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.autoPlace(**kwargs)
			super(AutoPlace, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.autoPlace(name, exists=True):
				super(AutoPlace, self).__init__(name)
			else:
				name = cmds.autoPlace(name, **kwargs)
				super(AutoPlace, self).__init__(name, **dict(qtParent=parent))