
import nuke
from .Group import Group

################################################################################
class Root(Group):
	NODE_TYPE_RELATION  = "Root"
	#----------------------------------------------------------------------
	def addView(self,*args,**kwargs):
		"""
			self.addView(name, color) -> None.

			Add view.

			@param name: String - name of view.

			@param color: Optional. String in the format #RGB, #RRGGBB, #RRRGGGBBB, #RRRRGGGGBBBB or a name from the list of colors defined in the list of SVG color keyword names.

			@return: None.

		"""
		return self.nuke_object.addView(*args,**kwargs)
	#----------------------------------------------------------------------
	def deleteView(self,*args,**kwargs):
		"""
			self.deleteView(s) -> None.

			Delete view.

			@param s: Name of view.

			@return: None.

		"""
		return self.nuke_object.deleteView(*args,**kwargs)
	#----------------------------------------------------------------------
	def fps(self):
		"""
			self.fps() -> integer

			Return the FPS rounded to an int. This is deprecated. Please use real_fps().

		"""
		return self.nuke_object.fps()
	#----------------------------------------------------------------------
	def getOCIOColorspaceFamily(self,*args,**kwargs):
		"""
			nuke.root.getOCIOColorspaceFamily(colorspace) -> Family of colorspace

			Gets the name of the family to which the specified colorspace belongs,

			for the root node's current OCIO config.

			@param colorspace: Colorspace name.

			@return: Family name, may be an empty string.

		"""
		return self.nuke_object.getOCIOColorspaceFamily(*args,**kwargs)
	#----------------------------------------------------------------------
	def getOCIOColorspaceFromViewTransform(self,*args,**kwargs):
		"""
			nuke.root.getOCIOColorspaceFromViewTransform(display, view) -> Colorspace name

			Gets the name of the colorspace to which the specified display and view names are mapped

			for the root node's current OCIO config.

			@param display: Display name.

			@param view: View name.

			@return: The corresponding colorspace name.

		"""
		return self.nuke_object.getOCIOColorspaceFromViewTransform(*args,**kwargs)
	#----------------------------------------------------------------------
	def layers(self):
		"""
			nuke.Root.layers() -> Layer list.

			Class method.

			@return: Layer list.

		"""
		return self.nuke_object.layers()
	#----------------------------------------------------------------------
	def mergeFrameRange(self,*args,**kwargs):
		"""
			self.mergeFrameRange(a, b) -> None.

			Merge frame range.

			@param a: Low-end of interval range.

			@param b: High-end of interval range.

			@return: None.

		"""
		return self.nuke_object.mergeFrameRange(*args,**kwargs)
	#----------------------------------------------------------------------
	def modified(self):
		"""
			self.modified() -> True if modified, False otherwise.

			Get or set the 'modified' flag in a script

			@return: True if modified, False otherwise.

		"""
		return self.nuke_object.modified()
	#----------------------------------------------------------------------
	def realFps(self):
		"""
			self.realFps() -> float

			The global frames per second setting.

		"""
		return self.nuke_object.realFps()
	#----------------------------------------------------------------------
	def setFrame(self,*args,**kwargs):
		"""
			self.setFrame(n) -> None.

			Set frame.

			@param n: Frame number.

			@return: None.

		"""
		return self.nuke_object.setFrame(*args,**kwargs)
	#----------------------------------------------------------------------
	def setModified(self,*args,**kwargs):
		"""
			self.setModified(b) -> None.

			Set the 'modified' flag in a script.

			Setting the value will turn the indicator in the title bar on/off and will start or stop the autosave timeout.

			@param b: Boolean convertible object.

			@return: None.

		"""
		return self.nuke_object.setModified(*args,**kwargs)
	#----------------------------------------------------------------------
	def setProxy(self,*args,**kwargs):
		"""
			self.setProxy(b) -> None.

			Set proxy.

			@param b: Boolean convertible object.

			@return: None.

		"""
		return self.nuke_object.setProxy(*args,**kwargs)
	#----------------------------------------------------------------------
	def setView(self,*args,**kwargs):
		"""
			self.setView(s) -> None.

			Set view.

			@param s: Name of view.

			@return: None.

		"""
		return self.nuke_object.setView(*args,**kwargs)
