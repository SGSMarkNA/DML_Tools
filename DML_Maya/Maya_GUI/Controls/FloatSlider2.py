

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class FloatSlider2(UI_Object.UI):
	"""
	This command creates a float slider containing two handles.
	The two handles are arranged such that they cannot pass one
	another, thus handle 1 will always have a value less than
	or or equal to handle 2 when you adjust the values.
	Each handle may have a MEL command associated with it which is
	issued when the handle moves and thus can be used to update the
	values of plugs such as via a setAttr command. Each handle can
	also be associated with a float textfield to display the current
	value of the handle.
	
	Note: the floatSlider2 widget currently only supports vertical
	(columnLayout) orientation.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.floatSlider2(**kwargs)
			super(FloatSlider2, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.floatSlider2(name, exists=True):
				super(FloatSlider2, self).__init__(name)
			else:
				name = cmds.floatSlider2(name, **kwargs)
				super(FloatSlider2, self).__init__(name, **dict(qtParent=parent))
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
	def changeCommand1(self,value):
		"""
		
				Command to be associated with handle 1 and issued
				whenever the value of the handle is changed (except when values
				are changed via the -hv/handleValue flag). An example command might be
				"setAttr nurbsSphere1.tx" and if handle 1 were to move to
				value 0.23 the slider would issue the command
				"setAttr nurbsSphere1.tx 0.23;".
				
		"""
		self.edit(changeCommand1=value)
	#----------------------------------------------------------------------
	def changeCommand2(self,value):
		"""
		
				Command to be associated with handle 2 and issued
				whenever the value of the handle is changed (except when values
				are changed via the -hv/handleValue flag). An example command might be
				"setAttr nurbsSphere1.tx" and if handle 2 were to move to
				value 0.23 the slider would issue the command
				"setAttr nurbsSphere1.tx 0.23;".
				
		"""
		self.edit(changeCommand2=value)
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
	def get_maximum(self):
		"""
		
				Maximum limit of the slider. The default value is 10.0.
				The maximum value occurs at the top(right) end of the slider
				unless -polarity was specified. Note: you cannot set the
				maximum value greater than or equal to the current minimum.
				
		"""
		return self.query(maximum=True)
	#----------------------------------------------------------------------
	def set_maximum(self, value):
		"""
		
				Maximum limit of the slider. The default value is 10.0.
				The maximum value occurs at the top(right) end of the slider
				unless -polarity was specified. Note: you cannot set the
				maximum value greater than or equal to the current minimum.
				
		"""
		self.edit(maximum=value)
	#----------------------------------------------------------------------
	maximum = property(get_maximum, set_maximum)
	#----------------------------------------------------------------------
	def get_minimum(self):
		"""
		
				Minimum limit of the slider. The default value is 0.0.
				The minimum value occurs at the bottom end of the slider
				unless -polarity was specified. Note: you cannot set the
				minimum value greater than or equal to the current maximum.
				
		"""
		return self.query(minimum=True)
	#----------------------------------------------------------------------
	def set_minimum(self, value):
		"""
		
				Minimum limit of the slider. The default value is 0.0.
				The minimum value occurs at the bottom end of the slider
				unless -polarity was specified. Note: you cannot set the
				minimum value greater than or equal to the current maximum.
				
		"""
		self.edit(minimum=value)
	#----------------------------------------------------------------------
	minimum = property(get_minimum, set_minimum)
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
	def get_polarity(self):
		"""
		
				Specifies the polarity of the slider. If 0 (the default), the minimum
				value (specified by the -minimum flag) occurs at the bottom end of
				the slider and maximum at the top(right), with values increasing as the slider
				handles are moved towards the upper end of the slider. If the polarity
				is specified as 1, the reverse behaviour occurs, with the maximum
				occurring at the bottom end, the mimimum occuring at the top(right) end
				and values decreasing as the handles are moved towards the upper end.
				
		"""
		return self.query(polarity=True)
	#----------------------------------------------------------------------
	def set_polarity(self, value):
		"""
		
				Specifies the polarity of the slider. If 0 (the default), the minimum
				value (specified by the -minimum flag) occurs at the bottom end of
				the slider and maximum at the top(right), with values increasing as the slider
				handles are moved towards the upper end of the slider. If the polarity
				is specified as 1, the reverse behaviour occurs, with the maximum
				occurring at the bottom end, the mimimum occuring at the top(right) end
				and values decreasing as the handles are moved towards the upper end.
				
		"""
		self.edit(polarity=value)
	#----------------------------------------------------------------------
	polarity = property(get_polarity, set_polarity)
	#----------------------------------------------------------------------
	@property
	def popupMenuArray(self):
		"""
		
				Return the names of all the popup menus attached to this
				control.
				
		"""
		return self.query(popupMenuArray=True)
	#----------------------------------------------------------------------
	def positionControl1(self,value):
		"""
		
				Set the name of the control (if any) which is associated with
				handle 1 of this slider. The control must be a "floatField". The
				control always displays the value of the handle, and is updated as
				the handle moves.
				
		"""
		self.edit(positionControl1=value)
	#----------------------------------------------------------------------
	def positionControl2(self,value):
		"""
		
				Set the name of the control (if any) which is associated with
				handle 2 of this slider. The control must be a "floatField". The
				control always displays the value of the handle, and is updated as
				the handle moves.
				
		"""
		self.edit(positionControl2=value)
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
	def get_value1(self):
		"""
		
				Value of handle 1. To ensure that handle 1 stays at
				or below handle 2, an error will occur if the value specified
				is too large. If you wish to set both handles simultaneously,
				use the -values flag.
				
		"""
		return self.query(value1=True)
	#----------------------------------------------------------------------
	def set_value1(self, value):
		"""
		
				Value of handle 1. To ensure that handle 1 stays at
				or below handle 2, an error will occur if the value specified
				is too large. If you wish to set both handles simultaneously,
				use the -values flag.
				
		"""
		self.edit(value1=value)
	#----------------------------------------------------------------------
	value1 = property(get_value1, set_value1)
	#----------------------------------------------------------------------
	def get_value2(self):
		"""
		
				Value of handle 2. To ensure that handle 2 stays at
				or above handle 2, an error will occur if the value specified
				is too large. If you wish to set both handles simultaneously,
				use the -values flag.
				
		"""
		return self.query(value2=True)
	#----------------------------------------------------------------------
	def set_value2(self, value):
		"""
		
				Value of handle 2. To ensure that handle 2 stays at
				or above handle 2, an error will occur if the value specified
				is too large. If you wish to set both handles simultaneously,
				use the -values flag.
				
		"""
		self.edit(value2=value)
	#----------------------------------------------------------------------
	value2 = property(get_value2, set_value2)
	#----------------------------------------------------------------------
	def values(self,value):
		"""
		
				Sets the value for handles 1 and 2 simulteneously. The
				first argument is applied to handle 1 and must be less than
				or equal to the second (handle 2) argument or an error will
				be issued.
				
		"""
		self.edit(values=value)
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