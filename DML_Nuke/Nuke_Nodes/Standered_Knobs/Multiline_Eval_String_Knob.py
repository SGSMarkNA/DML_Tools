import nuke
from .EvalString_Knob import EvalString_Knob

################################################################################
class Multiline_Eval_String_Knob(EvalString_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "Multiline_Eval_String_Knob"