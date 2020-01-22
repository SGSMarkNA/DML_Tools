import nuke
from ..Abstract_Nodes import Knob

################################################################################
class Password_Knob(Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "Password_Knob"
	#----------------------------------------------------------------------
	def setValue(self):
		"""self.setValue(val, view='default') -> None  Set value of knob. @param val: The new value. @param view: Optional parameter specifying which view to set the value for. If omitted, the value will be set for the default view. @return: None"""
		return self.nuke_object.setValue()
	#----------------------------------------------------------------------
	def value(self):
		"""self.value() -> str  Get the value of this knob as a string. @return: String value."""
		return self.nuke_object.value()
	#----------------------------------------------------------------------
	def getText(self):
		"""self.getText() -> string  Return text associated with knob."""
		return self.nuke_object.getText()
