

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class ShelfLayout(UI_Object.UI):
	"""
	This command creates a new empty shelf layout.
	The shelf layout can accept drops of commands scripts.
	Use the  MEL command to add a shelf to the top level shelves.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.shelfLayout(**kwargs)
			super(ShelfLayout, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.shelfLayout(name, exists=True):
				super(ShelfLayout, self).__init__(name)
			else:
				name = cmds.shelfLayout(name, **kwargs)
				super(ShelfLayout, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def get_alignment(self):
		"""
		
				Sets the alignment of the buttons in the layout.
				When horizontal is true, valid options are "left" and "right".
				When horizontal is false, valid options are "top" and "bottom".
				
		"""
		return self.query(alignment=True)
	#----------------------------------------------------------------------
	def set_alignment(self, value):
		"""
		
				Sets the alignment of the buttons in the layout.
				When horizontal is true, valid options are "left" and "right".
				When horizontal is false, valid options are "top" and "bottom".
				
		"""
		self.edit(alignment=value)
	#----------------------------------------------------------------------
	alignment = property(get_alignment, set_alignment)
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
		
				Set or query the height of the items in the shelf.
				
		"""
		return self.query(cellHeight=True)
	#----------------------------------------------------------------------
	def set_cellHeight(self, value):
		"""
		
				Set or query the height of the items in the shelf.
				
		"""
		self.edit(cellHeight=value)
	#----------------------------------------------------------------------
	cellHeight = property(get_cellHeight, set_cellHeight)
	#----------------------------------------------------------------------
	def get_cellWidth(self):
		"""
		
				Set or query the width of the items in the shelf.
				
		"""
		return self.query(cellWidth=True)
	#----------------------------------------------------------------------
	def set_cellWidth(self, value):
		"""
		
				Set or query the width of the items in the shelf.
				
		"""
		self.edit(cellWidth=value)
	#----------------------------------------------------------------------
	cellWidth = property(get_cellWidth, set_cellWidth)
	#----------------------------------------------------------------------
	def get_cellWidthHeight(self):
		"""
		
				Set the width and height of the items in the shelf.
				
		"""
		return self.query(cellWidthHeight=True)
	#----------------------------------------------------------------------
	def set_cellWidthHeight(self, value):
		"""
		
				Set the width and height of the items in the shelf.
				
		"""
		self.edit(cellWidthHeight=value)
	#----------------------------------------------------------------------
	cellWidthHeight = property(get_cellWidthHeight, set_cellWidthHeight)
	#----------------------------------------------------------------------
	@property
	def childArray(self):
		"""
		
				Returns a string array of the names of the layout's
				immediate children.
				
		"""
		return self.query(childArray=True)
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
	def get_horizontal(self):
		"""
		
				Orientation of the layout. This flag is true by default, which corresponds to a horizontally laid out shelf.
				
		"""
		return self.query(horizontal=True)
	#----------------------------------------------------------------------
	def set_horizontal(self, value):
		"""
		
				Orientation of the layout. This flag is true by default, which corresponds to a horizontally laid out shelf.
				
		"""
		self.edit(horizontal=value)
	#----------------------------------------------------------------------
	horizontal = property(get_horizontal, set_horizontal)
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
	def position(self,value):
		"""
		
				Specify the name of a child control in the grid layout along with
				a 1-based integer value indicating the desired
				position of the child. Positions increase from left to right
				within a row and then wrap around to the next row increasing from
				top to bottom. For example, a grid layout with 3 columns and 2
				rows has 6 visible positions where 1, 2 and 3 occupy the first row
				and 4, 5 and 6 occupy the second.
				
		"""
		self.edit(position=value)
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
	def get_spacing(self):
		"""
		
				Sets the space between children.
				
		"""
		return self.query(spacing=True)
	#----------------------------------------------------------------------
	def set_spacing(self, value):
		"""
		
				Sets the space between children.
				
		"""
		self.edit(spacing=value)
	#----------------------------------------------------------------------
	spacing = property(get_spacing, set_spacing)
	#----------------------------------------------------------------------
	def statusBarMessage(self,value):
		"""
		
				Extra string to display in the status bar when the mouse is over the control.
				
		"""
		self.edit(statusBarMessage=value)
	#----------------------------------------------------------------------
	def get_style(self):
		"""
		
				Set or query the current style of the items in the shelf.  Valid
				styles are "iconOnly", "textOnly", "iconAndTextHorizontal"
				and "iconAndTextVertical".
				
		"""
		return self.query(style=True)
	#----------------------------------------------------------------------
	def set_style(self, value):
		"""
		
				Set or query the current style of the items in the shelf.  Valid
				styles are "iconOnly", "textOnly", "iconAndTextHorizontal"
				and "iconAndTextVertical".
				
		"""
		self.edit(style=value)
	#----------------------------------------------------------------------
	style = property(get_style, set_style)
	#----------------------------------------------------------------------
	def get_version(self):
		"""
		
				Specify the version that this feature was introduced.
				The argument should be given as a string of the version number
				(e.g. "2014", "2015"). Currently only accepts major version
				numbers (e.g. 2014.5 should be given as "2014").
				
		"""
		return self.query(version=True)
	#----------------------------------------------------------------------
	def set_version(self, value):
		"""
		
				Specify the version that this feature was introduced.
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