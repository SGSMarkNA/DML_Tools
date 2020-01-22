from .... import QT

class Standard_QTreeWidgetItem(QT.QTreeWidgetItem):
	''''''
	Item_Data_Roles = QT.Constants.ItemDataRole
	ITEM_TYPE       = QT.userType_generator()
	def __init__(self,*args,**kwargs):
		''''''
		super(Standard_QTreeWidgetItem,self).__init__(*args,**kwargs)
		if False:
			self.ITEM_TYPE = int
	#----------------------------------------------------------------------
	def childCount(self):
		"""
		Returns the number of child items.
		"""
		res = super(Standard_QTreeWidgetItem,self).childCount()
		
		return res
	#----------------------------------------------------------------------
	def iter_children(self):
		"""
		iterate child items.
		"""
		for index in range(self.ChildCount):
			yield self.child(index)
	#----------------------------------------------------------------------
	def childIndicatorPolicy(self):
		"""
		Returns the item indicator policy
		This policy decides when the tree branch expand/collapse indicator is shown.
		"""
		res = super(Standard_QTreeWidgetItem,self).childIndicatorPolicy()
		isinstance(res,QT.QTreeWidgetItem.ChildIndicatorPolicy)
		return res
	#----------------------------------------------------------------------
	def columnCount(self):
		"""
		Returns the number of columns in the item.
		"""
		res = super(Standard_QTreeWidgetItem,self).columnCount()
		
		return res
	#----------------------------------------------------------------------
	def emitDataChanged(self):
		"""
		Causes the model associated with this item to emit a PySide.QT.QAbstractItemModel.dataChanged() () signal for this item.
		You normally only need to call this function if you have subclassed PySide.QT.QTreeWidgetItem and reimplemented PySide.QT.QTreeWidgetItem.data() and/or PySide.QT.QTreeWidgetItem.setData() .
		"""
		res = super(Standard_QTreeWidgetItem,self).emitDataChanged()
		return res
	#----------------------------------------------------------------------
	def executePendingSort(self):
		"""

		"""
		res = super(Standard_QTreeWidgetItem,self).executePendingSort()
		return res
	#----------------------------------------------------------------------
	def flags(self):
		"""
		Returns the flags used to describe the item
		These determine whether the item can be checked, edited, and selected.
		The default value for flags is QT.ItemIsSelectable | QT.ItemIsUserCheckable | QT.ItemIsEnabled | QT.ItemIsDragEnabled
		If the item was constructed with a parent, flags will in addition contain QT.ItemIsDropEnabled .
		"""
		res = super(Standard_QTreeWidgetItem,self).flags()
		return res
	#----------------------------------------------------------------------
	def isDisabled(self):
		"""
		Returns true if the item is disabled; otherwise returns false.
		"""
		res = super(Standard_QTreeWidgetItem,self).isDisabled()
		
		return res
	#----------------------------------------------------------------------
	def isExpanded(self):
		"""
		Returns true if the item is expanded, otherwise returns false.
		"""
		res = super(Standard_QTreeWidgetItem,self).isExpanded()
		
		return res
	#----------------------------------------------------------------------
	def isFirstColumnSpanned(self):
		"""
		Returns true if the item is spanning all the columns in a row; otherwise returns false.
		"""
		res = super(Standard_QTreeWidgetItem,self).isFirstColumnSpanned()
		
		return res
	#----------------------------------------------------------------------
	def isHidden(self):
		"""
		Returns true if the item is hidden, otherwise returns false.
		"""
		res = super(Standard_QTreeWidgetItem,self).isHidden()
		
		return res
	#----------------------------------------------------------------------
	def isSelected(self):
		"""
		Returns true if the item is selected, otherwise returns false.
		"""
		res = super(Standard_QTreeWidgetItem,self).isSelected()
		
		return res
	#----------------------------------------------------------------------
	def parent(self):
		"""
		Returns the items parent.
		"""
		res = super(Standard_QTreeWidgetItem,self).parent()
		isinstance(res,QT.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def takeChildren(self):
		"""
		Removes the list of children and returns it, otherwise returns an empty list.
		"""
		res = super(Standard_QTreeWidgetItem,self).takeChildren()
		return res
	#----------------------------------------------------------------------
	def treeWidget(self):
		"""
		Returns the tree widget that contains the item.
		"""
		res = super(Standard_QTreeWidgetItem,self).treeWidget()
		isinstance(res,QT.QTreeWidget)
		return res
	#----------------------------------------------------------------------
	def type(self):
		"""
		Returns the type of this item
		The type is used to distinguish custom items from the base class
		When subclassing PySide.QT.QStandardItem , you should reimplement this function and return a new value greater than or equal to UserType .
		"""
		
		return self.ITEM_TYPE
	#----------------------------------------------------------------------
	def addChild(self,child):
		"""
		addChild(child)
			child=QT.QTreeWidgetItem

		Appends the child item to the list of children.
		"""
		res = super(Standard_QTreeWidgetItem,self).addChild(child)
		return res
	#----------------------------------------------------------------------
	def addChildren(self,children):
		"""
		addChildren(children)
			children=unKnown


		"""
		res = super(Standard_QTreeWidgetItem,self).addChildren(children)
		return res
	#----------------------------------------------------------------------
	def background(self,column=0):
		"""
		background(column)
			column=QT.int

		Returns the brush used to render the background of the specified column .
		"""
		res = super(Standard_QTreeWidgetItem,self).background(column)
		isinstance(res,QT.QBrush)
		return res
	#----------------------------------------------------------------------
	def checkState(self,column=0):
		"""
		checkState(column)
			column=QT.int

		Returns the check state of the label in the given column .
		"""
		res = super(Standard_QTreeWidgetItem,self).checkState(column)
		return res
	#----------------------------------------------------------------------
	def child(self,index):
		"""
		child(index)
			index=QT.int

		Returns the item at the given index in the list of the items children.
		"""
		res = super(Standard_QTreeWidgetItem,self).child(index)
		isinstance(res,QT.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def children(self):
		res = []
		for row in  range(self.ChildCount):
			res.append(self.child(row))
		return res
	#----------------------------------------------------------------------
	def childrenCheckState(self,column=0):
		"""
		childrenCheckState(column)
			column=QT.int


		"""
		res = super(Standard_QTreeWidgetItem,self).childrenCheckState(column)
		return res
	#----------------------------------------------------------------------
	def data(self,column=0,role=QT.Constants.ItemDataRole.DISPLAY):
		"""
		data(column,role)
			column=QT.int
			role=QT.int

		Returns the value for the items column and role .
		"""
		res = super(Standard_QTreeWidgetItem,self).data(column,role)
		return res
	#----------------------------------------------------------------------
	def font(self,column=0):
		"""
		font(column)
			column=QT.int

		Returns the font used to render the text in the specified column .
		"""
		res = super(Standard_QTreeWidgetItem,self).font(column)
		isinstance(res,QT.QFont)
		return res
	#----------------------------------------------------------------------
	def foreground(self,column=0):
		"""
		foreground(column)
			column=QT.int

		Returns the brush used to render the foreground (e.g
		text) of the specified column .
		"""
		res = super(Standard_QTreeWidgetItem,self).foreground(column)
		isinstance(res,QT.QBrush)
		return res
	#----------------------------------------------------------------------
	def icon(self,column=0):
		"""
		icon(column)
			column=QT.int

		Returns the icon that is displayed in the specified column .
		"""
		res = super(Standard_QTreeWidgetItem,self).icon(column)
		isinstance(res,QT.QIcon)
		return res
	#----------------------------------------------------------------------
	def indexOfChild(self,child):
		"""
		indexOfChild(child)
			child=QT.QTreeWidgetItem

		Returns the index of the given child in the items list of children.
		"""
		res = super(Standard_QTreeWidgetItem,self).indexOfChild(child)
		
		return res
	#----------------------------------------------------------------------
	def row(self):
		""""""
		parent = self.parent()
		if parent == None:
			parent = self.treeWidget()
			return parent.indexOfTopLevelItem(self)
		else:
			return parent.indexOfChild(self)
	#----------------------------------------------------------------------
	def insertChild(self,index,child):
		"""
		insertChild(index,child)
			index=QT.int
			child=QT.QTreeWidgetItem

		Inserts the child item at index in the list of children.
		If the child has already been inserted somewhere else it wont be inserted again.
		"""
		res = super(Standard_QTreeWidgetItem,self).insertChild(index,child)
		return res
	#----------------------------------------------------------------------
	def insertChildren(self,index,children):
		"""
		insertChildren(index,children)
			index=QT.int
			children=unKnown


		"""
		res = super(Standard_QTreeWidgetItem,self).insertChildren(index,children)
		return res
	#----------------------------------------------------------------------
	def read(self,stream):
		"""
		read(in)
			in=QT.QDataStream

		Reads the item from stream in
		This only reads data into a single item.
		"""
		res = super(Standard_QTreeWidgetItem,self).read(stream)
		return res
	#----------------------------------------------------------------------
	def removeChild(self,child):
		"""
		removeChild(child)
			child=QT.QTreeWidgetItem

		Removes the given item indicated by child
		The removed item will not be deleted.
		"""
		res = super(Standard_QTreeWidgetItem,self).removeChild(child)
		return res
	#----------------------------------------------------------------------
	def remove_Child_By_value(self, value, column=0, role=QT.Constants.ItemDataRole.DISPLAY, max=1):
		count = 0
		for child in self.iter_children():
			if child.data(column=column, role=role) == value:
				self.removeChild(child)
				count += 1
				if count == max:
					break
	#----------------------------------------------------------------------
	def setBackground(self,column=0,brush=None):
		"""
		setBackground(column,brush)
			column=QT.int
			brush=QT.QBrush

		Sets the background brush of the label in the given column to the specified brush .
		"""
		res = super(Standard_QTreeWidgetItem,self).setBackground(column,brush)
		return res
	#----------------------------------------------------------------------
	def setCheckState(self,column=0,state=None):
		"""
		setCheckState(column,state)
			column=QT.int
			state=QT.QT.CheckState


		"""
		res = super(Standard_QTreeWidgetItem,self).setCheckState(column,state)
		return res
	#----------------------------------------------------------------------
	def setChildIndicatorPolicy(self,policy):
		"""
		setChildIndicatorPolicy(policy)
			policy=QT.QTreeWidgetItem.ChildIndicatorPolicy


		"""
		res = super(Standard_QTreeWidgetItem,self).setChildIndicatorPolicy(policy)
		return res
	#----------------------------------------------------------------------
	def setData(self,column=0,role=QT.Constants.ItemDataRole.DISPLAY,value=""):
		"""
		setData(column,role,value)
			column=QT.int
			role=QT.int
			value=object

		Sets the value for the items column and role to the given value .
		The role describes the type of data specified by value , and is defined by the QT.ItemDataRole enum.
		"""
		res = super(Standard_QTreeWidgetItem,self).setData(column,role,value)
		return res
	#----------------------------------------------------------------------
	def setDisabled(self,disabled=True):
		"""
		setDisabled(disabled)
			disabled=QT.bool

		Disables the item if disabled is true; otherwise enables the item.
		"""
		res = super(Standard_QTreeWidgetItem,self).setDisabled(disabled)
		return res
	#----------------------------------------------------------------------
	def setExpanded(self,expand=True):
		"""
		setExpanded(expand)
			expand=QT.bool

		Expands the item if expand is true, otherwise collapses the item.
		"""
		res = super(Standard_QTreeWidgetItem,self).setExpanded(expand)
		return res
	#----------------------------------------------------------------------
	def setFirstColumnSpanned(self,span):
		"""
		setFirstColumnSpanned(span)
			span=QT.bool

		Sets the first section to span all columns if span is true; otherwise all item sections are shown.
		"""
		res = super(Standard_QTreeWidgetItem,self).setFirstColumnSpanned(span)
		return res
	#----------------------------------------------------------------------
	def setFlags(self,flags):
		"""
		setFlags(flags)
			flags=QT.QT.ItemFlags


		"""
		res = super(Standard_QTreeWidgetItem,self).setFlags(flags)
		return res
	#----------------------------------------------------------------------
	def setFont(self,column,font):
		"""
		setFont(column,font)
			column=QT.int
			font=QT.QFont

		Sets the font used to display the text in the given column to the given font .
		"""
		res = super(Standard_QTreeWidgetItem,self).setFont(column,font)
		return res
	#----------------------------------------------------------------------
	def setForeground(self,column,brush):
		"""
		setForeground(column,brush)
			column=QT.int
			brush=QT.QBrush

		Sets the foreground brush of the label in the given column to the specified brush .
		"""
		res = super(Standard_QTreeWidgetItem,self).setForeground(column,brush)
		return res
	#----------------------------------------------------------------------
	def setHidden(self,hide):
		"""
		setHidden(hide)
			hide=QT.bool

		Hides the item if hide is true, otherwise shows the item.
		"""
		res = super(Standard_QTreeWidgetItem,self).setHidden(hide)
		return res
	#----------------------------------------------------------------------
	def setIcon(self,column,icon):
		"""
		setIcon(column,icon)
			column=QT.int
			icon=QT.QIcon

		Sets the icon to be displayed in the given column to icon .
		"""
		res = super(Standard_QTreeWidgetItem,self).setIcon(column,icon)
		return res
	#----------------------------------------------------------------------
	def setSelected(self,select):
		"""
		setSelected(select)
			select=QT.bool

		Sets the selected state of the item to select .
		"""
		res = super(Standard_QTreeWidgetItem,self).setSelected(select)
		return res
	#----------------------------------------------------------------------
	def setSizeHint(self,column,size):
		"""
		setSizeHint(column,size)
			column=QT.int
			size=QT.QSize

		Sets the size hint for the tree item in the given column to be size
		If no size hint is set, the item delegate will compute the size hint based on the item data.
		"""
		res = super(Standard_QTreeWidgetItem,self).setSizeHint(column,size)
		return res
	#----------------------------------------------------------------------
	def setStatusTip(self,column,statusTip):
		"""
		setStatusTip(column,statusTip)
			column=QT.int
			statusTip=unicode

		Sets the status tip for the given column to the given statusTip
		PySide.QT.QTreeWidget mouse tracking needs to be enabled for this feature to work.
		"""
		res = super(Standard_QTreeWidgetItem,self).setStatusTip(column,statusTip)
		return res
	#----------------------------------------------------------------------
	def setText(self,column,text):
		"""
		setText(column,text)
			column=QT.int
			text=unicode

		Sets the text to be displayed in the given column to the given text .
		"""
		res = super(Standard_QTreeWidgetItem,self).setText(column,text)
		return res
	#----------------------------------------------------------------------
	def setTextAlignment(self,column,alignment):
		"""
		setTextAlignment(column,alignment)
			column=QT.int
			alignment=QT.int

		Sets the text alignment for the label in the given column to the alignment specified (see QT.AlignmentFlag ).
		"""
		res = super(Standard_QTreeWidgetItem,self).setTextAlignment(column,alignment)
		return res
	#----------------------------------------------------------------------
	def setToolTip(self,column,toolTip):
		"""
		setToolTip(column,toolTip)
			column=QT.int
			toolTip=unicode

		Sets the tooltip for the given column to toolTip .
		"""
		res = super(Standard_QTreeWidgetItem,self).setToolTip(column,toolTip)
		return res
	#----------------------------------------------------------------------
	def setWhatsThis(self,column,whatsThis):
		"""
		setWhatsThis(column,whatsThis)
			column=QT.int
			whatsThis=unicode

		Sets the Whats This? help for the given column to whatsThis .
		"""
		res = super(Standard_QTreeWidgetItem,self).setWhatsThis(column,whatsThis)
		return res
	#----------------------------------------------------------------------
	def sizeHint(self,column=0):
		"""
		sizeHint(column)
			column=QT.int

		Returns the size hint set for the tree item in the given column (see PySide.QT.QSize ).
		"""
		res = super(Standard_QTreeWidgetItem,self).sizeHint(column)
		isinstance(res,QT.QSize)
		return res
	#----------------------------------------------------------------------
	def sortChildren(self,*args,**kwargs):
		"""
		sortChildren(column,order)
			column=QT.int
			order=QT.QT.SortOrder

		sortChildren(column,order,climb)
			column=QT.int
			order=QT.QT.SortOrder
			climb=QT.bool


		"""
		res = super(Standard_QTreeWidgetItem,self).sortChildren(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def statusTip(self,column=0):
		"""
		statusTip(column)
			column=QT.int

		Returns the status tip for the contents of the given column .
		"""
		res = super(Standard_QTreeWidgetItem,self).statusTip(column)
		return res
	#----------------------------------------------------------------------
	def takeChild(self,index):
		"""
		takeChild(index)
			index=QT.int

		Removes the item at index and returns it, otherwise return 0.
		"""
		res = super(Standard_QTreeWidgetItem,self).takeChild(index)
		isinstance(res,QT.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def text(self,column=0):
		"""
		text(column)
			column=QT.int

		Returns the text in the specified column .
		"""
		res = super(Standard_QTreeWidgetItem,self).text(column)
		return res
	#----------------------------------------------------------------------
	def textAlignment(self,column=0):
		"""
		textAlignment(column)
			column=QT.int

		Returns the text alignment for the label in the given column (see QT.AlignmentFlag ).
		"""
		res = super(Standard_QTreeWidgetItem,self).textAlignment(column)
		
		return res
	#----------------------------------------------------------------------
	def toolTip(self,column=0):
		"""
		toolTip(column)
			column=QT.int

		Returns the tool tip for the given column .
		"""
		res = super(Standard_QTreeWidgetItem,self).toolTip(column)
		return res
	#----------------------------------------------------------------------
	def whatsThis(self,column=0):
		"""
		whatsThis(column)
			column=QT.int

		Returns the Whats This? help for the contents of the given column .
		"""
		res = super(Standard_QTreeWidgetItem,self).whatsThis(column)
		return res
	#----------------------------------------------------------------------
	def write(self,out):
		"""
		write(out)
			out=QT.QDataStream

		Writes the item to stream out
		This only writes data from one single item.
		"""
		res = super(Standard_QTreeWidgetItem,self).write(out)
		return res
	
	ChildCount  = property(childCount)
	Disabled    = property(isDisabled,setDisabled)
	Expanded    = property(isExpanded,setExpanded)
	Hidden      = property(isHidden,setHidden)
	Selected    = property(isSelected,setSelected)
	Flags       = property(flags,setFlags)
	ColumnCount = property(columnCount)
	IsDisabled  = property(isDisabled, setDisabled)
	Foreground  = property(foreground, setForeground)
	Icon        = property(icon, setIcon)
	Font        = property(font, setFont)
	CheckState  = property(checkState, setCheckState)
	Background  = property(background, setBackground)
	Parent      = property(parent)
	IsExpanded  = property(isExpanded, setExpanded)
	IsHidden    = property(isHidden, setHidden)

