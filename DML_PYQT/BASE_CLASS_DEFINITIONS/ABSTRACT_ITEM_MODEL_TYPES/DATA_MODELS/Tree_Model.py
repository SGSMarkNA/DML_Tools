
from .... import QT
from ....BASE_CLASS_DEFINITIONS.QT_SUBCLASS import Mime_Data
from ..DATA_TYPES import Model_Items,Item_Data_Storage
from ..Item_Data_Roles import Base_Item_Data_Roles



########################################################################
class TreeModel(QT.QAbstractItemModel):
	def __init__(self, parent=None, root_item=None, headers=[]):
		super(TreeModel, self).__init__(parent)

		if len(headers) == 0:
			headers.append("First Name")
			headers.append("Last Name")
		if root_item is None:
			root_item = Model_Items.Root_Model_Item(self, headers=headers)

		self.rootItem = root_item
	# #----------------------------------------------------------------------
	# def canFetchMore(self, parent):
		# """"""
		# return True
	# #----------------------------------------------------------------------
	# def fetchMore(self, parent):
		# """"""
		# return True
	#----------------------------------------------------------------------
	def parentWidget(self):
		return QT.QObject.parent(self)

	def columnCount(self, parent):
		""""""
		if parent.isValid():
			return parent.internalPointer().column_Count
		else:
			return self.rootItem.column_Count
	#----------------------------------------------------------------------
	def data(self, index, role):
		if not index.isValid():
			return None
		item = index.internalPointer()
		if role == Base_Item_Data_Roles.INTERNAL_DATA:
			res = item
		else:
			try:
				res = item.data(index.column(),role)
			except:
				res = item.data(role)
		return res
	#----------------------------------------------------------------------
	def setData(self, index, value, role):
		if not index.isValid():
			return True
		item = index.internalPointer()
		try:
			res = item.setData(value, index.column(),role)
		except:
			res =  item.setData(role,value)
		# try:
			# self.dataChanged.emit(index, index, role)
		# except:
			# self.dataChanged.emit(index, index)
		return True
	#----------------------------------------------------------------------
	def flags(self, index):
		if not index.isValid():
			return QT.Qt.NoItemFlags
		item = index.internalPointer()
		isinstance(item, Model_Items.Base_Model_Item)
		try:
			return item.flags(column=index.column())
		except:
			return item.flags
	#----------------------------------------------------------------------
	def headerData(self, section, orientation, role):
		""""""
		if orientation == QT.Qt.Horizontal:
			if role in [Base_Item_Data_Roles.FOREGROUND, Base_Item_Data_Roles.BACKGROUND]:
				return None
			d = self.rootItem.data(section, role)
			if d is None and role == QT.Qt.DisplayRole:
				return str(section+1)
			return d
		if orientation == QT.Qt.Vertical and role == QT.Qt.DisplayRole:
			return str(section+1)
	#----------------------------------------------------------------------
	def index(self, row, column, parent):
		if not self.hasIndex(row, column, parent):
			return QT.QModelIndex()

		if not parent.isValid():
			parentItem = self.rootItem
		else:
			parentItem = parent.internalPointer()

		childItem = parentItem.child(row)
		try:
			return self.createIndex(row, column, childItem)
		except:
			print("Can Not Create Index")

		if childItem:
			return self.createIndex(row, column, childItem)
		else:
			return QT.QModelIndex()
	#----------------------------------------------------------------------
	def getItem(self, index):
		if index.isValid():
			item = index.internalPointer()
			if item:
				return item

		return self.rootItem
	#----------------------------------------------------------------------
	def item_From_Index(self,index):
		return self.getItem(index)
	#----------------------------------------------------------------------
	def indexFromItem(self, item):
		root_index = self.index(0, 0, QT.QModelIndex())
		row_path = [item.row]
		current_item = item.parent
		if not hasattr(current_item, "row"):
			return root_index
		if item == self.rootItem:
			return root_index
		while current_item != self.rootItem:
			row_path.append(current_item.row)
			current_item = current_item.parent
		row_path.reverse()
		current_index = root_index.sibling(row_path.pop(0), 0)
		for row in row_path:
			current_index = current_index.child(row, 0)
		return current_index
	#----------------------------------------------------------------------
	def indexFromItemData(self, itemData):
		isinstance(itemData, Item_Data_Storage.Internal_Item_Data)
		item = itemData.tree_item
		root_index = self.index(0, 0, QT.QModelIndex())
		row_path = [item.row]
		current_item = item.parent
		if not hasattr(current_item, "row"):
			return root_index
		if item == self.rootItem:
			return root_index
		while current_item != self.rootItem:
			row_path.append(current_item.row)
			current_item = current_item.parent
		#row_path = row_path[:-1]
		row_path.reverse()
		#row_path.append(item.row)
		current_index = root_index.sibling(row_path.pop(0), itemData.column)
		for row in row_path:
			current_index = current_index.child(row, itemData.column)
		return current_index
	#----------------------------------------------------------------------
	def parent(self, index):
		if not index.isValid():
			return QT.QModelIndex()

		childItem = index.internalPointer()
		isinstance(childItem, Model_Items.Base_Model_Item)
		parentItem = childItem.parentItem
		if childItem == self.rootItem:
			return QT.QModelIndex()
		if parentItem == self.rootItem or parentItem is None:
			return QT.QModelIndex()

		return self.createIndex(parentItem.row, 0, parentItem)
	#----------------------------------------------------------------------
	def rowCount(self, parent):
		if parent.column() > 0:
			return 0

		if not parent.isValid():
			parentItem = self.rootItem
		else:
			parentItem = parent.internalPointer()

		return parentItem.child_Count
	#----------------------------------------------------------------------
	def removeRows(self, position, rows, parent=QT.QModelIndex()):
		parentItem = self.getItem(parent)
		items      = [parentItem.childItems[position]]
		success    = parentItem.removeChildren(items)
		return success
	#----------------------------------------------------------------------
	def insertRows(self, position, items, parent=QT.QModelIndex()):
		parentItem = self.getItem(parent)
		count = len(items)
		success = parentItem.insertChildren(position, items)
		return success
	#----------------------------------------------------------------------
	def insertColumns(self, position, items, parent=QT.QModelIndex()):
		parentItem = self.getItem(parent)
		count = len(items)
		success = parentItem.insertColumns(position, items)
		return success
	#----------------------------------------------------------------------
	def _recursive_Item_Data_Collector(self, item, temp_storage=[]):
		""""""
		item_data = {}
		item_data["column_items"] = item._get_Current_State()
		item_data["child_items"] = []
		temp_storage.append(item_data)
		for child in item.childItems:
			self._recursive_Item_Data_Collector(child, item_data["child_items"])
	#----------------------------------------------------------------------
	def collect_tree_data(self):
		return self.rootItem.get_Current_Tree_State()
	##----------------------------------------------------------------------
	#def restore_tree_data(self, collection):
		#self.remove_Row_Item_By_Index(self.rootItem.index)
		#self.rootItem = Standered_Data_Items.Tree_Item(self, items=collection['column_items'])
		#self.rootItem.load_child_data(collection["child_items"])
	#----------------------------------------------------------------------
	def dropMimeData(self, data, action, row, column, parent):
		""""""
		if isinstance(data, Mime_Data.MimeData):
			items       = data.row_items
			indices     = data.indexs
			destination = data.drop_destination
			source      = data.drag_source
			if action == QT.Constants.DropActions.MoveAction:
				destination_item = self.getItem(data.dest_item)
				if destination.DropIndicatorPosition ==  QT.Constants.AbstractItemView.DropIndicatorPosition.OnItem:
					items.reverse()
					destination_item.moveChildren(items, destination_item.child_Count)
				else:
					if destination.DropIndicatorPosition ==  QT.Constants.AbstractItemView.DropIndicatorPosition.AboveItem:
						items.reverse()
					destination_item.parentItem.moveChildren(items, destination_item.row)
			elif action == QT.Constants.DropActions.CopyAction:
				new_items = []
				for item in items:
					if not item.parentItem in items:
						new_items.append(item)
				destination_item = self.getItem(data.dest_item)
				for item in new_items:
					item.clone(destination_item)
		return False
	#----------------------------------------------------------------------
	def mimeData(self, indexs):
		""""""
		row_items = []
		for index in indexs:
			index = index.sibling(index.row(), 0)
			item = self.getItem(index)
			if not item in row_items:
				row_items.append(item)
		data = super(TreeModel, self).mimeData(indexs)
		mimedata = Mime_Data.MimeData(row_items, indexs, data)
		return mimedata
	#----------------------------------------------------------------------
	def supportedDropActions(self): 
		""""""
		return QT.Constants.DropActions.CopyAction | QT.Constants.DropActions.MoveAction | QT.Constants.DropActions.LinkAction
	#----------------------------------------------------------------------
	def create_Sibling_Item(self, index):
		"""Create A New Item Under The Same Parent of the input index"""
		item = self.getItem(index)
		_item_datas = [Item_Data_Storage.Standered_Item_Data(display_name="New Item")]
		_item_datas.extend([Item_Data_Storage.Standered_Item_Data(display_name=None) for i in range(self.rootItem.column_Count-1)])
		new_item = Model_Items.Base_Model_Item(items=_item_datas)
		if not item.isRoot:
			item.insertChild(item.row, new_item)
	#----------------------------------------------------------------------
	def create_Child_Item(self, parent_Index):
		"""Create A New Item Under The input parent_Index"""
		item = self.getItem(parent_Index)
		_item_datas = [Item_Data_Storage.Standered_Item_Data(display_name="New Item")]
		_item_datas.extend([Item_Data_Storage.Standered_Item_Data() for i in range(self.rootItem.column_Count-1)])
		new_item = Model_Items.Base_Model_Item(parent_item=item, items=_item_datas)
		return new_item
	#----------------------------------------------------------------------
	def create_Column_Item(self, index, item_data=None):
		"""Create A New Item Under The input parent_Index"""
		item = self.getItem(index)
		if item_data is None or not isinstance(item_data, Item_Data_Storage.Standered_Item_Data):
			item_data = Item_Data_Storage.Standered_Item_Data(display_name="Column")
		item.appendColumn(item_data)
	#----------------------------------------------------------------------
	def add_Header_item_Item(self,item_data=None):
		"""Create A New Item Under The input parent_Index"""
		item = self.rootItem
		if item_data is None or not isinstance(item_data, Item_Data_Storage.Standered_Item_Data):
			item_data = Item_Data_Storage.Standered_Item_Data(display_name="Column")
		item.appendColumn(item_data)
	#----------------------------------------------------------------------
	def remove_Row_Item_By_Index(self, index):
		"""Remove The Item And All Its Children For The input index"""
		item = self.getItem(index)
		item.parentItem.removeChild(item)