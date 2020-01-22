from .... import QT

class Standard_QSortFilterProxyModel(QT.QSortFilterProxyModel):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(Standard_QSortFilterProxyModel,self).__init__(*args,**kwargs)
	def source_Index_From_Item(self,item):
		index = self.mapFromSource(item.index())
		return index
	#----------------------------------------------------------------------
	def item_From_Index(self,index):
		""""""
		if not index.model() == self:
			index = self.mapToSource(index)
		item = self.sourceModel().itemFromIndex(index)
		return item
	#----------------------------------------------------------------------
	def invalidateFilter(self):
		"""
		Invalidates the current filtering.
		This function should be called if you are implementing custom filtering (e.g
		PySide.QT.QSortFilterProxyModel.filterAcceptsRow() ), and your filter parameters have changed.
		"""
		res = super(Standard_QSortFilterProxyModel,self).invalidateFilter()
		return res
	#----------------------------------------------------------------------
	def sortColumn(self):
		"""
		the column currently used for sorting
		This returns the most recently used sort column.
		"""
		res = super(Standard_QSortFilterProxyModel,self).sortColumn()
		
		return res
	#----------------------------------------------------------------------
	def sortOrder(self):
		"""
		the order currently used for sorting
		This returns the most recently used sort order.
		"""
		res = super(Standard_QSortFilterProxyModel,self).sortOrder()
		isinstance(res,QT.Qt.SortOrder)
		return res
	#----------------------------------------------------------------------
	def filterAcceptsColumn(self,source_column,source_parent):
		"""
		filterAcceptsColumn(source_column,source_parent)
			source_column=QT.int
			source_parent=QT.QModelIndex

		Returns true if the item in the column indicated by the given source_column and source_parent should be included in the model; otherwise returns false.
		The default implementation returns true if the value held by the relevant item matches the filter string, wildcard string or regular expression.
		"""
		res = super(Standard_QSortFilterProxyModel,self).filterAcceptsColumn(source_column,source_parent)
		
		return res
	#----------------------------------------------------------------------
	def filterAcceptsRow(self,source_row,source_parent):
		"""
		filterAcceptsRow(source_row,source_parent)
			source_row=QT.int
			source_parent=QT.QModelIndex

		Returns true if the item in the row indicated by the given source_row and source_parent should be included in the model; otherwise returns false.
		The default implementation returns true if the value held by the relevant item matches the filter string, wildcard string or regular expression.
		"""
		res = super(Standard_QSortFilterProxyModel,self).filterAcceptsRow(source_row,source_parent)
		
		return res
	#----------------------------------------------------------------------
	def lessThan(self,left,right):
		"""
		lessThan(left,right)
			left=QT.QModelIndex
			right=QT.QModelIndex

		Returns true if the value of the item referred to by the given index left is less than the value of the item referred to by the given index right , otherwise returns false.
		This function is used as the < operator when sorting, and handles the following PySide.QT.QVariant types:
		Any other type will be converted to a PySide.QT.QString using QVariant.toString() .
		Comparison of PySide.QT.QString s is case sensitive by default; this can be changed using the PySide.QT.QSortFilterProxyModel.sortCaseSensitivity() property.
		By default, the Qt.DisplayRole associated with the PySide.QT.QModelIndex es is used for comparisons
		This can be changed by setting the PySide.QT.QSortFilterProxyModel.sortRole() property.
		"""
		res = super(Standard_QSortFilterProxyModel,self).lessThan(left,right)
		
		return res
	#----------------------------------------------------------------------
	def filterCaseSensitivity(self):
		"""
		This property holds the case sensitivity of the PySide.QT.QRegExp pattern used to filter the contents of the source model.
		By default, the filter is case sensitive.
		"""
		res = super(Standard_QSortFilterProxyModel,self).filterCaseSensitivity()
		isinstance(res,QT.Qt.CaseSensitivity)
		return res
	#----------------------------------------------------------------------
	def setFilterCaseSensitivity(self,cs):
		"""
		setFilterCaseSensitivity(cs)
			cs=QT.Qt.CaseSensitivity

		This property holds the case sensitivity of the PySide.QT.QRegExp pattern used to filter the contents of the source model.
		By default, the filter is case sensitive.
		"""
		res = super(Standard_QSortFilterProxyModel,self).setFilterCaseSensitivity(cs)
		return res
	#----------------------------------------------------------------------
	def filterKeyColumn(self):
		"""
		This property holds the column where the key used to filter the contents of the source model is read from..
		The default value is 0
		If the value is -1, the keys will be read from all columns.
		"""
		res = super(Standard_QSortFilterProxyModel,self).filterKeyColumn()
		
		return res
	#----------------------------------------------------------------------
	def setFilterKeyColumn(self,column):
		"""
		setFilterKeyColumn(column)
			column=QT.int

		This property holds the column where the key used to filter the contents of the source model is read from..
		The default value is 0
		If the value is -1, the keys will be read from all columns.
		"""
		res = super(Standard_QSortFilterProxyModel,self).setFilterKeyColumn(column)
		return res
	#----------------------------------------------------------------------
	def filterRegExp(self):
		"""
		This property holds the PySide.QT.QRegExp used to filter the contents of the source model.
		Setting this property overwrites the current PySide.QT.QSortFilterProxyModel.filterCaseSensitivity()
		By default, the PySide.QT.QRegExp is an empty string matching all contents.
		If no PySide.QT.QRegExp or an empty string is set, everything in the source model will be accepted.
		"""
		res = super(Standard_QSortFilterProxyModel,self).filterRegExp()
		isinstance(res,QT.QRegExp)
		return res	
	#----------------------------------------------------------------------
	def setFilterRegExp(self,*args,**kwargs):
		"""
		setFilterRegExp(regExp)
			regExp=QT.QRegExp

		setFilterRegExp(pattern)
			pattern=unicode

		This property holds the PySide.QT.QRegExp used to filter the contents of the source model.
		Setting this property overwrites the current PySide.QT.QSortFilterProxyModel.filterCaseSensitivity()
		By default, the PySide.QT.QRegExp is an empty string matching all contents.
		If no PySide.QT.QRegExp or an empty string is set, everything in the source model will be accepted.
		"""
		res = super(Standard_QSortFilterProxyModel,self).setFilterRegExp(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def filterRole(self):
		"""
		This property holds the item role that is used to query the source models data when filtering items.
		The default value is Qt.DisplayRole .
		"""
		res = super(Standard_QSortFilterProxyModel,self).filterRole()
		
		return res
	#----------------------------------------------------------------------
	def setFilterRole(self,role):
		"""
		setFilterRole(role)
			role=QT.int

		This property holds the item role that is used to query the source models data when filtering items.
		The default value is Qt.DisplayRole .
		"""
		res = super(Standard_QSortFilterProxyModel,self).setFilterRole(role)
		return res
	#----------------------------------------------------------------------
	def sortCaseSensitivity(self):
		"""
		This property holds the case sensitivity setting used for comparing strings when sorting.
		By default, sorting is case sensitive.
		"""
		res = super(Standard_QSortFilterProxyModel,self).sortCaseSensitivity()
		isinstance(res,QT.Qt.CaseSensitivity)
		return res
	#----------------------------------------------------------------------
	def setSortCaseSensitivity(self,cs):
		"""
		setSortCaseSensitivity(cs)
			cs=QT.Qt.CaseSensitivity

		This property holds the case sensitivity setting used for comparing strings when sorting.
		By default, sorting is case sensitive.
		"""
		res = super(Standard_QSortFilterProxyModel,self).setSortCaseSensitivity(cs)
		return res
	#----------------------------------------------------------------------
	def isSortLocaleAware(self):
		"""
		This property holds the local aware setting used for comparing strings when sorting.
		By default, sorting is not local aware.
		"""
		res = super(Standard_QSortFilterProxyModel,self).isSortLocaleAware()
		
		return res
	#----------------------------------------------------------------------
	def setSortLocaleAware(self,on):
		"""
		setSortLocaleAware(on)
			on=QT.bool

		This property holds the local aware setting used for comparing strings when sorting.
		By default, sorting is not local aware.
		"""
		res = super(Standard_QSortFilterProxyModel,self).setSortLocaleAware(on)
		return res
	#----------------------------------------------------------------------
	def sortRole(self):
		"""
		This property holds the item role that is used to query the source models data when sorting items.
		The default value is Qt.DisplayRole .
		"""
		res = super(Standard_QSortFilterProxyModel,self).sortRole()
		
		return res
	#----------------------------------------------------------------------
	def setSortRole(self,role):
		"""
		setSortRole(role)
			role=QT.int

		This property holds the item role that is used to query the source models data when sorting items.
		The default value is Qt.DisplayRole .
		"""
		res = super(Standard_QSortFilterProxyModel,self).setSortRole(role)
		return res
	#----------------------------------------------------------------------
	def dynamicSortFilter(self):
		"""
		This property holds whether the proxy model is dynamically sorted and filtered whenever the contents of the source model change.
		Note that you should not update the source model through the proxy model when PySide.QT.QSortFilterProxyModel.dynamicSortFilter() is true
		For instance, if you set the proxy model on a PySide.QT.QComboBox , then using functions that update the model, e.g., PySide.QT.QComboBox.addItem() , will not work as expected
		An alternative is to set PySide.QT.QSortFilterProxyModel.dynamicSortFilter() to false and call PySide.QT.QSortFilterProxyModel.sort() after adding items to the PySide.QT.QComboBox .
		The default value is false.
		"""
		res = super(Standard_QSortFilterProxyModel,self).dynamicSortFilter()
		
		return res
	#----------------------------------------------------------------------
	def setDynamicSortFilter(self,enable):
		"""
		setDynamicSortFilter(enable)
			enable=QT.bool

		This property holds whether the proxy model is dynamically sorted and filtered whenever the contents of the source model change.
		Note that you should not update the source model through the proxy model when PySide.QT.QSortFilterProxyModel.dynamicSortFilter() is true
		For instance, if you set the proxy model on a PySide.QT.QComboBox , then using functions that update the model, e.g., PySide.QT.QComboBox.addItem() , will not work as expected
		An alternative is to set PySide.QT.QSortFilterProxyModel.dynamicSortFilter() to false and call PySide.QT.QSortFilterProxyModel.sort() after adding items to the PySide.QT.QComboBox .
		The default value is false.
		"""
		res = super(Standard_QSortFilterProxyModel,self).setDynamicSortFilter(enable)
		return res
	

	#----------------------------------------------------------------------
	def sourceModel(self):
		"""
		Returns the model that contains the data that is available through the proxy model.
		"""
		res = super(Standard_QSortFilterProxyModel,self).sourceModel()
		isinstance(res,QT.QStandardItemModel)
		return res
	#----------------------------------------------------------------------
	def mapFromSource(self,sourceIndex):
		"""
		mapFromSource(sourceIndex)
			sourceIndex=QT.QModelIndex

		Reimplement this function to return the model index in the proxy model that corresponds to the sourceIndex from the source model.
		"""
		res = super(Standard_QSortFilterProxyModel,self).mapFromSource(sourceIndex)
		isinstance(res,QT.QModelIndex)
		if res.isValid():
			if self.sourceModel() != sourceIndex.model():
				raise IndexError("invalied index")
		return res
	#----------------------------------------------------------------------
	def mapSelectionFromSource(self,selection):
		"""
		mapSelectionFromSource(selection)
			selection=QT.QItemSelection

		Returns a proxy selection mapped from the specified sourceSelection .
		Reimplement this method to map source selections to proxy selections.
		"""
		res = super(Standard_QSortFilterProxyModel,self).mapSelectionFromSource(selection)
		return res
	#----------------------------------------------------------------------
	def mapSelectionToSource(self,selection):
		"""
		mapSelectionToSource(selection)
			selection=QT.QItemSelection

		Returns a source selection mapped from the specified proxySelection .
		Reimplement this method to map proxy selections to source selections.
		"""
		res = super(Standard_QSortFilterProxyModel,self).mapSelectionToSource(selection)
		return res
	#----------------------------------------------------------------------
	def mapToSource(self,proxyIndex):
		"""
		mapToSource(proxyIndex)
			proxyIndex=QT.QModelIndex

		Reimplement this function to return the model index in the source model that corresponds to the proxyIndex in the proxy model.
		"""
		res = super(Standard_QSortFilterProxyModel,self).mapToSource(proxyIndex)
		isinstance(res,QT.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def setSourceModel(self,sourceModel):
		"""
		setSourceModel(sourceModel)
			sourceModel=QT.QAbstractItemModel

		Sets the given sourceModel to be processed by the proxy model.
		"""
		res = super(Standard_QSortFilterProxyModel,self).setSourceModel(sourceModel)
		return res
	
	
	
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
		res = super(Standard_QSortFilterProxyModel,self).beginResetModel()
		return res
	#----------------------------------------------------------------------
	def endInsertColumns(self):
		"""
		Ends a column insertion operation.
		When reimplementing PySide.QT.QAbstractItemModel.insertColumns() in a subclass, you must call this function after inserting data into the models underlying data store.
		"""
		res = super(Standard_QSortFilterProxyModel,self).endInsertColumns()
		return res
	#----------------------------------------------------------------------
	def endInsertRows(self):
		"""
		Ends a row insertion operation.
		When reimplementing PySide.QT.QAbstractItemModel.insertRows() in a subclass, you must call this function after inserting data into the models underlying data store.
		"""
		res = super(Standard_QSortFilterProxyModel,self).endInsertRows()
		return res
	#----------------------------------------------------------------------
	def endMoveColumns(self):
		"""
		Ends a column move operation.
		When implementing a subclass, you must call this function after moving data within the models underlying data store.
		layoutChanged is emitted by this method for compatibility reasons.
		"""
		res = super(Standard_QSortFilterProxyModel,self).endMoveColumns()
		return res
	#----------------------------------------------------------------------
	def endMoveRows(self):
		"""
		Ends a row move operation.
		When implementing a subclass, you must call this function after moving data within the models underlying data store.
		layoutChanged is emitted by this method for compatibility reasons.
		"""
		res = super(Standard_QSortFilterProxyModel,self).endMoveRows()
		return res
	#----------------------------------------------------------------------
	def endRemoveColumns(self):
		"""
		Ends a column removal operation.
		When reimplementing PySide.QT.QAbstractItemModel.removeColumns() in a subclass, you must call this function after removing data from the models underlying data store.
		"""
		res = super(Standard_QSortFilterProxyModel,self).endRemoveColumns()
		return res
	#----------------------------------------------------------------------
	def endRemoveRows(self):
		"""
		Ends a row removal operation.
		When reimplementing PySide.QT.QAbstractItemModel.removeRows() in a subclass, you must call this function after removing data from the models underlying data store.
		"""
		res = super(Standard_QSortFilterProxyModel,self).endRemoveRows()
		return res
	#----------------------------------------------------------------------
	def endResetModel(self):
		"""
		Completes a model reset operation.
		You must call this function after resetting any internal data structure in your model or proxy model.
		"""
		res = super(Standard_QSortFilterProxyModel,self).endResetModel()
		return res
	#----------------------------------------------------------------------
	def layoutAboutToBeChanged(self):
		"""

		"""
		res = super(Standard_QSortFilterProxyModel,self).layoutAboutToBeChanged()
		return res
	#----------------------------------------------------------------------
	def layoutChanged(self):
		"""

		"""
		res = super(Standard_QSortFilterProxyModel,self).layoutChanged()
		return res
	#----------------------------------------------------------------------
	def mimeTypes(self):
		"""
		Returns a list of MIME types that can be used to describe a list of model indexes.
		"""
		res = super(Standard_QSortFilterProxyModel,self).mimeTypes()
		return res
	#----------------------------------------------------------------------
	def modelAboutToBeReset(self):
		"""

		"""
		res = super(Standard_QSortFilterProxyModel,self).modelAboutToBeReset()
		return res
	#----------------------------------------------------------------------
	def modelReset(self):
		"""

		"""
		res = super(Standard_QSortFilterProxyModel,self).modelReset()
		return res
	#----------------------------------------------------------------------
	def persistentIndexList(self):
		"""
		Returns the list of indexes stored as persistent indexes in the model.
		"""
		res = super(Standard_QSortFilterProxyModel,self).persistentIndexList()
		return res
	#----------------------------------------------------------------------
	def reset(self):
		"""
		Resets the model to its original state in any attached views.
		"""
		res = super(Standard_QSortFilterProxyModel,self).reset()
		return res
	#----------------------------------------------------------------------
	def revert(self):
		"""
		Lets the model know that it should discard cached information
		This function is typically used for row editing.
		"""
		res = super(Standard_QSortFilterProxyModel,self).revert()
		return res
	#----------------------------------------------------------------------
	def roleNames(self):
		"""
		Returns the models role names.
		"""
		res = super(Standard_QSortFilterProxyModel,self).roleNames()
		return res
	#----------------------------------------------------------------------
	def submit(self):
		"""
		Lets the model know that it should submit cached information to permanent storage
		This function is typically used for row editing.
		Returns true if there is no error; otherwise returns false.
		"""
		res = super(Standard_QSortFilterProxyModel,self).submit()

		return res
	#----------------------------------------------------------------------
	def supportedDragActions(self):
		"""
		Returns the actions supported by the data in this model.
		The default implementation returns PySide.QT.QAbstractItemModel.supportedDropActions() unless specific values have been set with PySide.QT.QAbstractItemModel.setSupportedDragActions() .
		PySide.QT.QAbstractItemModel.supportedDragActions() is used by QAbstractItemView.startDrag() as the default values when a drag occurs.
		"""
		res = super(Standard_QSortFilterProxyModel,self).supportedDragActions()
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
		res = super(Standard_QSortFilterProxyModel,self).supportedDropActions()
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
		res = super(Standard_QSortFilterProxyModel,self).beginInsertColumns(parent,first,last)
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
		res = super(Standard_QSortFilterProxyModel,self).beginInsertRows(parent,first,last)
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
		res = super(Standard_QSortFilterProxyModel,self).beginMoveColumns(sourceParent,sourceFirst,sourceLast,destinationParent,destinationColumn)

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
		res = super(Standard_QSortFilterProxyModel,self).beginMoveRows(sourceParent,sourceFirst,sourceLast,destinationParent,destinationRow)

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
		res = super(Standard_QSortFilterProxyModel,self).beginRemoveColumns(parent,first,last)
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
		res = super(Standard_QSortFilterProxyModel,self).beginRemoveRows(parent,first,last)
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
		res = super(Standard_QSortFilterProxyModel,self).buddy(index)
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
		res = super(Standard_QSortFilterProxyModel,self).canFetchMore(parent)

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
		res = super(Standard_QSortFilterProxyModel,self).changePersistentIndex(f,t)
		return res
	#----------------------------------------------------------------------
	def changePersistentIndexList(self,f,t):
		"""
		changePersistentIndexList(from,to)
			from=unKnown
			to=unKnown


		"""
		res = super(Standard_QSortFilterProxyModel,self).changePersistentIndexList(f,t)
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
		res = super(Standard_QSortFilterProxyModel,self).columnCount(parent)

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
		res = super(Standard_QSortFilterProxyModel,self).createIndex(*args,**kwargs)
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
		res = super(Standard_QSortFilterProxyModel,self).data(index,role)
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
		res = super(Standard_QSortFilterProxyModel,self).decodeData(row,column,parent,stream)

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
		res = super(Standard_QSortFilterProxyModel,self).dropMimeData(data,action,row,column,parent)

		return res
	#----------------------------------------------------------------------
	def encodeData(self,indexes,stream):
		"""
		encodeData(indexes,stream)
			indexes=unKnown
			stream=QT.QDataStream


		"""
		res = super(Standard_QSortFilterProxyModel,self).encodeData(indexes,stream)
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
		res = super(Standard_QSortFilterProxyModel,self).fetchMore(parent)
		return res
	#----------------------------------------------------------------------
	def flags(self,index):
		"""
		flags(index)
			index=QT.QModelIndex

		Returns the item flags for the given index .
		The base class implementation returns a combination of flags that enables the item (ItemIsEnabled ) and allows it to be selected (ItemIsSelectable ).
		"""
		res = super(Standard_QSortFilterProxyModel,self).flags(index)
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
		res = super(Standard_QSortFilterProxyModel,self).hasChildren(parent)

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
		res = super(Standard_QSortFilterProxyModel,self).hasIndex(row,column,parent)

		return res
	#----------------------------------------------------------------------
	def headerData(self,section,orientation,role=None):
		"""
		headerData(section,orientation,role=None)
			section=QT.int
			orientation=QT.Qt.Orientation
			role=QT.int


		"""
		res = super(Standard_QSortFilterProxyModel,self).headerData(section,orientation,role)
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
		res = super(Standard_QSortFilterProxyModel,self).index(row,column,parent)
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
		res = super(Standard_QSortFilterProxyModel,self).insertColumn(column,parent)

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
		res = super(Standard_QSortFilterProxyModel,self).insertColumns(column,count,parent)

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
		res = super(Standard_QSortFilterProxyModel,self).insertRow(row,parent)

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
		res = super(Standard_QSortFilterProxyModel,self).insertRows(row,count,parent)

		return res
	#----------------------------------------------------------------------
	def itemData(self,index):
		"""
		itemData(index)
			index=QT.QModelIndex

		Returns a map with values for all predefined roles in the model for the item at the given index .
		Reimplement this function if you want to extend the default behavior of this function to include custom roles in the map.
		"""
		res = super(Standard_QSortFilterProxyModel,self).itemData(index)
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
		res = super(Standard_QSortFilterProxyModel,self).match(start,role,value,hits,flags)
		return res
	#----------------------------------------------------------------------
	def mimeData(self,indexes):
		"""
		mimeData(indexes)
			indexes=unKnown


		"""
		res = super(Standard_QSortFilterProxyModel,self).mimeData(indexes)
		isinstance(res,QT.QMimeData)
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
		res = super(Standard_QSortFilterProxyModel,self).parent(child)
		isinstance(res,QT.QModelIndex)
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
		res = super(Standard_QSortFilterProxyModel,self).removeColumn(column,parent)

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
		res = super(Standard_QSortFilterProxyModel,self).removeColumns(column,count,parent)

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
		res = super(Standard_QSortFilterProxyModel,self).removeRow(row,parent)

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
		res = super(Standard_QSortFilterProxyModel,self).removeRows(row,count,parent)

		return res
	#----------------------------------------------------------------------
	def rowCount(self,parent=None):
		"""
		rowCount(parent=None)
			parent=QT.QModelIndex

		Returns the number of rows under the given parent
		When the parent is valid it means that rowCount is returning the number of children of parent.
		"""
		res = super(Standard_QSortFilterProxyModel,self).rowCount(parent)

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
		res = super(Standard_QSortFilterProxyModel,self).setData(index,value,role)

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
		res = super(Standard_QSortFilterProxyModel,self).setHeaderData(section,orientation,value,role)

		return res
	#----------------------------------------------------------------------
	def setItemData(self,index,roles):
		"""
		setItemData(index,roles)
			index=QT.QModelIndex
			roles=unKnown


		"""
		res = super(Standard_QSortFilterProxyModel,self).setItemData(index,roles)

		return res
	#----------------------------------------------------------------------
	def setRoleNames(self,roleNames):
		"""
		setRoleNames(roleNames)
			roleNames=unKnown


		"""
		res = super(Standard_QSortFilterProxyModel,self).setRoleNames(roleNames)
		return res
	#----------------------------------------------------------------------
	def setSupportedDragActions(self,arg__1):
		"""
		setSupportedDragActions(arg__1)
			arg__1=QT.Qt.DropActions


		"""
		res = super(Standard_QSortFilterProxyModel,self).setSupportedDragActions(arg__1)
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
		res = super(Standard_QSortFilterProxyModel,self).sibling(row,column,idx)
		isinstance(res,QT.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def sort(self,column=0,order=QT.Qt.AscendingOrder):
		"""
		sort(column,order=None)
			column=QT.int
			order=QT.Qt.SortOrder


		"""
		res = super(Standard_QSortFilterProxyModel,self).sort(column,order)
		return res
	#----------------------------------------------------------------------
	def span(self,index):
		"""
		span(index)
			index=QT.QModelIndex

		Returns the row and column span of the item represented by index .
		"""
		res = super(Standard_QSortFilterProxyModel,self).span(index)
		isinstance(res,QT.QSize)
		return res

	SourceModel = property(sourceModel,setSourceModel)
	SortColumn            = property(sortColumn)
	SortOrder             = property(sortOrder)
	FilterCaseSensitivity = property(filterCaseSensitivity,setFilterCaseSensitivity)
	FilterKeyColumn       = property(filterKeyColumn,setFilterKeyColumn)
	FilterRegExp          = property(filterRegExp,setFilterRegExp)
	FilterRole            = property(filterRole,setFilterRole)
	SortCaseSensitivity   = property(sortCaseSensitivity,setSortCaseSensitivity)
	SortLocaleAware       = property(isSortLocaleAware,setSortLocaleAware)
	SortRole              = property(sortRole,setSortRole)
	DynamicSortFilter     = property(dynamicSortFilter,setDynamicSortFilter)
	
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
