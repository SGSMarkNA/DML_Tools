

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class FontDialog(UI_Object.UI):
	"""
	Displays a dialog of available fonts for the user to select from. The
	name of the selected font is returned, or an empty string if no font was selected.
	
	When the  flag is used, no dialog is displayed. Instead
	the command returns an array of the available fonts.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.fontDialog(**kwargs)
			super(FontDialog, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.fontDialog(name, exists=True):
				super(FontDialog, self).__init__(name)
			else:
				name = cmds.fontDialog(name, **kwargs)
				super(FontDialog, self).__init__(name, **dict(qtParent=parent))