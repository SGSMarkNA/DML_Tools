

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class CreateEditor(UI_Object.UI):
	"""
	This command creates a property sheet for any dependency node. The
	second argument is the name of the node, and the first is the name of
	a layout into which the property sheet controls should be placed.
	
	The property sheets created by this command can by user-customized
	using the  command.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.createEditor(**kwargs)
			super(CreateEditor, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.createEditor(name, exists=True):
				super(CreateEditor, self).__init__(name)
			else:
				name = cmds.createEditor(name, **kwargs)
				super(CreateEditor, self).__init__(name, **dict(qtParent=parent))