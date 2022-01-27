

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class ConfirmDialog(UI_Object.UI):
	"""
	The confirmDialog command creates a modal dialog with a message to the
	user and a variable number of buttons to dismiss the dialog.  The
	dialog is dismissed when the user presses any button or chooses the
	close item from the window menu.  In the case where a button is
	pressed then the name of the button selected is returned.  If the
	dialog is dismissed via the close item then the string returned is
	specified by the  flag.
	
	The default behaviour when no arguments are specified is to create an
	empty single button dialog.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.confirmDialog(**kwargs)
			super(ConfirmDialog, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.confirmDialog(name, exists=True):
				super(ConfirmDialog, self).__init__(name)
			else:
				name = cmds.confirmDialog(name, **kwargs)
				super(ConfirmDialog, self).__init__(name, **dict(qtParent=parent))