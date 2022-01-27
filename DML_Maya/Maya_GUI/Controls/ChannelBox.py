

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class ChannelBox(UI_Object.UI):
	"""
	This command creates a channel box, which is sensitive to the active
	list.  It displays certain attributes (channels) of the last node on
	the active list, and provides a two-way connection to keep the widget
	up to date.
	
	Note: when setting the color of attribute names, that color is only valid
	for its current Maya session; each subsequent session will display the default
	color for the attribute name(s) listed in the Channel Box. Any subsequent
	attributes that are added to the Channel Box will be affected by prior
	regular expressions in their current Maya session.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.channelBox(**kwargs)
			super(ChannelBox, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.channelBox(name, exists=True):
				super(ChannelBox, self).__init__(name)
			else:
				name = cmds.channelBox(name, **kwargs)
				super(ChannelBox, self).__init__(name, **dict(qtParent=parent))
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
	def get_attrBgColor(self):
		"""
		
				Controls the background text color of specific attribute names. As with the foreground
				option, this text coloring also depends on the node name choice for the nodeRegex flag.
				Arguments correspond to the red, green, and blue color components.
				Each component ranges in value from 0.0 to 1.0. If attrRegex is
				unspecified then it will assume a value of "*" for a regular expression.
				The same idea simultaneously applies to the flag nodeRegex.
				Note: nodes that are renamed will have their node name coloring be affected
				in the channel box.
				
		"""
		return self.query(attrBgColor=True)
	#----------------------------------------------------------------------
	def set_attrBgColor(self, value):
		"""
		
				Controls the background text color of specific attribute names. As with the foreground
				option, this text coloring also depends on the node name choice for the nodeRegex flag.
				Arguments correspond to the red, green, and blue color components.
				Each component ranges in value from 0.0 to 1.0. If attrRegex is
				unspecified then it will assume a value of "*" for a regular expression.
				The same idea simultaneously applies to the flag nodeRegex.
				Note: nodes that are renamed will have their node name coloring be affected
				in the channel box.
				
		"""
		self.edit(attrBgColor=value)
	#----------------------------------------------------------------------
	attrBgColor = property(get_attrBgColor, set_attrBgColor)
	#----------------------------------------------------------------------
	def get_attrColor(self):
		"""
		
				Controls the foreground text color of specific attribute names. This
				text coloring also depends on the node name choice for the nodeRegex flag.
				Arguments correspond to the red, green, and blue color components.
				Each component ranges in value from 0.0 to 1.0. If attrRegex is
				unspecified then it will assume a value of "*" for a regular expression.
				The same idea simultaneously applies to the flag nodeRegex.
				Note: nodes that are renamed will have their node name coloring be affected
				in the channel box.
				
		"""
		return self.query(attrColor=True)
	#----------------------------------------------------------------------
	def set_attrColor(self, value):
		"""
		
				Controls the foreground text color of specific attribute names. This
				text coloring also depends on the node name choice for the nodeRegex flag.
				Arguments correspond to the red, green, and blue color components.
				Each component ranges in value from 0.0 to 1.0. If attrRegex is
				unspecified then it will assume a value of "*" for a regular expression.
				The same idea simultaneously applies to the flag nodeRegex.
				Note: nodes that are renamed will have their node name coloring be affected
				in the channel box.
				
		"""
		self.edit(attrColor=value)
	#----------------------------------------------------------------------
	attrColor = property(get_attrColor, set_attrColor)
	#----------------------------------------------------------------------
	def get_attrFilter(self):
		"""
		
				Specifies the name of an itemFilter object to be placed on the channel box.
				This filters the attributes displayed. A filter of "0" can be used to reset the
				filter.
				
		"""
		return self.query(attrFilter=True)
	#----------------------------------------------------------------------
	def set_attrFilter(self, value):
		"""
		
				Specifies the name of an itemFilter object to be placed on the channel box.
				This filters the attributes displayed. A filter of "0" can be used to reset the
				filter.
				
		"""
		self.edit(attrFilter=value)
	#----------------------------------------------------------------------
	attrFilter = property(get_attrFilter, set_attrFilter)
	#----------------------------------------------------------------------
	def get_attrRegex(self):
		"""
		
				Specifies a valid regular expression to specify which attribute names
				should be selected for foreground text coloring. If attrRegex is
				unspecified then it will assume a value of "*" for a regular expression.
				The same idea simultaneously applies to the flag nodeRegex.
				The attrColor flag is required to be specified.
				Note: this regular expression will be treated as though it were case-insensitve
				
		"""
		return self.query(attrRegex=True)
	#----------------------------------------------------------------------
	def set_attrRegex(self, value):
		"""
		
				Specifies a valid regular expression to specify which attribute names
				should be selected for foreground text coloring. If attrRegex is
				unspecified then it will assume a value of "*" for a regular expression.
				The same idea simultaneously applies to the flag nodeRegex.
				The attrColor flag is required to be specified.
				Note: this regular expression will be treated as though it were case-insensitve
				
		"""
		self.edit(attrRegex=value)
	#----------------------------------------------------------------------
	attrRegex = property(get_attrRegex, set_attrRegex)
	#----------------------------------------------------------------------
	def get_attributeEditorMode(self):
		"""
		
				Modifies what appears in the channel box for use in the
				attribute editor. Default is false. Queried, returns a boolean.
				
		"""
		return self.query(attributeEditorMode=True)
	#----------------------------------------------------------------------
	def set_attributeEditorMode(self, value):
		"""
		
				Modifies what appears in the channel box for use in the
				attribute editor. Default is false. Queried, returns a boolean.
				
		"""
		self.edit(attributeEditorMode=value)
	#----------------------------------------------------------------------
	attributeEditorMode = property(get_attributeEditorMode, set_attributeEditorMode)
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
	def get_containerAtTop(self):
		"""
		
				This flag can be used to specify whether or not the container is drawn at the
				top of the channel box when a node in the container is selected.
				
		"""
		return self.query(containerAtTop=True)
	#----------------------------------------------------------------------
	def set_containerAtTop(self, value):
		"""
		
				This flag can be used to specify whether or not the container is drawn at the
				top of the channel box when a node in the container is selected.
				
		"""
		self.edit(containerAtTop=value)
	#----------------------------------------------------------------------
	containerAtTop = property(get_containerAtTop, set_containerAtTop)
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
	def get_enableLabelSelection(self):
		"""
		
				Enables the selection of attributes in the channelBox
				when used in conjunction with -attributeEditorMode.
				Default is false.  Queried, returns a boolean.
				
		"""
		return self.query(enableLabelSelection=True)
	#----------------------------------------------------------------------
	def set_enableLabelSelection(self, value):
		"""
		
				Enables the selection of attributes in the channelBox
				when used in conjunction with -attributeEditorMode.
				Default is false.  Queried, returns a boolean.
				
		"""
		self.edit(enableLabelSelection=value)
	#----------------------------------------------------------------------
	enableLabelSelection = property(get_enableLabelSelection, set_enableLabelSelection)
	#----------------------------------------------------------------------
	def execute(self,value):
		"""
		
				Immediately executes the command string once for every cell (or every
				selected cell, if the boolean argument is TRUE) in the
				channel box, for every matching selected object (ie, for every object would
				be affected if you changed a cell value.)  Before the command is executed,
				"#A" is substituted with the name of the attribute, and "#N" with the name
				of the node, and "#P" with the full path name of the node.
				
		"""
		self.edit(execute=value)
	#----------------------------------------------------------------------
	def get_fieldWidth(self):
		"""
		
				An optional flag which is used to modify the width assigned
				to fields appearing in the channelBox.
				
		"""
		return self.query(fieldWidth=True)
	#----------------------------------------------------------------------
	def set_fieldWidth(self, value):
		"""
		
				An optional flag which is used to modify the width assigned
				to fields appearing in the channelBox.
				
		"""
		self.edit(fieldWidth=value)
	#----------------------------------------------------------------------
	fieldWidth = property(get_fieldWidth, set_fieldWidth)
	#----------------------------------------------------------------------
	def get_fixedAttrList(self):
		"""
		
				Forces the channel box to only display attributes with the
				specified names, in the order they are specified.  If an empty
				list is specified, then the channel box will revert to its default
				behaviour of listing all keyable attributes.
				
		"""
		return self.query(fixedAttrList=True)
	#----------------------------------------------------------------------
	def set_fixedAttrList(self, value):
		"""
		
				Forces the channel box to only display attributes with the
				specified names, in the order they are specified.  If an empty
				list is specified, then the channel box will revert to its default
				behaviour of listing all keyable attributes.
				
		"""
		self.edit(fixedAttrList=value)
	#----------------------------------------------------------------------
	fixedAttrList = property(get_fixedAttrList, set_fixedAttrList)
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
	def historyObjectList(self):
		"""
		
				Returns a list of strings, the names of every INPUT node associated with
				an object on the main object list that is of the same type as the node
				displayed in the INPUT section of the channel box.
				
		"""
		return self.query(historyObjectList=True)
	#----------------------------------------------------------------------
	def get_hyperbolic(self):
		"""
		
				Determines whether or not the distance that the mouse has been dragged
				should be interpreted as a linear or hyperbolic function.  The default
				is set to hyperbolic being false.
				
		"""
		return self.query(hyperbolic=True)
	#----------------------------------------------------------------------
	def set_hyperbolic(self, value):
		"""
		
				Determines whether or not the distance that the mouse has been dragged
				should be interpreted as a linear or hyperbolic function.  The default
				is set to hyperbolic being false.
				
		"""
		self.edit(hyperbolic=value)
	#----------------------------------------------------------------------
	hyperbolic = property(get_hyperbolic, set_hyperbolic)
	#----------------------------------------------------------------------
	@property
	def inputs(self):
		"""
		
				Returns the items shown under the 'INPUTS' heading in the channel box.
				
		"""
		return self.query(inputs=True)
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
	def get_labelWidth(self):
		"""
		
				An optional flag which is used to modify the width assigned
				to labels appearing in the channelBox.
				
		"""
		return self.query(labelWidth=True)
	#----------------------------------------------------------------------
	def set_labelWidth(self, value):
		"""
		
				An optional flag which is used to modify the width assigned
				to labels appearing in the channelBox.
				
		"""
		self.edit(labelWidth=value)
	#----------------------------------------------------------------------
	labelWidth = property(get_labelWidth, set_labelWidth)
	#----------------------------------------------------------------------
	def get_longNames(self):
		"""
		
				Controls whether long or short attribute names will be used
				in the interface.  Note that this flag is ignored if the -niceNames
				flag is set.  Default is short names. Queried, returns a boolean.
				
		"""
		return self.query(longNames=True)
	#----------------------------------------------------------------------
	def set_longNames(self, value):
		"""
		
				Controls whether long or short attribute names will be used
				in the interface.  Note that this flag is ignored if the -niceNames
				flag is set.  Default is short names. Queried, returns a boolean.
				
		"""
		self.edit(longNames=value)
	#----------------------------------------------------------------------
	longNames = property(get_longNames, set_longNames)
	#----------------------------------------------------------------------
	def get_mainListConnection(self):
		"""
		
				Specifies the name of a selectionConnection object which the
				editor will use as its source of content.  The channel box will
				only display the (last) item contained in the selectionConnection object.
				If a NULL string ("") is specified, then the channel box will revert
				to its default behaviour of working on the active list.
				
		"""
		return self.query(mainListConnection=True)
	#----------------------------------------------------------------------
	def set_mainListConnection(self, value):
		"""
		
				Specifies the name of a selectionConnection object which the
				editor will use as its source of content.  The channel box will
				only display the (last) item contained in the selectionConnection object.
				If a NULL string ("") is specified, then the channel box will revert
				to its default behaviour of working on the active list.
				
		"""
		self.edit(mainListConnection=value)
	#----------------------------------------------------------------------
	mainListConnection = property(get_mainListConnection, set_mainListConnection)
	#----------------------------------------------------------------------
	@property
	def mainObjectList(self):
		"""
		
				Returns a list of strings, the names of every object on the active
				list that is the same type as the object displayed in the top (main)
				section of the channel box.
				
		"""
		return self.query(mainObjectList=True)
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
	def get_maxHeight(self):
		"""
		
				An optional flag which is used to limit the height of the
				channelBox.
				
		"""
		return self.query(maxHeight=True)
	#----------------------------------------------------------------------
	def set_maxHeight(self, value):
		"""
		
				An optional flag which is used to limit the height of the
				channelBox.
				
		"""
		self.edit(maxHeight=value)
	#----------------------------------------------------------------------
	maxHeight = property(get_maxHeight, set_maxHeight)
	#----------------------------------------------------------------------
	def get_maxWidth(self):
		"""
		
				An optional flag which is used to limit the width of the
				channelBox.
				
		"""
		return self.query(maxWidth=True)
	#----------------------------------------------------------------------
	def set_maxWidth(self, value):
		"""
		
				An optional flag which is used to limit the width of the
				channelBox.
				
		"""
		self.edit(maxWidth=value)
	#----------------------------------------------------------------------
	maxWidth = property(get_maxWidth, set_maxWidth)
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
	def get_nodeRegex(self):
		"""
		
				Specifies a valid regular expression to specify which node names should
				(potentially) have their attributes selected for foreground text coloring.
				If nodeRegex is unspecified then it will assume a value of "*' for a
				regular expression. The same idea simultaneously applies to the flag
				attrRegex. The attrColor flag is required to be specified.
				Note: this regular expression will be treated as though it were case-insensitve
				Note: nodes in namespaces have regular expressions applied as though those
				nodes weren't in namespaces
				
		"""
		return self.query(nodeRegex=True)
	#----------------------------------------------------------------------
	def set_nodeRegex(self, value):
		"""
		
				Specifies a valid regular expression to specify which node names should
				(potentially) have their attributes selected for foreground text coloring.
				If nodeRegex is unspecified then it will assume a value of "*' for a
				regular expression. The same idea simultaneously applies to the flag
				attrRegex. The attrColor flag is required to be specified.
				Note: this regular expression will be treated as though it were case-insensitve
				Note: nodes in namespaces have regular expressions applied as though those
				nodes weren't in namespaces
				
		"""
		self.edit(nodeRegex=value)
	#----------------------------------------------------------------------
	nodeRegex = property(get_nodeRegex, set_nodeRegex)
	#----------------------------------------------------------------------
	@property
	def numberOfPopupMenus(self):
		"""
		
				Return the number of popup menus attached to this control.
				
		"""
		return self.query(numberOfPopupMenus=True)
	#----------------------------------------------------------------------
	@property
	def outputObjectList(self):
		"""
		
				Returns a list of strings, the names of every OUTPUT node associated
				an object on the main object list that is of the same type as the node
				displayed in the OUTPUT section of the channel box.
				
		"""
		return self.query(outputObjectList=True)
	#----------------------------------------------------------------------
	@property
	def outputs(self):
		"""
		
				Returns the items shown under the 'OUTPUTS' heading in the channel box.
				
		"""
		return self.query(outputs=True)
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
	def get_precision(self):
		"""
		
				Controls the number of digits to the right of the decimal
				point that will be displayed for float-valued channels.
				Default is 3.  Queried, returns an int.
				
		"""
		return self.query(precision=True)
	#----------------------------------------------------------------------
	def set_precision(self, value):
		"""
		
				Controls the number of digits to the right of the decimal
				point that will be displayed for float-valued channels.
				Default is 3.  Queried, returns an int.
				
		"""
		self.edit(precision=value)
	#----------------------------------------------------------------------
	precision = property(get_precision, set_precision)
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
	def select(self,value):
		"""
		
				Allows programmatic selection of items (nodes or plugs) in the channel box.
				Selection is equivalent to clicking the item with the mouse; therefore
				only items currently shown in the channel box can be selected this way.
				
		"""
		self.edit(select=value)
	#----------------------------------------------------------------------
	@property
	def selectedHistoryAttributes(self):
		"""
		
				Returns a list of strings, the names of all the selected attributes
				in the INPUT section of the channel box.
				
		"""
		return self.query(selectedHistoryAttributes=True)
	#----------------------------------------------------------------------
	@property
	def selectedMainAttributes(self):
		"""
		
				Returns a list of strings, the names of all the selected attributes in the
				top section of the channel box.
				
		"""
		return self.query(selectedMainAttributes=True)
	#----------------------------------------------------------------------
	@property
	def selectedOutputAttributes(self):
		"""
		
				Returns a list of strings, the names of all the selected attributes
				in the OUTPUT section of the channel box.
				
		"""
		return self.query(selectedOutputAttributes=True)
	#----------------------------------------------------------------------
	@property
	def selectedShapeAttributes(self):
		"""
		
				Returns a list of strings, the names of all the selected attributes
				in the middle (shape) section of the channel box.
				
		"""
		return self.query(selectedShapeAttributes=True)
	#----------------------------------------------------------------------
	@property
	def shapeObjectList(self):
		"""
		
				Returns a list of strings, the names of every shape associated with
				an object on the main object list that is of the same type as the object
				displayed in the middle (shape) section of the channel box.
				
		"""
		return self.query(shapeObjectList=True)
	#----------------------------------------------------------------------
	@property
	def shapes(self):
		"""
		
				Returns the items shown under the 'SHAPES' heading in the channel box.
				
		"""
		return self.query(shapes=True)
	#----------------------------------------------------------------------
	def get_showNamespace(self):
		"""
		
				Controls whether or not the namespace of an object is displayed
				if the object is not in the root namespace.
				
		"""
		return self.query(showNamespace=True)
	#----------------------------------------------------------------------
	def set_showNamespace(self, value):
		"""
		
				Controls whether or not the namespace of an object is displayed
				if the object is not in the root namespace.
				
		"""
		self.edit(showNamespace=value)
	#----------------------------------------------------------------------
	showNamespace = property(get_showNamespace, set_showNamespace)
	#----------------------------------------------------------------------
	def get_showTransforms(self):
		"""
		
				Controls whether this control will display transform attributes
				only, or all other attributes. False by default. Queried, returns a
				boolean.
				
		"""
		return self.query(showTransforms=True)
	#----------------------------------------------------------------------
	def set_showTransforms(self, value):
		"""
		
				Controls whether this control will display transform attributes
				only, or all other attributes. False by default. Queried, returns a
				boolean.
				
		"""
		self.edit(showTransforms=value)
	#----------------------------------------------------------------------
	showTransforms = property(get_showTransforms, set_showTransforms)
	#----------------------------------------------------------------------
	def get_speed(self):
		"""
		
				Controls the speed at which the attributes are changed based on the
				distance the mouse has been dragged.  Common settings for
				slow/medium/fast are 0.1/1.0/10.0 respectively.  The default is 1.0.
				
		"""
		return self.query(speed=True)
	#----------------------------------------------------------------------
	def set_speed(self, value):
		"""
		
				Controls the speed at which the attributes are changed based on the
				distance the mouse has been dragged.  Common settings for
				slow/medium/fast are 0.1/1.0/10.0 respectively.  The default is 1.0.
				
		"""
		self.edit(speed=value)
	#----------------------------------------------------------------------
	speed = property(get_speed, set_speed)
	#----------------------------------------------------------------------
	def statusBarMessage(self,value):
		"""
		
				Extra string to display in the status bar when the mouse is over the control.
				
		"""
		self.edit(statusBarMessage=value)
	#----------------------------------------------------------------------
	def takeFocus(self,value):
		"""
		
				causes the channel box to take over the keyboard focus, if it can.
				
		"""
		self.edit(takeFocus=value)
	#----------------------------------------------------------------------
	def update(self,value):
		"""
		
				This flag can be used to force an update of the channel box display, for
				example after changing a display preference.
				
		"""
		self.edit(update=value)
	#----------------------------------------------------------------------
	def get_useManips(self):
		"""
		
				When you click on a field or label in the channel box, the
				tool switches to a manipulator that can change that value if you
				drag in the 3d view.  This flag controls the kind of manips.  Allowed
				values are "none" (self-explanatory), "invisible" (you won't see anything,
				but dragging in the window will adjust any of the selected attributes),
				and "standard" (the same as invisible, except for scale, rotate, and
				translate, which will be represented by their usual manips.)
				
		"""
		return self.query(useManips=True)
	#----------------------------------------------------------------------
	def set_useManips(self, value):
		"""
		
				When you click on a field or label in the channel box, the
				tool switches to a manipulator that can change that value if you
				drag in the 3d view.  This flag controls the kind of manips.  Allowed
				values are "none" (self-explanatory), "invisible" (you won't see anything,
				but dragging in the window will adjust any of the selected attributes),
				and "standard" (the same as invisible, except for scale, rotate, and
				translate, which will be represented by their usual manips.)
				
		"""
		self.edit(useManips=value)
	#----------------------------------------------------------------------
	useManips = property(get_useManips, set_useManips)
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