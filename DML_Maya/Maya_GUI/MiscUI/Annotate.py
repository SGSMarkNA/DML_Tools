

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class Annotate(UI_Object.UI):
	"""
	This command is used to create an annotation to be attached to the
	specified objects at the specified point.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.annotate(**kwargs)
			super(Annotate, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.annotate(name, exists=True):
				super(Annotate, self).__init__(name)
			else:
				name = cmds.annotate(name, **kwargs)
				super(Annotate, self).__init__(name, **dict(qtParent=parent))