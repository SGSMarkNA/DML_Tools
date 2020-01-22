

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class EditorTemplate(UI_Object.UI):
	"""
	The editorTemplate command allows the user to specify the
	conceptual layout of an attribute editor and leave the details
	of exactly which UI elements are used in the final result to the
	automatic dialog generation mechanism.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.editorTemplate(**kwargs)
			super(EditorTemplate, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.editorTemplate(name, exists=True):
				super(EditorTemplate, self).__init__(name)
			else:
				name = cmds.editorTemplate(name, **kwargs)
				super(EditorTemplate, self).__init__(name, **dict(qtParent=parent))