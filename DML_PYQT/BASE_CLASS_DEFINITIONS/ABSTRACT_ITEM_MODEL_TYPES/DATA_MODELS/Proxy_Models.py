
from .... import QT

class Sort_Filter_Proxy_Model(QT.QSortFilterProxyModel):
	''''''
	def __init__(self,parent=None):
		''''''
		super(Sort_Filter_Proxy_Model,self).__init__(parent=parent)

	#----------------------------------------------------------------------
	def parentWidget(self):
		return QT.QObject.parent(self)

	def source_Index_From_Item(self,item):
		try:
			index = item.index()
		except:
			index = item.index
		res = self.mapFromSource(index)
		return res
	#----------------------------------------------------------------------
	def item_From_Index(self,index):
		""""""
		if not index.model() == self:
			index = self.mapToSource(index)
		item = self.SourceModel.getItem(index)
		return item
	#----------------------------------------------------------------------
	def invalidateFilter(self):
		"""
		Invalidates the current filtering.
		This function should be called if you are implementing custom filtering (e.g
		PYQT.QSortFilterProxyModel.filterAcceptsRow() ), and your filter parameters have changed.
		"""
		res = super(Sort_Filter_Proxy_Model,self).invalidateFilter()
		return res
	#----------------------------------------------------------------------
	def sortColumn(self):
		"""
		the column currently used for sorting
		This returns the most recently used sort column.
		"""
		res = super(Sort_Filter_Proxy_Model,self).sortColumn()

		return res
	#----------------------------------------------------------------------
	def sortOrder(self):
		"""
		the order currently used for sorting
		This returns the most recently used sort order.
		"""
		res = super(Sort_Filter_Proxy_Model,self).sortOrder()
		isinstance(res,QT.Qt.SortOrder)
		return res
	#----------------------------------------------------------------------
	def filterAcceptsColumn(self,source_column,source_parent):
		"""
		filterAcceptsColumn(source_column,source_parent)
			source_column=PYQT.int
			source_parent=PYQT.QModelIndex

		Returns true if the item in the column indicated by the given source_column and source_parent should be included in the model; otherwise returns false.
		The default implementation returns true if the value held by the relevant item matches the filter string, wildcard string or regular expression.
		"""
		res = super(Sort_Filter_Proxy_Model,self).filterAcceptsColumn(source_column,source_parent)

		return res
	#----------------------------------------------------------------------
	def filterAcceptsRow(self,source_row,source_parent):
		"""
		filterAcceptsRow(source_row,source_parent)
			source_row=PYQT.int
			source_parent=PYQT.QModelIndex

		Returns true if the item in the row indicated by the given source_row and source_parent should be included in the model; otherwise returns false.
		The default implementation returns true if the value held by the relevant item matches the filter string, wildcard string or regular expression.
		"""
		res = super(Sort_Filter_Proxy_Model,self).filterAcceptsRow(source_row,source_parent)

		return res
	#----------------------------------------------------------------------
	def lessThan(self,left,right):
		"""
		lessThan(left,right)
			left=PYQT.QModelIndex
			right=PYQT.QModelIndex

		Returns true if the value of the item referred to by the given index left is less than the value of the item referred to by the given index right , otherwise returns false.
		This function is used as the < operator when sorting, and handles the following PYQT.QVariant types:
		Any other type will be converted to a PYQT.QString using QVariant.toString() .
		Comparison of PYQT.QString s is case sensitive by default; this can be changed using the PYQT.QSortFilterProxyModel.sortCaseSensitivity() property.
		By default, the PYQT.Qt.DisplayRole associated with the PYQT.QModelIndex es is used for comparisons
		This can be changed by setting the PYQT.QSortFilterProxyModel.sortRole() property.
		"""
		res = super(Sort_Filter_Proxy_Model,self).lessThan(left,right)

		return res
	#----------------------------------------------------------------------
	def filterCaseSensitivity(self):
		"""
		This property holds the case sensitivity of the PYQT.QRegExp pattern used to filter the contents of the source model.
		By default, the filter is case sensitive.
		"""
		res = super(Sort_Filter_Proxy_Model,self).filterCaseSensitivity()
		isinstance(res,QT.Qt.CaseSensitivity)
		return res
	#----------------------------------------------------------------------
	def setFilterCaseSensitivity(self,cs):
		"""
		setFilterCaseSensitivity(cs)
			cs=PYQT.Qt.CaseSensitivity

		This property holds the case sensitivity of the PYQT.QRegExp pattern used to filter the contents of the source model.
		By default, the filter is case sensitive.
		"""
		res = super(Sort_Filter_Proxy_Model,self).setFilterCaseSensitivity(cs)
		return res
	#----------------------------------------------------------------------
	def filterKeyColumn(self):
		"""
		This property holds the column where the key used to filter the contents of the source model is read from..
		The default value is 0
		If the value is -1, the keys will be read from all columns.
		"""
		res = super(Sort_Filter_Proxy_Model,self).filterKeyColumn()

		return res
	#----------------------------------------------------------------------
	def setFilterKeyColumn(self,column):
		"""
		setFilterKeyColumn(column)
			column=PYQT.int

		This property holds the column where the key used to filter the contents of the source model is read from..
		The default value is 0
		If the value is -1, the keys will be read from all columns.
		"""
		res = super(Sort_Filter_Proxy_Model,self).setFilterKeyColumn(column)
		return res
	#----------------------------------------------------------------------
	def filterRegExp(self):
		"""
		This property holds the PYQT.QRegExp used to filter the contents of the source model.
		Setting this property overwrites the current PYQT.QSortFilterProxyModel.filterCaseSensitivity()
		By default, the PYQT.QRegExp is an empty string matching all contents.
		If no PYQT.QRegExp or an empty string is set, everything in the source model will be accepted.
		"""
		res = super(Sort_Filter_Proxy_Model,self).filterRegExp()
		isinstance(res,QT.QRegExp)
		return res	
	#----------------------------------------------------------------------
	def setFilterRegExp(self,*args,**kwargs):
		"""
		setFilterRegExp(regExp)
			regExp=PYQT.QRegExp

		setFilterRegExp(pattern)
			pattern=unicode

		This property holds the PYQT.QRegExp used to filter the contents of the source model.
		Setting this property overwrites the current PYQT.QSortFilterProxyModel.filterCaseSensitivity()
		By default, the PYQT.QRegExp is an empty string matching all contents.
		If no PYQT.QRegExp or an empty string is set, everything in the source model will be accepted.
		"""
		res = super(Sort_Filter_Proxy_Model,self).setFilterRegExp(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def filterRole(self):
		"""
		This property holds the item role that is used to query the source models data when filtering items.
		The default value is PYQT.Qt.DisplayRole .
		"""
		res = super(Sort_Filter_Proxy_Model,self).filterRole()

		return res
	#----------------------------------------------------------------------
	def setFilterRole(self,role):
		"""
		setFilterRole(role)
			role=PYQT.int

		This property holds the item role that is used to query the source models data when filtering items.
		The default value is PYQT.Qt.DisplayRole .
		"""
		res = super(Sort_Filter_Proxy_Model,self).setFilterRole(role)
		return res
	#----------------------------------------------------------------------
	def sortCaseSensitivity(self):
		"""
		This property holds the case sensitivity setting used for comparing strings when sorting.
		By default, sorting is case sensitive.
		"""
		res = super(Sort_Filter_Proxy_Model,self).sortCaseSensitivity()
		isinstance(res,QT.Qt.CaseSensitivity)
		return res
	#----------------------------------------------------------------------
	def setSortCaseSensitivity(self,cs):
		"""
		setSortCaseSensitivity(cs)
			cs=PYQT.Qt.CaseSensitivity

		This property holds the case sensitivity setting used for comparing strings when sorting.
		By default, sorting is case sensitive.
		"""
		res = super(Sort_Filter_Proxy_Model,self).setSortCaseSensitivity(cs)
		return res
	#----------------------------------------------------------------------
	def isSortLocaleAware(self):
		"""
		This property holds the local aware setting used for comparing strings when sorting.
		By default, sorting is not local aware.
		"""
		res = super(Sort_Filter_Proxy_Model,self).isSortLocaleAware()

		return res
	#----------------------------------------------------------------------
	def setSortLocaleAware(self,on):
		"""
		setSortLocaleAware(on)
			on=PYQT.bool

		This property holds the local aware setting used for comparing strings when sorting.
		By default, sorting is not local aware.
		"""
		res = super(Sort_Filter_Proxy_Model,self).setSortLocaleAware(on)
		return res
	#----------------------------------------------------------------------
	def sortRole(self):
		"""
		This property holds the item role that is used to query the source models data when sorting items.
		The default value is PYQT.Qt.DisplayRole .
		"""
		res = super(Sort_Filter_Proxy_Model,self).sortRole()

		return res
	#----------------------------------------------------------------------
	def setSortRole(self,role):
		"""
		setSortRole(role)
			role=PYQT.int

		This property holds the item role that is used to query the source models data when sorting items.
		The default value is PYQT.Qt.DisplayRole .
		"""
		res = super(Sort_Filter_Proxy_Model,self).setSortRole(role)
		return res
	#----------------------------------------------------------------------
	def dynamicSortFilter(self):
		"""
		This property holds whether the proxy model is dynamically sorted and filtered whenever the contents of the source model change.
		Note that you should not update the source model through the proxy model when PYQT.QSortFilterProxyModel.dynamicSortFilter() is true
		For instance, if you set the proxy model on a PYQT.QComboBox , then using functions that update the model, e.g., PYQT.QComboBox.addItem() , will not work as expected
		An alternative is to set PYQT.QSortFilterProxyModel.dynamicSortFilter() to false and call PYQT.QSortFilterProxyModel.sort() after adding items to the PYQT.QComboBox .
		The default value is false.
		"""
		res = super(Sort_Filter_Proxy_Model,self).dynamicSortFilter()

		return res
	#----------------------------------------------------------------------
	def setDynamicSortFilter(self,enable):
		"""
		setDynamicSortFilter(enable)
			enable=PYQT.bool

		This property holds whether the proxy model is dynamically sorted and filtered whenever the contents of the source model change.
		Note that you should not update the source model through the proxy model when PYQT.QSortFilterProxyModel.dynamicSortFilter() is true
		For instance, if you set the proxy model on a PYQT.QComboBox , then using functions that update the model, e.g., PYQT.QComboBox.addItem() , will not work as expected
		An alternative is to set PYQT.QSortFilterProxyModel.dynamicSortFilter() to false and call PYQT.QSortFilterProxyModel.sort() after adding items to the PYQT.QComboBox .
		The default value is false.
		"""
		res = super(Sort_Filter_Proxy_Model,self).setDynamicSortFilter(enable)
		return res

	#----------------------------------------------------------------------
	def sourceModel(self):
		"""
		Returns the model that contains the data that is available through the proxy model.
		"""
		res = super(Sort_Filter_Proxy_Model,self).sourceModel()

		return res
	#----------------------------------------------------------------------
	def mapFromSource(self,sourceIndex):
		"""
		mapFromSource(sourceIndex)
			sourceIndex=PYQT.QModelIndex

		Reimplement this function to return the model index in the proxy model that corresponds to the sourceIndex from the source model.
		"""
		res = super(Sort_Filter_Proxy_Model,self).mapFromSource(sourceIndex)
		isinstance(res,QT.QModelIndex)
		if res.isValid():
			if self.sourceModel() != sourceIndex.model():
				raise IndexError("invalied index")
		return res
	#----------------------------------------------------------------------
	def mapSelectionFromSource(self,selection):
		"""
		mapSelectionFromSource(selection)
			selection=PYQT.QItemSelection

		Returns a proxy selection mapped from the specified sourceSelection .
		Reimplement this method to map source selections to proxy selections.
		"""
		res = super(Sort_Filter_Proxy_Model,self).mapSelectionFromSource(selection)
		isinstance(res,QT.QItemSelection)
		return res
	#----------------------------------------------------------------------
	def mapSelectionToSource(self,selection):
		"""
		mapSelectionToSource(selection)
			selection=PYQT.QItemSelection

		Returns a source selection mapped from the specified proxySelection .
		Reimplement this method to map proxy selections to source selections.
		"""
		res = super(Sort_Filter_Proxy_Model,self).mapSelectionToSource(selection)
		isinstance(res,QT.QItemSelection)
		return res
	#----------------------------------------------------------------------
	def mapToSource(self,proxyIndex):
		"""
		mapToSource(proxyIndex)
			proxyIndex=PYQT.QModelIndex

		Reimplement this function to return the model index in the source model that corresponds to the proxyIndex in the proxy model.
		"""
		res = super(Sort_Filter_Proxy_Model,self).mapToSource(proxyIndex)
		isinstance(res,QT.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def setSourceModel(self,sourceModel):
		"""
		setSourceModel(sourceModel)
			sourceModel=PYQT.QAbstractItemModel

		Sets the given sourceModel to be processed by the proxy model.
		"""
		res = super(Sort_Filter_Proxy_Model,self).setSourceModel(sourceModel)
		return res
	#----------------------------------------------------------------------
	def mimeTypes(self):
		"""
		Returns a list of MIME types that can be used to describe a list of model indexes.
		"""
		res = super(Sort_Filter_Proxy_Model,self).mimeTypes()
		return res
	#----------------------------------------------------------------------
	def roleNames(self):
		"""
		Returns the models role names.
		"""
		res = super(Sort_Filter_Proxy_Model,self).roleNames()
		return res
	#----------------------------------------------------------------------
	def columnCount(self,parent=None):
		"""
		columnCount(parent=None)
			parent=PYQT.QModelIndex

		Returns the number of columns for the children of the given parent .
		In most subclasses, the number of columns is independent of the parent .
		For example:
		"""
		res = super(Sort_Filter_Proxy_Model,self).columnCount(parent)

		return res
	#----------------------------------------------------------------------
	def createIndex(self,*args,**kwargs):
		"""
		createIndex(row,column,id=None)
			row=PYQT.int
			column=PYQT.int
			id=PYQT.int

		createIndex(row,column,ptr)
			row=PYQT.int
			column=PYQT.int
			ptr=Object

		Use PYQT.QModelIndex QAbstractItemModel::createIndex(int row, int column, quint32 id) instead.
		"""
		res = super(Sort_Filter_Proxy_Model,self).createIndex(*args,**kwargs)
		isinstance(res,QT.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def data(self,index,role=None):
		"""
		data(index,role=None)
			index=PYQT.QModelIndex
			role=PYQT.int

		Returns the data stored under the given role for the item referred to by the index .
		"""
		res = super(Sort_Filter_Proxy_Model,self).data(index,role)
		return res
	#----------------------------------------------------------------------
	def decodeData(self,row,column,parent,stream):
		"""
		decodeData(row,column,parent,stream)
			row=PYQT.int
			column=PYQT.int
			parent=PYQT.QModelIndex
			stream=PYQT.QDataStream


		"""
		res = super(Sort_Filter_Proxy_Model,self).decodeData(row,column,parent,stream)

		return res
	#----------------------------------------------------------------------
	def dropMimeData(self,data,action,row,column,parent):
		"""
		dropMimeData(data,action,row,column,parent)
			data=PYQT.QMimeData
			action=PYQT.Qt.DropAction
			row=PYQT.int
			column=PYQT.int
			parent=PYQT.QModelIndex


		"""
		res = super(Sort_Filter_Proxy_Model,self).dropMimeData(data,action,row,column,parent)

		return res
	#----------------------------------------------------------------------
	def encodeData(self,indexes,stream):
		"""
		encodeData(indexes,stream)
			indexes=unKnown
			stream=PYQT.QDataStream


		"""
		res = super(Sort_Filter_Proxy_Model,self).encodeData(indexes,stream)
		return res
	#----------------------------------------------------------------------
	def fetchMore(self,parent):
		"""
		fetchMore(parent)
			parent=PYQT.QModelIndex

		Fetches any available data for the items with the parent specified by the parent index.
		Reimplement this if you are populating your model incrementally.
		The default implementation does nothing.
		"""
		res = super(Sort_Filter_Proxy_Model,self).fetchMore(parent)
		return res
	#----------------------------------------------------------------------
	def flags(self,index):
		"""
		flags(index)
			index=PYQT.QModelIndex

		Returns the item flags for the given index .
		The base class implementation returns a combination of flags that enables the item (ItemIsEnabled ) and allows it to be selected (ItemIsSelectable ).
		"""
		res = super(Sort_Filter_Proxy_Model,self).flags(index)
		isinstance(res,QT.Qt.ItemFlags)
		return res
	#----------------------------------------------------------------------
	def hasChildren(self,parent=None):
		"""
		hasChildren(parent=None)
			parent=PYQT.QModelIndex

		Returns true if parent has any children; otherwise returns false.
		Use PYQT.QAbstractItemModel.rowCount() on the parent to find out the number of children.
		"""
		res = super(Sort_Filter_Proxy_Model,self).hasChildren(parent)

		return res
	#----------------------------------------------------------------------
	def hasIndex(self,row,column,parent=None):
		"""
		hasIndex(row,column,parent=None)
			row=PYQT.int
			column=PYQT.int
			parent=PYQT.QModelIndex

		Returns true if the model returns a valid PYQT.QModelIndex for row and column with parent , otherwise returns false.
		"""
		res = super(Sort_Filter_Proxy_Model,self).hasIndex(row,column,parent)

		return res
	#----------------------------------------------------------------------
	def headerData(self,section,orientation,role=None):
		"""
		headerData(section,orientation,role=None)
			section=PYQT.int
			orientation=PYQT.Qt.Orientation
			role=PYQT.int


		"""
		res = super(Sort_Filter_Proxy_Model,self).headerData(section,orientation,role)
		return res
	#----------------------------------------------------------------------
	def index(self,row,column,parent=None):
		"""
		index(row,column,parent=None)
			row=PYQT.int
			column=PYQT.int
			parent=PYQT.QModelIndex

		Returns the index of the item in the model specified by the given row , column and parent index.
		When reimplementing this function in a subclass, call PYQT.QAbstractItemModel.createIndex() to generate model indexes that other components can use to refer to items in your model.
		"""
		res = super(Sort_Filter_Proxy_Model,self).index(row,column,parent)
		isinstance(res,QT.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def itemData(self,index):
		"""
		itemData(index)
			index=PYQT.QModelIndex

		Returns a map with values for all predefined roles in the model for the item at the given index .
		Reimplement this function if you want to extend the default behavior of this function to include custom roles in the map.
		"""
		res = super(Sort_Filter_Proxy_Model,self).itemData(index)
		return res
	#----------------------------------------------------------------------
	def match(self,start,role,value,hits=None,flags=None):
		"""
		match(start,role,value,hits=None,flags=None)
			start=PYQT.QModelIndex
			role=PYQT.int
			value=object
			hits=PYQT.int
			flags=PYQT.Qt.MatchFlags


		"""
		res = super(Sort_Filter_Proxy_Model,self).match(start,role,value,hits,flags)
		return res
	#----------------------------------------------------------------------
	def mimeData(self,indexes):
		"""
		mimeData(indexes)
			indexes=unKnown


		"""
		res = super(Sort_Filter_Proxy_Model,self).mimeData(indexes)
		isinstance(res,QT.QMimeData)
		return res
	#----------------------------------------------------------------------
	def parent(self,child):
		"""
		parent(child)
			child=PYQT.QModelIndex

		Returns the parent of the model item with the given index
		If the item has no parent, an invalid PYQT.QModelIndex is returned.
		A common convention used in models that expose tree data structures is that only items in the first column have children
		For that case, when reimplementing this function in a subclass the column of the returned PYQT.QModelIndex would be 0.
		When reimplementing this function in a subclass, be careful to avoid calling PYQT.QModelIndex member functions, such as QModelIndex.parent() , since indexes belonging to your model will simply call your implementation, leading to infinite recursion.
		"""
		res = super(Sort_Filter_Proxy_Model,self).parent(child)
		isinstance(res,QT.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def removeColumn(self,column,parent=None):
		"""
		removeColumn(column,parent=None)
			column=PYQT.int
			parent=PYQT.QModelIndex

		Removes the given column from the child items of the parent specified.
		Returns true if the column is removed; otherwise returns false.
		"""
		res = super(Sort_Filter_Proxy_Model,self).removeColumn(column,parent)

		return res
	#----------------------------------------------------------------------
	def removeColumns(self,column,count,parent=None):
		"""
		removeColumns(column,count,parent=None)
			column=PYQT.int
			count=PYQT.int
			parent=PYQT.QModelIndex

		On models that support this, removes count columns starting with the given column under parent parent from the model.
		Returns true if the columns were successfully removed; otherwise returns false.
		The base class implementation does nothing and returns false.
		If you implement your own model, you can reimplement this function if you want to support removing
		Alternatively, you can provide your own API for altering the data.
		"""
		res = super(Sort_Filter_Proxy_Model,self).removeColumns(column,count,parent)

		return res
	#----------------------------------------------------------------------
	def removeRow(self,row,parent=None):
		"""
		removeRow(row,parent=None)
			row=PYQT.int
			parent=PYQT.QModelIndex

		Removes the given row from the child items of the parent specified.
		Returns true if the row is removed; otherwise returns false.
		This is a convenience function that calls PYQT.QAbstractItemModel.removeRows()
		The PYQT.QAbstractItemModel implementation of PYQT.QAbstractItemModel.removeRows() does nothing.
		"""
		res = super(Sort_Filter_Proxy_Model,self).removeRow(row,parent)

		return res
	#----------------------------------------------------------------------
	def removeRows(self,row,count,parent=None):
		"""
		removeRows(row,count,parent=None)
			row=PYQT.int
			count=PYQT.int
			parent=PYQT.QModelIndex

		On models that support this, removes count rows starting with the given row under parent parent from the model.
		Returns true if the rows were successfully removed; otherwise returns false.
		The base class implementation does nothing and returns false.
		If you implement your own model, you can reimplement this function if you want to support removing
		Alternatively, you can provide your own API for altering the data.
		"""
		res = super(Sort_Filter_Proxy_Model,self).removeRows(row,count,parent)

		return res
	#----------------------------------------------------------------------
	def rowCount(self,parent=None):
		"""
		rowCount(parent=None)
			parent=PYQT.QModelIndex

		Returns the number of rows under the given parent
		When the parent is valid it means that rowCount is returning the number of children of parent.
		"""
		res = super(Sort_Filter_Proxy_Model,self).rowCount(parent)

		return res
	#----------------------------------------------------------------------
	def setData(self,index,value,role=None):
		"""
		setData(index,value,role=None)
			index=PYQT.QModelIndex
			value=object
			role=PYQT.int

		Sets the role data for the item at index to value .
		Returns true if successful; otherwise returns false.
		The PYQT.QAbstractItemModel.dataChanged() signal should be emitted if the data was successfully set.
		The base class implementation returns false
		This function and PYQT.QAbstractItemModel.data() must be reimplemented for editable models.
		"""
		res = super(Sort_Filter_Proxy_Model,self).setData(index,value,role)

		return res
	#----------------------------------------------------------------------
	def setHeaderData(self,section,orientation,value,role=None):
		"""
		setHeaderData(section,orientation,value,role=None)
			section=PYQT.int
			orientation=PYQT.Qt.Orientation
			value=object
			role=PYQT.int


		"""
		res = super(Sort_Filter_Proxy_Model,self).setHeaderData(section,orientation,value,role)

		return res
	#----------------------------------------------------------------------
	def setItemData(self,index,roles):
		"""
		setItemData(index,roles)
			index=PYQT.QModelIndex
			roles=unKnown


		"""
		res = super(Sort_Filter_Proxy_Model,self).setItemData(index,roles)

		return res
	#----------------------------------------------------------------------
	def setRoleNames(self,roleNames):
		"""
		setRoleNames(roleNames)
			roleNames=unKnown


		"""
		res = super(Sort_Filter_Proxy_Model,self).setRoleNames(roleNames)
		return res
	#----------------------------------------------------------------------
	def setSupportedDragActions(self,arg__1):
		"""
		setSupportedDragActions(arg__1)
			arg__1=PYQT.Qt.DropActions


		"""
		res = super(Sort_Filter_Proxy_Model,self).setSupportedDragActions(arg__1)
		return res
	#----------------------------------------------------------------------
	def sibling(self,row,column,idx):
		"""
		sibling(row,column,idx)
			row=PYQT.int
			column=PYQT.int
			idx=PYQT.QModelIndex

		Returns the sibling at row and column for the item at index , or an invalid PYQT.QModelIndex if there is no sibling at that location.
		PYQT.QAbstractItemModel.sibling() is just a convenience function that finds the items parent, and uses it to retrieve the index of the child item in the specified row and column .
		"""
		res = super(Sort_Filter_Proxy_Model,self).sibling(row,column,idx)
		isinstance(res,QT.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def sort(self,column=0,order=QT.Qt.AscendingOrder):
		"""
		sort(column,order=None)
			column=PYQT.int
			order=PYQT.Qt.SortOrder


		"""
		res = super(Sort_Filter_Proxy_Model,self).sort(column,order)
		return res
	#----------------------------------------------------------------------
	def span(self,index):
		"""
		span(index)
			index=PYQT.QModelIndex

		Returns the row and column span of the item represented by index .
		"""
		res = super(Sort_Filter_Proxy_Model,self).span(index)
		isinstance(res,QT.QSize)
		return res

	SourceModel           = property(sourceModel,setSourceModel)
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

	MimeTypes              = property(mimeTypes)
	RoleNames              = property(roleNames)