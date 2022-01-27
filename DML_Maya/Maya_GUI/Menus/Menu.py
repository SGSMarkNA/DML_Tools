

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class Menu(UI_Object.UI):
	"""
	This command creates a new menu and adds it to the default window's
	menubar if no parent is specified.  The menu can be enabled/disabled.
	Note that this command may also be used on menu objects created using
	the command
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.menu(**kwargs)
			super(Menu, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.menu(name, exists=True):
				super(Menu, self).__init__(name)
			else:
				name = cmds.menu(name, **kwargs)
				super(Menu, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def allowOptionBoxes(self):
		"""
		
				Deprecated. All menus now always allow option boxes.
				Indicate whether the menu will be able to support option box
				menu items.
				
		"""
		return self.query(allowOptionBoxes=True)
	#----------------------------------------------------------------------
	def deleteAllItems(self,value):
		"""
		
				Delete all the items in this menu.
				
		"""
		self.edit(deleteAllItems=value)
	#----------------------------------------------------------------------
	def get_docTag(self):
		"""
		
				Attaches a tag to the menu.
				
		"""
		return self.query(docTag=True)
	#----------------------------------------------------------------------
	def set_docTag(self, value):
		"""
		
				Attaches a tag to the menu.
				
		"""
		self.edit(docTag=value)
	#----------------------------------------------------------------------
	docTag = property(get_docTag, set_docTag)
	#----------------------------------------------------------------------
	def get_enable(self):
		"""
		
				Enables/disables the menu.
				
		"""
		return self.query(enable=True)
	#----------------------------------------------------------------------
	def set_enable(self, value):
		"""
		
				Enables/disables the menu.
				
		"""
		self.edit(enable=value)
	#----------------------------------------------------------------------
	enable = property(get_enable, set_enable)
	#----------------------------------------------------------------------
	def get_familyImage(self):
		"""
		
				The filename of the icon associated with the menu. This
				icon will be used if a menu item does not have an icon image
				defined.
				
		"""
		return self.query(familyImage=True)
	#----------------------------------------------------------------------
	def set_familyImage(self, value):
		"""
		
				The filename of the icon associated with the menu. This
				icon will be used if a menu item does not have an icon image
				defined.
				
		"""
		self.edit(familyImage=value)
	#----------------------------------------------------------------------
	familyImage = property(get_familyImage, set_familyImage)
	#----------------------------------------------------------------------
	def get_helpMenu(self):
		"""
		
				Indicates that this menu is the help menu and will be the
				right most menu in the menu bar. On Unix systems the help menu
				is also right justified in the menu bar.
				
		"""
		return self.query(helpMenu=True)
	#----------------------------------------------------------------------
	def set_helpMenu(self, value):
		"""
		
				Indicates that this menu is the help menu and will be the
				right most menu in the menu bar. On Unix systems the help menu
				is also right justified in the menu bar.
				
		"""
		self.edit(helpMenu=value)
	#----------------------------------------------------------------------
	helpMenu = property(get_helpMenu, set_helpMenu)
	#----------------------------------------------------------------------
	@property
	def itemArray(self):
		"""
		
				Return string array of the menu item names.
				
		"""
		return self.query(itemArray=True)
	#----------------------------------------------------------------------
	def get_label(self):
		"""
		
				The text that is displayed for the menu.  If no label is
				supplied then the menuName will be used.
				
		"""
		return self.query(label=True)
	#----------------------------------------------------------------------
	def set_label(self, value):
		"""
		
				The text that is displayed for the menu.  If no label is
				supplied then the menuName will be used.
				
		"""
		self.edit(label=value)
	#----------------------------------------------------------------------
	label = property(get_label, set_label)
	#----------------------------------------------------------------------
	def get_ltVersion(self):
		"""
		
				This flag is used to specify the Maya LT version that this control
				feature was introduced, if the version flag is not specified, or
				if the version flag is specified but its argument is different.
				This value is only used by Maya LT, and otherwise ignored.
				The argument should be given as a string of the version number
				(e.g. "2014", "2015"). Currently only accepts major version
				numbers (e.g. 2014.5 should be given as "2014").
				
		"""
		return self.query(ltVersion=True)
	#----------------------------------------------------------------------
	def set_ltVersion(self, value):
		"""
		
				This flag is used to specify the Maya LT version that this control
				feature was introduced, if the version flag is not specified, or
				if the version flag is specified but its argument is different.
				This value is only used by Maya LT, and otherwise ignored.
				The argument should be given as a string of the version number
				(e.g. "2014", "2015"). Currently only accepts major version
				numbers (e.g. 2014.5 should be given as "2014").
				
		"""
		self.edit(ltVersion=value)
	#----------------------------------------------------------------------
	ltVersion = property(get_ltVersion, set_ltVersion)
	#----------------------------------------------------------------------
	def get_mnemonic(self):
		"""
		
				Set the Alt key to post that menu.  The character
				specified must match the case of its corresponding character in
				the menu item text, but selection from the keyboard is case
				insensitive.
				
		"""
		return self.query(mnemonic=True)
	#----------------------------------------------------------------------
	def set_mnemonic(self, value):
		"""
		
				Set the Alt key to post that menu.  The character
				specified must match the case of its corresponding character in
				the menu item text, but selection from the keyboard is case
				insensitive.
				
		"""
		self.edit(mnemonic=value)
	#----------------------------------------------------------------------
	mnemonic = property(get_mnemonic, set_mnemonic)
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
		
				Specify a script to be executed when the menu is about to be
				shown.
				
		"""
		self.edit(postMenuCommand=value)
	#----------------------------------------------------------------------
	def get_postMenuCommandOnce(self):
		"""
		
				Indicate the -pmc/postMenuCommand should only be
				invoked once.  Default value is false, ie.
				the -pmc/postMenuCommand is invoked every time the menu is
				shown.
				
		"""
		return self.query(postMenuCommandOnce=True)
	#----------------------------------------------------------------------
	def set_postMenuCommandOnce(self, value):
		"""
		
				Indicate the -pmc/postMenuCommand should only be
				invoked once.  Default value is false, ie.
				the -pmc/postMenuCommand is invoked every time the menu is
				shown.
				
		"""
		self.edit(postMenuCommandOnce=value)
	#----------------------------------------------------------------------
	postMenuCommandOnce = property(get_postMenuCommandOnce, set_postMenuCommandOnce)
	#----------------------------------------------------------------------
	def get_scrollable(self):
		"""
		
				Make the popup menus support scrolling. Default value is false.
				
		"""
		return self.query(scrollable=True)
	#----------------------------------------------------------------------
	def set_scrollable(self, value):
		"""
		
				Make the popup menus support scrolling. Default value is false.
				
		"""
		self.edit(scrollable=value)
	#----------------------------------------------------------------------
	scrollable = property(get_scrollable, set_scrollable)
	#----------------------------------------------------------------------
	def get_version(self):
		"""
		
				Specify the version that this menu feature was introduced.
				The argument should be given as a string of the version number
				(e.g. "2014", "2015"). Currently only accepts major version
				numbers (e.g. 2014.5 should be given as "2014").
				
		"""
		return self.query(version=True)
	#----------------------------------------------------------------------
	def set_version(self, value):
		"""
		
				Specify the version that this menu feature was introduced.
				The argument should be given as a string of the version number
				(e.g. "2014", "2015"). Currently only accepts major version
				numbers (e.g. 2014.5 should be given as "2014").
				
		"""
		self.edit(version=value)
	#----------------------------------------------------------------------
	version = property(get_version, set_version)
	#----------------------------------------------------------------------
	def get_visible(self):
		"""
		
				Shows/hides the menu.
				
		"""
		return self.query(visible=True)
	#----------------------------------------------------------------------
	def set_visible(self, value):
		"""
		
				Shows/hides the menu.
				
		"""
		self.edit(visible=value)
	#----------------------------------------------------------------------
	visible = property(get_visible, set_visible)