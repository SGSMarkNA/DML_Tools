import nuke
from ..Abstract_Nodes import Knob

################################################################################
class Link_Knob(Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "Link_Knob"
	#----------------------------------------------------------------------
	def setValue(self):
		"""setValue() -> None  Set value of knob."""
		return self.nuke_object.setValue()
	#----------------------------------------------------------------------
	def getLinkedKnob(self):
		"""getLinkedKnob() -> knob """
		return self.nuke_object.getLinkedKnob()
	#----------------------------------------------------------------------
	def value(self):
		"""value() -> string  Return value of knob."""
		return self.nuke_object.value()
	#----------------------------------------------------------------------
	def getLink(self):
		"""getLink() -> s """
		return self.nuke_object.getLink()
	#----------------------------------------------------------------------
	def setLink(self,s):
		"""setLink(s) -> None """
		return self.nuke_object.setLink(s)
	#----------------------------------------------------------------------
	def makeLink(self):
		"""makeLink(s, t) -> None """
		return self.nuke_object.makeLink()
