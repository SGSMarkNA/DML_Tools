import nuke
from ..Abstract_Nodes import Knob

################################################################################
class Text_Knob(Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "Text_Knob"