

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class SaveViewportSettings(UI_Object.UI):
	"""
	This command causes all the 3d views to save their settings as optionVar's.
	This is called automatically by the system when Maya exits.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.saveViewportSettings(**kwargs)
			super(SaveViewportSettings, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.saveViewportSettings(name, exists=True):
				super(SaveViewportSettings, self).__init__(name)
			else:
				name = cmds.saveViewportSettings(name, **kwargs)
				super(SaveViewportSettings, self).__init__(name, **dict(qtParent=parent))