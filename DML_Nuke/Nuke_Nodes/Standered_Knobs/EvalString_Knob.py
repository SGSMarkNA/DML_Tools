import nuke
from .String_Knob import String_Knob

################################################################################
class EvalString_Knob(String_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "EvalString_Knob"
	#----------------------------------------------------------------------
	def evaluate(self):
		"""self.evaluate() -> String. Evaluate the string, performing substitutions. @return: String."""
		return self.nuke_object.evaluate()