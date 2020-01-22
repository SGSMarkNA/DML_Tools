import nuke
from ..Abstract_Nodes import Node

################################################################################
class Viewer(Node):
	NODE_TYPE_RELATION        = "Viewer"
	#----------------------------------------------------------------------
	def capture(self):
		"""
			capture(file) -> None

			Capture the viewer image to a file.  Only jpg files are supported at present.  The image is captured immediately even if the viewer is mid-render.To capture a fully rendered image at a frame or frame range use nuke.render passing in the viewer node you want to capture.When using nuke.render the filename is specified by the 'file' knob on the viewer node.

		"""
		return self.nuke_object.capture()
	#----------------------------------------------------------------------
	def frameCached(self):
		"""
			frameCached(f) -> Bool

			Determine whether frame /f/ is known to be in the memory cache.

		"""
		return self.nuke_object.frameCached()
	#----------------------------------------------------------------------
	def isPlayingOrRecording(self):
		"""
			isPlayingOrRecording() -> Bool 

			@return: Is a recording being made or played?

		"""
		return self.nuke_object.isPlayingOrRecording()
	#----------------------------------------------------------------------
	def playbackRange(self):
		"""
			self.playbackRange() -> FrameRange.

			Return the frame range that's currently set to be played back in the viewer.@return: FrameRange.

		"""
		return self.nuke_object.playbackRange()
	#----------------------------------------------------------------------
	def recordMouse(self):
		"""
			recordMouse() -> Bool

			Start viewer window mouse recording.@return: Recording started?

		"""
		return self.nuke_object.recordMouse()
	#----------------------------------------------------------------------
	def recordMouseStop(self):
		"""
			recordMouseStop()

			Stop viewer window mouse recording.

		"""
		return self.nuke_object.recordMouseStop()
	#----------------------------------------------------------------------
	def replayMouseAsync(self):
		"""
			replayMouseAsync(xmlRecordingFilename) -> Bool

			Start timer based (asynchronous) playback of a viewer window mouse recording.@param: Name of recording xml file to play@return: Replay started?

		"""
		return self.nuke_object.replayMouseAsync()
	#----------------------------------------------------------------------
	def replayMouseSync(self):
		"""
			replayMouseSync(xmlRecordingFilename) -> Bool

			Start direct (synchronous) playback of a viewer window mouse recording.@param: Name of recording xml file to play@return: Replay succeeded?

		"""
		return self.nuke_object.replayMouseSync()
	#----------------------------------------------------------------------
	def roi(self):
		"""
			self.roi() -> dict

			Region of interest set in the viewer in pixel space coordinates.

			Returns None if the Viewer has no window yet.

			@return: Dict with keys x, y, r and t or None.

		"""
		return self.nuke_object.roi()
	#----------------------------------------------------------------------
	def roiEnabled(self):
		"""
			self.roiEnabled() -> bool

			Whether the viewing of just a region of interest is enabled.

			Returns None if the Viewer has no window yet.

			@return: Boolean or None.

		"""
		return self.nuke_object.roiEnabled()
	#----------------------------------------------------------------------
	def sendMouseEvent(self):
		"""
			sendMouseEvent() -> Bool

			Temporary:

			Post a mouse event to the viewer window.

		"""
		return self.nuke_object.sendMouseEvent()
	#----------------------------------------------------------------------
	def setRoi(self,*args,**kwargs):
		"""
			self.setRoi(box) -> None.

			Set the region of interest in pixel space.

			@param box: A dictionary with the x, y, r and t keys.@return: None.

		"""
		return self.nuke_object.setRoi(*args,**kwargs)
	#----------------------------------------------------------------------
	def toggleMouseTrails(self):
		"""
			toggleMouseTrails() -> Bool 

			Toggle mouse trails in the viewer window on/off.@return: Trails now showing?

		"""
		return self.nuke_object.toggleMouseTrails()
	#----------------------------------------------------------------------
	def toggleWaitOnReplayEvents(self):
		"""
			toggleWaitOnEvents() -> Bool 

			Toggle whether asynchronous playback waits on each event.

			Otherwise events will be handled by the next nuke update.@return: Now waiting?

		"""
		return self.nuke_object.toggleWaitOnReplayEvents()
