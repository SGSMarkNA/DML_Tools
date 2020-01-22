

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class SetNodeTypeFlag(UI_Object.UI):
	"""
	This command sets static data on the specified node type. This will affect the
	class of node type as a whole.  The argument passed may be the name of the node
	type or the node type tag.  Node type tags may be found using the objectType
	command.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.setNodeTypeFlag(**kwargs)
			super(SetNodeTypeFlag, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.setNodeTypeFlag(name, exists=True):
				super(SetNodeTypeFlag, self).__init__(name)
			else:
				name = cmds.setNodeTypeFlag(name, **kwargs)
				super(SetNodeTypeFlag, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def display(self):
		"""
		
				Sets whether the node type will appear in the UI or not.  Setting
				display to false will cause the node type to not appear in the UI.
				Query mode to obtain the value of the display flag.
				
		"""
		return self.query(display=True)
	#----------------------------------------------------------------------
	@property
	def threadSafe(self):
		"""
		
				Sets whether the node type will evaluate in parallel when using the parallel DG
				evaluation option in Viewport 2.0.
				In query mode returns true if the node type will evaluate in parallel when using
				the parallel DG evaluation option in Viewport 2.0.
				
		"""
		return self.query(threadSafe=True)