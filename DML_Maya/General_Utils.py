#from __future__ import with_statement  # required only for Maya2009/8
import sys,os,time,re,logging,inspect,warnings
import maya.cmds as cmds
import maya.mel as mel

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)



import string
invalid_chars = list(string.punctuation.replace("_", "") + string.whitespace)
string_digits = list(string.digits)
del string


none_To_List  = lambda val:val if val is not None else []
none_To_Zero  = lambda val:val if val is not None else 0

# Generic Utility Functions ---
#---------------------------------------------------------------------------------
#----------------------------------------------------------------------
def string_To_Valid_Attribute_Name(value):
	""""""
	if len(value):
		value = str(value)
		new_value = "".join([char for char in list(value) if not char in invalid_chars])
		new_value = str("n_" + new_value) if new_value[0] in string_digits else new_value
		return new_value
	else:
		raise ValueError("input must not be an empty string")
#----------------------------------------------------------------------
def flatten(x):
	result = []
	for el in x:
		if hasattr(el, "__iter__") and not isinstance(el, str):
			result.extend(flatten(el))
		else:
			result.append(el)
	return result
#---------------------------------------------------------------------------------
def sortNumerically(data):
	"""
	Sort the given data in the way that humans expect.

	>>> data=['Joint_1','Joint_2','Joint_9','Joint_10','Joint_11','Joint_12']
	>>>
	>>> #standard gives us:
	>>> data.sort()
	>>> ['Joint_1', 'Joint_10', 'Joint_11', 'Joint_12', 'Joint_2', 'Joint_9']
	>>> 
	>>> #sortNumerically gives us:
	>>> sortNumerically(data)
	>>> ['Joint_1', 'Joint_2', 'Joint_9', 'Joint_10', 'Joint_11', 'Joint_12']
	"""
	convert = lambda text: int(text) if text.isdigit() else text
	alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
	return sorted(data, key=alphanum_key)
#---------------------------------------------------------------------------------
def floatIsEqual(a, b, tolerance=0.01, allowGimbal=True):
	'''
	compare 2 floats with tolerance.

	:param a: value 1 
	:param b: value 2 
	:param tolerance: compare with this tolerance default=0.001 
	:param allowGimbal: allow values differences to be divisible by 180 compensate for gimbal flips 

	'''
	if abs(a - b) < tolerance:
		return True
	else:
		if allowGimbal:
			mod = abs(a - b) % 180.0
			if mod < tolerance:
				log.debug('compare passed with gimbal : %f == %f : diff = %f' % (a, b, mod))
				return True
			elif abs(180.0 - mod) < tolerance:
				log.debug('compare passed with gimbal 180 : %f == %f : diff = %f' % (a, b, abs(180 - mod)))
				return True
			elif abs(90.0 - mod) < tolerance:
				log.debug('compare passed with gimbal 90 : %f == %f diff = %f' % (a, b, abs(90.0 - mod)))
				return True
			log.debug('compare with gimbal failed against mod 180: best diff :%f' % (abs(180.0-mod)))
			log.debug('compare with gimbal failed against mod 90: best diff :%f' % (abs(90.0-mod)))
	log.debug('float is out of tolerance : %f - %f == %f' % (a, b, abs(a - b)))
	return False
#---------------------------------------------------------------------------------
def forceToString(text):
	'''
	simple function to ensure that data can be passed correctly into
	textFields for the UI (ensuring lists are converted)
	'''
	if issubclass(type(text), list):
		return ','.join(text)
	else:
		return text
#---------------------------------------------------------------------------------
def formatPath(path):
	'''
	take a path and format it to forward slashes with catches for the exceptions
	'''
	return os.path.normpath(path).replace('\\','/').replace('\t','/t').replace('\n','/n').replace('\a', '/a')
#---------------------------------------------------------------------------------
def itersubclasses(cls, _seen=None):
	"""
	itersubclasses(cls)
	http://code.activestate.com/recipes/576949-find-all-subclasses-of-a-given-class/
	Iterator to yield full inheritance from a given class, including subclasses. This
	is used in the MetaClass to build the RED9_META_REGISTERY inheritance dict
	"""
	if _seen is None:
		_seen = set()
	try:
		subs = cls.__subclasses__()
	except TypeError:  # fails only when cls is type
		subs = cls.__subclasses__(cls)
	for sub in subs:
		if sub not in _seen:
			_seen.add(sub)
			yield sub
			for sub in itersubclasses(sub, _seen):
				yield sub


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

# Generic Utility Classes ---
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