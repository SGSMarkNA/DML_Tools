

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class ArtBuildPaintMenu(UI_Object.UI):
	"""
	polygons
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.artBuildPaintMenu(**kwargs)
			super(ArtBuildPaintMenu, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.artBuildPaintMenu(name, exists=True):
				super(ArtBuildPaintMenu, self).__init__(name)
			else:
				name = cmds.artBuildPaintMenu(name, **kwargs)
				super(ArtBuildPaintMenu, self).__init__(name, **dict(qtParent=parent))