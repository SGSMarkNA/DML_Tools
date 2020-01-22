import maya.OpenMaya as V1_OM
import maya.api.OpenMaya as V2_OM
	
class MMessage(object):
	V1 = V1_OM.MMessage
	V2 = V2_OM.MMessage

class MSceneMessage(object):
	V1 = V1_OM.MSceneMessage
	V2 = V2_OM.MSceneMessage

class MNodeMessage(object):
	V1 = V1_OM.MNodeMessage
	V2 = V2_OM.MNodeMessage

class MCommandMessage(object):
	V1 = V1_OM.MCommandMessage
	V2 = V2_OM.MCommandMessage
	
class MDGMessage(object):
	V1 = V1_OM.MDGMessage
	V2 = V2_OM.MDGMessage
	#----------------------------------------------------------------------
	@classmethod
	def get_MDGMessage_Function(cls,version,fname):
		""""""
		if version == 2:
			api = cls.V2
		else:
			api = cls.V1
		function = getattr(api,fname)
		return function
	
########################################################################
class V1_Node_Message_Flages:
	AttributeAdded        = MNodeMessage.V1.kAttributeAdded
	AttributeArrayAdded   = MNodeMessage.V1.kAttributeArrayAdded
	AttributeArrayRemoved = MNodeMessage.V1.kAttributeArrayRemoved
	AttributeEval         = MNodeMessage.V1.kAttributeEval
	AttributeKeyable      = MNodeMessage.V1.kAttributeKeyable
	AttributeLocked       = MNodeMessage.V1.kAttributeLocked
	AttributeRemoved      = MNodeMessage.V1.kAttributeRemoved
	AttributeRenamed      = MNodeMessage.V1.kAttributeRenamed
	AttributeSet          = MNodeMessage.V1.kAttributeSet
	AttributeUnkeyable    = MNodeMessage.V1.kAttributeUnkeyable
	AttributeUnlocked     = MNodeMessage.V1.kAttributeUnlocked
	ConnectionBroken      = MNodeMessage.V1.kConnectionBroken
	ConnectionMade        = MNodeMessage.V1.kConnectionMade
	IncomingDirection     = MNodeMessage.V1.kIncomingDirection
	KeyChangeInvalid      = MNodeMessage.V1.kKeyChangeInvalid
	KeyChangeLast         = MNodeMessage.V1.kKeyChangeLast
	Last                  = MNodeMessage.V1.kLast
	MakeKeyable           = MNodeMessage.V1.kMakeKeyable
	OtherPlugSet          = MNodeMessage.V1.kOtherPlugSet
########################################################################
class V2_Node_Message_Flages:
	AttributeAdded        = MNodeMessage.V2.kAttributeAdded
	AttributeArrayAdded   = MNodeMessage.V2.kAttributeArrayAdded
	AttributeArrayRemoved = MNodeMessage.V2.kAttributeArrayRemoved
	AttributeEval         = MNodeMessage.V2.kAttributeEval
	AttributeKeyable      = MNodeMessage.V2.kAttributeKeyable
	AttributeLocked       = MNodeMessage.V2.kAttributeLocked
	AttributeRemoved      = MNodeMessage.V2.kAttributeRemoved
	AttributeRenamed      = MNodeMessage.V2.kAttributeRenamed
	AttributeSet          = MNodeMessage.V2.kAttributeSet
	AttributeUnkeyable    = MNodeMessage.V2.kAttributeUnkeyable
	AttributeUnlocked     = MNodeMessage.V2.kAttributeUnlocked
	ConnectionBroken      = MNodeMessage.V2.kConnectionBroken
	ConnectionMade        = MNodeMessage.V2.kConnectionMade
	IncomingDirection     = MNodeMessage.V2.kIncomingDirection
	KeyChangeInvalid      = MNodeMessage.V2.kKeyChangeInvalid
	KeyChangeLast         = MNodeMessage.V2.kKeyChangeLast
	Last                  = MNodeMessage.V2.kLast
	MakeKeyable           = MNodeMessage.V2.kMakeKeyable
	OtherPlugSet          = MNodeMessage.V2.kOtherPlugSet

########################################################################
class Node_Messages:
	AttributeAdded        = MNodeMessage.V2.kAttributeAdded
	AttributeArrayAdded   = MNodeMessage.V2.kAttributeArrayAdded
	AttributeArrayRemoved = MNodeMessage.V2.kAttributeArrayRemoved
	AttributeEval         = MNodeMessage.V2.kAttributeEval
	AttributeKeyable      = MNodeMessage.V2.kAttributeKeyable
	AttributeLocked       = MNodeMessage.V2.kAttributeLocked
	AttributeRemoved      = MNodeMessage.V2.kAttributeRemoved
	AttributeRenamed      = MNodeMessage.V2.kAttributeRenamed
	AttributeSet          = MNodeMessage.V2.kAttributeSet
	AttributeUnkeyable    = MNodeMessage.V2.kAttributeUnkeyable
	AttributeUnlocked     = MNodeMessage.V2.kAttributeUnlocked
	ConnectionBroken      = MNodeMessage.V2.kConnectionBroken
	ConnectionMade        = MNodeMessage.V2.kConnectionMade
	IncomingDirection     = MNodeMessage.V2.kIncomingDirection
	KeyChangeInvalid      = MNodeMessage.V2.kKeyChangeInvalid
	KeyChangeLast         = MNodeMessage.V2.kKeyChangeLast
	Last                  = MNodeMessage.V2.kLast
	MakeKeyable           = MNodeMessage.V2.kMakeKeyable
	OtherPlugSet          = MNodeMessage.V2.kOtherPlugSet
	#----------------------------------------------------------------------
	@classmethod
	def Was_Connection_Made(cls,msg):
		""""""
		return bool(msg & cls.ConnectionMade)
	#----------------------------------------------------------------------
	@classmethod
	def Was_Connection_Broken(cls,msg):
		""""""
		return bool(msg & cls.ConnectionBroken)
	#----------------------------------------------------------------------
	@classmethod
	def Was_Attribute_Set(cls,msg):
		""""""
		return bool(msg & cls.AttributeSet)
	#----------------------------------------------------------------------
	@classmethod
	def Was_Attribute_Unlocked(cls,msg):
		""""""
		return bool(msg & cls.AttributeUnlocked)
	#----------------------------------------------------------------------
	@classmethod
	def Was_Attribute_Locked(cls,msg):
		""""""
		return bool(msg & cls.AttributeLocked)
	#----------------------------------------------------------------------
	@classmethod
	def Was_Attribute_Added(cls,msg):
		""""""
		return bool(msg & cls.AttributeAdded)
	#----------------------------------------------------------------------
	@classmethod
	def Was_Attribute_Removed(cls,msg):
		""""""
		return bool(msg & cls.AttributeRemoved)
	#----------------------------------------------------------------------
	@classmethod
	def Was_Array_Attribute_Added(cls,msg):
		""""""
		return bool(msg & cls.AttributeArrayAdded)
	#----------------------------------------------------------------------
	@classmethod
	def Was_Array_Attribute_Removed(cls,msg):
		""""""
		return bool(msg & cls.AttributeArrayRemoved)
	#----------------------------------------------------------------------
	@classmethod
	def Is_Incoming_Connection(cls,msg):
		""""""
		return bool(msg & cls.IncomingDirection)
	#----------------------------------------------------------------------
	@classmethod
	def Was_Other_Plug_Set(cls,msg):
		""""""
		return bool(msg & cls.OtherPlugSet)
	#----------------------------------------------------------------------
	@classmethod
	def Was_Attribute_Evaluated(cls,msg):
		""""""
		return bool(msg & cls.AttributeEval)
	#----------------------------------------------------------------------
	@classmethod
	def Was_Attribute_Renamed(cls,msg):
		""""""
		return bool(msg & cls.AttributeRenamed)
	#----------------------------------------------------------------------
	@classmethod
	def Was_Attribute_Renamed(cls,msg):
		""""""
		return bool(msg & cls.AttributeRenamed)

########################################################################
class V1_Scene_Message_After_Flags:
	CreateReference               = MSceneMessage.V1.kAfterCreateReference
	Export                        = MSceneMessage.V1.kAfterExport
	ExportReference               = MSceneMessage.V1.kAfterExportReference
	Import                        = MSceneMessage.V1.kAfterImport
	ImportReference               = MSceneMessage.V1.kAfterImportReference
	LoadReference                 = MSceneMessage.V1.kAfterLoadReference
	New                           = MSceneMessage.V1.kAfterNew
	Open                          = MSceneMessage.V1.kAfterOpen
	PluginLoad                    = MSceneMessage.V1.kAfterPluginLoad
	PluginUnload                  = MSceneMessage.V1.kAfterPluginUnload
	RemoveReference               = MSceneMessage.V1.kAfterRemoveReference
	Save                          = MSceneMessage.V1.kAfterSave
	SoftwareFrameRender           = MSceneMessage.V1.kAfterSoftwareFrameRender
	SoftwareRender                = MSceneMessage.V1.kAfterSoftwareRender
	UnloadReference               = MSceneMessage.V1.kAfterUnloadReference
	Scene_Read_And_Record_Edits   = MSceneMessage.V1.kAfterSceneReadAndRecordEdits
########################################################################
class V2_Scene_Message_After_Flags:
	CreateReference               = MSceneMessage.V2.kAfterCreateReference
	Export                        = MSceneMessage.V2.kAfterExport
	ExportReference               = MSceneMessage.V2.kAfterExportReference
	Import                        = MSceneMessage.V2.kAfterImport
	ImportReference               = MSceneMessage.V2.kAfterImportReference
	LoadReference                 = MSceneMessage.V2.kAfterLoadReference
	New                           = MSceneMessage.V2.kAfterNew
	Open                          = MSceneMessage.V2.kAfterOpen
	PluginLoad                    = MSceneMessage.V2.kAfterPluginLoad
	PluginUnload                  = MSceneMessage.V2.kAfterPluginUnload
	RemoveReference               = MSceneMessage.V2.kAfterRemoveReference
	Save                          = MSceneMessage.V2.kAfterSave
	SoftwareFrameRender           = MSceneMessage.V2.kAfterSoftwareFrameRender
	SoftwareRender                = MSceneMessage.V2.kAfterSoftwareRender
	UnloadReference               = MSceneMessage.V2.kAfterUnloadReference
	Scene_Read_And_Record_Edits   = MSceneMessage.V2.kAfterSceneReadAndRecordEdits
########################################################################
class V1_Scene_Message_Before_Flags:
	CreateReference               = MSceneMessage.V1.kBeforeCreateReference
	Export                        = MSceneMessage.V1.kBeforeExport
	ExportReference               = MSceneMessage.V1.kBeforeExportReference
	Import                        = MSceneMessage.V1.kBeforeImport
	ImportReference               = MSceneMessage.V1.kBeforeImportReference
	LoadReference                 = MSceneMessage.V1.kBeforeLoadReference
	New                           = MSceneMessage.V1.kBeforeNew
	Open                          = MSceneMessage.V1.kBeforeOpen
	PluginLoad                    = MSceneMessage.V1.kBeforePluginLoad
	PluginUnload                  = MSceneMessage.V1.kBeforePluginUnload
	RemoveReference               = MSceneMessage.V1.kBeforeRemoveReference
	Save                          = MSceneMessage.V1.kBeforeSave
	SoftwareFrameRender           = MSceneMessage.V1.kBeforeSoftwareFrameRender
	SoftwareRender                = MSceneMessage.V1.kBeforeSoftwareRender
	UnloadReference               = MSceneMessage.V1.kBeforeUnloadReference
########################################################################
class V2_Scene_Message_Before_Flags:
	CreateReference               = MSceneMessage.V2.kBeforeCreateReference
	Export                        = MSceneMessage.V2.kBeforeExport
	ExportReference               = MSceneMessage.V2.kBeforeExportReference
	Import                        = MSceneMessage.V2.kBeforeImport
	ImportReference               = MSceneMessage.V2.kBeforeImportReference
	LoadReference                 = MSceneMessage.V2.kBeforeLoadReference
	New                           = MSceneMessage.V2.kBeforeNew
	Open                          = MSceneMessage.V2.kBeforeOpen
	PluginLoad                    = MSceneMessage.V2.kBeforePluginLoad
	PluginUnload                  = MSceneMessage.V2.kBeforePluginUnload
	RemoveReference               = MSceneMessage.V2.kBeforeRemoveReference
	Save                          = MSceneMessage.V2.kBeforeSave
	SoftwareFrameRender           = MSceneMessage.V2.kBeforeSoftwareFrameRender
	SoftwareRender                = MSceneMessage.V2.kBeforeSoftwareRender
	UnloadReference               = MSceneMessage.V2.kBeforeUnloadReference
########################################################################
class V1_Scene_Message_Checks_Flags:
	CreateReferenceCheck          = MSceneMessage.V1.kBeforeCreateReferenceCheck
	ExportCheck                   = MSceneMessage.V1.kBeforeExportCheck
	ImportCheck                   = MSceneMessage.V1.kBeforeImportCheck
	LoadReferenceCheck            = MSceneMessage.V1.kBeforeLoadReferenceCheck
	NewCheck                      = MSceneMessage.V1.kBeforeNewCheck
	OpenCheck                     = MSceneMessage.V1.kBeforeOpenCheck
	ReferenceCheck                = MSceneMessage.V1.kBeforeReferenceCheck
	SaveCheck                     = MSceneMessage.V1.kBeforeSaveCheck
########################################################################
class V2_Scene_Message_Checks_Flags:
	CreateReferenceCheck          = MSceneMessage.V2.kBeforeCreateReferenceCheck
	ExportCheck                   = MSceneMessage.V2.kBeforeExportCheck
	ImportCheck                   = MSceneMessage.V2.kBeforeImportCheck
	LoadReferenceCheck            = MSceneMessage.V2.kBeforeLoadReferenceCheck
	NewCheck                      = MSceneMessage.V2.kBeforeNewCheck
	OpenCheck                     = MSceneMessage.V2.kBeforeOpenCheck
	ReferenceCheck                = MSceneMessage.V2.kBeforeReferenceCheck
	SaveCheck                     = MSceneMessage.V2.kBeforeSaveCheck
########################################################################
class V1_Scene_Message_Flags:
	ExportStarted             = MSceneMessage.V1.kExportStarted
	Last                      = MSceneMessage.V1.kLast
	MayaExiting               = MSceneMessage.V1.kMayaExiting
	MayaInitialized           = MSceneMessage.V1.kMayaInitialized
	SceneUpdate               = MSceneMessage.V1.kSceneUpdate
	SoftwareRenderInterrupted = MSceneMessage.V1.kSoftwareRenderInterrupted
########################################################################
class V2_Scene_Message_Flags:
	ExportStarted             = MSceneMessage.V2.kExportStarted
	Last                      = MSceneMessage.V2.kLast
	MayaExiting               = MSceneMessage.V2.kMayaExiting
	MayaInitialized           = MSceneMessage.V2.kMayaInitialized
	SceneUpdate               = MSceneMessage.V2.kSceneUpdate
	SoftwareRenderInterrupted = MSceneMessage.V2.kSoftwareRenderInterrupted
########################################################################
class V1_Command_Message_Flags:
	History    = MCommandMessage.V1.kHistory
	Display    = MCommandMessage.V1.kDisplay
	Info       = MCommandMessage.V1.kInfo
	Warning    = MCommandMessage.V1.kWarning
	Error      = MCommandMessage.V1.kError
	Result     = MCommandMessage.V1.kResult
	MELCommand = MCommandMessage.V1.kMELCommand
	MELProc    = MCommandMessage.V1.kMELProc
	StackTrace = MCommandMessage.V1.kStackTrace
########################################################################
class V2_Command_Message_Flags:
	History    = MCommandMessage.V2.kHistory
	Display    = MCommandMessage.V2.kDisplay
	Info       = MCommandMessage.V2.kInfo
	Warning    = MCommandMessage.V2.kWarning
	Error      = MCommandMessage.V2.kError
	Result     = MCommandMessage.V2.kResult
	MELCommand = MCommandMessage.V2.kMELCommand
	MELProc    = MCommandMessage.V2.kMELProc
	StackTrace = MCommandMessage.V2.kStackTrace