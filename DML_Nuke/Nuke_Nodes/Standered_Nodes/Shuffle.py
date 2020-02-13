import nuke
from ..Abstract_Nodes import Node
from ..Standered_Knobs import Enumeration_Knob
from functools import partial

########################################################################
class Shuffle_Channels:
	""""""
	RED    = "red"
	GREEN  = "green"
	BLUE   = "blue"
	ALPHA  = "alpha"
	RED2   = "black"
	GREEN2 = "white"
	BLUE2  = "red2"
	ALPHA2 = "green2"
	VALUES = [RED,RED2,GREEN,GREEN2,BLUE,BLUE2,ALPHA,ALPHA2]
	
	#----------------------------------------------------------------------
	@classmethod
	def is_Valid_Value(cls,value):
		""""""
		return value in cls.VALUES
########################################################################
class Shuffle_Channel_Values:
	""""""
	ALPHA  = 'alpha'
	ALPHA2 = 'alpha2'
	BLACK  = 'black'
	BLUE   = 'blue'
	BLUE2  = 'blue2'
	GREEN  = 'green'
	GREEN2 = 'green2'
	OFF    = 'off'
	RED    = 'red'
	RED2   = 'red2'
	WHITE  = 'white'
	VALUES = [ALPHA,ALPHA2,BLACK,BLUE,BLUE2,GREEN,GREEN2,OFF,RED,RED2,WHITE]
	#----------------------------------------------------------------------
	@classmethod
	def is_Valid_Value(cls,value):
		""""""
		return value in cls.VALUES
	



########################################################################
class Shuffle_Channel_Knob(Enumeration_Knob):
	""""""
	KNOB_TYPE_RELATION        = None
	RETURN_OVERIDE_CHECK_TYPE = "Enumeration_Knob"
	#----------------------------------------------------------------------
	@classmethod
	def _overide_Return_Check(cls,knob):
		""""""
		return knob.node().Class() == "Shuffle" and knob.name() in Shuffle_Channels.VALUES 
	#----------------------------------------------------------------------
	def set_To_Red(self):
		""""""
		self.setValue("red")
	#----------------------------------------------------------------------
	def set_To_Red2(self):
		""""""
		self.setValue("red2")
	#----------------------------------------------------------------------
	def set_To_Green(self):
		""""""
		self.setValue("green")
	#----------------------------------------------------------------------
	def set_To_Green2(self):
		""""""
		self.setValue("green2")
	#----------------------------------------------------------------------
	def set_To_Blue(self):
		""""""
		self.setValue("blue")
	#----------------------------------------------------------------------
	def set_To_Blue2(self):
		""""""
		self.setValue("blue2")
	#----------------------------------------------------------------------
	def set_To_Alpha(self):
		""""""
		self.setValue("alpha")
	#----------------------------------------------------------------------
	def set_To_Alpha2(self):
		""""""
		self.setValue("alpha2")
	#----------------------------------------------------------------------
	def set_To_White(self):
		""""""
		self.setValue("white")
	#----------------------------------------------------------------------
	def set_To_Black(self):
		""""""
		self.setValue("black")

########################################################################
class Shuffle_Channel_Knobs(object):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,node):
		""""""
		self.red    = node.knob("red")
		self.green  = node.knob("green")
		self.blue   = node.knob("blue")
		self.alpha  = node.knob("alpha")
		self.red2   = node.knob("black")
		self.green2 = node.knob("white")
		self.blue2  = node.knob("red2")
		self.alpha2 = node.knob("green2")
		
################################################################################
class Shuffle(Node):
	NODE_TYPE_RELATION  = "Shuffle"
	CHANNEL_OPTIONS = Shuffle_Channels
	CHANNEL_VALUES  = Shuffle_Channel_Values
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		""""""
		super(Shuffle,self).__init__(*args,**kwargs)
		#self.channels_knobs = Shuffle_Channel_Knobs(self)
	#----------------------------------------------------------------------
	def set_In_Layer(self,layerName,section=1):
		"""
			self.set_In_Layer("rgba",1) -> bool

			Set the channal layer used by this shuffle node 

			@param layerName The name of the a channal layer
			
			@param section choose wich in to set : 1 for in and 2 for in2 

		"""
		if section == 1:
			return self.nuke_object.knob("in").setValue(layerName)
		elif section == 2:
			return self.nuke_object.knob("in2").setValue(layerName)
		else:
			raise ValueError("section value is invalid {} value must be 1 or 2".format(section))
		
	#----------------------------------------------------------------------
	def get_In_Layer(self,section=1):
		"""
			self.get_In_Layer(1) -> string

			get the channal layer used by this shuffle node
			
			@param section choose wich in to get: 1 for in and 2 for in2 
		"""
		if section == 1:
			return self.nuke_object.knob("in").value()
		elif section == 2:
			return self.nuke_object.knob("in2").value()
		else:
			raise ValueError("section value is invalid {} value must be 1 or 2".format(section))
		
	#----------------------------------------------------------------------
	def set_Out_Layer(self,layerName,section=1):
		"""
			self.set_Out_Layer("rgba",1) -> bool

			Set the channal layer used by this shuffle node 

			@param layerName The name of the a channal layer
			
			@param section choose wich in to set : 1 for out and 2 for out2 

		"""
		if section == 1:
			return self.nuke_object.knob("out").setValue(layerName)
		elif section == 2:
			return self.nuke_object.knob("out2").setValue(layerName)
		else:
			raise ValueError("section value is invalid {} value must be 1 or 2".format(section))
		
	#----------------------------------------------------------------------
	def get_Out_Layer(self,section=1):
		"""
			self.get_Out_Layer(1) -> string
			
			get the channal layer used by this shuffle node
			
			@param section choose wich in to get: 1 for out and 2 for out2 
		"""
		if section == 1:
			return self.nuke_object.knob("out").value()
		elif section == 2:
			return self.nuke_object.knob("out2").value()
		else:
			raise ValueError("section value is invalid {} value must be 1 or 2".format(section))
		
	
	
	#----------------------------------------------------------------------
	def set_Channel_Value(self,channel,value):
		"""
			self.set_Channel_Value("red", "alpha") -> bool

			Set the channal to value
			
			@param channel the channal to be used valid options are: red green blue alpha black white red2 green2
			
			@param value value for the channel to use valid options are: alpha alpha2 black blue blue2 green green2 off red red2 white

		"""
		if not self.CHANNEL_OPTIONS.is_Valid_Value(channel):
			raise ValueError("{} is not a vaild channel".format(channel))
		if not self.CHANNEL_VALUES.is_Valid_Value(value):
			raise ValueError("{} is not a vaild channal value".format(value))
		
		return self.nuke_object.knob(channel).setValue(value)
	
	in_layer_value  = property(fget=partial(get_In_Layer,section=1), fset= partial(set_In_Layer,section=1), doc="in knob value access")
	in2_layer_value = property(fget=partial(get_In_Layer,section=2), fset= partial(set_In_Layer,section=2), doc="in2 knob value access")
	
	out_layer_value  = property(fget=partial(get_Out_Layer,section=1), fset= partial(set_Out_Layer,section=1), doc="out knob value access")
	out2_layer_value = property(fget=partial(get_Out_Layer,section=2), fset= partial(set_Out_Layer,section=2), doc="out2 knob value access")