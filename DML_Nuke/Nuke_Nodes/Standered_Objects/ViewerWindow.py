import nuke
from ..Base_Nodes import DML_Nuke_Object

################################################################################
class ViewerWindow(DML_Nuke_Object):
	#----------------------------------------------------------------------
	def node(self):
		"""self.node() -> Node. Returns the Viewer node currently associated with this window. @return: Node."""
		return self.nuke_object.node()
	#----------------------------------------------------------------------
	def activeInput(self,secondary=False):
		"""self.activeInput(secondary=False) -> int Returns the currently active input of the viewer - i. e. the one with its image in the output window. @param secondary: True to return the index of the active secondary (wipe) input, or False (the default) to return the primary input. @return: int: The currently active input of the viewer, starting with 0 for the first, or None if no input is active."""
		return self.nuke_object.activeInput(secondary=False)
	#----------------------------------------------------------------------
	def play(self):
		"""Play forward (1) or reverse (0)."""
		return self.nuke_object.play()
	#----------------------------------------------------------------------
	def previousView(self):
		"""self.previousView() -> switch to previous view in settings Views list. """
		return self.nuke_object.previousView()
	#----------------------------------------------------------------------
	def nextView(self):
		"""self.nextView() -> switch to next view in settings Views list. """
		return self.nuke_object.nextView()
	#----------------------------------------------------------------------
	def getGLCameraMatrix(self):
		"""self.getGLCameraMatrix() -> Matrix4 Return the world transformations of the current GL viewer camera. @return: Matrix4: GL camera world transformation."""
		return self.nuke_object.getGLCameraMatrix()
	#----------------------------------------------------------------------
	def getGeometryNodes(self):
		"""self.getGeometry() -> None Returns the a list of geometry nodes attached with this viewer @return: Nodes: a list of the geometry nodes."""
		return self.nuke_object.getGeometryNodes()
	#----------------------------------------------------------------------
	def stop(self):
		"""Stop playing."""
		return self.nuke_object.stop()
	#----------------------------------------------------------------------
	def activateInput(self):
		"""self.activateInput(input, secondary=False) -> None Set the given viewer input to be active - i. e. show its image in the output window. @param input: The viewer input number, starting with 0 for the first.  If the input is not connected, a ValueError exception is raised. @param secondary: True if the input should be connected as the secondary (wipe) input, or False to connect it as the primary input (the default). @return: None"""
		return self.nuke_object.activateInput()
	#----------------------------------------------------------------------
	def setView(self,s):
		"""self.setView(s) -> set 'current' multi-view view to 's'. """
		return self.nuke_object.setView(s)
	#----------------------------------------------------------------------
	def frameControl(self,i):
		"""self.frameControl(i) -> True.  i is an integer indicating viewer frame control 'button' to execute:     -6 go to start    -5 play reverse    -4 go to previous keyframe    -3 step back by increment    -2 go back previous keyframe or increment, whichever is closer    -1 step back one frame      0 stop     +1 step forward one frame    +2 go to next keyframe or increment, whichever is closer    +3 step forward by increment    +4 go to next keyframe    +5 play forward    +6 go to end"""
		return self.nuke_object.frameControl(i)
	#----------------------------------------------------------------------
	def view(self):
		"""self.view() -> string name of 'current' multi-view view. """
		return self.nuke_object.view()
