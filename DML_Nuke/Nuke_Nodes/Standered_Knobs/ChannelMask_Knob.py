import nuke
from .Channel_Knob import Channel_Knob

################################################################################
class ChannelMask_Knob(Channel_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "ChannelMask_Knob"