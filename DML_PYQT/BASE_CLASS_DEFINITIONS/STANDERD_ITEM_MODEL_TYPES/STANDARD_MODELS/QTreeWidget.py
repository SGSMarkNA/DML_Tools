from .... import QT

class Standard_QTreeWidget(QT.QTreeWidget):
	''''''
	Item_Data_Roles     = QT.Constants.ItemDataRole
	Item_View_Constants = QT.Constants.AbstractItemView
	def __init__(self,*args,**kwargs):
		''''''
		super(Standard_QTreeWidget,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def columnCount(self):
		"""
		This property holds the number of columns displayed in the tree widget.
		By default, this property has a value of 1.
		"""
		res = super(Standard_QTreeWidget,self).columnCount()
		return res
	#----------------------------------------------------------------------
	def currentColumn(self):
		"""
		Returns the current column in the tree widget.
		"""
		res = super(Standard_QTreeWidget,self).currentColumn()
		
		return res
	#----------------------------------------------------------------------
	def currentItem(self):
		"""
		Returns the current item in the tree widget.
		"""
		res = super(Standard_QTreeWidget,self).currentItem()
		isinstance(res,QT.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def headerItem(self):
		"""
		Returns the item used for the tree widgets header.
		"""
		res = super(Standard_QTreeWidget,self).headerItem()
		isinstance(res,QT.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def invisibleRootItem(self):
		"""
		Returns the tree widgets invisible root item.
		The invisible root item provides access to the tree widgets top-level items through the PySide.QT.QTreeWidgetItem API, making it possible to write functions that can treat top-level items and their children in a uniform way; for example, recursive functions.
		"""
		res = super(Standard_QTreeWidget,self).invisibleRootItem()
		isinstance(res,QT.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def mimeTypes(self):
		"""
		Returns a list of MIME types that can be used to describe a list of treewidget items.
		"""
		res = super(Standard_QTreeWidget,self).mimeTypes()
		return res
	#----------------------------------------------------------------------
	def selectedItems(self):
		"""
		Returns a list of all selected non-hidden items.
		"""
		res = super(Standard_QTreeWidget,self).selectedItems()
		return res
	#----------------------------------------------------------------------
	def sortColumn(self):
		"""
		Returns the column used to sort the contents of the widget.
		"""
		res = super(Standard_QTreeWidget,self).sortColumn()
		
		return res
	#----------------------------------------------------------------------
	def supportedDropActions(self):
		"""
		Returns the drop actions supported by this view.
		"""
		res = super(Standard_QTreeWidget,self).supportedDropActions()
		isinstance(res,QT.Qt.DropActions)
		return res
	#----------------------------------------------------------------------
	def topLevelItemCount(self):
		"""
		This property holds the number of top-level items.
		By default, this property has a value of 0.
		"""
		res = super(Standard_QTreeWidget,self).topLevelItemCount()
		
		return res
	#----------------------------------------------------------------------
	def addTopLevelItem(self,item):
		"""
		addTopLevelItem(item)
			item=QT.QTreeWidgetItem

		Appends the item as a top-level item in the widget.
		"""
		res = super(Standard_QTreeWidget,self).addTopLevelItem(item)
		return res
	#----------------------------------------------------------------------
	def addTopLevelItems(self,items):
		"""
		addTopLevelItems(items)
			items=unKnown


		"""
		res = super(Standard_QTreeWidget,self).addTopLevelItems(items)
		return res
	#----------------------------------------------------------------------
	def closePersistentEditor(self,item,column=None):
		"""
		closePersistentEditor(item,column=None)
			item=QT.QTreeWidgetItem
			column=DML_PYQT.int

		Closes the persistent editor for the item in the given column .
		This function has no effect if no persistent editor is open for this combination of item and column.
		"""
		res = super(Standard_QTreeWidget,self).closePersistentEditor(item,column)
		return res
	##----------------------------------------------------------------------
	#def dropMimeData(self,parent,index,data,action):
		#"""
		#dropMimeData(parent,index,data,action)
			#parent=QT.QTreeWidgetItem
			#index=DML_PYQT.int
			#data=DML_PYQT.QMimeData
			#action=DML_PYQT.QT.DropAction


		#"""
		#res = super(Tree_Widget,self).dropMimeData(parent,index,data,action)
		
		#return res
	#----------------------------------------------------------------------
	def editItem(self,item,column=None):
		"""
		editItem(item,column=None)
			item=DML_PYQT.QTreeWidgetItem
			column=DML_PYQT.int

		Starts editing the item in the given column if it is editable.
		"""
		res = super(Standard_QTreeWidget,self).editItem(item,column)
		return res
	#----------------------------------------------------------------------
	def findItems(self,text,flags=QT.Constants.MatchFlag.Exactly|QT.Constants.MatchFlag.Recursive|QT.Constants.MatchFlag.CaseSensitive, column=0):
		"""
		findItems(text,flags,column=None)
			text=unicode
			flags=DML_PYQT.QT.MatchFlags
			column=DML_PYQT.int


		"""
		res = super(Standard_QTreeWidget,self).findItems(text,flags,column)
		return res
	#----------------------------------------------------------------------
	def indexFromItem(self,item,column=0):
		"""
		indexFromItem(item,column=None)
			item=DML_PYQT.QTreeWidgetItem
			column=DML_PYQT.int

		Returns the PySide.DML_PYQT.QModelIndex assocated with the given item in the given column .
		"""
		res = super(Standard_QTreeWidget,self).indexFromItem(item,column)
		isinstance(res,QT.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def indexOfTopLevelItem(self,item):
		"""
		indexOfTopLevelItem(item)
			item=DML_PYQT.QTreeWidgetItem

		Returns the index of the given top-level item , or -1 if the item cannot be found.
		"""
		res = super(Standard_QTreeWidget,self).indexOfTopLevelItem(item)
		
		return res
	#----------------------------------------------------------------------
	def insertTopLevelItem(self,index,item):
		"""
		insertTopLevelItem(index,item)
			index=DML_PYQT.int
			item=DML_PYQT.QTreeWidgetItem

		Inserts the item at index in the top level in the view.
		If the item has already been inserted somewhere else it wont be inserted.
		"""
		res = super(Standard_QTreeWidget,self).insertTopLevelItem(index,item)
		return res
	#----------------------------------------------------------------------
	def insertTopLevelItems(self,index,items):
		"""
		insertTopLevelItems(index,items)
			index=DML_PYQT.int
			items=unKnown


		"""
		res = super(Standard_QTreeWidget,self).insertTopLevelItems(index,items)
		return res
	#----------------------------------------------------------------------
	def isFirstItemColumnSpanned(self,item):
		"""
		isFirstItemColumnSpanned(item)
			item=DML_PYQT.QTreeWidgetItem

		Returns true if the given item is set to show only one section over all columns; otherwise returns false.
		"""
		res = super(Standard_QTreeWidget,self).isFirstItemColumnSpanned(item)
		
		return res
	#----------------------------------------------------------------------
	def isItemExpanded(self,item):
		"""
		isItemExpanded(item)
			item=DML_PYQT.QTreeWidgetItem

		Returns true if the given item is open; otherwise returns false.
		This function is deprecated
		Use QTreeWidgetItem.isExpanded() instead.
		"""
		res = super(Standard_QTreeWidget,self).isItemExpanded(item)
		
		return res
	#----------------------------------------------------------------------
	def isItemHidden(self,item):
		"""
		isItemHidden(item)
			item=DML_PYQT.QTreeWidgetItem

		Returns true if the item is explicitly hidden, otherwise returns false.
		This function is deprecated
		Use QTreeWidgetItem.isHidden() instead.
		"""
		res = super(Standard_QTreeWidget,self).isItemHidden(item)
		
		return res
	#----------------------------------------------------------------------
	def isItemSelected(self,item):
		"""
		isItemSelected(item)
			item=DML_PYQT.QTreeWidgetItem

		Returns true if the item is selected; otherwise returns false.
		This function is deprecated
		Use QTreeWidgetItem.isSelected() instead.
		"""
		res = super(Standard_QTreeWidget,self).isItemSelected(item)
		
		return res
	#----------------------------------------------------------------------
	def itemAbove(self,item):
		"""
		itemAbove(item)
			item=DML_PYQT.QTreeWidgetItem

		Returns the item above the given item .
		"""
		res = super(Standard_QTreeWidget,self).itemAbove(item)
		isinstance(res,QT.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def itemAt(self,*args,**kwargs):
		"""
		itemAt(x,y)
			x=DML_PYQT.int
			y=DML_PYQT.int

		itemAt(p)
			p=DML_PYQT.QPoint

		This is an overloaded function.
		Returns a pointer to the item at the coordinates (x , y ).
		"""
		res = super(Standard_QTreeWidget,self).itemAt(*args,**kwargs)
		isinstance(res,QT.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def itemBelow(self,item):
		"""
		itemBelow(item)
			item=DML_PYQT.QTreeWidgetItem

		Returns the item visually below the given item .
		"""
		res = super(Standard_QTreeWidget,self).itemBelow(item)
		isinstance(res,QT.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def itemFromIndex(self,index):
		"""
		itemFromIndex(index)
			index=DML_PYQT.QModelIndex

		Returns a pointer to the PySide.DML_PYQT.QTreeWidgetItem assocated with the given index .
		"""
		res = super(Standard_QTreeWidget,self).itemFromIndex(index)
		isinstance(res,QT.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def itemWidget(self,item,column):
		"""
		itemWidget(item,column)
			item=DML_PYQT.QTreeWidgetItem
			column=DML_PYQT.int

		Returns the widget displayed in the cell specified by item and the given column .
		"""
		res = super(Standard_QTreeWidget,self).itemWidget(item,column)
		isinstance(res,QT.QWidget)
		return res
	##----------------------------------------------------------------------
	#def mimeData(self,items):
		#"""
		#mimeData(items)
			#items=unKnown


		#"""
		#res = super(Tree_Widget,self).mimeData(items)
		#isinstance(res,DML_PYQT.QMimeData)
		#return res
	#----------------------------------------------------------------------
	def openPersistentEditor(self,item,column=None):
		"""
		openPersistentEditor(item,column=None)
			item=DML_PYQT.QTreeWidgetItem
			column=DML_PYQT.int

		Opens a persistent editor for the item in the given column .
		"""
		res = super(Standard_QTreeWidget,self).openPersistentEditor(item,column)
		return res
	#----------------------------------------------------------------------
	def removeItemWidget(self,item,column):
		"""
		removeItemWidget(item,column)
			item=DML_PYQT.QTreeWidgetItem
			column=DML_PYQT.int

		Removes the widget set in the given item in the given column .
		"""
		res = super(Standard_QTreeWidget,self).removeItemWidget(item,column)
		return res
	#----------------------------------------------------------------------
	def setColumnCount(self,columns):
		"""
		setColumnCount(columns)
			columns=DML_PYQT.int

		This property holds the number of columns displayed in the tree widget.
		By default, this property has a value of 1.
		"""
		res = super(Standard_QTreeWidget,self).setColumnCount(columns)
		return res
	#----------------------------------------------------------------------
	def setCurrentItem(self,*args,**kwargs):
		"""
		setCurrentItem(item,column)
			item=DML_PYQT.QTreeWidgetItem
			column=DML_PYQT.int

		setCurrentItem(item,column,command)
			item=DML_PYQT.QTreeWidgetItem
			column=DML_PYQT.int
			command=DML_PYQT.QItemSelectionModel.SelectionFlags

		setCurrentItem(item)
			item=DML_PYQT.QTreeWidgetItem

		Sets the current item in the tree widget and the current column to column .
		"""
		res = super(Standard_QTreeWidget,self).setCurrentItem(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setFirstItemColumnSpanned(self,item,span):
		"""
		setFirstItemColumnSpanned(item,span)
			item=DML_PYQT.QTreeWidgetItem
			span=DML_PYQT.bool

		Sets the given item to only show one section for all columns if span is true; otherwise the item will show one section per column.
		"""
		res = super(Standard_QTreeWidget,self).setFirstItemColumnSpanned(item,span)
		return res
	#----------------------------------------------------------------------
	def setHeaderItem(self,item):
		"""
		setHeaderItem(item)
			item=DML_PYQT.QTreeWidgetItem

		Sets the header item for the tree widget
		The label for each column in the header is supplied by the corresponding label in the item.
		The tree widget takes ownership of the item.
		"""
		res = super(Standard_QTreeWidget,self).setHeaderItem(item)
		return res
	#----------------------------------------------------------------------
	def setHeaderLabel(self,label):
		"""
		setHeaderLabel(label)
			label=unicode

		Same as setHeaderLabels( PySide.DML_PYQT.QStringList (label )).
		"""
		res = super(Standard_QTreeWidget,self).setHeaderLabel(label)
		return res
	#----------------------------------------------------------------------
	def setHeaderLabels(self,labels):
		"""
		setHeaderLabels(labels)
			labels=list

		Adds a column in the header for each item in the labels list, and sets the label for each column.
		Note that PySide.DML_PYQT.QTreeWidget.setHeaderLabels() wont remove existing columns.
		"""
		res = super(Standard_QTreeWidget,self).setHeaderLabels(labels)
		return res
	#----------------------------------------------------------------------
	def setItemExpanded(self,item,expand):
		"""
		setItemExpanded(item,expand)
			item=DML_PYQT.QTreeWidgetItem
			expand=DML_PYQT.bool

		Sets the item referred to by item to either closed or opened, depending on the value of expand .
		This function is deprecated
		Use QTreeWidgetItem.setExpanded() instead.
		"""
		res = super(Standard_QTreeWidget,self).setItemExpanded(item,expand)
		return res
	#----------------------------------------------------------------------
	def setItemHidden(self,item,hide):
		"""
		setItemHidden(item,hide)
			item=DML_PYQT.QTreeWidgetItem
			hide=DML_PYQT.bool

		Hides the given item if hide is true; otherwise shows the item.
		This function is deprecated
		Use QTreeWidgetItem.setHidden() instead.
		"""
		res = super(Standard_QTreeWidget,self).setItemHidden(item,hide)
		return res
	#----------------------------------------------------------------------
	def setItemSelected(self,item,select):
		"""
		setItemSelected(item,select)
			item=DML_PYQT.QTreeWidgetItem
			select=DML_PYQT.bool

		If select is true, the given item is selected; otherwise it is deselected.
		This function is deprecated
		Use QTreeWidgetItem.setSelected() instead.
		"""
		res = super(Standard_QTreeWidget,self).setItemSelected(item,select)
		return res
	#----------------------------------------------------------------------
	def setItemWidget(self,item,column,widget):
		"""
		setItemWidget(item,column,widget)
			item=DML_PYQT.QTreeWidgetItem
			column=DML_PYQT.int
			widget=DML_PYQT.QWidget

		Sets the given widget to be displayed in the cell specified by the given item and column .
		The given widget s PySide.DML_PYQT.QWidget.autoFillBackground() property must be set to true, otherwise the widgets background will be transparent, showing both the model data and the tree widget item.
		This function should only be used to display static content in the place of a tree widget item
		If you want to display custom dynamic content or implement a custom editor widget, use PySide.DML_PYQT.QTreeView and subclass PySide.DML_PYQT.QItemDelegate instead.
		This function cannot be called before the item hierarchy has been set up, i.e., the PySide.DML_PYQT.QTreeWidgetItem that will hold widget must have been added to the view before widget is set.
		"""
		res = super(Standard_QTreeWidget,self).setItemWidget(item,column,widget)
		return res
	#----------------------------------------------------------------------
	def sortItems(self,column,order):
		"""
		sortItems(column,order)
			column=DML_PYQT.int
			order=DML_PYQT.QT.SortOrder


		"""
		res = super(Standard_QTreeWidget,self).sortItems(column,order)
		return res
	#----------------------------------------------------------------------
	def takeTopLevelItem(self,index):
		"""
		takeTopLevelItem(index)
			index=DML_PYQT.int

		Removes the top-level item at the given index in the tree and returns it, otherwise returns 0;
		"""
		res = super(Standard_QTreeWidget,self).takeTopLevelItem(index)
		isinstance(res,QT.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def topLevelItem(self,index):
		"""
		topLevelItem(index)
			index=DML_PYQT.int

		Returns the top level item at the given index , or 0 if the item does not exist.
		"""
		res = super(Standard_QTreeWidget,self).topLevelItem(index)
		isinstance(res,QT.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def visualItemRect(self,item):
		"""
		visualItemRect(item)
			item=DML_PYQT.QTreeWidgetItem

		Returns the rectangle on the viewport occupied by the item at item .
		"""
		res = super(Standard_QTreeWidget,self).visualItemRect(item)
		isinstance(res,QT.QRect)
		return res
	#----------------------------------------------------------------------
	def iter_TopLevelItems(self):
		""""""
		for row in range(self.topLevelItemCount()):
			yield self.topLevelItem(row)
	#----------------------------------------------------------------------
	def add_Item(self, item, parent=None):
		"""Add a TreeWidgetItem if Parent is a QTreeWidgetItem The Item is add as a child to that parent else it is added as a top level item"""
		if not isinstance(item, QT.QTreeWidgetItem):
			raise ValueError(item)
		
		if isinstance(parent, QT.QTreeWidgetItem):
			parent.addChild(item)
		else:
			self.addTopLevelItem(item)
	#----------------------------------------------------------------------
	def remove_Item(self, item):
		"""Removes and returns the item for the tree if the item is not a top level item it removes it for its part"""
		if not isinstance(item, QT.QTreeWidgetItem):
			raise ValueError(item)
		parent = item.parent()
		if isinstance(parent, QT.QTreeWidgetItem):
			index = parent.indexOfChild(item)
			res   = parent.takeChild(index)
		else:
			index = self.indexOfTopLevelItem(item)
			res   = self.takeTopLevelItem(index)
		isinstance(res, QT.QTreeWidgetItem)
		return res
	
	ColumnCount   = property(columnCount,setColumnCount)
	CurrentItem   = property(currentItem)
	SelectedItems = property(selectedItems)
	
