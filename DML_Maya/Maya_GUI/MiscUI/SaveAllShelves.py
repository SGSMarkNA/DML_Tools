

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class SaveAllShelves(UI_Object.UI):
	"""
	This command writes all shelves that are immediate children of the specified
	control layout to the prefs directory.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.saveAllShelves(**kwargs)
			super(SaveAllShelves, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.saveAllShelves(name, exists=True):
				super(SaveAllShelves, self).__init__(name)
			else:
				name = cmds.saveAllShelves(name, **kwargs)
				super(SaveAllShelves, self).__init__(name, **dict(qtParent=parent))