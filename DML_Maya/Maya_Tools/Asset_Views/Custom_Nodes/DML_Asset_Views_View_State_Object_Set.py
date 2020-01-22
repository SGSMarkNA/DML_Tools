import maya.cmds as cmds
import DML_Tools.Maya.DML_Maya as DML_Maya

if False:
	from DML_Asset_Views_View_State import Asset_Views_View_State

########################################################################
class Asset_Views_View_State_Object_Set(DML_Maya.Maya_Nodes.Object_Set):
	RETURN_OVERIDE_CHECK_TYPE = "objectSet"
	#----------------------------------------------------------------------
	@classmethod
	def _overide_Return_Check(cls,node):
		""""""
		return cmds.attributeQuery( 'dmlAssetViewsViewStateObjectSet', node=node, exists=True )
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		self.addAttr('dmlAssetViewsViewStateObjectSet', dt="string",hidden=True)
		self.plg_view_state = self.addAttr('viewState', at="message")
		self.lockNode()
		
	#----------------------------------------------------------------------
	def get_View_State(self):
		""""""
		res = self.plg_view_state.source_node()
		if False:
			isinstance(res,Asset_Views_View_State)
		return res