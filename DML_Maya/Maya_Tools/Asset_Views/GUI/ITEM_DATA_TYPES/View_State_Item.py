
import base64
import DML_Tools.Maya.DML_Maya
import DML_Tools.DML_PYQT
DML_PYQT = DML_Tools.DML_PYQT
DML_Maya = DML_Tools.Maya.DML_Maya
Node_Messages = DML_Maya.Maya_Utils.API_Callback_Builders.Call_Back_Constants.Node_Messages
import maya.cmds as cmds
import maya.api.OpenMaya as OM
from . import Maya_Node_Item
from ... import CallBack_Data_Storage

if False:
	from ...Custom_Nodes.DML_Asset_Views_View_State import Asset_Views_View_State
	import DML_Tools.Maya.Maya_Tools.Asset_Views.GUI.ITEM_DATA_TYPES.Maya_Node_Item
	DML_Tools.Maya.Maya_Tools.Asset_Views.GUI.ITEM_DATA_TYPES.Maya_Node_Item.Maya_Node_Data_Model_Item

########################################################################
class View_State_Item_Data(Maya_Node_Item.Maya_Node_Item_Data):
	#----------------------------------------------------------------------
	def __init__(self,maya_node,**kwargs):
		"""
		Params: Name: Type
		------------------------------
			| **maya_node** : **DML_Asset_Views_View_State**
		
		Optional Params: Name: Type: Default
		------------------------------------
			| **tree_item** : *Base_Model_Item* : None
			| **selectable** : *bool* : True
			| **enabled** : *bool* : True
			| **editable** : *bool* : True
			| **dragable** : *bool* : False
			| **dropable** : *bool* : False
			| **checkable** : *bool* : False
			| **checked** : *bool* : False
			| **font_family** : *str* : None
			| **font_size** : *int* : None
			| **size_hint** : *QSize* : None
			| **status_tip** : *str* : None
			| **tool_tip** : *str* : None
			| **brush** : *QBrush* : None
			| **icon_visable** : *bool* : False
			| **icon_color** : *GlobalColor* : None
			| **background_color** : *GlobalColor* : None
			| **foreground_color** : *GlobalColor* : None
		"""
		super(View_State_Item_Data, self).__init__(maya_node,**kwargs)
		
		if False:
			self.internal_data = Asset_Views_View_State()
	#----------------------------------------------------------------------
	def _fn_get_display_name_value(self):
		return self.internal_data.get_View_Name()
	#----------------------------------------------------------------------
	def _fn_set_display_name_value(self, value):
		if not isinstance(value,basestring):
			raise ValueError("input value must be an instance of basestring and a %r was given" % type(value))
		self.internal_data.set_View_Name(value)

########################################################################
class Item_Members_Changed_Callback(object):
	""""""

	def __init__(self,model_item):
		"""Constructor"""
		# Used To Check If The Action Needed To Taken Has Allready Been Set To Run
		# I am doing it this way because I don't need to update this model item every time 
		# a membership changes only once after all modifcation in maya are done
		self.qued = False
		
		self.main_window      = model_item.model.parentWidget()
		self.model_item       = model_item
		self.obj_set          = self.model_item.get_Maya_Node().object_set
		self.cashed           = self.obj_set.members()
		self.added_items      = []
		self.removed_items    = []
		self.DependencyNode_Fn = OM.MFnDependencyNode()
		self.cashed_set       = set(self.cashed)
		if False:
			isinstance(self.cashed,list)
			isinstance(self.cashed_set,set)
			isinstance(self.current_members,list)
			isinstance(self.current_members_set,set)
	#----------------------------------------------------------------------
	def __call__(self,msg,plug,otherPlug,clientData):
		"""
		the callback function takes the following parameters:
			msg        : the kind of attribute change triggering the callback
			plug       : the node's plug where the connection changed
			otherPlug  : the plug opposite the node's plug where the connection changed
			clientData : User defined data passed to the callback function
		"""
		if plug.partialName() == 'dsm':
			
			if Node_Messages.Was_Connection_Made(msg) or Node_Messages.Was_Connection_Broken(msg):
				
				if not self.qued:
					cmds.evalDeferred(self.action,lowestPriority=True)
					self.qued = True
				
				if Node_Messages.Was_Connection_Made(msg):
					item = DML_Maya.dml.to_DML_Node(otherPlug.node())
					Maya_Node_Item.Maya_Node_Data_Model_Item(item,model=self.model_item.model,parent_item=self.model_item)
					
				elif Node_Messages.Was_Connection_Broken(msg):
					self.DependencyNode_Fn.setObject(otherPlug.node())
					child = self.model_item.find_child(self.DependencyNode_Fn.uuid().asString(), role=self.model_item.ID_ROLE.INTERNAL_ID)
					if child is not None:
						self.model_item.removeChild(child)
	#----------------------------------------------------------------------
	def action(self):
		self.qued = False
		try:
			self.update_Model_Editor()
		except:
			pass
	#----------------------------------------------------------------------
	def update_Model_Editor(self):
		""""""
		if self.main_window.Model_Editor.get_Active_Object_Set() == self.obj_set:
			self.main_window.Model_Editor.refresh_Active_Object_Set()

########################################################################
class On_Maya_Object_Pre_Removal_Callback(object):
	""""""

	def __init__(self,model_item):
		"""Constructor"""
		# Used To Check If The Action Needed To Taken Has Allready Been Set To Run
		# I am doing it this way because I don't need to update this model item every time 
		# a membership changes only once after all modifcation in maya are done
		self.qued = False
		
		self.main_window      = model_item.model.parentWidget()
		self.model_item       = model_item
	#----------------------------------------------------------------------
	def __call__(self,node,clientData):
		CallBack_Data_Storage.Callbacks_Collection_Storage.remove_Per_Tree_Item_Callbacks(self.model_item)
		self.model_item.parentItem.removeChild(self.model_item)


########################################################################
class View_State_Data_Model_Item(Maya_Node_Item.Maya_Node_Data_Model_Item):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,internal_item,**kwargs):
		"""
		Params: Name: Type
		------------------------------
			| **internal_item** : *DML_Asset_Views_View_State*
			
		Optional Params: Name: Type: Default
		------------------------------------
			| **model** : *Data_Model* : None
			| **parent_item** : *Base_Model_Item* : None
			| **selectable** : *bool* : True
			| **enabled** : *bool* : True
			| **editable** : *bool* : True
			| **dragable** : *bool* : False
			| **dropable** : *bool* : False
			| **checkable** : *bool* : False
			| **checked** : *bool* : False
			| **font_family** : *str* : None
			| **font_size** : *int* : None
			| **size_hint** : *QSize* : None
			| **status_tip** : *str* : None
			| **tool_tip** : *str* : None
			| **brush** : *QBrush* : None
			| **icon_visable** : *bool* : False
			| **icon_color** : *GlobalColor* : None
			| **background_color** : *GlobalColor* : None
			| **foreground_color** : *GlobalColor* : None
		"""
		internal_item = View_State_Item_Data(internal_item)
		super(View_State_Data_Model_Item,self).__init__(internal_item,**kwargs)
		self.DependencyNode_Fn = OM.MFnDependencyNode()
		self.model_editor_refresh_qued = False
		if internal_item.internal_data.plug_thumbnail_icon.value != "" and internal_item.internal_data.plug_thumbnail_icon.value != None:
			decoded_data = base64.b64decode(internal_item.internal_data.plug_thumbnail_icon.value)
			pix = DML_PYQT.QPixmap()
			pix.loadFromData(decoded_data)
			icon = DML_PYQT.QIcon(pix)
			self.setData(True,0,role=self.ID_ROLE.ICON_VISABLE)
			self.setData(icon,role=self.ID_ROLE.ICON_COLOR)
		
		self.rebuild_Children()
		
	#----------------------------------------------------------------------
	def Register_Node_Callbacks(self):
		""""""
		maya_node = self.get_Maya_Node()
		maya_objset = maya_node.object_set
		cbs = []
		cbs.append(DML_Tools.DML_Maya.Maya_Utils.API_Callback_Builders.create_Attribute_Changed_Callback(maya_objset.apiMObject, self.On_Object_Set_Members_Changed_Callback))
		return cbs
	#----------------------------------------------------------------------
	def get_Maya_Node(self):
		"""Returns The DML_Maya_Node assigned to this model item"""
		data = self.get_internal_Data(0)
		if False:
			isinstance(data,Asset_Views_View_State)
		return data
	#----------------------------------------------------------------------
	def rebuild_Children(self):
		""""""
		super(View_State_Data_Model_Item,self).rebuild_Children()
		for node in self.get_Maya_Node().get_Nodes():
			Maya_Node_Item.Maya_Node_Data_Model_Item(node,model=self.model,parent_item=self)
	#----------------------------------------------------------------------
	def On_Object_Set_Members_Changed_Callback(self,msg,plug,otherPlug,clientData):
		"""
		the callback function takes the following parameters:
			msg        : the kind of attribute change triggering the callback
			plug       : the node's plug where the connection changed
			otherPlug  : the plug opposite the node's plug where the connection changed
			clientData : User defined data passed to the callback function
		"""
		if plug.partialName() == 'dsm':
			
			if Node_Messages.Was_Connection_Made(msg) or Node_Messages.Was_Connection_Broken(msg):
				
				if not self.model_editor_refresh_qued:
					cmds.evalDeferred(self.update_Model_Editor,lowestPriority=True)
					self.model_editor_refresh_qued = True
				
				if Node_Messages.Was_Connection_Made(msg):
					item = DML_Maya.dml.to_DML_Node(otherPlug.node())
					Maya_Node_Item.Maya_Node_Data_Model_Item(item,model=self.model,parent_item=self)
					
				elif Node_Messages.Was_Connection_Broken(msg):
					self.DependencyNode_Fn.setObject(otherPlug.node())
					child = self.find_child(self.DependencyNode_Fn.uuid().asString(), role=self.ID_ROLE.INTERNAL_ID)
					if child is not None:
						self.removeChild(child)

	#----------------------------------------------------------------------
	def update_Model_Editor(self):
		""""""
		self.model_editor_refresh_qued = False
		try:
			with DML_Maya.MayaSkipUndoChunk():
				model_editor = self.model.parentWidget().Model_Editor
				if model_editor.get_Active_Object_Set() == self.get_Maya_Node().object_set:
					model_editor.refresh_Active_Object_Set()
		except:
			pass