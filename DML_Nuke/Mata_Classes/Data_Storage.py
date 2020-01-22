import sys,os,warnings
#---------------------------------------------------------------------------------
class Singleton(type):
	""""""
	def __new__(mcl, classname, bases, classdict):

		# newcls =  super(Singleton, mcl).__new__(mcl, classname, bases, classdict)

		# redefine __new__
		def __new__(cls, *p, **k):
			if '_the_instance' not in cls.__dict__:
				cls._the_instance = super(newcls, cls).__new__(cls, *p, **k)
			return cls._the_instance
		newdict = { '__new__': __new__}
		# define __init__ if it has not been defined in the class being created
		def __init__(self, *p, **k):
			cls = self.__class__
			if p :
				if hasattr(self, 'clear') :
					self.clear()
				else :
					super(newcls, self).__init__()
				super(newcls, self).__init__(*p, **k)
		if '__init__' not in classdict :
			newdict['__init__'] = __init__
		# Note: could have defined the __new__ method like it is done in Singleton but it's as easy to derive from it
		for k in classdict :
			if k in newdict :
				warnings.warn("Attribute %r is predefined in class %r of type %r and can't be overriden" % (k, classname, mcl.__name__))
			else :
				newdict[k] = classdict[k]

		newcls =  super(Singleton, mcl).__new__(mcl, classname, bases, newdict)

		return newcls

########################################################################
class Nuke_Node_Type_To_Class_Wapper_Container(dict):
	""""""
	__metaclass__ = Singleton

########################################################################
class Nuke_Node_Type_Overide_Return_Wapper_Check_Container(dict):
	""""""
	__metaclass__ = Singleton

########################################################################
class Nuke_Knob_Type_To_Class_Wapper_Container(dict):
	""""""
	__metaclass__ = Singleton
	
########################################################################
class Nuke_Knob_Type_Overide_Return_Wapper_Check_Container(dict):
	""""""
	__metaclass__ = Singleton
	
########################################################################
class Nuke_Object_Type_To_Class_Wapper_Container(dict):
	""""""
	__metaclass__ = Singleton
	
Node_Return_Type_Relations      = Nuke_Node_Type_To_Class_Wapper_Container()
Node_Return_Type_Overides       = Nuke_Node_Type_Overide_Return_Wapper_Check_Container()
Knob_Return_Type_Relations      = Nuke_Knob_Type_To_Class_Wapper_Container()
Knob_Return_Type_Overides       = Nuke_Knob_Type_Overide_Return_Wapper_Check_Container()
Object_Return_Type_Relations    = Nuke_Object_Type_To_Class_Wapper_Container()