

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class GrabColor(UI_Object.UI):
	"""
	This command changes the cursor and enters a modal state which will be
	exited by pressing a mouse button.  The color component values of the
	pixel below the cursor at the time of the button press are returned.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.grabColor(**kwargs)
			super(GrabColor, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.grabColor(name, exists=True):
				super(GrabColor, self).__init__(name)
			else:
				name = cmds.grabColor(name, **kwargs)
				super(GrabColor, self).__init__(name, **dict(qtParent=parent))