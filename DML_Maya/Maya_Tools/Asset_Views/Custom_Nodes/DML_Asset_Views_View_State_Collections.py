
import maya.cmds as cmds
import DML_Tools.Maya.DML_Maya as DML_Maya
from .DML_Asset_Views_View_State_Collection import Asset_Views_View_State_Collection
if False:
	from .DML_Asset_Views_Manager import Asset_Views_Manager

########################################################################
class Asset_Views_View_State_Collections(DML_Maya.Maya_Nodes.Network):
	RETURN_OVERIDE_CHECK_TYPE = "network"
	#----------------------------------------------------------------------
	@classmethod
	def _overide_Return_Check(cls,node):
		""""""
		return cmds.attributeQuery( 'dmlAssetViewsViewStateCollections', node=node, exists=True )
	#----------------------------------------------------------------------
	@classmethod
	def createNode(cls,*args,**kwargs):
		""""""
		if not "name" in kwargs or kwargs.get("name") == None:
			kwargs["name"] = "View_State_Collections"
		res = DML_Maya.Maya_Nodes.Network.createNode(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		self.addAttr('dmlAssetViewsViewStateCollections', dt="string",hidden=True)
		self.plg_manager            = self.addAttr('manager', at="message",writable=True,readable=False)
		self.plg_state_Collections  = self.addAttr('stateCollections', at="message",writable=False,readable=True)
		self.lockNode()
		if not self.plg_state_Collections.isConnected:
			default_state = self.add_View_State_Collection(name=self.name.replace("_Collections","_Defalut_Collection"))
			default_state.rename("Defalut_Collection")
	#----------------------------------------------------------------------
	def add_View_State_Collection(self,name=None):
		""""""
		view_state_Collection = Asset_Views_View_State_Collection(name=name)
		view_state_Collection.plg_state_Collections.value = self.plg_state_Collections
		view_state_Collection.plg_name.value = view_state_Collection.nice_name
		return view_state_Collection 
	#----------------------------------------------------------------------
	def find_View_State_Collection(self,arg):
		""""""
		res = None
		if isinstance(arg,int):
			if len(self) > arg:
				res = self.plg_state_Collections.destination_nodes()[arg]
			else:
				raise IndexError("The input index is larger then the number of states")
		elif isinstance(arg,str):
			for collection in self:
				isinstance(collection,Asset_Views_View_State_Collection)
				if collection.nice_name == arg or collection.plg_name.value == arg:
					res = collection
		isinstance(res,Asset_Views_View_State_Collection)
		return res
	#----------------------------------------------------------------------
	def get_View_State_Collections(self):
		""""""
		return self.plg_state_Collections.destination_nodes()
	#----------------------------------------------------------------------
	def get_Manager(self):
		""""""
		res = self.plg_manager.source_node()
		if False:
			isinstance(res,Asset_Views_Manager)
		return res
	#----------------------------------------------------------------------
	view_state_collections = property(get_View_State_Collections)
	#----------------------------------------------------------------------
	def __len__(self):
		""""""
		return len(self.plg_state_Collections.destination_nodes())
	#----------------------------------------------------------------------
	def __iter__(self):
		""""""
		for item in self.view_state_collections:
			yield item
