

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class RadioMenuItemCollection(UI_Object.UI):
	"""
	This command creates a radioMenuItemCollection.  Attach radio menu
	items to radio menu item collection objects to get radio button
	behaviour.  Radio menu item collections will be parented to the
	current menu if no parent is specified with the 
	flag. As children of the menu they will be deleted when the menu is
	deleted. Collections may also span more than one menu if
	the  flag is used. In this case the collection has no
	parent menu and must be explicitly deleted with the 
	command when it is no longer wanted.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.radioMenuItemCollection(**kwargs)
			super(RadioMenuItemCollection, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.radioMenuItemCollection(name, exists=True):
				super(RadioMenuItemCollection, self).__init__(name)
			else:
				name = cmds.radioMenuItemCollection(name, **kwargs)
				super(RadioMenuItemCollection, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def gl(self):
		"""
		
				Set the collection to have no parent menu.  Global
				collections must be explicitly deleted.
				
		"""
		return self.query(gl=True)