

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class TreeView(UI_Object.UI):
	"""
	This command creates a custom control.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.treeView(**kwargs)
			super(TreeView, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.treeView(name, exists=True):
				super(TreeView, self).__init__(name)
			else:
				name = cmds.treeView(name, **kwargs)
				super(TreeView, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def addItem(self,value):
		"""
		
				Adds a tree view item to the tree view.
				First argument specifies the item's name, second argument specifies the item's parent (use an empty string to have it at the top level of the tree)
				
		"""
		self.edit(addItem=value)
	#----------------------------------------------------------------------
	def get_allowDragAndDrop(self):
		"""
		
				Allow the user to perform drag and drop of treeView items.  If enabled,
				re-ordering / re-parenting operations can be perfomed with the middle mouse button.
				This flag takes precendence over other drag and drop related flags.
				Defaults to true.
				
		"""
		return self.query(allowDragAndDrop=True)
	#----------------------------------------------------------------------
	def set_allowDragAndDrop(self, value):
		"""
		
				Allow the user to perform drag and drop of treeView items.  If enabled,
				re-ordering / re-parenting operations can be perfomed with the middle mouse button.
				This flag takes precendence over other drag and drop related flags.
				Defaults to true.
				
		"""
		self.edit(allowDragAndDrop=value)
	#----------------------------------------------------------------------
	allowDragAndDrop = property(get_allowDragAndDrop, set_allowDragAndDrop)
	#----------------------------------------------------------------------
	def get_allowHiddenParents(self):
		"""
		
				If not cleared(default), the treeView will make parent nodes of visible nodes automatically visible
				
		"""
		return self.query(allowHiddenParents=True)
	#----------------------------------------------------------------------
	def set_allowHiddenParents(self, value):
		"""
		
				If not cleared(default), the treeView will make parent nodes of visible nodes automatically visible
				
		"""
		self.edit(allowHiddenParents=value)
	#----------------------------------------------------------------------
	allowHiddenParents = property(get_allowHiddenParents, set_allowHiddenParents)
	#----------------------------------------------------------------------
	def get_allowMultiSelection(self):
		"""
		
				Specify multi or single selection mode.
				Allow the user to perform multiple selection by holding
				ctrl or shift key while selecting items of treeView items.
				Defaults to true.
				
		"""
		return self.query(allowMultiSelection=True)
	#----------------------------------------------------------------------
	def set_allowMultiSelection(self, value):
		"""
		
				Specify multi or single selection mode.
				Allow the user to perform multiple selection by holding
				ctrl or shift key while selecting items of treeView items.
				Defaults to true.
				
		"""
		self.edit(allowMultiSelection=value)
	#----------------------------------------------------------------------
	allowMultiSelection = property(get_allowMultiSelection, set_allowMultiSelection)
	#----------------------------------------------------------------------
	def get_allowReparenting(self):
		"""
		
				Allow the user to reparent items in the tree view using the middle
				mouse button. Defaults to true. If false, user can still reorder items
				within a group using the middle mouse button.
				
		"""
		return self.query(allowReparenting=True)
	#----------------------------------------------------------------------
	def set_allowReparenting(self, value):
		"""
		
				Allow the user to reparent items in the tree view using the middle
				mouse button. Defaults to true. If false, user can still reorder items
				within a group using the middle mouse button.
				
		"""
		self.edit(allowReparenting=value)
	#----------------------------------------------------------------------
	allowReparenting = property(get_allowReparenting, set_allowReparenting)
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
	def attachButtonRight(self,value):
		"""
		
				Sets tree view item's buttons to appear on the right or left.
				Argument specifies if they are to be attached to the right, if it is set to false they will attach on the left.
				
		"""
		self.edit(attachButtonRight=value)
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
	def borderHighlite(self,value):
		"""
		
				Sets an item's border as highlit or not.
				First Argument specifies item, second argument specifies on or off.
				
		"""
		self.edit(borderHighlite=value)
	#----------------------------------------------------------------------
	def borderHighliteColor(self,value):
		"""
		
				Sets the color an item's border highlite will turn when highlite is enabled.
				first parameter specifies layer
				three float values specify RGB values, between 0 and 1.
				
		"""
		self.edit(borderHighliteColor=value)
	#----------------------------------------------------------------------
	def get_buttonErase(self):
		"""
		
				If buttonErase was set true , then even if the button of the treeView item  is set invisible , the treeView will still erase the buttonRect of this treeView item with background .
				First argument is the item name, second argument is whether buttonErase was set true or false
				
		"""
		return self.query(buttonErase=True)
	#----------------------------------------------------------------------
	def set_buttonErase(self, value):
		"""
		
				If buttonErase was set true , then even if the button of the treeView item  is set invisible , the treeView will still erase the buttonRect of this treeView item with background .
				First argument is the item name, second argument is whether buttonErase was set true or false
				
		"""
		self.edit(buttonErase=value)
	#----------------------------------------------------------------------
	buttonErase = property(get_buttonErase, set_buttonErase)
	#----------------------------------------------------------------------
	def buttonState(self,value):
		"""
		
				Sets the state of a button.
				First argument specifies the layer, second argument specifies which button, third argument specifies the state
				Possible states:
				"buttonUp" - button is up
				"buttonDown" - button is down
				"buttonThirdState" - button is in state three (used by the "3StateButton" button style)
				
		"""
		self.edit(buttonState=value)
	#----------------------------------------------------------------------
	def buttonStyle(self,value):
		"""
		
				Sets the type of button, used to indicate possible states and if the button is reset upon release.
				First argument specifies the layer, second argument specifies which button, third argument specifies the type of button
				Possible button types:
				"pushButton" - two possible states, button is reset to up upon release
				"2StateButton" - two possible states, button changes state on click
				"3StateButton" - three button states, button changes state on click
				
		"""
		self.edit(buttonStyle=value)
	#----------------------------------------------------------------------
	def buttonTextIcon(self,value):
		"""
		
				Sets a one letter text to use as the icon to use for a specific button on a specific item.
				First argument specifies the item, second argument specifies the button, third argument specifies the icon text.
				
		"""
		self.edit(buttonTextIcon=value)
	#----------------------------------------------------------------------
	def buttonTooltip(self,value):
		"""
		
				Sets a tooltip for specific button on a specific item.
				First argument specifies the item, second argument specifies the button, third argument specifies the tooltip.
				
		"""
		self.edit(buttonTooltip=value)
	#----------------------------------------------------------------------
	def buttonTransparencyColor(self,value):
		"""
		
				Sets the background color of a button that will be used if buttonTransparencyOverride is enabled.
				First argument specifies item, second argument specifies button,
				three floats specify RGB values, between 0 and 1.
				
		"""
		self.edit(buttonTransparencyColor=value)
	#----------------------------------------------------------------------
	def buttonTransparencyOverride(self,value):
		"""
		
				Sets a button's background as being overridden or not.
				First argument specifies item, second argument specifies button, third argument specifies overridden or not.
				
		"""
		self.edit(buttonTransparencyOverride=value)
	#----------------------------------------------------------------------
	@property
	def children(self):
		"""
		
				Query the children of an item. If the argument is null, all items will be returned.
				      In query mode, this flag needs a value.
				
		"""
		return self.query(children=True)
	#----------------------------------------------------------------------
	def clearSelection(self,value):
		"""
		
				Clears all selected items.
				
		"""
		self.edit(clearSelection=value)
	#----------------------------------------------------------------------
	def contextMenuCommand(self,value):
		"""
		
				Set the callback function to be invoked just before any attached context
				menu is shown. This can be used as a replacement to, or in addition to the
				postMenuCommand flag on the popupMenu command. The function should accept
				a string which will be the item that was clicked on (empty if no item was hit).
				The function should return true if the menu should be shown, false otherwise.
				
		"""
		self.edit(contextMenuCommand=value)
	#----------------------------------------------------------------------
	def displayLabel(self,value):
		"""
		
				Set a label for the item that is different than the
				string that identifies the item. This label will be used in the
				display of the item. The first parameter specifies
				the item, the second specifies the display label.
				
		"""
		self.edit(displayLabel=value)
	#----------------------------------------------------------------------
	def displayLabelSuffix(self,value):
		"""
		
				Set a suffix for the display label for the item. This suffix will
				not be shown when renaming the item in the tree view.
				
		"""
		self.edit(displayLabelSuffix=value)
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
	def dragAndDropCommand(self,value):
		"""
		
				Sets the callback function to be invoked upon drag and drop of layers.
				the callback function should take as parameters:
				- a string array of the dropped items
				- a string array of the items previous parents
				- an integer array of the items previous indexes
				- a string for the item(s) new parent
				- an integer array for the item's new indexes
				- a string for the item that now comes before the dropped items
				- a string for the item that now comes after the dropped items
				
		"""
		self.edit(dragAndDropCommand=value)
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
	def editLabelCommand(self,value):
		"""
		
				Set the callback function to be invoked when the user changes
				the name of an item by double clicking it in the UI. The callback should
				accept two string arguments: the item name and the new name. The item
				name refers to the name of the item and not the display label. The callback
				function should return a string. An empty string indicates that the rename
				operation was invalid and the control should revert to the original name.
				If the rename operation is valid the callback should return a string that
				identifies the item, possibly different from the new display name entered
				by the user.
				
		"""
		self.edit(editLabelCommand=value)
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
	def enableButton(self,value):
		"""
		
				Sets a specific button on a specific item to being usable or not.
				First argument specifies the item, second argument specifies the button, third argument specifies on or off.
				
		"""
		self.edit(enableButton=value)
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
	def enableKeys(self,value):
		"""
		
				By default the treeview does not accept input from the keyboard.  By enabling keyboard support
				The treeview will support up/down navigation using the up/down arrow keys.
				
		"""
		self.edit(enableKeys=value)
	#----------------------------------------------------------------------
	def enableLabel(self,value):
		"""
		
				enables or disables the label of a tree view item from being displayed. The first parameter specifies
				the item, the second specifies on or off.
				
		"""
		self.edit(enableLabel=value)
	#----------------------------------------------------------------------
	def expandCollapseCommand(self,value):
		"""
		
				Set the callback function to be invoked upon hitting the expand/collapse button.
				The function should take as parameters:
				- a string for the item for which the expand/collapse button was hit
				- an integer for the state of expansion
				
		"""
		self.edit(expandCollapseCommand=value)
	#----------------------------------------------------------------------
	def expandItem(self,value):
		"""
		
				Expands or collapses an item's children.
				First argument specifies the item, second argument specifies expanded or collapsed.
				
		"""
		self.edit(expandItem=value)
	#----------------------------------------------------------------------
	def get_flatButton(self):
		"""
		
				Type of flat button to use.
				
		"""
		return self.query(flatButton=True)
	#----------------------------------------------------------------------
	def set_flatButton(self, value):
		"""
		
				Type of flat button to use.
				
		"""
		self.edit(flatButton=value)
	#----------------------------------------------------------------------
	flatButton = property(get_flatButton, set_flatButton)
	#----------------------------------------------------------------------
	def get_font(self):
		"""
		
				The first parameter specifies the item string for
				the TtreeViewNode in the TtreeNodeMap.
				The second string specifies the font for the text.
				Valid values are
				"boldLabelFont", "smallBoldLabelFont", "tinyBoldLabelFont",
				"plainLabelFont", "smallPlainLabelFont", "obliqueLabelFont",
				"smallObliqueLabelFont", "fixedWidthFont" and
				"smallFixedWidthFont".
				
		"""
		return self.query(font=True)
	#----------------------------------------------------------------------
	def set_font(self, value):
		"""
		
				The first parameter specifies the item string for
				the TtreeViewNode in the TtreeNodeMap.
				The second string specifies the font for the text.
				Valid values are
				"boldLabelFont", "smallBoldLabelFont", "tinyBoldLabelFont",
				"plainLabelFont", "smallPlainLabelFont", "obliqueLabelFont",
				"smallObliqueLabelFont", "fixedWidthFont" and
				"smallFixedWidthFont".
				
		"""
		self.edit(font=value)
	#----------------------------------------------------------------------
	font = property(get_font, set_font)
	#----------------------------------------------------------------------
	def fontFace(self,value):
		"""
		
				Sets the font face used for the specified item's text:
				0 for normal,
				1 for bold,
				2 for italic.
				
		"""
		self.edit(fontFace=value)
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
	def hideButtons(self,value):
		"""
		
				Hides the buttons for an item in the tree view. Can only be used when
				adding the item to the tree with the "addItem" flag. Space for the buttons
				is left to make sure items still line up correctly under their parent.
				
		"""
		self.edit(hideButtons=value)
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
	def highlite(self,value):
		"""
		
				Sets an item as highlit. Highliting is shown by outlining the item.
				First parameter specifies the item, the second specifies the highliting
				or not.
				
		"""
		self.edit(highlite=value)
	#----------------------------------------------------------------------
	def highliteColor(self,value):
		"""
		
				Sets the color an item's highlite will turn when highlite is enabled.
				first parameter specifies layer
				three float values specify RGB values, between 0 and 1.
				
		"""
		self.edit(highliteColor=value)
	#----------------------------------------------------------------------
	def ignoreButtonClick(self,value):
		"""
		
				Sets a specific button on a specific item to ignore the button clicks
				First argument specifies the item ,second argument specifies the button, third argument specifies on or off
				
		"""
		self.edit(ignoreButtonClick=value)
	#----------------------------------------------------------------------
	def image(self,value):
		"""
		
				Sets an image to use as the icon for the button.
				First argument specifies the item, second argument specifies the button, third argument specifies the image.
				
		"""
		self.edit(image=value)
	#----------------------------------------------------------------------
	@property
	def isItemExpanded(self):
		"""
		
				Is the item in the tree view expanded.
				      In query mode, this flag needs a value.
				
		"""
		return self.query(isItemExpanded=True)
	#----------------------------------------------------------------------
	@property
	def isLeaf(self):
		"""
		
				Query whether an item is a leaf.
				      In query mode, this flag needs a value.
				
		"""
		return self.query(isLeaf=True)
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
	@property
	def item(self):
		"""
		
				Specify the item to query. Used with the flag "selectionColor" and "itemAnnotation".
				      In query mode, this flag needs a value.
				
		"""
		return self.query(item=True)
	#----------------------------------------------------------------------
	def get_itemAnnotation(self):
		"""
		
				Annotate the specified item with an extra string value.
				When used for query, this flag has no argument and needs to be used with the
				flag "item".
				
		"""
		return self.query(itemAnnotation=True)
	#----------------------------------------------------------------------
	def set_itemAnnotation(self, value):
		"""
		
				Annotate the specified item with an extra string value.
				When used for query, this flag has no argument and needs to be used with the
				flag "item".
				
		"""
		self.edit(itemAnnotation=value)
	#----------------------------------------------------------------------
	itemAnnotation = property(get_itemAnnotation, set_itemAnnotation)
	#----------------------------------------------------------------------
	def itemDblClickCommand(self,value):
		"""
		
				Set the callback function to be invoked when an item in the tree has been
				double clicked. The callback should accept one string, the display label of the
				item that was double clicked. If this callback is defined, it supersedes
				the normal item renaming behavior.
				
		"""
		self.edit(itemDblClickCommand=value)
	#----------------------------------------------------------------------
	def itemDblClickCommand2(self,value):
		"""
		
				Set the callback function to be invoked when an item in the tree has been
				double clicked. This callback is similar to itemDblClickCommand(idc), but it accepts two strings:
				the name and the display label of the item that was double clicked. If this callback is defined,
				it supersedes the normal item renaming behavior
				
		"""
		self.edit(itemDblClickCommand2=value)
	#----------------------------------------------------------------------
	@property
	def itemExists(self):
		"""
		
				Queries the existence of the specified Tree View item.
				      In query mode, this flag needs a value.
				
		"""
		return self.query(itemExists=True)
	#----------------------------------------------------------------------
	@property
	def itemIndex(self):
		"""
		
				Get the index for the specified item in the list of children of the item's
				parent. Index is 0-based.
				      In query mode, this flag needs a value.
				
		"""
		return self.query(itemIndex=True)
	#----------------------------------------------------------------------
	@property
	def itemParent(self):
		"""
		
				If the specified item is a child, it returns the parent item. If the specified item is not a child it returns nothing.
				      In query mode, this flag needs a value.
				
		"""
		return self.query(itemParent=True)
	#----------------------------------------------------------------------
	def itemRenamedCommand(self,value):
		"""
		
				Set the callback function to be invoked when an item in the tree has been
				renamed. This occurs if there is a successful return of the command attached
				by "editLabelCommand" or unconditionally if there is no editLabelCommand.
				The callback should accept two strings, the old name and the new name of the
				item that was renamed.
				
		"""
		self.edit(itemRenamedCommand=value)
	#----------------------------------------------------------------------
	@property
	def itemSelected(self):
		"""
		
				Queries the item is currently selected or not.
				      In query mode, this flag needs a value.
				
		"""
		return self.query(itemSelected=True)
	#----------------------------------------------------------------------
	def get_itemVisible(self):
		"""
		
				Control the given item's visibility.
				
		"""
		return self.query(itemVisible=True)
	#----------------------------------------------------------------------
	def set_itemVisible(self, value):
		"""
		
				Control the given item's visibility.
				
		"""
		self.edit(itemVisible=value)
	#----------------------------------------------------------------------
	itemVisible = property(get_itemVisible, set_itemVisible)
	#----------------------------------------------------------------------
	def labelBackgroundColor(self,value):
		"""
		
				Set the background color for text label for a particular item
				in the tree. The first parameter specifies layer.
				Set (-1.0, -1.0, -1.0) to restore the background
				to the default of "transparent"
				
		"""
		self.edit(labelBackgroundColor=value)
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
	def numberOfButtons(self,value):
		"""
		
				Specifies the number of buttons for items in the tree.
				
		"""
		self.edit(numberOfButtons=value)
	#----------------------------------------------------------------------
	@property
	def numberOfPopupMenus(self):
		"""
		
				Return the number of popup menus attached to this control.
				
		"""
		return self.query(numberOfPopupMenus=True)
	#----------------------------------------------------------------------
	def ornament(self,value):
		"""
		
				Sets an item as having an ornament (a small colored circle), its on/off state, if it should have a dot, and its size.
				First Argument specifies item,
				second argument specifies on or off,
				third argument specifies dotted or not,
				fourth argument specifies radius (in pixels).
				
		"""
		self.edit(ornament=value)
	#----------------------------------------------------------------------
	def ornamentColor(self,value):
		"""
		
				Sets the color an ornament will be draw with for the specified layer.
				
		"""
		self.edit(ornamentColor=value)
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
	def pressCommand(self,value):
		"""
		
				Sets the callback function to be invoked upon clicking a treeView button.
				First argument specifies which treeView button.
				Second argument specifies the callback function to be executed
				the callback function should take as parameters:
				- a string for the clicked button's item
				- an int for the clicked button's state
				
		"""
		self.edit(pressCommand=value)
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
	def removeAll(self,value):
		"""
		
				Removes all items from the tree view.
				
		"""
		self.edit(removeAll=value)
	#----------------------------------------------------------------------
	def removeItem(self,value):
		"""
		
				Removes a tree view item from the tree view. If this item has children items, all children items are removed.
				First argument specifies the item's name.
				
		"""
		self.edit(removeItem=value)
	#----------------------------------------------------------------------
	def reverseTreeOrder(self,value):
		"""
		
				Controls the order the tree will be drawn in (reversed if true).
				
		"""
		self.edit(reverseTreeOrder=value)
	#----------------------------------------------------------------------
	def rightPressCommand(self,value):
		"""
		
				Sets the callback function to be invoked upon right clicking a treeView button.
				First argument specifies which treeView button.
				Second argument specifies the callback function to be executed
				the callback function should take as parameters:
				- a string for the clicked button's item
				- an int for the clicked button's state
				
		"""
		self.edit(rightPressCommand=value)
	#----------------------------------------------------------------------
	def select(self,value):
		"""
		
				Set selection on an element. The first parameter specifies the item, the second specifies on or off.
				
		"""
		self.edit(select=value)
	#----------------------------------------------------------------------
	def selectCommand(self,value):
		"""
		
				Set the callback function to be invoked when an item is selected or deselected
				in the tree. The function should accept one string argument and
				one integer argument: the item name and the select state respectively. If the
				function returns true, the select/deselect is considered valid and will
				occur normally, otherwise it will be disallowed.
				name and
				
		"""
		self.edit(selectCommand=value)
	#----------------------------------------------------------------------
	def get_selectItem(self):
		"""
		
				Sets an item's selected state.
				first argument specifies the item, second argument specifies selection status.
				When used for query without arguments, return all selected items in the treeview.
				
		"""
		return self.query(selectItem=True)
	#----------------------------------------------------------------------
	def set_selectItem(self, value):
		"""
		
				Sets an item's selected state.
				first argument specifies the item, second argument specifies selection status.
				When used for query without arguments, return all selected items in the treeview.
				
		"""
		self.edit(selectItem=value)
	#----------------------------------------------------------------------
	selectItem = property(get_selectItem, set_selectItem)
	#----------------------------------------------------------------------
	def selectionChangedCommand(self,value):
		"""
		
				Set the callback function to be invoked when a complete selection operation
				triggered by the user has occurred successfully. The callback is invoked if
				the "selectCommand" callback has returned a non-empty value (or always there
				is no "selectCommand" callback). This differs from selectCommand in that a
				simple selection replacement will generate two callbacks with "selectCommand"
				(one for deselect of the old item and one for select of the new), whereas
				"selectionChangedCommand" will only be invoked once, after the selection is
				complete. The callback is not passed any parameters and does not need to
				return any value (i.e. It is simply a notification mechanism).
				
		"""
		self.edit(selectionChangedCommand=value)
	#----------------------------------------------------------------------
	def get_selectionColor(self):
		"""
		
				Sets the color an item will turn to indicate that it is selected.
				first parameter specifies the item
				three float values specify RGB values, between 0 and 1.
				When used for query, this flag has no argument and needs to be used with the
				flag "item". It returns the color an item will become if it is selected.
				
		"""
		return self.query(selectionColor=True)
	#----------------------------------------------------------------------
	def set_selectionColor(self, value):
		"""
		
				Sets the color an item will turn to indicate that it is selected.
				first parameter specifies the item
				three float values specify RGB values, between 0 and 1.
				When used for query, this flag has no argument and needs to be used with the
				flag "item". It returns the color an item will become if it is selected.
				
		"""
		self.edit(selectionColor=value)
	#----------------------------------------------------------------------
	selectionColor = property(get_selectionColor, set_selectionColor)
	#----------------------------------------------------------------------
	def showItem(self,value):
		"""
		
				Show the  item. Scroll the list as necessary so that item is visible.
				
		"""
		self.edit(showItem=value)
	#----------------------------------------------------------------------
	def statusBarMessage(self,value):
		"""
		
				Extra string to display in the status bar when the mouse is over the control.
				
		"""
		self.edit(statusBarMessage=value)
	#----------------------------------------------------------------------
	def textColor(self,value):
		"""
		
				Sets the label's text color for the specified layer.
				first argument specifies layer.
				three float values specify RGB values, between 0 and 1.
				
		"""
		self.edit(textColor=value)
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