import nuke
from ..Abstract_Nodes import Knob

################################################################################
class Format_Knob(Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "Format_Knob"
	#----------------------------------------------------------------------
	def setValue(self,format):
		"""setValue(format) -> True if succeeded, False otherwise.  Set value of knob to format (either a Format object or a name of a format, e.g. "NTSC")."""
		return self.nuke_object.setValue(format)
	#----------------------------------------------------------------------
	def fromScript(self,s):
		"""fromScript(s) -> True if succeeded, False otherwise.  Initialise from script s."""
		return self.nuke_object.fromScript(s)
	#----------------------------------------------------------------------
	def value(self):
		"""value() -> Format.  Return value of knob."""
		return self.nuke_object.value()
	#----------------------------------------------------------------------
	def actualValue(self):
		"""actualValue() -> Format.  Return value of knob."""
		return self.nuke_object.actualValue()
	#----------------------------------------------------------------------
	def toScript(self):
		"""toScript(quote, context=current) -> string.  Return the value of the knob in script syntax. Pass True for quote to return results quoted in {}. Pass None for context to get results for all views and key times (as stored in a .nk file)."""
		return self.nuke_object.toScript()
	#----------------------------------------------------------------------
	def notDefault(self):
		"""notDefault() -> True if set to its default value, False otherwise."""
		return self.nuke_object.notDefault()
	#----------------------------------------------------------------------
	def name(self):
		"""name() -> string.  Return name of knob."""
		return self.nuke_object.name()
