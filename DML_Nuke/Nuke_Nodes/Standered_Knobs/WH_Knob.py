import nuke
from .Array_Knob import Array_Knob

################################################################################
class WH_Knob(Array_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "WH_Knob"
	#----------------------------------------------------------------------
	def y_at(self,t):
		"""Return value for Y position at time 't'."""
		return self.nuke_object.y_at(t)
	#----------------------------------------------------------------------
	def names(self):
		"""Return name for dimension 'i'."""
		return self.nuke_object.names()
	#----------------------------------------------------------------------
	def y(self):
		"""Return value for Y position."""
		return self.nuke_object.y()
	#----------------------------------------------------------------------
	def x(self):
		"""Return value for X position."""
		return self.nuke_object.x()
	#----------------------------------------------------------------------
	def x_at(self,t):
		"""Return value for X position at time 't'."""
		return self.nuke_object.x_at(t)
