
from ... import QT

class Item_Delegate(QT.QItemDelegate):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(Item_Delegate,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def hasClipping(self):
		"""
		This property holds if the delegate should clip the paint events.
		This property will set the paint clip to the size of the item
		The default value is on
		It is useful for cases such as when images are larger than the size of the item.
		"""
		res = super(Item_Delegate,self).hasClipping()
		return res
	#----------------------------------------------------------------------
	def itemEditorFactory(self):
		"""
		Returns the editor factory used by the item delegate
		If no editor factory is set, the function will return null.
		"""
		res = super(Item_Delegate,self).itemEditorFactory()
		isinstance(res,QT.QItemEditorFactory)
		return res
	#----------------------------------------------------------------------
	def decoration(self,option,variant):
		"""
		decoration(option,variant)
			option=QT.QStyleOptionViewItem
			variant=object

		Returns the pixmap used to decorate the root of the item view
		The style option controls the appearance of the root; the variant refers to the data associated with an item.
		"""
		res = super(Item_Delegate,self).decoration(option,variant)
		isinstance(res,QT.QPixmap)
		return res
	#----------------------------------------------------------------------
	def drawBackground(self,painter,option,index):
		"""
		drawBackground(painter,option,index)
			painter=QT.QPainter
			option=QT.QStyleOptionViewItem
			index=QT.QModelIndex

		Renders the item background for the given index , using the given painter and style option .
		"""
		res = super(Item_Delegate,self).drawBackground(painter,option,index)
		return res
	#----------------------------------------------------------------------
	def drawCheck(self,painter,option,rect,state):
		"""
		drawCheck(painter,option,rect,state)
			painter=QT.QPainter
			option=QT.QStyleOptionViewItem
			rect=QT.QRect
			state=QT.Qt.CheckState


		"""
		res = super(Item_Delegate,self).drawCheck(painter,option,rect,state)
		return res
	#----------------------------------------------------------------------
	def drawDecoration(self,painter,option,rect,pixmap):
		"""
		drawDecoration(painter,option,rect,pixmap)
			painter=QT.QPainter
			option=QT.QStyleOptionViewItem
			rect=QT.QRect
			pixmap=QT.QPixmap

		Renders the decoration pixmap within the rectangle specified by rect using the given painter and style option .
		"""
		res = super(Item_Delegate,self).drawDecoration(painter,option,rect,pixmap)
		return res
	#----------------------------------------------------------------------
	def drawDisplay(self,painter,option,rect,text):
		"""
		drawDisplay(painter,option,rect,text)
			painter=QT.QPainter
			option=QT.QStyleOptionViewItem
			rect=QT.QRect
			text=unicode

		Renders the item view text within the rectangle specified by rect using the given painter and style option .
		"""
		res = super(Item_Delegate,self).drawDisplay(painter,option,rect,text)
		return res
	#----------------------------------------------------------------------
	def drawFocus(self,painter,option,rect):
		"""
		drawFocus(painter,option,rect)
			painter=QT.QPainter
			option=QT.QStyleOptionViewItem
			rect=QT.QRect

		Renders the region within the rectangle specified by rect , indicating that it has the focus, using the given painter and style option .
		"""
		res = super(Item_Delegate,self).drawFocus(painter,option,rect)
		return res
	#----------------------------------------------------------------------
	def rect(self,option,index,role):
		"""
		rect(option,index,role)
			option=QT.QStyleOptionViewItem
			index=QT.QModelIndex
			role=QT.int


		"""
		res = super(Item_Delegate,self).rect(option,index,role)
		isinstance(res,QT.QRect)
		return res
	#----------------------------------------------------------------------
	def setClipping(self,clip):
		"""
		setClipping(clip)
			clip=QT.bool

		This property holds if the delegate should clip the paint events.
		This property will set the paint clip to the size of the item
		The default value is on
		It is useful for cases such as when images are larger than the size of the item.
		"""
		res = super(Item_Delegate,self).setClipping(clip)
		return res
	#----------------------------------------------------------------------
	def setItemEditorFactory(self,factory):
		"""
		setItemEditorFactory(factory)
			factory=QT.QItemEditorFactory

		Sets the editor factory to be used by the item delegate to be the factory specified
		If no editor factory is set, the item delegate will use the default editor factory.
		"""
		res = super(Item_Delegate,self).setItemEditorFactory(factory)
		return res
	#----------------------------------------------------------------------
	def setOptions(self,index,option):
		"""
		setOptions(index,option)
			index=QT.QModelIndex
			option=QT.QStyleOptionViewItem


		"""
		res = super(Item_Delegate,self).setOptions(index,option)
		isinstance(res,QT.QStyleOptionViewItem)
		return res
	#----------------------------------------------------------------------
	def textRectangle(self,painter,rect,font,text):
		"""
		textRectangle(painter,rect,font,text)
			painter=QT.QPainter
			rect=QT.QRect
			font=QT.QFont
			text=unicode


		"""
		res = super(Item_Delegate,self).textRectangle(painter,rect,font,text)
		isinstance(res,QT.QRect)
		return res
