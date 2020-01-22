import nuke
from .AColor_Knob import AColor_Knob

################################################################################
class Eyedropper_Knob(AColor_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "Eyedropper_Knob"