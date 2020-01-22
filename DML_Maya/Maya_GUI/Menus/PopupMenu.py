

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class PopupMenu(UI_Object.UI):
	"""
	This command creates a popup menu and attaches it to the current
	control if no parent is specified.  The popup menu is posted with the
	right mouse button by default.
	
	Popup menus can be added to any kind of control, however,
	on some widgets, only the standard menu button (3rd mouse button)
	can be used to trigger popup menus. This is to meet generally
	accepted UI guidelines that assign the 3rd mouse button and only
	this one to popup menus, and also to prevent unexpected behavior
	of controls like text fields, that expect 1st and 2nd button to be
	reserved for contextual operations like text or item selection...
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.popupMenu(**kwargs)
			super(PopupMenu, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.popupMenu(name, exists=True):
				super(PopupMenu, self).__init__(name)
			else:
				name = cmds.popupMenu(name, **kwargs)
				super(PopupMenu, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def allowOptionBoxes(self):
		"""
		
				Indicate whether the menu will be able to support option box
				menu items.  An error results if an option box item is added to a
				menu that doesn't allow them.  This flag may be queried and must be
				specified when the popup menu is created.  The default value is
				false.
				
		"""
		return self.query(allowOptionBoxes=True)
	#----------------------------------------------------------------------
	def get_altModifier(self):
		"""
		
				Specify this flag if the Alt modifier must be pressed when
				posting the popup menu.
				
		"""
		return self.query(altModifier=True)
	#----------------------------------------------------------------------
	def set_altModifier(self, value):
		"""
		
				Specify this flag if the Alt modifier must be pressed when
				posting the popup menu.
				
		"""
		self.edit(altModifier=value)
	#----------------------------------------------------------------------
	altModifier = property(get_altModifier, set_altModifier)
	#----------------------------------------------------------------------
	def get_button(self):
		"""
		
				Indicate which button posts the popup menu.  Valid values
				range from 1 to 3 where 1 is the left most button on the mouse.
				
		"""
		return self.query(button=True)
	#----------------------------------------------------------------------
	def set_button(self, value):
		"""
		
				Indicate which button posts the popup menu.  Valid values
				range from 1 to 3 where 1 is the left most button on the mouse.
				
		"""
		self.edit(button=value)
	#----------------------------------------------------------------------
	button = property(get_button, set_button)
	#----------------------------------------------------------------------
	def get_ctrlModifier(self):
		"""
		
				Specify this flag if the Cntl modifier must be pressed when
				posting the popup menu.
				
		"""
		return self.query(ctrlModifier=True)
	#----------------------------------------------------------------------
	def set_ctrlModifier(self, value):
		"""
		
				Specify this flag if the Cntl modifier must be pressed when
				posting the popup menu.
				
		"""
		self.edit(ctrlModifier=value)
	#----------------------------------------------------------------------
	ctrlModifier = property(get_ctrlModifier, set_ctrlModifier)
	#----------------------------------------------------------------------
	def deleteAllItems(self,value):
		"""
		
				Delete all the items in this menu.
				
		"""
		self.edit(deleteAllItems=value)
	#----------------------------------------------------------------------
	@property
	def itemArray(self):
		"""
		
				Return string array of the menu item names.
				
		"""
		return self.query(itemArray=True)
	#----------------------------------------------------------------------
	def get_markingMenu(self):
		"""
		
				Set the marking menu state of this popup menu.
				
		"""
		return self.query(markingMenu=True)
	#----------------------------------------------------------------------
	def set_markingMenu(self, value):
		"""
		
				Set the marking menu state of this popup menu.
				
		"""
		self.edit(markingMenu=value)
	#----------------------------------------------------------------------
	markingMenu = property(get_markingMenu, set_markingMenu)
	#----------------------------------------------------------------------
	@property
	def numberOfItems(self):
		"""
		
				Return number of items in the menu.
				
		"""
		return self.query(numberOfItems=True)
	#----------------------------------------------------------------------
	def postMenuCommand(self,value):
		"""
		
				Specify a script to be executed when the popup menu is about
				to be shown.
				
		"""
		self.edit(postMenuCommand=value)
	#----------------------------------------------------------------------
	def get_postMenuCommandOnce(self):
		"""
		
				Indicate the -pmc/postMenuCommand should only be
				invoked once.  Default value is false, ie.
				the -pmc/postMenuCommand is invoked every time the popup menu is
				shown.
				
		"""
		return self.query(postMenuCommandOnce=True)
	#----------------------------------------------------------------------
	def set_postMenuCommandOnce(self, value):
		"""
		
				Indicate the -pmc/postMenuCommand should only be
				invoked once.  Default value is false, ie.
				the -pmc/postMenuCommand is invoked every time the popup menu is
				shown.
				
		"""
		self.edit(postMenuCommandOnce=value)
	#----------------------------------------------------------------------
	postMenuCommandOnce = property(get_postMenuCommandOnce, set_postMenuCommandOnce)
	#----------------------------------------------------------------------
	def get_shiftModifier(self):
		"""
		
				Specify this flag if the Shift modifier must be pressed
				when posting the popup menu.
				
		"""
		return self.query(shiftModifier=True)
	#----------------------------------------------------------------------
	def set_shiftModifier(self, value):
		"""
		
				Specify this flag if the Shift modifier must be pressed
				when posting the popup menu.
				
		"""
		self.edit(shiftModifier=value)
	#----------------------------------------------------------------------
	shiftModifier = property(get_shiftModifier, set_shiftModifier)