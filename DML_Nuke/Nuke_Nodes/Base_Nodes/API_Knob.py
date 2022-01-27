import inspect
import nuke
from ...Mata_Classes.Knob_Return_Type_Publication_Metaclass import Knob_Return_Type_Publication
from ...Decorators.Node_Wraper_Manager import to_DML_Node


#----------------------------------------------------------------------
def get_nuke_object(self):
	return self._nuke_object
#----------------------------------------------------------------------
def set_nuke_object(self, value):
	self.__dict__["_nuke_object"] = value

#----------------------------------------------------------------------
def get_nuke_knob_name(self):
	return self._nuke_object.name()
#----------------------------------------------------------------------
def set_nuke_knob_name(self, value):
	self._nuke_object.setName(value)

#----------------------------------------------------------------------
def get_nuke_knob_full_name(self):
	return self._nuke_object.fullyQualifiedName()

#----------------------------------------------------------------------
def get_nuke_knob_label(self):
	return self._nuke_object.label()
#----------------------------------------------------------------------
def set_nuke_knob_label(self, value):
	self._nuke_object.setLabel(value)

#----------------------------------------------------------------------
def get_nuke_knob_tooltip(self):
	return self._nuke_object.tooltip()
#----------------------------------------------------------------------
def set_nuke_knob_tooltip(self, value):
	self._nuke_object.setTooltip(value)

#----------------------------------------------------------------------
def get_nuke_knob_enabled(self):
	return self._nuke_object.enabled()
#----------------------------------------------------------------------
def set_nuke_knob_enabled(self, value):
	self._nuke_object.setEnabled(value)

#----------------------------------------------------------------------
def get_nuke_knob_Animated(self):
	return self._nuke_object.isAnimated()
#----------------------------------------------------------------------
def set_nuke_knob_Animated(self, value):
	self._nuke_object.setAnimated(value)

#----------------------------------------------------------------------
def get_nuke_knob_visible(self):
	if self._nuke_object.Class() in ['Tab_Knob',"Link_Knob"]:
		return self._nuke_object.getFlag(nuke.INVISIBLE) is False
	else:
		return self._nuke_object.visible()
#----------------------------------------------------------------------
def set_nuke_knob_visible(self, value):
	if self._nuke_object.Class() in ['Tab_Knob',"Link_Knob"]:
		if not value:
			self._nuke_object.setFlag(nuke.INVISIBLE)
		else:
			self._nuke_object.clearFlag(nuke.INVISIBLE)
	else:
		self._nuke_object.setVisible(value)

########################################################################
class DML_Knob(object, metaclass=Knob_Return_Type_Publication):
	KNOB_TYPE_RELATION        = None
	IS_CREATABLE              = False
	CREATE_COMMAND            = None
	DEFAULT_ARGS              = ""
	_is_dml_object            = None
	nuke_object               = property(fget=get_nuke_object, fset=set_nuke_object, doc="The Wrapped Nuke Object")
	name                      = property(fget=get_nuke_knob_name, fset=set_nuke_knob_name, doc="The name of this knob")
	fullName                  = property(fget=get_nuke_knob_full_name, doc="The full path to the this knob")
	label                     = property(fget=get_nuke_knob_label, fset=set_nuke_knob_label, doc="The label shown in the editor for this knob")
	tooltip                   = property(fget=get_nuke_knob_tooltip, fset=set_nuke_knob_tooltip, doc="tooltip for this knob")
	enabled                   = property(fget=get_nuke_knob_enabled, fset=set_nuke_knob_enabled, doc="enabled state")
	animated                  = property(fget=get_nuke_knob_Animated, fset=set_nuke_knob_Animated, doc="")
	visible                   = property(fget=get_nuke_knob_visible, fset=set_nuke_knob_visible, doc="")
	#----------------------------------------------------------------------
	def __new__(cls,*args,**kwargs):
		if len(args):
			if isinstance(args[0],nuke.Knob):
				obj = object.__new__(cls)
				obj.nuke_object = args[0]
				return obj
			elif isinstance(args[0], DML_Knob):
				return args[0]
			elif isinstance(args[0], str):
				obj = object.__new__(cls)
				fn = getattr(nuke,cls.__name__)
				nuke_knob = fn(args[0])
				nuke_knob.setLabel(args[0])
				obj.nuke_object = nuke_knob
				
				return obj
		else:
			fn = getattr(nuke,cls.__name__)
			name          = kwargs.get("name",cls.__name__.lower())
			label         = kwargs.get("label",cls.__name__.lower().replace("_"," "))
			tcl_value     = kwargs.get("tcl_value",None)
			value         = kwargs.get("value",None)
			values        = kwargs.get("values",None)
			expression    = kwargs.get("expression",None)
			nuke_knob = fn(name)
			nuke_knob.setLabel(label)

			if tcl_value:
				nuke_knob.fromScript(tcl_value)
			elif value:
				nuke_knob.setValue(value)
			elif values:
				nuke_knob.setValues(values)
			elif expression:
				nuke_knob.setExpression(expression)

			obj.nuke_object = nuke_knob
			return obj
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		""""""
		pass
	#----------------------------------------------------------------------
	def __str__(self):
		return str(self.fullName)
	#----------------------------------------------------------------------
	def __repr__(self):
		return '{}.{}("{}")'.format(self.__module__,self.__class__.__name__,self.fullName)
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
			
if False:
	isinstance(DML_Knob.label,str)
	isinstance(DML_Knob.name,str)
	isinstance(DML_Knob.fullName,str)
	isinstance(DML_Knob.tooltip,str)
	isinstance(DML_Knob.nuke_object,nuke.Knob)