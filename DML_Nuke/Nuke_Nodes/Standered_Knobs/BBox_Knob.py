import nuke
from .Array_Knob import Array_Knob

################################################################################
class BBox_Knob(Array_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "BBox_Knob"
	#----------------------------------------------------------------------
	def fromDict(self,*args,**kwargs):
		"""
			self.fromDict(box) -> None

			Set the bounding box from the given box.

			@param box: Dictionary containing the x, y, r and t keys.

			@return: None

		"""
		return self.nuke_object.fromDict(*args,**kwargs)
	#----------------------------------------------------------------------
	def names(self,i):
		"""
			Return name for dimension 'i'

		"""
		return self.nuke_object.names(i)
	#----------------------------------------------------------------------
	def r(self):
		"""
			Return value for R extent.

		"""
		return self.nuke_object.r()
	#----------------------------------------------------------------------
	def setR(self,val):
		"""
			Set value for R extent.

		"""
		return self.nuke_object.setR(val)
	#----------------------------------------------------------------------
	def setT(self,val):
		"""
			Set value for T extent.

		"""
		return self.nuke_object.setT(val)
	#----------------------------------------------------------------------
	def setX(self,val):
		"""
			Set value for X position.

		"""
		return self.nuke_object.setX(val)
	#----------------------------------------------------------------------
	def setY(self,val):
		"""
			Set value for Y position.

		"""
		return self.nuke_object.setY(val)
	#----------------------------------------------------------------------
	def t(self):
		"""
			Return value for T extent.

		"""
		return self.nuke_object.t()
	#----------------------------------------------------------------------
	def toDict(self):
		"""
			self.toDict() -> dict.

			Returns the bounding box as a dict with x, y, r, and t keys.

			@return: dict with x, y, r and t keys

		"""
		return self.nuke_object.toDict()
	#----------------------------------------------------------------------
	def x(self):
		"""
			Return value for X position.

		"""
		return self.nuke_object.x()
	#----------------------------------------------------------------------
	def y(self):
		"""
			Return value for Y position.

		"""
		return self.nuke_object.y()

