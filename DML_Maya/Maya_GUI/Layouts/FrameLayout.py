

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class FrameLayout(UI_Object.UI):
	"""
	This command creates frame layout control. A frame layout may draw a
	border around its child controls as well as a display a title. Frame
	layouts may also be collapsable. Collapsing a frame layout will make
	the child of the frame layout invisible and shrink the frame layout
	size. The frame layout may then be expanded to make its child visible.
	Note that the frame layout may have only one child control.  If you
	wish to have more than one child inside a frame layout then you must
	use some other control layout as the immediate child of the frame
	layout.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.frameLayout(**kwargs)
			super(FrameLayout, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.frameLayout(name, exists=True):
				super(FrameLayout, self).__init__(name)
			else:
				name = cmds.frameLayout(name, **kwargs)
				super(FrameLayout, self).__init__(name, **dict(qtParent=parent))
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
	def get_backgroundShade(self):
		"""
		
				Controls whether the background of the frame layout draws with a shaded effect. It is turned off by default.
				
		"""
		return self.query(backgroundShade=True)
	#----------------------------------------------------------------------
	def set_backgroundShade(self, value):
		"""
		
				Controls whether the background of the frame layout draws with a shaded effect. It is turned off by default.
				
		"""
		self.edit(backgroundShade=value)
	#----------------------------------------------------------------------
	backgroundShade = property(get_backgroundShade, set_backgroundShade)
	#----------------------------------------------------------------------
	def get_borderStyle(self):
		"""
		
				This flag is obsolete. The border style is no longer supported.
				Using this flag will return a warning.
				
		"""
		return self.query(borderStyle=True)
	#----------------------------------------------------------------------
	def set_borderStyle(self, value):
		"""
		
				This flag is obsolete. The border style is no longer supported.
				Using this flag will return a warning.
				
		"""
		self.edit(borderStyle=value)
	#----------------------------------------------------------------------
	borderStyle = property(get_borderStyle, set_borderStyle)
	#----------------------------------------------------------------------
	def get_borderVisible(self):
		"""
		
				Visibility of the border.
				
		"""
		return self.query(borderVisible=True)
	#----------------------------------------------------------------------
	def set_borderVisible(self, value):
		"""
		
				Visibility of the border.
				
		"""
		self.edit(borderVisible=value)
	#----------------------------------------------------------------------
	borderVisible = property(get_borderVisible, set_borderVisible)
	#----------------------------------------------------------------------
	@property
	def childArray(self):
		"""
		
				Returns a string array of the names of the layout's
				immediate children.
				
		"""
		return self.query(childArray=True)
	#----------------------------------------------------------------------
	def get_collapsable(self):
		"""
		
				Collapsibility of the frame layout.
				
		"""
		return self.query(collapsable=True)
	#----------------------------------------------------------------------
	def set_collapsable(self, value):
		"""
		
				Collapsibility of the frame layout.
				
		"""
		self.edit(collapsable=value)
	#----------------------------------------------------------------------
	collapsable = property(get_collapsable, set_collapsable)
	#----------------------------------------------------------------------
	def get_collapse(self):
		"""
		
				Collapse state of the frame layout.
				
		"""
		return self.query(collapse=True)
	#----------------------------------------------------------------------
	def set_collapse(self, value):
		"""
		
				Collapse state of the frame layout.
				
		"""
		self.edit(collapse=value)
	#----------------------------------------------------------------------
	collapse = property(get_collapse, set_collapse)
	#----------------------------------------------------------------------
	def collapseCommand(self,value):
		"""
		
				Command executed after the frame is collapsed.
				
		"""
		self.edit(collapseCommand=value)
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
	def expandCommand(self,value):
		"""
		
				Command executed after the frame is expanded.
				
		"""
		self.edit(expandCommand=value)
	#----------------------------------------------------------------------
	def get_font(self):
		"""
		
				The font for the frame label.  Valid values are
				"boldLabelFont", "smallBoldLabelFont", "tinyBoldLabelFont",
				"plainLabelFont", "smallPlainLabelFont", "obliqueLabelFont",
				"smallObliqueLabelFont", "fixedWidthFont"
				and "smallFixedWidthFont".
				
		"""
		return self.query(font=True)
	#----------------------------------------------------------------------
	def set_font(self, value):
		"""
		
				The font for the frame label.  Valid values are
				"boldLabelFont", "smallBoldLabelFont", "tinyBoldLabelFont",
				"plainLabelFont", "smallPlainLabelFont", "obliqueLabelFont",
				"smallObliqueLabelFont", "fixedWidthFont"
				and "smallFixedWidthFont".
				
		"""
		self.edit(font=value)
	#----------------------------------------------------------------------
	font = property(get_font, set_font)
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
		
				Label string for the frame layout.
				
		"""
		return self.query(label=True)
	#----------------------------------------------------------------------
	def set_label(self, value):
		"""
		
				Label string for the frame layout.
				
		"""
		self.edit(label=value)
	#----------------------------------------------------------------------
	label = property(get_label, set_label)
	#----------------------------------------------------------------------
	def get_labelAlign(self):
		"""
		
				How to align the label. Default is "top".
				
		"""
		return self.query(labelAlign=True)
	#----------------------------------------------------------------------
	def set_labelAlign(self, value):
		"""
		
				How to align the label. Default is "top".
				
		"""
		self.edit(labelAlign=value)
	#----------------------------------------------------------------------
	labelAlign = property(get_labelAlign, set_labelAlign)
	#----------------------------------------------------------------------
	def get_labelIndent(self):
		"""
		
				Indentation for the frame label.
				
		"""
		return self.query(labelIndent=True)
	#----------------------------------------------------------------------
	def set_labelIndent(self, value):
		"""
		
				Indentation for the frame label.
				
		"""
		self.edit(labelIndent=value)
	#----------------------------------------------------------------------
	labelIndent = property(get_labelIndent, set_labelIndent)
	#----------------------------------------------------------------------
	def get_labelVisible(self):
		"""
		
				Visibility of the frame label.
				
		"""
		return self.query(labelVisible=True)
	#----------------------------------------------------------------------
	def set_labelVisible(self, value):
		"""
		
				Visibility of the frame label.
				
		"""
		self.edit(labelVisible=value)
	#----------------------------------------------------------------------
	labelVisible = property(get_labelVisible, set_labelVisible)
	#----------------------------------------------------------------------
	def get_labelWidth(self):
		"""
		
				Width of the label.
				
		"""
		return self.query(labelWidth=True)
	#----------------------------------------------------------------------
	def set_labelWidth(self, value):
		"""
		
				Width of the label.
				
		"""
		self.edit(labelWidth=value)
	#----------------------------------------------------------------------
	labelWidth = property(get_labelWidth, set_labelWidth)
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
	def get_marginHeight(self):
		"""
		
				Vertical distance between the frame and its children.
				
		"""
		return self.query(marginHeight=True)
	#----------------------------------------------------------------------
	def set_marginHeight(self, value):
		"""
		
				Vertical distance between the frame and its children.
				
		"""
		self.edit(marginHeight=value)
	#----------------------------------------------------------------------
	marginHeight = property(get_marginHeight, set_marginHeight)
	#----------------------------------------------------------------------
	def get_marginWidth(self):
		"""
		
				Horizontal distance between the frame and its children.
				
		"""
		return self.query(marginWidth=True)
	#----------------------------------------------------------------------
	def set_marginWidth(self, value):
		"""
		
				Horizontal distance between the frame and its children.
				
		"""
		self.edit(marginWidth=value)
	#----------------------------------------------------------------------
	marginWidth = property(get_marginWidth, set_marginWidth)
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
	def preCollapseCommand(self,value):
		"""
		
				Command executed just before the frame is collapsed.
				
		"""
		self.edit(preCollapseCommand=value)
	#----------------------------------------------------------------------
	def preExpandCommand(self,value):
		"""
		
				Command executed just before the frame is expanded.
				
		"""
		self.edit(preExpandCommand=value)
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
	def statusBarMessage(self,value):
		"""
		
				Extra string to display in the status bar when the mouse is over the control.
				
		"""
		self.edit(statusBarMessage=value)
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