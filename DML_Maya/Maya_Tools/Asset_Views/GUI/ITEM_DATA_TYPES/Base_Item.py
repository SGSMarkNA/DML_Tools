

import DML_Tools.DML_PYQT.BASE_CLASS_DEFINITIONS.ABSTRACT_ITEM_MODEL_TYPES
ABSTRACT_ITEM_MODEL_TYPES = DML_Tools.DML_PYQT.BASE_CLASS_DEFINITIONS.ABSTRACT_ITEM_MODEL_TYPES

import DML_Tools.DML_PYQT
DML_PYQT = DML_Tools.DML_PYQT

import DML_Tools.Maya.DML_Maya
DML_Maya = DML_Tools.Maya.DML_Maya

if False:
	import DML_PYQT
	import DML_PYQT.BASE_CLASS_DEFINITIONS.ABSTRACT_ITEM_MODEL_TYPES as ABSTRACT_ITEM_MODEL_TYPES

Item_Data_Roles = ABSTRACT_ITEM_MODEL_TYPES.Item_Data_Roles.Base_Item_Data_Roles

########################################################################
class Item_Data(ABSTRACT_ITEM_MODEL_TYPES.Internal_Item_Data):
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		"""
		Params: Name: Type: Default
		------------------------------
			| **internal_data** : *any* : None
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
			| **display_name** : *str* : None
			| **background_color** : *GlobalColor* : None
			| **foreground_color** : *GlobalColor* : None
		"""
		super(Item_Data, self).__init__(*args,**kwargs)

########################################################################
class Model_Item(ABSTRACT_ITEM_MODEL_TYPES.Base_Model_Item):
	""""""
	ID_ROLE = Item_Data_Roles
	#----------------------------------------------------------------------
	def __init__(self, model=None, parent_item=None, items=[], column_count=1):
		"""
		Params: Name: Type: Default
		------------------------------
			| **internal_data** : *any* : None
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
			| **display_name** : *str* : None
			| **background_color** : *GlobalColor* : None
			| **foreground_color** : *GlobalColor* : None
		"""
		super(Model_Item, self).__init__(model=model, parent_item=parent_item, items=items, column_count=column_count)