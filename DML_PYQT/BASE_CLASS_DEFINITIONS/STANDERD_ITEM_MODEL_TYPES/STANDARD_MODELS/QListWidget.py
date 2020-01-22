
from .... import QT

class Standard_QListWidget(QT.QListWidget):
	''''''
	Item_Data_Roles     = QT.Constants.ItemDataRole
	Item_View_Constants = QT.Constants.AbstractItemView
	
	def __init__(self,*args,**kwargs):
		''''''
		super(Standard_QListWidget,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def count(self):
		"""
		This property holds the number of items in the list including any hidden items..
		"""
		res = super(Standard_QListWidget,self).count()
		
		return res
	#----------------------------------------------------------------------
	def currentItem(self):
		"""
		Returns the current item.
		"""
		res = super(Standard_QListWidget,self).currentItem()
		isinstance(res,QT.QListWidgetItem)
		return res
	#----------------------------------------------------------------------
	def currentRow(self):
		"""
		This property holds the row of the current item..
		Depending on the current selection mode, the row may also be selected.
		"""
		res = super(Standard_QListWidget,self).currentRow()
		
		return res
	#----------------------------------------------------------------------
	def isSortingEnabled(self):
		"""
		This property holds whether sorting is enabled.
		If this property is true, sorting is enabled for the list; if the property is false, sorting is not enabled.
		The default value is false.
		"""
		res = super(Standard_QListWidget,self).isSortingEnabled()
		
		return res
	#----------------------------------------------------------------------
	def itemSelectionChanged(self):
		"""

		"""
		res = super(Standard_QListWidget,self).itemSelectionChanged()
		return res
	#----------------------------------------------------------------------
	def mimeTypes(self):
		"""
		Returns a list of MIME types that can be used to describe a list of listwidget items.
		"""
		res = super(Standard_QListWidget,self).mimeTypes()
		return res
	#----------------------------------------------------------------------
	def selectedItems(self):
		"""
		Returns a list of all selected items in the list widget.
		"""
		res = super(Standard_QListWidget,self).selectedItems()
		return res
	#----------------------------------------------------------------------
	def sortOrder(self):
		"""

		"""
		res = super(Standard_QListWidget,self).sortOrder()
		isinstance(res,QT.Qt.SortOrder)
		return res
	#----------------------------------------------------------------------
	def supportedDropActions(self):
		"""
		Returns the drop actions supported by this view.
		"""
		res = super(Standard_QListWidget,self).supportedDropActions()
		isinstance(res,QT.Qt.DropActions)
		return res
	#----------------------------------------------------------------------
	def addItem(self,*args,**kwargs):
		"""
		addItem(label)
			label=unicode

		addItem(item)
			item=QT.QListWidgetItem

		Inserts an item with the text label at the end of the list widget.
		"""
		res = super(Standard_QListWidget,self).addItem(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def addItems(self,labels):
		"""
		addItems(labels)
			labels=list

		Inserts items with the text labels at the end of the list widget.
		"""
		res = super(Standard_QListWidget,self).addItems(labels)
		return res
	#----------------------------------------------------------------------
	def closePersistentEditor(self,item):
		"""
		closePersistentEditor(item)
			item=QT.QListWidgetItem

		Closes the persistent editor for the given item .
		"""
		res = super(Standard_QListWidget,self).closePersistentEditor(item)
		return res
	#----------------------------------------------------------------------
	def dropMimeData(self,index,data,action):
		"""
		dropMimeData(index,data,action)
			index=QT.int
			data=QT.QMimeData
			action=QT.QT.DropAction


		"""
		res = super(Standard_QListWidget,self).dropMimeData(index,data,action)
		
		return res
	#----------------------------------------------------------------------
	def editItem(self,item):
		"""
		editItem(item)
			item=QT.QListWidgetItem

		Starts editing the item if it is editable.
		"""
		res = super(Standard_QListWidget,self).editItem(item)
		return res
	#----------------------------------------------------------------------
	def findItems(self,text,flags):
		"""
		findItems(text,flags)
			text=unicode
			flags=QT.QT.MatchFlags


		"""
		res = super(Standard_QListWidget,self).findItems(text,flags)
		return res
	#----------------------------------------------------------------------
	def indexFromItem(self,item):
		"""
		indexFromItem(item)
			item=QT.QListWidgetItem

		Returns the PySide.QT.QModelIndex assocated with the given item .
		"""
		res = super(Standard_QListWidget,self).indexFromItem(item)
		isinstance(res,QT.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def insertItem(self,*args,**kwargs):
		"""
		insertItem(row,label)
			row=QT.int
			label=unicode

		insertItem(row,item)
			row=QT.int
			item=QT.QListWidgetItem

		Inserts an item with the text label in the list widget at the position given by row .
		"""
		res = super(Standard_QListWidget,self).insertItem(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def insertItems(self,row,labels):
		"""
		insertItems(row,labels)
			row=QT.int
			labels=list

		Inserts items from the list of labels into the list, starting at the given row .
		"""
		res = super(Standard_QListWidget,self).insertItems(row,labels)
		return res
	#----------------------------------------------------------------------
	def item(self,row):
		"""
		item(row)
			row=QT.int

		Returns the item that occupies the given row in the list if one has been set; otherwise returns 0.
		"""
		res = super(Standard_QListWidget,self).item(row)
		isinstance(res,QT.QListWidgetItem)
		return res
	#----------------------------------------------------------------------
	def itemAt(self,*args,**kwargs):
		"""
		itemAt(x,y)
			x=QT.int
			y=QT.int

		itemAt(p)
			p=QT.QPoint

		This is an overloaded function.
		Returns a pointer to the item at the coordinates (x , y ).
		"""
		res = super(Standard_QListWidget,self).itemAt(*args,**kwargs)
		isinstance(res,QT.QListWidgetItem)
		return res
	#----------------------------------------------------------------------
	def itemFromIndex(self,index):
		"""
		itemFromIndex(index)
			index=QT.QModelIndex

		Returns a pointer to the PySide.QT.QListWidgetItem assocated with the given index .
		"""
		res = super(Standard_QListWidget,self).itemFromIndex(index)
		isinstance(res,QT.QListWidgetItem)
		return res
	#----------------------------------------------------------------------
	def itemWidget(self,item):
		"""
		itemWidget(item)
			item=QT.QListWidgetItem

		Returns the widget displayed in the given item .
		"""
		res = super(Standard_QListWidget,self).itemWidget(item)
		isinstance(res,QT.QWidget)
		return res
	#----------------------------------------------------------------------
	def items(self,data):
		"""
		items(data)
			data=QT.QMimeData

		Returns a list of pointers to the items contained in the data object
		If the object was not created by a PySide.QT.QListWidget in the same process, the list is empty.
		"""
		res = super(Standard_QListWidget,self).items(data)
		return res
	#----------------------------------------------------------------------
	def mimeData(self,items):
		"""
		mimeData(items)
			items=unKnown


		"""
		res = super(Standard_QListWidget,self).mimeData(items)
		isinstance(res,QT.QMimeData)
		return res
	#----------------------------------------------------------------------
	def openPersistentEditor(self,item):
		"""
		openPersistentEditor(item)
			item=QT.QListWidgetItem

		Opens an editor for the given item
		The editor remains open after editing.
		"""
		res = super(Standard_QListWidget,self).openPersistentEditor(item)
		return res
	#----------------------------------------------------------------------
	def removeItemWidget(self,item):
		"""
		removeItemWidget(item)
			item=QT.QListWidgetItem

		Removes the widget set on the given item .
		"""
		res = super(Standard_QListWidget,self).removeItemWidget(item)
		return res
	#----------------------------------------------------------------------
	def row(self,item):
		"""
		row(item)
			item=QT.QListWidgetItem

		Returns the row containing the given item .
		"""
		res = super(Standard_QListWidget,self).row(item)
		
		return res
	#----------------------------------------------------------------------
	def setCurrentItem(self,*args,**kwargs):
		"""
		setCurrentItem(item)
			item=QT.QListWidgetItem

		setCurrentItem(item,command)
			item=QT.QListWidgetItem
			command=QT.QItemSelectionModel.SelectionFlags

		Sets the current item to item .
		Unless the selection mode is NoSelection , the item is also be selected.
		"""
		res = super(Standard_QListWidget,self).setCurrentItem(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setCurrentRow(self,*args,**kwargs):
		"""
		setCurrentRow(row,command)
			row=QT.int
			command=QT.QItemSelectionModel.SelectionFlags

		setCurrentRow(row)
			row=QT.int


		"""
		res = super(Standard_QListWidget,self).setCurrentRow(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setItemWidget(self,item,widget):
		"""
		setItemWidget(item,widget)
			item=QT.QListWidgetItem
			widget=QT.QWidget

		Sets the widget to be displayed in the give item .
		This function should only be used to display static content in the place of a list widget item
		If you want to display custom dynamic content or implement a custom editor widget, use PySide.QT.QListView and subclass PySide.QT.QItemDelegate instead.
		"""
		res = super(Standard_QListWidget,self).setItemWidget(item,widget)
		return res
	#----------------------------------------------------------------------
	def setSortingEnabled(self,enable):
		"""
		setSortingEnabled(enable)
			enable=QT.bool

		This property holds whether sorting is enabled.
		If this property is true, sorting is enabled for the list; if the property is false, sorting is not enabled.
		The default value is false.
		"""
		res = super(Standard_QListWidget,self).setSortingEnabled(enable)
		return res
	#----------------------------------------------------------------------
	def sortItems(self,order=None):
		"""
		sortItems(order=None)
			order=QT.QT.SortOrder


		"""
		res = super(Standard_QListWidget,self).sortItems(order)
		return res
	#----------------------------------------------------------------------
	def takeItem(self,row):
		"""
		takeItem(row)
			row=QT.int

		Removes and returns the item from the given row in the list widget; otherwise returns 0.
		Items removed from a list widget will not be managed by Qt, and will need to be deleted manually.
		"""
		res = super(Standard_QListWidget,self).takeItem(row)
		isinstance(res,QT.QListWidgetItem)
		return res
	#----------------------------------------------------------------------
	def visualItemRect(self,item):
		"""
		visualItemRect(item)
			item=QT.QListWidgetItem

		Returns the rectangle on the viewport occupied by the item at item .
		"""
		res = super(Standard_QListWidget,self).visualItemRect(item)
		isinstance(res,QT.QRect)
		return res
