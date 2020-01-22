import nuke
from .Script_Knob import Script_Knob

################################################################################
class PyScript_Knob(Script_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "PyScript_Knob"