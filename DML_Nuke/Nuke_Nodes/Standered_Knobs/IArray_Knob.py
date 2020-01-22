import nuke
from .Array_Knob import Array_Knob

################################################################################
class IArray_Knob(Array_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "IArray_Knob"
	#----------------------------------------------------------------------
	def value(self):
		"""Return value of the array at position (x, y)."""
		return self.nuke_object.value()
	#----------------------------------------------------------------------
	def height(self):
		"""Return height of the array."""
		return self.nuke_object.height()
	#----------------------------------------------------------------------
	def width(self):
		"""Return width of the array."""
		return self.nuke_object.width()
	#----------------------------------------------------------------------
	def dimensions(self):
		"""Return number of dimensions."""
		return self.nuke_object.dimensions()
