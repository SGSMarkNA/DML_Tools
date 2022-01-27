

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class DisableIncorrectNameWarning(UI_Object.UI):
	"""
	Disable the warning dialog which complains about incorrect node names when opening
	Maya files.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.disableIncorrectNameWarning(**kwargs)
			super(DisableIncorrectNameWarning, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.disableIncorrectNameWarning(name, exists=True):
				super(DisableIncorrectNameWarning, self).__init__(name)
			else:
				name = cmds.disableIncorrectNameWarning(name, **kwargs)
				super(DisableIncorrectNameWarning, self).__init__(name, **dict(qtParent=parent))