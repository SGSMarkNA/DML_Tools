import nuke
from .Enumeration_Knob import Enumeration_Knob

################################################################################
class Bitmask_Knob(Enumeration_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "Bitmask_Knob"