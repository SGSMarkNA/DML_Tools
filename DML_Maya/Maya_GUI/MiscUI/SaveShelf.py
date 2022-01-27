

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class SaveShelf(UI_Object.UI):
	"""
	This command saves the specified shelf (first argument) to the
	specified file (second argument).
	
	Note that this command doesn't work well with controls that have
	mixed mel and python command callbacks.  Also, because it saves the
	state to a mel file, it does not work with callbacks that are python
	callable objects.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.saveShelf(**kwargs)
			super(SaveShelf, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.saveShelf(name, exists=True):
				super(SaveShelf, self).__init__(name)
			else:
				name = cmds.saveShelf(name, **kwargs)
				super(SaveShelf, self).__init__(name, **dict(qtParent=parent))