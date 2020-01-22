
import DML_Tools.Maya.DML_Maya
DML_Maya = DML_Tools.Maya.DML_Maya

from . import Maya_Node_Item
from . import View_State_Collections_Item
if False:
	from ...Custom_Nodes.DML_Asset_Views_Manager import Asset_Views_Manager




########################################################################
class View_State_Manager_Item_Data(Maya_Node_Item.Maya_Node_Item_Data):
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
		super(View_State_Manager_Item_Data, self).__init__(maya_node,**kwargs)
		
		if False:
			self.internal_data = Asset_Views_Manager()
		
########################################################################
class View_State_Manager_Data_Model_Item(Maya_Node_Item.Maya_Node_Data_Model_Item):
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
		internal_item = View_State_Manager_Item_Data(internal_item,**kwargs)
		super(View_State_Manager_Data_Model_Item,self).__init__(internal_item,**kwargs)
		self.rebuild_Children()
	#----------------------------------------------------------------------
	def rebuild_Children(self):
		""""""
		super(View_State_Manager_Data_Model_Item,self).rebuild_Children()
		maya_node = self.get_Maya_Node()
		View_State_Collections_Item.View_State_Collections_Data_Model_Item(maya_node.collections, model=self.model,parent_item=self)
	#----------------------------------------------------------------------
	def get_Maya_Node(self):
		"""Returns The DML_Maya_Node assigned to this model item"""
		data = self.get_internal_Data(0)
		if False:
			isinstance(data,Asset_Views_Manager)
		return data

