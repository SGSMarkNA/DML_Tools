
from .... import QT
from ..Item_Data_Roles import Base_Item_Data_Roles


class SpinBoxDelegate(QT.QItemDelegate):
	def createEditor(self, parent, option, index):
		val = index.data(Base_Item_Data_Roles.USER)
		editor = None
		if hasattr(val,"has_editor"):
			if val.has_editor:
				editor = val.create_editor(parent=parent)
		if editor == None:
			editor = super(SpinBoxDelegate,self).createEditor(parent, option, index)

		return editor

	def setEditorData(self, spinBox, index):
		value = index.model().data(index, QT.Qt.EditRole)

		spinBox.setValue(int(value))

	def setModelData(self, spinBox, model, index):
		spinBox.interpretText()
		value = spinBox.value()

		model.setData(index, value, QT.Qt.EditRole)

	def updateEditorGeometry(self, editor, option, index):
		editor.setGeometry(option.rect)

class Item_View_Delegate(QT.QItemDelegate):

	def paint(self, painter, option, index):
		super(Item_View_Delegate, self).paint(painter, option, index)
	# #----------------------------------------------------------------------
	def drawDisplay(self, painter, option, rect, text):
		if option.widget.underMouse():
			painter.drawRect(rect.adjusted(2, 2, -2, -1))
			painter.drawText(rect, QT.Constants.AlignmentFlag.Horizontal.Center|QT.Constants.AlignmentFlag.Vertical.Center, text)
			painter.fillRect(rect, QT.Constants.Colors.BLUE)
		else:
			super(Item_View_Delegate, self).drawDisplay(painter, option, rect, text)
	#----------------------------------------------------------------------
	def drawFocus(self, painter, option, rect):
		""""""
		isinstance(painter, QT.QPainter)
		isinstance(rect, QT.QRect)
		if option.widget._item_under_mouse is not None:
			painter.fillRect(option.widget.visualRect(option.widget._item_under_mouse), QT.Constants.Colors.RED)
			painter.drawText(rect, QT.Constants.AlignmentFlag.Horizontal.Center|QT.Constants.AlignmentFlag.Vertical.Center, option.widget._item_under_mouse.data())
		else:
			super(Item_View_Delegate, self).drawFocus(painter, option, rect)
	#----------------------------------------------------------------------
	def drawBackground (self, painter, option, index):
		painter.fillRect(option.widget.visualRect(option.widget.CurrentIndex), QT.Constants.Colors.BLUE)
		super(Item_View_Delegate, self).drawBackground(painter, option, index)
	#----------------------------------------------------------------------
	def createEditor(self, parent, option, index):
		# editor = QtGui.QSpinBox(parent)
		# editor.setMinimum(0)
		# editor.setMaximum(100)
		editor = super(Item_View_Delegate, self).createEditor(parent, option, index)
		return editor
	#----------------------------------------------------------------------
	def setEditorData(self, spinBox, index):
		super(Item_View_Delegate, self).setEditorData(spinBox, index)
		# value = index.model().data(index, QtCore.Qt.EditRole)
		# spinBox.setValue(value)
	#----------------------------------------------------------------------
	def setModelData(self, spinBox, model, index):
		# # spinBox.interpretText()
		# # value = spinBox.value()
		super(Item_View_Delegate, self).setModelData(spinBox, model, index)
		# model.setData(index, value, QtCore.Qt.EditRole)
	# #----------------------------------------------------------------------
	# def updateEditorGeometry(self, editor, option, index):
		# super(Item_View_Delegate, self).updateEditorGeometry(editor, option, index)
		# # editor.setGeometry(option.rect)

