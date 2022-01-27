import maya.cmds as cmds
import DML_Tools.Maya.DML_Maya as DML_Maya

from .DML_Asset_Views_View_State import Asset_Views_View_State

if False:
	from .DML_Asset_Views_View_State_Collections import Asset_Views_View_State_Collections
########################################################################
class Asset_Views_View_State_Collection(DML_Maya.Maya_Nodes.Network):
	RETURN_OVERIDE_CHECK_TYPE = "network"
	#----------------------------------------------------------------------
	@classmethod
	def _overide_Return_Check(cls,node):
		""""""
		return cmds.attributeQuery( 'dmlAssetViewsViewStateCollection', node=node, exists=True )
	#----------------------------------------------------------------------
	@classmethod
	def createNode(cls,*args,**kwargs):
		""""""
		if not "name" in kwargs or kwargs.get("name") == None:
			kwargs["name"] = "View_State_Collection"
		res = DML_Maya.Maya_Nodes.Network.createNode(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		self.addAttr('dmlAssetViewsViewStateCollection', dt="string",hidden=True)
		self.plg_state_Collections = self.addAttr('stateCollections', at="message",writable=True,readable=False)
		self.plg_view_states       = self.addAttr('viewStates', at="message")
		self.plg_name              = self.addAttr('name', dt="string")
		self.lockNode()
		if not self.plg_view_states.isConnected:
			default_state = self.add_View_State()
			default_state.rename("Defalut_View_State")
			default_state.set_View_Name(default_state.nice_name)
		
		if False:
			self.view_states = []
	#----------------------------------------------------------------------
	def get_State_Collections(self):
		""""""
		res = self.plg_state_Collections.source_node()
		if False:
			isinstance(res,Asset_Views_View_State_Collections)
		return res
	#----------------------------------------------------------------------
	@property
	def collection_name(self):
		return self.plg_name.value
	#----------------------------------------------------------------------
	@collection_name.setter
	def collection_name(self,val):
		self.plg_name.value = val
		self.rename(val)
	#----------------------------------------------------------------------
	def add_View_State(self,name=None):
		""""""
		view_state = Asset_Views_View_State(name=name)
		view_state.plg_state_Collection.value = self.plg_view_states
		return view_state
	#----------------------------------------------------------------------
	def get_View_State(self,arg):
		""""""
		res = None
		if isinstance(arg,int):
			if len(self) > arg:
				res = self.plg_view_states.destination_nodes()[arg]
			else:
				raise IndexError("The input index is larger then the number of states")
		elif isinstance(arg,str):
			for state in self:
				isinstance(state,Asset_Views_View_State)
				if state.nice_name == arg or state.plg_name.value == arg:
					res = state
		isinstance(res,Asset_Views_View_State)
		return res
	#----------------------------------------------------------------------
	def get_View_States(self):
		""""""
		return self.plg_view_states.destination_nodes()
	#----------------------------------------------------------------------
	view_states = property(get_View_States)
	#----------------------------------------------------------------------
	def __len__(self):
		""""""
		return len(self.plg_view_states.destination_nodes())
	#----------------------------------------------------------------------
	def __iter__(self):
		""""""
		for state in self.view_states:
			yield state
		