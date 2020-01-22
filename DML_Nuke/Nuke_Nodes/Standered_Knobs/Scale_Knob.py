import nuke
from .Array_Knob import Array_Knob

################################################################################
class Scale_Knob(Array_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "Scale_Knob"
	#----------------------------------------------------------------------
	def value(self):
		"""value(n, oc) -> float  Return value for dimension n. The optional argument oc is an OutputContext."""
		return self.nuke_object.value()
	#----------------------------------------------------------------------
	def names(self,n):
		"""names(n) -> string  Return name for dimension n. The argument n is an integer."""
		return self.nuke_object.names(n)
	#----------------------------------------------------------------------
	def y(self,oc):
		"""y(oc) -> float  Return value for y. The optional oc argument is an OutputContext"""
		return self.nuke_object.y(oc)
	#----------------------------------------------------------------------
	def x(self,oc):
		"""x(oc) -> float  Return value for x. The optional oc argument is an OutputContext"""
		return self.nuke_object.x(oc)
	#----------------------------------------------------------------------
	def z(self,oc):
		"""z(oc) -> float  Return value for z. The optional oc argument is an OutputContext"""
		return self.nuke_object.z(oc)
