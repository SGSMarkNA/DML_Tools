

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class SavePrefs(UI_Object.UI):
	"""
	This command saves preferences to disk. If no flags are specified
	then all pref types get saved out.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.savePrefs(**kwargs)
			super(SavePrefs, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.savePrefs(name, exists=True):
				super(SavePrefs, self).__init__(name)
			else:
				name = cmds.savePrefs(name, **kwargs)
				super(SavePrefs, self).__init__(name, **dict(qtParent=parent))