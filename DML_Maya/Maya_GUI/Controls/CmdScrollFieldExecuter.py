

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class CmdScrollFieldExecuter(UI_Object.UI):
	"""
	A script editor executer control used to issue script commands to
	Maya.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.cmdScrollFieldExecuter(**kwargs)
			super(CmdScrollFieldExecuter, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.cmdScrollFieldExecuter(name, exists=True):
				super(CmdScrollFieldExecuter, self).__init__(name)
			else:
				name = cmds.cmdScrollFieldExecuter(name, **kwargs)
				super(CmdScrollFieldExecuter, self).__init__(name, **dict(qtParent=parent))
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
	def appendText(self,value):
		"""
		
				Appends text to the end of this field.
				
		"""
		self.edit(appendText=value)
	#----------------------------------------------------------------------
	def get_autoCloseBraces(self):
		"""
		
				Specifies whether a closing brace should automatically be added when
				hitting enter after an opening brace. (default on)
				
		"""
		return self.query(autoCloseBraces=True)
	#----------------------------------------------------------------------
	def set_autoCloseBraces(self, value):
		"""
		
				Specifies whether a closing brace should automatically be added when
				hitting enter after an opening brace. (default on)
				
		"""
		self.edit(autoCloseBraces=value)
	#----------------------------------------------------------------------
	autoCloseBraces = property(get_autoCloseBraces, set_autoCloseBraces)
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
	def get_commandCompletion(self):
		"""
		
				Enable/disable command completion
				
		"""
		return self.query(commandCompletion=True)
	#----------------------------------------------------------------------
	def set_commandCompletion(self, value):
		"""
		
				Enable/disable command completion
				
		"""
		self.edit(commandCompletion=value)
	#----------------------------------------------------------------------
	commandCompletion = property(get_commandCompletion, set_commandCompletion)
	#----------------------------------------------------------------------
	def copySelection(self,value):
		"""
		
				Copies the current selection from this field.
				
		"""
		self.edit(copySelection=value)
	#----------------------------------------------------------------------
	def get_currentLine(self):
		"""
		
				Sets/returns the current line which the cursor is on.
				
		"""
		return self.query(currentLine=True)
	#----------------------------------------------------------------------
	def set_currentLine(self, value):
		"""
		
				Sets/returns the current line which the cursor is on.
				
		"""
		self.edit(currentLine=value)
	#----------------------------------------------------------------------
	currentLine = property(get_currentLine, set_currentLine)
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
	def execute(self,value):
		"""
		
				Executes the current selection.  If there is no selection, all text is executed.
				
		"""
		self.edit(execute=value)
	#----------------------------------------------------------------------
	def executeAll(self,value):
		"""
		
				Executes all text.
				
		"""
		self.edit(executeAll=value)
	#----------------------------------------------------------------------
	def fileChangedCommand(self,value):
		"""
		
				Only valid when this field contains a file.
				Sets a script which will be called whenever the file is externally modified,
				renamed or removed from disk.
				In MEL, the function should have the following signature:
				
				proc fileChanged(string $file)
				
		"""
		self.edit(fileChangedCommand=value)
	#----------------------------------------------------------------------
	@property
	def filename(self):
		"""
		
				Returns the full path + filename of the script which was either loaded or saved.
				If there isn't one returns an empty string.
				
		"""
		return self.query(filename=True)
	#----------------------------------------------------------------------
	def get_filterKeyPress(self):
		"""
		
				Sets a script which will be called to handle key-press events.
				The function should have the following signature:
				
				proc int filterKeyPress(int $modifiers, string $key)
				
				modifiers: a bit mask where Shift is bit 1, Ctrl is bit 3,
				Alt is bit 4, and bit 5 is the 'Windows' key on Windows keyboards
				and the Command key on Mac keyboards.
				
				key: Specifies what key was pressed. The key is either a single
				ascii character or one of the keyword strings for the special
				keyboard characters. For example:
				Up, Down, Right, Left,
				Home, End, Page_Up, Page_Down, Insert
				Return, Space
				F1 to F12
				
				The function should return 1 to indicate that they key event has been
				handled, and 0 to indicate that it has not been handled.
				
		"""
		return self.query(filterKeyPress=True)
	#----------------------------------------------------------------------
	def set_filterKeyPress(self, value):
		"""
		
				Sets a script which will be called to handle key-press events.
				The function should have the following signature:
				
				proc int filterKeyPress(int $modifiers, string $key)
				
				modifiers: a bit mask where Shift is bit 1, Ctrl is bit 3,
				Alt is bit 4, and bit 5 is the 'Windows' key on Windows keyboards
				and the Command key on Mac keyboards.
				
				key: Specifies what key was pressed. The key is either a single
				ascii character or one of the keyword strings for the special
				keyboard characters. For example:
				Up, Down, Right, Left,
				Home, End, Page_Up, Page_Down, Insert
				Return, Space
				F1 to F12
				
				The function should return 1 to indicate that they key event has been
				handled, and 0 to indicate that it has not been handled.
				
		"""
		self.edit(filterKeyPress=value)
	#----------------------------------------------------------------------
	filterKeyPress = property(get_filterKeyPress, set_filterKeyPress)
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
	@property
	def hasSelection(self):
		"""
		
				Whether this control currently has a selection or not.
				
		"""
		return self.query(hasSelection=True)
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
		
				Inserts the specified text into the position under the cursor,
				replacing any currently selected text. The selection and cursor
				position can be set using the select flag. Appends text to the
				end of this field.
				
		"""
		self.edit(insertText=value)
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
	def load(self,value):
		"""
		
				Prompts the user for a script to load into this field.  The loaded filename becomes
				associated with this executer field and saving will save directly to the file.
				
		"""
		self.edit(load=value)
	#----------------------------------------------------------------------
	def loadContents(self,value):
		"""
		
				Loads the contents of the specified filename into this field.  The path and extension for this filename
				is provided internally.  This command is only intended for loading the contents of this executer field from a previous
				instance of this executer field.
				
		"""
		self.edit(loadContents=value)
	#----------------------------------------------------------------------
	def loadFile(self,value):
		"""
		
				If the provided string is a fully specified file path, then attempts to load the
				file contents into this field.  If the string is empty or not valid then prompts
				the user for a script to load into this field.  In both cases the filename becomes
				associated with this executer field and saving will save directly to the file.
				
		"""
		self.edit(loadFile=value)
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
	def modificationChangedCommand(self,value):
		"""
		
				Sets a script which will be called whenever the content of this field changes in
				a way that affects the modification state.
				In MEL, the function should have the following signature:
				
				proc modificationChanged(int $m)
				
				If $m is true, the field has been modified; otherwise it is false.
				
		"""
		self.edit(modificationChangedCommand=value)
	#----------------------------------------------------------------------
	def get_modified(self):
		"""
		
				Sets or returns whether the field has been modified.
				
		"""
		return self.query(modified=True)
	#----------------------------------------------------------------------
	def set_modified(self, value):
		"""
		
				Sets or returns whether the field has been modified.
				
		"""
		self.edit(modified=value)
	#----------------------------------------------------------------------
	modified = property(get_modified, set_modified)
	#----------------------------------------------------------------------
	def noBackground(self,value):
		"""
		
				Clear/reset the control's background.
				Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.
				
		"""
		self.edit(noBackground=value)
	#----------------------------------------------------------------------
	@property
	def numberOfLines(self):
		"""
		
				Returns the total number of lines in the document.
				
		"""
		return self.query(numberOfLines=True)
	#----------------------------------------------------------------------
	@property
	def numberOfPopupMenus(self):
		"""
		
				Return the number of popup menus attached to this control.
				
		"""
		return self.query(numberOfPopupMenus=True)
	#----------------------------------------------------------------------
	def get_objectPathCompletion(self):
		"""
		
				Enable/disable path completion
				
		"""
		return self.query(objectPathCompletion=True)
	#----------------------------------------------------------------------
	def set_objectPathCompletion(self, value):
		"""
		
				Enable/disable path completion
				
		"""
		self.edit(objectPathCompletion=value)
	#----------------------------------------------------------------------
	objectPathCompletion = property(get_objectPathCompletion, set_objectPathCompletion)
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
	def redo(self,value):
		"""
		
				Redo the last operation.
				
		"""
		self.edit(redo=value)
	#----------------------------------------------------------------------
	def removeStoredContents(self,value):
		"""
		
				Removes the stored contents of this field with the specified filename.  The path and extension for the file is
				provided internally.  This command is only intended for removing previously stored contents of this executer field.
				
		"""
		self.edit(removeStoredContents=value)
	#----------------------------------------------------------------------
	def replaceAll(self,value):
		"""
		
				Replaces all instances of the first string in the field text with the
				second string.  The case sensitivity of this operation is set with the
				-searchMatchCase flag.
				
		"""
		self.edit(replaceAll=value)
	#----------------------------------------------------------------------
	def saveFile(self,value):
		"""
		
				Saves the entire script contents of this field directly to the specified file path.
				
		"""
		self.edit(saveFile=value)
	#----------------------------------------------------------------------
	def saveSelection(self,value):
		"""
		
				Prompts to save the current selection to a file.  The default filename prompt will be prepended with the given string.
				
		"""
		self.edit(saveSelection=value)
	#----------------------------------------------------------------------
	def saveSelectionToShelf(self,value):
		"""
		
				Prompts to save the current selection to an item in the shelf.
				
		"""
		self.edit(saveSelectionToShelf=value)
	#----------------------------------------------------------------------
	@property
	def searchAndSelect(self):
		"""
		
				Searches for (and selects) the specified search string using the
				specified search options.
				
		"""
		return self.query(searchAndSelect=True)
	#----------------------------------------------------------------------
	def get_searchDown(self):
		"""
		
				Specifies whether to search from the cursor down, or up.
				
		"""
		return self.query(searchDown=True)
	#----------------------------------------------------------------------
	def set_searchDown(self, value):
		"""
		
				Specifies whether to search from the cursor down, or up.
				
		"""
		self.edit(searchDown=value)
	#----------------------------------------------------------------------
	searchDown = property(get_searchDown, set_searchDown)
	#----------------------------------------------------------------------
	def get_searchMatchCase(self):
		"""
		
				Specifies whether the search is to be case sensitive or not.
				
		"""
		return self.query(searchMatchCase=True)
	#----------------------------------------------------------------------
	def set_searchMatchCase(self, value):
		"""
		
				Specifies whether the search is to be case sensitive or not.
				
		"""
		self.edit(searchMatchCase=value)
	#----------------------------------------------------------------------
	searchMatchCase = property(get_searchMatchCase, set_searchMatchCase)
	#----------------------------------------------------------------------
	def get_searchString(self):
		"""
		
				Specifies the string to search for.
				
		"""
		return self.query(searchString=True)
	#----------------------------------------------------------------------
	def set_searchString(self, value):
		"""
		
				Specifies the string to search for.
				
		"""
		self.edit(searchString=value)
	#----------------------------------------------------------------------
	searchString = property(get_searchString, set_searchString)
	#----------------------------------------------------------------------
	def get_searchWraps(self):
		"""
		
				Specifies whether the search should wrap around.
				
		"""
		return self.query(searchWraps=True)
	#----------------------------------------------------------------------
	def set_searchWraps(self, value):
		"""
		
				Specifies whether the search should wrap around.
				
		"""
		self.edit(searchWraps=value)
	#----------------------------------------------------------------------
	searchWraps = property(get_searchWraps, set_searchWraps)
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
	@property
	def selectedText(self):
		"""
		
				The text in the current selection range.
				
		"""
		return self.query(selectedText=True)
	#----------------------------------------------------------------------
	def get_showLineNumbers(self):
		"""
		
				Shows/hides the line numbes column.
				
		"""
		return self.query(showLineNumbers=True)
	#----------------------------------------------------------------------
	def set_showLineNumbers(self, value):
		"""
		
				Shows/hides the line numbes column.
				
		"""
		self.edit(showLineNumbers=value)
	#----------------------------------------------------------------------
	showLineNumbers = property(get_showLineNumbers, set_showLineNumbers)
	#----------------------------------------------------------------------
	def get_showTooltipHelp(self):
		"""
		
				Enable/disable tooltips in the command execution window
				
		"""
		return self.query(showTooltipHelp=True)
	#----------------------------------------------------------------------
	def set_showTooltipHelp(self, value):
		"""
		
				Enable/disable tooltips in the command execution window
				
		"""
		self.edit(showTooltipHelp=value)
	#----------------------------------------------------------------------
	showTooltipHelp = property(get_showTooltipHelp, set_showTooltipHelp)
	#----------------------------------------------------------------------
	def source(self,value):
		"""
		
				Prompts the user for a script to source (execute without loading).
				
		"""
		self.edit(source=value)
	#----------------------------------------------------------------------
	@property
	def sourceType(self):
		"""
		
				Sets the source type for this command executer field.
				Valid values are "mel" (enabled by default)
				and "python".
				
		"""
		return self.query(sourceType=True)
	#----------------------------------------------------------------------
	def get_spacesPerTab(self):
		"""
		
				Specifies the number of spaces equivalent to one tab stop. (default 4)
				
		"""
		return self.query(spacesPerTab=True)
	#----------------------------------------------------------------------
	def set_spacesPerTab(self, value):
		"""
		
				Specifies the number of spaces equivalent to one tab stop. (default 4)
				
		"""
		self.edit(spacesPerTab=value)
	#----------------------------------------------------------------------
	spacesPerTab = property(get_spacesPerTab, set_spacesPerTab)
	#----------------------------------------------------------------------
	def statusBarMessage(self,value):
		"""
		
				Extra string to display in the status bar when the mouse is over the control.
				
		"""
		self.edit(statusBarMessage=value)
	#----------------------------------------------------------------------
	def storeContents(self,value):
		"""
		
				If the provided string is a fully specified file path, then attempts to store the contents of this field
				to that path. Otherwise, uses the provided string as a filename only and uses an internally generated
				path and extension for the file, as used by the -loadContents and -removeStoredContents flags.
				In both cases, a new unique filename will be generated if the specified name exists.
				Returns the filename of the file saved upon completion, and an empty string otherwise.
				
		"""
		self.edit(storeContents=value)
	#----------------------------------------------------------------------
	def get_tabsForIndent(self):
		"""
		
				Specifies whether tab characters should be inserted when indenting. (default on)
				
		"""
		return self.query(tabsForIndent=True)
	#----------------------------------------------------------------------
	def set_tabsForIndent(self, value):
		"""
		
				Specifies whether tab characters should be inserted when indenting. (default on)
				
		"""
		self.edit(tabsForIndent=value)
	#----------------------------------------------------------------------
	tabsForIndent = property(get_tabsForIndent, set_tabsForIndent)
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
	def undo(self,value):
		"""
		
				Undo the last operation.
				
		"""
		self.edit(undo=value)
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