import nuke
from ..Abstract_Nodes import Knob

################################################################################
class Histogram_Knob(Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "Histogram_Knob"