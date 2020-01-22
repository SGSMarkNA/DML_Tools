import nuke
from .Array_Knob import Array_Knob

################################################################################
class Keyer_Knob(Array_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "Keyer_Knob"
	#----------------------------------------------------------------------
	def highTol(self):
		""""""
		return self.nuke_object.highTol()
	#----------------------------------------------------------------------
	def lowSoft(self):
		""""""
		return self.nuke_object.lowSoft()
	#----------------------------------------------------------------------
	def lowTol(self):
		""""""
		return self.nuke_object.lowTol()
	#----------------------------------------------------------------------
	def value(self):
		"""self.value(outputCtx, n) -> float  Get the value of argument n. @param outputCtx: The OutputContext to evaluate the argument in. @param n: The index of the argument to get the value of. @return: The value of argument n."""
		return self.nuke_object.value()
	#----------------------------------------------------------------------
	def names(self,n):
		"""self.names(n) -> string  @param n: The index of the name to return. @return: The name at position n."""
		return self.nuke_object.names(n)
	#----------------------------------------------------------------------
	def highSoft(self):
		""""""
		return self.nuke_object.highSoft()
