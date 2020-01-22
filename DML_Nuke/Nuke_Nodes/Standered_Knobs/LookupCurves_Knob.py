import nuke
from ..Abstract_Nodes import Knob

################################################################################
class LookupCurves_Knob(Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "LookupCurves_Knob"
	#----------------------------------------------------------------------
	def delCurve(self,curve):
		"""self.delCurve(curve) -> None Deletes a curve. @param curve: The name of the animation curve. @return: None"""
		return self.nuke_object.delCurve(curve)
	#----------------------------------------------------------------------
	def editCurve(self):
		"""self.editCurve(curve, expr=None) -> None Edits an existing curve. @param curve: The name of an animation curve. @param expr: The new expression for the curve. @return: None"""
		return self.nuke_object.editCurve()
	#----------------------------------------------------------------------
	def addCurve(self):
		"""self.addCurve(curve, expr=None) -> None Adds a curve. @param curve: The name of an animation curve, or an AnimationCurve instance. @param expr: Optional parameter giving an expression for the curve. @return: None"""
		return self.nuke_object.addCurve()
