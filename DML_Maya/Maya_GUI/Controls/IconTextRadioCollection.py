

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class IconTextRadioCollection(UI_Object.UI):
	"""
	This command creates a cluster for iconTextRadioButtons.  Clusters
	will be parented to the current default layout if no parent is
	specified with the -p/parent flag. As children of the layout they will
	be deleted when the layout is deleted. Clusters may also span more
	than one window if the -g/global flag is used. In this case the
	cluster has no parent so must be explicitly deleted with
	the 'deleteUI' command.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.iconTextRadioCollection(**kwargs)
			super(IconTextRadioCollection, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.iconTextRadioCollection(name, exists=True):
				super(IconTextRadioCollection, self).__init__(name)
			else:
				name = cmds.iconTextRadioCollection(name, **kwargs)
				super(IconTextRadioCollection, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def collectionItemArray(self):
		"""
		
				Returns a string list giving the long names of all the items
				in this collection.
				
		"""
		return self.query(collectionItemArray=True)
	#----------------------------------------------------------------------
	def disableCommands(self,value):
		"""
		
				Allows a particular iconTextRadioButton in the collection to
				be selected without invoking the commands attached to
				the -cc/changeCommand, -onc/onCommand, or -ofc/offCommand flags.
				This flag is only meaningful when used in conjuction with
				the -edit and -select flags.
				
		"""
		self.edit(disableCommands=value)
	#----------------------------------------------------------------------
	@property
	def gl(self):
		"""
		
				Set the collection to have no parent layout.  If the collection has
				a parent layout then it will be deleted with that layout, otherwise
				if it is specified to be global it must be explicitly deleted.
				
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