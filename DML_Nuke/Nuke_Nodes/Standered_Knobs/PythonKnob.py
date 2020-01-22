import nuke
from .String_Knob import String_Knob

################################################################################
class PythonKnob(String_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "PythonKnob"