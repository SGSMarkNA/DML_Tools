

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class MenuSet(UI_Object.UI):
	"""
	Create a menu set which is used to logically order menus for display
	in the main menu bar.  Such menu sets can be edited and reordered
	dynamically.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.menuSet(**kwargs)
			super(MenuSet, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.menuSet(name, exists=True):
				super(MenuSet, self).__init__(name)
			else:
				name = cmds.menuSet(name, **kwargs)
				super(MenuSet, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def allMenuSets(self):
		"""
		
				Returns an array of the all the menu set object names in use.  Query returns string array.
				
		"""
		return self.query(allMenuSets=True)
	#----------------------------------------------------------------------
	@property
	def currentMenuSet(self):
		"""
		
				The currently active menu set under which all operations affect (append, insert, remove, etc.).  Query returns string.
				
		"""
		return self.query(currentMenuSet=True)
	#----------------------------------------------------------------------
	@property
	def exists(self):
		"""
		
				Returns whether the specified menu set exists.  This query flag supports string arguments.
				ie. menuSet -q -exists animationMenuSet;
				      In query mode, this flag needs a value.
				
		"""
		return self.query(exists=True)
	#----------------------------------------------------------------------
	def get_hotBoxVisible(self):
		"""
		
				Whether this menu set should be displayed in the hotbox as well as in the main menubar.
				
		"""
		return self.query(hotBoxVisible=True)
	#----------------------------------------------------------------------
	def set_hotBoxVisible(self, value):
		"""
		
				Whether this menu set should be displayed in the hotbox as well as in the main menubar.
				
		"""
		self.edit(hotBoxVisible=value)
	#----------------------------------------------------------------------
	hotBoxVisible = property(get_hotBoxVisible, set_hotBoxVisible)
	#----------------------------------------------------------------------
	@property
	def label(self):
		"""
		
				The label of the current menu set.  Query returns string.
				
		"""
		return self.query(label=True)
	#----------------------------------------------------------------------
	@property
	def menuArray(self):
		"""
		
				An array of menu names (strings) in the current menu set.  Query returns string array.
				
		"""
		return self.query(menuArray=True)
	#----------------------------------------------------------------------
	@property
	def numberOfMenuSets(self):
		"""
		
				Number of menuSets in total.  Query returns int.
				
		"""
		return self.query(numberOfMenuSets=True)
	#----------------------------------------------------------------------
	@property
	def numberOfMenus(self):
		"""
		
				The mumber of menus in the current menu set.  Query returns int.
				
		"""
		return self.query(numberOfMenus=True)
	#----------------------------------------------------------------------
	def get_permanent(self):
		"""
		
				Whether this menu set can be removed.
				
		"""
		return self.query(permanent=True)
	#----------------------------------------------------------------------
	def set_permanent(self, value):
		"""
		
				Whether this menu set can be removed.
				
		"""
		self.edit(permanent=value)
	#----------------------------------------------------------------------
	permanent = property(get_permanent, set_permanent)