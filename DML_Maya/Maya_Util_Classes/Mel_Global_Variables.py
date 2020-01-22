
import maya.mel as mel
from ..General_Utils import Singleton
from .Mel_Variable import Mel_Variable 

########################################################################
class Mel_Global_Variables(object):
	__metaclass__ = Singleton
	#----------------------------------------------------------------------
	def __init__(self):
		""""""
		self.rebuild()

	def rebuild(self):
		for name in mel.eval("env"):
			var = Mel_Variable(name)
			setattr(self, name[1:], var)

	#----------------------------------------------------------------------
	def __getattribute__(self,name):
		obj = object.__getattribute__(self,name)
		if hasattr(obj,"value"):
			return obj.value
		return obj