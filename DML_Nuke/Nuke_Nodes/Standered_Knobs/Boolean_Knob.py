import nuke
from .Array_Knob import Array_Knob

################################################################################
class Boolean_Knob(Array_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "Boolean_Knob"