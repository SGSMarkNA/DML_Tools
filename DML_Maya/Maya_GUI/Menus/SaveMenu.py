

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class SaveMenu(UI_Object.UI):
	"""
	This command is used for saving the contents of a menu, so that
	another instance of the menu may be recreated later. The command
	writes out a file which, when run as a script, will rebuild the
	menuItems contained in the original menu. Note that the fileName
	is relative to the user's marking menu preference directory.
	
	Note that this command is used solely by the Marking Menu Editor
	and is not intended to be used for general purposes.
	
	Note that this command doesn't work well with controls that have
	mixed mel and python command callbacks.  Also, because it saves the menu
	state to a mel file, it does not work with callbacks that are python
	callable objects.
	
	The first argument is the name of the manu to save, the second one is
	the name of the file.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.saveMenu(**kwargs)
			super(SaveMenu, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.saveMenu(name, exists=True):
				super(SaveMenu, self).__init__(name)
			else:
				name = cmds.saveMenu(name, **kwargs)
				super(SaveMenu, self).__init__(name, **dict(qtParent=parent))