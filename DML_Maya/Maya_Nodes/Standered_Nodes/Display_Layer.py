
import maya.cmds as cmds
from ... import General_Utils
from ..Abstract_Nodes.Dependency_Node import Dependency_Node
from ...Decorators.Node_Wraper_Manager import node_Return_Wrapper
from ...Decorators.Node_Lock_Manager import locked_Node_Management

# This Has Reason Other Then To Compensate For Wing IDS Code Analizer
if False:
	from DML_Maya import General_Utils

__all__ = ["Display_Layer"]

########################################################################
class Display_Layer(Dependency_Node):
	MAYA_NODE_TYPE_RELATION = "displayLayer"
	#----------------------------------------------------------------------
	@locked_Node_Management
	def addMembers(self,*items, **kwargs):
		noRecurse = kwargs.get("noRecurse", kwargs.get("nr",False))
		items = General_Utils.flatten(items)
		if len(items):
			cmds.editDisplayLayerMembers(self, items, noRecurse=noRecurse)
	#----------------------------------------------------------------------
	@locked_Node_Management
	def removeMembers(self,*items, **kwargs):
		noRecurse = kwargs.get("noRecurse", kwargs.get("nr",False))
		items = General_Utils.flatten(items)
		if len(items):
			cmds.editDisplayLayerMembers("defaultLayer", items,noRecurse=noRecurse)
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def members(self):
		return General_Utils.none_To_List(cmds.editDisplayLayerMembers(self,q=True,fullNames=True))
	#----------------------------------------------------------------------
	@locked_Node_Management
	def clear(self):
		items = self.members()
		if len(items):
			cmds.editDisplayLayerMembers("defaultLayer", items)
	#----------------------------------------------------------------------
	def makeCurrent(self):
		cmds.editDisplayLayerGlobals( cdl=self )
	#----------------------------------------------------------------------
	def show(self):
		cmds.setAttr(self.uuidNode+".visibility",1)

	#----------------------------------------------------------------------
	def hide(self):
		cmds.setAttr(self.uuidNode+".visibility",0)
