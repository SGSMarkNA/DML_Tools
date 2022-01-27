
import DML_Tools.Maya.DML_Maya
from . import Custom_Nodes

#----------------------------------------------------------------------
def view_Manager_Create(name=None):
	""""""
	if name == None:
		name = "DML_AV_Manger"
	manager = Custom_Nodes.Asset_Views_Manager(name="DML_NEW_NODE_CREATED_PLACE_HOLDER_NAME")
	manager.rename(name)
	#manager.state_collections.add_View_State_Collection
	return manager
#----------------------------------------------------------------------
def list_View_Managers():
	""""""
	items = [plg.node for plg in DML_Tools.Maya.DML_Maya.dml.ls("*.dmlAssetViewsManager")]
	return items
#----------------------------------------------------------------------
def list_View_Collection():
	""""""
	items = [plg.node for plg in DML_Tools.Maya.DML_Maya.dml.ls("*.dmlAssetViewsViewStateCollection")]
	return items
#----------------------------------------------------------------------
def list_View_Collections():
	""""""
	items = [plg.node for plg in DML_Tools.Maya.DML_Maya.dml.ls("*.dmlAssetViewsViewStateCollections")]
	return items
#----------------------------------------------------------------------
def list_View_States():
	""""""
	items = [plg.node for plg in DML_Tools.Maya.DML_Maya.dml.ls("*.dmlAssetViewsViewState")]
	return items
#----------------------------------------------------------------------
def list_View_State_ObjectSets():
	""""""
	items = [plg.node for plg in DML_Tools.Maya.DML_Maya.dml.ls("*.dmlAssetViewsViewStateObjectSet")]
	return items

#----------------------------------------------------------------------
def view_Collection_Create(manager,name=None):
	""""""
	if not isinstance(manager,Custom_Nodes.Asset_Views_Manager):
		raise ValueError("manager must be a DML_Asset_Views_Manager instance and a {} was give".format(type(manager)))
	
	if name == None:
		name = "DML_AV_VS_Collection"
		
	view_state_collection = Custom_Nodes.Asset_Views_View_State_Collection(name="DML_NEW_NODE_CREATED_PLACE_HOLDER_NAME")
	view_state_collection.rename(name)
	
	view_state_collection.plg_state_Collections.value = manager.collections.plg_state_Collections
	view_state_collection.plg_name.value = view_state_collection.nice_name
	
	return view_state_collection
#----------------------------------------------------------------------
def view_Collection_Delete(view_state_collection):
	""""""
	if not isinstance(view_state_collection,Custom_Nodes.Asset_Views_View_State_Collection):
		raise ValueError("view_state_collection must be a DML_Asset_Views_View_State_Collection instance and a {} was give".format(type(view_state_collection)))
	with DML_Tools.Maya.DML_Maya.MayaUndoChunk():
		for view_state in view_state_collection.view_states:
			view_State_Delete(view_state)
		view_state_collection.delete()
#----------------------------------------------------------------------
def view_State_Create(state_collection,name=None):
	""""""
	if not isinstance(state_collection,Custom_Nodes.Asset_Views_View_State_Collection):
		raise ValueError("manager must be a DML_Asset_Views_View_State_Collection instance and a {} was give".format(type(state_collection)))
	
	if name == None:
		name = "DML_AV_View_State"
	
	view_state = Custom_Nodes.Asset_Views_View_State(name="DML_NEW_NODE_CREATED_PLACE_HOLDER_NAME")
	view_state.rename(name)
	view_state.plg_state_Collection.value = state_collection.plg_view_states
	view_state.view_state_name = view_state.name
	return view_state
#----------------------------------------------------------------------
def view_State_Delete(view_state):
	""""""
	if not isinstance(view_state,Custom_Nodes.Asset_Views_View_State):
		raise ValueError("view_state must be a DML_Asset_Views_View_State instance and a {} was give".format(type(view_state)))
	with DML_Tools.Maya.DML_Maya.MayaUndoChunk():
		view_state.camera_view.delete()
		view_state.object_set.delete()
		view_state.delete()
#----------------------------------------------------------------------
def view_State_Get_Objects(view_state):
	""""""
	if not isinstance(view_state,Custom_Nodes.Asset_Views_View_State):
		raise ValueError("view_state must be a DML_Asset_Views_View_State instance and a {} was give".format(type(view_state)))
	res = view_state.get_Nodes()
	return res
#----------------------------------------------------------------------
def view_State_Add_Objects(view_state,*args):
	""""""
	if not isinstance(view_state,Custom_Nodes.Asset_Views_View_State):
		raise ValueError("view_state must be a DML_Asset_Views_View_State instance and a {} was give".format(type(view_state)))
	with DML_Tools.Maya.DML_Maya.MayaUndoChunk():
		res = view_state.add_Objects(*args)
	return res
#----------------------------------------------------------------------
def view_State_Remove_Objects(view_state,*args):
	""""""
	if not isinstance(view_state,Custom_Nodes.Asset_Views_View_State):
		raise ValueError("view_state must be a DML_Asset_Views_View_State instance and a {} was give".format(type(view_state)))
	with DML_Tools.Maya.DML_Maya.MayaUndoChunk():
		res = view_state.remove_Objects(*args)
	return res
#----------------------------------------------------------------------
def view_State_Update_Camera(view_state):
	""""""
	if not isinstance(view_state,Custom_Nodes.Asset_Views_View_State):
		raise ValueError("view_state must be a DML_Asset_Views_View_State instance and a {} was give".format(type(view_state)))
	view_state.update_Camera_View()
#----------------------------------------------------------------------
def view_State_Apply_Camera(view_state):
	""""""
	if not isinstance(view_state,Custom_Nodes.Asset_Views_View_State):
		raise ValueError("view_state must be a DML_Asset_Views_View_State instance and a {} was give".format(type(view_state)))
	view_state.apply_Camera_View()