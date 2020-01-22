

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class LoadPrefObjects(UI_Object.UI):
	"""
	This command loads preference dependency nodes from "userPrefObjects.ma", if it
	exists, from the user preference directory.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.loadPrefObjects(**kwargs)
			super(LoadPrefObjects, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.loadPrefObjects(name, exists=True):
				super(LoadPrefObjects, self).__init__(name)
			else:
				name = cmds.loadPrefObjects(name, **kwargs)
				super(LoadPrefObjects, self).__init__(name, **dict(qtParent=parent))