

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class NodeOutliner(UI_Object.UI):
	"""
	The nodeOutliner command creates, edits and queries an outline control
	that shows dependency nodes and their attributes. Compound attributes
	are further expandable to show their children. Additional configure
	flags allow multi selection, customizable commands to issue upon
	selection, and showing connections (and connectability) to a single
	input attribute. There are also the abilities to add/remove/replace
	nodes through the command line interface, and drag/add.
	
	In some configurations, dragging a connected attribute of a node will
	load the node at the other end of the connection.
	
	There is a right mouse button menu and a flag to attach a command to
	it. The menu is used to list the specific connections of a connected
	attribute. Clicking over any spot but the row of a connected attribute
	will show an empty menu. By default, there is no command attached to
	the menu.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.nodeOutliner(**kwargs)
			super(NodeOutliner, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.nodeOutliner(name, exists=True):
				super(NodeOutliner, self).__init__(name)
			else:
				name = cmds.nodeOutliner(name, **kwargs)
				super(NodeOutliner, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def get_addCommand(self):
		"""
		
				Command executed when the node outliner adds something.
				String commands use substitution of the term %node for whatever is added, eg,
				if you want to print the object added, the command should be
				"print(\"%node \\n\")".  Callable python objects are passed the node name.
				
		"""
		return self.query(addCommand=True)
	#----------------------------------------------------------------------
	def set_addCommand(self, value):
		"""
		
				Command executed when the node outliner adds something.
				String commands use substitution of the term %node for whatever is added, eg,
				if you want to print the object added, the command should be
				"print(\"%node \\n\")".  Callable python objects are passed the node name.
				
		"""
		self.edit(addCommand=value)
	#----------------------------------------------------------------------
	addCommand = property(get_addCommand, set_addCommand)
	#----------------------------------------------------------------------
	def addObject(self,value):
		"""
		
				add the given object to the display
				
		"""
		self.edit(addObject=value)
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
	def get_attrAlphaOrder(self):
		"""
		
				Specify how attributes are to be sorted.  Current recognised values
				are "default" for no sorting and "ascend" to sort attributes from 'a' to ''z' and
				"descend" to sort from 'z' to 'a'.
				Notes: a) this only applies to top level attributes.
				
		"""
		return self.query(attrAlphaOrder=True)
	#----------------------------------------------------------------------
	def set_attrAlphaOrder(self, value):
		"""
		
				Specify how attributes are to be sorted.  Current recognised values
				are "default" for no sorting and "ascend" to sort attributes from 'a' to ''z' and
				"descend" to sort from 'z' to 'a'.
				Notes: a) this only applies to top level attributes.
				
		"""
		self.edit(attrAlphaOrder=value)
	#----------------------------------------------------------------------
	attrAlphaOrder = property(get_attrAlphaOrder, set_attrAlphaOrder)
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
	def get_connectivity(self):
		"""
		
				Takes an attribute argument ("nodeName.attributeName"), dims any attributes
				that can't connect to the given, and highlights any attributes already connected
				
		"""
		return self.query(connectivity=True)
	#----------------------------------------------------------------------
	def set_connectivity(self, value):
		"""
		
				Takes an attribute argument ("nodeName.attributeName"), dims any attributes
				that can't connect to the given, and highlights any attributes already connected
				
		"""
		self.edit(connectivity=value)
	#----------------------------------------------------------------------
	connectivity = property(get_connectivity, set_connectivity)
	#----------------------------------------------------------------------
	@property
	def currentSelection(self):
		"""
		
				Retruns a string array containing what is currently selected
				
		"""
		return self.query(currentSelection=True)
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
	@property
	def lastClickedNode(self):
		"""
		
				Returns a string with the last clicked node
				
		"""
		return self.query(lastClickedNode=True)
	#----------------------------------------------------------------------
	@property
	def lastMenuChoice(self):
		"""
		
				Returns the text of the most recent menu selection.
				
		"""
		return self.query(lastMenuChoice=True)
	#----------------------------------------------------------------------
	def get_longNames(self):
		"""
		
				Controls whether long or short attribute names will be used
				in the interface.  Note that this flag is ignored if the niceNames
				flag is set.  Default is short names. Queried, returns a boolean.
				
		"""
		return self.query(longNames=True)
	#----------------------------------------------------------------------
	def set_longNames(self, value):
		"""
		
				Controls whether long or short attribute names will be used
				in the interface.  Note that this flag is ignored if the niceNames
				flag is set.  Default is short names. Queried, returns a boolean.
				
		"""
		self.edit(longNames=value)
	#----------------------------------------------------------------------
	longNames = property(get_longNames, set_longNames)
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
	def menuCommand(self,value):
		"""
		
				Attaches the given command to each item in the popup menu.
				
		"""
		self.edit(menuCommand=value)
	#----------------------------------------------------------------------
	def get_menuMultiOption(self):
		"""
		
				Sets whether a menu option labelled "next available" will appear as the first
				option on any multi-attribute's right mouse button menu.  Defaults to True.
				
		"""
		return self.query(menuMultiOption=True)
	#----------------------------------------------------------------------
	def set_menuMultiOption(self, value):
		"""
		
				Sets whether a menu option labelled "next available" will appear as the first
				option on any multi-attribute's right mouse button menu.  Defaults to True.
				
		"""
		self.edit(menuMultiOption=value)
	#----------------------------------------------------------------------
	menuMultiOption = property(get_menuMultiOption, set_menuMultiOption)
	#----------------------------------------------------------------------
	def get_multiSelect(self):
		"""
		
				Allow multiSelect; more than one thing to be selected at a time
				
		"""
		return self.query(multiSelect=True)
	#----------------------------------------------------------------------
	def set_multiSelect(self, value):
		"""
		
				Allow multiSelect; more than one thing to be selected at a time
				
		"""
		self.edit(multiSelect=value)
	#----------------------------------------------------------------------
	multiSelect = property(get_multiSelect, set_multiSelect)
	#----------------------------------------------------------------------
	def get_niceNames(self):
		"""
		
				Controls whether the attribute names will be displayed in
				a more user-friendly, readable way.  When this is on, the longNames
				flag is ignored.  When this is off, attribute names will be displayed
				either long or short, according to the longNames flag.
				Default is on. Queried, returns a boolean.
				
		"""
		return self.query(niceNames=True)
	#----------------------------------------------------------------------
	def set_niceNames(self, value):
		"""
		
				Controls whether the attribute names will be displayed in
				a more user-friendly, readable way.  When this is on, the longNames
				flag is ignored.  When this is off, attribute names will be displayed
				either long or short, according to the longNames flag.
				Default is on. Queried, returns a boolean.
				
		"""
		self.edit(niceNames=value)
	#----------------------------------------------------------------------
	niceNames = property(get_niceNames, set_niceNames)
	#----------------------------------------------------------------------
	def noBackground(self,value):
		"""
		
				Clear/reset the control's background.
				Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.
				
		"""
		self.edit(noBackground=value)
	#----------------------------------------------------------------------
	def noConnectivity(self,value):
		"""
		
				Reset the node outliner to not show any connectivity, ie, redraw all rows normally.
				
		"""
		self.edit(noConnectivity=value)
	#----------------------------------------------------------------------
	@property
	def nodesDisplayed(self):
		"""
		
				Returns a string array containing the list of nodes showing in the node Outliner
				
		"""
		return self.query(nodesDisplayed=True)
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
	def get_pressHighlightsUnconnected(self):
		"""
		
				Sets whether clicking on an unconnected plug will select it or not.  Default is True.
				
		"""
		return self.query(pressHighlightsUnconnected=True)
	#----------------------------------------------------------------------
	def set_pressHighlightsUnconnected(self, value):
		"""
		
				Sets whether clicking on an unconnected plug will select it or not.  Default is True.
				
		"""
		self.edit(pressHighlightsUnconnected=value)
	#----------------------------------------------------------------------
	pressHighlightsUnconnected = property(get_pressHighlightsUnconnected, set_pressHighlightsUnconnected)
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
	def redraw(self,value):
		"""
		
				Redraws the displayed space
				
		"""
		self.edit(redraw=value)
	#----------------------------------------------------------------------
	def redrawRow(self,value):
		"""
		
				Redraws the given row
				
		"""
		self.edit(redrawRow=value)
	#----------------------------------------------------------------------
	def remove(self,value):
		"""
		
				remove the given object from the display
				
		"""
		self.edit(remove=value)
	#----------------------------------------------------------------------
	def removeAll(self,value):
		"""
		
				remove all objects from the display
				
		"""
		self.edit(removeAll=value)
	#----------------------------------------------------------------------
	def get_replace(self):
		"""
		
				replace what's displayed with the given objects
				
		"""
		return self.query(replace=True)
	#----------------------------------------------------------------------
	def set_replace(self, value):
		"""
		
				replace what's displayed with the given objects
				
		"""
		self.edit(replace=value)
	#----------------------------------------------------------------------
	replace = property(get_replace, set_replace)
	#----------------------------------------------------------------------
	def get_selectCommand(self):
		"""
		
				Command issued by selecting.  Different from the c flag in that this
				command will only be issued if something is selected.
				
		"""
		return self.query(selectCommand=True)
	#----------------------------------------------------------------------
	def set_selectCommand(self, value):
		"""
		
				Command issued by selecting.  Different from the c flag in that this
				command will only be issued if something is selected.
				
		"""
		self.edit(selectCommand=value)
	#----------------------------------------------------------------------
	selectCommand = property(get_selectCommand, set_selectCommand)
	#----------------------------------------------------------------------
	def get_showConnectedOnly(self):
		"""
		
				show (true) or hide (false) only attributes that are connected matching input/output criteria
				
		"""
		return self.query(showConnectedOnly=True)
	#----------------------------------------------------------------------
	def set_showConnectedOnly(self, value):
		"""
		
				show (true) or hide (false) only attributes that are connected matching input/output criteria
				
		"""
		self.edit(showConnectedOnly=value)
	#----------------------------------------------------------------------
	showConnectedOnly = property(get_showConnectedOnly, set_showConnectedOnly)
	#----------------------------------------------------------------------
	def get_showHidden(self):
		"""
		
				show (true) or hide (false) UI invisible attributes that match the input/output criteria
				
		"""
		return self.query(showHidden=True)
	#----------------------------------------------------------------------
	def set_showHidden(self, value):
		"""
		
				show (true) or hide (false) UI invisible attributes that match the input/output criteria
				
		"""
		self.edit(showHidden=value)
	#----------------------------------------------------------------------
	showHidden = property(get_showHidden, set_showHidden)
	#----------------------------------------------------------------------
	def get_showInputs(self):
		"""
		
				show only UI visible attributes that can be connected to
				
		"""
		return self.query(showInputs=True)
	#----------------------------------------------------------------------
	def set_showInputs(self, value):
		"""
		
				show only UI visible attributes that can be connected to
				
		"""
		self.edit(showInputs=value)
	#----------------------------------------------------------------------
	showInputs = property(get_showInputs, set_showInputs)
	#----------------------------------------------------------------------
	def get_showNonConnectable(self):
		"""
		
				show (true) or hide (false) non connectable attributes that match the input/output criteria
				
		"""
		return self.query(showNonConnectable=True)
	#----------------------------------------------------------------------
	def set_showNonConnectable(self, value):
		"""
		
				show (true) or hide (false) non connectable attributes that match the input/output criteria
				
		"""
		self.edit(showNonConnectable=value)
	#----------------------------------------------------------------------
	showNonConnectable = property(get_showNonConnectable, set_showNonConnectable)
	#----------------------------------------------------------------------
	def get_showNonKeyable(self):
		"""
		
				show (true) or hide (false) non keyframeable (animatable) attributes that match the input/output criteria
				
		"""
		return self.query(showNonKeyable=True)
	#----------------------------------------------------------------------
	def set_showNonKeyable(self, value):
		"""
		
				show (true) or hide (false) non keyframeable (animatable) attributes that match the input/output criteria
				
		"""
		self.edit(showNonKeyable=value)
	#----------------------------------------------------------------------
	showNonKeyable = property(get_showNonKeyable, set_showNonKeyable)
	#----------------------------------------------------------------------
	def get_showOutputs(self):
		"""
		
				show only UI visible attributes that can be connected from
				
		"""
		return self.query(showOutputs=True)
	#----------------------------------------------------------------------
	def set_showOutputs(self, value):
		"""
		
				show only UI visible attributes that can be connected from
				
		"""
		self.edit(showOutputs=value)
	#----------------------------------------------------------------------
	showOutputs = property(get_showOutputs, set_showOutputs)
	#----------------------------------------------------------------------
	def get_showPublished(self):
		"""
		
				Show only published attributes for an asset or a member of an asset.
				This flag is ignored on nodes not related to assets.
				
		"""
		return self.query(showPublished=True)
	#----------------------------------------------------------------------
	def set_showPublished(self, value):
		"""
		
				Show only published attributes for an asset or a member of an asset.
				This flag is ignored on nodes not related to assets.
				
		"""
		self.edit(showPublished=value)
	#----------------------------------------------------------------------
	showPublished = property(get_showPublished, set_showPublished)
	#----------------------------------------------------------------------
	def get_showReadOnly(self):
		"""
		
				show only read only attributes attributes that can be connected from
				
		"""
		return self.query(showReadOnly=True)
	#----------------------------------------------------------------------
	def set_showReadOnly(self, value):
		"""
		
				show only read only attributes attributes that can be connected from
				
		"""
		self.edit(showReadOnly=value)
	#----------------------------------------------------------------------
	showReadOnly = property(get_showReadOnly, set_showReadOnly)
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