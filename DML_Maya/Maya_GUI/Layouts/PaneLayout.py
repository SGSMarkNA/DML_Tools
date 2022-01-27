

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class PaneLayout(UI_Object.UI):
	"""
	This command creates a pane layout.  A pane layout may have any
	number of children but at any one time only certain children may be
	visible, as determined by the current layout configuration.  For
	example a horizontally split pane shows only two children, one on top
	of the other and a visible separator between the two.  The separator
	may be moved to vary the size of each pane.  Various other pane
	configurations are available and all display a moveable separator
	that define the size of each pane in the layout.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.paneLayout(**kwargs)
			super(PaneLayout, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.paneLayout(name, exists=True):
				super(PaneLayout, self).__init__(name)
			else:
				name = cmds.paneLayout(name, **kwargs)
				super(PaneLayout, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def get_activeFrameThickness(self):
		"""
		
				The thickness of the frame drawn around the active frame.
				Specify an integer value greater than or equal to 0.
				
		"""
		return self.query(activeFrameThickness=True)
	#----------------------------------------------------------------------
	def set_activeFrameThickness(self, value):
		"""
		
				The thickness of the frame drawn around the active frame.
				Specify an integer value greater than or equal to 0.
				
		"""
		self.edit(activeFrameThickness=value)
	#----------------------------------------------------------------------
	activeFrameThickness = property(get_activeFrameThickness, set_activeFrameThickness)
	#----------------------------------------------------------------------
	def get_activePane(self):
		"""
		
				The active pane has a colored border surrounding it.  Only
				one pane may be active at any one time.  Using either of the
				flags -ap/activePane    or -api/activePaneIndex will
				automatically deactivate the previously active pane.  The argument
				is the full or short name of the child control.
				
		"""
		return self.query(activePane=True)
	#----------------------------------------------------------------------
	def set_activePane(self, value):
		"""
		
				The active pane has a colored border surrounding it.  Only
				one pane may be active at any one time.  Using either of the
				flags -ap/activePane    or -api/activePaneIndex will
				automatically deactivate the previously active pane.  The argument
				is the full or short name of the child control.
				
		"""
		self.edit(activePane=value)
	#----------------------------------------------------------------------
	activePane = property(get_activePane, set_activePane)
	#----------------------------------------------------------------------
	def get_activePaneIndex(self):
		"""
		
				The active pane index.  The active pane has a
				colored border surrounding it.  Only one pane may be active
				at any one time.  Using either of the flags -ap/activePane
				or -api/activePaneIndex will automatically deactivate the
				previously active pane.  The argument is an integer
				value ranging from 1 to 4.  Panes for any particular configuration
				are numbered clockwise beginning with the pane in the top left
				corner of the layout.  If any other index is specified then the
				current active pane is deactivated.
				
		"""
		return self.query(activePaneIndex=True)
	#----------------------------------------------------------------------
	def set_activePaneIndex(self, value):
		"""
		
				The active pane index.  The active pane has a
				colored border surrounding it.  Only one pane may be active
				at any one time.  Using either of the flags -ap/activePane
				or -api/activePaneIndex will automatically deactivate the
				previously active pane.  The argument is an integer
				value ranging from 1 to 4.  Panes for any particular configuration
				are numbered clockwise beginning with the pane in the top left
				corner of the layout.  If any other index is specified then the
				current active pane is deactivated.
				
		"""
		self.edit(activePaneIndex=value)
	#----------------------------------------------------------------------
	activePaneIndex = property(get_activePaneIndex, set_activePaneIndex)
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
	@property
	def childArray(self):
		"""
		
				Returns a string array of the names of the layout's
				immediate children.
				
		"""
		return self.query(childArray=True)
	#----------------------------------------------------------------------
	def get_configuration(self):
		"""
		
				Set the layout configuration for the panes.  Valid values
				are:
				"single", "horizontal2", "vertical2", "horizontal3", "vertical3",
				"top3", "left3", "bottom3", "right3", "horizontal4", "vertical4",
				"top4", "left4", "bottom4", "right4", "quad"
				
		"""
		return self.query(configuration=True)
	#----------------------------------------------------------------------
	def set_configuration(self, value):
		"""
		
				Set the layout configuration for the panes.  Valid values
				are:
				"single", "horizontal2", "vertical2", "horizontal3", "vertical3",
				"top3", "left3", "bottom3", "right3", "horizontal4", "vertical4",
				"top4", "left4", "bottom4", "right4", "quad"
				
		"""
		self.edit(configuration=value)
	#----------------------------------------------------------------------
	configuration = property(get_configuration, set_configuration)
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
	def numberOfVisiblePanes(self):
		"""
		
				Return the number of panes visible for the present
				configuration.
				
		"""
		return self.query(numberOfVisiblePanes=True)
	#----------------------------------------------------------------------
	@property
	def pane1(self):
		""""""
		return self.query(pane1=True)
	#----------------------------------------------------------------------
	@property
	def pane2(self):
		""""""
		return self.query(pane2=True)
	#----------------------------------------------------------------------
	@property
	def pane3(self):
		""""""
		return self.query(pane3=True)
	#----------------------------------------------------------------------
	@property
	def pane4(self):
		"""
		
				Return the name of the control in the respective pane.
				
		"""
		return self.query(pane4=True)
	#----------------------------------------------------------------------
	def get_paneSize(self):
		"""
		
				The size of a pane in the current pane layout
				configuration.  The first argument specifies the pane index and
				is an integer value ranging from 1 to 4.  Panes for any particular
				configuration are numbered clockwise beginning with the pane in
				the top left corner of the layout.  The width and height of the
				pane are specified by the last two arguments.  Both are
				integer values and they indicate the percentage of the total
				pane layout size rather that the number of pixels.
				
		"""
		return self.query(paneSize=True)
	#----------------------------------------------------------------------
	def set_paneSize(self, value):
		"""
		
				The size of a pane in the current pane layout
				configuration.  The first argument specifies the pane index and
				is an integer value ranging from 1 to 4.  Panes for any particular
				configuration are numbered clockwise beginning with the pane in
				the top left corner of the layout.  The width and height of the
				pane are specified by the last two arguments.  Both are
				integer values and they indicate the percentage of the total
				pane layout size rather that the number of pixels.
				
		"""
		self.edit(paneSize=value)
	#----------------------------------------------------------------------
	paneSize = property(get_paneSize, set_paneSize)
	#----------------------------------------------------------------------
	@property
	def paneUnderPointer(self):
		"""
		
				Return the name of the child occupying the
				pane that the pointer is currently over.  An empty string is
				returned if the pointer is not over a pane.
				
		"""
		return self.query(paneUnderPointer=True)
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
	def separatorMovedCommand(self,value):
		"""
		
				This command executed when the pane separators are moved.
				
		"""
		self.edit(separatorMovedCommand=value)
	#----------------------------------------------------------------------
	def get_separatorThickness(self):
		"""
		
				The thickness of the separators between the panes.
				Specify an integer value greater than 0. This flag has no effect
				on Windows systems.
				
		"""
		return self.query(separatorThickness=True)
	#----------------------------------------------------------------------
	def set_separatorThickness(self, value):
		"""
		
				The thickness of the separators between the panes.
				Specify an integer value greater than 0. This flag has no effect
				on Windows systems.
				
		"""
		self.edit(separatorThickness=value)
	#----------------------------------------------------------------------
	separatorThickness = property(get_separatorThickness, set_separatorThickness)
	#----------------------------------------------------------------------
	def setPane(self,value):
		"""
		
				This flag allows you to put a child of this layout in a
				particular pane.  The first argument is the full or short name of
				the control.  The second argument is an integer value ranging from
				1 to 4.  Panes for any particular configuration are numbered
				clockwise beginning with the pane in the top left corner of the
				layout.
				
		"""
		self.edit(setPane=value)
	#----------------------------------------------------------------------
	def staticHeightPane(self,value):
		"""
		
				Set a pane to have a static height, i.e. its height will not
				change when the layout is dynamically resized. Only one pane
				can be set to have a static height at one time. This state
				will be retained even if another child is switched into the
				pane. Specify 0 to set a pane back to the default state. Any
				state will be lost if the pane configuration is changed.
				
		"""
		self.edit(staticHeightPane=value)
	#----------------------------------------------------------------------
	def staticWidthPane(self,value):
		"""
		
				Set a pane to have a static width, i.e. its width will not
				change when the layout is dynamically resized. Only one pane
				can be set to have a static width at one time. This state
				will be retained even if another child is switched into the
				pane. Specify 0 to set a pane back to the default state. Any
				state will be lost if the pane configuration is changed.
				
		"""
		self.edit(staticWidthPane=value)
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