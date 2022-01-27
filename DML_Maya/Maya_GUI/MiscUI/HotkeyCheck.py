

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class HotkeyCheck(UI_Object.UI):
	"""
	This command checks if the given hotkey is mapped to a nameCommand
	object.  If so, the annotation of the nameCommand object is returned.
	Otherwise an empty string is returned.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.hotkeyCheck(**kwargs)
			super(HotkeyCheck, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.hotkeyCheck(name, exists=True):
				super(HotkeyCheck, self).__init__(name)
			else:
				name = cmds.hotkeyCheck(name, **kwargs)
				super(HotkeyCheck, self).__init__(name, **dict(qtParent=parent))