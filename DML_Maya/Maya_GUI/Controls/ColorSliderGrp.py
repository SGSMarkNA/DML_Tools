

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class ColorSliderGrp(UI_Object.UI):
	"""
	All of the group commands position their individual controls in columns
	starting at column 1.  The layout of each control (ie. column) can be
	customized using the , and
	 flags.  By default, columns are left aligned
	with no offset and are 100 pixels wide.  Only one column in any group can
	be adjustable.
	
	This command creates a color Slider group consisting of a label, a
	color canvas and a slider.  Clicking on the canvas will bring up
	the color editor dialog.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.colorSliderGrp(**kwargs)
			super(ColorSliderGrp, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.colorSliderGrp(name, exists=True):
				super(ColorSliderGrp, self).__init__(name)
			else:
				name = cmds.colorSliderGrp(name, **kwargs)
				super(ColorSliderGrp, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def adjustableColumn(self,value):
		"""
		
				Specifies which column has an adjustable size that changes with the
				sizing of the layout.  The column value is a 1-based index.
				Passing 0 as argument turns off the previous adjustable column.
				
		"""
		self.edit(adjustableColumn=value)
	#----------------------------------------------------------------------
	def adjustableColumn2(self,value):
		"""
		
				Specifies which column has an adjustable size that changes with
				the size of the parent layout. Ignored if there are not exactly
				two columns.
				
		"""
		self.edit(adjustableColumn2=value)
	#----------------------------------------------------------------------
	def adjustableColumn3(self,value):
		"""
		
				Specifies that the column has an adjustable size that changes with
				the size of the parent layout. Ignored if there are not exactly
				three columns.
				
		"""
		self.edit(adjustableColumn3=value)
	#----------------------------------------------------------------------
	def adjustableColumn4(self,value):
		"""
		
				Specifies which column has an adjustable size that changes with
				the size of the parent layout. Ignored if there are not exactly
				four columns.
				
		"""
		self.edit(adjustableColumn4=value)
	#----------------------------------------------------------------------
	def adjustableColumn5(self,value):
		"""
		
				Specifies which column has an adjustable size that changes with
				the size of the parent layout. Ignored if there are not exactly
				five columns.
				
		"""
		self.edit(adjustableColumn5=value)
	#----------------------------------------------------------------------
	def adjustableColumn6(self,value):
		"""
		
				Specifies which column has an adjustable size that changes with
				the size of the parent layout. Ignored if there are not exactly
				six columns.
				
		"""
		self.edit(adjustableColumn6=value)
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
		
				Command string executed when slider value changes.
				
		"""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	def columnAlign(self,value):
		"""
		
				Arguments are : column number, alignment type.
				Possible alignments are: left | right | center.
				Specifies alignment type for the specified column.
				
		"""
		self.edit(columnAlign=value)
	#----------------------------------------------------------------------
	def columnAlign2(self,value):
		"""
		
				Sets the text alignment of both columns.  Ignored if there are not
				exactly two columns. Valid values are "left", "right", and "center".
				
		"""
		self.edit(columnAlign2=value)
	#----------------------------------------------------------------------
	def columnAlign3(self,value):
		"""
		
				Sets the text alignment for all three columns.  Ignored if there are not
				exactly three columns. Valid values are "left", "right", and "center".
				
		"""
		self.edit(columnAlign3=value)
	#----------------------------------------------------------------------
	def columnAlign4(self,value):
		"""
		
				Sets the text alignment for all four columns.  Ignored if there are not
				exactly four columns. Valid values are "left", "right", and "center".
				
		"""
		self.edit(columnAlign4=value)
	#----------------------------------------------------------------------
	def columnAlign5(self,value):
		"""
		
				Sets the text alignment for all five columns.  Ignored if there are not
				exactly five columns. Valid values are "left", "right", and "center".
				
		"""
		self.edit(columnAlign5=value)
	#----------------------------------------------------------------------
	def columnAlign6(self,value):
		"""
		
				Sets the text alignment for all six columns.  Ignored if there are not
				exactly six columns. Valid values are "left", "right", and "center".
				
		"""
		self.edit(columnAlign6=value)
	#----------------------------------------------------------------------
	def columnAttach(self,value):
		"""
		
				Arguments are : column number, attachment type, and offset.
				Possible attachments are: left | right | both.
				Specifies column attachment types and offets.
				
		"""
		self.edit(columnAttach=value)
	#----------------------------------------------------------------------
	def columnAttach2(self,value):
		"""
		
				Sets the attachment type of both columns. Ignored if there are not
				exactly two columns. Valid values are "left", "right", and "both".
				
		"""
		self.edit(columnAttach2=value)
	#----------------------------------------------------------------------
	def columnAttach3(self,value):
		"""
		
				Sets the attachment type for all three columns. Ignored if there are not
				exactly three columns. Valid values are "left", "right", and "both".
				
		"""
		self.edit(columnAttach3=value)
	#----------------------------------------------------------------------
	def columnAttach4(self,value):
		"""
		
				Sets the attachment type for all four columns. Ignored if there are not
				exactly four columns. Valid values are "left", "right", and "both".
				
		"""
		self.edit(columnAttach4=value)
	#----------------------------------------------------------------------
	def columnAttach5(self,value):
		"""
		
				Sets the attachment type for all five columns. Ignored if there are not
				exactly five columns. Valid values are "left", "right", and "both".
				
		"""
		self.edit(columnAttach5=value)
	#----------------------------------------------------------------------
	def columnAttach6(self,value):
		"""
		
				Sets the attachment type for all six columns. Ignored if there are not
				exactly six columns. Valid values are "left", "right", and "both".
				
		"""
		self.edit(columnAttach6=value)
	#----------------------------------------------------------------------
	def columnOffset2(self,value):
		"""
		
				This flag is used in conjunction with the -columnAttach2 flag.  If that
				flag is not used then this flag will be ignored.  It sets the offset for
				the two columns.  The offsets applied are based on the attachments
				specified with the -columnAttach2 flag.  Ignored if there are not exactly
				two columns.
				
		"""
		self.edit(columnOffset2=value)
	#----------------------------------------------------------------------
	def columnOffset3(self,value):
		"""
		
				This flag is used in conjunction with the -columnAttach3 flag.  If that
				flag is not used then this flag will be ignored.  It sets the offset for
				the three columns.  The offsets applied are based on the attachments
				specified with the -columnAttach3 flag.  Ignored if there are not exactly
				three columns.
				
		"""
		self.edit(columnOffset3=value)
	#----------------------------------------------------------------------
	def columnOffset4(self,value):
		"""
		
				This flag is used in conjunction with the -columnAttach4 flag.  If that
				flag is not used then this flag will be ignored.  It sets the offset for
				the four columns.  The offsets applied are based on the attachments
				specified with the -columnAttach4 flag.  Ignored if there are not exactly
				four columns.
				
		"""
		self.edit(columnOffset4=value)
	#----------------------------------------------------------------------
	def columnOffset5(self,value):
		"""
		
				This flag is used in conjunction with the -columnAttach5 flag.  If that
				flag is not used then this flag will be ignored.  It sets the offset for
				the five columns.  The offsets applied are based on the attachments
				specified with the -columnAttach5 flag.  Ignored if there are not exactly
				five columns.
				
		"""
		self.edit(columnOffset5=value)
	#----------------------------------------------------------------------
	def columnOffset6(self,value):
		"""
		
				This flag is used in conjunction with the -columnAttach6 flag.  If that
				flag is not used then this flag will be ignored.  It sets the offset for
				the six columns.  The offsets applied are based on the attachments
				specified with the -columnAttach6 flag.  Ignored if there are not exactly
				six columns.
				
		"""
		self.edit(columnOffset6=value)
	#----------------------------------------------------------------------
	def columnWidth(self,value):
		"""
		
				Arguments are : column number, column width.
				Sets the width of the specified column where the first parameter specifies
				the column (1 based index) and the second parameter specifies the width.
				
		"""
		self.edit(columnWidth=value)
	#----------------------------------------------------------------------
	def columnWidth1(self,value):
		"""
		
				Sets the width of the first column. Ignored if there is not
				exactly one column.
				
		"""
		self.edit(columnWidth1=value)
	#----------------------------------------------------------------------
	def columnWidth2(self,value):
		"""
		
				Sets the column widths of both columns. Ignored if there are not
				exactly two columns.
				
		"""
		self.edit(columnWidth2=value)
	#----------------------------------------------------------------------
	def columnWidth3(self,value):
		"""
		
				Sets the column widths for all 3 columns. Ignored if there are not
				exactly 3 columns.
				
		"""
		self.edit(columnWidth3=value)
	#----------------------------------------------------------------------
	def columnWidth4(self,value):
		"""
		
				Sets the column widths for all 4 columns. Ignored if there are not
				exactly 4 columns.
				
		"""
		self.edit(columnWidth4=value)
	#----------------------------------------------------------------------
	def columnWidth5(self,value):
		"""
		
				Sets the column widths for all 5 columns. Ignored if there are not
				exactly 5 columns.
				
		"""
		self.edit(columnWidth5=value)
	#----------------------------------------------------------------------
	def columnWidth6(self,value):
		"""
		
				Sets the column widths for all 6 columns. Ignored if there are not
				exactly 6 columns.
				
		"""
		self.edit(columnWidth6=value)
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
	def dragCommand(self,value):
		"""
		
				Command string executed when slider value marker is dragged.
				
		"""
		self.edit(dragCommand=value)
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
	def get_forceDragRefresh(self):
		"""
		
				If used then force refresh on drag
				
		"""
		return self.query(forceDragRefresh=True)
	#----------------------------------------------------------------------
	def set_forceDragRefresh(self, value):
		"""
		
				If used then force refresh on drag
				
		"""
		self.edit(forceDragRefresh=value)
	#----------------------------------------------------------------------
	forceDragRefresh = property(get_forceDragRefresh, set_forceDragRefresh)
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
	def get_hsvValue(self):
		"""
		
				Color in hue, saturation, and value format.
				
		"""
		return self.query(hsvValue=True)
	#----------------------------------------------------------------------
	def set_hsvValue(self, value):
		"""
		
				Color in hue, saturation, and value format.
				
		"""
		self.edit(hsvValue=value)
	#----------------------------------------------------------------------
	hsvValue = property(get_hsvValue, set_hsvValue)
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
		
				Label text for the group.
				
		"""
		return self.query(label=True)
	#----------------------------------------------------------------------
	def set_label(self, value):
		"""
		
				Label text for the group.
				
		"""
		self.edit(label=value)
	#----------------------------------------------------------------------
	label = property(get_label, set_label)
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
	def get_rgbValue(self):
		"""
		
				Color in red, green, and blue format.
				
		"""
		return self.query(rgbValue=True)
	#----------------------------------------------------------------------
	def set_rgbValue(self, value):
		"""
		
				Color in red, green, and blue format.
				
		"""
		self.edit(rgbValue=value)
	#----------------------------------------------------------------------
	rgbValue = property(get_rgbValue, set_rgbValue)
	#----------------------------------------------------------------------
	def rowAttach(self,value):
		"""
		
				Arguments are : column, attachment type, offset.
				Possible attachments are: top | bottom | both.
				Specifies attachment types and offsets for the entire row.
				
		"""
		self.edit(rowAttach=value)
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