import nuke
from .Unsigned_Knob import Unsigned_Knob

################################################################################
class ColorChip_Knob(Unsigned_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "ColorChip_Knob"