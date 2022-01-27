import sys, os
import maya.api.OpenMaya as OpenMaya
import maya.cmds as cmds
from . import API_Version_Convershions
from .. import Maya_Util_Classes
Maya_API_Callback_ID = Maya_Util_Classes.Maya_API_Callback_ID.Maya_API_Callback_ID
from . import Call_Back_Constants
#--------------------------
# PyNode Exceptions
#--------------------------
class Input_Convershion_Error(TypeError):
	_objectDescription = 'Object'
	def __init__(self, node=None):
		self.node = str(node)
	def __str__(self):
		msg = "Maya %s does not exist (or is not unique) And Could Not Be Converted To An MObject:" % (self._objectDescription)
		if self.node:
			msg += ": %r" % (self.node)
		return msg

#----------------------------------------------------------------------
def input_Node_Arg_Convershion(node_name):
	""""""
	try:
		nodeObj = API_Version_Convershions.to_New_MObject(node_name)
	except:
		raise Input_Convershion_Error(node=node_name)
	return nodeObj

## SCENE_MESSAGE_CALLBACK
#----------------------------------------------------------------------
def create_Scene_Message_Callback(message, fn, clientData=None,version=2):
	""""""

	try:
		callbackId = Call_Back_Constants.MSceneMessage.V2.addCallback(message, fn, clientData) 
		res = Maya_API_Callback_ID(callbackId)
	except:
		sys.stderr.write( "Failed to install Scene Message callback\n" )
		res = False
	return res
#----------------------------------------------------------------------
def create_Scene_After_Read_And_Record_Edits_Message_Callback(fn, clientData=None):
	""""""
	return create_Scene_Message_Callback(Call_Back_Constants.V2_Scene_Message_After_Flags.Scene_Read_And_Record_Edits, fn, clientData=clientData)
#----------------------------------------------------------------------
def create_Scene_After_Open_Message_Callback(fn, clientData=None):
	""""""
	return create_Scene_Message_Callback(Call_Back_Constants.V2_Scene_Message_After_Flags.Open, fn, clientData=clientData)
#----------------------------------------------------------------------
def create_Scene_After_New_Message_Callback(fn, clientData=None):
	""""""
	return create_Scene_Message_Callback(Call_Back_Constants.V2_Scene_Message_After_Flags.New, fn, clientData=clientData)
#----------------------------------------------------------------------
def create_Scene_After_Save_Message_Callback(fn, clientData=None):
	""""""
	return create_Scene_Message_Callback(Call_Back_Constants.V2_Scene_Message_After_Flags.Save, fn, clientData=clientData)
#----------------------------------------------------------------------
def create_Scene_After_Create_Ref_Message_Callback(fn, clientData=None):
	""""""
	return create_Scene_Message_Callback(Call_Back_Constants.V2_Scene_Message_After_Flags.CreateReference, fn, clientData=clientData)
#----------------------------------------------------------------------
def create_Scene_After_Remove_Ref_Message_Callback(fn, clientData=None):
	""""""
	return create_Scene_Message_Callback(Call_Back_Constants.V2_Scene_Message_After_Flags.RemoveReference, fn, clientData=clientData)
#----------------------------------------------------------------------
def create_Scene_After_Load_Ref_Message_Callback(fn, clientData=None):
	""""""
	return create_Scene_Message_Callback(Call_Back_Constants.V2_Scene_Message_After_Flags.LoadReference, fn, clientData=clientData)
#----------------------------------------------------------------------
def create_Scene_After_UnLoad_Ref_Message_Callback(fn, clientData=None):
	""""""
	return create_Scene_Message_Callback(Call_Back_Constants.V2_Scene_Message_After_Flags.UnloadReference, fn, clientData=clientData)
#----------------------------------------------------------------------
def create_Scene_Before_Open_Message_Callback(fn, clientData=None):
	""""""
	return create_Scene_Message_Callback(Call_Back_Constants.V2_Scene_Message_Before_Flags.Open, fn, clientData=clientData)
#----------------------------------------------------------------------
def create_Scene_Before_New_Message_Callback(fn, clientData=None):
	""""""
	return create_Scene_Message_Callback(Call_Back_Constants.V2_Scene_Message_Before_Flags.New, fn, clientData=clientData)
#----------------------------------------------------------------------
def create_Scene_Before_Save_Message_Callback(fn, clientData=None):
	""""""
	return create_Scene_Message_Callback(Call_Back_Constants.V2_Scene_Message_Before_Flags.Save, fn, clientData=clientData)
#----------------------------------------------------------------------
def create_Scene_Before_Create_Ref_Message_Callback(fn, clientData=None):
	""""""
	return create_Scene_Message_Callback(Call_Back_Constants.V2_Scene_Message_Before_Flags.CreateReference, fn, clientData=clientData)
#----------------------------------------------------------------------
def create_Scene_Before_Remove_Ref_Message_Callback(fn, clientData=None):
	""""""
	return create_Scene_Message_Callback(Call_Back_Constants.V2_Scene_Message_Before_Flags.RemoveReference, fn, clientData=clientData)
#----------------------------------------------------------------------
def create_Scene_Before_Load_Ref_Message_Callback(fn, clientData=None):
	""""""
	return create_Scene_Message_Callback(Call_Back_Constants.V2_Scene_Message_Before_Flags.LoadReference, fn, clientData=clientData)
#----------------------------------------------------------------------
def create_Scene_Before_UnLoad_Ref_Message_Callback(fn, clientData=None):
	""""""
	return create_Scene_Message_Callback(Call_Back_Constants.V2_Scene_Message_Before_Flags.UnloadReference, fn, clientData=clientData)
#----------------------------------------------------------------------
def create_Scene_Check_Message_Callback(message, fn, clientData=None):
	""""""
	try:
		callbackId = Call_Back_Constants.MSceneMessage.V2.addCheckCallback(message, fn, clientData) 
		res = Maya_API_Callback_ID(callbackId)
	except:
		sys.stderr.write( "Failed to install Scene Message callback\n" )
		res = False
	return res
#----------------------------------------------------------------------
def create_Scene_New_Check_Message_Callback(fn, clientData=None):
	""""""
	res = create_Scene_Check_Message_Callback(Call_Back_Constants.V2_Scene_Message_Checks_Flags.NewCheck, fn, clientData)
	return res
#----------------------------------------------------------------------
def create_Scene_Open_Check_Message_Callback(fn, clientData=None):
	""""""
	res = create_Scene_Check_Message_Callback(Call_Back_Constants.V2_Scene_Message_Checks_Flags.OpenCheck, fn, clientData)
	return res
#----------------------------------------------------------------------
def create_Scene_Save_Check_Message_Callback(fn, clientData=None):
	""""""
	res = create_Scene_Check_Message_Callback(Call_Back_Constants.V2_Scene_Message_Checks_Flags.SaveCheck, fn, clientData)
	return res


#----------------------------------------------------------------------
def create_Event_Callback(eventName, fn, clientData=None):
	"""
	the callback function takes the following parameters:
		clientData  : User defined data passed to the callback function
	"""
	try:
		callbackId  = OpenMaya.MEventMessage.addEventCallback(eventName, fn, clientData)
		res = Maya_API_Callback_ID(callbackId)
	except:
		sys.stderr.write( "Failed to install %s Event callback\n" % eventName )
		res = False
	return res
########################################################################
class Event_Callback_Creators:
	""""""
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_ActiveViewChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("ActiveViewChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_ChannelBoxLabelSelected_Callback(fn, clientData=None):
		res = create_Event_Callback("ChannelBoxLabelSelected", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_ColorIndexChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("ColorIndexChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_CurveRGBColorChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("CurveRGBColorChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_DagObjectCreated_Callback(fn, clientData=None):
		res = create_Event_Callback("DagObjectCreated", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_DisplayColorChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("DisplayColorChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_DisplayPreferenceChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("DisplayPreferenceChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_DisplayRGBColorChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("DisplayRGBColorChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_DragRelease_Callback(fn, clientData=None):
		res = create_Event_Callback("DragRelease", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_LiveListChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("LiveListChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_MenuModeChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("MenuModeChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_ModelPanelSetFocus_Callback(fn, clientData=None):
		res = create_Event_Callback("ModelPanelSetFocus", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_NameChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("NameChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_NewSceneOpened_Callback(fn, clientData=None):
		res = create_Event_Callback("NewSceneOpened", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_PostSceneRead_Callback(fn, clientData=None):
		res = create_Event_Callback("PostSceneRead", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_PostSceneSegmentChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("PostSceneSegmentChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_PostToolChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("PostToolChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_PreFileNewOrOpened_Callback(fn, clientData=None):
		res = create_Event_Callback("PreFileNewOrOpened", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_RebuildUIValues_Callback(fn, clientData=None):
		res = create_Event_Callback("RebuildUIValues", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_RecentCommandChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("RecentCommandChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_Redo_Callback(fn, clientData=None):
		res = create_Event_Callback("Redo", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_SceneImported_Callback(fn, clientData=None):
		res = create_Event_Callback("SceneImported", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_SceneOpened_Callback(fn, clientData=None):
		res = create_Event_Callback("SceneOpened", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_SceneSaved_Callback(fn, clientData=None):
		res = create_Event_Callback("SceneSaved", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_SceneSegmentChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("SceneSegmentChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_SelectModeChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("SelectModeChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_SelectPreferenceChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("SelectPreferenceChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_SelectPriorityChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("SelectPriorityChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_SelectTypeChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("SelectTypeChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_SelectionChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("SelectionChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_SequencerActiveShotChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("SequencerActiveShotChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_SetModified_Callback(fn, clientData=None):
		res = create_Event_Callback("SetModified", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_ToolChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("ToolChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_ToolDirtyChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("ToolDirtyChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_Undo_Callback(fn, clientData=None):
		res = create_Event_Callback("Undo", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_UvTileProxyDirtyChangeTrigger_Callback(fn, clientData=None):
		res = create_Event_Callback("UvTileProxyDirtyChangeTrigger", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_angularToleranceChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("angularToleranceChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_angularUnitChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("angularUnitChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_animLayerAnimationChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("animLayerAnimationChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_animLayerBaseLockChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("animLayerBaseLockChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_animLayerGhostChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("animLayerGhostChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_animLayerLockChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("animLayerLockChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_animLayerRebuild_Callback(fn, clientData=None):
		res = create_Event_Callback("animLayerRebuild", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_animLayerRefresh_Callback(fn, clientData=None):
		res = create_Event_Callback("animLayerRefresh", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_axisAtOriginChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("axisAtOriginChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_cameraChange_Callback(fn, clientData=None):
		res = create_Event_Callback("cameraChange", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_cameraDisplayAttributesChange_Callback(fn, clientData=None):
		res = create_Event_Callback("cameraDisplayAttributesChange", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_constructionHistoryChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("constructionHistoryChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_currentContainerChange_Callback(fn, clientData=None):
		res = create_Event_Callback("currentContainerChange", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_currentSoundNodeChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("currentSoundNodeChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_deleteAll_Callback(fn, clientData=None):
		res = create_Event_Callback("deleteAll", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_displayLayerAdded_Callback(fn, clientData=None):
		res = create_Event_Callback("displayLayerAdded", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_displayLayerChange_Callback(fn, clientData=None):
		res = create_Event_Callback("displayLayerChange", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_displayLayerDeleted_Callback(fn, clientData=None):
		res = create_Event_Callback("displayLayerDeleted", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_displayLayerManagerChange_Callback(fn, clientData=None):
		res = create_Event_Callback("displayLayerManagerChange", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_displayLayerVisibilityChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("displayLayerVisibilityChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_glFrameTrigger_Callback(fn, clientData=None):
		res = create_Event_Callback("glFrameTrigger", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_gridDisplayChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("gridDisplayChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_idle_Callback(fn, clientData=None):
		res = create_Event_Callback("idle", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_idleHigh_Callback(fn, clientData=None):
		res = create_Event_Callback("idleHigh", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_interactionStyleChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("interactionStyleChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_lightLinkingChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("lightLinkingChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_lightLinkingChangedNonSG_Callback(fn, clientData=None):
		res = create_Event_Callback("lightLinkingChangedNonSG", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_linearToleranceChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("linearToleranceChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_linearUnitChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("linearUnitChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_modelEditorChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("modelEditorChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_nurbsCurveRebuildPrefsChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("nurbsCurveRebuildPrefsChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_nurbsToPolygonsPrefsChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("nurbsToPolygonsPrefsChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_nurbsToSubdivPrefsChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("nurbsToSubdivPrefsChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_passContributionMapChange_Callback(fn, clientData=None):
		res = create_Event_Callback("passContributionMapChange", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_playbackRangeChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("playbackRangeChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_playbackRangeSliderChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("playbackRangeSliderChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_polyTopoSymmetryValidChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("polyTopoSymmetryValidChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_quitApplication_Callback(fn, clientData=None):
		res = create_Event_Callback("quitApplication", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_renderLayerChange_Callback(fn, clientData=None):
		res = create_Event_Callback("renderLayerChange", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_renderLayerManagerChange_Callback(fn, clientData=None):
		res = create_Event_Callback("renderLayerManagerChange", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_renderPassChange_Callback(fn, clientData=None):
		res = create_Event_Callback("renderPassChange", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_renderPassSetChange_Callback(fn, clientData=None):
		res = create_Event_Callback("renderPassSetChange", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_renderPassSetMembershipChange_Callback(fn, clientData=None):
		res = create_Event_Callback("renderPassSetMembershipChange", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_selectionConstraintsChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("selectionConstraintsChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_selectionPipelineChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("selectionPipelineChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_snapModeChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("snapModeChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_softSelectOptionsChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("softSelectOptionsChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_start3dPaintTool_Callback(fn, clientData=None):
		res = create_Event_Callback("start3dPaintTool", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_startColorPerVertexTool_Callback(fn, clientData=None):
		res = create_Event_Callback("startColorPerVertexTool", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_stop3dPaintTool_Callback(fn, clientData=None):
		res = create_Event_Callback("stop3dPaintTool", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_stopColorPerVertexTool_Callback(fn, clientData=None):
		res = create_Event_Callback("stopColorPerVertexTool", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_symmetricModellingOptionsChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("symmetricModellingOptionsChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_threadCountChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("threadCountChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_timeChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("timeChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_timeUnitChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("timeUnitChanged", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_undoSupressed_Callback(fn, clientData=None):
		res = create_Event_Callback("undoSupressed", fn, clientData)
		return res
	@staticmethod
	#----------------------------------------------------------------------
	def create_Event_workspaceChanged_Callback(fn, clientData=None):
		res = create_Event_Callback("workspaceChanged", fn, clientData)
		return res
#----------------------------------------------------------------------
def create_Timer_Callback(period_seconds, fn, clientData=None):
	"""
	the callback function takes the following parameters:
		elapsedTime : The elapsed time since this function was last called
		lastTime    : The execution time of this function the last time it was called
		clientData  : User defined data passed to the callback function
	"""
	try:
		callbackId  = OpenMaya.MTimerMessage.addTimerCallback(period_seconds, fn, clientData)
		res = Maya_API_Callback_ID(callbackId)
	except:
		sys.stderr.write( "Failed to install Timer callback\n" )
		res = False
	return res

#----------------------------------------------------------------------
def get_MDGMessage_Function():
	""""""
	
#----------------------------------------------------------------------
def create_NodeAdded_Callback(node_type, fn, clientData=None,version=2):
	try:
		api_fn = Call_Back_Constants.MDGMessage.get_MDGMessage_Function(version, "addNodeAddedCallback")
		callbackId  = api_fn(fn, node_type, clientData)
		res = Maya_API_Callback_ID(callbackId)
	except:
		sys.stderr.write( "Failed to install Node Added callback\n" )
		res = False
	return res
#----------------------------------------------------------------------
def create_NodeRemoved_Callback(node_type, fn, clientData=None, version=2):
	try:
		api_fn = Call_Back_Constants.MDGMessage.get_MDGMessage_Function(version, "addNodeRemovedCallback")
		callbackId = api_fn(fn, node_type, clientData)
		res = Maya_API_Callback_ID(callbackId)
	except:
		sys.stderr.write( "Failed to install Node Removed callback\n" )
		res = False
	return res
#----------------------------------------------------------------------
def create_Name_Changed_Callback(node_name, fn, clientData=None):
	"""
	the callback function takes the following parameters:
		node       : the node
		prevName   : the previous name of the node
		clientData : User defined data passed to the callback function
	"""
	try:
		nodeObj = input_Node_Arg_Convershion(node_name)
		callbackId = OpenMaya.MNodeMessage.addNameChangedCallback(nodeObj, fn, clientData)
		res = Maya_API_Callback_ID(callbackId)
	except:
		sys.stderr.write( "Failed to install Name Changed callback\n" )
		res = False
	return res
#----------------------------------------------------------------------
def create_Attribute_Changed_Callback(node_name, fn, clientData=None):
	"""
	the callback function takes the following parameters:
		msg        : the kind of attribute change triggering the callback
		plug       : the node's plug where the connection changed
		otherPlug  : the plug opposite the node's plug where the connection changed
		clientData : User defined data passed to the callback function
	"""
	try:
		nodeObj = input_Node_Arg_Convershion(node_name)
		callbackId = OpenMaya.MNodeMessage.addAttributeChangedCallback(nodeObj, fn, clientData)
		res = Maya_API_Callback_ID(callbackId)
	except:
		sys.stderr.write( "Failed to install Attribute Changed callback\n" )
		res = False
	return res
#----------------------------------------------------------------------
def create_Attribute_Added_Or_Removed_Callback(node_name, fn, clientData=None):
	"""
	the callback function takes the following parameters:
		msg        : the kind of attribute change triggering the callback
		plug       : the node's plug where the connection changed
		clientData : User defined data passed to the callback function
	"""
	try:
		nodeObj = input_Node_Arg_Convershion(node_name)
		callbackId = OpenMaya.MNodeMessage.addAttributeAddedOrRemovedCallback(nodeObj, fn, clientData)
		res = Maya_API_Callback_ID(callbackId)
	except:
		sys.stderr.write( "Failed to install Attribute Added Or Removed callback\n" )
		res = False
	return res
#----------------------------------------------------------------------
def create_Node_About_To_Delete_Callback(node_name, fn, clientData=None):
	"""
	the callback function takes the following parameters:
		node       : the node that will be deleted
		modifier   : DG modifier used to delete the node
		clientData : User defined data passed to the callback function
	"""
	try:
		nodeObj = input_Node_Arg_Convershion(node_name)
		callbackId = OpenMaya.MNodeMessage.addNodeAboutToDeleteCallback(nodeObj, fn, clientData)
		res = Maya_API_Callback_ID(callbackId)
	except:
		sys.stderr.write( "Failed to install Node About To Delete callback\n" )
		res = False
	return res
#----------------------------------------------------------------------
def create_Node_Pre_Removal_Callback(node_name, fn, clientData=None):
	"""
	the callback function takes the following parameters:
		node       : the node that is being deleted
		clientData : User defined data passed to the callback function
	"""

	try:
		nodeObj = input_Node_Arg_Convershion(node_name)
		callbackId = OpenMaya.MNodeMessage.addNodePreRemovalCallback(nodeObj, fn, clientData)
		res = Maya_API_Callback_ID(callbackId)
	except:
		sys.stderr.write( "Failed to install Node Pre Removal callback\n" )
		res = False
	return res
#----------------------------------------------------------------------
def create_Node_About_To_Delete_Callback(node_name, fn, clientData=None):
	"""
	the callback function takes the following parameters:
		node       : the node that is being deleted
		modifier   : DG modifier used to delete the node
		clientData : User defined data passed to the callback function
	"""
	try:
		nodeObj = input_Node_Arg_Convershion(node_name)
		callbackId = OpenMaya.MNodeMessage.addNodeAboutToDeleteCallback(nodeObj, fn, clientData)
		res = Maya_API_Callback_ID(callbackId)
	except:
		sys.stderr.write( "Failed to install Node About To Delete callback\n" )
		res = False
	return res
#----------------------------------------------------------------------
def create_Node_Dirty_Plug_Callback(node_name, fn, clientData=None):
	"""
	the callback function takes the following parameters:
		node       : The node that has become dirty
		plug       : The plug on the node that has become dirty
		clientData : User defined data passed to the callback function
	"""
	try:
		nodeObj = input_Node_Arg_Convershion(node_name)
		callbackId = OpenMaya.MNodeMessage.addNodeDirtyPlugCallback(nodeObj, fn, clientData)
		res = Maya_API_Callback_ID(callbackId)
	except:
		sys.stderr.write( "Failed to install Node Dirty Plug callback\n" )
		res = False
	return res
#----------------------------------------------------------------------
def create_Node_Dirty_Callback(node_name, fn, clientData=None):
	"""
	the callback function takes the following parameters:
		node       : The node that has become dirty
		clientData : User defined data passed to the callback function
	"""	
	try:
		nodeObj = input_Node_Arg_Convershion(node_name)
		callbackId = OpenMaya.MNodeMessage.addNodeDirtyCallback(nodeObj, fn, clientData)
		res = Maya_API_Callback_ID(callbackId)
	except:
		sys.stderr.write( "Failed to install Node Dirty callback\n" )
		res = False
	return res
#----------------------------------------------------------------------
def create_Command_Callback(fn, cmd_name, clientData=None):
	"""
		This method registers a callback for command messages that are
		issued every time a MEL command is executed. It is only called
		when actual commands are executed and not when scripts are
		executed.
		
		NOTE: Setting up a callback using this method will
		degrade the performance of Maya since the installed callback will be
		invoked repeatedly as MEL operations are processed.
		
		 * function - callable which will be passed
					  a string containing the MEL command being executed,
					  and the clientData object
		 * clientData - User defined data passed to the callback function
	"""	
	try:
		callbackId = OpenMaya.MCommandMessage.addCommandCallback(fn, clientData)
		res = Maya_API_Callback_ID(callbackId)
	except:
		sys.stderr.write( "Failed to install Command callback\n" )
		res = False
	return res
#----------------------------------------------------------------------
def create_Command_Output_Callback(fn, clientData=None):
	"""
	This method registers a callback for whenever MEL commands generate
	output such as that which is printed into the command window.
	
	 * function - callable which will be passed a string containing the MEL command being executed,
	   a MessageType constant (see class docs for a list)
	   indicating the message type and the clientData object
	 * clientData - User defined data passed to the callback function
	"""	
	try:
		callbackId = OpenMaya.MCommandMessage.addCommandOutputCallback(fn, clientData)
		res = Maya_API_Callback_ID(callbackId)
	except:
		sys.stderr.write( "Failed to install Command Output callback\n" )
		res = False
	return res
#----------------------------------------------------------------------
def create_Command_Output_Filter_Callback(fn, clientData=None):
	"""
	This method registers a callback for whenever MEL commands generate
	output such as that which is printed into the command window.
	
	Returning True in the callback will filter the output from the
	script editor and command line., returning False will keep the output.
	
	 * function - callable which will be passed
	              a string containing the MEL command being executed
				  a MessageType constant indicating the message type
				  and the clientData object
	 * clientData - User defined data passed to the callback function
	"""	
	try:
		callbackId = OpenMaya.MCommandMessage.addCommandOutputFilterCallback(fn, clientData)
		res = Maya_API_Callback_ID(callbackId)
	except:
		sys.stderr.write( "Failed to install Command Output callback\n" )
		res = False
	return res
#----------------------------------------------------------------------
def create_Mel_Proc_Callback(fn, clientData=None):
	"""
	This method registers a callback that is executed every time a MEL
	procedure is run. The callback will be executed once when the procedure
	is about to be executed, and again when it has exited. If a non-existent
	procedure is called the callback will be called once for entry but there
	will be no call on exit.
	
	The callback cannot be registered multiple times.
	To register a new callback function for this,
	please de-register the original callback first
	
	NOTE: Setting up a callback using this method can potentially degrade the
	      performance of Maya since the installed callback will be invoked
	      repeatedly as MEL procedures are executed.
	
	 * function - callable which will be passed
	              a string containing the name of the procedure being invoked,
				  an integer indicating the ID for the procedure's invocation,
				  a bool set to True if the procedure is being entered false otherwise,
				  a ProcType constant indicating the type of call this is (MEL proc or MEL command)
				  and the clientData object
	   ProcType constant can take the folowing values:
		 kMELProc
		 kMELCommand
	 * clientData - User defined data passed to the callback function
	"""	
	try:
		callbackId = OpenMaya.MCommandMessage.addProcCallback(fn, clientData)
		res = Maya_API_Callback_ID(callbackId)
	except:
		sys.stderr.write( "Failed to install Mel Proc callback\n" )
		res = False
	return res
