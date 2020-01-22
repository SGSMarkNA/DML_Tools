import nuke
from ..Abstract_Nodes import Knob

################################################################################
class Help_Knob(Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "Help_Knob"