import maya.cmds as cmds
from ... import General_Utils
from ..Abstract_Nodes.Dependency_Node import Dependency_Node
from ...Decorators.Node_Wraper_Manager import node_Return_Wrapper
from ...Decorators.Node_Lock_Manager import locked_Node_Management

__all__ = ["Partition"]
########################################################################
class Partition(Dependency_Node):
	MAYA_NODE_TYPE_RELATION = "partition"
	#----------------------------------------------------------------------
	@classmethod
	def createNode(cls,*args,**kwargs):
		""""""
		return cmds.partition(*args,**kwargs)
	#----------------------------------------------------------------------
	@locked_Node_Management
	def removeSets(self,*items):
		items = General_Utils.flatten(items)
		if len(items):
			cmds.partition( items, removeSet=self)
	#----------------------------------------------------------------------
	@locked_Node_Management
	def addSets(self,*items):
		items = General_Utils.flatten(items)
		if len(items):
			cmds.partition( items, addSet=self)
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def members(self):
		return cmds.partition( self, q=True )
