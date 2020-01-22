
from .. import Data_Storage

########################################################################
class Plug_Return_Type_Publication(type):
	""""""
	#----------------------------------------------------------------------
	def __new__(mcs, name, bases, dct):
		"""This Is Run Before The Class Is Created. Not An Instance Of The Class But The Creation Of The Class Itself"""
		## Generate The New Class Type And Return It
		MAYA_PLUG_TYPE_RELATION   = dct.pop('MAYA_PLUG_TYPE_RELATION',None)
		RETURN_OVERIDE_CHECK_TYPE = dct.pop('RETURN_OVERIDE_CHECK_TYPE',None)
		
		res = type.__new__(mcs, name, bases, dct)
		
		if MAYA_PLUG_TYPE_RELATION is not None:
			Data_Storage.Plug_Return_Type_Relations[MAYA_PLUG_TYPE_RELATION]=res
			
		if RETURN_OVERIDE_CHECK_TYPE is not None:
			if not Data_Storage.Plug_Return_Type_Overides.has_key(RETURN_OVERIDE_CHECK_TYPE):
				Data_Storage.Plug_Return_Type_Overides[RETURN_OVERIDE_CHECK_TYPE]=[]
				
			if not res in Data_Storage.Plug_Return_Type_Overides[RETURN_OVERIDE_CHECK_TYPE]:
				Data_Storage.Plug_Return_Type_Overides[RETURN_OVERIDE_CHECK_TYPE].append(res)
		return res

	##----------------------------------------------------------------------
	#def __init__(cls, name, bases, dct):
		#return super(Plug_Return_Type_Publication, cls).__init__(name, bases, dct)

	##----------------------------------------------------------------------
	#def __call__(cls,*args,**kwargs):
		#"""This Is Run Before An Instance Of The Class Created And Allows For The Inspection And Manipulation Of The Values Used To Create The New Instance"""
		## Create The New Plug Instance
		#res = type.__call__(cls,*args,**kwargs)
		#return res