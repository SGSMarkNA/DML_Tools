import maya.cmds as cmds

from ..Abstract_Nodes.Selection_Set import Selection_Set

__all__ = ["Object_Set"]
########################################################################
class Object_Set(Selection_Set):
	MAYA_NODE_TYPE_RELATION = "objectSet"
	#----------------------------------------------------------------------
	@classmethod
	def createNode(cls,*args,**kwargs):
		""""""
		return cmds.sets(*args,**kwargs)