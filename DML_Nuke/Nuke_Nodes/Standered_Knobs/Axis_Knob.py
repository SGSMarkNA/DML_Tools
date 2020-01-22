import nuke
from ..Abstract_Nodes import Knob

################################################################################
class Axis_Knob(Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "Axis_Knob"
	#----------------------------------------------------------------------
	def uniformScale(self):
		"""self.uniformScale() -> Double_Knob  Return uniform scale knob."""
		return self.nuke_object.uniformScale()
	#----------------------------------------------------------------------
	def rotate(self):
		"""self.rotate() -> XYZ_Knob  Return rotation knob."""
		return self.nuke_object.rotate()
	#----------------------------------------------------------------------
	def skew(self):
		"""self.skew() -> XYZ_Knob  Return skew knob."""
		return self.nuke_object.skew()
	#----------------------------------------------------------------------
	def value(self):
		"""self.value() -> _nukemath.Matrix4 Return the transform matrix formed by combining the input knob values for translate, rotate, scale, skew and pivot."""
		return self.nuke_object.value()
	#----------------------------------------------------------------------
	def scale(self):
		"""self.scale() -> Scale_Knob  Return scale knob."""
		return self.nuke_object.scale()
	#----------------------------------------------------------------------
	def pivot(self):
		"""self.pivot() -> XYZ_Knob  Return pivot knob."""
		return self.nuke_object.pivot()
	#----------------------------------------------------------------------
	def translate(self):
		"""self.translate() -> XYZ_Knob  Return translation knob."""
		return self.nuke_object.translate()
