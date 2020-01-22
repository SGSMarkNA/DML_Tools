import nuke
from ..Abstract_Nodes import Knob

################################################################################
class MultiView_Knob(Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "MultiView_Knob"
	#----------------------------------------------------------------------
	def toScriptPrefix(self):
		""""""
		return self.nuke_object.toScriptPrefix()
	#----------------------------------------------------------------------
	def setValue(self,s):
		"""fromScript(s) -> True if succeeded, False otherwise.  Initialise from script s."""
		return self.nuke_object.setValue(s)
	#----------------------------------------------------------------------
	def fromScript(self,s):
		"""fromScript(s) -> True if succeeded, False otherwise.  Initialise from script s."""
		return self.nuke_object.fromScript(s)
	#----------------------------------------------------------------------
	def value(self):
		"""toScript(quote, context=current) -> string.  Return the value of the knob in script syntax. Pass True for quote to return results quoted in {}. Pass None for context to get results for all views and key times (as stored in a .nk file)."""
		return self.nuke_object.value()
	#----------------------------------------------------------------------
	def toScriptPrefixUserKnob(self):
		""""""
		return self.nuke_object.toScriptPrefixUserKnob()
	#----------------------------------------------------------------------
	def toScript(self):
		"""toScript(quote, context=current) -> string.  Return the value of the knob in script syntax. Pass True for quote to return results quoted in {}. Pass None for context to get results for all views and key times (as stored in a .nk file)."""
		return self.nuke_object.toScript()
	#----------------------------------------------------------------------
	def notDefault(self):
		"""notDefault() -> True if set to its default value, False otherwise."""
		return self.nuke_object.notDefault()
