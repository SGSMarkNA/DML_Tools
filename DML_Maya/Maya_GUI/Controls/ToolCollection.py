

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class ToolCollection(UI_Object.UI):
	"""
	This command creates a tool button collection. Collections are parented
	to the current default layout if no parent is specified with
	the -p/parent flag.  As children of the layout they will be deleted when
	the layout is deleted. Collections may also span more than one window
	if the -gl/global flag is used. In this case the collection has no parent
	and must be explicitly deleted with the 'deleteUI' command when it is no
	longer wanted.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.toolCollection(**kwargs)
			super(ToolCollection, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.toolCollection(name, exists=True):
				super(ToolCollection, self).__init__(name)
			else:
				name = cmds.toolCollection(name, **kwargs)
				super(ToolCollection, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def collectionItemArray(self):
		"""
		
				Returns a string list giving the long names of all the items
				in this collection.
				
		"""
		return self.query(collectionItemArray=True)
	#----------------------------------------------------------------------
	@property
	def gl(self):
		"""
		
				Set the collection to have no parent layout.  This flag must be
				specified when the collection is created and can not be queried
				or edited.  Consequently, global collections must be explicitly
				deleted.
				
		"""
		return self.query(gl=True)
	#----------------------------------------------------------------------
	@property
	def numberOfCollectionItems(self):
		"""
		
				Returns the number of items that are in this collection.
				
		"""
		return self.query(numberOfCollectionItems=True)
	#----------------------------------------------------------------------
	def get_select(self):
		"""
		
				Select the specified collection item.  If queried will return
				the name of the currently selected collection item.
				
		"""
		return self.query(select=True)
	#----------------------------------------------------------------------
	def set_select(self, value):
		"""
		
				Select the specified collection item.  If queried will return
				the name of the currently selected collection item.
				
		"""
		self.edit(select=value)
	#----------------------------------------------------------------------
	select = property(get_select, set_select)