import nuke
from .Enumeration_Knob import Enumeration_Knob

################################################################################
class Pulldown_Knob(Enumeration_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "Pulldown_Knob"
	#----------------------------------------------------------------------
	def commands(self):
		"""
			commands(n) -> string

			Return command n. The argument n is an integer and in the range of 0 and numValues.

		"""
		return self.nuke_object.commands()
	#----------------------------------------------------------------------
	def itemName(self):
		"""
			itemName(n) -> string

			Return name of item n. The argument n is an integer and in the range of 0 and numValues.

		"""
		return self.nuke_object.itemName()
