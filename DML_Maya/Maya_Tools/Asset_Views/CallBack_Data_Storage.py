import sys
import types
import maya.api.OpenMaya as OM

_modual_name = "DML_ASSET_VIEWS_CALLBACK_IDS"

#----------------------------------------------------------------------
def name_To_MObject(mobject):
	""""""
	res = None
	if not isinstance(mobject,OM.MObject):
		if not isinstance(mobject,str):
			raise ValueError("input must be a MObject or string")
		sel_list = OM.MSelectionList()
		sel_list.add(mobject)
		mobject = sel_list.getDependNode(0)	
	res = mobject
	isinstance(mobject,OM.MObject)
	return res
#----------------------------------------------------------------------
def name_To_Depend_Function(mobject):
	""""""
	mobject = name_To_MObject(mobject)
	res  = OM.MFnDependencyNode(mobject)
	return res
#----------------------------------------------------------------------
def name_To_Uuid(mobject):
	""""""
	fn  = name_To_Depend_Function(mobject)
	res = fn.uuid()
	isinstance(res,OM.MUuid)
	return res

########################################################################
class Callbacks_Collection_Storage(object):
	""""""
	MODUAL_NAME = "DML_ASSET_VIEWS_CALLBACK_IDS"
	_SCENE_IS_BEING_CLOSED = False
	#----------------------------------------------------------------------
	@staticmethod
	def Initialize_Callbacks_Modual():
		""""""
		if not Callbacks_Collection_Storage.Is_Initialized():
			modual = dict()
			modual["SCENE_CALLBACK_IDS"]    = []
			modual["PER_NODE_CALLBACK_IDS"] = {}
			sys.modules[Callbacks_Collection_Storage.MODUAL_NAME] = modual
	#----------------------------------------------------------------------
	@staticmethod
	def Re_Initialize_Callbacks_Modual():
		""""""
		if not Callbacks_Collection_Storage.Is_Initialized():
			Callbacks_Collection_Storage.Initialize_Callbacks_Modual()
		else:
			modual = dict()
			modual["SCENE_CALLBACK_IDS"] = []
			modual["PER_NODE_CALLBACK_IDS"] = {}
			sys.modules[Callbacks_Collection_Storage.MODUAL_NAME] = modual
	#----------------------------------------------------------------------
	@staticmethod
	def Is_Initialized():
		""""""
		return Callbacks_Collection_Storage.MODUAL_NAME in sys.modules
	#----------------------------------------------------------------------
	@staticmethod
	def get_Callbacks_Modual():
		""""""
		Callbacks_Collection_Storage.Initialize_Callbacks_Modual()
		res = sys.modules[Callbacks_Collection_Storage.MODUAL_NAME]
		isinstance(res,dict)
		return res
	#----------------------------------------------------------------------
	@staticmethod
	def get_Scene_Callback_Ids_Modual():
		""""""
		modual = Callbacks_Collection_Storage.get_Callbacks_Modual()
		res = modual["SCENE_CALLBACK_IDS"]
		isinstance(res,list)
		return res
	#----------------------------------------------------------------------
	@staticmethod
	def get_Per_Node_Callback_Ids_Modual():
		""""""
		modual = Callbacks_Collection_Storage.get_Callbacks_Modual()
		res = modual["PER_NODE_CALLBACK_IDS"]
		isinstance(res,dict)
		return res
	#----------------------------------------------------------------------
	@staticmethod
	def add_Per_Node_Callbacks(tree_item,mobject):
		""""""
		uid = name_To_Uuid(mobject)
		modual = Callbacks_Collection_Storage.get_Per_Node_Callback_Ids_Modual()
		
		cbs    = tree_item.Register_Node_Callbacks()
		
		if not isinstance(cbs,list):
			cbs = [cbs]
		if not uid.asString() in modual:
			modual[uid.asString()] = cbs
		else:
			modual[uid.asString()].extend(cbs)
	#----------------------------------------------------------------------
	@staticmethod
	def remove_Per_Node_Callbacks(mobject):
		""""""
		uid    = name_To_Uuid(mobject)
		modual = Callbacks_Collection_Storage.get_Per_Node_Callback_Ids_Modual()
		
		if uid.asString() in modual:
			del modual[uid.asString()]
	#----------------------------------------------------------------------
	@staticmethod
	def add_Scene_Callback_Ids(ids):
		""""""
		res = Callbacks_Collection_Storage.get_Scene_Callback_Ids_Modual()
		if not isinstance(ids,list):
			ids = [ids]
		res.extend(ids)
	#----------------------------------------------------------------------
	@staticmethod
	def clear_Scene_Callback_Ids():
		""""""
		modual = Callbacks_Collection_Storage.get_Callbacks_Modual()
		del modual["SCENE_CALLBACK_IDS"]
		modual["SCENE_CALLBACK_IDS"] = []
	#----------------------------------------------------------------------
	@staticmethod
	def clear_Per_Node_Callbacks():
		""""""
		modual = Callbacks_Collection_Storage.get_Callbacks_Modual()
		del modual["PER_NODE_CALLBACK_IDS"]
		modual["PER_NODE_CALLBACK_IDS"] = {}

Callbacks_Collection_Storage.Initialize_Callbacks_Modual()