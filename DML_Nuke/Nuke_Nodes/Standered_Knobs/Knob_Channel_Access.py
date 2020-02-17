

if False:
	from ..Abstract_Nodes import Knob 


########################################################################
class Knob_Channel(object):
	""""""
    #----------------------------------------------------------------------
	def __init__(self,knob,channelIndex):
		"""Constructor"""
		self.knob = knob
		self.channel = channelIndex
		if False:
			isinstance(self.knob,Knob)
	#----------------------------------------------------------------------
	def get_Value(self):
		""""""	
		return self.knob.getValue(self.channel)
	#----------------------------------------------------------------------
	def set_Value(self,val):
		""""""
		self.knob.setValue(val,channel=self.channel)
	#----------------------------------------------------------------------
	def set_Expression(self,expression):
		""""""
		self.knob.setExpression(expression,channel=self.channel)
	#----------------------------------------------------------------------
	def has_Expression(self):
		""""""
		return self.knob.hasExpression(index=self.channel)
	
	value = property(get_Value,set_Value)