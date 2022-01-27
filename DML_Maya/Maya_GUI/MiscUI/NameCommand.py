

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class NameCommand(UI_Object.UI):
	"""
	This command creates a nameCommand object. Each nameCommand object
	can be connected to a hotkey. Thereafter, the nameCommand's command
	string will be executed whenever the hotkey is pressed (or released,
	as specified by the user).
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.nameCommand(**kwargs)
			super(NameCommand, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.nameCommand(name, exists=True):
				super(NameCommand, self).__init__(name)
			else:
				name = cmds.nameCommand(name, **kwargs)
				super(NameCommand, self).__init__(name, **dict(qtParent=parent))