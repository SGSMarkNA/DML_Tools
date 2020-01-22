from .... import QT
from ..Item_Data_Roles import Base_Item_Data_Roles

class Base_Header_View(QT.QHeaderView):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(Base_Header_View,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def cascadingSectionResizes(self):
		"""
		This property holds whether interactive resizing will be cascaded to the following sections once the section being resized by the user has reached its minimum size.
		This property only affects sections that have Interactive as their resize mode.
		The default value is false.
		"""
		res = super(Base_Header_View,self).cascadingSectionResizes()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def count(self):
		"""
		Returns the number of sections in the header.
		"""
		res = super(Base_Header_View,self).count()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def defaultAlignment(self):
		"""
		This property holds the default alignment of the text in each header section.
		"""
		res = super(Base_Header_View,self).defaultAlignment()
		isinstance(res,QT.Qt.Alignment)
		return res
	#----------------------------------------------------------------------
	def defaultSectionSize(self):
		"""
		This property holds the default size of the header sections before resizing..
		This property only affects sections that have Interactive or Fixed as their resize mode.
		"""
		res = super(Base_Header_View,self).defaultSectionSize()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def geometriesChanged(self):
		"""

		"""
		res = super(Base_Header_View,self).geometriesChanged()
		return res
	#----------------------------------------------------------------------
	def hiddenSectionCount(self):
		"""
		Returns the number of sections in the header that has been hidden.
		"""
		res = super(Base_Header_View,self).hiddenSectionCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def highlightSections(self):
		"""
		This property holds whether the sections containing selected items are highlighted.
		By default, this property is false.
		"""
		res = super(Base_Header_View,self).highlightSections()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isClickable(self):
		"""
		Returns true if the header is clickable; otherwise returns false
		A clickable header could be set up to allow the user to change the representation of the data in the view related to the header.
		"""
		res = super(Base_Header_View,self).isClickable()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isMovable(self):
		"""
		Returns true if the header can be moved by the user; otherwise returns false.
		"""
		res = super(Base_Header_View,self).isMovable()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isSortIndicatorShown(self):
		"""
		This property holds whether the sort indicator is shown.
		By default, this property is false.
		"""
		res = super(Base_Header_View,self).isSortIndicatorShown()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def length(self):
		"""
		Returns the length along the orientation of the header.
		"""
		res = super(Base_Header_View,self).length()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def minimumSectionSize(self):
		"""
		This property holds the minimum size of the header sections..
		The minimum section size is the smallest section size allowed
		If the minimum section size is set to -1, QT.QHeaderView will use the maximum of the global strut or the font metrics size.
		This property is honored by all resize modes .
		"""
		res = super(Base_Header_View,self).minimumSectionSize()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def offset(self):
		"""
		Returns the offset of the header: this is the headers left-most (or top-most for vertical headers) visible pixel.
		"""
		res = super(Base_Header_View,self).offset()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def orientation(self):
		"""
		Returns the orientation of the header.
		"""
		res = super(Base_Header_View,self).orientation()
		isinstance(res,QT.Qt.Orientation)
		return res
	#----------------------------------------------------------------------
	def saveState(self):
		"""
		Saves the current state of this header view.
		To restore the saved state, pass the return value to QT.QHeaderView.restoreState() .
		"""
		res = super(Base_Header_View,self).saveState()
		isinstance(res,QT.QByteArray)
		return res
	#----------------------------------------------------------------------
	def sectionsHidden(self):
		"""
		Returns true if sections in the header has been hidden; otherwise returns false;
		"""
		res = super(Base_Header_View,self).sectionsHidden()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def sectionsMoved(self):
		"""
		Returns true if sections in the header has been moved; otherwise returns false;
		"""
		res = super(Base_Header_View,self).sectionsMoved()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def sortIndicatorOrder(self):
		"""
		Returns the order for the sort indicator
		If no section has a sort indicator the return value of this function is undefined.
		"""
		res = super(Base_Header_View,self).sortIndicatorOrder()
		isinstance(res,QT.Qt.SortOrder)
		return res
	#----------------------------------------------------------------------
	def sortIndicatorSection(self):
		"""
		Returns the logical index of the section that has a sort indicator
		By default this is section 0.
		"""
		res = super(Base_Header_View,self).sortIndicatorSection()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def stretchLastSection(self):
		"""
		This property holds whether the last visible section in the header takes up all the available space.
		The default value is false.
		"""
		res = super(Base_Header_View,self).stretchLastSection()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def stretchSectionCount(self):
		"""
		Returns the number of sections that are set to resize mode stretch
		In views, this can be used to see if the headerview needs to resize the sections when the views geometry changes.
		"""
		res = super(Base_Header_View,self).stretchSectionCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def hideSection(self,logicalIndex):
		"""
		hideSection(logicalIndex)
			logicalIndex=int

		Hides the section specified by logicalIndex .
		"""
		res = super(Base_Header_View,self).hideSection(logicalIndex)
		return res
	#----------------------------------------------------------------------
	def isSectionHidden(self,logicalIndex):
		"""
		isSectionHidden(logicalIndex)
			logicalIndex=int

		Returns true if the section specified by logicalIndex is explicitly hidden from the user; otherwise returns false.
		"""
		res = super(Base_Header_View,self).isSectionHidden(logicalIndex)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def logicalIndex(self,visualIndex):
		"""
		logicalIndex(visualIndex)
			visualIndex=int

		Returns the logicalIndex for the section at the given visualIndex position, or -1 if visualIndex < 0 or visualIndex >= QHeaderView.count() .
		Note that the visualIndex is not affected by hidden sections.
		"""
		res = super(Base_Header_View,self).logicalIndex(visualIndex)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def logicalIndexAt(self,*args,**kwargs):
		"""
		logicalIndexAt(x,y)
			x=int
			y=int

		logicalIndexAt(position)
			position=int

		logicalIndexAt(pos)
			pos=QT.QPoint

		Returns the logical index of the section at the given coordinate
		If the header is horizontal x will be used, otherwise y will be used to find the logical index.
		"""
		res = super(Base_Header_View,self).logicalIndexAt(*args,**kwargs)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def moveSection(self,f, t):
		"""
		moveSection(from,to)
			from=int
			to=int

		Moves the section at visual index from to occupy visual index to .
		"""
		res = super(Base_Header_View,self).moveSection(f,t)
		return res
	##----------------------------------------------------------------------
	#def paintSection(self,painter,rect,logicalIndex):
		#"""

		#paintSection(painter,rect,logicalIndex)
			#painter=QT.QPainter
			#rect=QT.QRect
			#logicalIndex=int

		#Paints the section specified by the given logicalIndex , using the given painter and rect .
		#Normally, you do not have to call this function.
		#"""
		#res = super(QHeaderView,self).paintSection(painter,rect,logicalIndex)
		#return res
	#----------------------------------------------------------------------
	def resizeMode(self,logicalIndex):
		"""
		resizeMode(logicalIndex)
			logicalIndex=int

		Returns the resize mode that applies to the section specified by the given logicalIndex .
		"""
		res = super(Base_Header_View,self).resizeMode(logicalIndex)
		isinstance(res,QT.QHeaderView.ResizeMode)
		return res
	#----------------------------------------------------------------------
	def resizeSection(self,logicalIndex,size):
		"""
		resizeSection(logicalIndex,size)
			logicalIndex=int
			size=int

		Resizes the section specified by logicalIndex to size measured in pixels.
		"""
		res = super(Base_Header_View,self).resizeSection(logicalIndex,size)
		return res
	#----------------------------------------------------------------------
	def restoreState(self,state):
		"""
		restoreState(state)
			state=QT.QByteArray

		Restores the state of this header view
		This function returns true if the state was restored; otherwise returns false.
		"""
		res = super(Base_Header_View,self).restoreState(state)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def sectionPosition(self,logicalIndex):
		"""
		sectionPosition(logicalIndex)
			logicalIndex=int

		Returns the section position of the given logicalIndex , or -1 if the section is hidden.
		"""
		res = super(Base_Header_View,self).sectionPosition(logicalIndex)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def sectionSize(self,logicalIndex):
		"""
		sectionSize(logicalIndex)
			logicalIndex=int

		Returns the width (or height for vertical headers) of the given logicalIndex .
		"""
		res = super(Base_Header_View,self).sectionSize(logicalIndex)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def sectionSizeFromContents(self,logicalIndex):
		"""
		sectionSizeFromContents(logicalIndex)
			logicalIndex=int

		Returns the size of the contents of the section specified by the given logicalIndex .
		"""
		res = super(Base_Header_View,self).sectionSizeFromContents(logicalIndex)
		isinstance(res,QT.QSize)
		return res
	#----------------------------------------------------------------------
	def sectionSizeHint(self,logicalIndex):
		"""
		sectionSizeHint(logicalIndex)
			logicalIndex=int

		Returns a suitable size hint for the section specified by logicalIndex .
		"""
		res = super(Base_Header_View,self).sectionSizeHint(logicalIndex)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def sectionViewportPosition(self,logicalIndex):
		"""
		sectionViewportPosition(logicalIndex)
			logicalIndex=int

		Returns the section viewport position of the given logicalIndex .
		If the section is hidden, the return value is undefined.
		"""
		res = super(Base_Header_View,self).sectionViewportPosition(logicalIndex)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def setCascadingSectionResizes(self,enable):
		"""
		setCascadingSectionResizes(enable)
			enable=bool

		This property holds whether interactive resizing will be cascaded to the following sections once the section being resized by the user has reached its minimum size.
		This property only affects sections that have Interactive as their resize mode.
		The default value is false.
		"""
		res = super(Base_Header_View,self).setCascadingSectionResizes(enable)
		return res
	#----------------------------------------------------------------------
	def setClickable(self,clickable):
		"""

		setClickable(clickable)
			clickable=bool

		If clickable is true, the header will respond to single clicks.
		"""
		if QT.PySide_version == 2:
			res = super(Base_Header_View,self).setSectionsClickable(clickable)
		else:
			res = super(Base_Header_View,self).setClickable(clickable)
		return res
	#----------------------------------------------------------------------
	def setDefaultAlignment(self,alignment):
		"""
		setDefaultAlignment(alignment)
			alignment=QT.Qt.Alignment

		This property holds the default alignment of the text in each header section.
		"""
		res = super(Base_Header_View,self).setDefaultAlignment(alignment)
		return res
	#----------------------------------------------------------------------
	def setDefaultSectionSize(self,size):
		"""
		setDefaultSectionSize(size)
			size=int

		This property holds the default size of the header sections before resizing..
		This property only affects sections that have Interactive or Fixed as their resize mode.
		"""
		res = super(Base_Header_View,self).setDefaultSectionSize(size)
		return res
	#----------------------------------------------------------------------
	def setHighlightSections(self,highlight):
		"""
		setHighlightSections(highlight)
			highlight=bool

		This property holds whether the sections containing selected items are highlighted.
		By default, this property is false.
		"""
		res = super(Base_Header_View,self).setHighlightSections(highlight)
		return res
	#----------------------------------------------------------------------
	def setMinimumSectionSize(self,size):
		"""
		setMinimumSectionSize(size)
			size=int

		This property holds the minimum size of the header sections..
		The minimum section size is the smallest section size allowed
		If the minimum section size is set to -1, QT.QHeaderView will use the maximum of the global strut or the font metrics size.
		This property is honored by all resize modes .
		"""
		res = super(Base_Header_View,self).setMinimumSectionSize(size)
		return res
	#----------------------------------------------------------------------
	def setResizeMode(self,*args,**kwargs):
		"""
		setResizeMode(logicalIndex,mode)
			logicalIndex=int
			mode=QT.QHeaderView.ResizeMode

		setResizeMode(mode)
			mode=QT.QHeaderView.ResizeMode

		This is an overloaded function.
		Sets the constraints on how the section specified by logicalIndex in the header can be resized to those described by the given mode
		The logical index should exist at the time this function is called.
		"""
		res = super(Base_Header_View,self).setResizeMode(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setSectionHidden(self,logicalIndex,hide):
		"""
		setSectionHidden(logicalIndex,hide)
			logicalIndex=int
			hide=bool

		If hide is true the section specified by logicalIndex is hidden; otherwise the section is shown.
		"""
		res = super(Base_Header_View,self).setSectionHidden(logicalIndex,hide)
		return res
	#----------------------------------------------------------------------
	def setSectionsMovable(self,val):
		"""
		setSectionHidden(logicalIndex,hide)
			logicalIndex=int
			hide=bool

		If hide is true the section specified by logicalIndex is hidden; otherwise the section is shown.
		"""
		try:
			res = super(Base_Header_View,self).setSectionsMovable(val)
		except:
			res = super(Base_Header_View,self).setMovable(val)
		return res
	#----------------------------------------------------------------------
	def setSortIndicator(self,logicalIndex,order):
		"""
		setSortIndicator(logicalIndex,order)
			logicalIndex=int
			order=QT.Qt.SortOrder


		"""
		res = super(Base_Header_View,self).setSortIndicator(logicalIndex,order)
		return res
	#----------------------------------------------------------------------
	def setSortIndicatorShown(self,show):
		"""
		setSortIndicatorShown(show)
			show=bool

		This property holds whether the sort indicator is shown.
		By default, this property is false.
		"""
		res = super(Base_Header_View,self).setSortIndicatorShown(show)
		return res
	#----------------------------------------------------------------------
	def setStretchLastSection(self,stretch):
		"""
		setStretchLastSection(stretch)
			stretch=bool

		This property holds whether the last visible section in the header takes up all the available space.
		The default value is false.
		"""
		res = super(Base_Header_View,self).setStretchLastSection(stretch)
		return res
	#----------------------------------------------------------------------
	def showSection(self,logicalIndex):
		"""
		showSection(logicalIndex)
			logicalIndex=int

		Shows the section specified by logicalIndex .
		"""
		res = super(Base_Header_View,self).showSection(logicalIndex)
		return res
	#----------------------------------------------------------------------
	def swapSections(self,first,second):
		"""
		swapSections(first,second)
			first=int
			second=int

		Swaps the section at visual index first with the section at visual index second .
		"""
		res = super(Base_Header_View,self).swapSections(first,second)
		return res
	#----------------------------------------------------------------------
	def visualIndex(self,logicalIndex):
		"""
		visualIndex(logicalIndex)
			logicalIndex=int

		Returns the visual index position of the section specified by the given logicalIndex , or -1 otherwise.
		Hidden sections still have valid visual indexes.
		"""
		res = super(Base_Header_View,self).visualIndex(logicalIndex)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def visualIndexAt(self,position):
		"""
		visualIndexAt(position)
			position=int

		Returns the visual index of the section that covers the given position in the viewport.
		"""
		res = super(Base_Header_View,self).visualIndexAt(position)
		isinstance(res,int)
		return res


