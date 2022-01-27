

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class InViewMessage(UI_Object.UI):
	"""
	Used for displaying in-view messages.
	
	Note: On Linux, the  flags for inViewMessage are
	only supported when running a window manager that supports compositing (transparency
	and opacity).  Otherwise, they are ignored.  In addition, the flags for message
	fading:  are supported,
	but the message will display without a fade effect if the window manager
	doesn't support compositing.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.inViewMessage(**kwargs)
			super(InViewMessage, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.inViewMessage(name, exists=True):
				super(InViewMessage, self).__init__(name)
			else:
				name = cmds.inViewMessage(name, **kwargs)
				super(InViewMessage, self).__init__(name, **dict(qtParent=parent))