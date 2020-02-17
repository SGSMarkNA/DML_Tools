import nuke
from .Color_Knob import Color_Knob
from .Knob_Channel_Access import Knob_Channel

########################################################################
class AColor_channels(object):
	""""""

	def __init__(self,knob):
		"""Constructor"""
		self._knob = knob
		self.r  = Knob_Channel(knob, 0)
		self.g = Knob_Channel(knob, 1)
		self.b  = Knob_Channel(knob, 2)
		self.a = Knob_Channel(knob, 3)
################################################################################
class AColor_Knob(Color_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "AColor_Knob"
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		""""""
		super(AColor_Knob,self).__init__(*args,**kwargs)
		self.channels = AColor_channels(self)
	