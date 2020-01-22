
import maya.api.OpenMaya as OpenMaya
import maya.cmds as cmds
from ..Base_Nodes.API_Component import API_Component
from ...Decorators.Node_Wraper_Manager import node_Return_Wrapper,to_DML_Node,to_DML_Nodes
from ... import General_Utils

########################################################################
class Component(API_Component):
	MAYA_COMPONENT_TYPE_RELATION   = "default"
	RETURN_OVERIDE_CHECK_TYPE = None
	#----------------------------------------------------------------------
	def select(self,**kwargs):
		""""""
		cmds.select(self,**kwargs)