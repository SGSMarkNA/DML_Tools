from .Generic_Functions import string_To_Valid_Attribute_Name
import warnings

#################################################################################
class Dict_Keys_Attribute_Object(object):
	def __init__(self, data):
		self._orig_data = data
		for key, value in list(data.items()):
			key = string_To_Valid_Attribute_Name(key)
			if isinstance(value, dict):
				self.__dict__[key] = Dict_Keys_Attribute_Object(value)
			elif isinstance(value, list):
				new_val = []
				for val in value:
					if isinstance(val, dict):
						val = Dict_Keys_Attribute_Object(val)
					new_val.append(val)
				self.__dict__[key] = new_val
			else:
				self.__dict__[key] = value
	def __repr__(self):
		return self.__class__.__name__ + "(%r)" % self._orig_data

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