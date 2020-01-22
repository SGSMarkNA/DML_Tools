import maya.cmds as cmds
from ... import General_Utils
from ..Abstract_Nodes.Dependency_Node import Dependency_Node
from ...Decorators.Node_Wraper_Manager import node_Return_Wrapper
from ...Decorators.Node_Lock_Manager import locked_Node_Management

__all__ = ["Shading_Node"]
########################################################################
class Shading_Node(Dependency_Node):
	MAYA_NODE_TYPE_RELATION = "material"
	#----------------------------------------------------------------------
	def shading_engine(self):
		return self.listConnections(s=0,d=1,type="shadingEngine")