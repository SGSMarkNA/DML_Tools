import nuke
from .Script_Knob import Script_Knob

################################################################################
class PythonCustomKnob(Script_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "PythonCustomKnob"
	def getObject(self):
		"""Returns the custom knob object as created in the by the 'command' argument to the PyCuston_Knob constructor."""
		return self.nuke_object.getObject()