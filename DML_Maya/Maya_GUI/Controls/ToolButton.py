

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class ToolButton(UI_Object.UI):
	"""
	This command creates a toolButton that is added to the most recently
	created tool button collection unless the  flag is
	used. It also attaches the named tool, activating it when this control
	is selected.
	
	By default, this control only handles one tool at a time.  Using
	the  flag to associate a new tool will simply override the
	previous attached tool.  If you use the 
	flag then you will be able to attach more than one tool with this
	control.  Only one tool will be current within the control.  To access
	the other tools press the right mouse button to display a popup menu
	containing all the tools associated with this control.  If you set
	the  flag then a small arrow will be
	drawn on the control to indicate that additional tools are attached to
	this control.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.toolButton(**kwargs)
			super(ToolButton, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.toolButton(name, exists=True):
				super(ToolButton, self).__init__(name)
			else:
				name = cmds.toolButton(name, **kwargs)
				super(ToolButton, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def allowMultipleTools(self):
		"""
		
				Indicates whether this control will allow you to attach more
				than one tool.  By default, this control accepts only one tool.
				You can add multiple tools by setting this flag to true.
				Only one tool will be current and displayed at any one time.
				Use the pop up menu attached to the right mouse button to view
				all the tools.
				
		"""
		return self.query(allowMultipleTools=True)
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
	def changeCommand(self,value):
		"""
		
				Command executed when the control's state is changed.
				Note that this flag should not be used in conjunction with
				onCommand and offCommand. That is, one should either use
				changeCommand and test the state of the control from inside
				the callback, or use onCommand and offCommand as separate
				callbacks.
				
		"""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	def collection(self,value):
		"""
		
				To explicitly add a tool button to a tool collection.
				
		"""
		self.edit(collection=value)
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
	def doubleClickCommand(self,value):
		"""
		
				Command executed when the control is double clicked.
				
		"""
		self.edit(doubleClickCommand=value)
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
	def get_image1(self):
		""""""
		return self.query(image1=True)
	#----------------------------------------------------------------------
	def set_image1(self, value):
		""""""
		self.edit(image1=value)
	#----------------------------------------------------------------------
	image1 = property(get_image1, set_image1)
	#----------------------------------------------------------------------
	def get_image2(self):
		""""""
		return self.query(image2=True)
	#----------------------------------------------------------------------
	def set_image2(self, value):
		""""""
		self.edit(image2=value)
	#----------------------------------------------------------------------
	image2 = property(get_image2, set_image2)
	#----------------------------------------------------------------------
	def get_image3(self):
		"""
		
				This control supports three images.  The image that best fits the
				current size of the control will be displayed.  This flag
				applies the image to the current tool.
				
		"""
		return self.query(image3=True)
	#----------------------------------------------------------------------
	def set_image3(self, value):
		"""
		
				This control supports three images.  The image that best fits the
				current size of the control will be displayed.  This flag
				applies the image to the current tool.
				
		"""
		self.edit(image3=value)
	#----------------------------------------------------------------------
	image3 = property(get_image3, set_image3)
	#----------------------------------------------------------------------
	def get_imageOverlayLabel(self):
		"""
		
				A short string (5 characters) label that will be displayed
				on top of the icon.
				
		"""
		return self.query(imageOverlayLabel=True)
	#----------------------------------------------------------------------
	def set_imageOverlayLabel(self, value):
		"""
		
				A short string (5 characters) label that will be displayed
				on top of the icon.
				
		"""
		self.edit(imageOverlayLabel=value)
	#----------------------------------------------------------------------
	imageOverlayLabel = property(get_imageOverlayLabel, set_imageOverlayLabel)
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
	def numberOfPopupMenus(self):
		"""
		
				Return the number of popup menus attached to this control.
				
		"""
		return self.query(numberOfPopupMenus=True)
	#----------------------------------------------------------------------
	def offCommand(self,value):
		"""
		
				Command executed when the control is turned off.
				
		"""
		self.edit(offCommand=value)
	#----------------------------------------------------------------------
	def onCommand(self,value):
		"""
		
				Command executed when the control is turned on.
				
		"""
		self.edit(onCommand=value)
	#----------------------------------------------------------------------
	@property
	def parent(self):
		"""
		
				The parent layout for this control.
				
		"""
		return self.query(parent=True)
	#----------------------------------------------------------------------
	def get_popupIndicatorVisible(self):
		"""
		
				Edit this flag to set the visibility of the popup tool indicator.
				The indicator is a simple image that appears in the top right corner
				of the button when more that one tool is associated with this control.
				This flag is queryable and true by default.
				
		"""
		return self.query(popupIndicatorVisible=True)
	#----------------------------------------------------------------------
	def set_popupIndicatorVisible(self, value):
		"""
		
				Edit this flag to set the visibility of the popup tool indicator.
				The indicator is a simple image that appears in the top right corner
				of the button when more that one tool is associated with this control.
				This flag is queryable and true by default.
				
		"""
		self.edit(popupIndicatorVisible=value)
	#----------------------------------------------------------------------
	popupIndicatorVisible = property(get_popupIndicatorVisible, set_popupIndicatorVisible)
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
	def select(self,value):
		"""
		
				Will set this button as the selected one.  This flag also
				queries the select state of the control.
				
		"""
		self.edit(select=value)
	#----------------------------------------------------------------------
	def statusBarMessage(self,value):
		"""
		
				Extra string to display in the status bar when the mouse is over the control.
				
		"""
		self.edit(statusBarMessage=value)
	#----------------------------------------------------------------------
	def style(self,value):
		"""
		
				The draw style of the control.  Valid styles are "iconOnly",
				"textOnly", "iconAndTextHorizontal" and "iconAndTextVertical".
				
		"""
		self.edit(style=value)
	#----------------------------------------------------------------------
	def get_tool(self):
		"""
		
				The name of the tool to be attached to the button.  If the
				tool specified is already attached to this button then it will
				be selected.  Query this flag to return the current tool.  This
				flag may be specified more than once to attach more than one
				tool.
				
		"""
		return self.query(tool=True)
	#----------------------------------------------------------------------
	def set_tool(self, value):
		"""
		
				The name of the tool to be attached to the button.  If the
				tool specified is already attached to this button then it will
				be selected.  Query this flag to return the current tool.  This
				flag may be specified more than once to attach more than one
				tool.
				
		"""
		self.edit(tool=value)
	#----------------------------------------------------------------------
	tool = property(get_tool, set_tool)
	#----------------------------------------------------------------------
	@property
	def toolArray(self):
		"""
		
				This query only flag returns the names of all the tools attached
				to the toolButton control.
				
		"""
		return self.query(toolArray=True)
	#----------------------------------------------------------------------
	@property
	def toolCount(self):
		"""
		
				This query only flag return the number of tools attached to the
				toolButton control.
				
		"""
		return self.query(toolCount=True)
	#----------------------------------------------------------------------
	def get_toolImage1(self):
		""""""
		return self.query(toolImage1=True)
	#----------------------------------------------------------------------
	def set_toolImage1(self, value):
		""""""
		self.edit(toolImage1=value)
	#----------------------------------------------------------------------
	toolImage1 = property(get_toolImage1, set_toolImage1)
	#----------------------------------------------------------------------
	def get_toolImage2(self):
		""""""
		return self.query(toolImage2=True)
	#----------------------------------------------------------------------
	def set_toolImage2(self, value):
		""""""
		self.edit(toolImage2=value)
	#----------------------------------------------------------------------
	toolImage2 = property(get_toolImage2, set_toolImage2)
	#----------------------------------------------------------------------
	def get_toolImage3(self):
		"""
		
				This control supports three images.  The image that best fits the
				current size of the control will be displayed.  This flag
				applies the image to the specified tool.  The first argument is the
				name of the tool and the second is the name of the image.  When
				queried an array of tool icon pairs is returned.
				
		"""
		return self.query(toolImage3=True)
	#----------------------------------------------------------------------
	def set_toolImage3(self, value):
		"""
		
				This control supports three images.  The image that best fits the
				current size of the control will be displayed.  This flag
				applies the image to the specified tool.  The first argument is the
				name of the tool and the second is the name of the image.  When
				queried an array of tool icon pairs is returned.
				
		"""
		self.edit(toolImage3=value)
	#----------------------------------------------------------------------
	toolImage3 = property(get_toolImage3, set_toolImage3)
	#----------------------------------------------------------------------
	def get_version(self):
		"""
		
				Specify the version that this tool button feature was introduced.
				The argument should be given as a string of the version number
				(e.g. "2013", "2014"). Currently only accepts major version
				numbers (e.g. 2013 Ext 1, or 2013.5 should be given as "2014").
				
		"""
		return self.query(version=True)
	#----------------------------------------------------------------------
	def set_version(self, value):
		"""
		
				Specify the version that this tool button feature was introduced.
				The argument should be given as a string of the version number
				(e.g. "2013", "2014"). Currently only accepts major version
				numbers (e.g. 2013 Ext 1, or 2013.5 should be given as "2014").
				
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