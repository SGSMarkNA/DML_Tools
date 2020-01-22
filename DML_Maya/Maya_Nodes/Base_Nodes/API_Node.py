
import maya.cmds as cmds
import maya.api.OpenMaya as OpenMaya
from ...Mata_Classes.Node_Return_Type_Publication_Metaclass import Node_Return_Type_Publication
from ... import Data_Storage
from ...General_Utils import flatten
from ... import dml

# This Has Reason Other Then To Compensate For Wing IDS Code Analizer
if False:
	from DML_Maya import Data_Storage
	from DML_Maya import dml
	from DML_Maya.General_Utils import flatten

########################################################################
class Maya_MObject_Attribute(object):
	""" """
	#----------------------------------------------------------------------
	def __get__(self, instance, cls):
		return instance.apiFn.object()
	#----------------------------------------------------------------------
	def __set__(self, instance, node):
		raise AttributeError("apiMObject is a read only")
########################################################################
class Maya_Node_Name_Attribute(object):
	""" """
	#----------------------------------------------------------------------
	def __get__(self, instance, cls):
		if hasattr(instance,"_api_name_function"):
			return instance._api_name_function()
		else:
			if hasattr(instance.apiFn,"fullPathName"):
				instance.__dict__["_api_name_function"]=instance.apiFn.fullPathName
			else:
				instance.__dict__["_api_name_function"]=instance.apiFn.name
			return instance._api_name_function()
	#----------------------------------------------------------------------
	def __set__(self, instance, node):
		raise AttributeError("name is a read only")
########################################################################
class Maya_Api_Function_Set_Attribute(object):
	""" """
	#----------------------------------------------------------------------
	def __get__(self, instance, cls):
		if hasattr(instance,"_api_function_set"):
			return instance._api_function_set
		else:
			sel = OpenMaya.MSelectionList()
			sel.add(instance.uuidNode)
			obj = sel.getDependNode(0)
			if obj.hasFn(OpenMaya.MFn.kDagNode):
				fnset = OpenMaya.MFnDagNode(obj)
			else:
				fnset = OpenMaya.MFnDependencyNode(obj)
			instance.__dict__["_api_function_set"]=fnset
		return instance._api_function_set
	#----------------------------------------------------------------------
	def __set__(self, instance, node):
		raise AttributeError("apiFn is read only")
########################################################################
class Maya_Uuid_Node_Attribute(object):
	""" """
	#----------------------------------------------------------------------
	def __get__(self, instance, cls):
		lookup = cmds.ls(instance._uuid,l=True)
		if len(lookup):
			return lookup[0]
		else:
			return None
	#----------------------------------------------------------------------
	def __set__(self, instance, node):
		if cmds.objExists(node):
			lookup = cmds.ls(node, uuid=True)
			instance._uuid = lookup[0]
		else:
			raise LookupError("maya object '{}' does not exist".format(node))
		
########################################################################
class Maya_Uuid_Attribute(object):
	""" """
	#----------------------------------------------------------------------
	def __get__(self, instance, cls):
		return instance._uuid
	#----------------------------------------------------------------------
	def __set__(self, instance, node):
		raise AttributeError("uuid is read only")
	
########################################################################
class Maya_Api_Uuid_Attribute(object):
	""" """
	#----------------------------------------------------------------------
	def __get__(self, instance, cls):
		return instance.apiFn.uuid()
	#----------------------------------------------------------------------
	def __set__(self, instance, node):
		raise AttributeError("apiUuid is read only")

########################################################################
class DML_Node(object):
	__metaclass__             = Node_Return_Type_Publication
	MAYA_NODE_TYPE_RELATION   = None
	RETURN_OVERIDE_CHECK_TYPE = None
	IS_CREATABLE              = False
	CREATE_COMMAND            = None
	_is_dml_maya_node         = None
	uuid                      = Maya_Uuid_Attribute()
	apiUuid                   = Maya_Api_Uuid_Attribute()
	uuidNode                  = Maya_Uuid_Node_Attribute()
	apiFn                     = Maya_Api_Function_Set_Attribute()
	apiMObject                = Maya_MObject_Attribute()
	name                      = Maya_Node_Name_Attribute()
	#----------------------------------------------------------------------
	def __new__(cls,*args,**kwargs):
		forceRecreate = kwargs.get("DML_forceRecreate",kwargs.get("DML_FRC",False))
		nodeName = kwargs.get("name", kwargs.get("n",None))
		node_created = False
		if nodeName == None and len(args) == 1:
			nodeName = args[0]
		
		if nodeName == None or not cmds.objExists(nodeName):
			if hasattr(cls,"createNode"):
				nodeName = cls.createNode(*args,**kwargs)
				node_created =True
			elif cls.CREATE_COMMAND != None:
				nodeName = cls.CREATE_COMMAND(*args,**kwargs)
				node_created =True
			else:
				if nodeName == None:
					raise ValueError("no name was given and this class {} has no create function".format(cls.__name__))
				else:
					raise LookupError("The input object {} does not exist and this class {} has no create function".format(nodeName, cls.__name__))
		
		if cmds.objExists(nodeName):
			uuids = cmds.ls(nodeName, uuid=True)
			if len(uuids) == 1:
				uuid = uuids[0]
				if uuid in Data_Storage.Cashed_Nodes_Container and not forceRecreate:
					obj = Data_Storage.Cashed_Nodes_Container.get(uuid)
					if not obj.apiMObject.isNull():
						if node_created and hasattr(obj,"_post_Create_Actions"):
							obj._post_Create_Actions()
						return obj
				obj = object.__new__(cls)
				obj._uuid = uuid
				
				sel = OpenMaya.MSelectionList()
				sel.add(obj.uuidNode)
				mobj = sel.getDependNode(0)
				if mobj.hasFn(OpenMaya.MFn.kDagNode):
					fnset = OpenMaya.MFnDagNode(mobj)
					obj._api_name_function = fnset.fullPathName
				else:
					fnset = OpenMaya.MFnDependencyNode(mobj)
					obj._api_name_function = fnset.name
				obj._api_function_set = fnset
				Data_Storage.Cashed_Nodes_Container[uuid] = obj
				if hasattr(obj,"_post_Create_Actions"):
					obj._post_Create_Actions()
			else:
				raise ValueError("The Input Node Named '{}' Is Not Unique".format(nodeName))
		else:
			raise LookupError("The Input Node Named '{}' Does Not Exist".format(nodeName))
		return obj
	##----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		if False:
			isinstance(self.apiFn,OpenMaya.MFnDependencyNode)
			isinstance(self.apiMObject,OpenMaya.MObject)
			self._uuid = ""
	#----------------------------------------------------------------------
	def _post_Create_Actions(self):
		""""""
		pass
	#----------------------------------------------------------------------
	def __str__(self):
		return self.name
	#----------------------------------------------------------------------
	def __repr__(self):
		return '{}.{}("{}")'.format(self.__module__,self.__class__.__name__,self.name)
	#----------------------------------------------------------------------
	def __hash__(self):
		return hash(self._uuid)
	#----------------------------------------------------------------------
	def __ne__(self, other):
		return str(self) != str(other)
	#----------------------------------------------------------------------
	def __eq__(self,other):
		""""""
		return str(self) == str(other)
	#----------------------------------------------------------------------
	def __add__(self,other):
		""""""
		return self.name + str(other)
	#----------------------------------------------------------------------
	def __radd__(self,other):
		""""""
		return str(other) + self.name
	#----------------------------------------------------------------------
	@classmethod
	def _overide_Return_Check(cls,node):
		""""""
		return False
	#----------------------------------------------------------------------
	@classmethod
	def get_Center_Of_Objects(cls,args,aslist=False):
		""""""
		args = flatten(args)
		nodes = dml.ls(args,typ="transform")
		res = OpenMaya.MVector()
		for node in nodes:
			res += node.get_Object_Center()
		res /= len(nodes)
		if aslist:
			return list(res)
		else:
			return res
		
		
