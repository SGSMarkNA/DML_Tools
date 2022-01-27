

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class DefaultNavigation(UI_Object.UI):
	"""
	The defaultNavigation command defines default behaviours when
	creating or manipulating connections between nodes and when
	navigating between nodes via those connections. This command is
	primarily used by attribute editors.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.defaultNavigation(**kwargs)
			super(DefaultNavigation, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.defaultNavigation(name, exists=True):
				super(DefaultNavigation, self).__init__(name)
			else:
				name = cmds.defaultNavigation(name, **kwargs)
				super(DefaultNavigation, self).__init__(name, **dict(qtParent=parent))