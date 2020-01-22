

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class OverrideModifier(UI_Object.UI):
	"""
	This command allows you to assign modifier key behaviour to other
	parts of the system.  For example you can use a hotkey
	or input device instead of a modifer key to perform the same action.
	
	Note that the original modifier key behaviour is not altered in anyway.
	For example, if you've assigned "Ctrl" key behaviour to the "c" key
	then the "Ctrl" key will still work as you expect, all you've done is
	allowed yourself to use the "c" key as an alternative to the "Ctrl" key.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.overrideModifier(**kwargs)
			super(OverrideModifier, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.overrideModifier(name, exists=True):
				super(OverrideModifier, self).__init__(name)
			else:
				name = cmds.overrideModifier(name, **kwargs)
				super(OverrideModifier, self).__init__(name, **dict(qtParent=parent))