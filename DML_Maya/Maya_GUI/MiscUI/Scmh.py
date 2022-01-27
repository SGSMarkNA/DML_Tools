

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class Scmh(UI_Object.UI):
	"""
	Set the current manipulator handle value(s).  In UI units (where
	applicable), though the syntax is set to handle the unit type
	of the current manipulator handle (if available).
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.scmh(**kwargs)
			super(Scmh, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.scmh(name, exists=True):
				super(Scmh, self).__init__(name)
			else:
				name = cmds.scmh(name, **kwargs)
				super(Scmh, self).__init__(name, **dict(qtParent=parent))