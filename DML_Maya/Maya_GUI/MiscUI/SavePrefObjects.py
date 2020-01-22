

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class SavePrefObjects(UI_Object.UI):
	"""
	This command saves preference dependency nodes to "userPrefObjects.ma" in
	the user preference directory.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.savePrefObjects(**kwargs)
			super(SavePrefObjects, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.savePrefObjects(name, exists=True):
				super(SavePrefObjects, self).__init__(name)
			else:
				name = cmds.savePrefObjects(name, **kwargs)
				super(SavePrefObjects, self).__init__(name, **dict(qtParent=parent))