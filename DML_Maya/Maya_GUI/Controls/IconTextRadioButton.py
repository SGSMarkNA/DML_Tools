

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class IconTextRadioButton(UI_Object.UI):
	"""
	This control supports up to 3 icon images and 4 different display
	styles.  The icon image displayed is the one that best fits the
	current size of the control given its current style.
	
	This command creates a iconTextRadioButton that is added to the most
	recently created iconTextRadioCollection unless the -cl/cluster flag is
	used.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.iconTextRadioButton(**kwargs)
			super(IconTextRadioButton, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.iconTextRadioButton(name, exists=True):
				super(IconTextRadioButton, self).__init__(name)
			else:
				name = cmds.iconTextRadioButton(name, **kwargs)
				super(IconTextRadioButton, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def get_align(self):
		"""
		
				The label alignment.  Alignment values are "left",
				"right", and "center". By default, the label is aligned "center".
				Currently only available when -st/style is set to "iconAndTextCentered".
				
		"""
		return self.query(align=True)
	#----------------------------------------------------------------------
	def set_align(self, value):
		"""
		
				The label alignment.  Alignment values are "left",
				"right", and "center". By default, the label is aligned "center".
				Currently only available when -st/style is set to "iconAndTextCentered".
				
		"""
		self.edit(align=value)
	#----------------------------------------------------------------------
	align = property(get_align, set_align)
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
	def get_changeCommand(self):
		"""
		
				Command executed when the control's state is changed.
				Note that this flag should not be used in conjunction with
				onCommand and offCommand. That is, one should either use
				changeCommand and test the state of the control from inside
				the callback, or use onCommand and offCommand as separate
				callbacks.
				
		"""
		return self.query(changeCommand=True)
	#----------------------------------------------------------------------
	def set_changeCommand(self, value):
		"""
		
				Command executed when the control's state is changed.
				Note that this flag should not be used in conjunction with
				onCommand and offCommand. That is, one should either use
				changeCommand and test the state of the control from inside
				the callback, or use onCommand and offCommand as separate
				callbacks.
				
		"""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	changeCommand = property(get_changeCommand, set_changeCommand)
	#----------------------------------------------------------------------
	def get_disabledImage(self):
		"""
		
				Image used when the button is disabled. Image size must
				be the same as the image specified with the i/image flag.
				This is a Windows only flag.
				
		"""
		return self.query(disabledImage=True)
	#----------------------------------------------------------------------
	def set_disabledImage(self, value):
		"""
		
				Image used when the button is disabled. Image size must
				be the same as the image specified with the i/image flag.
				This is a Windows only flag.
				
		"""
		self.edit(disabledImage=value)
	#----------------------------------------------------------------------
	disabledImage = property(get_disabledImage, set_disabledImage)
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
	def get_flat(self):
		"""
		
				Sets whether the control will be a flat button (0 false, 1 true).
				
		"""
		return self.query(flat=True)
	#----------------------------------------------------------------------
	def set_flat(self, value):
		"""
		
				Sets whether the control will be a flat button (0 false, 1 true).
				
		"""
		self.edit(flat=value)
	#----------------------------------------------------------------------
	flat = property(get_flat, set_flat)
	#----------------------------------------------------------------------
	def get_flipX(self):
		"""
		
				Is the image flipped horizontally?
				
		"""
		return self.query(flipX=True)
	#----------------------------------------------------------------------
	def set_flipX(self, value):
		"""
		
				Is the image flipped horizontally?
				
		"""
		self.edit(flipX=value)
	#----------------------------------------------------------------------
	flipX = property(get_flipX, set_flipX)
	#----------------------------------------------------------------------
	def get_flipY(self):
		"""
		
				Is the image flipped vertically?
				
		"""
		return self.query(flipY=True)
	#----------------------------------------------------------------------
	def set_flipY(self, value):
		"""
		
				Is the image flipped vertically?
				
		"""
		self.edit(flipY=value)
	#----------------------------------------------------------------------
	flipY = property(get_flipY, set_flipY)
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
	def get_highlightImage(self):
		"""
		
				Highlight image displayed while the cursor is over the
				control. Image size must be the same as the image specified with
				the -i/image flag. This is a Windows only flag.
				
		"""
		return self.query(highlightImage=True)
	#----------------------------------------------------------------------
	def set_highlightImage(self, value):
		"""
		
				Highlight image displayed while the cursor is over the
				control. Image size must be the same as the image specified with
				the -i/image flag. This is a Windows only flag.
				
		"""
		self.edit(highlightImage=value)
	#----------------------------------------------------------------------
	highlightImage = property(get_highlightImage, set_highlightImage)
	#----------------------------------------------------------------------
	def get_image(self):
		"""
		
				If you are not providing images with different sizes then you may
				use this flag for the control's image. If the "iconOnly" style is
				set, the icon will be scaled to the size of the control.
				
		"""
		return self.query(image=True)
	#----------------------------------------------------------------------
	def set_image(self, value):
		"""
		
				If you are not providing images with different sizes then you may
				use this flag for the control's image. If the "iconOnly" style is
				set, the icon will be scaled to the size of the control.
				
		"""
		self.edit(image=value)
	#----------------------------------------------------------------------
	image = property(get_image, set_image)
	#----------------------------------------------------------------------
	def get_image1(self):
		"""
		
				First of three possible icons. The icon that best fits the
				current size of the control will be displayed.
				
		"""
		return self.query(image1=True)
	#----------------------------------------------------------------------
	def set_image1(self, value):
		"""
		
				First of three possible icons. The icon that best fits the
				current size of the control will be displayed.
				
		"""
		self.edit(image1=value)
	#----------------------------------------------------------------------
	image1 = property(get_image1, set_image1)
	#----------------------------------------------------------------------
	def get_image2(self):
		"""
		
				Second of three possible icons. The icon that best fits the
				current size of the control will be displayed.
				
		"""
		return self.query(image2=True)
	#----------------------------------------------------------------------
	def set_image2(self, value):
		"""
		
				Second of three possible icons. The icon that best fits the
				current size of the control will be displayed.
				
		"""
		self.edit(image2=value)
	#----------------------------------------------------------------------
	image2 = property(get_image2, set_image2)
	#----------------------------------------------------------------------
	def get_image3(self):
		"""
		
				Third of three possible icons. The icon that best fits the
				current size of the control will be displayed.
				
		"""
		return self.query(image3=True)
	#----------------------------------------------------------------------
	def set_image3(self, value):
		"""
		
				Third of three possible icons. The icon that best fits the
				current size of the control will be displayed.
				
		"""
		self.edit(image3=value)
	#----------------------------------------------------------------------
	image3 = property(get_image3, set_image3)
	#----------------------------------------------------------------------
	def get_imageOverlayLabel(self):
		"""
		
				A short string, up to 6 characters, representing a label that will be displayed
				on top of the image.
				
		"""
		return self.query(imageOverlayLabel=True)
	#----------------------------------------------------------------------
	def set_imageOverlayLabel(self, value):
		"""
		
				A short string, up to 6 characters, representing a label that will be displayed
				on top of the image.
				
		"""
		self.edit(imageOverlayLabel=value)
	#----------------------------------------------------------------------
	imageOverlayLabel = property(get_imageOverlayLabel, set_imageOverlayLabel)
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
		
				The text that appears in the control.
				
		"""
		return self.query(label=True)
	#----------------------------------------------------------------------
	def set_label(self, value):
		"""
		
				The text that appears in the control.
				
		"""
		self.edit(label=value)
	#----------------------------------------------------------------------
	label = property(get_label, set_label)
	#----------------------------------------------------------------------
	def get_labelOffset(self):
		"""
		
				The label offset. Default is 0. Currently only available
				when -st/style is set to "iconAndTextCentered".
				
		"""
		return self.query(labelOffset=True)
	#----------------------------------------------------------------------
	def set_labelOffset(self, value):
		"""
		
				The label offset. Default is 0. Currently only available
				when -st/style is set to "iconAndTextCentered".
				
		"""
		self.edit(labelOffset=value)
	#----------------------------------------------------------------------
	labelOffset = property(get_labelOffset, set_labelOffset)
	#----------------------------------------------------------------------
	def get_ltVersion(self):
		"""
		
				This flag is used to specify the Maya LT version that this control
				feature was introduced, if the version flag is not specified, or
				if the version flag is specified but its argument is different.
				This value is only used by Maya LT, and otherwise ignored.
				The argument should be given as a string of the version number
				(e.g. "2013", "2014"). Currently only accepts major version
				numbers (e.g. 2013 Ext 1, or 2013.5 should be given as "2014").
				
		"""
		return self.query(ltVersion=True)
	#----------------------------------------------------------------------
	def set_ltVersion(self, value):
		"""
		
				This flag is used to specify the Maya LT version that this control
				feature was introduced, if the version flag is not specified, or
				if the version flag is specified but its argument is different.
				This value is only used by Maya LT, and otherwise ignored.
				The argument should be given as a string of the version number
				(e.g. "2013", "2014"). Currently only accepts major version
				numbers (e.g. 2013 Ext 1, or 2013.5 should be given as "2014").
				
		"""
		self.edit(ltVersion=value)
	#----------------------------------------------------------------------
	ltVersion = property(get_ltVersion, set_ltVersion)
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
	def get_marginHeight(self):
		"""
		
				The number of pixels above and below the control content.
				The default value is 1 pixel.
				
		"""
		return self.query(marginHeight=True)
	#----------------------------------------------------------------------
	def set_marginHeight(self, value):
		"""
		
				The number of pixels above and below the control content.
				The default value is 1 pixel.
				
		"""
		self.edit(marginHeight=value)
	#----------------------------------------------------------------------
	marginHeight = property(get_marginHeight, set_marginHeight)
	#----------------------------------------------------------------------
	def get_marginWidth(self):
		"""
		
				The number of pixels on either side of the control content.
				The default value is 1 pixel.
				
		"""
		return self.query(marginWidth=True)
	#----------------------------------------------------------------------
	def set_marginWidth(self, value):
		"""
		
				The number of pixels on either side of the control content.
				The default value is 1 pixel.
				
		"""
		self.edit(marginWidth=value)
	#----------------------------------------------------------------------
	marginWidth = property(get_marginWidth, set_marginWidth)
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
	def get_offCommand(self):
		"""
		
				Command executed when the control is turned off.
				
		"""
		return self.query(offCommand=True)
	#----------------------------------------------------------------------
	def set_offCommand(self, value):
		"""
		
				Command executed when the control is turned off.
				
		"""
		self.edit(offCommand=value)
	#----------------------------------------------------------------------
	offCommand = property(get_offCommand, set_offCommand)
	#----------------------------------------------------------------------
	def get_onCommand(self):
		"""
		
				Command executed when the control is turned on.
				
		"""
		return self.query(onCommand=True)
	#----------------------------------------------------------------------
	def set_onCommand(self, value):
		"""
		
				Command executed when the control is turned on.
				
		"""
		self.edit(onCommand=value)
	#----------------------------------------------------------------------
	onCommand = property(get_onCommand, set_onCommand)
	#----------------------------------------------------------------------
	def get_overlayLabelBackColor(self):
		"""
		
				The RGBA color of the shadow behind the label defined by
				imageOverlayLabel. Default is 50% transparent black: 0 0 0 .5
				
		"""
		return self.query(overlayLabelBackColor=True)
	#----------------------------------------------------------------------
	def set_overlayLabelBackColor(self, value):
		"""
		
				The RGBA color of the shadow behind the label defined by
				imageOverlayLabel. Default is 50% transparent black: 0 0 0 .5
				
		"""
		self.edit(overlayLabelBackColor=value)
	#----------------------------------------------------------------------
	overlayLabelBackColor = property(get_overlayLabelBackColor, set_overlayLabelBackColor)
	#----------------------------------------------------------------------
	def get_overlayLabelColor(self):
		"""
		
				The RGB color of the label defined by imageOverlayLabel. Default is a
				light grey: .8 .8 .8
				
		"""
		return self.query(overlayLabelColor=True)
	#----------------------------------------------------------------------
	def set_overlayLabelColor(self, value):
		"""
		
				The RGB color of the label defined by imageOverlayLabel. Default is a
				light grey: .8 .8 .8
				
		"""
		self.edit(overlayLabelColor=value)
	#----------------------------------------------------------------------
	overlayLabelColor = property(get_overlayLabelColor, set_overlayLabelColor)
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
	def get_rotation(self):
		"""
		
				The rotation value of the image in radians.
				
		"""
		return self.query(rotation=True)
	#----------------------------------------------------------------------
	def set_rotation(self, value):
		"""
		
				The rotation value of the image in radians.
				
		"""
		self.edit(rotation=value)
	#----------------------------------------------------------------------
	rotation = property(get_rotation, set_rotation)
	#----------------------------------------------------------------------
	def get_select(self):
		"""
		
				Will set this button as the selected one.
				
		"""
		return self.query(select=True)
	#----------------------------------------------------------------------
	def set_select(self, value):
		"""
		
				Will set this button as the selected one.
				
		"""
		self.edit(select=value)
	#----------------------------------------------------------------------
	select = property(get_select, set_select)
	#----------------------------------------------------------------------
	def get_selectionHighlightImage(self):
		"""
		
				Image displayed while the control is selected and the cursor
				is over the control. Image size
				must be the same as the image specified with the -i/image
				flag. This is a Windows only flag.
				
		"""
		return self.query(selectionHighlightImage=True)
	#----------------------------------------------------------------------
	def set_selectionHighlightImage(self, value):
		"""
		
				Image displayed while the control is selected and the cursor
				is over the control. Image size
				must be the same as the image specified with the -i/image
				flag. This is a Windows only flag.
				
		"""
		self.edit(selectionHighlightImage=value)
	#----------------------------------------------------------------------
	selectionHighlightImage = property(get_selectionHighlightImage, set_selectionHighlightImage)
	#----------------------------------------------------------------------
	def get_selectionImage(self):
		"""
		
				Image displayed while the control is selected. Image size
				must be the same as the image specified with the -i/image
				flag. This is a Windows only flag.
				
		"""
		return self.query(selectionImage=True)
	#----------------------------------------------------------------------
	def set_selectionImage(self, value):
		"""
		
				Image displayed while the control is selected. Image size
				must be the same as the image specified with the -i/image
				flag. This is a Windows only flag.
				
		"""
		self.edit(selectionImage=value)
	#----------------------------------------------------------------------
	selectionImage = property(get_selectionImage, set_selectionImage)
	#----------------------------------------------------------------------
	def statusBarMessage(self,value):
		"""
		
				Extra string to display in the status bar when the mouse is over the control.
				
		"""
		self.edit(statusBarMessage=value)
	#----------------------------------------------------------------------
	def get_style(self):
		"""
		
				The draw style of the control.  Valid styles are "iconOnly",
				"textOnly", "iconAndTextHorizontal", "iconAndTextVertical", and
				"iconAndTextCentered". (Note: "iconAndTextCentered" is only available on Windows).
				If the "iconOnly" style is set, the icon will be scaled to the size of the control.
				
		"""
		return self.query(style=True)
	#----------------------------------------------------------------------
	def set_style(self, value):
		"""
		
				The draw style of the control.  Valid styles are "iconOnly",
				"textOnly", "iconAndTextHorizontal", "iconAndTextVertical", and
				"iconAndTextCentered". (Note: "iconAndTextCentered" is only available on Windows).
				If the "iconOnly" style is set, the icon will be scaled to the size of the control.
				
		"""
		self.edit(style=value)
	#----------------------------------------------------------------------
	style = property(get_style, set_style)
	#----------------------------------------------------------------------
	def get_useAlpha(self):
		"""
		
				Is the image using alpha channel?
				
		"""
		return self.query(useAlpha=True)
	#----------------------------------------------------------------------
	def set_useAlpha(self, value):
		"""
		
				Is the image using alpha channel?
				
		"""
		self.edit(useAlpha=value)
	#----------------------------------------------------------------------
	useAlpha = property(get_useAlpha, set_useAlpha)
	#----------------------------------------------------------------------
	def get_version(self):
		"""
		
				Specify the version that this control feature was introduced.
				The argument should be given as a string of the version number
				(e.g. "2013", "2014"). Currently only accepts major version
				numbers (e.g. 2013 Ext 1, or 2013.5 should be given as "2014").
				
		"""
		return self.query(version=True)
	#----------------------------------------------------------------------
	def set_version(self, value):
		"""
		
				Specify the version that this control feature was introduced.
				The argument should be given as a string of the version number
				(e.g. "2013", "2014"). Currently only accepts major version
				numbers (e.g. 2013 Ext 1, or 2013.5 should be given as "2014").
				
		"""
		self.edit(version=value)
	#----------------------------------------------------------------------
	version = property(get_version, set_version)
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