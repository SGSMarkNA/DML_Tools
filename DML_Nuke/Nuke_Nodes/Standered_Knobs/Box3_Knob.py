import nuke
from .Array_Knob import Array_Knob

################################################################################
class Box3_Knob(Array_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "Box3_Knob"
	#----------------------------------------------------------------------
	def f(self):
		"""
			Return value for F extent. F (far) is the maximum Z extent of the box.
		"""
		return self.nuke_object.f()
	#----------------------------------------------------------------------
	def n(self):
		"""
			Return value for N position. N (near) is the minimum Z extent of the box.

		"""
		return self.nuke_object.n()
	#----------------------------------------------------------------------
	def names(self):
		"""
			Return name for dimension 'i'

		"""
		return self.nuke_object.names()
	#----------------------------------------------------------------------
	def r(self):
		"""
			Return value for R extent. R (right) is the right extent of the box.

		"""
		return self.nuke_object.r()
	#----------------------------------------------------------------------
	def setF(self,val):
		"""
			Set value for F extent. F (far) is the maximum Z extent of the box.

		"""
		return self.nuke_object.setF(val)
	#----------------------------------------------------------------------
	def setN(self,val):
		"""
			Set value for N position. N (near) is the minimum Z extent of the box.

		"""
		return self.nuke_object.setN(val)
	#----------------------------------------------------------------------
	def setR(self,val):
		"""
			Set value for R extent. R (right) is the right extent of the box.

		"""
		return self.nuke_object.setR(val)
	#----------------------------------------------------------------------
	def setT(self,val):
		"""
			Set value for T extent. T (top) is the maximum vertical extent of the box.

		"""
		return self.nuke_object.setT(val)
	#----------------------------------------------------------------------
	def setX(self,val):
		"""
			Set value for X position. X is the minimum horizontal extent of the box.

		"""
		return self.nuke_object.setX(val)
	#----------------------------------------------------------------------
	def setY(self,val):
		"""
			Set value for Y position. Y is the minimum vertical extent of the box.

		"""
		return self.nuke_object.setY(val)
	#----------------------------------------------------------------------
	def t(self):
		"""
			Return value for T extent. T (top) is the maximum vertical extent of the box.

		"""
		return self.nuke_object.t()
	#----------------------------------------------------------------------
	def x(self):
		"""
			Return value for X position. X is the minimum horizontal extent of the box.

		"""
		return self.nuke_object.x()
	#----------------------------------------------------------------------
	def y(self):
		"""
			Return value for Y position. Y is the minimum vertical extent of the box.

		"""
		return self.nuke_object.y()
