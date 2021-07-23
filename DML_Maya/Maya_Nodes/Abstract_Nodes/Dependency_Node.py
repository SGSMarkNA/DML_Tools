
import maya.cmds as cmds
from ..Base_Nodes.API_Node import DML_Node
from ... import dml
from ...Decorators.Node_Lock_Manager import locked_Node_Management
from ...Decorators.Node_Wraper_Manager import node_Return_Wrapper,to_DML_Node,to_DML_Plug

if False:
	from .Generic_Plug import Plug
	from DML_Tools.Maya.DML_Maya.Decorators.Node_Lock_Manager import locked_Node_Management
	from DML_Tools.Maya.DML_Maya.Decorators.Node_Wraper_Manager import node_Return_Wrapper,to_DML_Node,to_DML_Plug
########################################################################
class Node_Type_Command_Attribute(object):
	""" """
	#----------------------------------------------------------------------
	def __init__(self,flag):
		""""""
		self.flag = flag
	#----------------------------------------------------------------------
	def __get__(self, instance, cls):
		return cmds.nodeType( instance, **{self.flag:True})
	#----------------------------------------------------------------------
	def __set__(self, instance, name):
		raise AttributeError("is a read only")

########################################################################
class Object_Type_Command_Attribute(object):
	""" """
	#----------------------------------------------------------------------
	def __get__(self, instance, cls):
		return cmds.objectType(instance)
	#----------------------------------------------------------------------
	def __set__(self, instance, name):
		raise AttributeError("is a read only")
	
#----------------------------------------------------------------------	
def listDestinationConnectionsRecursively(node,**kwargs):
	""" """
	res = []
	for flg in ["s","d","p","c"," connections"]:
		if flg in kwargs:
			del kwargs[flg]
	kwargs["source"]=False
	kwargs["plugs"]=False
	kwargs["destination"]=True
	destinations = cmds.listConnections(node,**kwargs)

	if destinations == None:
		return res

	if len(destinations):
		res.extend(destinations)

		for destination in destinations:
			res.extend(listDestinationConnectionsRecursively(destination))

	res = list(set(res))
	return res

#----------------------------------------------------------------------	
def listSourceConnectionsRecursively(node,**kwargs):
	""" """
	res = []
	for flg in ["s","d","p","c"," connections"]:
		if flg in kwargs:
			del kwargs[flg]
	kwargs["source"]=True
	kwargs["plugs"]=False
	kwargs["destination"]=False
	sources = cmds.listConnections(node,**kwargs)

	if sources == None:
		return res

	if len(sources):
		res.extend(sources)

		for source in sources:
			res.extend(listSourceConnectionsRecursively(source))

	res = list(set(res))
	return res

########################################################################
class Dependency_Node(DML_Node):
	apiType        = Node_Type_Command_Attribute("apiType")
	derivedTypes   = Node_Type_Command_Attribute("derived")
	inheritedTypes = Node_Type_Command_Attribute("inherited")
	objectType     = Object_Type_Command_Attribute()
	MAYA_NODE_TYPE_RELATION   = "default"
	#----------------------------------------------------------------------
	def addAttr(self,name,**kwargs):
		""""""
		if not self.attributeExists(name):
			kwargs["ln"]=name
			cmds.addAttr(self,**kwargs)
		plg = to_DML_Plug(self,name)
		if False:
			plg = Plug()
		return plg
	#----------------------------------------------------------------------
	def isObjectType(self,type):
		"""true if the object is exactly of the specified type. False otherwise"""
		return cmds.objectType(self,isType=type)
	#----------------------------------------------------------------------
	@locked_Node_Management
	def rename(self,value):
		"rename this object"
		cmds.rename(self,value)
	#----------------------------------------------------------------------
	@property
	def nice_name(self):
		res = str(self.name)
		if not self.namespace == "":
			res = res.split(":")[-1]
		return res.split("|")[-1]
	#----------------------------------------------------------------------
	@property
	def namespace(self):
		return self.apiFn.namespace
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def listSets(self,**kwargs):
		""""""
		kwargs["object"]=self
		return cmds.listSets(**kwargs)
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def listConnections(self,**kwargs):
		""""""
		return cmds.listConnections(self,**kwargs)
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def listSourceConnectionsRecursively(self,**kwargs):
		""""""
		return listSourceConnectionsRecursively(self,**kwargs)
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def listDestinationConnectionsRecursively(self,**kwargs):
		""""""
		return listDestinationConnectionsRecursively(self,**kwargs)
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def duplicate(self,**kwargs):
		""""""
		return cmds.duplicate(self,**kwargs)
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def duplicate_upstreamNodes(self,**kwargs):
		""""""
		singleReturn = kwargs.pop("singleReturn",False)
		kwargs["upstreamNodes"]=True
		res = cmds.duplicate(self,**kwargs)
		if singleReturn:
			return res[0]
		else:
			return res
	#----------------------------------------------------------------------
	def attributeExists(self,attr):
		return cmds.attributeQuery( attr, node=self, exists=True )
	#----------------------------------------------------------------------
	@locked_Node_Management
	def delete(self):
		cmds.delete(self)
	#----------------------------------------------------------------------
	def lockNode(self):
		""""""
		cmds.lockNode(self,lock=True)
	#----------------------------------------------------------------------
	def unlockNode(self):
		""""""
		cmds.lockNode(self,lock=False)
	#----------------------------------------------------------------------
	def isLocked(self):
		return cmds.lockNode(self, q=True, lock=True,lockName=False)
	#----------------------------------------------------------------------
	def select(self, **kwargs):
		""""""
		cmds.select(self, **kwargs)
	#----------------------------------------------------------------------
	def attributeInfo(self,**kwargs):
		"""([allAttributes=boolean], [bool=boolean], [enumerated=boolean], [hidden=boolean], [inherited=boolean], [internal=boolean], [leaf=boolean], [logicalAnd=boolean], [multi=boolean], [short=boolean], [type=string], [userInterface=boolean], [writable=boolean])"""
		return cmds.attributeInfo( self, **kwargs)
	#----------------------------------------------------------------------
	def assinedDisplayLayer(self):
		"The name of the display layer that this object is assined to"
		if not self.attributeExists("drawOverride"):
			return []
		else:
			layer = cmds.listConnections( self.name+".drawOverride", destination=False, source=True, skipConversionNodes=True, shapes=False, type="displayLayer", exactType=True)
			if layer == None:
				return 'defaultLayer'
			return layer[0]
	#----------------------------------------------------------------------
	def __getattribute__(self,name):
		try:
			res = object.__getattribute__(self,name)
		except AttributeError:
			#if not name.startswith("_"):
			my_name = self.name
			path = my_name + "." + name
			if cmds.objExists(path):
				return to_DML_Plug(self,name)
			else:
				raise AttributeError("object has no attribute '{}'".format(name))
			#else:
				#raise AttributeError("object has no attribute '{}'".format(name))			
		return res