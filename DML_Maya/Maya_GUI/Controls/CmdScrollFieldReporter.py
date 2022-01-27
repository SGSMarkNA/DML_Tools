

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class CmdScrollFieldReporter(UI_Object.UI):
	"""
	A script editor reporter control used to receive and display the history of processed commmands.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.cmdScrollFieldReporter(**kwargs)
			super(CmdScrollFieldReporter, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.cmdScrollFieldReporter(name, exists=True):
				super(CmdScrollFieldReporter, self).__init__(name)
			else:
				name = cmds.cmdScrollFieldReporter(name, **kwargs)
				super(CmdScrollFieldReporter, self).__init__(name, **dict(qtParent=parent))
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
	def clear(self,value):
		"""
		
				Clears the field.
				
		"""
		self.edit(clear=value)
	#----------------------------------------------------------------------
	def copySelection(self,value):
		"""
		
				Copies the current selection from this field.
				
		"""
		self.edit(copySelection=value)
	#----------------------------------------------------------------------
	def cutSelection(self,value):
		"""
		
				Cuts the current selection from this field.
				
		"""
		self.edit(cutSelection=value)
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
	def get_echoAllCommands(self):
		"""
		
				Echo all commands.    (Global parameter, affects all command reporters)
				
		"""
		return self.query(echoAllCommands=True)
	#----------------------------------------------------------------------
	def set_echoAllCommands(self, value):
		"""
		
				Echo all commands.    (Global parameter, affects all command reporters)
				
		"""
		self.edit(echoAllCommands=value)
	#----------------------------------------------------------------------
	echoAllCommands = property(get_echoAllCommands, set_echoAllCommands)
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
	def get_filterSourceType(self):
		"""
		
				Filters the specified source type from showing in this command reporter.
				Currently supports either "mel", "python", or "" (default).
				Setting the filter to the empty string ("") will remove all filtering and show both "mel" and "python" results.
				
		"""
		return self.query(filterSourceType=True)
	#----------------------------------------------------------------------
	def set_filterSourceType(self, value):
		"""
		
				Filters the specified source type from showing in this command reporter.
				Currently supports either "mel", "python", or "" (default).
				Setting the filter to the empty string ("") will remove all filtering and show both "mel" and "python" results.
				
		"""
		self.edit(filterSourceType=value)
	#----------------------------------------------------------------------
	filterSourceType = property(get_filterSourceType, set_filterSourceType)
	#----------------------------------------------------------------------
	@property
	def fullPathName(self):
		"""
		
				Return the full path name of the widget, which includes all the parents.
				
		"""
		return self.query(fullPathName=True)
	#----------------------------------------------------------------------
	@property
	def hasFocus(self):
		"""
		
				Whether this control is currently in focus.
				
		"""
		return self.query(hasFocus=True)
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
	def get_lineNumbers(self):
		"""
		
				Show line numbers (in Error/Warning messages).    (Global parameter, affects all command reporters)
				
		"""
		return self.query(lineNumbers=True)
	#----------------------------------------------------------------------
	def set_lineNumbers(self, value):
		"""
		
				Show line numbers (in Error/Warning messages).    (Global parameter, affects all command reporters)
				
		"""
		self.edit(lineNumbers=value)
	#----------------------------------------------------------------------
	lineNumbers = property(get_lineNumbers, set_lineNumbers)
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
	def pasteSelection(self,value):
		"""
		
				Pastes text into this field at the current caret position.
				
		"""
		self.edit(pasteSelection=value)
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
	def saveSelection(self,value):
		"""
		
				Prompts to save the current selection to a file. The default filename prompt will be prepended with the given string.
				
		"""
		self.edit(saveSelection=value)
	#----------------------------------------------------------------------
	def saveSelectionToShelf(self,value):
		"""
		
				Prompts to save the current selection to an item in the shelf.
				
		"""
		self.edit(saveSelectionToShelf=value)
	#----------------------------------------------------------------------
	def select(self,value):
		"""
		
				Selects text within a specified range.
				
		"""
		self.edit(select=value)
	#----------------------------------------------------------------------
	def selectAll(self,value):
		"""
		
				Selects all text.
				
		"""
		self.edit(selectAll=value)
	#----------------------------------------------------------------------
	def get_stackTrace(self):
		"""
		
				Show stack trace.    (Global parameter, affects all command reporters)
				
		"""
		return self.query(stackTrace=True)
	#----------------------------------------------------------------------
	def set_stackTrace(self, value):
		"""
		
				Show stack trace.    (Global parameter, affects all command reporters)
				
		"""
		self.edit(stackTrace=value)
	#----------------------------------------------------------------------
	stackTrace = property(get_stackTrace, set_stackTrace)
	#----------------------------------------------------------------------
	def statusBarMessage(self,value):
		"""
		
				Extra string to display in the status bar when the mouse is over the control.
				
		"""
		self.edit(statusBarMessage=value)
	#----------------------------------------------------------------------
	def get_suppressErrors(self):
		"""
		
				Suppress errors.
				
		"""
		return self.query(suppressErrors=True)
	#----------------------------------------------------------------------
	def set_suppressErrors(self, value):
		"""
		
				Suppress errors.
				
		"""
		self.edit(suppressErrors=value)
	#----------------------------------------------------------------------
	suppressErrors = property(get_suppressErrors, set_suppressErrors)
	#----------------------------------------------------------------------
	def get_suppressInfo(self):
		"""
		
				Suppress info.
				
		"""
		return self.query(suppressInfo=True)
	#----------------------------------------------------------------------
	def set_suppressInfo(self, value):
		"""
		
				Suppress info.
				
		"""
		self.edit(suppressInfo=value)
	#----------------------------------------------------------------------
	suppressInfo = property(get_suppressInfo, set_suppressInfo)
	#----------------------------------------------------------------------
	def get_suppressResults(self):
		"""
		
				Suppress results.
				
		"""
		return self.query(suppressResults=True)
	#----------------------------------------------------------------------
	def set_suppressResults(self, value):
		"""
		
				Suppress results.
				
		"""
		self.edit(suppressResults=value)
	#----------------------------------------------------------------------
	suppressResults = property(get_suppressResults, set_suppressResults)
	#----------------------------------------------------------------------
	def get_suppressStackTrace(self):
		"""
		
				Suppress stack trace.
				
		"""
		return self.query(suppressStackTrace=True)
	#----------------------------------------------------------------------
	def set_suppressStackTrace(self, value):
		"""
		
				Suppress stack trace.
				
		"""
		self.edit(suppressStackTrace=value)
	#----------------------------------------------------------------------
	suppressStackTrace = property(get_suppressStackTrace, set_suppressStackTrace)
	#----------------------------------------------------------------------
	def get_suppressWarnings(self):
		"""
		
				Suppress warnings.
				
		"""
		return self.query(suppressWarnings=True)
	#----------------------------------------------------------------------
	def set_suppressWarnings(self, value):
		"""
		
				Suppress warnings.
				
		"""
		self.edit(suppressWarnings=value)
	#----------------------------------------------------------------------
	suppressWarnings = property(get_suppressWarnings, set_suppressWarnings)
	#----------------------------------------------------------------------
	def get_text(self):
		"""
		
				Replaces the field text with the given string.
				
		"""
		return self.query(text=True)
	#----------------------------------------------------------------------
	def set_text(self, value):
		"""
		
				Replaces the field text with the given string.
				
		"""
		self.edit(text=value)
	#----------------------------------------------------------------------
	text = property(get_text, set_text)
	#----------------------------------------------------------------------
	@property
	def textLength(self):
		"""
		
				The number of characters in this text field.
				
		"""
		return self.query(textLength=True)
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