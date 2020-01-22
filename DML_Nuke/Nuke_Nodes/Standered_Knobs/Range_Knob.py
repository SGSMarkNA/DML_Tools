import nuke
from .Array_Knob import Array_Knob

################################################################################
class Range_Knob(Array_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "Range_Knob"