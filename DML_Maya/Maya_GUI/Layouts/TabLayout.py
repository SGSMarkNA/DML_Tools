

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class TabLayout(UI_Object.UI):
	"""
	This command creates a tab group. Tab groups are a specialized form of
	control layouts that contain only control layouts.
	Whenever a control layout is added to a tab group it will have a tab
	provided for it that allows selection of that group
	from amongst other tabbed control groups. Only one child of a tab
	layout is visible at a time.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.tabLayout(**kwargs)
			super(TabLayout, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.tabLayout(name, exists=True):
				super(TabLayout, self).__init__(name)
			else:
				name = cmds.tabLayout(name, **kwargs)
				super(TabLayout, self).__init__(name, **dict(qtParent=parent))
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
	def get_borderStyle(self):
		"""
		
				Specify the style of the border for tab layout. Valid values are:
				"none", "top", "notop" and "full". By default, it will use "full" to draw a simple frame
				around the body area of the tab layout.
				
				"none"  - Do not draw borders around the body area of the tab layout
				"top"   - Only draw a simple line right below the tabs
				"notop" - Draw a simple frame on the left/right/bottom (no top) of the tab layout
				"full"  - Draw a simple frame around the body area of the tab layout
				
		"""
		return self.query(borderStyle=True)
	#----------------------------------------------------------------------
	def set_borderStyle(self, value):
		"""
		
				Specify the style of the border for tab layout. Valid values are:
				"none", "top", "notop" and "full". By default, it will use "full" to draw a simple frame
				around the body area of the tab layout.
				
				"none"  - Do not draw borders around the body area of the tab layout
				"top"   - Only draw a simple line right below the tabs
				"notop" - Draw a simple frame on the left/right/bottom (no top) of the tab layout
				"full"  - Draw a simple frame around the body area of the tab layout
				
		"""
		self.edit(borderStyle=value)
	#----------------------------------------------------------------------
	borderStyle = property(get_borderStyle, set_borderStyle)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		"""
		
				Command executed when a tab is selected interactively.
				This command is only invoked when the selected tab changes.
				Re-selecting the current tab will not invoke this command.
				
		"""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	@property
	def childArray(self):
		"""
		
				Returns a string array of the names of the layout's
				immediate children.
				
		"""
		return self.query(childArray=True)
	#----------------------------------------------------------------------
	@property
	def childResizable(self):
		"""
		
				Set to true if you want the child of the control layout to be
				as wide as the scroll area.  You may also indicate a minimum
				width for the child using the -mcw/minChildWidth flag.
				
		"""
		return self.query(childResizable=True)
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
		
				Command executed when a tab is double clicked on.  Note
				that the first click will select the tab and the second click
				will execute the double click command.  Double clicking the
				current tab will re-invoke the double click command.
				
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
	def horizontalScrollBarThickness(self,value):
		"""
		
				Thickness of the horizontal scroll bar.  Specify an
				integer value greater than or equal to zero. This flag has
				no effect on Windows systems.
				
		"""
		self.edit(horizontalScrollBarThickness=value)
	#----------------------------------------------------------------------
	def get_image(self):
		"""
		
				Image appearing in top right corner of tab layout.
				
		"""
		return self.query(image=True)
	#----------------------------------------------------------------------
	def set_image(self, value):
		"""
		
				Image appearing in top right corner of tab layout.
				
		"""
		self.edit(image=value)
	#----------------------------------------------------------------------
	image = property(get_image, set_image)
	#----------------------------------------------------------------------
	def get_imageVisible(self):
		"""
		
				Visibility of tab image.
				
		"""
		return self.query(imageVisible=True)
	#----------------------------------------------------------------------
	def set_imageVisible(self, value):
		"""
		
				Visibility of tab image.
				
		"""
		self.edit(imageVisible=value)
	#----------------------------------------------------------------------
	imageVisible = property(get_imageVisible, set_imageVisible)
	#----------------------------------------------------------------------
	@property
	def innerMarginHeight(self):
		"""
		
				Margin height for all tab children.
				
		"""
		return self.query(innerMarginHeight=True)
	#----------------------------------------------------------------------
	@property
	def innerMarginWidth(self):
		"""
		
				Margin width for all tab children.
				
		"""
		return self.query(innerMarginWidth=True)
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
	def minChildWidth(self):
		"""
		
				Specify a positive non-zero integer value indicating the
				minimum width the tab layout's children.  This flag only has
				meaning when the -cr/childResizable flag is set to true.
				
		"""
		return self.query(minChildWidth=True)
	#----------------------------------------------------------------------
	def moveTab(self,value):
		"""
		
				Move the tab from the current index to a new index.
				
		"""
		self.edit(moveTab=value)
	#----------------------------------------------------------------------
	def newTabCommand(self,value):
		"""
		
				Command executed when the 'New Tab' button (on the tab bar)
				is clicked.  Note: in order to show the new tab button use
				the -snt/showNewTab flag.  Using this command will
				override any internal Maya logic for adding a new tab (only
				this command will be executed).
				
		"""
		self.edit(newTabCommand=value)
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
	def preSelectCommand(self,value):
		"""
		
				Command executed when a tab is selected but before it's
				contents become visible.  Re-selecting the current tab will not
				invoke this command.  Note that this command is not executed by
				using either of the -st/selectTab
				or -sti/selectTabIndex flags.
				
		"""
		self.edit(preSelectCommand=value)
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
	@property
	def scrollable(self):
		"""
		
				Puts all children of this layout within a scroll area.
				
		"""
		return self.query(scrollable=True)
	#----------------------------------------------------------------------
	def get_scrollableTabs(self):
		"""
		
				If true, the active tab in the layout can be scrolled through with the mouse wheel.
				Default is true.
				
		"""
		return self.query(scrollableTabs=True)
	#----------------------------------------------------------------------
	def set_scrollableTabs(self, value):
		"""
		
				If true, the active tab in the layout can be scrolled through with the mouse wheel.
				Default is true.
				
		"""
		self.edit(scrollableTabs=value)
	#----------------------------------------------------------------------
	scrollableTabs = property(get_scrollableTabs, set_scrollableTabs)
	#----------------------------------------------------------------------
	def get_selectCommand(self):
		"""
		
				Command executed when a tab is selected interactively  This
				command will be invoked whenever a tab is selected, ie.
				re-selecting the current tab will invoke this command.  Note that
				this command is not executed by using either of
				the -st/selectTab or -sti/selectTabIndex flags.
				
		"""
		return self.query(selectCommand=True)
	#----------------------------------------------------------------------
	def set_selectCommand(self, value):
		"""
		
				Command executed when a tab is selected interactively  This
				command will be invoked whenever a tab is selected, ie.
				re-selecting the current tab will invoke this command.  Note that
				this command is not executed by using either of
				the -st/selectTab or -sti/selectTabIndex flags.
				
		"""
		self.edit(selectCommand=value)
	#----------------------------------------------------------------------
	selectCommand = property(get_selectCommand, set_selectCommand)
	#----------------------------------------------------------------------
	def get_selectTab(self):
		"""
		
				The name, in short form, of the selected tab.  An empty
				string is returned on query if there are no child tabs.
				
		"""
		return self.query(selectTab=True)
	#----------------------------------------------------------------------
	def set_selectTab(self, value):
		"""
		
				The name, in short form, of the selected tab.  An empty
				string is returned on query if there are no child tabs.
				
		"""
		self.edit(selectTab=value)
	#----------------------------------------------------------------------
	selectTab = property(get_selectTab, set_selectTab)
	#----------------------------------------------------------------------
	def get_selectTabIndex(self):
		"""
		
				Identical to the -st/selectTab flag except this
				flag takes a 1-based index to identify the selected tab.  A value of
				0 is returned on query if there are no child tabs.
				
		"""
		return self.query(selectTabIndex=True)
	#----------------------------------------------------------------------
	def set_selectTabIndex(self, value):
		"""
		
				Identical to the -st/selectTab flag except this
				flag takes a 1-based index to identify the selected tab.  A value of
				0 is returned on query if there are no child tabs.
				
		"""
		self.edit(selectTabIndex=value)
	#----------------------------------------------------------------------
	selectTabIndex = property(get_selectTabIndex, set_selectTabIndex)
	#----------------------------------------------------------------------
	def get_showNewTab(self):
		"""
		
				Set to true if you want to have a 'New Tab' button shown at the end of
				the tab bar.  Note: use the -ntc/newTabCommand flag to set the command
				executed when this button is clicked.
				
		"""
		return self.query(showNewTab=True)
	#----------------------------------------------------------------------
	def set_showNewTab(self, value):
		"""
		
				Set to true if you want to have a 'New Tab' button shown at the end of
				the tab bar.  Note: use the -ntc/newTabCommand flag to set the command
				executed when this button is clicked.
				
		"""
		self.edit(showNewTab=value)
	#----------------------------------------------------------------------
	showNewTab = property(get_showNewTab, set_showNewTab)
	#----------------------------------------------------------------------
	def statusBarMessage(self,value):
		"""
		
				Extra string to display in the status bar when the mouse is over the control.
				
		"""
		self.edit(statusBarMessage=value)
	#----------------------------------------------------------------------
	def get_tabLabel(self):
		"""
		
				Set a tab label.  The first argument is the name of a
				control that must be a child of the tab layout.  The second
				argument is the label for the tab associated with that child.
				If this flag is queried then the tab labels for all the children
				are returned.
				
		"""
		return self.query(tabLabel=True)
	#----------------------------------------------------------------------
	def set_tabLabel(self, value):
		"""
		
				Set a tab label.  The first argument is the name of a
				control that must be a child of the tab layout.  The second
				argument is the label for the tab associated with that child.
				If this flag is queried then the tab labels for all the children
				are returned.
				
		"""
		self.edit(tabLabel=value)
	#----------------------------------------------------------------------
	tabLabel = property(get_tabLabel, set_tabLabel)
	#----------------------------------------------------------------------
	def get_tabLabelIndex(self):
		"""
		
				Identical to the -tl/tabLabel flag except this
				flag takes a 1-based index to identify the tab you want to set the
				label for. If this flag is queried the tab labels for all the
				children are returned.
				
		"""
		return self.query(tabLabelIndex=True)
	#----------------------------------------------------------------------
	def set_tabLabelIndex(self, value):
		"""
		
				Identical to the -tl/tabLabel flag except this
				flag takes a 1-based index to identify the tab you want to set the
				label for. If this flag is queried the tab labels for all the
				children are returned.
				
		"""
		self.edit(tabLabelIndex=value)
	#----------------------------------------------------------------------
	tabLabelIndex = property(get_tabLabelIndex, set_tabLabelIndex)
	#----------------------------------------------------------------------
	def get_tabPosition(self):
		"""
		
				Changes the tab position. The possible values are: "north", "east" and "west".
				
		"""
		return self.query(tabPosition=True)
	#----------------------------------------------------------------------
	def set_tabPosition(self, value):
		"""
		
				Changes the tab position. The possible values are: "north", "east" and "west".
				
		"""
		self.edit(tabPosition=value)
	#----------------------------------------------------------------------
	tabPosition = property(get_tabPosition, set_tabPosition)
	#----------------------------------------------------------------------
	def get_tabTooltip(self):
		"""
		
				Set a tab tooltip.  The first argument is the name of a
				control that must be a child of the tab layout.  The second
				argument is the tooltip for the tab associated with that child.
				If this flag is queried then the tab tooltips for all the children
				are returned.
				
		"""
		return self.query(tabTooltip=True)
	#----------------------------------------------------------------------
	def set_tabTooltip(self, value):
		"""
		
				Set a tab tooltip.  The first argument is the name of a
				control that must be a child of the tab layout.  The second
				argument is the tooltip for the tab associated with that child.
				If this flag is queried then the tab tooltips for all the children
				are returned.
				
		"""
		self.edit(tabTooltip=value)
	#----------------------------------------------------------------------
	tabTooltip = property(get_tabTooltip, set_tabTooltip)
	#----------------------------------------------------------------------
	def get_tabTooltipIndex(self):
		"""
		
				Identical to the -tt/tabTooltip flag except this
				flag takes a 1-based index to identify the tab you want to set the
				tooltip for. If this flag is queried the tab tooltips for all the
				children are returned.
				
		"""
		return self.query(tabTooltipIndex=True)
	#----------------------------------------------------------------------
	def set_tabTooltipIndex(self, value):
		"""
		
				Identical to the -tt/tabTooltip flag except this
				flag takes a 1-based index to identify the tab you want to set the
				tooltip for. If this flag is queried the tab tooltips for all the
				children are returned.
				
		"""
		self.edit(tabTooltipIndex=value)
	#----------------------------------------------------------------------
	tabTooltipIndex = property(get_tabTooltipIndex, set_tabTooltipIndex)
	#----------------------------------------------------------------------
	@property
	def tabsClosable(self):
		"""
		
				Set to true if you want to have a close button icon on all created tabs.
				
		"""
		return self.query(tabsClosable=True)
	#----------------------------------------------------------------------
	def get_tabsVisible(self):
		"""
		
				Visibility of the tab labels.
				
		"""
		return self.query(tabsVisible=True)
	#----------------------------------------------------------------------
	def set_tabsVisible(self, value):
		"""
		
				Visibility of the tab labels.
				
		"""
		self.edit(tabsVisible=value)
	#----------------------------------------------------------------------
	tabsVisible = property(get_tabsVisible, set_tabsVisible)
	#----------------------------------------------------------------------
	def verticalScrollBarThickness(self,value):
		"""
		
				Thickness of the vertical scroll bar.  Specify an
				integer value greater than or equal to zero. This flag has
				no effect on Windows systems.
				
		"""
		self.edit(verticalScrollBarThickness=value)
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