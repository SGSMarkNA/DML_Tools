
import maya.cmds as cmds
import pymel.core as pm
import maya.api.OpenMaya as OpenMaya
from ...Mata_Classes.Component_Return_Type_Publication_Metaclass import Component_Return_Type_Publication
from ...Decorators.Node_Wraper_Manager import to_DML_Node
from ... import Data_Storage
from .DML_MPlug import MPlug
# This Has Reason Other Then To Compensate For Wing IDS Code Analizer
if False:
	from DML_Maya import Data_Storage
	from DML_Maya.Maya_Nodes.Abstract_Nodes.Dependency_Node import Dependency_Node
	
########################################################################
class Py_Mel_Node_Attribute(object):
	""" """
	#----------------------------------------------------------------------
	def __get__(self, instance, cls):
		return instance._pymel_node
	#----------------------------------------------------------------------
	def __set__(self, instance, name):
		raise AttributeError("plug_name is a read only")
	
########################################################################
class Maya_Component_Path_Attribute(object):
	""" """
	#----------------------------------------------------------------------
	def __get__(self, instance, cls):
		path = instance.node.name + "." + instance._raw_name
		return path
	#----------------------------------------------------------------------
	def __set__(self, instance, name):
		raise AttributeError("plug_path is a read only")
########################################################################
class API_Component(object, metaclass=Component_Return_Type_Publication):
	py_Node                      = Py_Mel_Node_Attribute()
	component_path               = Maya_Component_Path_Attribute()
	_is_dml_maya_node            = None
	MAYA_COMPONENT_TYPE_RELATION = None
	RETURN_OVERIDE_CHECK_TYPE    = None
	##----------------------------------------------------------------------
	def __new__(cls,node,attr):
		obj = object.__new__(cls)
		node = to_DML_Node(node)
		obj.node = node
		obj._raw_name = attr
		obj._pymel_node = pm.PyNode(str(node)+'.'+attr)	
		return obj
	#----------------------------------------------------------------------
	def __str__(self):
		return str(self.node.name + "." + self._raw_name)
	#----------------------------------------------------------------------
	def __repr__(self):
		return '{}.{}("{}")'.format(self.__module__,self.__class__.__name__,str(self.node.name + "." + self._raw_name))
	#----------------------------------------------------------------------
	def __hash__(self):
		return hash(self.node._uuid + self.component_path)
	#----------------------------------------------------------------------
	def __ne__(self, other):
		return self.component_path != str(other)
	#----------------------------------------------------------------------
	def __eq__(self,other):
		""""""
		return self.component_path == str(other)
	#----------------------------------------------------------------------
	def __add__(self,other):
		""""""
		return self.component_path + str(other)
	#----------------------------------------------------------------------
	def __radd__(self,other):
		""""""
		return str(other) + self.component_path
	#----------------------------------------------------------------------
	@classmethod
	def _overide_Return_Check(self,node):
		""""""
		return False
	
if False:
	isinstance(API_Component.py_Node,pm.general.MeshVertex)
	API_Component._raw_name = ""
	isinstance(API_Component.node,Dependency_Node)
	isinstance(API_Component.component_path,str)