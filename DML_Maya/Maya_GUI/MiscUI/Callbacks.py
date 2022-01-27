

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class Callbacks(UI_Object.UI):
	"""
	This command allows you to add callbacks at key times during UI creation so
	that the Maya UI can be extended.
	The list of standard Maya hooks, as well as the arguments which will be passed
	to the callback based on the context are enumerated in the 
	section below.
	Custom hooks can also be added if third parties want to add UI extensibility to
	their plugins.
		  
	      ui, callback
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.callbacks(**kwargs)
			super(Callbacks, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.callbacks(name, exists=True):
				super(Callbacks, self).__init__(name)
			else:
				name = cmds.callbacks(name, **kwargs)
				super(Callbacks, self).__init__(name, **dict(qtParent=parent))