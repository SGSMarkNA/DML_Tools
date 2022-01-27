

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class LayoutDialog(UI_Object.UI):
	"""
	The layoutDialog command creates a modal dialog containing a formLayout
	with 100 divisions. The formLayout can be populated with arbitrary UI
	elements through use of the '-ui/-uiScript' flag.
	NOTE:
	A layoutDialog is not a window and certain UI elements will not function
	properly within it. In particular menuBars and panels containing menuBars
	should not be used with the layoutDialog.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.layoutDialog(**kwargs)
			super(LayoutDialog, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.layoutDialog(name, exists=True):
				super(LayoutDialog, self).__init__(name)
			else:
				name = cmds.layoutDialog(name, **kwargs)
				super(LayoutDialog, self).__init__(name, **dict(qtParent=parent))