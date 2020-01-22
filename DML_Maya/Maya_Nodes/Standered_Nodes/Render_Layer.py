import maya.cmds as cmds
from ... import General_Utils
from ..Abstract_Nodes.Dependency_Node import Dependency_Node
from ...Decorators.Node_Wraper_Manager import node_Return_Wrapper
from ...Decorators.Node_Lock_Manager import locked_Node_Management
__all__ = ["Render_Layer"]

########################################################################
class Render_Layer(Dependency_Node):
	MAYA_NODE_TYPE_RELATION = "renderLayer"
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def addMembers(self,*items):
		items = General_Utils.flatten(items)
		if len(items):
			cmds.editRenderLayerMembers(self,items)
	#----------------------------------------------------------------------
	@locked_Node_Management
	def removeMembers(self,*items):
		items = General_Utils.flatten(items)
		if len(items):
			cmds.editRenderLayerMembers( self, items, remove=True)
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def members(self):
		return General_Utils.none_To_List(cmds.editRenderLayerMembers( self,fullNames=True, query=True ))
	#----------------------------------------------------------------------
	def baseID(self):
		return cmds.editRenderLayerGlobals(self,query=True, baseId=True )
	#----------------------------------------------------------------------
	def makeCurrent(self):
		try:
			cmds.editRenderLayerGlobals(currentRenderLayer=self)
		except RuntimeError:
			pass
	#----------------------------------------------------------------------
	@locked_Node_Management
	def enable_Attribute_overRide(self,Plugs):
		cmds.editRenderLayerAdjustment(Plugs,layer=self)
