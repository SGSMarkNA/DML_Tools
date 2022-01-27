
from . import Base_Item
import DML_Tools.Maya.DML_Maya
DML_Maya      = DML_Tools.Maya.DML_Maya
Node_Messages = DML_Maya.Maya_Utils.API_Callback_Builders.Call_Back_Constants.Node_Messages

from . import Maya_Node_Item
from . import View_State_Collection_Item
from ... import CallBack_Data_Storage

import maya.cmds as cmds
import maya.api.OpenMaya as OM
if False:
	from ...Custom_Nodes.DML_Asset_Views_View_State_Collections import Asset_Views_View_State_Collections
	

########################################################################
class View_State_Collections_Item_Data(Maya_Node_Item.Maya_Node_Item_Data):
	#----------------------------------------------------------------------
	def __init__(self,maya_node,**kwargs):
		"""
		Params: Name: Type
		------------------------------
			| **maya_node** : **valid maya object name**
		
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
		super(View_State_Collections_Item_Data, self).__init__(maya_node,**kwargs)
		
		if False:
			self.internal_data = Asset_Views_View_State_Collections()

########################################################################
class On_State_Collection_Added_Or_Removed_Callback(object):
	""""""
	def __init__(self,model_item):
		"""Constructor"""
		# Used To Check If The Action Needed To Taken Has Allready Been Set To Run
		# I am doing it this way because I don't need to update this model item every time 
		# a membership changes only once after all modifcation in maya are done
		self.qued = False
		isinstance(model_item,View_State_Collections_Data_Model_Item)
		self.main_window      = model_item.model.parentWidget()
		self.model_item       = model_item
		
	#----------------------------------------------------------------------
	def __call__(self,msg,plug,otherPlug,clientData):
		"""
		the callback function takes the following parameters:
			msg        : the kind of attribute change triggering the callback
			plug       : the node's plug where the connection changed
			otherPlug  : the plug opposite the node's plug where the connection changed
			clientData : User defined data passed to the callback function
		"""
		if plug.partialName() == "stateCollections":
			
			if Node_Messages.Was_Connection_Made(msg):
				fn  = OM.MFnDependencyNode(otherPlug.node())
				print(("View State Collecion {} Was Added To {}".format(fn.name(),clientData.name)))
				child_tree_item = self.model_item.find_child(fn.uuid().asString(), role=self.model_item.ID_ROLE.INTERNAL_ID)
				
				if child_tree_item is None:
					dml_node  = DML_Maya.dml.to_DML_Node(otherPlug.node())
					View_State_Collection_Item.View_State_Collection_Data_Model_Item(dml_node,model=self.model_item.model,parent_item=self.model_item)
				
			elif Node_Messages.Was_Connection_Broken(msg):
				fn  = OM.MFnDependencyNode(otherPlug.node())
				print(("View State Collecion {} Was Removed From {}".format(fn.name(),clientData.name)))
				
				child_tree_item = self.model_item.find_child(fn.uuid().asString(), role=self.model_item.ID_ROLE.INTERNAL_ID)
				
				if child_tree_item is not None:
					self.model_item.removeChild(child_tree_item)
	#----------------------------------------------------------------------
	def action(self):
		pass

		
########################################################################
class View_State_Collections_Data_Model_Item(Maya_Node_Item.Maya_Node_Data_Model_Item):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,internal_item,**kwargs):
		"""
		Params: Name: Type
		------------------------------
			| **internal_item** : *DML_Asset_Views_View_State or valid maya object name*
			
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
		internal_item = View_State_Collections_Item_Data(internal_item,**kwargs)
		super(View_State_Collections_Data_Model_Item,self).__init__(internal_item,**kwargs)
		self.rebuild_Children()
	#----------------------------------------------------------------------
	def Register_Node_Callbacks(self):
		""""""
		maya_node = self.get_Maya_Node()
		cbs = []
		cbs.append(DML_Tools.DML_Maya.Maya_Utils.API_Callback_Builders.create_Attribute_Changed_Callback(maya_node.apiMObject, On_State_Collection_Added_Or_Removed_Callback(self), clientData=maya_node))
		return cbs
	#----------------------------------------------------------------------
	def rebuild_Children(self):
		""""""
		super(View_State_Collections_Data_Model_Item,self).rebuild_Children()
		for node in self.get_Maya_Node().get_View_State_Collections():
			View_State_Collection_Item.View_State_Collection_Data_Model_Item(node,model=self.model,parent_item=self)
	#----------------------------------------------------------------------
	def get_Maya_Node(self):
		"""Returns The DML_Maya_Node assigned to this model item"""
		data = self.get_internal_Data(0)
		if False:
			isinstance(data,Asset_Views_View_State_Collections)
		return data

