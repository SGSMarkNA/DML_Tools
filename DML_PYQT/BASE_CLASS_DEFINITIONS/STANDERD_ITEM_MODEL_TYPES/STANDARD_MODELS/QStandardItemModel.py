from .... import QT

class Standard_QStandardItemModel(QT.QStandardItemModel):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(Standard_QStandardItemModel,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Removes all items (including header items) from the model and sets the number of rows and columns to zero.
		"""
		res = super(Standard_QStandardItemModel,self).clear()
		return res
	#----------------------------------------------------------------------
	def invisibleRootItem(self):
		"""
		Returns the models invisible root item.
		The invisible root item provides access to the models top-level items through the PySide.QT.QStandardItem API, making it possible to write functions that can treat top-level items and their children in a uniform way; for example, recursive functions involving a tree model.
		"""
		res = super(Standard_QStandardItemModel,self).invisibleRootItem()
		isinstance(res,QT.QStandardItem)
		return res
	#----------------------------------------------------------------------
	def itemPrototype(self):
		"""
		Returns the item prototype used by the model
		The model uses the item prototype as an item factory when it needs to construct new items on demand (for instance, when a view or item delegate calls PySide.QT.QStandardItemModel.setData() ).
		"""
		res = super(Standard_QStandardItemModel,self).itemPrototype()
		isinstance(res,QT.QStandardItem)
		return res
	#----------------------------------------------------------------------
	def sortRole(self):
		"""
		This property holds the item role that is used to query the models data when sorting items.
		The default value is Qt.DisplayRole .
		"""
		res = super(Standard_QStandardItemModel,self).sortRole()

		return res
	#----------------------------------------------------------------------
	def appendColumn(self,items):
		"""
		appendColumn(items)
			items=unKnown


		"""
		res = super(Standard_QStandardItemModel,self).appendColumn(items)
		return res
	#----------------------------------------------------------------------
	def appendRow(self,items):
		"""
		appendRow(items)
			items=unKnown

		appendRow(item)
			item=QT.QStandardItem


		"""
		res = super(Standard_QStandardItemModel,self).appendRow(items)
		return res
	#----------------------------------------------------------------------
	def findItems(self,text,flags=None,column=None):
		"""
		findItems(text,flags=None,column=None)
			text=unicode
			flags=QT.Qt.MatchFlags
			column=QT.int


		"""
		res = super(Standard_QStandardItemModel,self).findItems(text,flags,column)
		return res
	#----------------------------------------------------------------------
	def horizontalHeaderItem(self,column):
		"""
		horizontalHeaderItem(column)
			column=QT.int

		Returns the horizontal header item for column if one has been set; otherwise returns 0.
		"""
		res = super(Standard_QStandardItemModel,self).horizontalHeaderItem(column)
		isinstance(res,QT.QStandardItem)
		return res
	#----------------------------------------------------------------------
	def indexFromItem(self,item):
		"""
		indexFromItem(item)
			item=QT.QStandardItem

		Returns the PySide.QT.QModelIndex associated with the given item .
		Use this function when you want to perform an operation that requires the PySide.QT.QModelIndex of the item, such as QAbstractItemView.scrollTo()
		QStandardItem.index() is provided as convenience; it is equivalent to calling this function.
		"""
		res = super(Standard_QStandardItemModel,self).indexFromItem(item)
		isinstance(res,QT.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def insertColumn(self,column,items):
		"""
		insertColumn(column,items)
			column=QT.int
			items=unKnown


		"""
		res = super(Standard_QStandardItemModel,self).insertColumn(column,items)
		return res
	#----------------------------------------------------------------------
	def insertRow(self,*args,**kwargs):
		"""
		insertRow(row,items)
			row=QT.int
			items=unKnown

		insertRow(row,item)
			row=QT.int
			item=QT.QStandardItem


		"""
		res = super(Standard_QStandardItemModel,self).insertRow(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def item(self,row,column=0):
		"""
		item(row,column=None)
			row=QT.int
			column=QT.int

		Returns the item for the given row and column if one has been set; otherwise returns 0.
		"""
		res = super(Standard_QStandardItemModel,self).item(row,column)
		isinstance(res,QT.QStandardItem)
		return res
	#----------------------------------------------------------------------
	def itemFromIndex(self,index):
		"""
		itemFromIndex(index)
			index=QT.QModelIndex

		Returns a pointer to the PySide.QT.QStandardItem associated with the given index .
		Calling this function is typically the initial step when processing PySide.QT.QModelIndex -based signals from a view, such as QAbstractItemView.activated()
		In your slot, you call PySide.QT.QStandardItemModel.itemFromIndex() , with the PySide.QT.QModelIndex carried by the signal as argument, to obtain a pointer to the corresponding PySide.QT.QStandardItem .
		Note that this function will lazily create an item for the index (using PySide.QT.QStandardItemModel.itemPrototype() ), and set it in the parent items child table, if no item already exists at that index.
		If index is an invalid index, this function returns 0.
		"""
		res = super(Standard_QStandardItemModel,self).itemFromIndex(index)
		isinstance(res,QT.QStandardItem)
		return res
	#----------------------------------------------------------------------
	def setColumnCount(self,columns):
		"""
		setColumnCount(columns)
			columns=QT.int

		Sets the number of columns in this model to columns
		If this is less than PySide.QT.QStandardItemModel.columnCount() , the data in the unwanted columns is discarded.
		"""
		res = super(Standard_QStandardItemModel,self).setColumnCount(columns)
		return res
	#----------------------------------------------------------------------
	def setHorizontalHeaderItem(self,column,item):
		"""
		setHorizontalHeaderItem(column,item)
			column=QT.int
			item=QT.QStandardItem

		Sets the horizontal header item for column to item
		The model takes ownership of the item
		If necessary, the column count is increased to fit the item
		The previous header item (if there was one) is deleted.
		"""
		res = super(Standard_QStandardItemModel,self).setHorizontalHeaderItem(column,item)
		return res
	#----------------------------------------------------------------------
	def setHorizontalHeaderLabels(self,labels):
		"""
		setHorizontalHeaderLabels(labels)
			labels=list

		Sets the horizontal header labels using labels
		If necessary, the column count is increased to the size of labels .
		"""
		res = super(Standard_QStandardItemModel,self).setHorizontalHeaderLabels(labels)
		return res
	#----------------------------------------------------------------------
	def setItem(self,*args,**kwargs):
		"""
		setItem(row,item)
			row=QT.int
			item=QT.QStandardItem

		setItem(row,column,item)
			row=QT.int
			column=QT.int
			item=QT.QStandardItem

		This is an overloaded function.
		"""
		res = super(Standard_QStandardItemModel,self).setItem(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setItemPrototype(self,item):
		"""
		setItemPrototype(item)
			item=QT.QStandardItem

		Sets the item prototype for the model to the specified item
		The model takes ownership of the prototype.
		The item prototype acts as a PySide.QT.QStandardItem factory, by relying on the QStandardItem.clone() function
		To provide your own prototype, subclass PySide.QT.QStandardItem , reimplement QStandardItem.clone() and set the prototype to be an instance of your custom class
		Whenever PySide.QT.QStandardItemModel needs to create an item on demand (for instance, when a view or item delegate calls PySide.QT.QStandardItemModel.setData() )), the new items will be instances of your custom class.
		"""
		res = super(Standard_QStandardItemModel,self).setItemPrototype(item)
		return res
	#----------------------------------------------------------------------
	def setRowCount(self,rows):
		"""
		setRowCount(rows)
			rows=QT.int

		Sets the number of rows in this model to rows
		If this is less than PySide.QT.QStandardItemModel.rowCount() , the data in the unwanted rows is discarded.
		"""
		res = super(Standard_QStandardItemModel,self).setRowCount(rows)
		return res
	#----------------------------------------------------------------------
	def setSortRole(self,role):
		"""
		setSortRole(role)
			role=QT.int

		This property holds the item role that is used to query the models data when sorting items.
		The default value is Qt.DisplayRole .
		"""
		res = super(Standard_QStandardItemModel,self).setSortRole(role)
		return res
	#----------------------------------------------------------------------
	def setVerticalHeaderItem(self,row,item):
		"""
		setVerticalHeaderItem(row,item)
			row=QT.int
			item=QT.QStandardItem

		Sets the vertical header item for row to item
		The model takes ownership of the item
		If necessary, the row count is increased to fit the item
		The previous header item (if there was one) is deleted.
		"""
		res = super(Standard_QStandardItemModel,self).setVerticalHeaderItem(row,item)
		return res
	#----------------------------------------------------------------------
	def setVerticalHeaderLabels(self,labels):
		"""
		setVerticalHeaderLabels(labels)
			labels=list

		Sets the vertical header labels using labels
		If necessary, the row count is increased to the size of labels .
		"""
		res = super(Standard_QStandardItemModel,self).setVerticalHeaderLabels(labels)
		return res
	#----------------------------------------------------------------------
	def takeColumn(self,column):
		"""
		takeColumn(column)
			column=QT.int

		Removes the given column without deleting the column items, and returns a list of pointers to the removed items
		The model releases ownership of the items
		For items in the column that have not been set, the corresponding pointers in the list will be 0.
		"""
		res = super(Standard_QStandardItemModel,self).takeColumn(column)
		return res
	#----------------------------------------------------------------------
	def takeHorizontalHeaderItem(self,column):
		"""
		takeHorizontalHeaderItem(column)
			column=QT.int

		Removes the horizontal header item at column from the header without deleting it, and returns a pointer to the item
		The model releases ownership of the item.
		"""
		res = super(Standard_QStandardItemModel,self).takeHorizontalHeaderItem(column)
		isinstance(res,QT.QStandardItem)
		return res
	#----------------------------------------------------------------------
	def takeItem(self,row,column=None):
		"""
		takeItem(row,column=None)
			row=QT.int
			column=QT.int

		Removes the item at (row , column ) without deleting it
		The model releases ownership of the item.
		"""
		res = super(Standard_QStandardItemModel,self).takeItem(row,column)
		isinstance(res,QT.QStandardItem)
		return res
	#----------------------------------------------------------------------
	def takeRow(self,row):
		"""
		takeRow(row)
			row=QT.int

		Removes the given row without deleting the row items, and returns a list of pointers to the removed items
		The model releases ownership of the items
		For items in the row that have not been set, the corresponding pointers in the list will be 0.
		"""
		res = super(Standard_QStandardItemModel,self).takeRow(row)
		return res
	#----------------------------------------------------------------------
	def takeVerticalHeaderItem(self,row):
		"""
		takeVerticalHeaderItem(row)
			row=QT.int

		Removes the vertical header item at row from the header without deleting it, and returns a pointer to the item
		The model releases ownership of the item.
		"""
		res = super(Standard_QStandardItemModel,self).takeVerticalHeaderItem(row)
		isinstance(res,QT.QStandardItem)
		return res
	#----------------------------------------------------------------------
	def verticalHeaderItem(self,row):
		"""
		verticalHeaderItem(row)
			row=QT.int

		Returns the vertical header item for row row if one has been set; otherwise returns 0.
		"""
		res = super(Standard_QStandardItemModel,self).verticalHeaderItem(row)
		isinstance(res,QT.QStandardItem)
		return res


	### QAbstrateItemModel Methods
	#----------------------------------------------------------------------
	def beginResetModel(self):
		"""
		Begins a model reset operation.
		A reset operation resets the model to its current state in any attached views.
		When a model is reset it means that any previous data reported from the model is now invalid and has to be queried for again
		This also means that the current item and any selected items will become invalid.
		When a model radically changes its data it can sometimes be easier to just call this function rather than emit PySide.QT.QAbstractItemModel.dataChanged() to inform other components when the underlying data source, or its structure, has changed.
		You must call this function before resetting any internal data structures in your model or proxy model.
		"""
		res = super(Standard_QStandardItemModel,self).beginResetModel()
		return res
	#----------------------------------------------------------------------
	def endInsertColumns(self):
		"""
		Ends a column insertion operation.
		When reimplementing PySide.QT.QAbstractItemModel.insertColumns() in a subclass, you must call this function after inserting data into the models underlying data store.
		"""
		res = super(Standard_QStandardItemModel,self).endInsertColumns()
		return res
	#----------------------------------------------------------------------
	def endInsertRows(self):
		"""
		Ends a row insertion operation.
		When reimplementing PySide.QT.QAbstractItemModel.insertRows() in a subclass, you must call this function after inserting data into the models underlying data store.
		"""
		res = super(Standard_QStandardItemModel,self).endInsertRows()
		return res
	#----------------------------------------------------------------------
	def endMoveColumns(self):
		"""
		Ends a column move operation.
		When implementing a subclass, you must call this function after moving data within the models underlying data store.
		layoutChanged is emitted by this method for compatibility reasons.
		"""
		res = super(Standard_QStandardItemModel,self).endMoveColumns()
		return res
	#----------------------------------------------------------------------
	def endMoveRows(self):
		"""
		Ends a row move operation.
		When implementing a subclass, you must call this function after moving data within the models underlying data store.
		layoutChanged is emitted by this method for compatibility reasons.
		"""
		res = super(Standard_QStandardItemModel,self).endMoveRows()
		return res
	#----------------------------------------------------------------------
	def endRemoveColumns(self):
		"""
		Ends a column removal operation.
		When reimplementing PySide.QT.QAbstractItemModel.removeColumns() in a subclass, you must call this function after removing data from the models underlying data store.
		"""
		res = super(Standard_QStandardItemModel,self).endRemoveColumns()
		return res
	#----------------------------------------------------------------------
	def endRemoveRows(self):
		"""
		Ends a row removal operation.
		When reimplementing PySide.QT.QAbstractItemModel.removeRows() in a subclass, you must call this function after removing data from the models underlying data store.
		"""
		res = super(Standard_QStandardItemModel,self).endRemoveRows()
		return res
	#----------------------------------------------------------------------
	def endResetModel(self):
		"""
		Completes a model reset operation.
		You must call this function after resetting any internal data structure in your model or proxy model.
		"""
		res = super(Standard_QStandardItemModel,self).endResetModel()
		return res
	#----------------------------------------------------------------------
	def layoutAboutToBeChanged(self):
		"""

		"""
		res = super(Standard_QStandardItemModel,self).layoutAboutToBeChanged()
		return res
	#----------------------------------------------------------------------
	def layoutChanged(self):
		"""

		"""
		res = super(Standard_QStandardItemModel,self).layoutChanged()
		return res
	#----------------------------------------------------------------------
	def mimeTypes(self):
		"""
		Returns a list of MIME types that can be used to describe a list of model indexes.
		"""
		res = super(Standard_QStandardItemModel,self).mimeTypes()
		return res
	#----------------------------------------------------------------------
	def modelAboutToBeReset(self):
		"""

		"""
		res = super(Standard_QStandardItemModel,self).modelAboutToBeReset()
		return res
	#----------------------------------------------------------------------
	def modelReset(self):
		"""

		"""
		res = super(Standard_QStandardItemModel,self).modelReset()
		return res
	#----------------------------------------------------------------------
	def persistentIndexList(self):
		"""
		Returns the list of indexes stored as persistent indexes in the model.
		"""
		res = super(Standard_QStandardItemModel,self).persistentIndexList()
		return res
	#----------------------------------------------------------------------
	def reset(self):
		"""
		Resets the model to its original state in any attached views.
		"""
		res = super(Standard_QStandardItemModel,self).reset()
		return res
	#----------------------------------------------------------------------
	def revert(self):
		"""
		Lets the model know that it should discard cached information
		This function is typically used for row editing.
		"""
		res = super(Standard_QStandardItemModel,self).revert()
		return res
	#----------------------------------------------------------------------
	def roleNames(self):
		"""
		Returns the models role names.
		"""
		res = super(Standard_QStandardItemModel,self).roleNames()
		return res
	#----------------------------------------------------------------------
	def submit(self):
		"""
		Lets the model know that it should submit cached information to permanent storage
		This function is typically used for row editing.
		Returns true if there is no error; otherwise returns false.
		"""
		res = super(Standard_QStandardItemModel,self).submit()

		return res
	#----------------------------------------------------------------------
	def supportedDragActions(self):
		"""
		Returns the actions supported by the data in this model.
		The default implementation returns PySide.QT.QAbstractItemModel.supportedDropActions() unless specific values have been set with PySide.QT.QAbstractItemModel.setSupportedDragActions() .
		PySide.QT.QAbstractItemModel.supportedDragActions() is used by QAbstractItemView.startDrag() as the default values when a drag occurs.
		"""
		res = super(Standard_QStandardItemModel,self).supportedDragActions()
		isinstance(res,QT.Qt.DropActions)
		return res
	#----------------------------------------------------------------------
	def supportedDropActions(self):
		"""
		Returns the drop actions supported by this model.
		The default implementation returns Qt.CopyAction
		Reimplement this function if you wish to support additional actions
		You must also reimplement the PySide.QT.QAbstractItemModel.dropMimeData() function to handle the additional operations.
		"""
		res = super(Standard_QStandardItemModel,self).supportedDropActions()
		isinstance(res,QT.Qt.DropActions)
		return res
	#----------------------------------------------------------------------
	def beginInsertColumns(self,parent,first,last):
		"""
		beginInsertColumns(parent,first,last)
			parent=QT.QModelIndex
			first=QT.int
			last=QT.int

		Begins a column insertion operation.
		When reimplementing PySide.QT.QAbstractItemModel.insertColumns() in a subclass, you must call this function before inserting data into the models underlying data store.
		The parent index corresponds to the parent into which the new columns are inserted; first and last are the column numbers of the new columns will have after they have been inserted.
		"""
		res = super(Standard_QStandardItemModel,self).beginInsertColumns(parent,first,last)
		return res
	#----------------------------------------------------------------------
	def beginInsertRows(self,parent,first,last):
		"""
		beginInsertRows(parent,first,last)
			parent=QT.QModelIndex
			first=QT.int
			last=QT.int

		Begins a row insertion operation.
		When reimplementing PySide.QT.QAbstractItemModel.insertRows() in a subclass, you must call this function before inserting data into the models underlying data store.
		The parent index corresponds to the parent into which the new rows are inserted; first and last are the row numbers that the new rows will have after they have been inserted.
		"""
		res = super(Standard_QStandardItemModel,self).beginInsertRows(parent,first,last)
		return res
	#----------------------------------------------------------------------
	def beginMoveColumns(self,sourceParent,sourceFirst,sourceLast,destinationParent,destinationColumn):
		"""
		beginMoveColumns(sourceParent,sourceFirst,sourceLast,destinationParent,destinationColumn)
			sourceParent=QT.QModelIndex
			sourceFirst=QT.int
			sourceLast=QT.int
			destinationParent=QT.QModelIndex
			destinationColumn=QT.int

		Begins a column move operation.
		When reimplementing a subclass, this method simplifies moving entities in your model
		This method is responsible for moving persistent indexes in the model, which you would otherwise be required to do yourself
		Using beginMoveRows and endMoveRows is an alternative to emitting layoutAboutToBeChanged and layoutChanged directly along with changePersistentIndexes
		layoutAboutToBeChanged is emitted by this method for compatibility reasons.
		The sourceParent index corresponds to the parent from which the columns are moved; sourceFirst and sourceLast are the first and last column numbers of the columns to be moved
		The destinationParent index corresponds to the parent into which those columns are moved
		The destinationChild is the column to which the columns will be moved
		That is, the index at column sourceFirst in sourceParent will become column destinationChild in destinationParent , followed by all other columns up to sourceLast .
		However, when moving columns down in the same parent (sourceParent and destinationParent are equal), the columnss will be placed before the destinationChild index
		That is, if you wish to move columns 0 and 1 so they will become columns 1 and 2, destinationChild should be 3
		In this case, the new index for the source column i (which is between sourceFirst and sourceLast ) is equal to (destinationChild-sourceLast-1+i) .
		Note that if sourceParent and destinationParent are the same, you must ensure that the destinationChild is not within the range of sourceFirst and sourceLast + 1
		You must also ensure that you do not attempt to move a column to one of its own children or ancestors
		This method returns false if either condition is true, in which case you should abort your move operation.
		"""
		res = super(Standard_QStandardItemModel,self).beginMoveColumns(sourceParent,sourceFirst,sourceLast,destinationParent,destinationColumn)

		return res
	#----------------------------------------------------------------------
	def beginMoveRows(self,sourceParent,sourceFirst,sourceLast,destinationParent,destinationRow):
		"""
		beginMoveRows(sourceParent,sourceFirst,sourceLast,destinationParent,destinationRow)
			sourceParent=QT.QModelIndex
			sourceFirst=QT.int
			sourceLast=QT.int
			destinationParent=QT.QModelIndex
			destinationRow=QT.int

		Begins a row move operation.
		When reimplementing a subclass, this method simplifies moving entities in your model
		This method is responsible for moving persistent indexes in the model, which you would otherwise be required to do yourself
		Using beginMoveRows and endMoveRows is an alternative to emitting layoutAboutToBeChanged and layoutChanged directly along with changePersistentIndexes
		layoutAboutToBeChanged is emitted by this method for compatibility reasons.
		The sourceParent index corresponds to the parent from which the rows are moved; sourceFirst and sourceLast are the first and last row numbers of the rows to be moved
		The destinationParent index corresponds to the parent into which those rows are moved
		The destinationChild is the row to which the rows will be moved
		That is, the index at row sourceFirst in sourceParent will become row destinationChild in destinationParent , followed by all other rows up to sourceLast .
		However, when moving rows down in the same parent (sourceParent and destinationParent are equal), the rows will be placed before the destinationChild index
		That is, if you wish to move rows 0 and 1 so they will become rows 1 and 2, destinationChild should be 3
		In this case, the new index for the source row i (which is between sourceFirst and sourceLast ) is equal to (destinationChild-sourceLast-1+i) .
		Note that if sourceParent and destinationParent are the same, you must ensure that the destinationChild is not within the range of sourceFirst and sourceLast + 1
		You must also ensure that you do not attempt to move a row to one of its own children or ancestors
		This method returns false if either condition is true, in which case you should abort your move operation.
		"""
		res = super(Standard_QStandardItemModel,self).beginMoveRows(sourceParent,sourceFirst,sourceLast,destinationParent,destinationRow)

		return res
	#----------------------------------------------------------------------
	def beginRemoveColumns(self,parent,first,last):
		"""
		beginRemoveColumns(parent,first,last)
			parent=QT.QModelIndex
			first=QT.int
			last=QT.int

		Begins a column removal operation.
		When reimplementing PySide.QT.QAbstractItemModel.removeColumns() in a subclass, you must call this function before removing data from the models underlying data store.
		The parent index corresponds to the parent from which the new columns are removed; first and last are the column numbers of the first and last columns to be removed.
		"""
		res = super(Standard_QStandardItemModel,self).beginRemoveColumns(parent,first,last)
		return res
	#----------------------------------------------------------------------
	def beginRemoveRows(self,parent,first,last):
		"""
		beginRemoveRows(parent,first,last)
			parent=QT.QModelIndex
			first=QT.int
			last=QT.int

		Begins a row removal operation.
		When reimplementing PySide.QT.QAbstractItemModel.removeRows() in a subclass, you must call this function before removing data from the models underlying data store.
		The parent index corresponds to the parent from which the new rows are removed; first and last are the row numbers of the rows to be removed.
		"""
		res = super(Standard_QStandardItemModel,self).beginRemoveRows(parent,first,last)
		return res
	#----------------------------------------------------------------------
	def buddy(self,index):
		"""
		buddy(index)
			index=QT.QModelIndex

		Returns a model index for the buddy of the item represented by index
		When the user wants to edit an item, the view will call this function to check whether another item in the model should be edited instead
		Then, the view will construct a delegate using the model index returned by the buddy item.
		The default implementation of this function has each item as its own buddy.
		"""
		res = super(Standard_QStandardItemModel,self).buddy(index)
		isinstance(res,QT.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def canFetchMore(self,parent):
		"""
		canFetchMore(parent)
			parent=QT.QModelIndex

		Returns true if there is more data available for parent ; otherwise returns false.
		The default implementation always returns false.
		If PySide.QT.QAbstractItemModel.canFetchMore() returns true, PySide.QT.QAbstractItemView will call PySide.QT.QAbstractItemModel.fetchMore()
		However, the PySide.QT.QAbstractItemModel.fetchMore() function is only called when the model is being populated incrementally.
		"""
		res = super(Standard_QStandardItemModel,self).canFetchMore(parent)

		return res
	#----------------------------------------------------------------------
	def changePersistentIndex(self,f,t):
		"""
		changePersistentIndex(f,t)
			from=QT.QModelIndex
			to=QT.QModelIndex

		Changes the PySide.QT.QPersistentModelIndex that is equal to the given from model index to the given to model index.
		If no persistent model index equal to the given from model index was found, nothing is changed.
		"""
		res = super(Standard_QStandardItemModel,self).changePersistentIndex(f,t)
		return res
	#----------------------------------------------------------------------
	def changePersistentIndexList(self,f,t):
		"""
		changePersistentIndexList(from,to)
			from=unKnown
			to=unKnown


		"""
		res = super(Standard_QStandardItemModel,self).changePersistentIndexList(f,t)
		return res
	#----------------------------------------------------------------------
	def columnCount(self,parent=None):
		"""
		columnCount(parent=None)
			parent=QT.QModelIndex

		Returns the number of columns for the children of the given parent .
		In most subclasses, the number of columns is independent of the parent .
		For example:
		"""
		res = super(Standard_QStandardItemModel,self).columnCount(parent)

		return res
	#----------------------------------------------------------------------
	def createIndex(self,*args,**kwargs):
		"""
		createIndex(row,column,id=None)
			row=QT.int
			column=QT.int
			id=QT.int

		createIndex(row,column,ptr)
			row=QT.int
			column=QT.int
			ptr=Object

		Use PySide.QT.QModelIndex QAbstractItemModel::createIndex(int row, int column, quint32 id) instead.
		"""
		res = super(Standard_QStandardItemModel,self).createIndex(*args,**kwargs)
		isinstance(res,QT.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def data(self,index,role=None):
		"""
		data(index,role=None)
			index=QT.QModelIndex
			role=QT.int

		Returns the data stored under the given role for the item referred to by the index .
		"""
		res = super(Standard_QStandardItemModel,self).data(index,role)
		return res
	#----------------------------------------------------------------------
	def decodeData(self,row,column,parent,stream):
		"""
		decodeData(row,column,parent,stream)
			row=QT.int
			column=QT.int
			parent=QT.QModelIndex
			stream=QT.QDataStream


		"""
		res = super(Standard_QStandardItemModel,self).decodeData(row,column,parent,stream)

		return res
	#----------------------------------------------------------------------
	def dropMimeData(self,data,action,row,column,parent):
		"""
		dropMimeData(data,action,row,column,parent)
			data=QT.QMimeData
			action=QT.Qt.DropAction
			row=QT.int
			column=QT.int
			parent=QT.QModelIndex


		"""
		res = super(Standard_QStandardItemModel,self).dropMimeData(data,action,row,column,parent)

		return res
	#----------------------------------------------------------------------
	def encodeData(self,indexes,stream):
		"""
		encodeData(indexes,stream)
			indexes=unKnown
			stream=QT.QDataStream


		"""
		res = super(Standard_QStandardItemModel,self).encodeData(indexes,stream)
		return res
	#----------------------------------------------------------------------
	def fetchMore(self,parent):
		"""
		fetchMore(parent)
			parent=QT.QModelIndex

		Fetches any available data for the items with the parent specified by the parent index.
		Reimplement this if you are populating your model incrementally.
		The default implementation does nothing.
		"""
		res = super(Standard_QStandardItemModel,self).fetchMore(parent)
		return res
	#----------------------------------------------------------------------
	def flags(self,index):
		"""
		flags(index)
			index=QT.QModelIndex

		Returns the item flags for the given index .
		The base class implementation returns a combination of flags that enables the item (ItemIsEnabled ) and allows it to be selected (ItemIsSelectable ).
		"""
		res = super(Standard_QStandardItemModel,self).flags(index)
		isinstance(res,QT.Qt.ItemFlags)
		return res
	#----------------------------------------------------------------------
	def hasChildren(self,parent=None):
		"""
		hasChildren(parent=None)
			parent=QT.QModelIndex

		Returns true if parent has any children; otherwise returns false.
		Use PySide.QT.QAbstractItemModel.rowCount() on the parent to find out the number of children.
		"""
		res = super(Standard_QStandardItemModel,self).hasChildren(parent)

		return res
	#----------------------------------------------------------------------
	def hasIndex(self,row,column,parent=None):
		"""
		hasIndex(row,column,parent=None)
			row=QT.int
			column=QT.int
			parent=QT.QModelIndex

		Returns true if the model returns a valid PySide.QT.QModelIndex for row and column with parent , otherwise returns false.
		"""
		res = super(Standard_QStandardItemModel,self).hasIndex(row,column,parent)

		return res
	#----------------------------------------------------------------------
	def headerData(self,section,orientation,role=None):
		"""
		headerData(section,orientation,role=None)
			section=QT.int
			orientation=QT.Qt.Orientation
			role=QT.int


		"""
		res = super(Standard_QStandardItemModel,self).headerData(section,orientation,role)
		return res
	#----------------------------------------------------------------------
	def index(self,row,column,parent=None):
		"""
		index(row,column,parent=None)
			row=QT.int
			column=QT.int
			parent=QT.QModelIndex

		Returns the index of the item in the model specified by the given row , column and parent index.
		When reimplementing this function in a subclass, call PySide.QT.QAbstractItemModel.createIndex() to generate model indexes that other components can use to refer to items in your model.
		"""
		res = super(Standard_QStandardItemModel,self).index(row,column,parent)
		isinstance(res,QT.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def insertColumn(self,column,parent=None):
		"""
		insertColumn(column,parent=None)
			column=QT.int
			parent=QT.QModelIndex

		Inserts a single column before the given column in the child items of the parent specified.
		Returns true if the column is inserted; otherwise returns false.
		"""
		res = super(Standard_QStandardItemModel,self).insertColumn(column,parent)

		return res
	#----------------------------------------------------------------------
	def insertColumns(self,column,count,parent=None):
		"""
		insertColumns(column,count,parent=None)
			column=QT.int
			count=QT.int
			parent=QT.QModelIndex

		On models that support this, inserts count new columns into the model before the given column
		The items in each new column will be children of the item represented by the parent model index.
		If column is 0, the columns are prepended to any existing columns.
		If column is PySide.QT.QAbstractItemModel.columnCount() , the columns are appended to any existing columns.
		If parent has no children, a single row with count columns is inserted.
		Returns true if the columns were successfully inserted; otherwise returns false.
		The base class implementation does nothing and returns false.
		If you implement your own model, you can reimplement this function if you want to support insertions
		Alternatively, you can provide your own API for altering the data.
		"""
		res = super(Standard_QStandardItemModel,self).insertColumns(column,count,parent)

		return res
	#----------------------------------------------------------------------
	def insertRow(self,row,parent=None):
		"""
		insertRow(row,parent=None)
			row=QT.int
			parent=QT.QModelIndex

		Inserts a single row before the given row in the child items of the parent specified.
		Returns true if the row is inserted; otherwise returns false.
		"""
		res = super(Standard_QStandardItemModel,self).insertRow(row,parent)

		return res
	#----------------------------------------------------------------------
	def insertRows(self,row,count,parent=None):
		"""
		insertRows(row,count,parent=None)
			row=QT.int
			count=QT.int
			parent=QT.QModelIndex

		On models that support this, inserts count rows into the model before the given row
		Items in the new row will be children of the item represented by the parent model index.
		If row is 0, the rows are prepended to any existing rows in the parent.
		If row is PySide.QT.QAbstractItemModel.rowCount() , the rows are appended to any existing rows in the parent.
		If parent has no children, a single column with count rows is inserted.
		Returns true if the rows were successfully inserted; otherwise returns false.
		If you implement your own model, you can reimplement this function if you want to support insertions
		Alternatively, you can provide your own API for altering the data
		In either case, you will need to call PySide.QT.QAbstractItemModel.beginInsertRows() and PySide.QT.QAbstractItemModel.endInsertRows() to notify other components that the model has changed.
		"""
		res = super(Standard_QStandardItemModel,self).insertRows(row,count,parent)

		return res
	#----------------------------------------------------------------------
	def itemData(self,index):
		"""
		itemData(index)
			index=QT.QModelIndex

		Returns a map with values for all predefined roles in the model for the item at the given index .
		Reimplement this function if you want to extend the default behavior of this function to include custom roles in the map.
		"""
		res = super(Standard_QStandardItemModel,self).itemData(index)
		return res
	#----------------------------------------------------------------------
	def match(self,start,role,value,hits=None,flags=None):
		"""
		match(start,role,value,hits=None,flags=None)
			start=QT.QModelIndex
			role=QT.int
			value=object
			hits=QT.int
			flags=QT.Qt.MatchFlags


		"""
		res = super(Standard_QStandardItemModel,self).match(start,role,value,hits,flags)
		return res
	#----------------------------------------------------------------------
	def mimeData(self, *args, **kwargs):
		"""
		mimeData(indexes)
			indexes=unKnown


		"""
		res = super(Standard_QStandardItemModel,self).mimeData(*args, **kwargs)
		isinstance(res, QT.QMimeData)
		return res
	#----------------------------------------------------------------------
	def parent(self,child):
		"""
		parent(child)
			child=QT.QModelIndex

		Returns the parent of the model item with the given index
		If the item has no parent, an invalid PySide.QT.QModelIndex is returned.
		A common convention used in models that expose tree data structures is that only items in the first column have children
		For that case, when reimplementing this function in a subclass the column of the returned PySide.QT.QModelIndex would be 0.
		When reimplementing this function in a subclass, be careful to avoid calling PySide.QT.QModelIndex member functions, such as QModelIndex.parent() , since indexes belonging to your model will simply call your implementation, leading to infinite recursion.
		"""
		res = super(Standard_QStandardItemModel,self).parent(child)
		isinstance(res,QT.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def parentWidget(self):
		""" """
		res = QT.QObject.parent(self)
		isinstance(res,QT.QObject)
		return res
	#----------------------------------------------------------------------
	def removeColumn(self,column,parent=None):
		"""
		removeColumn(column,parent=None)
			column=QT.int
			parent=QT.QModelIndex

		Removes the given column from the child items of the parent specified.
		Returns true if the column is removed; otherwise returns false.
		"""
		res = super(Standard_QStandardItemModel,self).removeColumn(column,parent)

		return res
	#----------------------------------------------------------------------
	def removeColumns(self,column,count,parent=None):
		"""
		removeColumns(column,count,parent=None)
			column=QT.int
			count=QT.int
			parent=QT.QModelIndex

		On models that support this, removes count columns starting with the given column under parent parent from the model.
		Returns true if the columns were successfully removed; otherwise returns false.
		The base class implementation does nothing and returns false.
		If you implement your own model, you can reimplement this function if you want to support removing
		Alternatively, you can provide your own API for altering the data.
		"""
		res = super(Standard_QStandardItemModel,self).removeColumns(column,count,parent)

		return res
	#----------------------------------------------------------------------
	def removeRow(self,row,parent=None):
		"""
		removeRow(row,parent=None)
			row=QT.int
			parent=QT.QModelIndex

		Removes the given row from the child items of the parent specified.
		Returns true if the row is removed; otherwise returns false.
		This is a convenience function that calls PySide.QT.QAbstractItemModel.removeRows()
		The PySide.QT.QAbstractItemModel implementation of PySide.QT.QAbstractItemModel.removeRows() does nothing.
		"""
		res = super(Standard_QStandardItemModel,self).removeRow(row,parent)

		return res
	#----------------------------------------------------------------------
	def removeRows(self,row,count,parent=None):
		"""
		removeRows(row,count,parent=None)
			row=QT.int
			count=QT.int
			parent=QT.QModelIndex

		On models that support this, removes count rows starting with the given row under parent parent from the model.
		Returns true if the rows were successfully removed; otherwise returns false.
		The base class implementation does nothing and returns false.
		If you implement your own model, you can reimplement this function if you want to support removing
		Alternatively, you can provide your own API for altering the data.
		"""
		res = super(Standard_QStandardItemModel,self).removeRows(row,count,parent)

		return res
	#----------------------------------------------------------------------
	def rowCount(self,parent=None):
		"""
		rowCount(parent=None)
			parent=QT.QModelIndex

		Returns the number of rows under the given parent
		When the parent is valid it means that rowCount is returning the number of children of parent.
		"""
		res = super(Standard_QStandardItemModel,self).rowCount(parent)

		return res
	#----------------------------------------------------------------------
	def setData(self,index,value,role=None):
		"""
		setData(index,value,role=None)
			index=QT.QModelIndex
			value=object
			role=QT.int

		Sets the role data for the item at index to value .
		Returns true if successful; otherwise returns false.
		The PySide.QT.QAbstractItemModel.dataChanged() signal should be emitted if the data was successfully set.
		The base class implementation returns false
		This function and PySide.QT.QAbstractItemModel.data() must be reimplemented for editable models.
		"""
		res = super(Standard_QStandardItemModel,self).setData(index,value,role)

		return res
	#----------------------------------------------------------------------
	def setHeaderData(self,section,orientation,value,role=None):
		"""
		setHeaderData(section,orientation,value,role=None)
			section=QT.int
			orientation=QT.Qt.Orientation
			value=object
			role=QT.int


		"""
		res = super(Standard_QStandardItemModel,self).setHeaderData(section,orientation,value,role)

		return res
	#----------------------------------------------------------------------
	def setItemData(self,index,roles):
		"""
		setItemData(index,roles)
			index=QT.QModelIndex
			roles=unKnown


		"""
		res = super(Standard_QStandardItemModel,self).setItemData(index,roles)

		return res
	#----------------------------------------------------------------------
	def setRoleNames(self,roleNames):
		"""
		setRoleNames(roleNames)
			roleNames=unKnown


		"""
		res = super(Standard_QStandardItemModel,self).setRoleNames(roleNames)
		return res
	#----------------------------------------------------------------------
	def setSupportedDragActions(self,arg__1):
		"""
		setSupportedDragActions(arg__1)
			arg__1=QT.Qt.DropActions


		"""
		res = super(Standard_QStandardItemModel,self).setSupportedDragActions(arg__1)
		return res
	#----------------------------------------------------------------------
	def sibling(self,row,column,idx):
		"""
		sibling(row,column,idx)
			row=QT.int
			column=QT.int
			idx=QT.QModelIndex

		Returns the sibling at row and column for the item at index , or an invalid PySide.QT.QModelIndex if there is no sibling at that location.
		PySide.QT.QAbstractItemModel.sibling() is just a convenience function that finds the items parent, and uses it to retrieve the index of the child item in the specified row and column .
		"""
		res = super(Standard_QStandardItemModel,self).sibling(row,column,idx)
		isinstance(res,QT.QModelIndex)
		return res
	##----------------------------------------------------------------------
	#def sort(self,column,order=None):
		#"""
		#sort(column,order=None)
			#column=QT.int
			#order=QT.Qt.SortOrder


		#"""
		#res = super(QStandardItemModel,self).sort(column,order)
		#return res
	#----------------------------------------------------------------------
	def span(self,index):
		"""
		span(index)
			index=QT.QModelIndex

		Returns the row and column span of the item represented by index .
		"""
		res = super(Standard_QStandardItemModel,self).span(index)
		isinstance(res,QT.QSize)
		return res

	BeginResetModel        = property(beginResetModel)
	EndInsertColumns       = property(endInsertColumns)
	EndInsertRows          = property(endInsertRows)
	EndMoveColumns         = property(endMoveColumns)
	EndMoveRows            = property(endMoveRows)
	EndRemoveColumns       = property(endRemoveColumns)
	EndRemoveRows          = property(endRemoveRows)
	EndResetModel          = property(endResetModel)
	LayoutAboutToBeChanged = property(layoutAboutToBeChanged)
	LayoutChanged          = property(layoutChanged)
	MimeTypes              = property(mimeTypes)
	ModelAboutToBeReset    = property(modelAboutToBeReset)
	ModelReset             = property(modelReset)
	PersistentIndexList    = property(persistentIndexList)
	Reset                  = property(reset)
	Revert                 = property(revert)
	RoleNames              = property(roleNames)
	Submit                 = property(submit)
	SupportedDragActions   = property(supportedDragActions)
	SupportedDropActions   = property(supportedDropActions)
	Clear                  = property(clear)
	InvisibleRootItem      = property(invisibleRootItem)
	ItemPrototype          = property(itemPrototype)
	SortRole               = property(sortRole)

