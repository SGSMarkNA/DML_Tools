

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class ScriptTable(UI_Object.UI):
	"""
	This command creates/edits/queries the script table control.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.scriptTable(**kwargs)
			super(ScriptTable, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.scriptTable(name, exists=True):
				super(ScriptTable, self).__init__(name)
			else:
				name = cmds.scriptTable(name, **kwargs)
				super(ScriptTable, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def afterCellChangedCmd(self,value):
		"""
		
				Sets the script to call after the value of a cell has been
				changed. The procedure is called with
				2 integer arguments specifying the row and column for
				which the value was changed. The 3rd argument is the string
				which was entered into that cell. The procedure does not need to
				return any value.
				The row and column numbers passed in are 1-based
				(i.e. (1,1) is the upper left cell). The procedure should be
				of the form:
				
				global proc procedureName(int $row, int $column, string $value)
				
		"""
		self.edit(afterCellChangedCmd=value)
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
	def cellBackgroundColorCommand(self,value):
		"""
		
				Sets the script to call when it requires
				the background color of a cell.
				The procedure is called with
				2 integer arguments specifying the row and column for
				which the value is required. The procedure should return
				an array of ints which is the RGB color value for the cell.
				The row and column numbers passed in are 1-based
				(i.e. (1,1) is the upper left cell).
				The procedure should be of the form:
				
				global proc int[] procedureName(int $row, int $column) {
				return {255,0,0}; // return Red as cell background color
				}
				
		"""
		self.edit(cellBackgroundColorCommand=value)
	#----------------------------------------------------------------------
	def cellChangedCmd(self,value):
		"""
		
				Sets the script to call when somebody has
				changed the value of a cell. The procedure is called with
				2 integer arguments specifying the row and column for
				which the value was changed. The 3rd argument is the string
				which was entered into that cell. The procedure should return
				an integer value which indicates whether that value should be
				accepted (return 1 if yes, and 0 if no).
				The row and column numbers passed in are 1-based
				(i.e. (1,1) is the upper left cell). The procedure should be
				of the form:
				
				global proc int procedureName(int $row, int $column, string $value)
				
		"""
		self.edit(cellChangedCmd=value)
	#----------------------------------------------------------------------
	def cellForegroundColorCommand(self,value):
		"""
		
				Sets the script to call when it requires
				the foreground color of a cell.
				The procedure is called with
				2 integer arguments specifying the row and column for
				which the value is required. The procedure should return
				an array of ints which is the RGB color value for the cell.
				The row and column numbers passed in are 1-based
				(i.e. (1,1) is the upper left cell).
				The procedure should be of the form:
				
				global proc int[] procedureName(int $row, int $column) {
				return {0,0,0}; // return Black as Text color
				}
				
		"""
		self.edit(cellForegroundColorCommand=value)
	#----------------------------------------------------------------------
	def get_cellIndex(self):
		"""
		
				used with cellValue , to give the index of row and column
				This flag and its argument must be passed to the command before the
				-q flag (see examples).
				      In query mode, this flag needs a value.
				
		"""
		return self.query(cellIndex=True)
	#----------------------------------------------------------------------
	def set_cellIndex(self, value):
		"""
		
				used with cellValue , to give the index of row and column
				This flag and its argument must be passed to the command before the
				-q flag (see examples).
				      In query mode, this flag needs a value.
				
		"""
		self.edit(cellIndex=value)
	#----------------------------------------------------------------------
	cellIndex = property(get_cellIndex, set_cellIndex)
	#----------------------------------------------------------------------
	def get_cellValue(self):
		"""
		
				query and set the cell value on the table by the index of row and column referred in
				flag -cellIndex.
				In edit mode, if flag -multiEditEnabled is True and any cell is selected,
				the flag -cellIndex is not used and the selected cells will be changed.
				
		"""
		return self.query(cellValue=True)
	#----------------------------------------------------------------------
	def set_cellValue(self, value):
		"""
		
				query and set the cell value on the table by the index of row and column referred in
				flag -cellIndex.
				In edit mode, if flag -multiEditEnabled is True and any cell is selected,
				the flag -cellIndex is not used and the selected cells will be changed.
				
		"""
		self.edit(cellValue=value)
	#----------------------------------------------------------------------
	cellValue = property(get_cellValue, set_cellValue)
	#----------------------------------------------------------------------
	def clearRow(self,value):
		"""
		
				Clear the contents for all the cells on the specified
				row. Any procedure specified by the -gcc flag will be
				called to populate the cleared cells
				The row number is 1-based (i.e. the first row is 1 not 0).
				
		"""
		self.edit(clearRow=value)
	#----------------------------------------------------------------------
	def clearTable(self,value):
		"""
		
				Clears the contents of all the cells in the table.
				Any procedure specified by the -gcc flag will be
				called to populate the cleared cells
				
		"""
		self.edit(clearTable=value)
	#----------------------------------------------------------------------
	def columnFilter(self,value):
		"""
		
				Filter the specified column with the string value provided.
				Set filter to columns 0 will apply the filter to all columns.
				The filter is case insensitive and support wildcards.
				Wildcard Matching: Wildcard matching is much simpler than full regexps and has only four features:
				c	Any character represents itself apart from those mentioned below. Thus c matches the character c.
				?	Matches any single character. It is the same as . in full regexps.
				*	Matches zero or more of any characters. It is the same as .* in full regexps.
				[...]	Sets of characters can be represented in square brackets, similar to full regexps.
				Within the character class, backslash has no special meaning.
				(i.e. you can search for "MyValue" with "y*u" or "??Val??" or "[MyThe]Value" or any letters in "MyValue"
				The column number is 1-based (i.e. the first row is 1 not 0).
				
		"""
		self.edit(columnFilter=value)
	#----------------------------------------------------------------------
	def columnWidth(self,value):
		"""
		
				Set the width of the specified column
				The column number is 1-based (ie. the first column is 1 not 0).
				
		"""
		self.edit(columnWidth=value)
	#----------------------------------------------------------------------
	def get_columns(self):
		"""
		
				Set the number of columns in the table
				
		"""
		return self.query(columns=True)
	#----------------------------------------------------------------------
	def set_columns(self, value):
		"""
		
				Set the number of columns in the table
				
		"""
		self.edit(columns=value)
	#----------------------------------------------------------------------
	columns = property(get_columns, set_columns)
	#----------------------------------------------------------------------
	def deleteRow(self,value):
		"""
		
				Delete the specified row
				The row number is 1-based (i.e. the first row is 1 not 0).
				
		"""
		self.edit(deleteRow=value)
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
	def get_editable(self):
		"""
		
				The edit state of the table.
				By default, this flag is set to true, and the table can be edited.
				If false, then the table is 'read only' and cannot be typed into.
				
		"""
		return self.query(editable=True)
	#----------------------------------------------------------------------
	def set_editable(self, value):
		"""
		
				The edit state of the table.
				By default, this flag is set to true, and the table can be edited.
				If false, then the table is 'read only' and cannot be typed into.
				
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
	@property
	def excludingHeaders(self):
		"""
		
				when querying the count for the rows or the columns , the number returned will not include the headers
				
		"""
		return self.query(excludingHeaders=True)
	#----------------------------------------------------------------------
	@property
	def fullPathName(self):
		"""
		
				Return the full path name of the widget, which includes all the parents.
				
		"""
		return self.query(fullPathName=True)
	#----------------------------------------------------------------------
	def getCellCmd(self,value):
		"""
		
				Sets the script to call when it requires
				the contents of a cell. The procedure is called with
				2 integer arguments specifying the row and column for
				which the value is required. The procedure should return
				a string which is the value for the cell.
				The row and column numbers passed in are 1-based
				(ie. (1,1) is the upper left cell). The procedure should be
				of the form:
				
				global proc string procedureName(int $row, int $column)
				
		"""
		self.edit(getCellCmd=value)
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
	def insertRow(self,value):
		"""
		
				Insert an empty row before the specified row. Any
				procedure specified by the -gcc flag will be called to
				populate the new new cells.
				The row number is 1-based (i.e. the first row is 1 not 0).
				
		"""
		self.edit(insertRow=value)
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
	def label(self,value):
		"""
		
				Set the label of the specified column.
				The column number is 1-based (ie. the first column is 1 not 0).
				
		"""
		self.edit(label=value)
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
	def get_multiEditEnabled(self):
		"""
		
				True: scriptTable support multi-editing function
				
		"""
		return self.query(multiEditEnabled=True)
	#----------------------------------------------------------------------
	def set_multiEditEnabled(self, value):
		"""
		
				True: scriptTable support multi-editing function
				
		"""
		self.edit(multiEditEnabled=value)
	#----------------------------------------------------------------------
	multiEditEnabled = property(get_multiEditEnabled, set_multiEditEnabled)
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
	def get_rowHeight(self):
		"""
		
				Sets the height for each row in the scriptTable
				
		"""
		return self.query(rowHeight=True)
	#----------------------------------------------------------------------
	def set_rowHeight(self, value):
		"""
		
				Sets the height for each row in the scriptTable
				
		"""
		self.edit(rowHeight=value)
	#----------------------------------------------------------------------
	rowHeight = property(get_rowHeight, set_rowHeight)
	#----------------------------------------------------------------------
	def get_rows(self):
		"""
		
				Set the number of rows in the table
				
		"""
		return self.query(rows=True)
	#----------------------------------------------------------------------
	def set_rows(self, value):
		"""
		
				Set the number of rows in the table
				
		"""
		self.edit(rows=value)
	#----------------------------------------------------------------------
	rows = property(get_rows, set_rows)
	#----------------------------------------------------------------------
	def rowsRemovedCmd(self,value):
		"""
		
				Sets the script to call after rows are removed by pressing 'delete' or
				'backspace' key. The procedure is called with one argument
				specifying that selected rows have been removed.
				The rows passed in are 1-based. The procedure should be
				of the form:
				
				global proc procedureName(int $rows[])
				
		"""
		self.edit(rowsRemovedCmd=value)
	#----------------------------------------------------------------------
	def rowsToBeRemovedCmd(self,value):
		"""
		
				Sets the script to call when 'delete' or 'backspace' key is
				pressed. The procedure is called with one argument
				specifying the selected rows to be removed. The procedure
				should return an integer value which indicates whether the
				selected rows should be removed (return 1 if yes, and 0 if no).
				The rows passed in are 1-based. The procedure should be
				of the form:
				
				global proc int procedureName(int $rows[])
				
		"""
		self.edit(rowsToBeRemovedCmd=value)
	#----------------------------------------------------------------------
	def get_selectedCells(self):
		"""
		
				Select the cells or return  the cells currently selected.
				This returns a list of indices, the first of each pair is the row, the second is the column, repeated for each cell selected
				The returned cell numbers are 1-based (ie. the first row is 1 not 0, the first column is 1 not 0).
				
		"""
		return self.query(selectedCells=True)
	#----------------------------------------------------------------------
	def set_selectedCells(self, value):
		"""
		
				Select the cells or return  the cells currently selected.
				This returns a list of indices, the first of each pair is the row, the second is the column, repeated for each cell selected
				The returned cell numbers are 1-based (ie. the first row is 1 not 0, the first column is 1 not 0).
				
		"""
		self.edit(selectedCells=value)
	#----------------------------------------------------------------------
	selectedCells = property(get_selectedCells, set_selectedCells)
	#----------------------------------------------------------------------
	def get_selectedColumns(self):
		"""
		
				select the columns or return the columns currently selected.
				This returns a list of indices of each column completely selected
				The returned column numbers are 1-based
				
		"""
		return self.query(selectedColumns=True)
	#----------------------------------------------------------------------
	def set_selectedColumns(self, value):
		"""
		
				select the columns or return the columns currently selected.
				This returns a list of indices of each column completely selected
				The returned column numbers are 1-based
				
		"""
		self.edit(selectedColumns=value)
	#----------------------------------------------------------------------
	selectedColumns = property(get_selectedColumns, set_selectedColumns)
	#----------------------------------------------------------------------
	@property
	def selectedRow(self):
		"""
		
				The current row selected.
				The returned row number is 1-based (ie. the first row is 1 not 0).
				
		"""
		return self.query(selectedRow=True)
	#----------------------------------------------------------------------
	def get_selectedRows(self):
		"""
		
				In edit mode, select the rows given as argument.
				In query mode, return a list of indices of completely selected rows.
				The row numbers are 1-based
				
		"""
		return self.query(selectedRows=True)
	#----------------------------------------------------------------------
	def set_selectedRows(self, value):
		"""
		
				In edit mode, select the rows given as argument.
				In query mode, return a list of indices of completely selected rows.
				The row numbers are 1-based
				
		"""
		self.edit(selectedRows=value)
	#----------------------------------------------------------------------
	selectedRows = property(get_selectedRows, set_selectedRows)
	#----------------------------------------------------------------------
	def get_selectionBehavior(self):
		"""
		
				Set the selection behavior, valid values are from 0 to 2 (inclusive)
				0 - Selecting single items.
				1 - Selecting only rows.
				2 - Selecting only columns.
				
		"""
		return self.query(selectionBehavior=True)
	#----------------------------------------------------------------------
	def set_selectionBehavior(self, value):
		"""
		
				Set the selection behavior, valid values are from 0 to 2 (inclusive)
				0 - Selecting single items.
				1 - Selecting only rows.
				2 - Selecting only columns.
				
		"""
		self.edit(selectionBehavior=value)
	#----------------------------------------------------------------------
	selectionBehavior = property(get_selectionBehavior, set_selectionBehavior)
	#----------------------------------------------------------------------
	def selectionChangedCmd(self,value):
		"""
		
				Sets the script to call when a complete selection
				operation triggered by the user has occurred successfully.
				The script does not pass any parameters and does not need to
				return any value (i.e. It is simply a notification mechanism).
				
		"""
		self.edit(selectionChangedCmd=value)
	#----------------------------------------------------------------------
	def get_selectionMode(self):
		"""
		
				Set the selection Mode, valid values are from 0 to 4 (inclusive)
				0 - Items cannot be selected.
				1 - When the user selects an item, any already-selected item becomes unselected, and the user cannot unselect the selected item by clicking on it.
				2 - When the user selects an item in the usual way, the selection status of that item is toggled and the other items are left alone. Multiple items can be toggled by dragging the mouse over them.
				3 - When the user selects an item in the usual way, the selection is cleared and the new item selected. However, if the user presses the Ctrl key when clicking on an item, the clicked item gets toggled and all other items are left untouched. If the user presses the Shift key while clicking on an item, all items between the current item and the clicked item are selected or unselected, depending on the state of the clicked item. Multiple items can be selected by dragging the mouse over them.
				4 - When the user selects an item in the usual way, the selection is cleared and the new item selected. However, if the user presses the Shift key while clicking on an item, all items between the current item and the clicked item are selected or unselected, depending on the state of the clicked item.
				
		"""
		return self.query(selectionMode=True)
	#----------------------------------------------------------------------
	def set_selectionMode(self, value):
		"""
		
				Set the selection Mode, valid values are from 0 to 4 (inclusive)
				0 - Items cannot be selected.
				1 - When the user selects an item, any already-selected item becomes unselected, and the user cannot unselect the selected item by clicking on it.
				2 - When the user selects an item in the usual way, the selection status of that item is toggled and the other items are left alone. Multiple items can be toggled by dragging the mouse over them.
				3 - When the user selects an item in the usual way, the selection is cleared and the new item selected. However, if the user presses the Ctrl key when clicking on an item, the clicked item gets toggled and all other items are left untouched. If the user presses the Shift key while clicking on an item, all items between the current item and the clicked item are selected or unselected, depending on the state of the clicked item. Multiple items can be selected by dragging the mouse over them.
				4 - When the user selects an item in the usual way, the selection is cleared and the new item selected. However, if the user presses the Shift key while clicking on an item, all items between the current item and the clicked item are selected or unselected, depending on the state of the clicked item.
				
		"""
		self.edit(selectionMode=value)
	#----------------------------------------------------------------------
	selectionMode = property(get_selectionMode, set_selectionMode)
	#----------------------------------------------------------------------
	def get_sortEnabled(self):
		"""
		
				enable scriptTable sorted by column
				default value is false and the whole row will be sorted
				
		"""
		return self.query(sortEnabled=True)
	#----------------------------------------------------------------------
	def set_sortEnabled(self, value):
		"""
		
				enable scriptTable sorted by column
				default value is false and the whole row will be sorted
				
		"""
		self.edit(sortEnabled=value)
	#----------------------------------------------------------------------
	sortEnabled = property(get_sortEnabled, set_sortEnabled)
	#----------------------------------------------------------------------
	def statusBarMessage(self,value):
		"""
		
				Extra string to display in the status bar when the mouse is over the control.
				
		"""
		self.edit(statusBarMessage=value)
	#----------------------------------------------------------------------
	@property
	def underPointerColumn(self):
		"""
		
				The column under the pointer.
				The returned column number is 1-based (i.e. the first column is 1 not 0).
				
		"""
		return self.query(underPointerColumn=True)
	#----------------------------------------------------------------------
	@property
	def underPointerRow(self):
		"""
		
				The row under the pointer.
				The returned row number is 1-based (i.e. the first row is 1 not 0).
				
		"""
		return self.query(underPointerRow=True)
	#----------------------------------------------------------------------
	def get_useDoubleClickEdit(self):
		"""
		
				this controls the cell edit mode
				False: Click in the cell to select (in Row selection, the last cell of the row is edited, in Column selection, the last cell of the column is edited)(default) 
				True:  Clicked in cell is edited when double-clicked only
				
		"""
		return self.query(useDoubleClickEdit=True)
	#----------------------------------------------------------------------
	def set_useDoubleClickEdit(self, value):
		"""
		
				this controls the cell edit mode
				False: Click in the cell to select (in Row selection, the last cell of the row is edited, in Column selection, the last cell of the column is edited)(default) 
				True:  Clicked in cell is edited when double-clicked only
				
		"""
		self.edit(useDoubleClickEdit=value)
	#----------------------------------------------------------------------
	useDoubleClickEdit = property(get_useDoubleClickEdit, set_useDoubleClickEdit)
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