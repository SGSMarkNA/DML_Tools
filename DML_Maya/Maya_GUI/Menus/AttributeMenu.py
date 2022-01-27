

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class AttributeMenu(UI_Object.UI):
	"""
	Action to generate popup connection menus for Hypershade. This command is
	used internally by the Hypershade panel.
		  
	      render, hypergraph, shader, hypershade
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.attributeMenu(**kwargs)
			super(AttributeMenu, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.attributeMenu(name, exists=True):
				super(AttributeMenu, self).__init__(name)
			else:
				name = cmds.attributeMenu(name, **kwargs)
				super(AttributeMenu, self).__init__(name, **dict(qtParent=parent))