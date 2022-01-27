

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class AttrFieldSliderGrp(UI_Object.UI):
	"""
	All of the group commands position their individual controls in columns
	starting at column 1.  The layout of each control (ie. column) can be
	customized using the , and
	 flags.  By default, columns are left aligned
	with no offset and are 100 pixels wide.  Only one column in any group can
	be adjustable.
	
	This command creates a pre-packaged collection of label text, float
	field and float slider (for values with a min or max specified)
	The group
	also supports the notion of a larger secondary range of possible
	field values.
	
	If an attribute is specified for this object, then it will use any
	min and max values defined in the attribute.  The user-specified
	values can reduce the min and max, but cannot expand them.
	
	The field created here
	is an expression field -- while normally operating
	as a float field, the user can type in any expression starting with
	the character "=".  This will expand the field to occupy the space
	previously taken by the slider.
	
	The field also has
	an automatic menu brought up by the right mouse button.
	The contents of this menu change depending on the state of
	the attribute being watched by the field.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.attrFieldSliderGrp(**kwargs)
			super(AttrFieldSliderGrp, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.attrFieldSliderGrp(name, exists=True):
				super(AttrFieldSliderGrp, self).__init__(name)
			else:
				name = cmds.attrFieldSliderGrp(name, **kwargs)
				super(AttrFieldSliderGrp, self).__init__(name, **dict(qtParent=parent))
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
	def get_attribute(self):
		"""
		
				The name of a unique attribute of type double or int.
				This newly created field will be attached to the attribute, so
				that modifications to one will change the other.
				
		"""
		return self.query(attribute=True)
	#----------------------------------------------------------------------
	def set_attribute(self, value):
		"""
		
				The name of a unique attribute of type double or int.
				This newly created field will be attached to the attribute, so
				that modifications to one will change the other.
				
		"""
		self.edit(attribute=value)
	#----------------------------------------------------------------------
	attribute = property(get_attribute, set_attribute)
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
		
				The command string is executed when the value of the slider
				or floatField changes.  It will be executed only once after a
				drag of the slider.
				
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
	def extraButtonCommand(self,value):
		"""
		
				The command string is executed when the extra button is clicked.
				
		"""
		self.edit(extraButtonCommand=value)
	#----------------------------------------------------------------------
	def get_extraButtonIcon(self):
		"""
		
				The icon file name of the extra button.
				
		"""
		return self.query(extraButtonIcon=True)
	#----------------------------------------------------------------------
	def set_extraButtonIcon(self, value):
		"""
		
				The icon file name of the extra button.
				
		"""
		self.edit(extraButtonIcon=value)
	#----------------------------------------------------------------------
	extraButtonIcon = property(get_extraButtonIcon, set_extraButtonIcon)
	#----------------------------------------------------------------------
	def get_fieldMaxValue(self):
		"""
		
				Set the maximum value for the field.  This flag allows you
				to specify a maximum bound for the field higher than that
				of the slider.   (See note above
				about max and min values.)
				
		"""
		return self.query(fieldMaxValue=True)
	#----------------------------------------------------------------------
	def set_fieldMaxValue(self, value):
		"""
		
				Set the maximum value for the field.  This flag allows you
				to specify a maximum bound for the field higher than that
				of the slider.   (See note above
				about max and min values.)
				
		"""
		self.edit(fieldMaxValue=value)
	#----------------------------------------------------------------------
	fieldMaxValue = property(get_fieldMaxValue, set_fieldMaxValue)
	#----------------------------------------------------------------------
	def get_fieldMinValue(self):
		"""
		
				Set the minimum value for the field.  This flag allows you
				to specify a minimum bound for the field lower than that of
				the slider.  (See note above
				about max and min values.)
				
		"""
		return self.query(fieldMinValue=True)
	#----------------------------------------------------------------------
	def set_fieldMinValue(self, value):
		"""
		
				Set the minimum value for the field.  This flag allows you
				to specify a minimum bound for the field lower than that of
				the slider.  (See note above
				about max and min values.)
				
		"""
		self.edit(fieldMinValue=value)
	#----------------------------------------------------------------------
	fieldMinValue = property(get_fieldMinValue, set_fieldMinValue)
	#----------------------------------------------------------------------
	def get_fieldStep(self):
		"""
		
				Sets the increment for the float field.
				
		"""
		return self.query(fieldStep=True)
	#----------------------------------------------------------------------
	def set_fieldStep(self, value):
		"""
		
				Sets the increment for the float field.
				
		"""
		self.edit(fieldStep=value)
	#----------------------------------------------------------------------
	fieldStep = property(get_fieldStep, set_fieldStep)
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
	def get_label(self):
		"""
		
				By default, the label of this field will be the name of the
				attribute.  This flag can be used to override that name with
				whatever string you want.
				
		"""
		return self.query(label=True)
	#----------------------------------------------------------------------
	def set_label(self, value):
		"""
		
				By default, the label of this field will be the name of the
				attribute.  This flag can be used to override that name with
				whatever string you want.
				
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
	def get_maxValue(self):
		"""
		
				Sets the maximum value for both the slider and the field.
				(See note above about min and max values)
				
		"""
		return self.query(maxValue=True)
	#----------------------------------------------------------------------
	def set_maxValue(self, value):
		"""
		
				Sets the maximum value for both the slider and the field.
				(See note above about min and max values)
				
		"""
		self.edit(maxValue=value)
	#----------------------------------------------------------------------
	maxValue = property(get_maxValue, set_maxValue)
	#----------------------------------------------------------------------
	def get_minValue(self):
		"""
		
				Sets the minimum value for both the slider and the field.
				(by default max and min are set according to what is in the
				attribute, if anything.  If no max and min are specified,
				or if only one of the two are specified, then no slider
				is created.)
				
		"""
		return self.query(minValue=True)
	#----------------------------------------------------------------------
	def set_minValue(self, value):
		"""
		
				Sets the minimum value for both the slider and the field.
				(by default max and min are set according to what is in the
				attribute, if anything.  If no max and min are specified,
				or if only one of the two are specified, then no slider
				is created.)
				
		"""
		self.edit(minValue=value)
	#----------------------------------------------------------------------
	minValue = property(get_minValue, set_minValue)
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
	def precision(self,value):
		"""
		
				Sets the number of digits to the right of the decimal.
				(If attached to an int attribute, this is automatically
				set to 0 and cannot be overridden.)
				
		"""
		self.edit(precision=value)
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
	def rowAttach(self,value):
		"""
		
				Arguments are : column, attachment type, offset.
				Possible attachments are: top | bottom | both.
				Specifies attachment types and offsets for the entire row.
				
		"""
		self.edit(rowAttach=value)
	#----------------------------------------------------------------------
	def get_sliderMaxValue(self):
		"""
		
				Set the maximum value for the slider.  The slider
				max will be clipped to the field max.
				
		"""
		return self.query(sliderMaxValue=True)
	#----------------------------------------------------------------------
	def set_sliderMaxValue(self, value):
		"""
		
				Set the maximum value for the slider.  The slider
				max will be clipped to the field max.
				
		"""
		self.edit(sliderMaxValue=value)
	#----------------------------------------------------------------------
	sliderMaxValue = property(get_sliderMaxValue, set_sliderMaxValue)
	#----------------------------------------------------------------------
	def get_sliderMinValue(self):
		"""
		
				Set the minimum value for the slider.  The slider min
				will be clipped to the field min.
				
		"""
		return self.query(sliderMinValue=True)
	#----------------------------------------------------------------------
	def set_sliderMinValue(self, value):
		"""
		
				Set the minimum value for the slider.  The slider min
				will be clipped to the field min.
				
		"""
		self.edit(sliderMinValue=value)
	#----------------------------------------------------------------------
	sliderMinValue = property(get_sliderMinValue, set_sliderMinValue)
	#----------------------------------------------------------------------
	def get_sliderStep(self):
		"""
		
				On Linux the slider step value represents the
				amount the value will increase or decrease when
				you click either side of the slider.
				
		"""
		return self.query(sliderStep=True)
	#----------------------------------------------------------------------
	def set_sliderStep(self, value):
		"""
		
				On Linux the slider step value represents the
				amount the value will increase or decrease when
				you click either side of the slider.
				
		"""
		self.edit(sliderStep=value)
	#----------------------------------------------------------------------
	sliderStep = property(get_sliderStep, set_sliderStep)
	#----------------------------------------------------------------------
	def statusBarMessage(self,value):
		"""
		
				Extra string to display in the status bar when the mouse is over the control.
				
		"""
		self.edit(statusBarMessage=value)
	#----------------------------------------------------------------------
	def get_step(self):
		"""
		
				Sets the increment for both the slider and float field.
				
		"""
		return self.query(step=True)
	#----------------------------------------------------------------------
	def set_step(self, value):
		"""
		
				Sets the increment for both the slider and float field.
				
		"""
		self.edit(step=value)
	#----------------------------------------------------------------------
	step = property(get_step, set_step)
	#----------------------------------------------------------------------
	@property
	def vertical(self):
		"""
		
				Whether the orientation of the controls in this group
				are horizontal (default) or vertical.
				
		"""
		return self.query(vertical=True)
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