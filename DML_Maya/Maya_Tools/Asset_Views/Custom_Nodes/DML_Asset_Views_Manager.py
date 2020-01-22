import maya.cmds as cmds
import DML_Tools.Maya.DML_Maya as DML_Maya

from DML_Asset_Views_View_State_Collections import Asset_Views_View_State_Collections

########################################################################
class Asset_Views_Manager(DML_Maya.Maya_Nodes.Network):
	RETURN_OVERIDE_CHECK_TYPE = "network"
	#----------------------------------------------------------------------
	@classmethod
	def _overide_Return_Check(cls,node):
		""""""
		return cmds.attributeQuery( 'dmlAssetViewsManager', node=node, exists=True )
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		self.addAttr('dmlAssetViewsManager', dt="string",hidden=True)
		self.plg_state_collections        = self.addAttr('stateCollections', at="message")
		self.plg_camera                   = self.addAttr('camera', at="message",writable=True,readable=False)
		
		if not self.plg_camera.isConnected:
			view = DML_Maya.Maya_Nodes.Camera(name="DML_Asset_View_Camera")
			self.plg_camera.value = view.message
		#if not self.plg_state_object_set.isConnected:
			#object_set = Asset_Views_View_State_Object_Set(empty=True)
			#object_set.plg_view_state.value = self.plg_state_object_set
		self.camera.visibility.value = 0
		if not self.plg_state_collections.isConnected:
			self.state_collections = Asset_Views_View_State_Collections(name=self.name + "_Collections")
			self.state_collections.plg_manager.value = self.plg_state_collections
			self.state_collections.rename("View_State_Collections")
		self.lockNode()	
		if False:
			isinstance(self.collections,Asset_Views_View_State_Collections)
			isinstance(self.camera,DML_Maya.Maya_Nodes.Camera)
	#----------------------------------------------------------------------
	@property
	def collections(self):
		""""""
		res = self.plg_state_collections.destination_nodes()
		if len(res):
			return res[0]
		else:
			return None
		
	#----------------------------------------------------------------------
	@property
	def camera(self):
		""""""
		res = self.plg_camera.source_node()
		return res