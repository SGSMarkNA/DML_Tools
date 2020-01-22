

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class CanCreateCaddyManip(UI_Object.UI):
	"""
	This command returns true if there can be a manipulator made for
	the specified selection, false otherwise.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.canCreateCaddyManip(**kwargs)
			super(CanCreateCaddyManip, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.canCreateCaddyManip(name, exists=True):
				super(CanCreateCaddyManip, self).__init__(name)
			else:
				name = cmds.canCreateCaddyManip(name, **kwargs)
				super(CanCreateCaddyManip, self).__init__(name, **dict(qtParent=parent))