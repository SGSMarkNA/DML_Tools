

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class HeadsUpMessage(UI_Object.UI):
	"""
	This command draws a message in the 3d view.  The message
	is automatically erased at the next screen refresh.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.headsUpMessage(**kwargs)
			super(HeadsUpMessage, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.headsUpMessage(name, exists=True):
				super(HeadsUpMessage, self).__init__(name)
			else:
				name = cmds.headsUpMessage(name, **kwargs)
				super(HeadsUpMessage, self).__init__(name, **dict(qtParent=parent))