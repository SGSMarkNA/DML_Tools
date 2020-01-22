import nuke
from ..Abstract_Nodes import Knob

################################################################################
class Channel_Knob(Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "Channel_Knob"
	#----------------------------------------------------------------------
	def inputNumber(self):
		"""self.inputNumber() -> int"""
		return self.nuke_object.inputNumber()
	#----------------------------------------------------------------------
	def enableChannel(self,name, b):
		"""self.enableChannel(name, b) -> None  Enable or disable a channel. @param name: The name of the channel. @param b: True to enable the channel, False to disable it. @return: None"""
		return self.nuke_object.enableChannel(name, b)
	#----------------------------------------------------------------------
	def layerSelector(self):
		"""self.layerSelector() -> bool"""
		return self.nuke_object.layerSelector()
	#----------------------------------------------------------------------
	def setEnable(self,name):
		"""self.setEnable(name) -> None  Enable a channel. @param name: The name of the channel to enable. @return: None"""
		return self.nuke_object.setEnable(name)
	#----------------------------------------------------------------------
	def value(self):
		"""self.value() -> str Get the name of the selected channel. @return: The name of the channel as a string."""
		return self.nuke_object.value()
	#----------------------------------------------------------------------
	def checkMarks(self):
		"""self.checkMarks() -> bool"""
		return self.nuke_object.checkMarks()
	#----------------------------------------------------------------------
	def channelSelector(self):
		"""self.channelSelector() -> bool"""
		return self.nuke_object.channelSelector()
	#----------------------------------------------------------------------
	def depth(self):
		"""self.depth() -> int  Get the channel depth. @return: The depth of the channel as an int."""
		return self.nuke_object.depth()
	#----------------------------------------------------------------------
	def setValue(self,name):
		"""self.setValue(name) -> None Set the selected channel using the channel name. @param name: The name of the new channel as a string. @return: None @raise ValueError exception if the channel doesn't exist."""
		return self.nuke_object.setValue(name)
	#----------------------------------------------------------------------
	def setInput(self,num):
		"""self.setInput(num) -> None Set the input number for this knob.@param num: The number of the new input. @return: None"""
		return self.nuke_object.setInput(num)
	#----------------------------------------------------------------------
	def inputKnob(self):
		"""self.inputKnob() -> bool"""
		return self.nuke_object.inputKnob()
	#----------------------------------------------------------------------
	def isChannelEnabled(self,name):
		"""self.isChannelEnabled(name) -> bool  Test if a channel is enabled. @param name: The name of the channel.@return: True if the channel is enabled, False otherwise."""
		return self.nuke_object.isChannelEnabled(name)
