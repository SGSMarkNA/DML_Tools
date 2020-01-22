

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class MenuEditor(UI_Object.UI):
	"""
	A menuEditor displays the contents of a popup menu and allows the
	menu's items to be edited. Menu items are represented by labelled
	icons which can be dragged around within the editor to change the
	menu's layout.  Various objects can be dragged and dropped into
	the menuEditor to create new menu items: toolButtons from the shelf
	or toolbox, shelfButtons from the shelf, iconTextButtons with attached
	commands, and scripts from the command window.
	
	When editing a Marking Menu, the radial menu items correspond to 8
	icons arranged in a circle within the menuEditor.  Overflow items in
	the Marking Menu (or linear items in a normal menu) are displayed in
	a column below the radial items.
	
	To edit a submenu of a popup menu, a new menuEditor instance must be
	created (typically within its own window) and attached to its parent
	menuEditor.
	
	Some flags require the position of a menu item to be passed in as an
	argument.  For these, positions are specified with a (string,int)
	pair, where the string corresponds to a radial position
	(possibily "None") and the int corresponds to a linear position
	(possibly equal to 0 for none).  Radial positions are specified by
	one of ("N",0), ("NE",0), ("E",0), ("SE",0), ("S",0), ("SW",0),
	("W",0) or ("NW",0).  Overflow, or linear positions, are specified
	with ("None",i), where i is a 1-based index giving the position of
	the item within the overflow column. This command is not meant to be called explicitly. It was
	created to support the Marking Menu editor. It is recommended that you
	use that editor to modify marking menus.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.menuEditor(**kwargs)
			super(MenuEditor, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.menuEditor(name, exists=True):
				super(MenuEditor, self).__init__(name)
			else:
				name = cmds.menuEditor(name, **kwargs)
				super(MenuEditor, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def get_annotation(self):
		"""
		
				Annotate the control with an extra string value.
				
		"""
		return self.query(annotation=True)
	#----------------------------------------------------------------------
	def set_annotation(self, value):
		"""
		
				Annotate the control with an extra string value.
				
		"""
		self.edit(annotation=value)
	#----------------------------------------------------------------------
	annotation = property(get_annotation, set_annotation)
	#----------------------------------------------------------------------
	def get_backgroundColor(self):
		"""
		
				The background color of the control. The arguments correspond
				to the red, green, and blue color components. Each component ranges
				in value from 0.0 to 1.0.
				When setting backgroundColor, the background is automatically
				enabled, unless enableBackground is also specified with a false
				value.
				
		"""
		return self.query(backgroundColor=True)
	#----------------------------------------------------------------------
	def set_backgroundColor(self, value):
		"""
		
				The background color of the control. The arguments correspond
				to the red, green, and blue color components. Each component ranges
				in value from 0.0 to 1.0.
				When setting backgroundColor, the background is automatically
				enabled, unless enableBackground is also specified with a false
				value.
				
		"""
		self.edit(backgroundColor=value)
	#----------------------------------------------------------------------
	backgroundColor = property(get_backgroundColor, set_backgroundColor)
	#----------------------------------------------------------------------
	def get_cellHeight(self):
		"""
		
				The height of the icons in the menuEditor.
				
		"""
		return self.query(cellHeight=True)
	#----------------------------------------------------------------------
	def set_cellHeight(self, value):
		"""
		
				The height of the icons in the menuEditor.
				
		"""
		self.edit(cellHeight=value)
	#----------------------------------------------------------------------
	cellHeight = property(get_cellHeight, set_cellHeight)
	#----------------------------------------------------------------------
	def get_cellWidth(self):
		"""
		
				The width of the icons in the menuEditor.
				
		"""
		return self.query(cellWidth=True)
	#----------------------------------------------------------------------
	def set_cellWidth(self, value):
		"""
		
				The width of the icons in the menuEditor.
				
		"""
		self.edit(cellWidth=value)
	#----------------------------------------------------------------------
	cellWidth = property(get_cellWidth, set_cellWidth)
	#----------------------------------------------------------------------
	def cellWidthHeight(self,value):
		"""
		
				The width and height of the icons in the menuEditor.
				
		"""
		self.edit(cellWidthHeight=value)
	#----------------------------------------------------------------------
	def get_checkBoxPresent(self):
		"""
		
				This controls whether a menu item has a check box or not.
				The arguments are a flag indicating presence, followed by the position of the menu item.
				This flag is ignored if the menu item is a submenu item.
				If queried, an array of booleans is returned containing all the flags.
				The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),
				and all later entries correspond to overflow (or linear) menu items.
				
		"""
		return self.query(checkBoxPresent=True)
	#----------------------------------------------------------------------
	def set_checkBoxPresent(self, value):
		"""
		
				This controls whether a menu item has a check box or not.
				The arguments are a flag indicating presence, followed by the position of the menu item.
				This flag is ignored if the menu item is a submenu item.
				If queried, an array of booleans is returned containing all the flags.
				The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),
				and all later entries correspond to overflow (or linear) menu items.
				
		"""
		self.edit(checkBoxPresent=value)
	#----------------------------------------------------------------------
	checkBoxPresent = property(get_checkBoxPresent, set_checkBoxPresent)
	#----------------------------------------------------------------------
	def get_checkBoxState(self):
		"""
		
				The state of the check box associated with a menu item.
				The arguments are a flag indicating state, followed by the position of the menu item.
				This flag is ignored if the menu item does not have a check box.
				If queried, an array of booleans is returned containing all the flags.
				The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),
				and all later entries correspond to overflow (or linear) menu items.
				
		"""
		return self.query(checkBoxState=True)
	#----------------------------------------------------------------------
	def set_checkBoxState(self, value):
		"""
		
				The state of the check box associated with a menu item.
				The arguments are a flag indicating state, followed by the position of the menu item.
				This flag is ignored if the menu item does not have a check box.
				If queried, an array of booleans is returned containing all the flags.
				The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),
				and all later entries correspond to overflow (or linear) menu items.
				
		"""
		self.edit(checkBoxState=value)
	#----------------------------------------------------------------------
	checkBoxState = property(get_checkBoxState, set_checkBoxState)
	#----------------------------------------------------------------------
	@property
	def childArray(self):
		"""
		
				Returns a string array of the names of the layout's
				immediate children.
				
		"""
		return self.query(childArray=True)
	#----------------------------------------------------------------------
	def get_command(self):
		"""
		
				The command or script executed by a menu item.
				The arguments are the command string or script name, followed by the
				position of the menu item. This flag is ignored if the menu item is
				a submenu item or a separator item.
				If queried, an array of strings is returned containing all the commands.
				The first 8 entries of the array correspond to radial items (in
				order, "N", "NE", ... "NW"), and all later entries correspond to
				overflow (or linear) menu items.
				
		"""
		return self.query(command=True)
	#----------------------------------------------------------------------
	def set_command(self, value):
		"""
		
				The command or script executed by a menu item.
				The arguments are the command string or script name, followed by the
				position of the menu item. This flag is ignored if the menu item is
				a submenu item or a separator item.
				If queried, an array of strings is returned containing all the commands.
				The first 8 entries of the array correspond to radial items (in
				order, "N", "NE", ... "NW"), and all later entries correspond to
				overflow (or linear) menu items.
				
		"""
		self.edit(command=value)
	#----------------------------------------------------------------------
	command = property(get_command, set_command)
	#----------------------------------------------------------------------
	def delete(self,value):
		"""
		
				Deletes the menu item at the given position, removing it from
				the menu.  If the menu item has a submenu, and a sub-menuEditor is
				open and attached to it, then the sub-menuEditor's window and
				all its child menuEditor windows will be closed recursively.
				
		"""
		self.edit(delete=value)
	#----------------------------------------------------------------------
	def get_docTag(self):
		"""
		
				Add a documentation flag to the control.  The documentation flag
				has a directory structure.
				(e.g., -dt render/multiLister/createNode/material)
				
		"""
		return self.query(docTag=True)
	#----------------------------------------------------------------------
	def set_docTag(self, value):
		"""
		
				Add a documentation flag to the control.  The documentation flag
				has a directory structure.
				(e.g., -dt render/multiLister/createNode/material)
				
		"""
		self.edit(docTag=value)
	#----------------------------------------------------------------------
	docTag = property(get_docTag, set_docTag)
	#----------------------------------------------------------------------
	def dragCallback(self,value):
		"""
		
				Adds a callback that is called when the middle mouse button
				is pressed.  The MEL version of the callback is of the form:
				
				global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)
				
				The proc returns a string array that is transferred to the drop site.
				By convention the first string in the array describes the user settable
				message type.  Controls that are application defined drag sources may
				ignore the callback. $mods allows testing for the key modifiers CTRL and
				SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL,
				3 == CTRL + SHIFT.
				
				In Python, it is similar, but there are two ways to specify the callback.  The
				recommended way is to pass a Python function object as the argument.  In that
				case, the Python callback should have the form:
				
				def callbackName( dragControl, x, y, modifiers ):
				
				The values of these arguments are the same as those for the MEL version above.
				
				The other way to specify the callback in Python is to specify a string to be
				executed.  In that case, the string will have the values substituted into it
				via the standard Python format operator.  The format values are passed in a
				dictionary with the keys "dragControl", "x", "y", "modifiers".  The
				"dragControl" value is a string and the other values are integers (eg the
				callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")
				
		"""
		self.edit(dragCallback=value)
	#----------------------------------------------------------------------
	def dropCallback(self,value):
		"""
		
				Adds a callback that is called when a drag and drop
				operation is released above the drop site.  The MEL version of the callback is
				of the form:
				
				global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)
				
				The proc receives a string array that is transferred from the drag source.
				The first string in the msgs array describes the user defined message type.
				Controls that are application defined drop sites may ignore the
				callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.
				
				In Python, it is similar, but there are two ways to specify the callback.  The
				recommended way is to pass a Python function object as the argument.  In that
				case, the Python callback should have the form:
				
				def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):
				
				The values of these arguments are the same as those for the MEL version above.
				
				The other way to specify the callback in Python is to specify a string to be
				executed.  In that case, the string will have the values substituted into it
				via the standard Python format operator.  The format values are passed in a
				dictionary with the keys "dragControl", "dropControl", "messages", "x", "y",
				"type".  The "dragControl" value is a string and the other values are integers
				(eg the callback string could be
				"print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")
				
		"""
		self.edit(dropCallback=value)
	#----------------------------------------------------------------------
	def get_enable(self):
		"""
		
				The enable state of the control.  By default, this flag is
				set to true and the control is enabled.  Specify false and the control
				will appear dimmed or greyed-out indicating it is disabled.
				
		"""
		return self.query(enable=True)
	#----------------------------------------------------------------------
	def set_enable(self, value):
		"""
		
				The enable state of the control.  By default, this flag is
				set to true and the control is enabled.  Specify false and the control
				will appear dimmed or greyed-out indicating it is disabled.
				
		"""
		self.edit(enable=value)
	#----------------------------------------------------------------------
	enable = property(get_enable, set_enable)
	#----------------------------------------------------------------------
	def get_enableBackground(self):
		"""
		
				Enables the background color of the control.
				
		"""
		return self.query(enableBackground=True)
	#----------------------------------------------------------------------
	def set_enableBackground(self, value):
		"""
		
				Enables the background color of the control.
				
		"""
		self.edit(enableBackground=value)
	#----------------------------------------------------------------------
	enableBackground = property(get_enableBackground, set_enableBackground)
	#----------------------------------------------------------------------
	def get_enableKeyboardFocus(self):
		"""
		
				If enabled, the user can navigate to the control with the tab key and select values with the keyboard. If not, the user can only use the mouse.
				This flag would typically be used to turn off keyboard focus support from controls that get it by default, like Edit and List controls
				
		"""
		return self.query(enableKeyboardFocus=True)
	#----------------------------------------------------------------------
	def set_enableKeyboardFocus(self, value):
		"""
		
				If enabled, the user can navigate to the control with the tab key and select values with the keyboard. If not, the user can only use the mouse.
				This flag would typically be used to turn off keyboard focus support from controls that get it by default, like Edit and List controls
				
		"""
		self.edit(enableKeyboardFocus=value)
	#----------------------------------------------------------------------
	enableKeyboardFocus = property(get_enableKeyboardFocus, set_enableKeyboardFocus)
	#----------------------------------------------------------------------
	@property
	def fullPathName(self):
		"""
		
				Return the full path name of the widget, which includes all the parents.
				
		"""
		return self.query(fullPathName=True)
	#----------------------------------------------------------------------
	def get_height(self):
		"""
		
				The height of the control.  The control will attempt to
				be this size if it is not overruled by parent layout conditions.
				
		"""
		return self.query(height=True)
	#----------------------------------------------------------------------
	def set_height(self, value):
		"""
		
				The height of the control.  The control will attempt to
				be this size if it is not overruled by parent layout conditions.
				
		"""
		self.edit(height=value)
	#----------------------------------------------------------------------
	height = property(get_height, set_height)
	#----------------------------------------------------------------------
	def get_highlightColor(self):
		"""
		
				The highlight color of the control. The arguments correspond
				to the red, green, and blue color components. Each component ranges
				in value from 0.0 to 1.0.
				
		"""
		return self.query(highlightColor=True)
	#----------------------------------------------------------------------
	def set_highlightColor(self, value):
		"""
		
				The highlight color of the control. The arguments correspond
				to the red, green, and blue color components. Each component ranges
				in value from 0.0 to 1.0.
				
		"""
		self.edit(highlightColor=value)
	#----------------------------------------------------------------------
	highlightColor = property(get_highlightColor, set_highlightColor)
	#----------------------------------------------------------------------
	def get_image(self):
		"""
		
				The filename of the icon associated with a menu item.
				This icon is displayed by the menuEditor to represent the menu item.
				The arguments are the icon filename, followed by the position of the menu item.
				If queried, an array of strings is returned containing all the icon filenames.
				The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),
				and all later entries correspond to overflow (or linear) menu items.
				
		"""
		return self.query(image=True)
	#----------------------------------------------------------------------
	def set_image(self, value):
		"""
		
				The filename of the icon associated with a menu item.
				This icon is displayed by the menuEditor to represent the menu item.
				The arguments are the icon filename, followed by the position of the menu item.
				If queried, an array of strings is returned containing all the icon filenames.
				The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),
				and all later entries correspond to overflow (or linear) menu items.
				
		"""
		self.edit(image=value)
	#----------------------------------------------------------------------
	image = property(get_image, set_image)
	#----------------------------------------------------------------------
	@property
	def isObscured(self):
		"""
		
				Return whether the control can actually be seen by the user.
				The control will be obscured if its state is invisible, if it is
				blocked (entirely or partially) by some other control, if it or a
				parent layout is unmanaged, or if the control's window is
				invisible or iconified.
				
		"""
		return self.query(isObscured=True)
	#----------------------------------------------------------------------
	def get_label(self):
		"""
		
				The label of a menu item.
				The arguments are the label text, followed by the position of the
				menu item. If queried, an array of strings is returned containing
				all the labels. The first 8 entries of the array correspond to radial
				items (in order, "N", "NE", ... "NW"),
				and all later entries correspond to overflow (or linear) menu items.
				
		"""
		return self.query(label=True)
	#----------------------------------------------------------------------
	def set_label(self, value):
		"""
		
				The label of a menu item.
				The arguments are the label text, followed by the position of the
				menu item. If queried, an array of strings is returned containing
				all the labels. The first 8 entries of the array correspond to radial
				items (in order, "N", "NE", ... "NW"),
				and all later entries correspond to overflow (or linear) menu items.
				
		"""
		self.edit(label=value)
	#----------------------------------------------------------------------
	label = property(get_label, set_label)
	#----------------------------------------------------------------------
	def get_manage(self):
		"""
		
				Manage state of the control.  An unmanaged control is
				not visible, nor does it take up any screen real estate.  All
				controls are created managed by default.
				
		"""
		return self.query(manage=True)
	#----------------------------------------------------------------------
	def set_manage(self, value):
		"""
		
				Manage state of the control.  An unmanaged control is
				not visible, nor does it take up any screen real estate.  All
				controls are created managed by default.
				
		"""
		self.edit(manage=value)
	#----------------------------------------------------------------------
	manage = property(get_manage, set_manage)
	#----------------------------------------------------------------------
	@property
	def menuItemTypes(self):
		"""
		
				This is a query only flag.  Returns an array of strings indicating the type of contents in
				each cell of the menuEditor.  Cells can be "vacant", or may contain a regular menu "item",
				or a "separator", or a "submenu" item.  In each case, the corresponding string is returned.
				The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),
				and all later entries correspond to overflow (or linear) menu items.
				
		"""
		return self.query(menuItemTypes=True)
	#----------------------------------------------------------------------
	def noBackground(self,value):
		"""
		
				Clear/reset the control's background.
				Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.
				
		"""
		self.edit(noBackground=value)
	#----------------------------------------------------------------------
	@property
	def numberOfChildren(self):
		"""
		
				Returns in an int the number of immediate children of the layout.
				
		"""
		return self.query(numberOfChildren=True)
	#----------------------------------------------------------------------
	@property
	def numberOfPopupMenus(self):
		"""
		
				Return the number of popup menus attached to this control.
				
		"""
		return self.query(numberOfPopupMenus=True)
	#----------------------------------------------------------------------
	def get_optionBoxCommand(self):
		"""
		
				The command or script executed by a menu item's associated option box item.
				The arguments are the command string or script name, followed by the position of the menu item.
				This flag is ignored if the menu item does not have an associated option box item.
				If queried, an array of strings is returned containing all the commands.
				The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),
				and all later entries correspond to overflow (or linear) menu items.
				
		"""
		return self.query(optionBoxCommand=True)
	#----------------------------------------------------------------------
	def set_optionBoxCommand(self, value):
		"""
		
				The command or script executed by a menu item's associated option box item.
				The arguments are the command string or script name, followed by the position of the menu item.
				This flag is ignored if the menu item does not have an associated option box item.
				If queried, an array of strings is returned containing all the commands.
				The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),
				and all later entries correspond to overflow (or linear) menu items.
				
		"""
		self.edit(optionBoxCommand=value)
	#----------------------------------------------------------------------
	optionBoxCommand = property(get_optionBoxCommand, set_optionBoxCommand)
	#----------------------------------------------------------------------
	def get_optionBoxPresent(self):
		"""
		
				This controls whether a menu item has an associated option box item or not.
				The arguments are a flag indicating presence, followed by the position of the menu item.
				This flag is ignored if the menu item is a submenu item.
				If queried, an array of booleans is returned containing all the flags.
				The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),
				and all later entries correspond to overflow (or linear) menu items.
				
		"""
		return self.query(optionBoxPresent=True)
	#----------------------------------------------------------------------
	def set_optionBoxPresent(self, value):
		"""
		
				This controls whether a menu item has an associated option box item or not.
				The arguments are a flag indicating presence, followed by the position of the menu item.
				This flag is ignored if the menu item is a submenu item.
				If queried, an array of booleans is returned containing all the flags.
				The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),
				and all later entries correspond to overflow (or linear) menu items.
				
		"""
		self.edit(optionBoxPresent=value)
	#----------------------------------------------------------------------
	optionBoxPresent = property(get_optionBoxPresent, set_optionBoxPresent)
	#----------------------------------------------------------------------
	@property
	def parent(self):
		"""
		
				The parent layout for this control.
				
		"""
		return self.query(parent=True)
	#----------------------------------------------------------------------
	@property
	def popupMenuArray(self):
		"""
		
				Return the names of all the popup menus attached to this
				control.
				
		"""
		return self.query(popupMenuArray=True)
	#----------------------------------------------------------------------
	def get_preventOverride(self):
		"""
		
				If true, this flag prevents overriding the control's
				attribute via the control's right mouse button menu.
				
		"""
		return self.query(preventOverride=True)
	#----------------------------------------------------------------------
	def set_preventOverride(self, value):
		"""
		
				If true, this flag prevents overriding the control's
				attribute via the control's right mouse button menu.
				
		"""
		self.edit(preventOverride=value)
	#----------------------------------------------------------------------
	preventOverride = property(get_preventOverride, set_preventOverride)
	#----------------------------------------------------------------------
	def get_radioButtonPresent(self):
		"""
		
				This controls whether a menu item has a radio button or not.
				The arguments are a flag indicating presence, followed by the position of the menu item.
				This flag is ignored if the menu item is a submenu item.
				If queried, an array of booleans is returned containing all the flags.
				The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),
				and all later entries correspond to overflow (or linear) menu items.
				
		"""
		return self.query(radioButtonPresent=True)
	#----------------------------------------------------------------------
	def set_radioButtonPresent(self, value):
		"""
		
				This controls whether a menu item has a radio button or not.
				The arguments are a flag indicating presence, followed by the position of the menu item.
				This flag is ignored if the menu item is a submenu item.
				If queried, an array of booleans is returned containing all the flags.
				The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),
				and all later entries correspond to overflow (or linear) menu items.
				
		"""
		self.edit(radioButtonPresent=value)
	#----------------------------------------------------------------------
	radioButtonPresent = property(get_radioButtonPresent, set_radioButtonPresent)
	#----------------------------------------------------------------------
	def get_radioButtonState(self):
		"""
		
				The state of the radio button associated with a menu item.
				The arguments are a flag indicating state, followed by the position of the menu item.
				This flag is ignored if the menu item does not have a radio button.
				If queried, an array of booleans is returned containing all the flags.
				The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),
				and all later entries correspond to overflow (or linear) menu items.
				
		"""
		return self.query(radioButtonState=True)
	#----------------------------------------------------------------------
	def set_radioButtonState(self, value):
		"""
		
				The state of the radio button associated with a menu item.
				The arguments are a flag indicating state, followed by the position of the menu item.
				This flag is ignored if the menu item does not have a radio button.
				If queried, an array of booleans is returned containing all the flags.
				The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),
				and all later entries correspond to overflow (or linear) menu items.
				
		"""
		self.edit(radioButtonState=value)
	#----------------------------------------------------------------------
	radioButtonState = property(get_radioButtonState, set_radioButtonState)
	#----------------------------------------------------------------------
	def get_separator(self):
		"""
		
				In edit mode this adds a separator to the menuEditor at the
				specified position. The parameters are the radialPosition and the
				overflowRow. If queried, an array of booleans is returned indicating
				if the item is a separator item. The first 8 entries of the array
				correspond to radial items (in order, "N", "NE", ... "NW"),
				and all later entries correspond to overflow (or linear) menu items.
				
		"""
		return self.query(separator=True)
	#----------------------------------------------------------------------
	def set_separator(self, value):
		"""
		
				In edit mode this adds a separator to the menuEditor at the
				specified position. The parameters are the radialPosition and the
				overflowRow. If queried, an array of booleans is returned indicating
				if the item is a separator item. The first 8 entries of the array
				correspond to radial items (in order, "N", "NE", ... "NW"),
				and all later entries correspond to overflow (or linear) menu items.
				
		"""
		self.edit(separator=value)
	#----------------------------------------------------------------------
	separator = property(get_separator, set_separator)
	#----------------------------------------------------------------------
	def statusBarMessage(self,value):
		"""
		
				Extra string to display in the status bar when the mouse is over the control.
				
		"""
		self.edit(statusBarMessage=value)
	#----------------------------------------------------------------------
	def get_style(self):
		"""
		
				This is the style of icons within the menuEditor. Valid styles
				are "iconOnly", "textOnly", "iconAndTextHorizontal"
				and "iconAndTextVertical".
				
		"""
		return self.query(style=True)
	#----------------------------------------------------------------------
	def set_style(self, value):
		"""
		
				This is the style of icons within the menuEditor. Valid styles
				are "iconOnly", "textOnly", "iconAndTextHorizontal"
				and "iconAndTextVertical".
				
		"""
		self.edit(style=value)
	#----------------------------------------------------------------------
	style = property(get_style, set_style)
	#----------------------------------------------------------------------
	def subMenuAt(self,value):
		"""
		
				Creates a submenu item at the given position.  A submenu item
				created within the radial portion of a menu will overwrite whatever
				item (if any) is currently at the given position. A submenu item
				created within the overflow (linear) portion of a menu will be
				inserted before
				the item currently at the given position.
				
		"""
		self.edit(subMenuAt=value)
	#----------------------------------------------------------------------
	@property
	def subMenuEditorsOpen(self):
		"""
		
				This is a query only flag.  Returns an array of booleans, each of which indicates if a
				sub-menuEditor is open and attached to the menu item in a particular cell.  One boolean
				is returned for each cell in the menuEditor, even if the cell is vacant or contains
				a non-submenu item (false will be returned in both these cases).  Only when a cell contains
				a submenu item can true possibily be returned.
				The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),
				and all later entries correspond to overflow (or linear) menu items.
				
		"""
		return self.query(subMenuEditorsOpen=True)
	#----------------------------------------------------------------------
	def get_topLevelMenu(self):
		"""
		
				The popup menu to attach to the editor.  All editing operations
				performed in the editor (i.e. inserting/deleting/moving an item) will
				be immediately reflected in this menu. This flag is ignored if the
				editor is a sub-menuEditor.  The editor will update gracefully if the
				value of the flag is changed from its initial value.
				
		"""
		return self.query(topLevelMenu=True)
	#----------------------------------------------------------------------
	def set_topLevelMenu(self, value):
		"""
		
				The popup menu to attach to the editor.  All editing operations
				performed in the editor (i.e. inserting/deleting/moving an item) will
				be immediately reflected in this menu. This flag is ignored if the
				editor is a sub-menuEditor.  The editor will update gracefully if the
				value of the flag is changed from its initial value.
				
		"""
		self.edit(topLevelMenu=value)
	#----------------------------------------------------------------------
	topLevelMenu = property(get_topLevelMenu, set_topLevelMenu)
	#----------------------------------------------------------------------
	def get_visible(self):
		"""
		
				The visible state of the control.  A control is created
				visible by default.  Note that a control's actual appearance is
				also dependent on the visible state of its parent layout(s).
				
		"""
		return self.query(visible=True)
	#----------------------------------------------------------------------
	def set_visible(self, value):
		"""
		
				The visible state of the control.  A control is created
				visible by default.  Note that a control's actual appearance is
				also dependent on the visible state of its parent layout(s).
				
		"""
		self.edit(visible=value)
	#----------------------------------------------------------------------
	visible = property(get_visible, set_visible)
	#----------------------------------------------------------------------
	def get_visibleChangeCommand(self):
		"""
		
				Command that gets executed when visible state of the control changes.
				
		"""
		return self.query(visibleChangeCommand=True)
	#----------------------------------------------------------------------
	def set_visibleChangeCommand(self, value):
		"""
		
				Command that gets executed when visible state of the control changes.
				
		"""
		self.edit(visibleChangeCommand=value)
	#----------------------------------------------------------------------
	visibleChangeCommand = property(get_visibleChangeCommand, set_visibleChangeCommand)
	#----------------------------------------------------------------------
	def get_width(self):
		"""
		
				The width of the control.  The control will attempt to
				be this size if it is not overruled by parent layout conditions.
				
		"""
		return self.query(width=True)
	#----------------------------------------------------------------------
	def set_width(self, value):
		"""
		
				The width of the control.  The control will attempt to
				be this size if it is not overruled by parent layout conditions.
				
		"""
		self.edit(width=value)
	#----------------------------------------------------------------------
	width = property(get_width, set_width)