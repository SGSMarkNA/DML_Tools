
from . import Base_Item
import DML_Tools.Maya.DML_Maya
DML_Maya = DML_Tools.Maya.DML_Maya

from ..UI_Callbacks import Callbacks_Collection_Storage
if False:
	import Base_Item


########################################################################
class Maya_Node_Item_Data(Base_Item.Item_Data):
	#----------------------------------------------------------------------
	def __init__(self,maya_node,**kwargs):
		"""
		Params: Name: Type
		------------------------------
			| **maya_node** : *DML_Node or valid maya object name*
		
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
		# Force The Input To A DML_Node 
		maya_node = DML_Maya.dml.to_DML_Node(maya_node)
		# Check To Make Sure The Input Was A Maya Node
		if not isinstance(maya_node,DML_Maya.Maya_Nodes.Base_Nodes.API_Node.DML_Node):
			raise ValueError("The input was not a valid maya object {}".format(maya_node))
		# set the internal_data key value to the input maya_node arg
		kwargs["internal_data"] = maya_node
		super(Maya_Node_Item_Data, self).__init__(**kwargs)
		if False:
			self.internal_data = DML_Maya.Maya_Nodes.Dependency_Node()
	#----------------------------------------------------------------------
	def data(self,role=Base_Item.Item_Data_Roles.DISPLAY):
		""""""
		if role == self.ID_ROLE.INTERNAL_ID:
			return self.internal_data.uuid
		else:
			return super(Maya_Node_Item_Data, self).data(role=role)
	#----------------------------------------------------------------------
	def _fn_get_display_name_value(self):
		return self.internal_data.nice_name
	#----------------------------------------------------------------------
	def _fn_set_display_name_value(self, value):
		if not isinstance(value,basestring):
			raise ValueError("input value must be an instance of basestring and a %r was given" % type(value))
		self.internal_data.rename(value)
		
########################################################################
class Maya_Node_Data_Model_Item(Base_Item.Model_Item):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,internal_item,**kwargs):
		"""
		Params: Name: Type
		------------------------------
			| **internal_item** : *DML_Node or valid maya object name*
			
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
		# retrive and remove key values relative to the data model item
		model       = kwargs.pop("model", None)
		parent_item = kwargs.pop("parent_item", None)
		items       = []
		# Do To This Class will have many Subclass the input may
		# not be a maya node but a instance of a subclass of Maya_Node_Item_Data
		# if it is then just use it and bypass the creation of a Maya_Node_Item_Data
		if issubclass(type(internal_item),Maya_Node_Item_Data):
			items.append(internal_item)
		else:
			items.append(Maya_Node_Item_Data(internal_item,**kwargs))
		super(Maya_Node_Data_Model_Item,self).__init__(model=model, parent_item=parent_item, items=items)
		if hasattr(self,"Register_Node_Callbacks"):
			Callbacks_Collection_Storage.add_Per_Node_Callbacks(self, self.get_Maya_Node().apiMObject)
			
	#----------------------------------------------------------------------
	def Unregister_Node_Callbacks(self):
		""""""
		if hasattr(self,"Register_Node_Callbacks"):
			Callbacks_Collection_Storage.remove_Per_Node_Callbacks(self.get_Maya_Node().apiMObject)
			
	#----------------------------------------------------------------------
	def get_Maya_Node(self):
		"""Returns The DML_Maya_Node assigned to this model item"""
		data = self.get_internal_Data(0)
		isinstance(data,DML_Maya.Maya_Nodes.Dag_Node)
		return data