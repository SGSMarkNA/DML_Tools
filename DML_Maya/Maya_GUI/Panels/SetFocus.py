

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class SetFocus(UI_Object.UI):
	"""
	Give keyboard focus to a specific control or panel, passed
	as an argument.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.setFocus(**kwargs)
			super(SetFocus, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.setFocus(name, exists=True):
				super(SetFocus, self).__init__(name)
			else:
				name = cmds.setFocus(name, **kwargs)
				super(SetFocus, self).__init__(name, **dict(qtParent=parent))