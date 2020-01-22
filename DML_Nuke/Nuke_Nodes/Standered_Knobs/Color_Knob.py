import nuke
from .Array_Knob import Array_Knob

################################################################################
class Color_Knob(Array_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "Color_Knob"
	#----------------------------------------------------------------------
	def inputNumber(self):
		"""inputNumber() -> int  Return input number."""
		return self.nuke_object.inputNumber()
	#----------------------------------------------------------------------
	def names(self,n):
		"""names(n) -> string  Return name for dimension n. The argument n is an integer."""
		return self.nuke_object.names(n)