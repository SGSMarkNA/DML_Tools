

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class MultiTouch(UI_Object.UI):
	"""
	Used to interact with the Gestura (multi-touch) library.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.multiTouch(**kwargs)
			super(MultiTouch, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.multiTouch(name, exists=True):
				super(MultiTouch, self).__init__(name)
			else:
				name = cmds.multiTouch(name, **kwargs)
				super(MultiTouch, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def gestures(self):
		"""
		
				Enables/Disables multi touch gestures.
				
		"""
		return self.query(gestures=True)
	#----------------------------------------------------------------------
	@property
	def trackpad(self):
		"""
		
				Sets the trackpad mode.  Values can be:
				
				1 - Cursor Control only
				2 - Multi-touch Gestures Only
				3 - Cursor and Multi-touch
				
				Note: this is a "Mac" only flag.
				
		"""
		return self.query(trackpad=True)