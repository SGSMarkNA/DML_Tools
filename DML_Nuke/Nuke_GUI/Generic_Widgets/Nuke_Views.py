import os
from .. import Python_Custom_Widget_Knob
import DML_Tools
DML_PYQT = DML_Tools.DML_PYQT
import nuke
import uuid

	
########################################################################
class View_Modes(nuke.FnPySingleton):
	""""""
	viewMode,imageMode = range(2)
	def __init__(self):
		"""Constructor"""
		self.mode = 0
	#----------------------------------------------------------------------
	@property
	def isViewMode(self):
		""""""
		return self.mode == self.viewMode
	#----------------------------------------------------------------------
	@property
	def isImageMode(self):
		""""""
		return self.mode == self.imageMode

Nuke_View_Mode = View_Modes()


########################################################################
class DML_Nuke_View_Table_Widget_Item(DML_PYQT.QTableWidgetItem):
	""""""
	def __init__(self,nuke_view):
		"""Constructor"""
		super(DML_Nuke_View_Table_Widget_Item, self).__init__("",type=DML_PYQT.QTableWidgetItem.UserType)
		self._nuke_view = nuke_view
		self.setData(DML_PYQT.Qt.ItemDataRole.UserRole,nuke_view)
		
########################################################################
class DML_Nuke_View_Name_Table_Widget_Item(DML_Nuke_View_Table_Widget_Item):
	""""""
	
	#----------------------------------------------------------------------
	def data(self,role):
		""""""
		if role == DML_PYQT.Qt.ItemDataRole.DisplayRole or role == DML_PYQT.Qt.ItemDataRole.EditRole:
			return self._nuke_view.name
		else:
			return super(DML_Nuke_View_Name_Table_Widget_Item, self).data(role)
	#----------------------------------------------------------------------
	def setData(self,role,value):
		""""""
		if role == DML_PYQT.Qt.ItemDataRole.EditRole:
			self._nuke_view.name = value
		else:
			super(DML_Nuke_View_Name_Table_Widget_Item, self).setData(role,value)
			
########################################################################
class DML_Nuke_View_Color_Table_Widget_Item(DML_Nuke_View_Table_Widget_Item):
	""""""
	
	#----------------------------------------------------------------------
	def data(self,role):
		""""""
		if role == DML_PYQT.Qt.ItemDataRole.BackgroundRole:
			return self._nuke_view.color
		else:
			return super(DML_Nuke_View_Color_Table_Widget_Item, self).data(role)
	#----------------------------------------------------------------------
	def setData(self,role,value):
		""""""
		if role == DML_PYQT.Qt.ItemDataRole.BackgroundRole:
			self._nuke_view.color = value
		else:
			super(DML_Nuke_View_Color_Table_Widget_Item, self).setData(role,value)
			
########################################################################
class DML_Nuke_View_Image_Name_Table_Widget_Item(DML_Nuke_View_Table_Widget_Item):
	""""""
	
	#----------------------------------------------------------------------
	def data(self,role):
		""""""
		if role == DML_PYQT.Qt.ItemDataRole.DisplayRole or role == DML_PYQT.Qt.ItemDataRole.EditRole:
			return self._nuke_view.image_name
		else:
			return super(DML_Nuke_View_Image_Name_Table_Widget_Item, self).data(role)
	#----------------------------------------------------------------------
	def setData(self,role,value):
		""""""
		if role == DML_PYQT.Qt.ItemDataRole.EditRole:
			self._nuke_view.image_name = value
		else:
			super(DML_Nuke_View_Image_Name_Table_Widget_Item, self).setData(role,value)
			
########################################################################
class DML_Nuke_Views_Table_Widget(DML_PYQT.QTableWidget):
	""""""
	def __init__(self,parent=None):
		"""Constructor"""
		super(DML_Nuke_Views_Table_Widget,self).__init__(parent=parent)
		self.cellDoubleClicked.connect(self.on_cellDoubleClicked)
		nuke.DML_NUKE_VIEWS_CALLBACK_SINGLES.View_Added.connect(self.on_Nuke_View_Removed)
		nuke.DML_NUKE_VIEWS_CALLBACK_SINGLES.View_Remove.connect(self.on_Nuke_View_Removed)
		nuke.DML_NUKE_VIEWS_CALLBACK_SINGLES.Root_Views_Knob_Chaged.connect(self._rebuild)
		self.setHorizontalHeaderLabels(["View Name","Color","Image Name"])
	#----------------------------------------------------------------------
	@DML_PYQT.Slot(object)
	def on_Nuke_View_Removed(self,nuke_view):
		""""""
		self._rebuild()
		#isinstance(nuke_view,NVSYSTM.Nuke_View)
		#rows = self.rowCount()
		#for row in range(rows):
			#item = self.item(row,0)
			#if item._nuke_view == nuke_view:
				#self.removeRow(row)
				#break
	#----------------------------------------------------------------------
	@DML_PYQT.Slot(object)
	def on_Nuke_View_Added(self,nuke_view):
		""""""
		self._rebuild()
		#isinstance(nuke_view,NVSYSTM.Nuke_View)
		#rows = self.rowCount()
		#for row in range(rows):
			#item = self.item(row,0)
			#if item._nuke_view == nuke_view:
				#self.removeRow(row)
				#break
	#----------------------------------------------------------------------
	def _rebuild(self):
		""""""
		self._nuke_views = nuke.DML_Nuke_View_System
		self.clear()
		self.setRowCount(len(self._nuke_views.views))
		for row,view in enumerate(self._nuke_views):
			self.setItem(row, 0, DML_Nuke_View_Name_Table_Widget_Item(view))
			item = DML_Nuke_View_Color_Table_Widget_Item(view)
			item.setFlags(DML_PYQT.Qt.ItemFlag.ItemIsSelectable|DML_PYQT.Qt.ItemFlag.ItemIsEnabled)
			self.setItem(row, 1, item)
			self.setItem(row, 2, DML_Nuke_View_Image_Name_Table_Widget_Item(view))
			self.resizeRowsToContents()
		self.setHorizontalHeaderLabels(["View Name","Color","Output Name"])
	@DML_PYQT.Slot(int,int)
	def on_cellDoubleClicked(self,row,column):
		if column == 1:
			item = self.item(row,column)
			new_color = DML_PYQT.QColorDialog.getColor(item._nuke_view.color)
			if not new_color == None:
				nuke.DML_NUKE_VIEWS_UPDATE_ACTIONS.skip_update = True
				for item in self.selectedItems():
					if item.column() == 1:
						item._nuke_view.color = new_color
				nuke.DML_NUKE_VIEWS_UPDATE_ACTIONS.skip_update = False
				nuke.DML_NUKE_VIEWS_UPDATE_ACTIONS.external_change = False
				self._nuke_views._update_Nuke_Views_Knob()
				nuke.DML_NUKE_VIEWS_UPDATE_ACTIONS.external_change = True
	#---------------------------------------------------------------------
	def move_Selected_Up(self):
		""""""
		current_index = self.currentIndex()
		if current_index.isValid():
			current_row = current_index.row()
			if current_row != 0:
				current_item = self.takeItem(current_row)
				self.insertItem(current_row-1,current_item)
				self.setCurrentItem(current_item)
				self.ItemMoved.emit()
	#----------------------------------------------------------------------
	def move_Selected_Down(self):
		""""""
		current_index = self.currentIndex()
		if current_index.isValid():
			current_row = current_index.row()
			if current_row != self.count():
				current_item = self.takeItem(current_row)
				self.insertItem(current_row+1,current_item)
				self.setCurrentItem(current_item)
				self.ItemMoved.emit()


		

Python_Custom_Widget_Knob.Default_Ui_Loader.registerCustomWidget(DML_Nuke_Views_Table_Widget)

########################################################################
class Nuke_Views_Widget_Knob(Python_Custom_Widget_Knob.External_UI_Base_Widget_Knob):
	_class_knob_name  = "dml_nuke_views"
	_class_label_name = ""
	_class_tab_name   = "AW_Nuke_Views"
	
	def __init__(self,node,parent=None):
		if not hasattr(nuke,"DML_NUKE_VIEWS_CALLBACK_SINGLES"):
			import DML_Tools.DML_Nuke.Gizmos_And_Tools.Nuke_Views_System
		Python_Custom_Widget_Knob.External_UI_Base_Widget_Knob.__init__(self,node,parent)
		self._root_views_colours_knob = self.nuke_root.knob("views_colours")
		self._root_views_button_knob = self.nuke_root.knob("views_button")
		if not "DML_nuke_views_system_use_image_name" in  self.nuke_root.knobs():
			self._use_image_name_knob = nuke.Boolean_Knob("DML_nuke_views_system_use_image_name")
			self._use_image_name_knob.setVisible(False)
			self.nuke_root.addKnob(self._use_image_name_knob)
		else:
			self._use_image_name_knob = self.nuke_root.knob("DML_nuke_views_system_use_image_name")
			
		self.CHB_Use_View_Colors.setChecked(self._root_views_colours_knob.value())
		self.CHB_Use_View_Buttons.setChecked(self._root_views_colours_knob.value())
		self.CHB_Use_Image_Name.setChecked(self._use_image_name_knob.value())
		
		if False:
			self.Add_Remove_Views_Widget = DML_PYQT.QWidget()
			self.BNT_Add_View = DML_PYQT.QPushButtDML_PYQT()
			self.BNT_Remove_View = DML_PYQT.QPushButton()
			self.TBLWDG_Views = DML_Nuke_Views_Table_Widget()
			self.Move_View_Placement_Widget = DML_PYQT.QWidget()
			self.BNT_Move_View_UP = DML_PYQT.QPushButton()
			self.BNT_Move_View_Down = DML_PYQT.QPushButton()
			self.View_Display_Options_Widget = DML_PYQT.QWidget()
			self.CHB_Use_View_Buttons = DML_PYQT.QCheckBox()
			self.CHB_Use_View_Colors = DML_PYQT.QCheckBox()
			self.CHB_Use_Image_Name  = DML_PYQT.QCheckBox()
			
		self.TBLWDG_Views = self.findChild(DML_PYQT.QTableWidget,"TBLWDG_Views")
		self.TBLWDG_Views.setHorizontalHeaderLabels(["View Name","Color","Image Name"])
		self.TBLWDG_Views._rebuild()
		DML_PYQT.QMetaObject.connectSlotsByName(self)
	#----------------------------------------------------------------------
	@property
	def nuke_root(self):
		""""""
		return nuke.root()
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_CHB_Use_Image_Name_clicked(self):
		""""""
		self._use_image_name_knob.setValue(self.CHB_Use_Image_Name.isChecked())
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_CHB_Use_View_Colors_clicked(self):
		""""""
		self._root_views_colours_knob.setValue(self.CHB_Use_View_Colors.isChecked())
	@DML_PYQT.Slot()
	#----------------------------------------------------------------------
	def on_CHB_Use_View_Buttons_clicked(self):
		""""""
		self._root_views_button_knob.setValue(self.CHB_Use_View_Buttons.isChecked())
		
	#----------------------------------------------------------------------
	def _get_ui_file(self):
		""""""
		return os.path.join(os.path.dirname(__file__), "Nuke_Views.ui")
	#----------------------------------------------------------------------
	def _rebuild(self,layer_order=[]):
		""""""
		pass
	
_old_nuke_showSettings = nuke.showSettings

def showSettings():
	if nuke.root().knob("dml_nuke_views") == None:
		Nuke_Views_Widget_Knob.add_Widget_Knob(nuke.root())
	_old_nuke_showSettings()
	
nuke.showSettings = showSettings
		