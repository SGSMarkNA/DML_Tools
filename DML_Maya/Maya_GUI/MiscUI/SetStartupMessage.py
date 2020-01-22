

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class SetStartupMessage(UI_Object.UI):
	"""
	Update the startup window message.  Also know as the 'Splash Screen',
	this is the window that appears while the application is starting up.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.setStartupMessage(**kwargs)
			super(SetStartupMessage, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.setStartupMessage(name, exists=True):
				super(SetStartupMessage, self).__init__(name)
			else:
				name = cmds.setStartupMessage(name, **kwargs)
				super(SetStartupMessage, self).__init__(name, **dict(qtParent=parent))