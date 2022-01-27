

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class TextManip(UI_Object.UI):
	"""
	Shows/hides the text manip.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.textManip(**kwargs)
			super(TextManip, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.textManip(name, exists=True):
				super(TextManip, self).__init__(name)
			else:
				name = cmds.textManip(name, **kwargs)
				super(TextManip, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def visible(self):
		"""
		
				Shows/hides the text manip.
				
		"""
		return self.query(visible=True)