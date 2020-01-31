
""""""
from DML_General_Utilities.Generic_Functions  import flatten
import json

class ComplexEncoder(json.JSONEncoder):
	def default(self, obj):
		# Let the base class default method raise the TypeError
		return json.JSONEncoder.default(self, obj)


def as_complex(dct):
	if '__complex__' in dct:
		return complex(dct['real'], dct['imag'])
	return dct

json.loads('{"__complex__": true, "real": 1, "imag": 2}', object_hook=as_complex)


########################################################################
class Base_Object(object):
	""""""

########################################################################
class Object_Binding_Attribute_Access(object):
	""" """
	#----------------------------------------------------------------------
	def __get__(self, instance, cls):
		instance.objectBinding.bindedObject
		return 1
	#----------------------------------------------------------------------
	def __set__(self, instance, value):
		print "Test Set {}".format(repr(instance)),value
		
########################################################################
class Attribute_Accessor(Base_Object):
	""""""
	#----------------------------------------------------------------------
	def getter(self,objectBinding,attributeName):
		""""""
		if not isinstance(objectBinding,Base_Object_Binding):
			raise TypeError("objectBinding input must be Derived From Base_Object_Binding")
		if not isinstance(attributeName,basestring):
			raise TypeError("can initialize class attributeName must be Derived From basestring")
		
		binded_object = objectBinding.bindedObject
		
		if hasattr(binded_object,attributeName):
			return getattr(binded_object,attributeName)
		return None
	
	#----------------------------------------------------------------------
	def setter(self,objectBinding,attributeName, value):
		""""""
		if not isinstance(objectBinding,Base_Object_Binding):
			raise TypeError("objectBinding input must be Derived From Base_Object_Binding")
		if not isinstance(attributeName,basestring):
			raise TypeError("can initialize class attributeName must be Derived From basestring")
		
		binded_object = objectBinding.bindedObject
		
		if hasattr(binded_object,attributeName):
			setattr(binded_object,attributeName,value)
		
########################################################################
class Base_Template_Attribute(Base_Object):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,name,accessor):
		"""Constructor"""
		if not isinstance(name,basestring):
			raise TypeError("can initialize class with name of {} name must be Derived From basestring".format(name.__class__.__name__))
		if not isinstance(accessor,Attribute_Accessor):
			raise TypeError("can initialize class with accessor because it is not Derived From ".format(Attribute_Accessor.__name__))
		self._name = name
		self._accessor = accessor
	#----------------------------------------------------------------------
	def get_Name(self):
		"""returns the name of attribute"""
		return self._name
	
	name         = property(get_Name,None,None,"the name used to access the attribute of the application")
		
########################################################################
class Base_Template_Attribute_List(list):
	""""""

	def __init__(self,*args):
		"""Constructor"""
		args = self._validate_Item_To_Be_Added(args)
		super(Base_Template_Attribute_List,self).__init__(*args)
	#----------------------------------------------------------------------
	def append(self,*args):
		""""""
		validate_items = self._validate_Item_To_Be_Added(*args)
		for item in validate_items:
			super(Base_Template_Attribute_List,self).append(item)
	#----------------------------------------------------------------------
	def extend(self,*args):
		""""""
		validate_items = self._validate_Item_To_Be_Added(*args)
		super(Base_Template_Attribute_List,self).extend(validate_items)
	#----------------------------------------------------------------------
	def _validate_Item_To_Be_Added(self,*args):
		""""""
		args = flatten(*args)
		for item in args:
			if not isinstance(item, ):
				raise ValueError("Can Add item of class {} Only Items Derived From Base_Template_Attribute class can be added to this list".format(item.__class__.__name__))
		return args

########################################################################
class Base_Object_Binding(Base_Object):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,bindedObject,**extraInfo):
		"""Constructor"""
		self._binded_object = bindedObject
		self._extra_info = extraInfo
	#----------------------------------------------------------------------
	def get_ExtraInfo(self):
		"""returns the extraInfo value for this attribute"""
		return self._extra_info
	#----------------------------------------------------------------------
	def get_BindedObject(self):
		"""returns the object used for this binding"""
		return self._binded_object
	#----------------------------------------------------------------------
	def set_BindedObject(self,obj):
		"""set the object used for this binding"""
		self._binded_object = obj
	
	bindedObject = property(get_BindedObject,set_BindedObject,None,"the object used by this binding")
	extraInfo    = property(get_ExtraInfo,None,None,"metadata for this binding")

########################################################################
class Base_Attribute_Collection_Template(Base_Object):
	""""""
	def __init__(self,templateName,attributes=Base_Template_Attribute_List(),applicationName="Generic"):
		"""Constructor"""
		if not isinstance(attributes,Base_Template_Attribute_List):
			raise TypeError("can not initialize class with attributes of {} attributes must be Derived From Base_Template_Attribute_List".format(attributes.__class__.__name__))
		if not isinstance(applicationName,basestring):
			raise TypeError("can not initialize class with applicationName of {} applicationName must be Derived From basestring".format(applicationName.__class__.__name__))
		if not isinstance(templateName,basestring):
			raise TypeError("can not initialize class with templateName of {} templateName must be Derived From basestring".format(templateName.__class__.__name__))		
		
		self._template_name    = templateName
		self._application_name = applicationName
		self._attributes       = attributes
	#----------------------------------------------------------------------
	def get_TemplateName(self):
		"""returns the name of this template"""
		return self._template_name
	#----------------------------------------------------------------------
	def set_TemplateName(self,name):
		"""set the name of this template"""
		if not isinstance(name,basestring):
			raise TypeError("can not templateName of {} templateName must be Derived basestring".format(name.__class__.__name__))		
		self._template_name = name
	#----------------------------------------------------------------------
	def get_ApplicationName(self):
		"""returns the name this template is used with"""
		return self._application_name
	#----------------------------------------------------------------------
	def get_Attributes(self):
		"""returns the attributes used in the template"""
		return self._attributes
	#----------------------------------------------------------------------
	def add_Attribute(self,*args):
		""""""
		args = flatten(args)
		arg_count = len(args)
		if arg_count:
			if arg_count == 1:
				self.attributes.append(args[0])
			else:
				if all([isinstance(item) for item in args]):
					self.attributes.extend(args)
				
				elif arg_count == 2 or arg_count == 3:
					self.attributes.append(Base_Template_Attribute(*args))
				else:
					raise ValueError("add_Attribute takes a list of Derived Base_Template_Attributes or a initialize values for a New Attribute")
	
	templateName    = property(get_TemplateName,set_TemplateName,None,"the name for this template")
	attributes      = property(get_Attributes,None,None,"the attributes for this template")
	applicationName = property(get_ApplicationName,None,None,"the name this template is used with")

########################################################################
class Base_Attribute_State(Base_Object):
	""""""
	def __init__(self,):
		"""Constructor"""
		args = self._validate_Item_To_Be_Added(args)
		super(Base_Template_Attribute_List,self).__init__(*args)
	#----------------------------------------------------------------------
	def append(self,*args):
		""""""
		validate_items = self._validate_Item_To_Be_Added(*args)
		for item in validate_items:
			super(Base_Template_Attribute_List,self).append(item)
	#----------------------------------------------------------------------
	def extend(self,*args):
		""""""
		validate_items = self._validate_Item_To_Be_Added(*args)
		super(Base_Template_Attribute_List,self).extend(validate_items)
	#----------------------------------------------------------------------
	def _validate_Item_To_Be_Added(self,*args):
		""""""
		args = flatten(*args)
		for item in args:
			if not isinstance(item, ):
				raise ValueError("Can Add item of class {} Only Items Derived From Base_Template_Attribute class can be added to this list".format(item.__class__.__name__))
		return args

########################################################################
class Base_Attribute_State(Base_Object):
	""""""

	def __init__(self,collectionTemplate,bindedObject):
		"""Constructor"""
		
		
    
	
		
		
    
	
	