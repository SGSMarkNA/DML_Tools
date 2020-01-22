

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class ShowSelectionInTitle(UI_Object.UI):
	"""
	This command causes the title of the window specified as an argument
	to be linked to the current file and selection. When selection
	changes, the window title will change to show the current file name
	and the name of the last selected object.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.showSelectionInTitle(**kwargs)
			super(ShowSelectionInTitle, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.showSelectionInTitle(name, exists=True):
				super(ShowSelectionInTitle, self).__init__(name)
			else:
				name = cmds.showSelectionInTitle(name, **kwargs)
				super(ShowSelectionInTitle, self).__init__(name, **dict(qtParent=parent))