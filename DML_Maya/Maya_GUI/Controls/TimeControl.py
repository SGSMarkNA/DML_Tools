

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class TimeControl(UI_Object.UI):
	"""
	This command creates a control that can be used for
	changing current time, displaying/editing keys, and
	displaying/scrubbing sound.: only one timeControl may be created.  The one Maya creates
	on startup can be accessed from the global string variable $gPlayBackSlider.
	Also, it is not a good idea to delete it.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.timeControl(**kwargs)
			super(TimeControl, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.timeControl(name, exists=True):
				super(TimeControl, self).__init__(name)
			else:
				name = cmds.timeControl(name, **kwargs)
				super(TimeControl, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def animCurveNames(self):
		"""
		
				When "showKeys" is not "none", querying this flag will
				return the names of all the animCurves for which keyframe
				ticks are being displayed.  Query returns string[].
				
		"""
		return self.query(animCurveNames=True)
	#----------------------------------------------------------------------
	def get_animLayerFilterOptions(self):
		"""
		
				Specifies whether a filter is to be applied when displaying animation layers.
				If so, the options can be "allAffecting" (no filter), "active" (only the active
				layers on the object will be displayed) and "animLayerEditor" (the settings will
				be taken from the animation layer editor).
				
		"""
		return self.query(animLayerFilterOptions=True)
	#----------------------------------------------------------------------
	def set_animLayerFilterOptions(self, value):
		"""
		
				Specifies whether a filter is to be applied when displaying animation layers.
				If so, the options can be "allAffecting" (no filter), "active" (only the active
				layers on the object will be displayed) and "animLayerEditor" (the settings will
				be taken from the animation layer editor).
				
		"""
		self.edit(animLayerFilterOptions=value)
	#----------------------------------------------------------------------
	animLayerFilterOptions = property(get_animLayerFilterOptions, set_animLayerFilterOptions)
	#----------------------------------------------------------------------
	def get_animLayerShowWeight(self):
		"""
		
				Specifies or queries whether weights are to be shown when displaying animation layers.
				
		"""
		return self.query(animLayerShowWeight=True)
	#----------------------------------------------------------------------
	def set_animLayerShowWeight(self, value):
		"""
		
				Specifies or queries whether weights are to be shown when displaying animation layers.
				
		"""
		self.edit(animLayerShowWeight=value)
	#----------------------------------------------------------------------
	animLayerShowWeight = property(get_animLayerShowWeight, set_animLayerShowWeight)
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
	def beginScrub(self,value):
		"""
		
				Set this widget up for sound scrubbing.
				Subsequent changes to current time will result
				in "sound scrubbing" behavior, until the
				"-endScrub" command is issued for this widget.
				
		"""
		self.edit(beginScrub=value)
	#----------------------------------------------------------------------
	def currentFrameColor(self,value):
		"""
		
				This flag is used to specify the rgba color of the
				current frame overlay rectangle in the timeControl.
				
		"""
		self.edit(currentFrameColor=value)
	#----------------------------------------------------------------------
	def get_displaySound(self):
		"""
		
				Turn sound display off.  Query returns int.
				
		"""
		return self.query(displaySound=True)
	#----------------------------------------------------------------------
	def set_displaySound(self, value):
		"""
		
				Turn sound display off.  Query returns int.
				
		"""
		self.edit(displaySound=value)
	#----------------------------------------------------------------------
	displaySound = property(get_displaySound, set_displaySound)
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
	def endScrub(self,value):
		"""
		
				End sound scubbing for this widget.  This stops
				sound scrubbing behavior and should be issued
				before any subsequent "-beginScrub" flags
				
		"""
		self.edit(endScrub=value)
	#----------------------------------------------------------------------
	def forceRedraw(self,value):
		"""
		
				Force a redraw of the time control UI. Similiar to forceRefresh but
				does not rebuild key information.
				
		"""
		self.edit(forceRedraw=value)
	#----------------------------------------------------------------------
	def forceRefresh(self,value):
		"""
		
				Force a refresh of the time control UI.
				
		"""
		self.edit(forceRefresh=value)
	#----------------------------------------------------------------------
	def foregroundColor(self,value):
		"""
		
				This flag is used to specify the rgb color of the
				vertical lines and numeric text in the timeControl.
				
		"""
		self.edit(foregroundColor=value)
	#----------------------------------------------------------------------
	@property
	def fullPathName(self):
		"""
		
				Return the full path name of the widget, which includes all the parents.
				
		"""
		return self.query(fullPathName=True)
	#----------------------------------------------------------------------
	def get_globalTime(self):
		"""
		
				"true" means this widget controls and displays the global,
				dependency graph time.  "false" means time changes here
				do NOT affect the dependency graph. Query returns int.
				
		"""
		return self.query(globalTime=True)
	#----------------------------------------------------------------------
	def set_globalTime(self, value):
		"""
		
				"true" means this widget controls and displays the global,
				dependency graph time.  "false" means time changes here
				do NOT affect the dependency graph. Query returns int.
				
		"""
		self.edit(globalTime=value)
	#----------------------------------------------------------------------
	globalTime = property(get_globalTime, set_globalTime)
	#----------------------------------------------------------------------
	@property
	def greasePencilSequenceNames(self):
		"""
		
				Returns the names of all grease pencil sequences that have
				frames being displayed in the time line.  Query returns string[].
				
		"""
		return self.query(greasePencilSequenceNames=True)
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
	def get_mainListConnection(self):
		"""
		
				Specifies the name of a selectionConnection object that the
				time slider will use as its source of content.  The time slider will
				only display keys for items contained in the selectionConnection object.
				
		"""
		return self.query(mainListConnection=True)
	#----------------------------------------------------------------------
	def set_mainListConnection(self, value):
		"""
		
				Specifies the name of a selectionConnection object that the
				time slider will use as its source of content.  The time slider will
				only display keys for items contained in the selectionConnection object.
				
		"""
		self.edit(mainListConnection=value)
	#----------------------------------------------------------------------
	mainListConnection = property(get_mainListConnection, set_mainListConnection)
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
	def pressCommand(self,value):
		"""
		
				script to run on mouse-down in this control.
				
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
	@property
	def range(self):
		"""
		
				Returns string representing the currently highlighted
				range visible on the time slider.  A range from 10 to 20
				would be returned as "10:20".  When there's no range
				visible on the time slider, the query returns a range
				spanning the current time: for example, "10:11".  These
				values are in the current time unit.
				
		"""
		return self.query(range=True)
	#----------------------------------------------------------------------
	@property
	def rangeArray(self):
		"""
		
				Returns a float array representing the currently highlighted
				range visible on the time slider.  A range from 10 to 20
				would be returned as { 10.0, 20.0 }.  When there's no range
				visible on the time slider, the query returns values spanning
				the current time: { 10.0, 11.0 }.  These values are in the current time unit.
				
		"""
		return self.query(rangeArray=True)
	#----------------------------------------------------------------------
	@property
	def rangeVisible(self):
		"""
		
				Returns true if a currently highlighted range is visible
				on the time slider, false if no.
				
		"""
		return self.query(rangeVisible=True)
	#----------------------------------------------------------------------
	def releaseCommand(self,value):
		"""
		
				script to run on mouse-up in this control.
				
		"""
		self.edit(releaseCommand=value)
	#----------------------------------------------------------------------
	def get_repeatChunkSize(self):
		"""
		
				How much sound (in the current time unit) is repeated
				when -repeatOnHold is true.  Default is 1.0.
				
		"""
		return self.query(repeatChunkSize=True)
	#----------------------------------------------------------------------
	def set_repeatChunkSize(self, value):
		"""
		
				How much sound (in the current time unit) is repeated
				when -repeatOnHold is true.  Default is 1.0.
				
		"""
		self.edit(repeatChunkSize=value)
	#----------------------------------------------------------------------
	repeatChunkSize = property(get_repeatChunkSize, set_repeatChunkSize)
	#----------------------------------------------------------------------
	def get_repeatOnHold(self):
		"""
		
				Repeat sound during mouse-down events
				
		"""
		return self.query(repeatOnHold=True)
	#----------------------------------------------------------------------
	def set_repeatOnHold(self, value):
		"""
		
				Repeat sound during mouse-down events
				
		"""
		self.edit(repeatOnHold=value)
	#----------------------------------------------------------------------
	repeatOnHold = property(get_repeatOnHold, set_repeatOnHold)
	#----------------------------------------------------------------------
	def resample(self,value):
		"""
		
				Resample the sound display to fit the widget
				
		"""
		self.edit(resample=value)
	#----------------------------------------------------------------------
	def get_showGreaseFrames(self):
		"""
		
				"active" will show grease frames for the active camera.  "none"
				shows no grease frames.  "all" will show all grease frames.
				Default "active".  Query returns string.
				
		"""
		return self.query(showGreaseFrames=True)
	#----------------------------------------------------------------------
	def set_showGreaseFrames(self, value):
		"""
		
				"active" will show grease frames for the active camera.  "none"
				shows no grease frames.  "all" will show all grease frames.
				Default "active".  Query returns string.
				
		"""
		self.edit(showGreaseFrames=value)
	#----------------------------------------------------------------------
	showGreaseFrames = property(get_showGreaseFrames, set_showGreaseFrames)
	#----------------------------------------------------------------------
	def get_showKeys(self):
		"""
		
				"active" will show tick marks for keyframes on all active
				objects.  "none" shows no tick marks.  Any other name is
				taken as the name of a channel box whose selected attributes
				will display tick marks.  Default "active".  Query returns string.
				
		"""
		return self.query(showKeys=True)
	#----------------------------------------------------------------------
	def set_showKeys(self, value):
		"""
		
				"active" will show tick marks for keyframes on all active
				objects.  "none" shows no tick marks.  Any other name is
				taken as the name of a channel box whose selected attributes
				will display tick marks.  Default "active".  Query returns string.
				
		"""
		self.edit(showKeys=value)
	#----------------------------------------------------------------------
	showKeys = property(get_showKeys, set_showKeys)
	#----------------------------------------------------------------------
	def get_showKeysCombined(self):
		"""
		
				This flag can be used in conjunction with the showKeys flag to
				enable a combination of "active" + "channel box" behavior.
				Specifically, if channel box attributes are selected, tick marks will
				be shown for those attributes. If no channel box attributes are
				selected, tick marks will be shown for keyframes on all active objects.
				
		"""
		return self.query(showKeysCombined=True)
	#----------------------------------------------------------------------
	def set_showKeysCombined(self, value):
		"""
		
				This flag can be used in conjunction with the showKeys flag to
				enable a combination of "active" + "channel box" behavior.
				Specifically, if channel box attributes are selected, tick marks will
				be shown for those attributes. If no channel box attributes are
				selected, tick marks will be shown for keyframes on all active objects.
				
		"""
		self.edit(showKeysCombined=value)
	#----------------------------------------------------------------------
	showKeysCombined = property(get_showKeysCombined, set_showKeysCombined)
	#----------------------------------------------------------------------
	def get_snap(self):
		"""
		
				"true" means this widget is constrained to having
				values that are integers representing the current time unit..
				"false" means the current time indicator is "free floating"
				and not constrained.
				
		"""
		return self.query(snap=True)
	#----------------------------------------------------------------------
	def set_snap(self, value):
		"""
		
				"true" means this widget is constrained to having
				values that are integers representing the current time unit..
				"false" means the current time indicator is "free floating"
				and not constrained.
				
		"""
		self.edit(snap=value)
	#----------------------------------------------------------------------
	snap = property(get_snap, set_snap)
	#----------------------------------------------------------------------
	def get_sound(self):
		"""
		
				Name of audio depend node whose data should display in the
				sound-display widget. Query returns string.
				
		"""
		return self.query(sound=True)
	#----------------------------------------------------------------------
	def set_sound(self, value):
		"""
		
				Name of audio depend node whose data should display in the
				sound-display widget. Query returns string.
				
		"""
		self.edit(sound=value)
	#----------------------------------------------------------------------
	sound = property(get_sound, set_sound)
	#----------------------------------------------------------------------
	def statusBarMessage(self,value):
		"""
		
				Extra string to display in the status bar when the mouse is over the control.
				
		"""
		self.edit(statusBarMessage=value)
	#----------------------------------------------------------------------
	def get_tickSize(self):
		"""
		
				Specifies the width of keyframe ticks drawn in the time slider.
				The value will be clamped to the range [1, 63].
				
		"""
		return self.query(tickSize=True)
	#----------------------------------------------------------------------
	def set_tickSize(self, value):
		"""
		
				Specifies the width of keyframe ticks drawn in the time slider.
				The value will be clamped to the range [1, 63].
				
		"""
		self.edit(tickSize=value)
	#----------------------------------------------------------------------
	tickSize = property(get_tickSize, set_tickSize)
	#----------------------------------------------------------------------
	def get_tickSpan(self):
		"""
		
				Specifies the interval between keyframe ticks in the timeControl. For example,
				a value of 10, will place ticks at 0, 10, 20, etc.
				
		"""
		return self.query(tickSpan=True)
	#----------------------------------------------------------------------
	def set_tickSpan(self, value):
		"""
		
				Specifies the interval between keyframe ticks in the timeControl. For example,
				a value of 10, will place ticks at 0, 10, 20, etc.
				
		"""
		self.edit(tickSpan=value)
	#----------------------------------------------------------------------
	tickSpan = property(get_tickSpan, set_tickSpan)
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
	def get_waveform(self):
		"""
		
				Determines what part of the sound waveform to display,
				when -displaySound is "true". Valid values are "top", "bottom",
				and "both".  Default is "top". Query returns string.
				
		"""
		return self.query(waveform=True)
	#----------------------------------------------------------------------
	def set_waveform(self, value):
		"""
		
				Determines what part of the sound waveform to display,
				when -displaySound is "true". Valid values are "top", "bottom",
				and "both".  Default is "top". Query returns string.
				
		"""
		self.edit(waveform=value)
	#----------------------------------------------------------------------
	waveform = property(get_waveform, set_waveform)
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