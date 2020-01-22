from ... import QT

class ComboBox(QT.QComboBox):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(ComboBox,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def completer(self):
		"""
		Returns the completer that is used to auto complete text input for the combobox.
		"""
		res = super(ComboBox,self).completer()
		isinstance(res,QT.QCompleter)
		return res
	#----------------------------------------------------------------------
	def count(self):
		"""
		This property holds the number of items in the combobox.
		By default, for an empty combo box, this property has a value of 0.
		"""
		res = super(ComboBox,self).count()

		return res
	#----------------------------------------------------------------------
	def currentIndex(self):
		"""
		This property holds the index of the current item in the combobox..
		The current index can change when inserting or removing items.
		By default, for an empty combo box or a combo box in which no current item is set, this property has a value of -1.
		"""
		res = super(ComboBox,self).currentIndex()

		return res
	#----------------------------------------------------------------------
	def currentText(self):
		"""
		This property holds the text of the current item.
		By default, for an empty combo box or a combo box in which no current item is set, this property contains an empty string.
		"""
		res = super(ComboBox,self).currentText()
		return res
	#----------------------------------------------------------------------
	def duplicatesEnabled(self):
		"""
		This property holds whether the user can enter duplicate items into the combobox.
		Note that it is always possible to programmatically insert duplicate items into the combobox.
		By default, this property is false (duplicates are not allowed).
		"""
		res = super(ComboBox,self).duplicatesEnabled()

		return res
	#----------------------------------------------------------------------
	def hasFrame(self):
		"""
		This property holds whether the combo box draws itself with a frame.
		If enabled (the default) the combo box draws itself inside a frame, otherwise the combo box draws itself without any frame.
		"""
		res = super(ComboBox,self).hasFrame()

		return res
	#----------------------------------------------------------------------
	def hidePopup(self):
		"""
		Hides the list of items in the combobox if it is currently visible and resets the internal state, so that if the custom pop-up was shown inside the reimplemented PySide.QT.QComboBox.showPopup() , then you also need to reimplement the PySide.QT.QComboBox.hidePopup() function to hide your custom pop-up and call the base class implementation to reset the internal state whenever your custom pop-up widget is hidden.
		"""
		res = super(ComboBox,self).hidePopup()
		return res
	#----------------------------------------------------------------------
	def iconSize(self):
		"""
		This property holds the size of the icons shown in the combobox..
		Unless explicitly set this returns the default value of the current style
		This size is the maximum size that icons can have; icons of smaller size are not scaled up.
		"""
		res = super(ComboBox,self).iconSize()
		isinstance(res,QT.QSize)
		return res
	#----------------------------------------------------------------------
	def insertPolicy(self):
		"""
		This property holds the policy used to determine where user-inserted items should appear in the combobox.
		The default value is AtBottom , indicating that new items will appear at the bottom of the list of items.
		"""
		res = super(ComboBox,self).insertPolicy()
		isinstance(res,QT.QComboBox.InsertPolicy)
		return res
	#----------------------------------------------------------------------
	def isEditable(self):
		"""
		This property holds whether the combo box can be edited by the user.
		By default, this property is false.
		"""
		res = super(ComboBox,self).isEditable()

		return res
	#----------------------------------------------------------------------
	def itemDelegate(self):
		"""
		Returns the item delegate used by the popup list view.
		"""
		res = super(ComboBox,self).itemDelegate()
		isinstance(res,QT.QAbstractItemDelegate)
		return res
	#----------------------------------------------------------------------
	def lineEdit(self):
		"""
		Returns the line edit used to edit items in the combobox, or 0 if there is no line edit.
		Only editable combo boxes have a line edit.
		"""
		res = super(ComboBox,self).lineEdit()
		isinstance(res,QT.QLineEdit)
		return res
	#----------------------------------------------------------------------
	def maxCount(self):
		"""
		This property holds the maximum number of items allowed in the combobox.
		By default, this propertys value is derived from the highest signed integer available (typically 2147483647).
		"""
		res = super(ComboBox,self).maxCount()

		return res
	#----------------------------------------------------------------------
	def maxVisibleItems(self):
		"""
		This property holds the maximum allowed size on screen of the combo box, measured in items.
		By default, this property has a value of 10.
		"""
		res = super(ComboBox,self).maxVisibleItems()

		return res
	#----------------------------------------------------------------------
	def minimumContentsLength(self):
		"""
		This property holds the minimum number of characters that should fit into the combobox..
		The default value is 0.
		If this property is set to a positive value, the PySide.QT.QComboBox.minimumSizeHint() and PySide.QT.QComboBox.sizeHint() take it into account.
		"""
		res = super(ComboBox,self).minimumContentsLength()

		return res
	#----------------------------------------------------------------------
	def model(self):
		"""
		Returns the model used by the combobox.
		"""
		res = super(ComboBox,self).model()
		isinstance(res,QT.QAbstractItemModel)
		return res
	#----------------------------------------------------------------------
	def modelColumn(self):
		"""
		This property holds the column in the model that is visible..
		If set prior to populating the combo box, the pop-up view will not be affected and will show the first column (using this propertys default value).
		By default, this property has a value of 0.
		"""
		res = super(ComboBox,self).modelColumn()

		return res
	#----------------------------------------------------------------------
	def rootModelIndex(self):
		"""
		Returns the root model item index for the items in the combobox.
		"""
		res = super(ComboBox,self).rootModelIndex()
		isinstance(res,QT.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def showPopup(self):
		"""
		Displays the list of items in the combobox
		If the list is empty then the no items will be shown.
		If you reimplement this function to show a custom pop-up, make sure you call PySide.QT.QComboBox.hidePopup() to reset the internal state.
		"""
		res = super(ComboBox,self).showPopup()
		return res
	#----------------------------------------------------------------------
	def sizeAdjustPolicy(self):
		"""
		This property holds the policy describing how the size of the combobox changes when the content changes.
		The default value is AdjustToContentsOnFirstShow .
		"""
		res = super(ComboBox,self).sizeAdjustPolicy()
		isinstance(res,QT.QComboBox.SizeAdjustPolicy)
		return res
	#----------------------------------------------------------------------
	def validator(self):
		"""
		Returns the validator that is used to constrain text input for the combobox.
		"""
		res = super(ComboBox,self).validator()
		isinstance(res,QT.QValidator)
		return res
	#----------------------------------------------------------------------
	def view(self):
		"""
		Returns the list view used for the combobox popup.
		"""
		res = super(ComboBox,self).view()
		isinstance(res,QT.QAbstractItemView)
		return res
	#----------------------------------------------------------------------
	def addItem(self,*args,**kwargs):
		"""
		addItem(icon,text,userData=None)
			icon=QT.QIcon
			text=unicode
			userData=object

		addItem(text,userData=None)
			text=unicode
			userData=object

		Adds an item to the combobox with the given icon and text , and containing the specified userData (stored in the Qt.UserRole )
		The item is appended to the list of existing items.
		"""
		res = super(ComboBox,self).addItem(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def addItems(self,texts):
		"""
		addItems(texts)
			texts=list

		Adds each of the strings in the given texts to the combobox
		Each item is appended to the list of existing items in turn.
		"""
		res = super(ComboBox,self).addItems(texts)
		return res
	#----------------------------------------------------------------------
	def findData(self,data,role=None,flags=None):
		"""
		findData(data,role=None,flags=None)
			data=object
			role=QT.int
			flags=QT.Qt.MatchFlags


		"""
		res = super(ComboBox,self).findData(data,role,flags)

		return res
	#----------------------------------------------------------------------
	def findText(self,text,flags=QT.Constants.MatchFlag.Exactly):
		"""
		findText(text,flags=None)
			text=unicode
			flags=QT.Qt.MatchFlags


		"""
		res = super(ComboBox,self).findText(text,flags)

		return res
	#----------------------------------------------------------------------
	def initStyleOption(self,option):
		"""
		initStyleOption(option)
			option=QT.QStyleOptionComboBox

		Initialize option with the values from this PySide.QT.QComboBox
		This method is useful for subclasses when they need a PySide.QT.QStyleOptionComboBox , but dont want to fill in all the information themselves.
		"""
		res = super(ComboBox,self).initStyleOption(option)
		return res
	#----------------------------------------------------------------------
	def insertItem(self,*args,**kwargs):
		"""
		insertItem(index,text,userData=None)
			index=QT.int
			text=unicode
			userData=object

		insertItem(index,icon,text,userData=None)
			index=QT.int
			icon=QT.QIcon
			text=unicode
			userData=object

		Inserts the text and userData (stored in the Qt.UserRole ) into the combobox at the given index .
		If the index is equal to or higher than the total number of items, the new item is appended to the list of existing items
		If the index is zero or negative, the new item is prepended to the list of existing items.
		"""
		res = super(ComboBox,self).insertItem(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def insertItems(self,index,texts):
		"""
		insertItems(index,texts)
			index=QT.int
			texts=list

		Inserts the strings from the list into the combobox as separate items, starting at the index specified.
		If the index is equal to or higher than the total number of items, the new items are appended to the list of existing items
		If the index is zero or negative, the new items are prepended to the list of existing items.
		"""
		res = super(ComboBox,self).insertItems(index,texts)
		return res
	#----------------------------------------------------------------------
	def insertSeparator(self,index):
		"""
		insertSeparator(index)
			index=QT.int

		Inserts a separator item into the combobox at the given index .
		If the index is equal to or higher than the total number of items, the new item is appended to the list of existing items
		If the index is zero or negative, the new item is prepended to the list of existing items.
		"""
		res = super(ComboBox,self).insertSeparator(index)
		return res
	#----------------------------------------------------------------------
	def itemData(self,index,role=None):
		"""
		itemData(index,role=None)
			index=QT.int
			role=QT.int

		Returns the data for the given role in the given index in the combobox, or QVariant.Invalid if there is no data for this role.
		"""
		res = super(ComboBox,self).itemData(index,role)
		return res
	#----------------------------------------------------------------------
	def itemIcon(self,index):
		"""
		itemIcon(index)
			index=QT.int

		Returns the icon for the given index in the combobox.
		"""
		res = super(ComboBox,self).itemIcon(index)
		isinstance(res,QT.QIcon)
		return res
	#----------------------------------------------------------------------
	def itemText(self,index):
		"""
		itemText(index)
			index=QT.int

		Returns the text for the given index in the combobox.
		"""
		res = super(ComboBox,self).itemText(index)
		return res
	#----------------------------------------------------------------------
	def removeItem(self,index):
		"""
		removeItem(index)
			index=QT.int

		Removes the item at the given index from the combobox
		This will update the current index if the index is removed.
		This function does nothing if index is out of range.
		"""
		res = super(ComboBox,self).removeItem(index)
		return res
	#----------------------------------------------------------------------
	def setCompleter(self,c):
		"""
		setCompleter(c)
			c=QT.QCompleter

		Sets the completer to use instead of the current completer
		If completer is 0, auto completion is disabled.
		By default, for an editable combo box, a PySide.QT.QCompleter that performs case insensitive inline completion is automatically created.
		"""
		res = super(ComboBox,self).setCompleter(c)
		return res
	#----------------------------------------------------------------------
	def setDuplicatesEnabled(self,enable):
		"""
		setDuplicatesEnabled(enable)
			enable=QT.bool

		This property holds whether the user can enter duplicate items into the combobox.
		Note that it is always possible to programmatically insert duplicate items into the combobox.
		By default, this property is false (duplicates are not allowed).
		"""
		res = super(ComboBox,self).setDuplicatesEnabled(enable)
		return res
	#----------------------------------------------------------------------
	def setEditable(self,editable):
		"""
		setEditable(editable)
			editable=QT.bool

		This property holds whether the combo box can be edited by the user.
		By default, this property is false.
		"""
		res = super(ComboBox,self).setEditable(editable)
		return res
	#----------------------------------------------------------------------
	def setFrame(self,arg__1):
		"""
		setFrame(arg__1)
			arg__1=QT.bool

		This property holds whether the combo box draws itself with a frame.
		If enabled (the default) the combo box draws itself inside a frame, otherwise the combo box draws itself without any frame.
		"""
		res = super(ComboBox,self).setFrame(arg__1)
		return res
	#----------------------------------------------------------------------
	def setIconSize(self,size):
		"""
		setIconSize(size)
			size=QT.QSize

		This property holds the size of the icons shown in the combobox..
		Unless explicitly set this returns the default value of the current style
		This size is the maximum size that icons can have; icons of smaller size are not scaled up.
		"""
		res = super(ComboBox,self).setIconSize(size)
		return res
	#----------------------------------------------------------------------
	def setInsertPolicy(self,policy):
		"""
		setInsertPolicy(policy)
			policy=QT.QComboBox.InsertPolicy

		This property holds the policy used to determine where user-inserted items should appear in the combobox.
		The default value is AtBottom , indicating that new items will appear at the bottom of the list of items.
		"""
		res = super(ComboBox,self).setInsertPolicy(policy)
		return res
	#----------------------------------------------------------------------
	def setItemData(self,index,value,role=None):
		"""
		setItemData(index,value,role=None)
			index=QT.int
			value=object
			role=QT.int

		Sets the data role for the item on the given index in the combobox to the specified value .
		"""
		res = super(ComboBox,self).setItemData(index,value,role)
		return res
	#----------------------------------------------------------------------
	def setItemDelegate(self,delegate):
		"""
		setItemDelegate(delegate)
			delegate=QT.QAbstractItemDelegate

		Sets the item delegate for the popup list view
		The combobox takes ownership of the delegate.
		"""
		res = super(ComboBox,self).setItemDelegate(delegate)
		return res
	#----------------------------------------------------------------------
	def setItemIcon(self,index,icon):
		"""
		setItemIcon(index,icon)
			index=QT.int
			icon=QT.QIcon

		Sets the icon for the item on the given index in the combobox.
		"""
		res = super(ComboBox,self).setItemIcon(index,icon)
		return res
	#----------------------------------------------------------------------
	def setItemText(self,index,text):
		"""
		setItemText(index,text)
			index=QT.int
			text=unicode

		Sets the text for the item on the given index in the combobox.
		"""
		res = super(ComboBox,self).setItemText(index,text)
		return res
	#----------------------------------------------------------------------
	def setLineEdit(self,edit):
		"""
		setLineEdit(edit)
			edit=QT.QLineEdit

		Sets the line edit to use instead of the current line edit widget.
		The combo box takes ownership of the line edit.
		"""
		res = super(ComboBox,self).setLineEdit(edit)
		return res
	#----------------------------------------------------------------------
	def setMaxCount(self,max):
		"""
		setMaxCount(max)
			max=QT.int

		This property holds the maximum number of items allowed in the combobox.
		By default, this propertys value is derived from the highest signed integer available (typically 2147483647).
		"""
		res = super(ComboBox,self).setMaxCount(max)
		return res
	#----------------------------------------------------------------------
	def setMaxVisibleItems(self,maxItems):
		"""
		setMaxVisibleItems(maxItems)
			maxItems=QT.int

		This property holds the maximum allowed size on screen of the combo box, measured in items.
		By default, this property has a value of 10.
		"""
		res = super(ComboBox,self).setMaxVisibleItems(maxItems)
		return res
	#----------------------------------------------------------------------
	def setMinimumContentsLength(self,characters):
		"""
		setMinimumContentsLength(characters)
			characters=QT.int

		This property holds the minimum number of characters that should fit into the combobox..
		The default value is 0.
		If this property is set to a positive value, the PySide.QT.QComboBox.minimumSizeHint() and PySide.QT.QComboBox.sizeHint() take it into account.
		"""
		res = super(ComboBox,self).setMinimumContentsLength(characters)
		return res
	#----------------------------------------------------------------------
	def setModel(self,model):
		"""
		setModel(model)
			model=QT.QAbstractItemModel

		Sets the model to be model
		model must not be 0
		If you want to clear the contents of a model, call PySide.QT.QComboBox.clear() .
		"""
		res = super(ComboBox,self).setModel(model)
		return res
	#----------------------------------------------------------------------
	def setModelColumn(self,visibleColumn):
		"""
		setModelColumn(visibleColumn)
			visibleColumn=QT.int

		This property holds the column in the model that is visible..
		If set prior to populating the combo box, the pop-up view will not be affected and will show the first column (using this propertys default value).
		By default, this property has a value of 0.
		"""
		res = super(ComboBox,self).setModelColumn(visibleColumn)
		return res
	#----------------------------------------------------------------------
	def setRootModelIndex(self,index):
		"""
		setRootModelIndex(index)
			index=QT.QModelIndex

		Sets the root model item index for the items in the combobox.
		"""
		res = super(ComboBox,self).setRootModelIndex(index)
		return res
	#----------------------------------------------------------------------
	def setSizeAdjustPolicy(self,policy):
		"""
		setSizeAdjustPolicy(policy)
			policy=QT.QComboBox.SizeAdjustPolicy

		This property holds the policy describing how the size of the combobox changes when the content changes.
		The default value is AdjustToContentsOnFirstShow .
		"""
		res = super(ComboBox,self).setSizeAdjustPolicy(policy)
		return res
	#----------------------------------------------------------------------
	def setValidator(self,v):
		"""
		setValidator(v)
			v=QT.QValidator

		Sets the validator to use instead of the current validator.
		"""
		res = super(ComboBox,self).setValidator(v)
		return res
	#----------------------------------------------------------------------
	def setView(self,itemView):
		"""
		setView(itemView)
			itemView=QT.QAbstractItemView

		Sets the view to be used in the combobox popup to the given itemView
		The combobox takes ownership of the view.
		Note: If you want to use the convenience views (like PySide.QT.QListWidget , PySide.QT.QTableWidget or PySide.QT.QTreeWidget ), make sure to call PySide.QT.QComboBox.setModel() on the combobox with the convenience widgets model before calling this function.
		"""
		res = super(ComboBox,self).setView(itemView)
		return res

	Completer             = property(completer,setCompleter)
	Count                 = property(count)
	CurrentIndex          = property(currentIndex)
	CurrentText           = property(currentText)
	DuplicatesEnabled     = property(duplicatesEnabled,setDuplicatesEnabled)
	HasFrame              = property(hasFrame)
	HidePopup             = property(hidePopup)
	IconSize              = property(iconSize,setIconSize)
	InsertPolicy          = property(insertPolicy,setInsertPolicy)
	IsEditable            = property(isEditable)
	ItemDelegate          = property(itemDelegate,setItemDelegate)
	LineEdit              = property(lineEdit,setLineEdit)
	MaxCount              = property(maxCount,setMaxCount)
	MaxVisibleItems       = property(maxVisibleItems,setMaxVisibleItems)
	MinimumContentsLength = property(minimumContentsLength)
	Model                 = property(model,setModel)
	ModelColumn           = property(modelColumn,setModelColumn)
	RootModelIndex        = property(rootModelIndex)
	ShowPopup             = property(showPopup)
	SizeAdjustPolicy      = property(sizeAdjustPolicy,setSizeAdjustPolicy)
	Validator             = property(validator,setValidator)
	View                  = property(view,setView)