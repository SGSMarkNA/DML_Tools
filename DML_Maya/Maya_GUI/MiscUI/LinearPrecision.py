

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class LinearPrecision(UI_Object.UI):
	"""
	This command controls the display of linear strings in the interface.
	(See the linearField command). Setting this affects any linear strings
	displayed afterwards, formatting them so they will show at most the
	specified number of digits after the decimal point. Allowed values are
	0 through 6.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.linearPrecision(**kwargs)
			super(LinearPrecision, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.linearPrecision(name, exists=True):
				super(LinearPrecision, self).__init__(name)
			else:
				name = cmds.linearPrecision(name, **kwargs)
				super(LinearPrecision, self).__init__(name, **dict(qtParent=parent))