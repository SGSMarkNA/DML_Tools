from .... import QT

class Standard_QListWidgetItem(QT.QListWidgetItem):
	''''''
	ITEM_TYPE  = QT.userType_generator()
	def __init__(self,*args,**kwargs):
		''''''
		super(Standard_QListWidgetItem,self).__init__(*args,**kwargs)
		if False:
			self.ITEM_TYPE = int
	#----------------------------------------------------------------------
	def background(self):
		"""
		Returns the brush used to display the list items background.
		"""
		res = super(Standard_QListWidgetItem,self).background()
		isinstance(res,QT.QBrush)
		return res
	#----------------------------------------------------------------------
	def checkState(self):
		"""
		Returns the checked state of the list item (see QT.CheckState ).
		"""
		res = super(Standard_QListWidgetItem,self).checkState()
		isinstance(res,QT.Qt.CheckState)
		return res
	#----------------------------------------------------------------------
	def clone(self):
		"""
		Creates an exact copy of the item.
		"""
		res = super(Standard_QListWidgetItem,self).clone()
		isinstance(res,QT.QListWidgetItem)
		return res
	#----------------------------------------------------------------------
	def flags(self):
		"""
		Returns the item flags for this item (see QT.ItemFlags ).
		"""
		res = super(Standard_QListWidgetItem,self).flags()
		isinstance(res,QT.Qt.ItemFlags)
		return res
	#----------------------------------------------------------------------
	def font(self):
		"""
		Returns the font used to display this list items text.
		"""
		res = super(Standard_QListWidgetItem,self).font()
		isinstance(res,QT.QFont)
		return res
	#----------------------------------------------------------------------
	def foreground(self):
		"""
		Returns the brush used to display the list items foreground (e.g
		text).
		"""
		res = super(Standard_QListWidgetItem,self).foreground()
		isinstance(res,QT.QBrush)
		return res
	#----------------------------------------------------------------------
	def icon(self):
		"""
		Returns the list items icon.
		"""
		res = super(Standard_QListWidgetItem,self).icon()
		isinstance(res,QT.QIcon)
		return res
	#----------------------------------------------------------------------
	def isHidden(self):
		"""
		Returns true if the item is hidden; otherwise returns false.
		"""
		res = super(Standard_QListWidgetItem,self).isHidden()
		
		return res
	#----------------------------------------------------------------------
	def isSelected(self):
		"""
		Returns true if the item is selected; otherwise returns false.
		"""
		res = super(Standard_QListWidgetItem,self).isSelected()
		
		return res
	#----------------------------------------------------------------------
	def listWidget(self):
		"""
		Returns the list widget containing the item.
		"""
		res = super(Standard_QListWidgetItem,self).listWidget()
		isinstance(res,QT.QListWidget)
		return res
	#----------------------------------------------------------------------
	def sizeHint(self):
		"""
		Returns the size hint set for the list item.
		"""
		res = super(Standard_QListWidgetItem,self).sizeHint()
		isinstance(res,QT.QSize)
		return res
	#----------------------------------------------------------------------
	def statusTip(self):
		"""
		Returns the list items status tip.
		"""
		res = super(Standard_QListWidgetItem,self).statusTip()
		return res
	#----------------------------------------------------------------------
	def text(self):
		"""
		Returns the list items text.
		"""
		res = super(Standard_QListWidgetItem,self).text()
		return res
	#----------------------------------------------------------------------
	def textAlignment(self):
		"""
		Returns the text alignment for the list item.
		"""
		res = super(Standard_QListWidgetItem,self).textAlignment()
		
		return res
	#----------------------------------------------------------------------
	def toolTip(self):
		"""
		Returns the list items tooltip.
		"""
		res = super(Standard_QListWidgetItem,self).toolTip()
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
	def whatsThis(self):
		"""
		Returns the list items Whats This? help text.
		"""
		res = super(Standard_QListWidgetItem,self).whatsThis()
		return res
	#----------------------------------------------------------------------
	def data(self,role):
		"""
		data(role)
			role=QtCore.int

		Returns the items data for a given role
		Reimplement this function if you need extra roles or special behavior for certain roles.
		"""
		res = super(Standard_QListWidgetItem,self).data(role)
		return res
	#----------------------------------------------------------------------
	def __lt__(self,other):
		"""
		__lt__(other)
			other=QtGui.QListWidgetItem

		Returns true if this items text is less then other items text; otherwise returns false.
		"""
		res = super(Standard_QListWidgetItem,self).__lt__(other)
		
		return res
	#----------------------------------------------------------------------
	def read(self,DataStream):
		"""
		read(in)
			in=QtCore.QDataStream

		Reads the item from stream in .
		"""
		res = super(Standard_QListWidgetItem,self).read(DataStream)
		return res
	#----------------------------------------------------------------------
	def setBackground(self,brush):
		"""
		setBackground(brush)
			brush=QtGui.QBrush

		Sets the background brush of the list item to the given brush .
		"""
		res = super(Standard_QListWidgetItem,self).setBackground(brush)
		return res
	#----------------------------------------------------------------------
	def setCheckState(self,state):
		"""
		setCheckState(state)
			state=QT.CheckState


		"""
		res = super(Standard_QListWidgetItem,self).setCheckState(state)
		return res
	#----------------------------------------------------------------------
	def setData(self,role,value):
		"""
		setData(role,value)
			role=QtCore.int
			value=object

		Sets the data for a given role to the given value
		Reimplement this function if you need extra roles or special behavior for certain roles.
		"""
		res = super(Standard_QListWidgetItem,self).setData(role,value)
		return res
	#----------------------------------------------------------------------
	def setFlags(self,flags):
		"""
		setFlags(flags)
			flags=QT.ItemFlags


		"""
		res = super(Standard_QListWidgetItem,self).setFlags(flags)
		return res
	#----------------------------------------------------------------------
	def setFont(self,font):
		"""
		setFont(font)
			font=QtGui.QFont

		Sets the font used when painting the item to the given font .
		"""
		res = super(Standard_QListWidgetItem,self).setFont(font)
		return res
	#----------------------------------------------------------------------
	def setForeground(self,brush):
		"""
		setForeground(brush)
			brush=QtGui.QBrush

		Sets the foreground brush of the list item to the given brush .
		"""
		res = super(Standard_QListWidgetItem,self).setForeground(brush)
		return res
	#----------------------------------------------------------------------
	def setHidden(self,hide):
		"""
		setHidden(hide)
			hide=QtCore.bool

		Hides the item if hide is true; otherwise shows the item.
		"""
		res = super(Standard_QListWidgetItem,self).setHidden(hide)
		return res
	#----------------------------------------------------------------------
	def setIcon(self,icon):
		"""
		setIcon(icon)
			icon=QtGui.QIcon

		Sets the icon for the list item to the given icon .
		"""
		res = super(Standard_QListWidgetItem,self).setIcon(icon)
		return res
	#----------------------------------------------------------------------
	def setSelected(self,select):
		"""
		setSelected(select)
			select=QtCore.bool

		Sets the selected state of the item to select .
		"""
		res = super(Standard_QListWidgetItem,self).setSelected(select)
		return res
	#----------------------------------------------------------------------
	def setSizeHint(self,size):
		"""
		setSizeHint(size)
			size=QtCore.QSize

		Sets the size hint for the list item to be size
		If no size hint is set, the item delegate will compute the size hint based on the item data.
		"""
		res = super(Standard_QListWidgetItem,self).setSizeHint(size)
		return res
	#----------------------------------------------------------------------
	def setStatusTip(self,statusTip):
		"""
		setStatusTip(statusTip)
			statusTip=unicode

		Sets the status tip for the list item to the text specified by statusTip
		PySide.QtGui.QListWidget mouseTracking needs to be enabled for this feature to work.
		"""
		res = super(Standard_QListWidgetItem,self).setStatusTip(statusTip)
		return res
	#----------------------------------------------------------------------
	def setText(self,text):
		"""
		setText(text)
			text=unicode

		Sets the text for the list widget items to the given text .
		"""
		res = super(Standard_QListWidgetItem,self).setText(text)
		return res
	#----------------------------------------------------------------------
	def setTextAlignment(self,alignment):
		"""
		setTextAlignment(alignment)
			alignment=QtCore.int

		Sets the list items text alignment to alignment .
		"""
		res = super(Standard_QListWidgetItem,self).setTextAlignment(alignment)
		return res
	#----------------------------------------------------------------------
	def setToolTip(self,toolTip):
		"""
		setToolTip(toolTip)
			toolTip=unicode

		Sets the tooltip for the list item to the text specified by toolTip .
		"""
		res = super(Standard_QListWidgetItem,self).setToolTip(toolTip)
		return res
	#----------------------------------------------------------------------
	def setWhatsThis(self,whatsThis):
		"""
		setWhatsThis(whatsThis)
			whatsThis=unicode

		Sets the Whats This? help for the list item to the text specified by whatsThis .
		"""
		res = super(Standard_QListWidgetItem,self).setWhatsThis(whatsThis)
		return res
	#----------------------------------------------------------------------
	def write(self,out):
		"""
		write(out)
			out=QtCore.QDataStream

		Writes the item to stream out .
		"""
		res = super(Standard_QListWidgetItem,self).write(out)
		return res
