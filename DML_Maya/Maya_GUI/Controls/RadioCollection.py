

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class RadioCollection(UI_Object.UI):
	"""
	This command creates a radio button collection. Collections are
	parented to the current default layout if no parent is specified with
	the  flag.  As children of the layout they will be
	deleted when the layout is deleted. Collections may also span more
	than one window if the  flag is used. In this case
	the collection has no parent and must be explicitly deleted with the
	 command when it is no longer wanted.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.radioCollection(**kwargs)
			super(RadioCollection, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.radioCollection(name, exists=True):
				super(RadioCollection, self).__init__(name)
			else:
				name = cmds.radioCollection(name, **kwargs)
				super(RadioCollection, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def collectionItemArray(self):
		"""
		
				Return a string list giving the long names of all the items
				in this collection.
				
		"""
		return self.query(collectionItemArray=True)
	#----------------------------------------------------------------------
	@property
	def gl(self):
		"""
		
				Set the collection to have no parent layout.  Global
				collections must be explicitly deleted.
				
		"""
		return self.query(gl=True)
	#----------------------------------------------------------------------
	@property
	def numberOfCollectionItems(self):
		"""
		
				Return the number of items in this collection.
				
		"""
		return self.query(numberOfCollectionItems=True)
	#----------------------------------------------------------------------
	def get_select(self):
		"""
		
				Select the specified collection item.  If queried will
				return the name of the currently selected collection item.
				
		"""
		return self.query(select=True)
	#----------------------------------------------------------------------
	def set_select(self, value):
		"""
		
				Select the specified collection item.  If queried will
				return the name of the currently selected collection item.
				
		"""
		self.edit(select=value)
	#----------------------------------------------------------------------
	select = property(get_select, set_select)