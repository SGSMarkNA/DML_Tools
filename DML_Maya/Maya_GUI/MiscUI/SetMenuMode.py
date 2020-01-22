

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class SetMenuMode(UI_Object.UI):
	"""
	Optionally sets a new Menu Mode for the menu bar in the main Maya window.
	Returns the current Menu Mode, and if a new one is specified, then the previous
	Menu Mode is returned.
	Note that due to recent changes to the menu set architecture (8.0+), this function now
	takes a menu set as a parameter instead of a label.
		  
	      menu, menus, menubar
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.setMenuMode(**kwargs)
			super(SetMenuMode, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.setMenuMode(name, exists=True):
				super(SetMenuMode, self).__init__(name)
			else:
				name = cmds.setMenuMode(name, **kwargs)
				super(SetMenuMode, self).__init__(name, **dict(qtParent=parent))