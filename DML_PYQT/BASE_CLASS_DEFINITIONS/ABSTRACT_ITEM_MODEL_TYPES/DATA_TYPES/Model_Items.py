from .... import QT
Constants = QT.Constants
from . import Item_Data_Storage
from ..Item_Data_Roles import Base_Item_Data_Roles

if False:
	from ..DATA_MODELS import Tree_Model

########################################################################
class Base_Model_Item(object):
	ITEM_TYPE  = QT.userType_generator()
	ID_ROLES   = Base_Item_Data_Roles
	CHILDREN_CONTEXT, ITEMS_CONTEXT =  list(range(2))
	_Context_Attribute_Return = {CHILDREN_CONTEXT: "childItems", ITEMS_CONTEXT: "_column_items",}
	#----------------------------------------------------------------------
	def __init__(self, model=None, parent_item=None, items=[], column_count=1):
		self.parentItem    = parent_item
		self._column_items       = Item_Data_Storage.Column_Item_List(self)
		self.childItems          = []
		self._with_Context_Depth = 0
		self._model              = model
		isinstance(self.parentItem, Base_Model_Item)
		isinstance(self.column_items, Item_Data_Storage.Column_Item_List)

		if isinstance(items,list) and len(items):
			for i, column_item in enumerate(items):
				if isinstance(column_item, dict ):
					column_item = Item_Data_Storage.Internal_Item_Data(self, **column_item)
				elif hasattr(column_item, "tree_item" ):
					column_item.tree_item = self
				else:
					raise ValueError("index %i in items arg must be a instance of Tree_Item and a %r was found" % (i, type(column_item)) )
				self._column_items.items.append(column_item)
		elif isinstance(items,str):
			column_item = Item_Data_Storage.Internal_Item_Data(self,display_name=items)
			self._column_items.items.append(column_item)
		else:
			column_items = []
			for i in range(column_count):
				item = Item_Data_Storage.Internal_Item_Data(self)
				item.display_name = "column %i" % i
				self._column_items.items.append(item)

		if self.parentItem is not None:
			self.parentItem.appendChild(self)
		if False:
			isinstance(self.model, Tree_Model)
			isinstance(self.root_item, Base_Model_Item)
			isinstance(self.index, QT.QModelIndex)
			isinstance(self.parent, Base_Model_Item)
	#----------------------------------------------------------------------
	def __iter__(self):
		""""""
		for item in self.context_data:
			yield item
	#----------------------------------------------------------------------
	def flags(self, column=0):
		return self._column_items.get_Item_Flags(column)	
	#----------------------------------------------------------------------
	def data(self, column=0, role=Base_Item_Data_Roles.DISPLAY):
		return self._column_items.data(column, role)
	#----------------------------------------------------------------------
	def setData(self, value, column=0, role=Base_Item_Data_Roles.DISPLAY):
		return self._column_items.setData(value, column, role)
	#----------------------------------------------------------------------
	def _is_parent_in_list(self, list_of_parents):
		""""""
		for parent_item in self.all_parents:
			if parent_item in list_of_parents:
				return parent_item
		return False
	#----------------------------------------------------------------------
	def contains_Child(self, child_item):
		ac = self.all_childern
		if child_item in ac:
			return child_item
		return False
	#----------------------------------------------------------------------
	def insertChild(self, position, child_Item):
		isinstance(child_Item,Base_Model_Item)
		self.insertChildren(position, [child_Item])
	#----------------------------------------------------------------------
	def appendChild(self, child_Item):
		isinstance(child_Item,Base_Model_Item)
		self.insertChildren(self.child_Count, [child_Item])
	#----------------------------------------------------------------------
	def clone(self, destination):
		isinstance(destination,Base_Model_Item)
		cloned_item = Base_Model_Item(items=self._get_Current_State())
		destination.appendChild(cloned_item)
		for child in self.childItems:
			child.clone(cloned_item)
	#----------------------------------------------------------------------
	def appendColumn(self, item_data):
		isinstance(item_data,Item_Data_Storage.Internal_Item_Data)
		self.insertColumns(self.column_Count, [item_data])
	#----------------------------------------------------------------------
	def takeChildren(self, items):
		res = []
		if self.isRoot:
			parent_index = QT.QModelIndex()
			parentItem   = self
		else:
			parent_index = self.index
			parentItem   = self

		for item in items:
			position = item.row
			self.model.beginRemoveRows(parent_index, position, position)
			item = parentItem.childItems.pop(position)
			item.parentItem = None
			res.append(item)
			self.model.endRemoveRows()
		return res
	#----------------------------------------------------------------------
	def insertColumns(self, position, items):
		if not isinstance(items, list):
			return False
		if not len(items):
			return False

		if self.isRoot:
			parent_index = QT.QModelIndex()
		else:
			parent_index = self.index

		position = position if position > 0 else 0
		position = position if position <= self.column_Count else self.column_Count

		for item in items:
			self.model.beginInsertColumns(parent_index, position, position)
			item.tree_item = self
			self._column_items.items.insert(position, item)
			self.model.endInsertColumns()
			index =  self.model.indexFromItemData(item)
			try:
				self.model.dataChanged.emit(index, index, Base_Item_Data_Roles.DISPLAY)
			except:
				self.model.dataChanged.emit(index, index)
		return True
	#----------------------------------------------------------------------
	def removeColumns(self, items):
		res = []
		if not isinstance(items, list):
			return False
		if not len(items):
			return False

		if self.isRoot:
			parent_index = QT.QModelIndex()
		else:
			parent_index = self.index

		for item in items[::]:
			position = item.column
			self.model.beginRemoveColumns(parent_index, position, position)
			item = self._column_items.items.pop(position)
			self.model.endRemoveColumns()
			del item
		return True
	#----------------------------------------------------------------------
	def insertChildren(self, position, items):
		if not isinstance(items, list):
			return False
		if not len(items):
			return False

		if self.isRoot:
			parent_index = QT.QModelIndex()
		else:
			parent_index = self.index

		position = position if position > 0 else 0
		position = position if position <= self.child_Count else self.child_Count

		for item in items:
			self.model.beginInsertRows(parent_index, position, position)
			self.childItems.insert(position, item)
			item.parentItem = self
			self.model.endInsertRows()
		return True
	#----------------------------------------------------------------------
	def moveChildren(self, items, position):
		res = []
		if self.isRoot:
			parent_index = QT.QModelIndex()
			parentItem   = self
		else:
			parent_index = self.index
			parentItem   = self

		for item in items:
			child = item.parentItem.takeChildren([item])[0]
			self.insertChild(position, child)
		return True	
	#----------------------------------------------------------------------
	def moveChild(self, child, position):
		return self.moveChildren([child],position)
	#----------------------------------------------------------------------
	def removeChild(self, child_item):
		return self.removeChildren([child_item])	
	#----------------------------------------------------------------------
	def removeChildren(self, items):
		res = []
		if self.isRoot:
			parent_index = QT.QModelIndex()
			parentItem   = self
		else:
			parent_index = self.index
			parentItem   = self

		for item in items[::]:
			if hasattr(item, "Unregister_Node_Callbacks"):
				item.Unregister_Node_Callbacks()
				item.clear_Children()
			if hasattr(item, "row"):
				position = item.row
			else:
				position = item.index.row()
			self.model.beginRemoveRows(parent_index, position, position)
			item = parentItem.childItems.pop(position)
			self.model.endRemoveRows()
			
		return True
	#----------------------------------------------------------------------
	def clear_Children(self):
		""""""
		return self.removeChildren(self.childItems)
	#----------------------------------------------------------------------
	def rebuild_Children(self):
		"""clears and rebuilds This Model Items Children base implamentation just clears """
		self.clear_Children()
	#----------------------------------------------------------------------
	def child(self, row):
		child_item = self.childItems[row]
		isinstance(child_item, Base_Model_Item)
		return child_item
	#----------------------------------------------------------------------
	def find_child(self, value, column=0, role=Base_Item_Data_Roles.DISPLAY):
		res = None
		for child in self.all_childern:
			if child.data(column, role) == value:
				res = child
				break
		isinstance(res, Base_Model_Item)
		return res
	#----------------------------------------------------------------------
	def find_all_children(self, value, column=0, role=Base_Item_Data_Roles.DISPLAY):
		res = []
		for child in self.all_childern:
			if child.data(column, role) == value:
				res.append(child)
		return res
	#----------------------------------------------------------------------
	def get_internal_Data(self, column=0):
		""""""
		res = self.data(column=column, role=Base_Item_Data_Roles.INTERNAL_DATA)
		isinstance(res, Item_Data_Storage.Internal_Item_Data)
		return res
	#----------------------------------------------------------------------
	def set_internal_Data(self, value, column=0):
		""""""
		self.setData(value, column=column, role=Base_Item_Data_Roles.INTERNAL_DATA)
	#----------------------------------------------------------------------
	def _get_Current_State(self):
		""""""
		state =  self._column_items._get_Current_State()
		return state
	#----------------------------------------------------------------------
	def load_child_data(self, list_of_child_dicts):
		""""""
		for child_dict in list_of_child_dicts:
			data_items =  []
			for col_dict in child_dict["column_items"]:
				data_items.append(Item_Data_Storage.Internal_Item_Data(**col_dict))
			child_item = Base_Model_Item(parent_item=self, items=data_items)
			child_item.load_child_data(child_dict['child_items'])
	#----------------------------------------------------------------------
	def get_Current_Tree_State(self, collection={}):
		""""""
		item_data = {}
		item_data["column_items"] = self._get_Current_State()
		item_data["child_items"] = []
		if "child_items" in collection:
			collection["child_items"].append(item_data)
		for child in self.childItems:
			child.get_Current_Tree_State(item_data)
		return item_data
	#----------------------------------------------------------------------
	@property
	def column_items(self):
		""""""
		return self._column_items
	#----------------------------------------------------------------------
	@property
	def parent(self):
		return self.parentItem
	#----------------------------------------------------------------------
	@property
	def all_parents(self):
		res = []
		if self.isRoot:
			return res

		item = self
		while not item.isRoot:
			item = item.parentItem
			res.append(item)
		return res
	#----------------------------------------------------------------------
	@property
	def all_childern(self):
		def scan_childern(parent, item_list=[]):
			if parent.child_Count:
				item_list.extend(parent.childItems)
				for child in parent.childItems:
					scan_childern(child, item_list)
			return item_list
		res = []
		if not self.child_Count:
			return res
		res = scan_childern(self)
		return res
	#----------------------------------------------------------------------
	@property
	def row(self):
		if self.parentItem:
			return self.parentItem.childItems.index(self)
		return 0
	#----------------------------------------------------------------------
	@property
	def column_Count(self):
		return len(self._column_items.items)
	#----------------------------------------------------------------------
	@property
	def root_item(self):
		item = self
		while item.parentItem is not None:
			item = item.parentItem
		return item
	#----------------------------------------------------------------------
	@property
	def model(self):
		return self.root_item._model
	#----------------------------------------------------------------------
	@property
	def index(self):
		""""""
		return self.model.indexFromItem(self)
	#----------------------------------------------------------------------
	@property
	def child_Count(self):
		return len(self.childItems)
	@property
	#----------------------------------------------------------------------
	def current_context_state(self):
		""""""
		return self._with_Context_Depth
	@property
	#----------------------------------------------------------------------
	def context_data(self):
		""""""
		if self.current_context_state in list(self._Context_Attribute_Return.keys()):
			return getattr(self, self._Context_Attribute_Return[self.current_context_state])
		else:
			return self.childItems
	@property
	#----------------------------------------------------------------------
	def isRoot(self):
		""""""
		return self.root_item == self	
	#----------------------------------------------------------------------
	def __len__(self):
		""""""
		return len(self.childItems)
	
# ======================================================================
# DATA MODEL ROOT TREE ITEM
# ----------------------------------------------------------------------
# Synopsis:
#     This Is Special It Needs To Be The Root Of Any Data Model
#     Because All Elements Use It To Find Themself Within There Tree
# ======================================================================
########################################################################
class Root_Model_Item(Base_Model_Item):
	#----------------------------------------------------------------------
	def __init__(self, model, headers=[],column_Count=1):
		items = []
		if len(headers):
			for header in headers:
				if isinstance(header, str):
					item = Item_Data_Storage.Internal_Item_Data( tree_item=self, display_name=header)
				elif isinstance(header, dict):
					header["tree_item"] = self
					item = Item_Data_Storage.Internal_Item_Data(**header)
				elif isinstance(header,Item_Data_Storage.Internal_Item_Data):
					item = header
				else:
					raise ValueError("Incorrect Header Item Was Found %r" % header)
				items.append(item)
		else:
			for i in range(column_Count):
				item = Item_Data_Storage.Internal_Item_Data( self, display_name="Column %i" % (i+1))
				items.append(item)
		super(Root_Model_Item, self).__init__(model=model, items=items)