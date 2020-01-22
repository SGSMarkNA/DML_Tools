

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class ModelEditor(UI_Object.UI):
	"""
	Create, edit or query a model editor.
	
	Note that some of the flags of this command may have different settings
	for normal mode and for interactive/playback mode.  For example, a
	modelEditor can be set to use shaded mode normally, but to use wireframe
	during playback for greater speed.  Some flags also support having
	defaults set so that new model editors will be created with those settings.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.modelEditor(**kwargs)
			super(ModelEditor, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.modelEditor(name, exists=True):
				super(ModelEditor, self).__init__(name)
			else:
				name = cmds.modelEditor(name, **kwargs)
				super(ModelEditor, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def get_activeComponentsXray(self):
		"""Turns on or off Xray mode for active components."""
		return self.query(activeComponentsXray=True)
	#----------------------------------------------------------------------
	def set_activeComponentsXray(self, value):
		"""Turns on or off Xray mode for active components."""
		self.edit(activeComponentsXray=value)
	#----------------------------------------------------------------------
	activeComponentsXray = property(get_activeComponentsXray, set_activeComponentsXray)
	#----------------------------------------------------------------------
	def activeCustomEnvironment(self,value):
		"""		
			Specifies a path to an image file to be used as environment map.
			It is only enabled when a valid scene render filter is specified.	
		"""
		self.edit(activeCustomEnvironment=value)
	#----------------------------------------------------------------------
	def get_activeCustomGeometry(self):
		"""
			Specifies an identifier for custom geometry to override the geometry
			to display. It is only enabled when a valid scene render filter is specified.
		"""
		return self.query(activeCustomGeometry=True)
	#----------------------------------------------------------------------
	def set_activeCustomGeometry(self, value):
		"""
			Specifies an identifier for custom geometry to override the geometry
			to display. It is only enabled when a valid scene render filter is specified.
		"""
		self.edit(activeCustomGeometry=value)
	#----------------------------------------------------------------------
	activeCustomGeometry = property(get_activeCustomGeometry, set_activeCustomGeometry)
	#----------------------------------------------------------------------
	def get_activeCustomLighSet(self):
		"""
			Specifies an identifier for the light set to use
			with a scene render filter. It is only enabled when a valid scene render filter is specified.	
		"""
		return self.query(activeCustomLighSet=True)
	#----------------------------------------------------------------------
	def set_activeCustomLighSet(self, value):
		"""
				Specifies an identifier for the light set to use
				with a scene render filter. It is only enabled when a valid scene render filter is specified.
		"""
		self.edit(activeCustomLighSet=value)
	#----------------------------------------------------------------------
	activeCustomLighSet = property(get_activeCustomLighSet, set_activeCustomLighSet)
	#----------------------------------------------------------------------
	def get_activeCustomOverrideGeometry(self):
		"""
				Specifies an identifier for an override on the custom geometry for a scene
				render filter.
		"""
		return self.query(activeCustomOverrideGeometry=True)
	#----------------------------------------------------------------------
	def set_activeCustomOverrideGeometry(self, value):
		"""
				Specifies an identifier for an override on the custom geometry for a scene
				render filter.
		"""
		self.edit(activeCustomOverrideGeometry=value)
	#----------------------------------------------------------------------
	activeCustomOverrideGeometry = property(get_activeCustomOverrideGeometry, set_activeCustomOverrideGeometry)
	#----------------------------------------------------------------------
	def get_activeCustomRenderer(self):
		"""
				Specifies an identifier for custom renderer to use when
				a valid scene render filter is also specified.
		"""
		return self.query(activeCustomRenderer=True)
	#----------------------------------------------------------------------
	def set_activeCustomRenderer(self, value):
		"""
				Specifies an identifier for custom renderer to use when
				a valid scene render filter is also specified.
		"""
		self.edit(activeCustomRenderer=value)
	#----------------------------------------------------------------------
	activeCustomRenderer = property(get_activeCustomRenderer, set_activeCustomRenderer)
	#----------------------------------------------------------------------
	def get_activeOnly(self):
		"""
				Sets whether only active objects should appear shaded in
				shaded display.
		"""
		return self.query(activeOnly=True)
	#----------------------------------------------------------------------
	def set_activeOnly(self, value):
		"""
				Sets whether only active objects should appear shaded in
				shaded display.
		"""
		self.edit(activeOnly=value)
	#----------------------------------------------------------------------
	activeOnly = property(get_activeOnly, set_activeOnly)
	#----------------------------------------------------------------------
	def get_activeShadingGraph(self):
		"""
				Specifies the shading graph to use to override material display.
				Only enabled when a valid scene render filter is specified.
		"""
		return self.query(activeShadingGraph=True)
	#----------------------------------------------------------------------
	def set_activeShadingGraph(self, value):
		"""
				Specifies the shading graph to use to override material display.
				Only enabled when a valid scene render filter is specified.
		"""
		self.edit(activeShadingGraph=value)
	#----------------------------------------------------------------------
	activeShadingGraph = property(get_activeShadingGraph, set_activeShadingGraph)
	#----------------------------------------------------------------------
	def get_activeView(self):
		"""
				Sets this model editor to be the active view.  Returns true
				if successful.  On query this flag will return whether the view is
				the active view.
		"""
		return self.query(activeView=True)
	#----------------------------------------------------------------------
	def set_activeView(self, value):
		"""
				Sets this model editor to be the active view.  Returns true
				if successful.  On query this flag will return whether the view is
				the active view.
		"""
		self.edit(activeView=value)
	#----------------------------------------------------------------------
	activeView = property(get_activeView, set_activeView)
	#----------------------------------------------------------------------
	def addObjects(self,value):
		"""
				This flag causes the objects contained within the selection
				connection to be added to the list of objects visible in the view
				(if viewSelected is true).
		"""
		self.edit(addObjects=value)
	#----------------------------------------------------------------------
	def addSelected(self,value):
		"""
				This flag causes the currently active objects to be added
				to the list of objects visible in the view (if viewSelected is true).
		"""
		self.edit(addSelected=value)
	#----------------------------------------------------------------------
	def get_allObjects(self):
		"""
				Turn on/off the display of all objects for the view of
				the model editor. This excludes NURBS, CVs, hulls, grids and
				manipulators.
		"""
		return self.query(allObjects=True)
	#----------------------------------------------------------------------
	def set_allObjects(self, value):
		"""
				Turn on/off the display of all objects for the view of
				the model editor. This excludes NURBS, CVs, hulls, grids and
				manipulators.
		"""
		self.edit(allObjects=value)
	#----------------------------------------------------------------------
	allObjects = property(get_allObjects, set_allObjects)
	#----------------------------------------------------------------------
	def get_backfaceCulling(self):
		"""
				Turns on or off backface culling for the whole view.  This
				setting overrides the culling settings of individual objects.  All
				objects draw in the view will be backface culled.  When backface
				culling is turned on, surfaces becomes invisible in areas where the
				normal is pointing away from the camera.
		"""
		return self.query(backfaceCulling=True)
	#----------------------------------------------------------------------
	def set_backfaceCulling(self, value):
		"""
				Turns on or off backface culling for the whole view.  This
				setting overrides the culling settings of individual objects.  All
				objects draw in the view will be backface culled.  When backface
				culling is turned on, surfaces becomes invisible in areas where the
				normal is pointing away from the camera.
		"""
		self.edit(backfaceCulling=value)
	#----------------------------------------------------------------------
	backfaceCulling = property(get_backfaceCulling, set_backfaceCulling)
	#----------------------------------------------------------------------
	def get_bufferMode(self):
		"""
				Deprecated: this is not supported in Viewport 2.0.  Sets the
				graphic buffer mode.  Possible values are "single" or "double".
		"""
		return self.query(bufferMode=True)
	#----------------------------------------------------------------------
	def set_bufferMode(self, value):
		"""
				Deprecated: this is not supported in Viewport 2.0.  Sets the
				graphic buffer mode.  Possible values are "single" or "double".
		"""
		self.edit(bufferMode=value)
	#----------------------------------------------------------------------
	bufferMode = property(get_bufferMode, set_bufferMode)
	#----------------------------------------------------------------------
	def get_bumpResolution(self):
		"""
				Set the resolution for "baked" bump map textures when using the
				hardware renderer. The default value is 512, 512 respectively.
		"""
		return self.query(bumpResolution=True)
	#----------------------------------------------------------------------
	def set_bumpResolution(self, value):
		"""
				Set the resolution for "baked" bump map textures when using the
				hardware renderer. The default value is 512, 512 respectively.
		"""
		self.edit(bumpResolution=value)
	#----------------------------------------------------------------------
	bumpResolution = property(get_bumpResolution, set_bumpResolution)
	#----------------------------------------------------------------------
	def get_camera(self):
		"""Change or query the name of the camera in model editor."""
		return self.query(camera=True)
	#----------------------------------------------------------------------
	def set_camera(self, value):
		"""Change or query the name of the camera in model editor."""
		self.edit(camera=value)
	#----------------------------------------------------------------------
	camera = property(get_camera, set_camera)
	#----------------------------------------------------------------------
	def cameraName(self,value):
		"""
				Set the name of the panel's camera transform and shape. The
				shape name is computed by appending the string "Shape" to the
				transform name. This flag may not be queried.
		"""
		self.edit(cameraName=value)
	#----------------------------------------------------------------------
	def get_cameraSet(self):
		"""Name of the camera set"""
		return self.query(cameraSet=True)
	#----------------------------------------------------------------------
	def set_cameraSet(self, value):
		"""Name of the camera set"""
		self.edit(cameraSet=value)
	#----------------------------------------------------------------------
	cameraSet = property(get_cameraSet, set_cameraSet)
	#----------------------------------------------------------------------
	@property
	def cameraSetup(self):
		"""
		
				Based on the model editor name passed in will
				returns a string list containing camera setups.
				A camera setup can contain one or more cameras
				which are associated with each other.
				Camera setups are defined as pairs of consecutive
				strings in the list. Each pair is comprised of:
				a string which identifies an active camera,
				and a string which defines a script
				to set up a given active camera. As many pairs of strings
				can be returned as the number of active cameras. If nothing
				is returned then it is assumed that no set up is
				required to activate a given camera.
				
		"""
		return self.query(cameraSetup=True)
	#----------------------------------------------------------------------
	def get_capture(self):
		"""
		
				Perform an one-time capture of the viewport to the named image file on disk.
				
		"""
		return self.query(capture=True)
	#----------------------------------------------------------------------
	def set_capture(self, value):
		"""
		
				Perform an one-time capture of the viewport to the named image file on disk.
				
		"""
		self.edit(capture=value)
	#----------------------------------------------------------------------
	capture = property(get_capture, set_capture)
	#----------------------------------------------------------------------
	def get_captureSequenceNumber(self):
		"""
		
				When a number greater or equal to 0 is specified each subsequent refresh will
				save an image file to disk if the capture flag has been enabled.
				
				The naming of the file is:
				
				{root name}.#.{extension}
				
				if the name {root name}.{extension} is used for the capture flag argument.
				
				The value of # starts at the number specified to for this argument and
				increments for each subsequent refresh.
				
				Sequence capture can be disabled by specifying a number less than 0 or an
				empty file name for the capture flag.
				
		"""
		return self.query(captureSequenceNumber=True)
	#----------------------------------------------------------------------
	def set_captureSequenceNumber(self, value):
		"""
		
				When a number greater or equal to 0 is specified each subsequent refresh will
				save an image file to disk if the capture flag has been enabled.
				
				The naming of the file is:
				
				{root name}.#.{extension}
				
				if the name {root name}.{extension} is used for the capture flag argument.
				
				The value of # starts at the number specified to for this argument and
				increments for each subsequent refresh.
				
				Sequence capture can be disabled by specifying a number less than 0 or an
				empty file name for the capture flag.
				
		"""
		self.edit(captureSequenceNumber=value)
	#----------------------------------------------------------------------
	captureSequenceNumber = property(get_captureSequenceNumber, set_captureSequenceNumber)
	#----------------------------------------------------------------------
	def get_clipGhosts(self):
		"""
		
				Define whether the clip ghosts should be added or not
				
		"""
		return self.query(clipGhosts=True)
	#----------------------------------------------------------------------
	def set_clipGhosts(self, value):
		"""
		
				Define whether the clip ghosts should be added or not
				
		"""
		self.edit(clipGhosts=value)
	#----------------------------------------------------------------------
	clipGhosts = property(get_clipGhosts, set_clipGhosts)
	#----------------------------------------------------------------------
	def get_cmEnabled(self):
		"""
		
				Turn on or off applying color management in the editor.  If set, the color
				management configuration set in the current editor is used.
				
		"""
		return self.query(cmEnabled=True)
	#----------------------------------------------------------------------
	def set_cmEnabled(self, value):
		"""
		
				Turn on or off applying color management in the editor.  If set, the color
				management configuration set in the current editor is used.
				
		"""
		self.edit(cmEnabled=value)
	#----------------------------------------------------------------------
	cmEnabled = property(get_cmEnabled, set_cmEnabled)
	#----------------------------------------------------------------------
	@property
	def colorMap(self):
		"""
		
				Queries the color map style for the model panel. Possible
				values are "colorIndex" and "rgb".
				
		"""
		return self.query(colorMap=True)
	#----------------------------------------------------------------------
	def get_colorResolution(self):
		"""
		
				Set the resolution for "baked" color textures when using the
				hardware renderer. The default value is 256, 256 respectively.
				
		"""
		return self.query(colorResolution=True)
	#----------------------------------------------------------------------
	def set_colorResolution(self, value):
		"""
		
				Set the resolution for "baked" color textures when using the
				hardware renderer. The default value is 256, 256 respectively.
				
		"""
		self.edit(colorResolution=value)
	#----------------------------------------------------------------------
	colorResolution = property(get_colorResolution, set_colorResolution)
	#----------------------------------------------------------------------
	@property
	def control(self):
		"""
		
				Query only. Returns the top level control for this editor.
				Usually used for getting a parent to attach popup menus.
				Caution: It is possible for an editor to exist without a
				control. The query will return "NONE" if no control is present.
				
		"""
		return self.query(control=True)
	#----------------------------------------------------------------------
	def get_cullingOverride(self):
		"""
		
				Set whether to override the culling attributes on objects when using
				the hardware renderer. The options are:
				
				"none" : Use the culling object attributes per object.
				"doubleSided" : Force all objects to be double sided.
				"singleSided": Force all objects to be single sided.
				
				The default value is "none".
				
		"""
		return self.query(cullingOverride=True)
	#----------------------------------------------------------------------
	def set_cullingOverride(self, value):
		"""
		
				Set whether to override the culling attributes on objects when using
				the hardware renderer. The options are:
				
				"none" : Use the culling object attributes per object.
				"doubleSided" : Force all objects to be double sided.
				"singleSided": Force all objects to be single sided.
				
				The default value is "none".
				
		"""
		self.edit(cullingOverride=value)
	#----------------------------------------------------------------------
	cullingOverride = property(get_cullingOverride, set_cullingOverride)
	#----------------------------------------------------------------------
	def get_default(self):
		"""
		
				Causes this command to modify the default value of this setting.
				Newly created model editors will inherit the values.  This flag may
				be used with the -interactive to set default interactive settings.
				
		"""
		return self.query(default=True)
	#----------------------------------------------------------------------
	def set_default(self, value):
		"""
		
				Causes this command to modify the default value of this setting.
				Newly created model editors will inherit the values.  This flag may
				be used with the -interactive to set default interactive settings.
				
		"""
		self.edit(default=value)
	#----------------------------------------------------------------------
	default = property(get_default, set_default)
	#----------------------------------------------------------------------
	def get_deformers(self):
		"""
		
				Turn on/off the display of deformer objects for the view
				of the model editor.
				
		"""
		return self.query(deformers=True)
	#----------------------------------------------------------------------
	def set_deformers(self, value):
		"""
		
				Turn on/off the display of deformer objects for the view
				of the model editor.
				
		"""
		self.edit(deformers=value)
	#----------------------------------------------------------------------
	deformers = property(get_deformers, set_deformers)
	#----------------------------------------------------------------------
	def get_dimensions(self):
		"""
		
				Turn on/off the display of dimension objects for the view
				of the model editor.
				
		"""
		return self.query(dimensions=True)
	#----------------------------------------------------------------------
	def set_dimensions(self, value):
		"""
		
				Turn on/off the display of dimension objects for the view
				of the model editor.
				
		"""
		self.edit(dimensions=value)
	#----------------------------------------------------------------------
	dimensions = property(get_dimensions, set_dimensions)
	#----------------------------------------------------------------------
	def get_displayAppearance(self):
		"""
		
				Sets the display appearance of the model panel.  Possible
				values are "wireframe", "points", "boundingBox", "smoothShaded",
				"flatShaded".  This flag may be used with the -interactive
				and -default flags.  Note that only "wireframe", "points", and
				"boundingBox" are valid for the interactive mode.
				
		"""
		return self.query(displayAppearance=True)
	#----------------------------------------------------------------------
	def set_displayAppearance(self, value):
		"""
		
				Sets the display appearance of the model panel.  Possible
				values are "wireframe", "points", "boundingBox", "smoothShaded",
				"flatShaded".  This flag may be used with the -interactive
				and -default flags.  Note that only "wireframe", "points", and
				"boundingBox" are valid for the interactive mode.
				
		"""
		self.edit(displayAppearance=value)
	#----------------------------------------------------------------------
	displayAppearance = property(get_displayAppearance, set_displayAppearance)
	#----------------------------------------------------------------------
	def get_displayLights(self):
		"""
		
				Sets the lighting for shaded mode.  Possible values are
				"selected", "active", "all", "default", "none".
				
		"""
		return self.query(displayLights=True)
	#----------------------------------------------------------------------
	def set_displayLights(self, value):
		"""
		
				Sets the lighting for shaded mode.  Possible values are
				"selected", "active", "all", "default", "none".
				
		"""
		self.edit(displayLights=value)
	#----------------------------------------------------------------------
	displayLights = property(get_displayLights, set_displayLights)
	#----------------------------------------------------------------------
	def get_displayTextures(self):
		"""
		
				Turns on or off display of textures in shaded mode
				
		"""
		return self.query(displayTextures=True)
	#----------------------------------------------------------------------
	def set_displayTextures(self, value):
		"""
		
				Turns on or off display of textures in shaded mode
				
		"""
		self.edit(displayTextures=value)
	#----------------------------------------------------------------------
	displayTextures = property(get_displayTextures, set_displayTextures)
	#----------------------------------------------------------------------
	def get_docTag(self):
		"""
		
				Attaches a tag to the editor.
				
		"""
		return self.query(docTag=True)
	#----------------------------------------------------------------------
	def set_docTag(self, value):
		"""
		
				Attaches a tag to the editor.
				
		"""
		self.edit(docTag=value)
	#----------------------------------------------------------------------
	docTag = property(get_docTag, set_docTag)
	#----------------------------------------------------------------------
	def get_dynamicConstraints(self):
		"""
		
				Turn on/off the display of dynamicConstraints for the view
				of the model editor.
				
		"""
		return self.query(dynamicConstraints=True)
	#----------------------------------------------------------------------
	def set_dynamicConstraints(self, value):
		"""
		
				Turn on/off the display of dynamicConstraints for the view
				of the model editor.
				
		"""
		self.edit(dynamicConstraints=value)
	#----------------------------------------------------------------------
	dynamicConstraints = property(get_dynamicConstraints, set_dynamicConstraints)
	#----------------------------------------------------------------------
	def get_dynamics(self):
		"""
		
				Turn on/off the display of dynamics objects for the view
				of the model editor.
				
		"""
		return self.query(dynamics=True)
	#----------------------------------------------------------------------
	def set_dynamics(self, value):
		"""
		
				Turn on/off the display of dynamics objects for the view
				of the model editor.
				
		"""
		self.edit(dynamics=value)
	#----------------------------------------------------------------------
	dynamics = property(get_dynamics, set_dynamics)
	#----------------------------------------------------------------------
	def get_editorChanged(self):
		"""
		
				An optional script callback which is called when the editors
				options have changed.  This is useful in a situation where a scripted
				panel contains a modelEditor and wants to be notified when the contained
				editor changes its options.
				
		"""
		return self.query(editorChanged=True)
	#----------------------------------------------------------------------
	def set_editorChanged(self, value):
		"""
		
				An optional script callback which is called when the editors
				options have changed.  This is useful in a situation where a scripted
				panel contains a modelEditor and wants to be notified when the contained
				editor changes its options.
				
		"""
		self.edit(editorChanged=value)
	#----------------------------------------------------------------------
	editorChanged = property(get_editorChanged, set_editorChanged)
	#----------------------------------------------------------------------
	def get_exposure(self):
		"""
		
				The exposure value used by the color management of the current editor.
				
		"""
		return self.query(exposure=True)
	#----------------------------------------------------------------------
	def set_exposure(self, value):
		"""
		
				The exposure value used by the color management of the current editor.
				
		"""
		self.edit(exposure=value)
	#----------------------------------------------------------------------
	exposure = property(get_exposure, set_exposure)
	#----------------------------------------------------------------------
	def get_filter(self):
		"""
		
				Specifies the name of an itemFilter object to be used with this editor.
				This filters the information coming onto the main list
				of the editor.
				
		"""
		return self.query(filter=True)
	#----------------------------------------------------------------------
	def set_filter(self, value):
		"""
		
				Specifies the name of an itemFilter object to be used with this editor.
				This filters the information coming onto the main list
				of the editor.
				
		"""
		self.edit(filter=value)
	#----------------------------------------------------------------------
	filter = property(get_filter, set_filter)
	#----------------------------------------------------------------------
	@property
	def filteredObjectList(self):
		"""
		
				For model editors with filtering on (either using an object filter, or isolate
				select), this flag returns a string list of the objects which are displayed in
				this editor. Note that this list does not take into account visibility (based on
				camera frustum or flags), it purely captures the objects which are considered
				when rendering the view.
				
		"""
		return self.query(filteredObjectList=True)
	#----------------------------------------------------------------------
	def get_fluids(self):
		"""
		
				Turn on/off the display of fluids for the view
				of the model editor.
				
		"""
		return self.query(fluids=True)
	#----------------------------------------------------------------------
	def set_fluids(self, value):
		"""
		
				Turn on/off the display of fluids for the view
				of the model editor.
				
		"""
		self.edit(fluids=value)
	#----------------------------------------------------------------------
	fluids = property(get_fluids, set_fluids)
	#----------------------------------------------------------------------
	def get_fogColor(self):
		"""
		
				The color used for hardware fogging.
				
		"""
		return self.query(fogColor=True)
	#----------------------------------------------------------------------
	def set_fogColor(self, value):
		"""
		
				The color used for hardware fogging.
				
		"""
		self.edit(fogColor=value)
	#----------------------------------------------------------------------
	fogColor = property(get_fogColor, set_fogColor)
	#----------------------------------------------------------------------
	def get_fogDensity(self):
		"""
		
				Determines the density of hardware fogging.
				
		"""
		return self.query(fogDensity=True)
	#----------------------------------------------------------------------
	def set_fogDensity(self, value):
		"""
		
				Determines the density of hardware fogging.
				
		"""
		self.edit(fogDensity=value)
	#----------------------------------------------------------------------
	fogDensity = property(get_fogDensity, set_fogDensity)
	#----------------------------------------------------------------------
	def get_fogEnd(self):
		"""
		
				The end location of hardware fogging.
				
		"""
		return self.query(fogEnd=True)
	#----------------------------------------------------------------------
	def set_fogEnd(self, value):
		"""
		
				The end location of hardware fogging.
				
		"""
		self.edit(fogEnd=value)
	#----------------------------------------------------------------------
	fogEnd = property(get_fogEnd, set_fogEnd)
	#----------------------------------------------------------------------
	def get_fogMode(self):
		"""
		
				This determines the drop-off mode for fog. The possibilities are:
				
				"linear" : linear drop-off
				"exponent" : exponential drop-off
				"exponent2" : squared exponential drop-off
				
		"""
		return self.query(fogMode=True)
	#----------------------------------------------------------------------
	def set_fogMode(self, value):
		"""
		
				This determines the drop-off mode for fog. The possibilities are:
				
				"linear" : linear drop-off
				"exponent" : exponential drop-off
				"exponent2" : squared exponential drop-off
				
		"""
		self.edit(fogMode=value)
	#----------------------------------------------------------------------
	fogMode = property(get_fogMode, set_fogMode)
	#----------------------------------------------------------------------
	def get_fogSource(self):
		"""
		
				Set the type of fog algorithm to use. If the argument
				is "fragment" (default) then fog is computed per pixel. If
				the argument is "coordinate" then if the geometry has
				specified vertex fog coordinates, and the OpenGL extension
				for vertex fog is supported by the graphics system, then
				fog is computed per vertex.
				
		"""
		return self.query(fogSource=True)
	#----------------------------------------------------------------------
	def set_fogSource(self, value):
		"""
		
				Set the type of fog algorithm to use. If the argument
				is "fragment" (default) then fog is computed per pixel. If
				the argument is "coordinate" then if the geometry has
				specified vertex fog coordinates, and the OpenGL extension
				for vertex fog is supported by the graphics system, then
				fog is computed per vertex.
				
		"""
		self.edit(fogSource=value)
	#----------------------------------------------------------------------
	fogSource = property(get_fogSource, set_fogSource)
	#----------------------------------------------------------------------
	def get_fogStart(self):
		"""
		
				The start location of hardware fogging.
				
		"""
		return self.query(fogStart=True)
	#----------------------------------------------------------------------
	def set_fogStart(self, value):
		"""
		
				The start location of hardware fogging.
				
		"""
		self.edit(fogStart=value)
	#----------------------------------------------------------------------
	fogStart = property(get_fogStart, set_fogStart)
	#----------------------------------------------------------------------
	def get_fogging(self):
		"""
		
				Set whether hardware fogging is enabled or not.
				
		"""
		return self.query(fogging=True)
	#----------------------------------------------------------------------
	def set_fogging(self, value):
		"""
		
				Set whether hardware fogging is enabled or not.
				
		"""
		self.edit(fogging=value)
	#----------------------------------------------------------------------
	fogging = property(get_fogging, set_fogging)
	#----------------------------------------------------------------------
	def get_follicles(self):
		"""
		
				Turn on/off the display of follicles for the view
				of the model editor.
				
		"""
		return self.query(follicles=True)
	#----------------------------------------------------------------------
	def set_follicles(self, value):
		"""
		
				Turn on/off the display of follicles for the view
				of the model editor.
				
		"""
		self.edit(follicles=value)
	#----------------------------------------------------------------------
	follicles = property(get_follicles, set_follicles)
	#----------------------------------------------------------------------
	def get_forceMainConnection(self):
		"""
		
				Specifies the name of a selectionConnection object that the
				editor will use as its source of content. The editor will only
				display items contained in the selectionConnection object. This is
				a variant of the -mainListConnection flag in that it will force a
				change even when the connection is locked. This flag is used to
				reduce the overhead when using the -unlockMainConnection
				, -mainListConnection, -lockMainConnection flags in immediate
				succession.
				
		"""
		return self.query(forceMainConnection=True)
	#----------------------------------------------------------------------
	def set_forceMainConnection(self, value):
		"""
		
				Specifies the name of a selectionConnection object that the
				editor will use as its source of content. The editor will only
				display items contained in the selectionConnection object. This is
				a variant of the -mainListConnection flag in that it will force a
				change even when the connection is locked. This flag is used to
				reduce the overhead when using the -unlockMainConnection
				, -mainListConnection, -lockMainConnection flags in immediate
				succession.
				
		"""
		self.edit(forceMainConnection=value)
	#----------------------------------------------------------------------
	forceMainConnection = property(get_forceMainConnection, set_forceMainConnection)
	#----------------------------------------------------------------------
	def get_gamma(self):
		"""
		
				The gamma value used by the color management of the current editor.
				
		"""
		return self.query(gamma=True)
	#----------------------------------------------------------------------
	def set_gamma(self, value):
		"""
		
				The gamma value used by the color management of the current editor.
				
		"""
		self.edit(gamma=value)
	#----------------------------------------------------------------------
	gamma = property(get_gamma, set_gamma)
	#----------------------------------------------------------------------
	def get_greasePencils(self):
		"""
		
				Define whether the grease pencil marks should be added or not
				
		"""
		return self.query(greasePencils=True)
	#----------------------------------------------------------------------
	def set_greasePencils(self, value):
		"""
		
				Define whether the grease pencil marks should be added or not
				
		"""
		self.edit(greasePencils=value)
	#----------------------------------------------------------------------
	greasePencils = property(get_greasePencils, set_greasePencils)
	#----------------------------------------------------------------------
	def get_grid(self):
		"""
		
				Turn on/off the display of the grid for the view of the
				model editor.
				
		"""
		return self.query(grid=True)
	#----------------------------------------------------------------------
	def set_grid(self, value):
		"""
		
				Turn on/off the display of the grid for the view of the
				model editor.
				
		"""
		self.edit(grid=value)
	#----------------------------------------------------------------------
	grid = property(get_grid, set_grid)
	#----------------------------------------------------------------------
	def get_hairSystems(self):
		"""
		
				Turn on/off the display of hairSystems for the view
				of the model editor.
				
		"""
		return self.query(hairSystems=True)
	#----------------------------------------------------------------------
	def set_hairSystems(self, value):
		"""
		
				Turn on/off the display of hairSystems for the view
				of the model editor.
				
		"""
		self.edit(hairSystems=value)
	#----------------------------------------------------------------------
	hairSystems = property(get_hairSystems, set_hairSystems)
	#----------------------------------------------------------------------
	def get_handles(self):
		"""
		
				Turn on/off the display of select handles for the view
				of the model editor.
				
		"""
		return self.query(handles=True)
	#----------------------------------------------------------------------
	def set_handles(self, value):
		"""
		
				Turn on/off the display of select handles for the view
				of the model editor.
				
		"""
		self.edit(handles=value)
	#----------------------------------------------------------------------
	handles = property(get_handles, set_handles)
	#----------------------------------------------------------------------
	def get_headsUpDisplay(self):
		"""
		
				Sets whether the model panel will draw any enabled heads up
				display	elements in this window (if true).  Currently this requires
				the HUD elements to be globally enabled.
				
		"""
		return self.query(headsUpDisplay=True)
	#----------------------------------------------------------------------
	def set_headsUpDisplay(self, value):
		"""
		
				Sets whether the model panel will draw any enabled heads up
				display	elements in this window (if true).  Currently this requires
				the HUD elements to be globally enabled.
				
		"""
		self.edit(headsUpDisplay=value)
	#----------------------------------------------------------------------
	headsUpDisplay = property(get_headsUpDisplay, set_headsUpDisplay)
	#----------------------------------------------------------------------
	@property
	def height(self):
		"""
		
				Return the height of the associated viewport in pixels
				
		"""
		return self.query(height=True)
	#----------------------------------------------------------------------
	def get_highlightConnection(self):
		"""
		
				Specifies the name of a selectionConnection object that
				the editor will synchronize with its highlight list. Not all
				editors have a highlight list. For those that do, it is a secondary
				selection list.
				
		"""
		return self.query(highlightConnection=True)
	#----------------------------------------------------------------------
	def set_highlightConnection(self, value):
		"""
		
				Specifies the name of a selectionConnection object that
				the editor will synchronize with its highlight list. Not all
				editors have a highlight list. For those that do, it is a secondary
				selection list.
				
		"""
		self.edit(highlightConnection=value)
	#----------------------------------------------------------------------
	highlightConnection = property(get_highlightConnection, set_highlightConnection)
	#----------------------------------------------------------------------
	def get_ignorePanZoom(self):
		"""
		
				Sets whether the model panel will ignore the 2D pan/zoom value to
				give an overview of the scene.
				
		"""
		return self.query(ignorePanZoom=True)
	#----------------------------------------------------------------------
	def set_ignorePanZoom(self, value):
		"""
		
				Sets whether the model panel will ignore the 2D pan/zoom value to
				give an overview of the scene.
				
		"""
		self.edit(ignorePanZoom=value)
	#----------------------------------------------------------------------
	ignorePanZoom = property(get_ignorePanZoom, set_ignorePanZoom)
	#----------------------------------------------------------------------
	def get_ikHandles(self):
		"""
		
				Turn on/off the display of ik handles and end effectors
				for the view of the model editor.
				
		"""
		return self.query(ikHandles=True)
	#----------------------------------------------------------------------
	def set_ikHandles(self, value):
		"""
		
				Turn on/off the display of ik handles and end effectors
				for the view of the model editor.
				
		"""
		self.edit(ikHandles=value)
	#----------------------------------------------------------------------
	ikHandles = property(get_ikHandles, set_ikHandles)
	#----------------------------------------------------------------------
	def get_interactive(self):
		"""
		
				Causes this command to modify the interactive refresh settings of
				the view.  In this way it is possible to change the behavior of the
				model editor during playback for improved performance.
				
		"""
		return self.query(interactive=True)
	#----------------------------------------------------------------------
	def set_interactive(self, value):
		"""
		
				Causes this command to modify the interactive refresh settings of
				the view.  In this way it is possible to change the behavior of the
				model editor during playback for improved performance.
				
		"""
		self.edit(interactive=value)
	#----------------------------------------------------------------------
	interactive = property(get_interactive, set_interactive)
	#----------------------------------------------------------------------
	def get_interactiveBackFaceCull(self):
		"""
		
				Define whether interactive backface culling should be on or not
				
		"""
		return self.query(interactiveBackFaceCull=True)
	#----------------------------------------------------------------------
	def set_interactiveBackFaceCull(self, value):
		"""
		
				Define whether interactive backface culling should be on or not
				
		"""
		self.edit(interactiveBackFaceCull=value)
	#----------------------------------------------------------------------
	interactiveBackFaceCull = property(get_interactiveBackFaceCull, set_interactiveBackFaceCull)
	#----------------------------------------------------------------------
	def get_interactiveDisableShadows(self):
		"""
		
				Define whether interactive shadows should be disabled or not
				
		"""
		return self.query(interactiveDisableShadows=True)
	#----------------------------------------------------------------------
	def set_interactiveDisableShadows(self, value):
		"""
		
				Define whether interactive shadows should be disabled or not
				
		"""
		self.edit(interactiveDisableShadows=value)
	#----------------------------------------------------------------------
	interactiveDisableShadows = property(get_interactiveDisableShadows, set_interactiveDisableShadows)
	#----------------------------------------------------------------------
	@property
	def isFiltered(self):
		"""
		
				Returns true for model editors with filtering applied to their view of the
				scene. This could either be an explicit object filter, or a display option such
				as isolate select which filters the objects that are displayed.
				
		"""
		return self.query(isFiltered=True)
	#----------------------------------------------------------------------
	def get_jointXray(self):
		"""
		
				Turns on or off Xray mode for joints.
				
		"""
		return self.query(jointXray=True)
	#----------------------------------------------------------------------
	def set_jointXray(self, value):
		"""
		
				Turns on or off Xray mode for joints.
				
		"""
		self.edit(jointXray=value)
	#----------------------------------------------------------------------
	jointXray = property(get_jointXray, set_jointXray)
	#----------------------------------------------------------------------
	def get_lineWidth(self):
		"""
		
				Set width of lines for display
				
		"""
		return self.query(lineWidth=True)
	#----------------------------------------------------------------------
	def set_lineWidth(self, value):
		"""
		
				Set width of lines for display
				
		"""
		self.edit(lineWidth=value)
	#----------------------------------------------------------------------
	lineWidth = property(get_lineWidth, set_lineWidth)
	#----------------------------------------------------------------------
	def get_locators(self):
		"""
		
				Turn on/off the display of locator objects for the view
				of the model editor.
				
		"""
		return self.query(locators=True)
	#----------------------------------------------------------------------
	def set_locators(self, value):
		"""
		
				Turn on/off the display of locator objects for the view
				of the model editor.
				
		"""
		self.edit(locators=value)
	#----------------------------------------------------------------------
	locators = property(get_locators, set_locators)
	#----------------------------------------------------------------------
	def lockMainConnection(self,value):
		"""
		
				Locks the current list of objects within the mainConnection,
				so that only those objects are displayed within the editor.
				Further changes to the original mainConnection are ignored.
				
		"""
		self.edit(lockMainConnection=value)
	#----------------------------------------------------------------------
	def get_lowQualityLighting(self):
		"""
		
				Set whether to use "low quality lighting" when using the
				hardware renderer. The default value is false.
				
		"""
		return self.query(lowQualityLighting=True)
	#----------------------------------------------------------------------
	def set_lowQualityLighting(self, value):
		"""
		
				Set whether to use "low quality lighting" when using the
				hardware renderer. The default value is false.
				
		"""
		self.edit(lowQualityLighting=value)
	#----------------------------------------------------------------------
	lowQualityLighting = property(get_lowQualityLighting, set_lowQualityLighting)
	#----------------------------------------------------------------------
	def get_mainListConnection(self):
		"""
		
				Specifies the name of a selectionConnection object that the
				editor will use as its source of content. The editor will
				only display items contained in the selectionConnection object.
				
		"""
		return self.query(mainListConnection=True)
	#----------------------------------------------------------------------
	def set_mainListConnection(self, value):
		"""
		
				Specifies the name of a selectionConnection object that the
				editor will use as its source of content. The editor will
				only display items contained in the selectionConnection object.
				
		"""
		self.edit(mainListConnection=value)
	#----------------------------------------------------------------------
	mainListConnection = property(get_mainListConnection, set_mainListConnection)
	#----------------------------------------------------------------------
	def get_manipulators(self):
		"""
		
				Turn on/off the display of manipulator objects for the view
				of the model editor.
				
		"""
		return self.query(manipulators=True)
	#----------------------------------------------------------------------
	def set_manipulators(self, value):
		"""
		
				Turn on/off the display of manipulator objects for the view
				of the model editor.
				
		"""
		self.edit(manipulators=value)
	#----------------------------------------------------------------------
	manipulators = property(get_manipulators, set_manipulators)
	#----------------------------------------------------------------------
	def get_maxConstantTransparency(self):
		"""
		
				Sets the maximum constant transparency.  Setting this value remaps
				constant transparency values from the range [0.0, 1.0] to the range
				[0.0, maxConstantTransparency]. All transparency values are shifted
				linearly to the new range, so a fully transparency object
				(transparency 1.0) would
				appear with a transparency of maxConstantTransparency in the viewport,
				allowing highly transparent objects to be made visible.  This flag only
				affects constant (non-textured) transparent objects.
				
		"""
		return self.query(maxConstantTransparency=True)
	#----------------------------------------------------------------------
	def set_maxConstantTransparency(self, value):
		"""
		
				Sets the maximum constant transparency.  Setting this value remaps
				constant transparency values from the range [0.0, 1.0] to the range
				[0.0, maxConstantTransparency]. All transparency values are shifted
				linearly to the new range, so a fully transparency object
				(transparency 1.0) would
				appear with a transparency of maxConstantTransparency in the viewport,
				allowing highly transparent objects to be made visible.  This flag only
				affects constant (non-textured) transparent objects.
				
		"""
		self.edit(maxConstantTransparency=value)
	#----------------------------------------------------------------------
	maxConstantTransparency = property(get_maxConstantTransparency, set_maxConstantTransparency)
	#----------------------------------------------------------------------
	def get_maximumNumHardwareLights(self):
		"""
		
				Define whether the hardware light maximum should be respected or not
				
		"""
		return self.query(maximumNumHardwareLights=True)
	#----------------------------------------------------------------------
	def set_maximumNumHardwareLights(self, value):
		"""
		
				Define whether the hardware light maximum should be respected or not
				
		"""
		self.edit(maximumNumHardwareLights=value)
	#----------------------------------------------------------------------
	maximumNumHardwareLights = property(get_maximumNumHardwareLights, set_maximumNumHardwareLights)
	#----------------------------------------------------------------------
	def get_motionTrails(self):
		"""
		
				Turn on/off the Motion Trail display in the Viewport.
				
		"""
		return self.query(motionTrails=True)
	#----------------------------------------------------------------------
	def set_motionTrails(self, value):
		"""
		
				Turn on/off the Motion Trail display in the Viewport.
				
		"""
		self.edit(motionTrails=value)
	#----------------------------------------------------------------------
	motionTrails = property(get_motionTrails, set_motionTrails)
	#----------------------------------------------------------------------
	def get_nCloths(self):
		"""
		
				Turn on/off the display of nCloths for the view
				of the model editor.
				
		"""
		return self.query(nCloths=True)
	#----------------------------------------------------------------------
	def set_nCloths(self, value):
		"""
		
				Turn on/off the display of nCloths for the view
				of the model editor.
				
		"""
		self.edit(nCloths=value)
	#----------------------------------------------------------------------
	nCloths = property(get_nCloths, set_nCloths)
	#----------------------------------------------------------------------
	def get_nParticles(self):
		"""
		
				Turn on/off the display of nParticles for the view
				of the model editor.
				
		"""
		return self.query(nParticles=True)
	#----------------------------------------------------------------------
	def set_nParticles(self, value):
		"""
		
				Turn on/off the display of nParticles for the view
				of the model editor.
				
		"""
		self.edit(nParticles=value)
	#----------------------------------------------------------------------
	nParticles = property(get_nParticles, set_nParticles)
	#----------------------------------------------------------------------
	def get_nRigids(self):
		"""
		
				Turn on/off the display of nRigids for the view
				of the model editor.
				
		"""
		return self.query(nRigids=True)
	#----------------------------------------------------------------------
	def set_nRigids(self, value):
		"""
		
				Turn on/off the display of nRigids for the view
				of the model editor.
				
		"""
		self.edit(nRigids=value)
	#----------------------------------------------------------------------
	nRigids = property(get_nRigids, set_nRigids)
	#----------------------------------------------------------------------
	def noUndo(self,value):
		"""
		
				This flag prevents some viewport operations (such as isolate
				select) from being added to the undo queue.
				
		"""
		self.edit(noUndo=value)
	#----------------------------------------------------------------------
	def get_objectFilter(self):
		""""""
		return self.query(objectFilter=True)
	#----------------------------------------------------------------------
	def set_objectFilter(self, value):
		"""Set or query the current object filter name. An object filter
		is required to have already been registered."""
		self.edit(objectFilter=value)
	#----------------------------------------------------------------------
	objectFilter = property(get_objectFilter, set_objectFilter)
	#----------------------------------------------------------------------
	@property
	def objectFilterList(self):
		"""Return a list of names of registered filters."""
		return self.query(objectFilterList=True)
	#----------------------------------------------------------------------
	@property
	def objectFilterListUI(self):
		"""Return a list of names of registered filters."""
		return self.query(objectFilterListUI=True)
	#----------------------------------------------------------------------
	def get_objectFilterShowInHUD(self):
		"""
		Sets whether or not to display the object filter UI name in the heads
		up display when an object filter is active. This string is concatenated
		with the camera name.
		"""
		return self.query(objectFilterShowInHUD=True)
	#----------------------------------------------------------------------
	def set_objectFilterShowInHUD(self, value):
		"""
		Sets whether or not to display the object filter UI name in the heads
		up display when an object filter is active. This string is concatenated
		with the camera name.
		"""
		self.edit(objectFilterShowInHUD=value)
	#----------------------------------------------------------------------
	objectFilterShowInHUD = property(get_objectFilterShowInHUD, set_objectFilterShowInHUD)
	#----------------------------------------------------------------------
	@property
	def objectFilterUI(self):
		"""
		
				Query the current object filter UI name. The object filter
				is required to have already been registered.
				
		"""
		return self.query(objectFilterUI=True)
	#----------------------------------------------------------------------
	def get_occlusionCulling(self):
		"""
		
				Set whether to enable occlusion culling testing when using
				the hardware renderer. The default value is false.
				
		"""
		return self.query(occlusionCulling=True)
	#----------------------------------------------------------------------
	def set_occlusionCulling(self, value):
		"""
		
				Set whether to enable occlusion culling testing when using
				the hardware renderer. The default value is false.
				
		"""
		self.edit(occlusionCulling=value)
	#----------------------------------------------------------------------
	occlusionCulling = property(get_occlusionCulling, set_occlusionCulling)
	#----------------------------------------------------------------------
	@property
	def panel(self):
		"""
		
				Specifies the panel for this editor. By default if
				an editor is created in the create callback of a scripted panel it
				will belong to that panel. If an editor does not belong to a panel
				it will be deleted when the window that it is in is deleted.
				
		"""
		return self.query(panel=True)
	#----------------------------------------------------------------------
	def get_parent(self):
		"""
		
				Specifies the parent layout for this editor. This flag will only
				have an effect if the editor is currently un-parented.
				
		"""
		return self.query(parent=True)
	#----------------------------------------------------------------------
	def set_parent(self, value):
		"""
		
				Specifies the parent layout for this editor. This flag will only
				have an effect if the editor is currently un-parented.
				
		"""
		self.edit(parent=value)
	#----------------------------------------------------------------------
	parent = property(get_parent, set_parent)
	#----------------------------------------------------------------------
	def get_particleInstancers(self):
		"""
		
				Define whether the particle instances should be shown or not
				
		"""
		return self.query(particleInstancers=True)
	#----------------------------------------------------------------------
	def set_particleInstancers(self, value):
		"""
		
				Define whether the particle instances should be shown or not
				
		"""
		self.edit(particleInstancers=value)
	#----------------------------------------------------------------------
	particleInstancers = property(get_particleInstancers, set_particleInstancers)
	#----------------------------------------------------------------------
	def get_pivots(self):
		"""
		
				Turn on/off the display of transform pivots for the view
				of the model editor.
				
		"""
		return self.query(pivots=True)
	#----------------------------------------------------------------------
	def set_pivots(self, value):
		"""
		
				Turn on/off the display of transform pivots for the view
				of the model editor.
				
		"""
		self.edit(pivots=value)
	#----------------------------------------------------------------------
	pivots = property(get_pivots, set_pivots)
	#----------------------------------------------------------------------
	def pluginObjects(self,value):
		"""
		
				Turn on/off the display of plug-in objects for the view.
				It depends on the plug-in implementation whether to respect this flag.
				
		"""
		self.edit(pluginObjects=value)
	#----------------------------------------------------------------------
	def pluginShapes(self,value):
		"""
		
				Turn on/off the display of plug-in shapes for the view.
				It depends on the plug-in implementation whether to respect this flag.
				
		"""
		self.edit(pluginShapes=value)
	#----------------------------------------------------------------------
	@property
	def queryPluginObjects(self):
		"""
		
				Query the on/off state of plug-in objects display for the view.
				To set the on/off state, use -pluginObjects instead.
				
		"""
		return self.query(queryPluginObjects=True)
	#----------------------------------------------------------------------
	def removeSelected(self,value):
		"""
		
				This flag causes the currently active objects to be removed
				from the list of objects visible in the view (if viewSelected is true).
				
		"""
		self.edit(removeSelected=value)
	#----------------------------------------------------------------------
	@property
	def rendererDeviceName(self):
		"""
		
				Query for the name of the draw API used by the Viewport 2.0 renderer for a 3d modeling viewport.
				The possible return values are "VirtualDeviceGL" if Maya is set to use "OpenGL - Legacy" for Viewport 2.0,
				"VirtualDeviceGLCore" if Maya is set to use "OpenGL - Core Profile" (either Compatibility or Strict) for
				Viewport 2.0, or "VirtualDeviceDx11" if Maya is set to use DirectX for Viewport 2.0.
				If the renderer for the 3d modeling viewport is not Viewport 2.0, an empty string will be returned.
				
		"""
		return self.query(rendererDeviceName=True)
	#----------------------------------------------------------------------
	@property
	def rendererList(self):
		"""
		
				Query for a list of the internal names for renderers available for use with the
				3d modeling viewport. The default list contains at least "vp2Renderer", if supported. See
				rendererName for more details on these renderers. Any plug-in viewport renderers will also appear
				in this list.
				
		"""
		return self.query(rendererList=True)
	#----------------------------------------------------------------------
	@property
	def rendererListUI(self):
		"""
		
				Query for a list of the UI names for renderers available for use with the
				3d modeling viewport. The default list consists of the UI name for "vp2Renderer", if it is supported.
				Any plug-in viewport renderer's UI names will also appear in this list. This list
				and the list returned from rendererList have a 1:1 correspondance.
				
		"""
		return self.query(rendererListUI=True)
	#----------------------------------------------------------------------
	def get_rendererName(self):
		"""
		
				Set or get the renderer used for a 3d modeling viewport. The name provided
				should be an internal name of a renderer. The 'rendererList' flag
				can be used to query for a list of available names.
				The default renderer is "vp2Renderer": Viewport 2.0.
				
		"""
		return self.query(rendererName=True)
	#----------------------------------------------------------------------
	def set_rendererName(self, value):
		"""
		
				Set or get the renderer used for a 3d modeling viewport. The name provided
				should be an internal name of a renderer. The 'rendererList' flag
				can be used to query for a list of available names.
				The default renderer is "vp2Renderer": Viewport 2.0.
				
		"""
		self.edit(rendererName=value)
	#----------------------------------------------------------------------
	rendererName = property(get_rendererName, set_rendererName)
	#----------------------------------------------------------------------
	@property
	def rendererOverrideList(self):
		"""
		
				Query for a list of the internal names for renderer overrides for a 3d viewport renderer.
				Currently only the "Viewport 2" renderer supports renderer overrides.
				
		"""
		return self.query(rendererOverrideList=True)
	#----------------------------------------------------------------------
	@property
	def rendererOverrideListUI(self):
		"""
		
				Query for a list of the UI names for renderer overrides for a 3d viewport renderer.
				Currently only the "Viewport 2" renderer supports renderer overrides.
				
		"""
		return self.query(rendererOverrideListUI=True)
	#----------------------------------------------------------------------
	def get_rendererOverrideName(self):
		"""
		
				Set or get the override used for a 3d viewport renderer. The name provided
				should be the internal name for an override.  The 'rendererOverrideList' flag
				can be used to query for a list of available names.
				Currently only the "Viewport 2" renderer  supports renderer overrides.
				Setting an empty string will unset any currently active override.
				
		"""
		return self.query(rendererOverrideName=True)
	#----------------------------------------------------------------------
	def set_rendererOverrideName(self, value):
		"""
		
				Set or get the override used for a 3d viewport renderer. The name provided
				should be the internal name for an override.  The 'rendererOverrideList' flag
				can be used to query for a list of available names.
				Currently only the "Viewport 2" renderer  supports renderer overrides.
				Setting an empty string will unset any currently active override.
				
		"""
		self.edit(rendererOverrideName=value)
	#----------------------------------------------------------------------
	rendererOverrideName = property(get_rendererOverrideName, set_rendererOverrideName)
	#----------------------------------------------------------------------
	def resetCustomCamera(self,value):
		"""
		
				When specified will reset the camera transform for the active custom camera
				used for a scene render filter. It is only enabled when a valid scene render filter is specified.
				
		"""
		self.edit(resetCustomCamera=value)
	#----------------------------------------------------------------------
	def get_sceneRenderFilter(self):
		"""
		
				Specifies the name of a scene render filter
				
		"""
		return self.query(sceneRenderFilter=True)
	#----------------------------------------------------------------------
	def set_sceneRenderFilter(self, value):
		"""
		
				Specifies the name of a scene render filter
				
		"""
		self.edit(sceneRenderFilter=value)
	#----------------------------------------------------------------------
	sceneRenderFilter = property(get_sceneRenderFilter, set_sceneRenderFilter)
	#----------------------------------------------------------------------
	def get_selectionConnection(self):
		"""
		
				Specifies the name of a selectionConnection object that the
				editor will synchronize with its own selection list. As the user
				selects things in this editor, they will be selected in the
				selectionConnection object. If the object undergoes changes, the
				editor updates to show the changes.
				
		"""
		return self.query(selectionConnection=True)
	#----------------------------------------------------------------------
	def set_selectionConnection(self, value):
		"""
		
				Specifies the name of a selectionConnection object that the
				editor will synchronize with its own selection list. As the user
				selects things in this editor, they will be selected in the
				selectionConnection object. If the object undergoes changes, the
				editor updates to show the changes.
				
		"""
		self.edit(selectionConnection=value)
	#----------------------------------------------------------------------
	selectionConnection = property(get_selectionConnection, set_selectionConnection)
	#----------------------------------------------------------------------
	def get_selectionHiliteDisplay(self):
		"""
		
				Sets whether the model panel will draw any selection hiliting
				on the objects in this window.
				
		"""
		return self.query(selectionHiliteDisplay=True)
	#----------------------------------------------------------------------
	def set_selectionHiliteDisplay(self, value):
		"""
		
				Sets whether the model panel will draw any selection hiliting
				on the objects in this window.
				
		"""
		self.edit(selectionHiliteDisplay=value)
	#----------------------------------------------------------------------
	selectionHiliteDisplay = property(get_selectionHiliteDisplay, set_selectionHiliteDisplay)
	#----------------------------------------------------------------------
	def setSelected(self,value):
		"""
		
				This flag causes the currently active objects to be the
				only objects visible in the view (if viewSelected is true).
				
		"""
		self.edit(setSelected=value)
	#----------------------------------------------------------------------
	def get_shadingModel(self):
		"""
		
				Shading model to use
				
		"""
		return self.query(shadingModel=True)
	#----------------------------------------------------------------------
	def set_shadingModel(self, value):
		"""
		
				Shading model to use
				
		"""
		self.edit(shadingModel=value)
	#----------------------------------------------------------------------
	shadingModel = property(get_shadingModel, set_shadingModel)
	#----------------------------------------------------------------------
	def get_shadows(self):
		"""
		
				Turn on/off the display of hardware shadows in shaded mode.
				
		"""
		return self.query(shadows=True)
	#----------------------------------------------------------------------
	def set_shadows(self, value):
		"""
		
				Turn on/off the display of hardware shadows in shaded mode.
				
		"""
		self.edit(shadows=value)
	#----------------------------------------------------------------------
	shadows = property(get_shadows, set_shadows)
	#----------------------------------------------------------------------
	def get_smallObjectCulling(self):
		"""
		
				Define whether small object culling should be enabled or not
				
		"""
		return self.query(smallObjectCulling=True)
	#----------------------------------------------------------------------
	def set_smallObjectCulling(self, value):
		"""
		
				Define whether small object culling should be enabled or not
				
		"""
		self.edit(smallObjectCulling=value)
	#----------------------------------------------------------------------
	smallObjectCulling = property(get_smallObjectCulling, set_smallObjectCulling)
	#----------------------------------------------------------------------
	def get_smallObjectThreshold(self):
		"""
		
				Threshold used for small object culling
				
		"""
		return self.query(smallObjectThreshold=True)
	#----------------------------------------------------------------------
	def set_smallObjectThreshold(self, value):
		"""
		
				Threshold used for small object culling
				
		"""
		self.edit(smallObjectThreshold=value)
	#----------------------------------------------------------------------
	smallObjectThreshold = property(get_smallObjectThreshold, set_smallObjectThreshold)
	#----------------------------------------------------------------------
	def get_smoothWireframe(self):
		"""
		
				Turns on or off smoothing of wireframe lines and points
				
		"""
		return self.query(smoothWireframe=True)
	#----------------------------------------------------------------------
	def set_smoothWireframe(self, value):
		"""
		
				Turns on or off smoothing of wireframe lines and points
				
		"""
		self.edit(smoothWireframe=value)
	#----------------------------------------------------------------------
	smoothWireframe = property(get_smoothWireframe, set_smoothWireframe)
	#----------------------------------------------------------------------
	def get_sortTransparent(self):
		"""
		
				This flag turns on/off sorting of transparent objects during
				shaded mode refresh. Normally, objects are sorted according to their
				origin in camera space but when this flag is turned off they will be
				drawn according to their (depth-first traversal) order in the scene
				graph. This is a global flag that affects all model editors.
				
		"""
		return self.query(sortTransparent=True)
	#----------------------------------------------------------------------
	def set_sortTransparent(self, value):
		"""
		
				This flag turns on/off sorting of transparent objects during
				shaded mode refresh. Normally, objects are sorted according to their
				origin in camera space but when this flag is turned off they will be
				drawn according to their (depth-first traversal) order in the scene
				graph. This is a global flag that affects all model editors.
				
		"""
		self.edit(sortTransparent=value)
	#----------------------------------------------------------------------
	sortTransparent = property(get_sortTransparent, set_sortTransparent)
	#----------------------------------------------------------------------
	@property
	def stateString(self):
		"""
		
				Query only flag. Returns the MEL command that will create an
				editor to match the current editor state. The returned command string
				uses the string variable $editorName in place of a specific name.
				
		"""
		return self.query(stateString=True)
	#----------------------------------------------------------------------
	def get_stereoDrawMode(self):
		"""
		
				If this flag is used then set stereo draw mode
				
		"""
		return self.query(stereoDrawMode=True)
	#----------------------------------------------------------------------
	def set_stereoDrawMode(self, value):
		"""
		
				If this flag is used then set stereo draw mode
				
		"""
		self.edit(stereoDrawMode=value)
	#----------------------------------------------------------------------
	stereoDrawMode = property(get_stereoDrawMode, set_stereoDrawMode)
	#----------------------------------------------------------------------
	def get_strokes(self):
		"""
		
				Turn on/off the display of Paint Effects strokes for the view
				
		"""
		return self.query(strokes=True)
	#----------------------------------------------------------------------
	def set_strokes(self, value):
		"""
		
				Turn on/off the display of Paint Effects strokes for the view
				
		"""
		self.edit(strokes=value)
	#----------------------------------------------------------------------
	strokes = property(get_strokes, set_strokes)
	#----------------------------------------------------------------------
	def get_textureAnisotropic(self):
		"""
		
				Set whether to perform anisotropic texture filtering.
				Will work only if the anisotropic texture filtering extension
				is supported in OpenGL on the graphics system.
				
		"""
		return self.query(textureAnisotropic=True)
	#----------------------------------------------------------------------
	def set_textureAnisotropic(self, value):
		"""
		
				Set whether to perform anisotropic texture filtering.
				Will work only if the anisotropic texture filtering extension
				is supported in OpenGL on the graphics system.
				
		"""
		self.edit(textureAnisotropic=value)
	#----------------------------------------------------------------------
	textureAnisotropic = property(get_textureAnisotropic, set_textureAnisotropic)
	#----------------------------------------------------------------------
	def get_textureCompression(self):
		"""
		
				Defines whether texture compression should be used or not
				
		"""
		return self.query(textureCompression=True)
	#----------------------------------------------------------------------
	def set_textureCompression(self, value):
		"""
		
				Defines whether texture compression should be used or not
				
		"""
		self.edit(textureCompression=value)
	#----------------------------------------------------------------------
	textureCompression = property(get_textureCompression, set_textureCompression)
	#----------------------------------------------------------------------
	def get_textureDisplay(self):
		"""
		
				Set the type of blending to use for textures.
				The blend is performed between the destination fragment
				and the texture fragment. The source is usually the
				material color. Argument options are:
				"modulate" : multiply the destination and texture fragment
				"decal" : overwrite the destination with the texture fragment
				
		"""
		return self.query(textureDisplay=True)
	#----------------------------------------------------------------------
	def set_textureDisplay(self, value):
		"""
		
				Set the type of blending to use for textures.
				The blend is performed between the destination fragment
				and the texture fragment. The source is usually the
				material color. Argument options are:
				"modulate" : multiply the destination and texture fragment
				"decal" : overwrite the destination with the texture fragment
				
		"""
		self.edit(textureDisplay=value)
	#----------------------------------------------------------------------
	textureDisplay = property(get_textureDisplay, set_textureDisplay)
	#----------------------------------------------------------------------
	def get_textureEnvironmentMap(self):
		"""
		
				If true then use a texture environment map
				
		"""
		return self.query(textureEnvironmentMap=True)
	#----------------------------------------------------------------------
	def set_textureEnvironmentMap(self, value):
		"""
		
				If true then use a texture environment map
				
		"""
		self.edit(textureEnvironmentMap=value)
	#----------------------------------------------------------------------
	textureEnvironmentMap = property(get_textureEnvironmentMap, set_textureEnvironmentMap)
	#----------------------------------------------------------------------
	def get_textureHilight(self):
		"""
		
				Set whether to show specular hilighting
				when the display is in shaded textured mode.
				
		"""
		return self.query(textureHilight=True)
	#----------------------------------------------------------------------
	def set_textureHilight(self, value):
		"""
		
				Set whether to show specular hilighting
				when the display is in shaded textured mode.
				
		"""
		self.edit(textureHilight=value)
	#----------------------------------------------------------------------
	textureHilight = property(get_textureHilight, set_textureHilight)
	#----------------------------------------------------------------------
	def get_textureMaxSize(self):
		"""
		
				Set maximum texture size for hardware texturing.  The integer
				value must be a power of 2.  Recommended values are 128 or 256.  If
				the value specified is larger than the OpenGL maximim textures size
				for the graphics hardware it will be clamped to the OpenGL size.  If
				many large textures are used in a scene reducing this value improves
				performance.  On Impact texture memory is pinned in RAM so using
				large textures can cause reliability and performance problems. Again
				reducing this value will help. Software rendering does not use this
				value.
				This flag is obsolete as of Maya 6.5. The maxTextureResolution/mtr
				argument on the displayPref command should be used instead.
				
		"""
		return self.query(textureMaxSize=True)
	#----------------------------------------------------------------------
	def set_textureMaxSize(self, value):
		"""
		
				Set maximum texture size for hardware texturing.  The integer
				value must be a power of 2.  Recommended values are 128 or 256.  If
				the value specified is larger than the OpenGL maximim textures size
				for the graphics hardware it will be clamped to the OpenGL size.  If
				many large textures are used in a scene reducing this value improves
				performance.  On Impact texture memory is pinned in RAM so using
				large textures can cause reliability and performance problems. Again
				reducing this value will help. Software rendering does not use this
				value.
				This flag is obsolete as of Maya 6.5. The maxTextureResolution/mtr
				argument on the displayPref command should be used instead.
				
		"""
		self.edit(textureMaxSize=value)
	#----------------------------------------------------------------------
	textureMaxSize = property(get_textureMaxSize, set_textureMaxSize)
	#----------------------------------------------------------------------
	@property
	def textureMemoryUsed(self):
		"""
		
				Returns the total number of bytes used by all texture maps.  This
				is typicly width*height*channels for all texture objects in the scene
				If the texture is mip mapped all mip map levels are included in the
				total though not never more than two level will be in use at one time
				
		"""
		return self.query(textureMemoryUsed=True)
	#----------------------------------------------------------------------
	def get_textureSampling(self):
		"""
		
				Set the type of sampling to be used for texture
				display. The argument can be either:
				
				1 : means to perform point sample
				2 : means to perform bilinear interpolation (default)
				
		"""
		return self.query(textureSampling=True)
	#----------------------------------------------------------------------
	def set_textureSampling(self, value):
		"""
		
				Set the type of sampling to be used for texture
				display. The argument can be either:
				
				1 : means to perform point sample
				2 : means to perform bilinear interpolation (default)
				
		"""
		self.edit(textureSampling=value)
	#----------------------------------------------------------------------
	textureSampling = property(get_textureSampling, set_textureSampling)
	#----------------------------------------------------------------------
	def get_textures(self):
		"""
		
				Turn on/off the display of texture objects for the view
				
		"""
		return self.query(textures=True)
	#----------------------------------------------------------------------
	def set_textures(self, value):
		"""
		
				Turn on/off the display of texture objects for the view
				
		"""
		self.edit(textures=value)
	#----------------------------------------------------------------------
	textures = property(get_textures, set_textures)
	#----------------------------------------------------------------------
	def toggleExposure(self,value):
		"""
		
				Toggles between the current and the default exposure value of the editor.
				
		"""
		self.edit(toggleExposure=value)
	#----------------------------------------------------------------------
	def toggleGamma(self,value):
		"""
		
				Toggles between the current and the default gamma value of the editor.
				
		"""
		self.edit(toggleGamma=value)
	#----------------------------------------------------------------------
	def get_transpInShadows(self):
		"""
		
				Set whether to enable display of transparency in shadows when
				using the hardware renderer. The default value is false.
				
		"""
		return self.query(transpInShadows=True)
	#----------------------------------------------------------------------
	def set_transpInShadows(self, value):
		"""
		
				Set whether to enable display of transparency in shadows when
				using the hardware renderer. The default value is false.
				
		"""
		self.edit(transpInShadows=value)
	#----------------------------------------------------------------------
	transpInShadows = property(get_transpInShadows, set_transpInShadows)
	#----------------------------------------------------------------------
	def get_transparencyAlgorithm(self):
		"""
		
				Set the transparency algorithm.
				The options are:
				
				1) "frontAndBackCull" : Two pass front and back culling technique.
				2) "perPolygonSort" : Draw transparent polygons in back-to-front order technique.
				
				transparency pptions 1) and 2) are supported by the hardware renderer. Options 1) is
				supported by the interactive modeling viewports.
				The default value is "frontAndBackCull".
				
		"""
		return self.query(transparencyAlgorithm=True)
	#----------------------------------------------------------------------
	def set_transparencyAlgorithm(self, value):
		"""
		
				Set the transparency algorithm.
				The options are:
				
				1) "frontAndBackCull" : Two pass front and back culling technique.
				2) "perPolygonSort" : Draw transparent polygons in back-to-front order technique.
				
				transparency pptions 1) and 2) are supported by the hardware renderer. Options 1) is
				supported by the interactive modeling viewports.
				The default value is "frontAndBackCull".
				
		"""
		self.edit(transparencyAlgorithm=value)
	#----------------------------------------------------------------------
	transparencyAlgorithm = property(get_transparencyAlgorithm, set_transparencyAlgorithm)
	#----------------------------------------------------------------------
	def get_twoSidedLighting(self):
		"""
		
				Turns on or off two sided lighting.  This may be used with
				the -default flag.
				
		"""
		return self.query(twoSidedLighting=True)
	#----------------------------------------------------------------------
	def set_twoSidedLighting(self, value):
		"""
		
				Turns on or off two sided lighting.  This may be used with
				the -default flag.
				
		"""
		self.edit(twoSidedLighting=value)
	#----------------------------------------------------------------------
	twoSidedLighting = property(get_twoSidedLighting, set_twoSidedLighting)
	#----------------------------------------------------------------------
	def unParent(self,value):
		"""
		
				Specifies that the editor should be removed from its layout.
				This cannot be used in query mode.
				
		"""
		self.edit(unParent=value)
	#----------------------------------------------------------------------
	def unlockMainConnection(self,value):
		"""
		
				Unlocks the mainConnection, effectively restoring the original
				mainConnection (if it is still available), and dynamic updates.
				
		"""
		self.edit(unlockMainConnection=value)
	#----------------------------------------------------------------------
	def updateColorMode(self,value):
		"""
		
				Using this flag tells the model panel to check which color
				mode it should be in, and to switch accordingly.  This flag may
				be used to update a model panel after a camera image plane has
				been added or removed.
				
		"""
		self.edit(updateColorMode=value)
	#----------------------------------------------------------------------
	def updateMainConnection(self,value):
		"""
		
				Causes a locked mainConnection to be updated from the orginal
				mainConnection, but preserves the lock state.
				
		"""
		self.edit(updateMainConnection=value)
	#----------------------------------------------------------------------
	def get_useBaseRenderer(self):
		"""
		
				Set whether to use the "base" renderer when using
				the hardware renderer and in "interactive display mode" (-useInteractiveMode)
				The default value is false.
				
		"""
		return self.query(useBaseRenderer=True)
	#----------------------------------------------------------------------
	def set_useBaseRenderer(self, value):
		"""
		
				Set whether to use the "base" renderer when using
				the hardware renderer and in "interactive display mode" (-useInteractiveMode)
				The default value is false.
				
		"""
		self.edit(useBaseRenderer=value)
	#----------------------------------------------------------------------
	useBaseRenderer = property(get_useBaseRenderer, set_useBaseRenderer)
	#----------------------------------------------------------------------
	def get_useColorIndex(self):
		"""
		
				Sets whether the model panel will attempt to use color index
				mode when possible.  Color index mode can provide a performance
				increase for point, bounding box, and wireframe display modes.
				This may be used with the -default flag.
				
		"""
		return self.query(useColorIndex=True)
	#----------------------------------------------------------------------
	def set_useColorIndex(self, value):
		"""
		
				Sets whether the model panel will attempt to use color index
				mode when possible.  Color index mode can provide a performance
				increase for point, bounding box, and wireframe display modes.
				This may be used with the -default flag.
				
		"""
		self.edit(useColorIndex=value)
	#----------------------------------------------------------------------
	useColorIndex = property(get_useColorIndex, set_useColorIndex)
	#----------------------------------------------------------------------
	def get_useDefaultMaterial(self):
		"""
		
				Sets whether the model panel will draw all the shaded surfaces
				using the default material as opposed to using the material(s) currently
				assigned to the surfaces.
				
		"""
		return self.query(useDefaultMaterial=True)
	#----------------------------------------------------------------------
	def set_useDefaultMaterial(self, value):
		"""
		
				Sets whether the model panel will draw all the shaded surfaces
				using the default material as opposed to using the material(s) currently
				assigned to the surfaces.
				
		"""
		self.edit(useDefaultMaterial=value)
	#----------------------------------------------------------------------
	useDefaultMaterial = property(get_useDefaultMaterial, set_useDefaultMaterial)
	#----------------------------------------------------------------------
	def get_useInteractiveMode(self):
		"""
		
				Turns on or off the use of the special interaction settings
				during playback.  This flag may be used with the -default flag.
				
		"""
		return self.query(useInteractiveMode=True)
	#----------------------------------------------------------------------
	def set_useInteractiveMode(self, value):
		"""
		
				Turns on or off the use of the special interaction settings
				during playback.  This flag may be used with the -default flag.
				
		"""
		self.edit(useInteractiveMode=value)
	#----------------------------------------------------------------------
	useInteractiveMode = property(get_useInteractiveMode, set_useInteractiveMode)
	#----------------------------------------------------------------------
	def get_useRGBImagePlane(self):
		"""
		
				Sets whether the model panel will be forced into RGB mode
				when there is an image plane attached to the panel's camera.
				
		"""
		return self.query(useRGBImagePlane=True)
	#----------------------------------------------------------------------
	def set_useRGBImagePlane(self, value):
		"""
		
				Sets whether the model panel will be forced into RGB mode
				when there is an image plane attached to the panel's camera.
				
		"""
		self.edit(useRGBImagePlane=value)
	#----------------------------------------------------------------------
	useRGBImagePlane = property(get_useRGBImagePlane, set_useRGBImagePlane)
	#----------------------------------------------------------------------
	def get_useReducedRenderer(self):
		"""
		
				Set true if using the reduced renderer
				
		"""
		return self.query(useReducedRenderer=True)
	#----------------------------------------------------------------------
	def set_useReducedRenderer(self, value):
		"""
		
				Set true if using the reduced renderer
				
		"""
		self.edit(useReducedRenderer=value)
	#----------------------------------------------------------------------
	useReducedRenderer = property(get_useReducedRenderer, set_useReducedRenderer)
	#----------------------------------------------------------------------
	def get_userNode(self):
		"""
		
				Allows the user to associate a node name with the modelEditor.
				The value is automatically updated in the event the node is deleted
				or renamed.
				
		"""
		return self.query(userNode=True)
	#----------------------------------------------------------------------
	def set_userNode(self, value):
		"""
		
				Allows the user to associate a node name with the modelEditor.
				The value is automatically updated in the event the node is deleted
				or renamed.
				
		"""
		self.edit(userNode=value)
	#----------------------------------------------------------------------
	userNode = property(get_userNode, set_userNode)
	#----------------------------------------------------------------------
	@property
	def viewObjects(self):
		"""
		
				Returns the name (if any) of the objectSet which contains the
				list of objects visible in the view if viewSelected is true and the
				list of objects being displayed does not come from the
				active list.
				
		"""
		return self.query(viewObjects=True)
	#----------------------------------------------------------------------
	def get_viewSelected(self):
		"""
		
				This flag turns on/off viewing of selected objects. When the
				flag is set to true, the currently active objects are captured and
				used as the list of objects to view.
				
		"""
		return self.query(viewSelected=True)
	#----------------------------------------------------------------------
	def set_viewSelected(self, value):
		"""
		
				This flag turns on/off viewing of selected objects. When the
				flag is set to true, the currently active objects are captured and
				used as the list of objects to view.
				
		"""
		self.edit(viewSelected=value)
	#----------------------------------------------------------------------
	viewSelected = property(get_viewSelected, set_viewSelected)
	#----------------------------------------------------------------------
	def get_viewTransformName(self):
		"""
		
				Sets the view pipeline to be applied if color management is enabled in the
				current editor.
				
		"""
		return self.query(viewTransformName=True)
	#----------------------------------------------------------------------
	def set_viewTransformName(self, value):
		"""
		
				Sets the view pipeline to be applied if color management is enabled in the
				current editor.
				
		"""
		self.edit(viewTransformName=value)
	#----------------------------------------------------------------------
	viewTransformName = property(get_viewTransformName, set_viewTransformName)
	#----------------------------------------------------------------------
	@property
	def viewType(self):
		"""
		
				Returns a string indicating the type of the model editor. For the
				default model editor, returns the empty string. For custom model
				editor types created via the API, returns the same string as is
				returned via the method MPx3dModelView::viewType().
				
		"""
		return self.query(viewType=True)
	#----------------------------------------------------------------------
	@property
	def width(self):
		"""
		
				Return the width of the associated viewport in pixels.
				
		"""
		return self.query(width=True)
	#----------------------------------------------------------------------
	def get_wireframeBackingStore(self):
		"""
		
				Sets whether a backing store is used to optimization the drawing
				of active objects. This mode can provide a performance increase in
				wireframe mode for certain scenes.
				
		"""
		return self.query(wireframeBackingStore=True)
	#----------------------------------------------------------------------
	def set_wireframeBackingStore(self, value):
		"""
		
				Sets whether a backing store is used to optimization the drawing
				of active objects. This mode can provide a performance increase in
				wireframe mode for certain scenes.
				
		"""
		self.edit(wireframeBackingStore=value)
	#----------------------------------------------------------------------
	wireframeBackingStore = property(get_wireframeBackingStore, set_wireframeBackingStore)
	#----------------------------------------------------------------------
	def get_wireframeOnShaded(self):
		"""
		
				Sets whether the model panel will draw the wireframe on
				all shaded objects (if true) or only for active objects (if false).
				
		"""
		return self.query(wireframeOnShaded=True)
	#----------------------------------------------------------------------
	def set_wireframeOnShaded(self, value):
		"""
		Sets whether the model panel will draw the wireframe on
		all shaded objects (if true) or only for active objects (if false).
		"""
		self.edit(wireframeOnShaded=value)
	#----------------------------------------------------------------------
	wireframeOnShaded = property(get_wireframeOnShaded, set_wireframeOnShaded)
	#----------------------------------------------------------------------
	def get_xray(self):
		"""
		
				Turns on or off Xray mode.  This may be used with the -default
				flag.
				
		"""
		return self.query(xray=True)
	#----------------------------------------------------------------------
	def set_xray(self, value):
		"""
		
				Turns on or off Xray mode.  This may be used with the -default
				flag.
				
		"""
		self.edit(xray=value)
	#----------------------------------------------------------------------
	xray = property(get_xray, set_xray)
	
	#----------------------------------------------------------------------
	def get_nurbsCurves(self):
		"""
		
				Turn on/off the display of nurbs curves for the view
				of the model editor.
				
		"""
		return self.query(nurbsCurves=True)
	#----------------------------------------------------------------------
	def set_nurbsCurves(self, value):
		"""
		
				Turn on/off the display of nurbs curves for the view
				of the model editor.
				
		"""
		self.edit(nurbsCurves=value)
	#----------------------------------------------------------------------
	nurbsCurves = property(get_nurbsCurves, set_nurbsCurves)
	#----------------------------------------------------------------------
	def get_controllers(self):
		""""""
		return self.query(controllers=True)
	#----------------------------------------------------------------------
	def set_controllers(self, value):
		""""""
		self.edit(controllers=value)
	#----------------------------------------------------------------------
	controllers = property(get_controllers, set_controllers)
	#----------------------------------------------------------------------
	def get_nurbsSurfaces(self):
		"""
		
				Turn on/off the display of nurbs surfaces for the view
				of the model editor.
				
		"""
		return self.query(nurbsSurfaces=True)
	#----------------------------------------------------------------------
	def set_nurbsSurfaces(self, value):
		"""
		
				Turn on/off the display of nurbs surfaces for the view
				of the model editor.
				
		"""
		self.edit(nurbsSurfaces=value)
	#----------------------------------------------------------------------
	nurbsSurfaces = property(get_nurbsSurfaces, set_nurbsSurfaces)
	#----------------------------------------------------------------------
	def get_controlVertices(self):
		"""
		
				Turn on/off the display of NURBS CVs for the view of the
				model editor.
				
		"""
		return self.query(controlVertices=True)
	#----------------------------------------------------------------------
	def set_controlVertices(self, value):
		"""
		
				Turn on/off the display of NURBS CVs for the view of the
				model editor.
				
		"""
		self.edit(controlVertices=value)
	#----------------------------------------------------------------------
	controlVertices = property(get_controlVertices, set_controlVertices)
	#----------------------------------------------------------------------
	def get_hulls(self):
		"""
		
				Turn on/off the display of NURBS hulls for the view of the
				model editor.
				
		"""
		return self.query(hulls=True)
	#----------------------------------------------------------------------
	def set_hulls(self, value):
		"""
		
				Turn on/off the display of NURBS hulls for the view of the
				model editor.
				
		"""
		self.edit(hulls=value)
	#----------------------------------------------------------------------
	hulls = property(get_hulls, set_hulls)
	#----------------------------------------------------------------------
	def get_polymeshes(self):
		"""
		
				Turn on/off the display of polygon meshes for the view
				of the model editor.
				
		"""
		return self.query(polymeshes=True)
	#----------------------------------------------------------------------
	def set_polymeshes(self, value):
		"""
		
				Turn on/off the display of polygon meshes for the view
				of the model editor.
				
		"""
		self.edit(polymeshes=value)
	#----------------------------------------------------------------------
	polymeshes = property(get_polymeshes, set_polymeshes)
	#----------------------------------------------------------------------
	def get_subdivSurfaces(self):
		"""
		
				Turn on/off the display of subdivision surfaces for the view
				of the model editor.
				
		"""
		return self.query(subdivSurfaces=True)
	#----------------------------------------------------------------------
	def set_subdivSurfaces(self, value):
		"""
		
				Turn on/off the display of subdivision surfaces for the view
				of the model editor.
				
		"""
		self.edit(subdivSurfaces=value)
	#----------------------------------------------------------------------
	subdivSurfaces = property(get_subdivSurfaces, set_subdivSurfaces)
	#----------------------------------------------------------------------
	def get_planes(self):
		"""
		
				Turn on/off the display of sketch planes for the view
				of the model editor.
				
		"""
		return self.query(planes=True)
	#----------------------------------------------------------------------
	def set_planes(self, value):
		"""
		
				Turn on/off the display of sketch planes for the view
				of the model editor.
				
		"""
		self.edit(planes=value)
	#----------------------------------------------------------------------
	planes = property(get_planes, set_planes)
	#----------------------------------------------------------------------
	def get_lights(self):
		"""
		
				Turn on/off the display of lights for the view of the
				model editor.
				
		"""
		return self.query(lights=True)
	#----------------------------------------------------------------------
	def set_lights(self, value):
		"""
		
				Turn on/off the display of lights for the view of the
				model editor.
				
		"""
		self.edit(lights=value)
	#----------------------------------------------------------------------
	lights = property(get_lights, set_lights)
	#----------------------------------------------------------------------
	def get_cameras(self):
		"""
		
				Turn on/off the display of cameras for the view of the
				model editor.
				
		"""
		return self.query(cameras=True)
	#----------------------------------------------------------------------
	def set_cameras(self, value):
		"""
		
				Turn on/off the display of cameras for the view of the
				model editor.
				
		"""
		self.edit(cameras=value)
	#----------------------------------------------------------------------
	cameras = property(get_cameras, set_cameras)
	#----------------------------------------------------------------------
	def get_imagePlane(self):
		"""
		
				Turn on/off the display of image plane for the view
				
		"""
		return self.query(imagePlane=True)
	#----------------------------------------------------------------------
	def set_imagePlane(self, value):
		"""
		
				Turn on/off the display of image plane for the view
				
		"""
		self.edit(imagePlane=value)
	#----------------------------------------------------------------------
	imagePlane = property(get_imagePlane, set_imagePlane)
	#----------------------------------------------------------------------
	def get_joints(self):
		"""
		
				Turn on/off the display of joints for the view of the
				model editor.
				
		"""
		return self.query(joints=True)
	#----------------------------------------------------------------------
	def set_joints(self, value):
		"""
		
				Turn on/off the display of joints for the view of the
				model editor.
				
		"""
		self.edit(joints=value)
	#----------------------------------------------------------------------
	joints = property(get_joints, set_joints)