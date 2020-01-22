

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class MenuItem(UI_Object.UI):
	"""
	This command creates/edits/queries menu items.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.menuItem(**kwargs)
			super(MenuItem, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.menuItem(name, exists=True):
				super(MenuItem, self).__init__(name)
			else:
				name = cmds.menuItem(name, **kwargs)
				super(MenuItem, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def allowOptionBoxes(self):
		"""
		
				Deprecated. All menus and menu items always allow option boxes.
				In the case of submenu items this flag specifies whether the
				submenu will be able to support option box menu items.
				Always returns true.
				
		"""
		return self.query(allowOptionBoxes=True)
	#----------------------------------------------------------------------
	def get_annotation(self):
		"""
		
				Annotate the menu item with an extra string value.
				
		"""
		return self.query(annotation=True)
	#----------------------------------------------------------------------
	def set_annotation(self, value):
		"""
		
				Annotate the menu item with an extra string value.
				
		"""
		self.edit(annotation=value)
	#----------------------------------------------------------------------
	annotation = property(get_annotation, set_annotation)
	#----------------------------------------------------------------------
	@property
	def boldFont(self):
		"""
		
				Specify if text should be bold. Only supported in menus
				which use the marking menu implementation.  Default is false
				for Windows, and true for all other platforms.
				
		"""
		return self.query(boldFont=True)
	#----------------------------------------------------------------------
	def get_checkBox(self):
		"""
		
				Creates a check box menu item.  Argument specifies the
				check box value.
				
		"""
		return self.query(checkBox=True)
	#----------------------------------------------------------------------
	def set_checkBox(self, value):
		"""
		
				Creates a check box menu item.  Argument specifies the
				check box value.
				
		"""
		self.edit(checkBox=value)
	#----------------------------------------------------------------------
	checkBox = property(get_checkBox, set_checkBox)
	#----------------------------------------------------------------------
	@property
	def collection(self):
		"""
		
				To explicitly add a radio menu item to a radioMenuItemCollection.
				
		"""
		return self.query(collection=True)
	#----------------------------------------------------------------------
	def get_command(self):
		"""
		
				Attaches a command/script that will be executed when the
				item is selected. Note this command is not executed when the
				menu item is in an optionMenu control.
				
		"""
		return self.query(command=True)
	#----------------------------------------------------------------------
	def set_command(self, value):
		"""
		
				Attaches a command/script that will be executed when the
				item is selected. Note this command is not executed when the
				menu item is in an optionMenu control.
				
		"""
		self.edit(command=value)
	#----------------------------------------------------------------------
	command = property(get_command, set_command)
	#----------------------------------------------------------------------
	def get_data(self):
		"""
		
				Attaches a piece of user-defined data to the menu item.
				
		"""
		return self.query(data=True)
	#----------------------------------------------------------------------
	def set_data(self, value):
		"""
		
				Attaches a piece of user-defined data to the menu item.
				
		"""
		self.edit(data=value)
	#----------------------------------------------------------------------
	data = property(get_data, set_data)
	#----------------------------------------------------------------------
	@property
	def divider(self):
		"""
		
				Creates a divider menu item.
				
		"""
		return self.query(divider=True)
	#----------------------------------------------------------------------
	def get_dividerLabel(self):
		"""
		
				Adds a label to a divider menu item.
				
		"""
		return self.query(dividerLabel=True)
	#----------------------------------------------------------------------
	def set_dividerLabel(self, value):
		"""
		
				Adds a label to a divider menu item.
				
		"""
		self.edit(dividerLabel=value)
	#----------------------------------------------------------------------
	dividerLabel = property(get_dividerLabel, set_dividerLabel)
	#----------------------------------------------------------------------
	def get_docTag(self):
		"""
		
				Attaches a tag to the menu item.
				
		"""
		return self.query(docTag=True)
	#----------------------------------------------------------------------
	def set_docTag(self, value):
		"""
		
				Attaches a tag to the menu item.
				
		"""
		self.edit(docTag=value)
	#----------------------------------------------------------------------
	docTag = property(get_docTag, set_docTag)
	#----------------------------------------------------------------------
	def get_dragDoubleClickCommand(self):
		"""
		
				If the menu item is put on the shelf then this command
				will be invoked when the corresponding shelf object is double
				clicked.
				
		"""
		return self.query(dragDoubleClickCommand=True)
	#----------------------------------------------------------------------
	def set_dragDoubleClickCommand(self, value):
		"""
		
				If the menu item is put on the shelf then this command
				will be invoked when the corresponding shelf object is double
				clicked.
				
		"""
		self.edit(dragDoubleClickCommand=value)
	#----------------------------------------------------------------------
	dragDoubleClickCommand = property(get_dragDoubleClickCommand, set_dragDoubleClickCommand)
	#----------------------------------------------------------------------
	def get_dragMenuCommand(self):
		"""
		
				If the menu item is put on the shelf then this command
				will be invoked when the corresponding shelf object is clicked.
				
		"""
		return self.query(dragMenuCommand=True)
	#----------------------------------------------------------------------
	def set_dragMenuCommand(self, value):
		"""
		
				If the menu item is put on the shelf then this command
				will be invoked when the corresponding shelf object is clicked.
				
		"""
		self.edit(dragMenuCommand=value)
	#----------------------------------------------------------------------
	dragMenuCommand = property(get_dragMenuCommand, set_dragMenuCommand)
	#----------------------------------------------------------------------
	def get_echoCommand(self):
		"""
		
				Specify whether the action attached with
				the c/command flag should echo to the command output
				areas when invoked. This flag is false by default and must be
				specified with the c/command flag.
				
		"""
		return self.query(echoCommand=True)
	#----------------------------------------------------------------------
	def set_echoCommand(self, value):
		"""
		
				Specify whether the action attached with
				the c/command flag should echo to the command output
				areas when invoked. This flag is false by default and must be
				specified with the c/command flag.
				
		"""
		self.edit(echoCommand=value)
	#----------------------------------------------------------------------
	echoCommand = property(get_echoCommand, set_echoCommand)
	#----------------------------------------------------------------------
	def get_enable(self):
		"""
		
				Enable state for the menu item.  A disabled menu item is
				dimmed and unresponsive.  An enabled menu item is selectable and
				has normal appearance.
				
		"""
		return self.query(enable=True)
	#----------------------------------------------------------------------
	def set_enable(self, value):
		"""
		
				Enable state for the menu item.  A disabled menu item is
				dimmed and unresponsive.  An enabled menu item is selectable and
				has normal appearance.
				
		"""
		self.edit(enable=value)
	#----------------------------------------------------------------------
	enable = property(get_enable, set_enable)
	#----------------------------------------------------------------------
	def get_enableCommandRepeat(self):
		"""
		
				This flag only affects menu items to which a command can be
				attached.  Specify true and the command may be repeated by
				executing the command repeatLast.  This flag is true by
				default for all items except for option box items.
				
		"""
		return self.query(enableCommandRepeat=True)
	#----------------------------------------------------------------------
	def set_enableCommandRepeat(self, value):
		"""
		
				This flag only affects menu items to which a command can be
				attached.  Specify true and the command may be repeated by
				executing the command repeatLast.  This flag is true by
				default for all items except for option box items.
				
		"""
		self.edit(enableCommandRepeat=value)
	#----------------------------------------------------------------------
	enableCommandRepeat = property(get_enableCommandRepeat, set_enableCommandRepeat)
	#----------------------------------------------------------------------
	@property
	def familyImage(self):
		"""
		
				Get the filename of the family icon associated with the menu.
				The family icon will be used for the shelf unless an icon is specified with
				the image flag.
				
		"""
		return self.query(familyImage=True)
	#----------------------------------------------------------------------
	def get_image(self):
		"""
		
				The filename of the icon associated with the menu item.  If
				the menu containing the menu item is being edited with a
				menuEditor widget, then the menuEditor will use this icon to
				represent the menu item. This icon will be displayed on the
				shelf when the menu item is placed there.
				
		"""
		return self.query(image=True)
	#----------------------------------------------------------------------
	def set_image(self, value):
		"""
		
				The filename of the icon associated with the menu item.  If
				the menu containing the menu item is being edited with a
				menuEditor widget, then the menuEditor will use this icon to
				represent the menu item. This icon will be displayed on the
				shelf when the menu item is placed there.
				
		"""
		self.edit(image=value)
	#----------------------------------------------------------------------
	image = property(get_image, set_image)
	#----------------------------------------------------------------------
	def get_imageOverlayLabel(self):
		"""
		
				Specify a short (5 character) text string to be overlayed
				on top of the icon associated with the menu item. This is primarily
				a mechanism for differentiating menu items that are using a Family
				icon due to the fact that an icon image had not been explicitly
				defined. The image overlay label will not be used if an icon
				image is defined for the menu item.
				
		"""
		return self.query(imageOverlayLabel=True)
	#----------------------------------------------------------------------
	def set_imageOverlayLabel(self, value):
		"""
		
				Specify a short (5 character) text string to be overlayed
				on top of the icon associated with the menu item. This is primarily
				a mechanism for differentiating menu items that are using a Family
				icon due to the fact that an icon image had not been explicitly
				defined. The image overlay label will not be used if an icon
				image is defined for the menu item.
				
		"""
		self.edit(imageOverlayLabel=value)
	#----------------------------------------------------------------------
	imageOverlayLabel = property(get_imageOverlayLabel, set_imageOverlayLabel)
	#----------------------------------------------------------------------
	@property
	def isCheckBox(self):
		"""
		
				Returns true if the item is a check box item.
				
		"""
		return self.query(isCheckBox=True)
	#----------------------------------------------------------------------
	@property
	def isOptionBox(self):
		"""
		
				Returns true if the item is an option box item.
				
		"""
		return self.query(isOptionBox=True)
	#----------------------------------------------------------------------
	@property
	def isRadioButton(self):
		"""
		
				Returns true if the item is a radio button item.
				
		"""
		return self.query(isRadioButton=True)
	#----------------------------------------------------------------------
	@property
	def italicized(self):
		"""
		
				Specify if text should be italicized. Only supported in menus
				which use the marking menu implementation.  Default is false.
				
		"""
		return self.query(italicized=True)
	#----------------------------------------------------------------------
	def get_label(self):
		"""
		
				The text that appears in the item.
				
		"""
		return self.query(label=True)
	#----------------------------------------------------------------------
	def set_label(self, value):
		"""
		
				The text that appears in the item.
				
		"""
		self.edit(label=value)
	#----------------------------------------------------------------------
	label = property(get_label, set_label)
	#----------------------------------------------------------------------
	def get_longDivider(self):
		"""
		
				Indicate whether the divider is long or short. Has no effect
				if divider label is set. Default is true.
				
		"""
		return self.query(longDivider=True)
	#----------------------------------------------------------------------
	def set_longDivider(self, value):
		"""
		
				Indicate whether the divider is long or short. Has no effect
				if divider label is set. Default is true.
				
		"""
		self.edit(longDivider=value)
	#----------------------------------------------------------------------
	longDivider = property(get_longDivider, set_longDivider)
	#----------------------------------------------------------------------
	def get_ltVersion(self):
		"""
		
				This flag is used to specify the Maya LT version that this control
				feature was introduced, if the version flag is not specified, or
				if the version flag is specified but its argument is different.
				This value is only used by Maya LT, and otherwise ignored.
				The argument should be given as a string of the version number
				(e.g. "2013", "2014"). Currently only accepts major version
				numbers (e.g. 2013 Ext 1, or 2013.5 should be given as "2014").
				
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
				(e.g. "2013", "2014"). Currently only accepts major version
				numbers (e.g. 2013 Ext 1, or 2013.5 should be given as "2014").
				
		"""
		self.edit(ltVersion=value)
	#----------------------------------------------------------------------
	ltVersion = property(get_ltVersion, set_ltVersion)
	#----------------------------------------------------------------------
	@property
	def optionBox(self):
		"""
		
				Indicates that the menu item will be an option box item.  This
				item will appear to the right of the preceeding menu item.
				
		"""
		return self.query(optionBox=True)
	#----------------------------------------------------------------------
	def get_optionBoxIcon(self):
		"""
		
				The filename of an icon to be used instead of the usual option box icon.
				The icon is searched for in the folder specified by the XBMLANGPATH
				environment variable.
				The icon can be any size, but will be resized to the standard 16x16 pixels
				when drawn.
				
		"""
		return self.query(optionBoxIcon=True)
	#----------------------------------------------------------------------
	def set_optionBoxIcon(self, value):
		"""
		
				The filename of an icon to be used instead of the usual option box icon.
				The icon is searched for in the folder specified by the XBMLANGPATH
				environment variable.
				The icon can be any size, but will be resized to the standard 16x16 pixels
				when drawn.
				
		"""
		self.edit(optionBoxIcon=value)
	#----------------------------------------------------------------------
	optionBoxIcon = property(get_optionBoxIcon, set_optionBoxIcon)
	#----------------------------------------------------------------------
	def get_postMenuCommand(self):
		"""
		
				Specify a script to be executed when the submenu is about
				to be shown.
				
		"""
		return self.query(postMenuCommand=True)
	#----------------------------------------------------------------------
	def set_postMenuCommand(self, value):
		"""
		
				Specify a script to be executed when the submenu is about
				to be shown.
				
		"""
		self.edit(postMenuCommand=value)
	#----------------------------------------------------------------------
	postMenuCommand = property(get_postMenuCommand, set_postMenuCommand)
	#----------------------------------------------------------------------
	def get_postMenuCommandOnce(self):
		"""
		
				Indicate the pmc/postMenuCommand should only be
				invoked once.  Default value is false, ie.
				the pmc/postMenuCommand is invoked everytime the sub menu
				is shown.
				
		"""
		return self.query(postMenuCommandOnce=True)
	#----------------------------------------------------------------------
	def set_postMenuCommandOnce(self, value):
		"""
		
				Indicate the pmc/postMenuCommand should only be
				invoked once.  Default value is false, ie.
				the pmc/postMenuCommand is invoked everytime the sub menu
				is shown.
				
		"""
		self.edit(postMenuCommandOnce=value)
	#----------------------------------------------------------------------
	postMenuCommandOnce = property(get_postMenuCommandOnce, set_postMenuCommandOnce)
	#----------------------------------------------------------------------
	def get_radialPosition(self):
		"""
		
				The radial position of the menu item if it is in a Marking
				Menu.  Radial positions are given in the form of a cardinal
				direction, and may be "N", "NW", "W", "SW", "S", "SE", "E" or "NE".
				
		"""
		return self.query(radialPosition=True)
	#----------------------------------------------------------------------
	def set_radialPosition(self, value):
		"""
		
				The radial position of the menu item if it is in a Marking
				Menu.  Radial positions are given in the form of a cardinal
				direction, and may be "N", "NW", "W", "SW", "S", "SE", "E" or "NE".
				
		"""
		self.edit(radialPosition=value)
	#----------------------------------------------------------------------
	radialPosition = property(get_radialPosition, set_radialPosition)
	#----------------------------------------------------------------------
	def get_radioButton(self):
		"""
		
				Creates a radio button menu item.  Argument specifies the
				radio button value.
				
		"""
		return self.query(radioButton=True)
	#----------------------------------------------------------------------
	def set_radioButton(self, value):
		"""
		
				Creates a radio button menu item.  Argument specifies the
				radio button value.
				
		"""
		self.edit(radioButton=value)
	#----------------------------------------------------------------------
	radioButton = property(get_radioButton, set_radioButton)
	#----------------------------------------------------------------------
	def get_sourceType(self):
		"""
		
				Set the language type for a command script. Can only be used in
				conjunction with a command flag.  Without this flag, commands are
				assumed to be the same language of the executing script.  In query
				mode, will return the language of the specified command.
				Valid values are "mel" and "python".
				
		"""
		return self.query(sourceType=True)
	#----------------------------------------------------------------------
	def set_sourceType(self, value):
		"""
		
				Set the language type for a command script. Can only be used in
				conjunction with a command flag.  Without this flag, commands are
				assumed to be the same language of the executing script.  In query
				mode, will return the language of the specified command.
				Valid values are "mel" and "python".
				
		"""
		self.edit(sourceType=value)
	#----------------------------------------------------------------------
	sourceType = property(get_sourceType, set_sourceType)
	#----------------------------------------------------------------------
	@property
	def subMenu(self):
		"""
		
				Indicates that the item will have a submenu.
				Subsequent menuItems will be added to the submenu
				until setParent -menu is called.  Note that a submenu item
				creates a menu object and consequently the menu command may
				be used on the submenu item.
				
		"""
		return self.query(subMenu=True)
	#----------------------------------------------------------------------
	@property
	def tearOff(self):
		"""
		
				For the case where the menu item is a sub menu this flag will
				make the sub menu tear-off-able. Note that this flag has no
				effect on the other menu item types.
				
		"""
		return self.query(tearOff=True)
	#----------------------------------------------------------------------
	def get_version(self):
		"""
		
				Specify the version that this menu item feature was introduced.
				The argument should be given as a string of the version number
				(e.g. "2013", "2014"). Currently only accepts major version
				numbers (e.g. 2013 Ext 1, or 2013.5 should be given as "2014").
				
		"""
		return self.query(version=True)
	#----------------------------------------------------------------------
	def set_version(self, value):
		"""
		
				Specify the version that this menu item feature was introduced.
				The argument should be given as a string of the version number
				(e.g. "2013", "2014"). Currently only accepts major version
				numbers (e.g. 2013 Ext 1, or 2013.5 should be given as "2014").
				
		"""
		self.edit(version=value)
	#----------------------------------------------------------------------
	version = property(get_version, set_version)