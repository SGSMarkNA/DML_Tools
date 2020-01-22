import maya.cmds as cmds
from .. import Dependency_Node 
from ...General_Utils import flatten
	
########################################################################
class Network(Dependency_Node):
	MAYA_NODE_TYPE_RELATION = "network"
	#----------------------------------------------------------------------
	@classmethod
	def createNode(cls,*args,**kwargs):
		""""""
		new_keys = {}
		if "name" in kwargs:
			if not kwargs["name"] == None:
				new_keys["name"] = kwargs.get("name")
		if kwargs.has_key("parent"):
			new_keys["parent"] = kwargs.get("parent")
		if "skipSelect" in kwargs:
			new_keys["skipSelect"] = kwargs.get("skipSelect")
		else:
			new_keys["skipSelect"] = True
			
		res = cmds.createNode("network",**new_keys)
		return res