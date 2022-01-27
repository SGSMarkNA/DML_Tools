

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class LayerButton(UI_Object.UI):
	"""
	Creates a layer bar button widget.  This widget contains both the name of
	the layer to which it refers and a color swatch indicating it's color
	assignment.  It is used primarily in the construction of the layerBar
	and layer Editor window, being the widget used for each layer in the
	respective lists.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.layerButton(**kwargs)
			super(LayerButton, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.layerButton(name, exists=True):
				super(LayerButton, self).__init__(name)
			else:
				name = cmds.layerButton(name, **kwargs)
				super(LayerButton, self).__init__(name, **dict(qtParent=parent))
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
		
				Set the command to call on a change of any kind.
				
		"""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	def color(self,value):
		"""
		
				Layer color, specified with normalized real numbers in R, G,
				B space.
				
		"""
		self.edit(color=value)
	#----------------------------------------------------------------------
	def command(self,value):
		"""
		
				Set the command to call on a single click.
				
		"""
		self.edit(command=value)
	#----------------------------------------------------------------------
	def current(self,value):
		"""
		
				Set this button to display as the current layer.  The current
				layer is the one which the user has the option of adding all newly
				created objects into.  NB: Setting the layer button to this state
				has no effect on the actual current layer.
				
		"""
		self.edit(current=value)
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
		
				Set the command to call on a double click.
				
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
	def hideOnPlaybackCommand(self,value):
		"""
		
				Command that is called when the hide on playback indicator of
				the layer button is pressed.
				
		"""
		self.edit(hideOnPlaybackCommand=value)
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
	def get_identification(self):
		"""
		
				This is the integer identification number associated with
				the layer.
				
		"""
		return self.query(identification=True)
	#----------------------------------------------------------------------
	def set_identification(self, value):
		"""
		
				This is the integer identification number associated with
				the layer.
				
		"""
		self.edit(identification=value)
	#----------------------------------------------------------------------
	identification = property(get_identification, set_identification)
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
		
				Label text for the button.
				
		"""
		return self.query(label=True)
	#----------------------------------------------------------------------
	def set_label(self, value):
		"""
		
				Label text for the button.
				
		"""
		self.edit(label=value)
	#----------------------------------------------------------------------
	label = property(get_label, set_label)
	#----------------------------------------------------------------------
	@property
	def labelWidth(self):
		"""
		
				Query the width of the label part so as to determine if
				button clicks are in the label part or the colour swatch part.
				
		"""
		return self.query(labelWidth=True)
	#----------------------------------------------------------------------
	def get_layerHideOnPlayback(self):
		"""
		
				Indicates whether the layer is visible or invisible during the playback.
				
		"""
		return self.query(layerHideOnPlayback=True)
	#----------------------------------------------------------------------
	def set_layerHideOnPlayback(self, value):
		"""
		
				Indicates whether the layer is visible or invisible during the playback.
				
		"""
		self.edit(layerHideOnPlayback=value)
	#----------------------------------------------------------------------
	layerHideOnPlayback = property(get_layerHideOnPlayback, set_layerHideOnPlayback)
	#----------------------------------------------------------------------
	def get_layerState(self):
		"""
		
				Describes the state of the layer.  This may be one of
				normal, template, or reference.
				
		"""
		return self.query(layerState=True)
	#----------------------------------------------------------------------
	def set_layerState(self, value):
		"""
		
				Describes the state of the layer.  This may be one of
				normal, template, or reference.
				
		"""
		self.edit(layerState=value)
	#----------------------------------------------------------------------
	layerState = property(get_layerState, set_layerState)
	#----------------------------------------------------------------------
	def get_layerVisible(self):
		"""
		
				Indicates whether the layer is visible or invisible.
				
		"""
		return self.query(layerVisible=True)
	#----------------------------------------------------------------------
	def set_layerVisible(self, value):
		"""
		
				Indicates whether the layer is visible or invisible.
				
		"""
		self.edit(layerVisible=value)
	#----------------------------------------------------------------------
	layerVisible = property(get_layerVisible, set_layerVisible)
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
	def name(self):
		"""
		
				Name of the layer.
				
		"""
		return self.query(name=True)
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
	def renameCommand(self,value):
		"""
		
				Set the command to call when the layer gets renamed. The string
				'#1' will be substituted with the control's name and '#2' will be
				replaced with the layer's new name.
				
		"""
		self.edit(renameCommand=value)
	#----------------------------------------------------------------------
	def get_select(self):
		"""
		
				Set this button to display as a selected layer.
				
		"""
		return self.query(select=True)
	#----------------------------------------------------------------------
	def set_select(self, value):
		"""
		
				Set this button to display as a selected layer.
				
		"""
		self.edit(select=value)
	#----------------------------------------------------------------------
	select = property(get_select, set_select)
	#----------------------------------------------------------------------
	def statusBarMessage(self,value):
		"""
		
				Extra string to display in the status bar when the mouse is over the control.
				
		"""
		self.edit(statusBarMessage=value)
	#----------------------------------------------------------------------
	def get_transparent(self):
		"""
		
				Indicate whether the layer color is visible or transparent.
				
		"""
		return self.query(transparent=True)
	#----------------------------------------------------------------------
	def set_transparent(self, value):
		"""
		
				Indicate whether the layer color is visible or transparent.
				
		"""
		self.edit(transparent=value)
	#----------------------------------------------------------------------
	transparent = property(get_transparent, set_transparent)
	#----------------------------------------------------------------------
	def typeCommand(self,value):
		"""
		
				Command that is called when the type indicator of
				the layer button is pressed.
				
		"""
		self.edit(typeCommand=value)
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
	def visibleCommand(self,value):
		"""
		
				Command that is called when the visibility indicator of
				the layer button is pressed.
				
		"""
		self.edit(visibleCommand=value)
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