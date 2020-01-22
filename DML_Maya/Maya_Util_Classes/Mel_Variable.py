
from ..Maya_Util_Functions import get_Mel_Variable 

########################################################################
class Mel_Variable_Attribute(object):
	""" """
	#----------------------------------------------------------------------
	def __get__(self, instance, cls):
		try:
			return instance._name
		except AttributeError:
			raise AttributeError("Mel Variable Name Has Not Been Set")
	#----------------------------------------------------------------------
	def __set__(self, instance, name):
		instance.__dict__["_name"]=name

########################################################################
class Mel_Value_Attribute(object):
	""" """
	#----------------------------------------------------------------------
	def __get__(self, instance, cls):
		return get_Mel_Variable(instance.name)
	#----------------------------------------------------------------------
	def __set__(self, instance, node):
		raise AttributeError("apiMObject is a read only")

########################################################################
class Mel_Variable(object):
	name  = Mel_Variable_Attribute()
	value = Mel_Value_Attribute()
	def __init__(self,name):
		self.name = name