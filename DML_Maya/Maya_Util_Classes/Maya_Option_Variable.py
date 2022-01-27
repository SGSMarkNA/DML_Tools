
import maya.cmds as cmds
import types
from ..General_Utils import Singleton,string_To_Valid_Attribute_Name,flatten

does_Option_Exist = lambda option_name: cmds.optionVar(exists=option_name) == True
get_Option_Size   = lambda option_name: cmds.optionVar(  arraySize=option_name)

########################################################################
def get_Optional_Variable_Type(option_name):
	""" """
	siz = get_Option_Size(option_name)
	if siz == 0:
		return None
	elif siz == 1:
		val = cmds.optionVar(  q=option_name)
	else:
		val = cmds.optionVar(  q=option_name)[0]
	
	if isinstance(val,int):
		return int
	elif isinstance(val,(bytes,str)):
		return str
	elif isinstance(val,float):
		return float
	else:
		return None

########################################################################
class Base_Option_Variable(object):
	#----------------------------------------------------------------------
	def __init__(self,name,val=None):
		self._name = name
	#----------------------------------------------------------------------
	@property
	def name(self):
		""""""
		return self._name
	#----------------------------------------------------------------------
	@property
	def exists(self):
		""""""
		return does_Option_Exist(self.name)
	#----------------------------------------------------------------------
	@property
	def type(self):
		""""""
		return get_Optional_Variable_Type(self.name)
	#----------------------------------------------------------------------
	@property
	def size(self):
		""""""
		return get_Option_Size(self.name)
	#----------------------------------------------------------------------
	def __repr__(self):
		""""""
		return repr(self.value)
########################################################################
class Option_Variable(Base_Option_Variable):
	#----------------------------------------------------------------------
	def __init__(self,name,val=None):
		super(Option_Variable,self).__init__(name)
		if not val == None:
			self.value = val
	#----------------------------------------------------------------------
	def get_Value(self):
		""""""
		if self.size == 0:
			return None
		else:
			val = cmds.optionVar(q=self.name)	
		if self.size == 1:
			return val
		else:
			typ = self.type
			return [typ(v) for v in val]
	#----------------------------------------------------------------------
	def set_Value(self,val):
		""""""
		typ = type(val)
		if typ == int:
			cmds.optionVar(intValue=[self.name, int(val)])
		elif typ == bool:
			cmds.optionVar(intValue=[self.name, 1 if val else 0])
		elif typ == str or typ == str:
			cmds.optionVar(stringValue=[self.name, str(val)])
		elif typ == float:
			cmds.optionVar(floatValue=[self.name, float(val)])
		else:
			raise NotImplementedError("{} is not a recinized type".format(typ))
	value = property(fget=get_Value, fset=set_Value)
	#----------------------------------------------------------------------
	def append(self,val):
		"""adds this value to the end of the array"""
		self_typ   = self.type
		value_typ  = type(val)
		if value_typ == self_typ:
			if self_typ == int:
				cmds.optionVar(intValueAppend=[self.name, int(val)])
			elif value_typ == str:
				cmds.optionVar(stringValueAppend=[self.name, str(val)])
			elif value_typ == float:
				cmds.optionVar(floatValueAppend=[self.name, float(val)])
			else:
				raise ValueError("The Input Value Must Be A Int String or Float and a {} was found".format(value_typ))
		else:
			raise ValueError("Can Not Append A {} value to a Option_Variable of {}".format(str(value_typ),str(self_typ)))
########################################################################
class Represnted_Option_Variable(Base_Option_Variable):
	#----------------------------------------------------------------------
	def __init__(self,name,val=None):
		super(Represnted_Option_Variable,self).__init__(name)
		if not val == None:
			self.value = val
	#----------------------------------------------------------------------
	def get_Value(self):
		""""""
		if get_Option_Size(self._name) == 0:
			return None
		else:
			return eval(cmds.optionVar(q=self.name))
	#----------------------------------------------------------------------
	def set_Value(self,val):
		""""""
		val_rep = repr(val)
		cmds.optionVar(stringValue=[self.name, val_rep])
		
	value = property(fget=get_Value, fset=set_Value)
	#----------------------------------------------------------------------
	@property
	def type(self):
		""""""
		return type(self.value)
	#----------------------------------------------------------------------
	@property
	def size(self):
		""""""
		if get_Option_Size(self._name) == 0:
			return 0
		else:
			return len(self.value)
########################################################################
class All_Option_Variables(object, metaclass=Singleton):
	def __init__(self):
		""""""
		self._last_rebuild_collected_names = []
		self.rebuild()
	def rebuild(self):
		for name in self._last_rebuild_collected_names:
			del self.__dict__[name]
		self._last_rebuild_collected_names = []
		for name in cmds.optionVar(list=True):
			try:
				att_name = string_To_Valid_Attribute_Name(name) 
				var  = Option_Variable(name)
				self.__dict__[att_name] = var
				self._last_rebuild_collected_names.append(att_name)
			except ValueError:
				continue