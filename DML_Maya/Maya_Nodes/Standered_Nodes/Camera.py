import maya.cmds as cmds
from ..Abstract_Nodes import Dag_Node
from ...General_Utils import flatten
	
########################################################################
class Camera(Dag_Node):
	RETURN_OVERIDE_CHECK_TYPE = "transform"
	#----------------------------------------------------------------------
	@classmethod
	def _overide_Return_Check(cls,node):
		""""""
		return cmds.listRelatives(node,typ='camera', children=True, shapes=True,) != None
	#----------------------------------------------------------------------
	@classmethod
	def createNode(cls,*args,**kwargs):
		""""""
		return cmds.camera(*args,**kwargs)[0]
	
	#----------------------------------------------------------------------
	def _edit(self,**kwargs):
		""""""
		kwargs["edit"]=True
		cmds.camera(self,**kwargs)
	#----------------------------------------------------------------------
	def _query(self,**kwargs):
		""""""
		kwargs["query"]=True
		cmds.camera(self,**kwargs)	
		
	
	#----------------------------------------------------------------------
	def get_aspectRatio(self):
		"""The ratio of the film back width to the film back height.
		"""
		return self._query(aspectRatio=True)
	#----------------------------------------------------------------------
	def set_aspectRatio(self,value):
		"""The ratio of the film back width to the film back height.
		"""
		self._edit(aspectRatio=value)
	#----------------------------------------------------------------------
	aspectRatio = property(fget=get_aspectRatio,fset=set_aspectRatio)

	#----------------------------------------------------------------------
	def get_cameraScale(self):
		"""Scale the camera.
		"""
		return self._query(cameraScale=True)
	#----------------------------------------------------------------------
	def set_cameraScale(self,value):
		"""Scale the camera.
		"""
		self._edit(cameraScale=value)
	#----------------------------------------------------------------------
	cameraScale = property(fget=get_cameraScale,fset=set_cameraScale)

	#----------------------------------------------------------------------
	def get_centerOfInterest(self):
		"""Set the linear distance from the camera's eye point to the
		center of interest.
		"""
		return self._query(centerOfInterest=True)
	#----------------------------------------------------------------------
	def set_centerOfInterest(self,value):
		"""Set the linear distance from the camera's eye point to the
		center of interest.
		"""
		self._edit(centerOfInterest=value)
	#----------------------------------------------------------------------
	centerOfInterest = property(fget=get_centerOfInterest,fset=set_centerOfInterest)

	#----------------------------------------------------------------------
	def get_clippingPlanes(self):
		"""Activate manual clipping planes.
		"""
		return self._query(clippingPlanes=True)
	#----------------------------------------------------------------------
	def set_clippingPlanes(self,value):
		"""Activate manual clipping planes.
		"""
		self._edit(clippingPlanes=value)
	#----------------------------------------------------------------------
	clippingPlanes = property(fget=get_clippingPlanes,fset=set_clippingPlanes)

	#----------------------------------------------------------------------
	def get_depthOfField(self):
		"""Determines whether a depth of field calculation is performed
		to give varying focus depending on the distance of the
		objects.
		"""
		return self._query(depthOfField=True)
	#----------------------------------------------------------------------
	def set_depthOfField(self,value):
		"""Determines whether a depth of field calculation is performed
		to give varying focus depending on the distance of the
		objects.
		"""
		self._edit(depthOfField=value)
	#----------------------------------------------------------------------
	depthOfField = property(fget=get_depthOfField,fset=set_depthOfField)

	#----------------------------------------------------------------------
	def get_displayFieldChart(self):
		"""Activate display of the video field chart when looking through
		the camera.
		"""
		return self._query(displayFieldChart=True)
	#----------------------------------------------------------------------
	def set_displayFieldChart(self,value):
		"""Activate display of the video field chart when looking through
		the camera.
		"""
		self._edit(displayFieldChart=value)
	#----------------------------------------------------------------------
	displayFieldChart = property(fget=get_displayFieldChart,fset=set_displayFieldChart)

	#----------------------------------------------------------------------
	def get_displayFilmGate(self):
		"""Activate display of the film gate icons when looking through
		the camera.
		"""
		return self._query(displayFilmGate=True)
	#----------------------------------------------------------------------
	def set_displayFilmGate(self,value):
		"""Activate display of the film gate icons when looking through
		the camera.
		"""
		self._edit(displayFilmGate=value)
	#----------------------------------------------------------------------
	displayFilmGate = property(fget=get_displayFilmGate,fset=set_displayFilmGate)

	#----------------------------------------------------------------------
	def get_displayFilmOrigin(self):
		"""Activate the display of the film origin guide when
		looking through the camera.
		"""
		return self._query(displayFilmOrigin=True)
	#----------------------------------------------------------------------
	def set_displayFilmOrigin(self,value):
		"""Activate the display of the film origin guide when
		looking through the camera.
		"""
		self._edit(displayFilmOrigin=value)
	#----------------------------------------------------------------------
	displayFilmOrigin = property(fget=get_displayFilmOrigin,fset=set_displayFilmOrigin)

	#----------------------------------------------------------------------
	def get_displayFilmPivot(self):
		"""Activate display of the film pivot guide when looking
		through the camera.
		"""
		return self._query(displayFilmPivot=True)
	#----------------------------------------------------------------------
	def set_displayFilmPivot(self,value):
		"""Activate display of the film pivot guide when looking
		through the camera.
		"""
		self._edit(displayFilmPivot=value)
	#----------------------------------------------------------------------
	displayFilmPivot = property(fget=get_displayFilmPivot,fset=set_displayFilmPivot)

	#----------------------------------------------------------------------
	def get_displayGateMask(self):
		"""Display the gate mask, file or resolution, as a shaded area
		to the edge of the viewport.
		"""
		return self._query(displayGateMask=True)
	#----------------------------------------------------------------------
	def set_displayGateMask(self,value):
		"""Display the gate mask, file or resolution, as a shaded area
		to the edge of the viewport.
		"""
		self._edit(displayGateMask=value)
	#----------------------------------------------------------------------
	displayGateMask = property(fget=get_displayGateMask,fset=set_displayGateMask)

	#----------------------------------------------------------------------
	def get_displayResolution(self):
		"""Activate display of the current rendering resolution (as
		defined in the render globals) when looking through the
		camera.
		"""
		return self._query(displayResolution=True)
	#----------------------------------------------------------------------
	def set_displayResolution(self,value):
		"""Activate display of the current rendering resolution (as
		defined in the render globals) when looking through the
		camera.
		"""
		self._edit(displayResolution=value)
	#----------------------------------------------------------------------
	displayResolution = property(fget=get_displayResolution,fset=set_displayResolution)

	#----------------------------------------------------------------------
	def get_displaySafeAction(self):
		"""Activate display of the video Safe Action guide
		when looking through the camera.
		"""
		return self._query(displaySafeAction=True)
	#----------------------------------------------------------------------
	def set_displaySafeAction(self,value):
		"""Activate display of the video Safe Action guide
		when looking through the camera.
		"""
		self._edit(displaySafeAction=value)
	#----------------------------------------------------------------------
	displaySafeAction = property(fget=get_displaySafeAction,fset=set_displaySafeAction)

	#----------------------------------------------------------------------
	def get_displaySafeTitle(self):
		"""Activate display of the video Safe Title guide
		when looking through the camera.
		"""
		return self._query(displaySafeTitle=True)
	#----------------------------------------------------------------------
	def set_displaySafeTitle(self,value):
		"""Activate display of the video Safe Title guide
		when looking through the camera.
		"""
		self._edit(displaySafeTitle=value)
	#----------------------------------------------------------------------
	displaySafeTitle = property(fget=get_displaySafeTitle,fset=set_displaySafeTitle)

	#----------------------------------------------------------------------
	def get_fStop(self):
		"""A real lens normally contains a diaphragm or other stop which
		blocks some of the light that would otherwise pass through
		it. This stop is usually approximately round, and its diameter
		as seen from the front of the lens is called the lens
		diameter. The lens diameter is often described by its relation
		to the focal length of the lens. A lens whose diameter is
		one-eighth its local length is said to have an F-stop of
		8. This is an optical property of the lens.
		"""
		return self._query(fStop=True)
	#----------------------------------------------------------------------
	def set_fStop(self,value):
		"""A real lens normally contains a diaphragm or other stop which
		blocks some of the light that would otherwise pass through
		it. This stop is usually approximately round, and its diameter
		as seen from the front of the lens is called the lens
		diameter. The lens diameter is often described by its relation
		to the focal length of the lens. A lens whose diameter is
		one-eighth its local length is said to have an F-stop of
		8. This is an optical property of the lens.
		"""
		self._edit(fStop=value)
	#----------------------------------------------------------------------
	fStop = property(fget=get_fStop,fset=set_fStop)

	#----------------------------------------------------------------------
	def get_farClipPlane(self):
		"""Specify the distance to the far clipping plane.
		"""
		return self._query(farClipPlane=True)
	#----------------------------------------------------------------------
	def set_farClipPlane(self,value):
		"""Specify the distance to the far clipping plane.
		"""
		self._edit(farClipPlane=value)
	#----------------------------------------------------------------------
	farClipPlane = property(fget=get_farClipPlane,fset=set_farClipPlane)

	#----------------------------------------------------------------------
	def get_farFocusDistance(self):
		"""Linear distance to the far focus plane.
		"""
		return self._query(farFocusDistance=True)
	#----------------------------------------------------------------------
	def set_farFocusDistance(self,value):
		"""Linear distance to the far focus plane.
		"""
		self._edit(farFocusDistance=value)
	#----------------------------------------------------------------------
	farFocusDistance = property(fget=get_farFocusDistance,fset=set_farFocusDistance)

	#----------------------------------------------------------------------
	def get_filmFit(self):
		"""This describes how the digital image (in pixels) relates to
		the film back. Since the film back is defined in terms of real
		numbers with some arbitrary film aspect, and the digital image
		is defined in integer pixels with an equally arbitrary (and
		different) resolution, relating the two can get
		complicated. There are 4 choices: 
		
		horizontal 
		In this case the digital image is made to fit the film
		back exactly in the horizontal direction. This then gives each
		pixel a horizontal size = (film back width) / (horizontal
		resolution). The pixel height is then = (pixel width) / (pixel
		aspect ratio). Now that the pixel has a size, resolution gives
		us a complete image. That image will match the film back
		exactly in width. It will almost never match in height, either
		being too tall or too short. By playing with the numbers you
		can get it pretty close though.
		vertical
		This is the same idea as horizontal fit, only applied
		vertically. Thus the digital image will match the film back
		exactly in height, but miss in width.
		fill
		This is a convenience item. The system calculates both
		horizontal and vertical fits and then applies the one that
		makes the digital image larger than the film back.
		overscan
		Overscanning the film gate in the camera view allows us
		to choreograph action outside of the frustum from within the
		camera view without having to resort to a dolly or zoom. This
		feature is also essential for animating image planes.
		"""
		return self._query(filmFit=True)
	#----------------------------------------------------------------------
	def set_filmFit(self,value):
		"""This describes how the digital image (in pixels) relates to
		the film back. Since the film back is defined in terms of real
		numbers with some arbitrary film aspect, and the digital image
		is defined in integer pixels with an equally arbitrary (and
		different) resolution, relating the two can get
		complicated. There are 4 choices: 
		
		horizontal 
		In this case the digital image is made to fit the film
		back exactly in the horizontal direction. This then gives each
		pixel a horizontal size = (film back width) / (horizontal
		resolution). The pixel height is then = (pixel width) / (pixel
		aspect ratio). Now that the pixel has a size, resolution gives
		us a complete image. That image will match the film back
		exactly in width. It will almost never match in height, either
		being too tall or too short. By playing with the numbers you
		can get it pretty close though.
		vertical
		This is the same idea as horizontal fit, only applied
		vertically. Thus the digital image will match the film back
		exactly in height, but miss in width.
		fill
		This is a convenience item. The system calculates both
		horizontal and vertical fits and then applies the one that
		makes the digital image larger than the film back.
		overscan
		Overscanning the film gate in the camera view allows us
		to choreograph action outside of the frustum from within the
		camera view without having to resort to a dolly or zoom. This
		feature is also essential for animating image planes.
		"""
		self._edit(filmFit=value)
	#----------------------------------------------------------------------
	filmFit = property(fget=get_filmFit,fset=set_filmFit)

	#----------------------------------------------------------------------
	def get_filmFitOffset(self):
		"""Since we know from the above that the digital image may not
		match the film back exactly, we now have the question of how
		to position one relative to the other. Thus fit
		offset. Normally the centers are aligned. Fit offset lets you
		move the smaller image within the larger one. Specify the
		distance for film offset (inches).
		"""
		return self._query(filmFitOffset=True)
	#----------------------------------------------------------------------
	def set_filmFitOffset(self,value):
		"""Since we know from the above that the digital image may not
		match the film back exactly, we now have the question of how
		to position one relative to the other. Thus fit
		offset. Normally the centers are aligned. Fit offset lets you
		move the smaller image within the larger one. Specify the
		distance for film offset (inches).
		"""
		self._edit(filmFitOffset=value)
	#----------------------------------------------------------------------
	filmFitOffset = property(fget=get_filmFitOffset,fset=set_filmFitOffset)

	#----------------------------------------------------------------------
	def get_filmRollOrder(self):
		"""Specifies how the roll is applied with respect to the
		pivot value.
		
		Rotate-Translate
		The film back is first rotated then translated by the
		pivot point value.
		Translate-Rotate
		The film back is first translated then rotated by the
		film roll value.
		"""
		return self._query(filmRollOrder=True)
	#----------------------------------------------------------------------
	def set_filmRollOrder(self,value):
		"""Specifies how the roll is applied with respect to the
		pivot value.
		
		Rotate-Translate
		The film back is first rotated then translated by the
		pivot point value.
		Translate-Rotate
		The film back is first translated then rotated by the
		film roll value.
		"""
		self._edit(filmRollOrder=value)
	#----------------------------------------------------------------------
	filmRollOrder = property(fget=get_filmRollOrder,fset=set_filmRollOrder)

	#----------------------------------------------------------------------
	def get_filmRollValue(self):
		"""This specifies that amount of rotation around the film back.
		The roll value is specified in degrees. The rotation occurs around
		the specified pivot point. This value is used to compute a film
		roll matrix, which is a component of the post-projection matrix.
		"""
		return self._query(filmRollValue=True)
	#----------------------------------------------------------------------
	def set_filmRollValue(self,value):
		"""This specifies that amount of rotation around the film back.
		The roll value is specified in degrees. The rotation occurs around
		the specified pivot point. This value is used to compute a film
		roll matrix, which is a component of the post-projection matrix.
		"""
		self._edit(filmRollValue=value)
	#----------------------------------------------------------------------
	filmRollValue = property(fget=get_filmRollValue,fset=set_filmRollValue)

	#----------------------------------------------------------------------
	def get_filmTranslateH(self):
		"""The horizontal film translation. Values are normalized to
		the viewing area.
		"""
		return self._query(filmTranslateH=True)
	#----------------------------------------------------------------------
	def set_filmTranslateH(self,value):
		"""The horizontal film translation. Values are normalized to
		the viewing area.
		"""
		self._edit(filmTranslateH=value)
	#----------------------------------------------------------------------
	filmTranslateH = property(fget=get_filmTranslateH,fset=set_filmTranslateH)

	#----------------------------------------------------------------------
	def get_filmTranslateV(self):
		"""The vertical film translation. Values are normalized to the
		viewing area.
		"""
		return self._query(filmTranslateV=True)
	#----------------------------------------------------------------------
	def set_filmTranslateV(self,value):
		"""The vertical film translation. Values are normalized to the
		viewing area.
		"""
		self._edit(filmTranslateV=value)
	#----------------------------------------------------------------------
	filmTranslateV = property(fget=get_filmTranslateV,fset=set_filmTranslateV)

	#----------------------------------------------------------------------
	def get_focalLength(self):
		"""This is the distance along the lens axis between the lens and
		the film plane when "focal distance" is infinitely large. This
		is an optical property of the lens. This double precision
		parameter is always specified in millimeters.
		"""
		return self._query(focalLength=True)
	#----------------------------------------------------------------------
	def set_focalLength(self,value):
		"""This is the distance along the lens axis between the lens and
		the film plane when "focal distance" is infinitely large. This
		is an optical property of the lens. This double precision
		parameter is always specified in millimeters.
		"""
		self._edit(focalLength=value)
	#----------------------------------------------------------------------
	focalLength = property(fget=get_focalLength,fset=set_focalLength)

	#----------------------------------------------------------------------
	def get_focusDistance(self):
		"""Set the focus at a certain distance in front of the camera.
		"""
		return self._query(focusDistance=True)
	#----------------------------------------------------------------------
	def set_focusDistance(self,value):
		"""Set the focus at a certain distance in front of the camera.
		"""
		self._edit(focusDistance=value)
	#----------------------------------------------------------------------
	focusDistance = property(fget=get_focusDistance,fset=set_focusDistance)

	#----------------------------------------------------------------------
	def get_homeCommand(self):
		"""Specify the command to execute when "viewSet -home" is applied
		to this camera. All occurances of "%camera" will be replaced
		with the cameras name before viewSet runs the command.
		"""
		return self._query(homeCommand=True)
	#----------------------------------------------------------------------
	def set_homeCommand(self,value):
		"""Specify the command to execute when "viewSet -home" is applied
		to this camera. All occurances of "%camera" will be replaced
		with the cameras name before viewSet runs the command.
		"""
		self._edit(homeCommand=value)
	#----------------------------------------------------------------------
	homeCommand = property(fget=get_homeCommand,fset=set_homeCommand)

	#----------------------------------------------------------------------
	def get_horizontalFieldOfView(self):
		"""This is the film back width as seen by the lens when focused
		at infinity (ie., focal length away) measured as an
		angle. Note that it has nothing to do with pixels or the
		digital image or any aspects. Angle of view is a derived
		field, that is, it is not used internally by Alias and can be
		completely determined from other information. It is included
		as a convenience for the user. Its derivation is aov = 2 *
		atan( fbw / (2 * f) ) where "aov" is the angle of view, "fbw"
		is the film back width and "f" is the focal length.
		"""
		return self._query(horizontalFieldOfView=True)
	#----------------------------------------------------------------------
	def set_horizontalFieldOfView(self,value):
		"""This is the film back width as seen by the lens when focused
		at infinity (ie., focal length away) measured as an
		angle. Note that it has nothing to do with pixels or the
		digital image or any aspects. Angle of view is a derived
		field, that is, it is not used internally by Alias and can be
		completely determined from other information. It is included
		as a convenience for the user. Its derivation is aov = 2 *
		atan( fbw / (2 * f) ) where "aov" is the angle of view, "fbw"
		is the film back width and "f" is the focal length.
		"""
		self._edit(horizontalFieldOfView=value)
	#----------------------------------------------------------------------
	horizontalFieldOfView = property(fget=get_horizontalFieldOfView,fset=set_horizontalFieldOfView)

	#----------------------------------------------------------------------
	def get_horizontalFilmAperture(self):
		"""The horizontal width of the camera's film plane. The camera's
		film is located on the film plane. The extent of the film
		which will be exposed to an image of the scene in front of the
		lens is limited to a rectangular area described by the film
		back. This double precision parameter is always specified in
		inches.
		"""
		return self._query(horizontalFilmAperture=True)
	#----------------------------------------------------------------------
	def set_horizontalFilmAperture(self,value):
		"""The horizontal width of the camera's film plane. The camera's
		film is located on the film plane. The extent of the film
		which will be exposed to an image of the scene in front of the
		lens is limited to a rectangular area described by the film
		back. This double precision parameter is always specified in
		inches.
		"""
		self._edit(horizontalFilmAperture=value)
	#----------------------------------------------------------------------
	horizontalFilmAperture = property(fget=get_horizontalFilmAperture,fset=set_horizontalFilmAperture)

	#----------------------------------------------------------------------
	def get_horizontalFilmOffset(self):
		"""Horizontal offset from the center of the film back. Normally
		the film back will be centered on the lens axis. However, this
		need not be so. Film offset is the displacement of the center
		of the film back from the lens axis, also measured in
		inches. Note that offsetting the film back will distort the
		image, but will not alter the focus. This double precision
		parameter is always specified in inches.
		"""
		return self._query(horizontalFilmOffset=True)
	#----------------------------------------------------------------------
	def set_horizontalFilmOffset(self,value):
		"""Horizontal offset from the center of the film back. Normally
		the film back will be centered on the lens axis. However, this
		need not be so. Film offset is the displacement of the center
		of the film back from the lens axis, also measured in
		inches. Note that offsetting the film back will distort the
		image, but will not alter the focus. This double precision
		parameter is always specified in inches.
		"""
		self._edit(horizontalFilmOffset=value)
	#----------------------------------------------------------------------
	horizontalFilmOffset = property(fget=get_horizontalFilmOffset,fset=set_horizontalFilmOffset)

	#----------------------------------------------------------------------
	def get_horizontalPan(self):
		"""Horizontal 2D camera pan (inches)
		"""
		return self._query(horizontalPan=True)
	#----------------------------------------------------------------------
	def set_horizontalPan(self,value):
		"""Horizontal 2D camera pan (inches)
		"""
		self._edit(horizontalPan=value)
	#----------------------------------------------------------------------
	horizontalPan = property(fget=get_horizontalPan,fset=set_horizontalPan)

	#----------------------------------------------------------------------
	def get_horizontalRollPivot(self):
		"""The horizontal pivot point from the center of the film back.
		The pivot point is used during rotation of the film back.  The pivot
		is the point where the rotation occurs around. This double precision
		parameter corresponds to the normalized viewport. This value is a
		part of the post projection matrix.
		"""
		return self._query(horizontalRollPivot=True)
	#----------------------------------------------------------------------
	def set_horizontalRollPivot(self,value):
		"""The horizontal pivot point from the center of the film back.
		The pivot point is used during rotation of the film back.  The pivot
		is the point where the rotation occurs around. This double precision
		parameter corresponds to the normalized viewport. This value is a
		part of the post projection matrix.
		"""
		self._edit(horizontalRollPivot=value)
	#----------------------------------------------------------------------
	horizontalRollPivot = property(fget=get_horizontalRollPivot,fset=set_horizontalRollPivot)

	#----------------------------------------------------------------------
	def get_horizontalShake(self):
		"""Another horizontal offset from the center of the film back,
		which can be used and stored on the camera in addition to the
		horizonal film offset attribute.  This allows for film-based
		camera shake internal to the camera.  This works in exactly the same
		units and coordinates that the film offset attribute does.
		The effect of this attribute is toggled by the shake enabled attribute.
		"""
		return self._query(horizontalShake=True)
	#----------------------------------------------------------------------
	def set_horizontalShake(self,value):
		"""Another horizontal offset from the center of the film back,
		which can be used and stored on the camera in addition to the
		horizonal film offset attribute.  This allows for film-based
		camera shake internal to the camera.  This works in exactly the same
		units and coordinates that the film offset attribute does.
		The effect of this attribute is toggled by the shake enabled attribute.
		"""
		self._edit(horizontalShake=value)
	#----------------------------------------------------------------------
	horizontalShake = property(fget=get_horizontalShake,fset=set_horizontalShake)

	#----------------------------------------------------------------------
	def get_journalCommand(self):
		"""Journal interactive camera commands. Commands can be undone
		when a camera is journaled.
		"""
		return self._query(journalCommand=True)
	#----------------------------------------------------------------------
	def set_journalCommand(self,value):
		"""Journal interactive camera commands. Commands can be undone
		when a camera is journaled.
		"""
		self._edit(journalCommand=value)
	#----------------------------------------------------------------------
	journalCommand = property(fget=get_journalCommand,fset=set_journalCommand)

	#----------------------------------------------------------------------
	def get_lensSqueezeRatio(self):
		"""This is presently just an information field in the camera
		editor is meant to convey the horizontal distortion of the
		anamorphic lens normally used with some film formats. If it
		were used, it would do something like pixel aspect. Remember
		however that lens distortion (intentional or not) is slightly
		different than the output hardware's quantization. The fact
		that a "net" distortion parameter could be used for both may
		or may not confuse the issue.
		"""
		return self._query(lensSqueezeRatio=True)
	#----------------------------------------------------------------------
	def set_lensSqueezeRatio(self,value):
		"""This is presently just an information field in the camera
		editor is meant to convey the horizontal distortion of the
		anamorphic lens normally used with some film formats. If it
		were used, it would do something like pixel aspect. Remember
		however that lens distortion (intentional or not) is slightly
		different than the output hardware's quantization. The fact
		that a "net" distortion parameter could be used for both may
		or may not confuse the issue.
		"""
		self._edit(lensSqueezeRatio=value)
	#----------------------------------------------------------------------
	lensSqueezeRatio = property(fget=get_lensSqueezeRatio,fset=set_lensSqueezeRatio)

	#----------------------------------------------------------------------
	def get_lockTransform(self):
		"""Lock the camera. When a camera is locked, its transformation information,
		that is, its Translate and Rotate properties cannot be adjusted, and the
		center of interest point cannot be moved.
		For orthographic cameras, Orthographic Width is also locked.
		For camera groups, Aim and Up locator's translate is also locked.
		For stereo cameras, the root camera is locked.
		"""
		return self._query(lockTransform=True)
	#----------------------------------------------------------------------
	def set_lockTransform(self,value):
		"""Lock the camera. When a camera is locked, its transformation information,
		that is, its Translate and Rotate properties cannot be adjusted, and the
		center of interest point cannot be moved.
		For orthographic cameras, Orthographic Width is also locked.
		For camera groups, Aim and Up locator's translate is also locked.
		For stereo cameras, the root camera is locked.
		"""
		self._edit(lockTransform=value)
	#----------------------------------------------------------------------
	lockTransform = property(fget=get_lockTransform,fset=set_lockTransform)

	#----------------------------------------------------------------------
	def get_motionBlur(self):
		"""Determines whether the camera's image is motion blured (as
		opposed to an object's image). For example, if you want to
		blur the camera movement when you are performing a flyby.
		"""
		return self._query(motionBlur=True)
	#----------------------------------------------------------------------
	def set_motionBlur(self,value):
		"""Determines whether the camera's image is motion blured (as
		opposed to an object's image). For example, if you want to
		blur the camera movement when you are performing a flyby.
		"""
		self._edit(motionBlur=value)
	#----------------------------------------------------------------------
	motionBlur = property(fget=get_motionBlur,fset=set_motionBlur)

	#----------------------------------------------------------------------
	def get_nearClipPlane(self):
		"""Specify the distance to the NEAR clipping plane.
		"""
		return self._query(nearClipPlane=True)
	#----------------------------------------------------------------------
	def set_nearClipPlane(self,value):
		"""Specify the distance to the NEAR clipping plane.
		"""
		self._edit(nearClipPlane=value)
	#----------------------------------------------------------------------
	nearClipPlane = property(fget=get_nearClipPlane,fset=set_nearClipPlane)

	#----------------------------------------------------------------------
	def get_nearFocusDistance(self):
		"""Linear distance to the near focus plane.
		"""
		return self._query(nearFocusDistance=True)
	#----------------------------------------------------------------------
	def set_nearFocusDistance(self,value):
		"""Linear distance to the near focus plane.
		"""
		self._edit(nearFocusDistance=value)
	#----------------------------------------------------------------------
	nearFocusDistance = property(fget=get_nearFocusDistance,fset=set_nearFocusDistance)

	#----------------------------------------------------------------------
	def get_orthographic(self):
		"""Activate the orthographic camera.
		"""
		return self._query(orthographic=True)
	#----------------------------------------------------------------------
	def set_orthographic(self,value):
		"""Activate the orthographic camera.
		"""
		self._edit(orthographic=value)
	#----------------------------------------------------------------------
	orthographic = property(fget=get_orthographic,fset=set_orthographic)

	#----------------------------------------------------------------------
	def get_orthographicWidth(self):
		"""Set the orthographic projection width.
		"""
		return self._query(orthographicWidth=True)
	#----------------------------------------------------------------------
	def set_orthographicWidth(self,value):
		"""Set the orthographic projection width.
		"""
		self._edit(orthographicWidth=value)
	#----------------------------------------------------------------------
	orthographicWidth = property(fget=get_orthographicWidth,fset=set_orthographicWidth)

	#----------------------------------------------------------------------
	def get_overscan(self):
		"""Set the percent of overscan.
		"""
		return self._query(overscan=True)
	#----------------------------------------------------------------------
	def set_overscan(self,value):
		"""Set the percent of overscan.
		"""
		self._edit(overscan=value)
	#----------------------------------------------------------------------
	overscan = property(fget=get_overscan,fset=set_overscan)

	#----------------------------------------------------------------------
	def get_panZoomEnabled(self):
		"""Toggle camera 2D pan and zoom
		"""
		return self._query(panZoomEnabled=True)
	#----------------------------------------------------------------------
	def set_panZoomEnabled(self,value):
		"""Toggle camera 2D pan and zoom
		"""
		self._edit(panZoomEnabled=value)
	#----------------------------------------------------------------------
	panZoomEnabled = property(fget=get_panZoomEnabled,fset=set_panZoomEnabled)

	#----------------------------------------------------------------------
	def get_position(self):
		"""Three linear values can be specified to translate the camera.
		"""
		return self._query(position=True)
	#----------------------------------------------------------------------
	def set_position(self,value):
		"""Three linear values can be specified to translate the camera.
		"""
		self._edit(position=value)
	#----------------------------------------------------------------------
	position = property(fget=get_position,fset=set_position)

	#----------------------------------------------------------------------
	def get_postScale(self):
		"""The post-scale value.  This value multiplied against
		the computed projection matrix. It is applied after the
		the film roll.
		"""
		return self._query(postScale=True)
	#----------------------------------------------------------------------
	def set_postScale(self,value):
		"""The post-scale value.  This value multiplied against
		the computed projection matrix. It is applied after the
		the film roll.
		"""
		self._edit(postScale=value)
	#----------------------------------------------------------------------
	postScale = property(fget=get_postScale,fset=set_postScale)

	#----------------------------------------------------------------------
	def get_preScale(self):
		"""The pre-scale value. The value is multiplied against
		the computed projection matrix. It is applied before the film
		roll.
		"""
		return self._query(preScale=True)
	#----------------------------------------------------------------------
	def set_preScale(self,value):
		"""The pre-scale value. The value is multiplied against
		the computed projection matrix. It is applied before the film
		roll.
		"""
		self._edit(preScale=value)
	#----------------------------------------------------------------------
	preScale = property(fget=get_preScale,fset=set_preScale)

	#----------------------------------------------------------------------
	def get_renderPanZoom(self):
		"""Toggle camera 2D pan and zoom in render
		"""
		return self._query(renderPanZoom=True)
	#----------------------------------------------------------------------
	def set_renderPanZoom(self,value):
		"""Toggle camera 2D pan and zoom in render
		"""
		self._edit(renderPanZoom=value)
	#----------------------------------------------------------------------
	renderPanZoom = property(fget=get_renderPanZoom,fset=set_renderPanZoom)

	#----------------------------------------------------------------------
	def get_rotation(self):
		"""Three angular values can be specified to rotate the camera.
		"""
		return self._query(rotation=True)
	#----------------------------------------------------------------------
	def set_rotation(self,value):
		"""Three angular values can be specified to rotate the camera.
		"""
		self._edit(rotation=value)
	#----------------------------------------------------------------------
	rotation = property(fget=get_rotation,fset=set_rotation)

	#----------------------------------------------------------------------
	def get_shakeEnabled(self):
		"""Toggles the effect of the horizontal and vertical shake
		attributes.
		"""
		return self._query(shakeEnabled=True)
	#----------------------------------------------------------------------
	def set_shakeEnabled(self,value):
		"""Toggles the effect of the horizontal and vertical shake
		attributes.
		"""
		self._edit(shakeEnabled=value)
	#----------------------------------------------------------------------
	shakeEnabled = property(fget=get_shakeEnabled,fset=set_shakeEnabled)

	#----------------------------------------------------------------------
	def get_shakeOverscan(self):
		"""Controls the amount of overscan in the output rendered image.
		For use when adding film-based camera shake.  Acts as a multiplier
		to the film aperture on the camera.
		"""
		return self._query(shakeOverscan=True)
	#----------------------------------------------------------------------
	def set_shakeOverscan(self,value):
		"""Controls the amount of overscan in the output rendered image.
		For use when adding film-based camera shake.  Acts as a multiplier
		to the film aperture on the camera.
		"""
		self._edit(shakeOverscan=value)
	#----------------------------------------------------------------------
	shakeOverscan = property(fget=get_shakeOverscan,fset=set_shakeOverscan)

	#----------------------------------------------------------------------
	def get_shakeOverscanEnabled(self):
		"""Toggles the effect of the shake overscan attribute.
		"""
		return self._query(shakeOverscanEnabled=True)
	#----------------------------------------------------------------------
	def set_shakeOverscanEnabled(self,value):
		"""Toggles the effect of the shake overscan attribute.
		"""
		self._edit(shakeOverscanEnabled=value)
	#----------------------------------------------------------------------
	shakeOverscanEnabled = property(fget=get_shakeOverscanEnabled,fset=set_shakeOverscanEnabled)

	#----------------------------------------------------------------------
	def get_shutterAngle(self):
		"""Specify the shutter angle (degrees).
		"""
		return self._query(shutterAngle=True)
	#----------------------------------------------------------------------
	def set_shutterAngle(self,value):
		"""Specify the shutter angle (degrees).
		"""
		self._edit(shutterAngle=value)
	#----------------------------------------------------------------------
	shutterAngle = property(fget=get_shutterAngle,fset=set_shutterAngle)

	#----------------------------------------------------------------------
	def get_startupCamera(self):
		"""A startup camera is marked undeletable and implicit. This flag
		can be used to set or query the startup state of a
		camera. There must always be at least one startup camera.
		"""
		return self._query(startupCamera=True)
	#----------------------------------------------------------------------
	def set_startupCamera(self,value):
		"""A startup camera is marked undeletable and implicit. This flag
		can be used to set or query the startup state of a
		camera. There must always be at least one startup camera.
		"""
		self._edit(startupCamera=value)
	#----------------------------------------------------------------------
	startupCamera = property(fget=get_startupCamera,fset=set_startupCamera)

	#----------------------------------------------------------------------
	def get_stereoHorizontalImageTranslate(self):
		"""A film-back offset for use in stereo camera rigs.
		"""
		return self._query(stereoHorizontalImageTranslate=True)
	#----------------------------------------------------------------------
	def set_stereoHorizontalImageTranslate(self,value):
		"""A film-back offset for use in stereo camera rigs.
		"""
		self._edit(stereoHorizontalImageTranslate=value)
	#----------------------------------------------------------------------
	stereoHorizontalImageTranslate = property(fget=get_stereoHorizontalImageTranslate,fset=set_stereoHorizontalImageTranslate)

	#----------------------------------------------------------------------
	def get_stereoHorizontalImageTranslateEnabled(self):
		"""Toggles the effect of the stereo HIT attribute.
		"""
		return self._query(stereoHorizontalImageTranslateEnabled=True)
	#----------------------------------------------------------------------
	def set_stereoHorizontalImageTranslateEnabled(self,value):
		"""Toggles the effect of the stereo HIT attribute.
		"""
		self._edit(stereoHorizontalImageTranslateEnabled=value)
	#----------------------------------------------------------------------
	stereoHorizontalImageTranslateEnabled = property(fget=get_stereoHorizontalImageTranslateEnabled,fset=set_stereoHorizontalImageTranslateEnabled)

	#----------------------------------------------------------------------
	def get_verticalFieldOfView(self):
		"""Set the vertical field of view.
		"""
		return self._query(verticalFieldOfView=True)
	#----------------------------------------------------------------------
	def set_verticalFieldOfView(self,value):
		"""Set the vertical field of view.
		"""
		self._edit(verticalFieldOfView=value)
	#----------------------------------------------------------------------
	verticalFieldOfView = property(fget=get_verticalFieldOfView,fset=set_verticalFieldOfView)

	#----------------------------------------------------------------------
	def get_verticalFilmAperture(self):
		"""The vertical height of the camera's film plane. This double
		precision parameter is always specified in inches.
		"""
		return self._query(verticalFilmAperture=True)
	#----------------------------------------------------------------------
	def set_verticalFilmAperture(self,value):
		"""The vertical height of the camera's film plane. This double
		precision parameter is always specified in inches.
		"""
		self._edit(verticalFilmAperture=value)
	#----------------------------------------------------------------------
	verticalFilmAperture = property(fget=get_verticalFilmAperture,fset=set_verticalFilmAperture)

	#----------------------------------------------------------------------
	def get_verticalFilmOffset(self):
		"""Vertical offset from the center of the film back. This double
		precision parameter is always specified in inches.
		"""
		return self._query(verticalFilmOffset=True)
	#----------------------------------------------------------------------
	def set_verticalFilmOffset(self,value):
		"""Vertical offset from the center of the film back. This double
		precision parameter is always specified in inches.
		"""
		self._edit(verticalFilmOffset=value)
	#----------------------------------------------------------------------
	verticalFilmOffset = property(fget=get_verticalFilmOffset,fset=set_verticalFilmOffset)

	#----------------------------------------------------------------------
	def get_verticalLock(self):
		"""Lock the size of the vertical film aperture.
		"""
		return self._query(verticalLock=True)
	#----------------------------------------------------------------------
	def set_verticalLock(self,value):
		"""Lock the size of the vertical film aperture.
		"""
		self._edit(verticalLock=value)
	#----------------------------------------------------------------------
	verticalLock = property(fget=get_verticalLock,fset=set_verticalLock)

	#----------------------------------------------------------------------
	def get_verticalPan(self):
		"""Vertical 2D camera pan (inches)
		"""
		return self._query(verticalPan=True)
	#----------------------------------------------------------------------
	def set_verticalPan(self,value):
		"""Vertical 2D camera pan (inches)
		"""
		self._edit(verticalPan=value)
	#----------------------------------------------------------------------
	verticalPan = property(fget=get_verticalPan,fset=set_verticalPan)

	#----------------------------------------------------------------------
	def get_verticalRollPivot(self):
		"""Vertical pivot point used for rotating the film back. This
		double precision parameter corresponds to the normalized viewport.
		This value is used to compute the film roll matrix, which is a
		component of the post projection matrix.
		"""
		return self._query(verticalRollPivot=True)
	#----------------------------------------------------------------------
	def set_verticalRollPivot(self,value):
		"""Vertical pivot point used for rotating the film back. This
		double precision parameter corresponds to the normalized viewport.
		This value is used to compute the film roll matrix, which is a
		component of the post projection matrix.
		"""
		self._edit(verticalRollPivot=value)
	#----------------------------------------------------------------------
	verticalRollPivot = property(fget=get_verticalRollPivot,fset=set_verticalRollPivot)

	#----------------------------------------------------------------------
	def get_verticalShake(self):
		"""Vertical offset from the center of the film back.  See horizontal
		shake attribute description.  This is toggled by the shake enabled
		attribute.
		"""
		return self._query(verticalShake=True)
	#----------------------------------------------------------------------
	def set_verticalShake(self,value):
		"""Vertical offset from the center of the film back.  See horizontal
		shake attribute description.  This is toggled by the shake enabled
		attribute.
		"""
		self._edit(verticalShake=value)
	#----------------------------------------------------------------------
	verticalShake = property(fget=get_verticalShake,fset=set_verticalShake)

	#----------------------------------------------------------------------
	def get_worldCenterOfInterest(self):
		"""Camera world center of interest point.
		"""
		return self._query(worldCenterOfInterest=True)
	#----------------------------------------------------------------------
	def set_worldCenterOfInterest(self,value):
		"""Camera world center of interest point.
		"""
		self._edit(worldCenterOfInterest=value)
	#----------------------------------------------------------------------
	worldCenterOfInterest = property(fget=get_worldCenterOfInterest,fset=set_worldCenterOfInterest)

	#----------------------------------------------------------------------
	def get_worldUp(self):
		"""Camera world up vector.
		"""
		return self._query(worldUp=True)
	#----------------------------------------------------------------------
	def set_worldUp(self,value):
		"""Camera world up vector.
		"""
		self._edit(worldUp=value)
	#----------------------------------------------------------------------
	worldUp = property(fget=get_worldUp,fset=set_worldUp)

	#----------------------------------------------------------------------
	def get_zoom(self):
		"""The percent over the film viewable frustum to display
		"""
		return self._query(zoom=True)
	#----------------------------------------------------------------------
	def set_zoom(self,value):
		"""The percent over the film viewable frustum to display
		"""
		self._edit(zoom=value)
	#----------------------------------------------------------------------
	zoom = property(fget=get_zoom,fset=set_zoom)