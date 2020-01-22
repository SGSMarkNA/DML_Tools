

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class RefreshEditorTemplates(UI_Object.UI):
	"""
	This command refreshes all cached attribute editor templates,
	including those copied from the standard AE. These are the templates
	constructed internally on a per node type basis. This is useful
	if attribute elements have changed and the templates need to
	be re-evaluated accordingly.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.refreshEditorTemplates(**kwargs)
			super(RefreshEditorTemplates, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.refreshEditorTemplates(name, exists=True):
				super(RefreshEditorTemplates, self).__init__(name)
			else:
				name = cmds.refreshEditorTemplates(name, **kwargs)
				super(RefreshEditorTemplates, self).__init__(name, **dict(qtParent=parent))