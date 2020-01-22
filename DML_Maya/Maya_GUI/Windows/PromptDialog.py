

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class PromptDialog(UI_Object.UI):
	"""
	The promptDialog command creates a modal dialog with a message to the
	user, a text field in which the user may enter a response, and a
	variable number of buttons to dismiss the dialog.  The dialog is
	dismissed when the user presses any button or chooses the
	close item from the window menu.  In the case where a button is
	pressed then the name of the button selected is returned.  If the
	dialog is dismissed via the close item then the string returned is
	specified by the  flag.
	
	The default behaviour when no arguments are specified is to create an
	empty single button dialog.
	
	To obtain the text entered by the user simply query
	the  flag.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.promptDialog(**kwargs)
			super(PromptDialog, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.promptDialog(name, exists=True):
				super(PromptDialog, self).__init__(name)
			else:
				name = cmds.promptDialog(name, **kwargs)
				super(PromptDialog, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def text(self):
		"""
		
				The field text.
				
		"""
		return self.query(text=True)