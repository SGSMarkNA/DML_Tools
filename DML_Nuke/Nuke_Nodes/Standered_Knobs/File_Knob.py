import nuke
from .EvalString_Knob import EvalString_Knob

################################################################################
class File_Knob(EvalString_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "File_Knob"
	#----------------------------------------------------------------------
	def fromUserText(self,s):
		"""self.fromUserText(s) -> None. Assign string to knob, parses frame range off the end and opens file to get set the format. @param s: String to assign. @return: None."""
		return self.nuke_object.fromUserText(s)
	#----------------------------------------------------------------------
	def setValue(self,s):
		"""self.fromScript(s) -> None. Assign string to knob. @param s: String to assign. @return: None."""
		return self.nuke_object.setValue(s)
	#----------------------------------------------------------------------
	def fromScript(self,s):
		"""self.fromScript(s) -> None. Assign string to knob. @param s: String to assign. @return: None."""
		return self.nuke_object.fromScript(s)
	#----------------------------------------------------------------------
	def value(self):
		"""self.getEvaluatedValue() -> String. Returns the string on this knob, will be normalized to technical notation if sequence (%4d). @return: String."""
		return self.nuke_object.value()
	#----------------------------------------------------------------------
	def getValue(self):
		"""self.getEvaluatedValue() -> String. Returns the string on this knob, will be normalized to technical notation if sequence (%4d). @return: String."""
		return self.nuke_object.getValue()
	#----------------------------------------------------------------------
	def getEvaluatedValue(self,oc):
		"""self.getValue(oc) -> String. Returns the string on this knob, will be normalized to technical notation if sequence (%4d). Will also evaluate the string for any tcl expressions @parm oc: the output context to use, if None the knob uiContext will be used. @return: String."""
		return self.nuke_object.getEvaluatedValue(oc)