#from __future__ import with_statement  # required only for Maya2009/8

import os
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

