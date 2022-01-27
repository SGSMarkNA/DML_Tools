

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class TextField(UI_Object.UI):
	"""
	Create a text field control.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.textField(**kwargs)
			super(TextField, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.textField(name, exists=True):
				super(TextField, self).__init__(name)
			else:
				name = cmds.textField(name, **kwargs)
				super(TextField, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def get_alwaysInvokeEnterCommandOnReturn(self):
		"""
		
				Sets whether to always invoke the enter command when the return key is
				pressed by the user.
				By default, this option is false.
				
		"""
		return self.query(alwaysInvokeEnterCommandOnReturn=True)
	#----------------------------------------------------------------------
	def set_alwaysInvokeEnterCommandOnReturn(self, value):
		"""
		
				Sets whether to always invoke the enter command when the return key is
				pressed by the user.
				By default, this option is false.
				
		"""
		self.edit(alwaysInvokeEnterCommandOnReturn=value)
	#----------------------------------------------------------------------
	alwaysInvokeEnterCommandOnReturn = property(get_alwaysInvokeEnterCommandOnReturn, set_alwaysInvokeEnterCommandOnReturn)
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
		
				Command executed when the text changes.  This command is
				not invoked when the value changes via the -tx/text flag.
				
		"""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	def get_disableButtons(self):
		"""
		
				Sets the visibility state of search field buttons to true/false depending on the passed value.
				In Query mode returns whether both buttons are visible or not.
				
		"""
		return self.query(disableButtons=True)
	#----------------------------------------------------------------------
	def set_disableButtons(self, value):
		"""
		
				Sets the visibility state of search field buttons to true/false depending on the passed value.
				In Query mode returns whether both buttons are visible or not.
				
		"""
		self.edit(disableButtons=value)
	#----------------------------------------------------------------------
	disableButtons = property(get_disableButtons, set_disableButtons)
	#----------------------------------------------------------------------
	def get_disableClearButton(self):
		"""
		
				Sets the visibility state of search field clear button to true/false depending on the passed value.
				In Query mode returns whether clear button of search field is visible or not.
				
		"""
		return self.query(disableClearButton=True)
	#----------------------------------------------------------------------
	def set_disableClearButton(self, value):
		"""
		
				Sets the visibility state of search field clear button to true/false depending on the passed value.
				In Query mode returns whether clear button of search field is visible or not.
				
		"""
		self.edit(disableClearButton=value)
	#----------------------------------------------------------------------
	disableClearButton = property(get_disableClearButton, set_disableClearButton)
	#----------------------------------------------------------------------
	def get_disableHistoryButton(self):
		"""
		
				Sets the visibility state of search field history button to true/false depending on the passed value.
				In Query mode returns whether history button of search field is visible or not.
				
		"""
		return self.query(disableHistoryButton=True)
	#----------------------------------------------------------------------
	def set_disableHistoryButton(self, value):
		"""
		
				Sets the visibility state of search field history button to true/false depending on the passed value.
				In Query mode returns whether history button of search field is visible or not.
				
		"""
		self.edit(disableHistoryButton=value)
	#----------------------------------------------------------------------
	disableHistoryButton = property(get_disableHistoryButton, set_disableHistoryButton)
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
	def get_drawInactiveFrame(self):
		"""
		
				Sets whether the text field draws itself with a frame when it's inactive.
				By default, this option is false.
				
		"""
		return self.query(drawInactiveFrame=True)
	#----------------------------------------------------------------------
	def set_drawInactiveFrame(self, value):
		"""
		
				Sets whether the text field draws itself with a frame when it's inactive.
				By default, this option is false.
				
		"""
		self.edit(drawInactiveFrame=value)
	#----------------------------------------------------------------------
	drawInactiveFrame = property(get_drawInactiveFrame, set_drawInactiveFrame)
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
	def get_editable(self):
		"""
		
				The edit state of the field.  By default, this flag is
				set to true and the field value may be changed by typing into it.
				If false then the field is 'read only' and can not be typed into.
				The text in the field can always be changed with the -tx/text flag
				regardless of the state of the -ed/editable flag.
				
		"""
		return self.query(editable=True)
	#----------------------------------------------------------------------
	def set_editable(self, value):
		"""
		
				The edit state of the field.  By default, this flag is
				set to true and the field value may be changed by typing into it.
				If false then the field is 'read only' and can not be typed into.
				The text in the field can always be changed with the -tx/text flag
				regardless of the state of the -ed/editable flag.
				
		"""
		self.edit(editable=value)
	#----------------------------------------------------------------------
	editable = property(get_editable, set_editable)
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
	def enterCommand(self,value):
		"""
		
				Command executed when the keypad 'Enter' key is pressed.
				
		"""
		self.edit(enterCommand=value)
	#----------------------------------------------------------------------
	def get_fileName(self):
		"""
		
				Text in the field as a filename. This does conversions between
				internal and external (UI) file representation.
				
		"""
		return self.query(fileName=True)
	#----------------------------------------------------------------------
	def set_fileName(self, value):
		"""
		
				Text in the field as a filename. This does conversions between
				internal and external (UI) file representation.
				
		"""
		self.edit(fileName=value)
	#----------------------------------------------------------------------
	fileName = property(get_fileName, set_fileName)
	#----------------------------------------------------------------------
	def get_font(self):
		"""
		
				The font for the text.  Valid values are
				"boldLabelFont", "smallBoldLabelFont", "tinyBoldLabelFont",
				"plainLabelFont", "smallPlainLabelFont", "obliqueLabelFont",
				"smallObliqueLabelFont", "fixedWidthFont" and
				"smallFixedWidthFont".
				
		"""
		return self.query(font=True)
	#----------------------------------------------------------------------
	def set_font(self, value):
		"""
		
				The font for the text.  Valid values are
				"boldLabelFont", "smallBoldLabelFont", "tinyBoldLabelFont",
				"plainLabelFont", "smallPlainLabelFont", "obliqueLabelFont",
				"smallObliqueLabelFont", "fixedWidthFont" and
				"smallFixedWidthFont".
				
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
	def insertText(self,value):
		"""
		
				Insert text into the field at the current insertion
				position (specified by the -ip/insertionPosition flag).
				
		"""
		self.edit(insertText=value)
	#----------------------------------------------------------------------
	def get_insertionPosition(self):
		"""
		
				The insertion position for inserted text.  This is a
				1 based value where position 1 specifies the beginning of the
				field.  Position 0 may be used to specify the end of the field.
				
		"""
		return self.query(insertionPosition=True)
	#----------------------------------------------------------------------
	def set_insertionPosition(self, value):
		"""
		
				The insertion position for inserted text.  This is a
				1 based value where position 1 specifies the beginning of the
				field.  Position 0 may be used to specify the end of the field.
				
		"""
		self.edit(insertionPosition=value)
	#----------------------------------------------------------------------
	insertionPosition = property(get_insertionPosition, set_insertionPosition)
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
	def get_placeholderText(self):
		"""
		
				Setting this property makes the line edit display a grayed-out placeholder text as long as the text field is empty and the widget doesn't have focus.
				By default, this property contains an empty string.
				
		"""
		return self.query(placeholderText=True)
	#----------------------------------------------------------------------
	def set_placeholderText(self, value):
		"""
		
				Setting this property makes the line edit display a grayed-out placeholder text as long as the text field is empty and the widget doesn't have focus.
				By default, this property contains an empty string.
				
		"""
		self.edit(placeholderText=value)
	#----------------------------------------------------------------------
	placeholderText = property(get_placeholderText, set_placeholderText)
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
	def receiveFocusCommand(self,value):
		"""
		
				Command executed when the field receives focus.
				
		"""
		self.edit(receiveFocusCommand=value)
	#----------------------------------------------------------------------
	def statusBarMessage(self,value):
		"""
		
				Extra string to display in the status bar when the mouse is over the control.
				
		"""
		self.edit(statusBarMessage=value)
	#----------------------------------------------------------------------
	def get_text(self):
		"""
		
				The field text.
				
		"""
		return self.query(text=True)
	#----------------------------------------------------------------------
	def set_text(self, value):
		"""
		
				The field text.
				
		"""
		self.edit(text=value)
	#----------------------------------------------------------------------
	text = property(get_text, set_text)
	#----------------------------------------------------------------------
	def textChangedCommand(self,value):
		"""
		
				Command executed immediately when the field text changes.
				
		"""
		self.edit(textChangedCommand=value)
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