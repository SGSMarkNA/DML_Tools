import inspect
import nuke
from ...Mata_Classes.Nuke_Object_Return_Type_Publication_Metaclass import Nuke_Object_Return_Type_Publication
from ...Decorators.Node_Wraper_Manager import to_DML_Node

########################################################################
class Read_Only_Attribute(object):
	""" """
	#----------------------------------------------------------------------
	def __set__(self, instance, value):
		raise AttributeError("attribute is a read only")

########################################################################
class Nuke_Object_Attribute(Read_Only_Attribute):
	""" """
	#----------------------------------------------------------------------
	def __get__(self, instance, cls):
		return instance._nuke_object
	#----------------------------------------------------------------------
	def __set__(self, instance, value):
		instance.__dict__["_nuke_object"] = value
		
########################################################################
class DML_Nuke_Object(object):
	__metaclass__             = Nuke_Object_Return_Type_Publication
	IS_CREATABLE              = False
	CREATE_COMMAND            = None
	DEFAULT_ARGS              = ""
	_is_dml_object            = None
	nuke_object               = Nuke_Object_Attribute()
	#----------------------------------------------------------------------
	def __new__(cls,*args,**kwargs):
		if len(args) and isinstance(args[0], DML_Nuke_Object):
			return args[0]
		else:
			obj = object.__new__(cls)
			obj.nuke_object = args[0]
			return obj
	##----------------------------------------------------------------------
	#def __init__(self,*args,**kwargs):
		#""""""
		#print "test"
	#----------------------------------------------------------------------
	def __str__(self):
		return str(self.nuke_object)
	#----------------------------------------------------------------------
	def __repr__(self):
		return repr(self.nuke_object)
	#----------------------------------------------------------------------
	def __getattribute__(self,name):
		try:
			return object.__getattribute__(self,name)
		except AttributeError:
			nuke_object = object.__getattribute__(self,"_nuke_object")
			if hasattr(nuke_object,name):
				return getattr(nuke_object,name)
			else:
				raise AttributeError("object has no attribute '{}'".format(name))