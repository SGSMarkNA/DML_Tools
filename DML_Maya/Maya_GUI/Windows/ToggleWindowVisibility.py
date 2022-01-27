

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class ToggleWindowVisibility(UI_Object.UI):
	"""
	Toggle the visibility of a window. If no window is specified then
	the current window (most recently created) is used. See also
	the  command's  flag.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.toggleWindowVisibility(**kwargs)
			super(ToggleWindowVisibility, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.toggleWindowVisibility(name, exists=True):
				super(ToggleWindowVisibility, self).__init__(name)
			else:
				name = cmds.toggleWindowVisibility(name, **kwargs)
				super(ToggleWindowVisibility, self).__init__(name, **dict(qtParent=parent))