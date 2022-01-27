

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class GetPanel(UI_Object.UI):
	"""
	This command returns panel and panel configuration information.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.getPanel(**kwargs)
			super(GetPanel, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.getPanel(name, exists=True):
				super(GetPanel, self).__init__(name)
			else:
				name = cmds.getPanel(name, **kwargs)
				super(GetPanel, self).__init__(name, **dict(qtParent=parent))