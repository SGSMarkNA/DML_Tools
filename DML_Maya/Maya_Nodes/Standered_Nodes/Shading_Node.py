import maya.cmds as cmds
#from ... import General_Utils
from ..Abstract_Nodes.Dependency_Node import Dependency_Node
#from ...Decorators.Node_Wraper_Manager import node_Return_Wrapper
#from ...Decorators.Node_Lock_Manager import locked_Node_Management
from Shading_Engine import Shading_Engine

__all__ = ["Shading_Node"]
########################################################################
class Shading_Node(Dependency_Node):
	MAYA_NODE_TYPE_RELATION = "material"
	CREATE_COMMAND          = cmds.joint
	#----------------------------------------------------------------------
	def shading_engine(self):
		sg = self.listConnections(s=0,d=1,type="shadingEngine")
		if len(sg):
			sg = sg[0]
			isinstance(sg,Shading_Engine)
			return sg
		else:
			return None
	#----------------------------------------------------------------------
	def add_Elements(self,*elements):
		""""""
		sg = self.shading_engine()
		if sg is not None:
			sg.forceElement(*elements)
		else:
			raise RuntimeError("Shader {} is not attached to a shadingEngine".format(self.name))
	#----------------------------------------------------------------------
	@classmethod
	def createNode(cls,shaderType,**kwargs):
		""""""
		kwargs["asShader"] = True
		res = cmds.shadingNode(shaderType,**kwargs)
		sg = Shading_Engine(res+"SG")
		sg.rename(res+"SG")
		sg.Assine_To_Material(res)
		return res