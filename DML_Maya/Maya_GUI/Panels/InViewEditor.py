

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class InViewEditor(UI_Object.UI):
	"""
	Mel access to the In-View Editor.
	In-View Editors display a customizable subset of a node's attributes,
	letting you adjust attributes directly in a scene instead of opening
	the Channel Box or Attribute Editor.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.inViewEditor(**kwargs)
			super(InViewEditor, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.inViewEditor(name, exists=True):
				super(InViewEditor, self).__init__(name)
			else:
				name = cmds.inViewEditor(name, **kwargs)
				super(InViewEditor, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def visible(self):
		"""
		
				Shows/hides the In-View Editor outside the Show Manips context.
				
		"""
		return self.query(visible=True)