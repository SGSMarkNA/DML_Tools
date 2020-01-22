import nuke
from .Enumeration_Knob import Enumeration_Knob

################################################################################
class CascadingEnumeration_Knob(Enumeration_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "CascadingEnumeration_Knob"