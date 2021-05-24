from __future__ import print_function
import DML_Tools.DML_PYQT as PYQT
GUI_Loader = PYQT.GUI.UI_Loader.GUI_Loader
import Data_Structures
import os


#----------------------------------------------------------------------
def get_Nissan_Material_Codes():
	""""""
	Nissan_Material_Codes = os.path.join(os.path.dirname(__file__),"Nissan_Material_Codes.csv")
	with open(Nissan_Material_Codes,"r") as f:
		data = f.read()
	return data.splitlines()
	





def openFileName(parent,native=False,startFolder=None):
	options = PYQT.QFileDialog.Options()
	if startFolder == None:
		startFolder == os.environ["USERPROFILE"]
	if not native:
		options |= PYQT.QFileDialog.DontUseNativeDialog
	fileName, filtr = PYQT.QFileDialog.getOpenFileName(parent,"QFileDialog.getOpenFileName()",startFolder,"All Files (*);;CSV Files (*.csv)", "", options)
	if fileName:
		return fileName
	
def saveFileName(parent,native=False,startFolder=None):
	options = PYQT.QFileDialog.Options()
	if startFolder == None:
		startFolder == os.environ["USERPROFILE"]
		
	if not native:
		options |= PYQT.QFileDialog.DontUseNativeDialog
		
	fileName, filtr = PYQT.QFileDialog.getSaveFileName(parent,"QFileDialog.getSaveFileName()",startFolder,"Text Files (*.csv)", "", options)
	
	if fileName:
		return fileName

class Delegate(PYQT.QStyledItemDelegate):
	def __init__(self, owner, model_data):
		super(Delegate,self).__init__(owner)
		self.model_data = model_data
		self.choices =[]
		for row in range(self.model_data.rowCount()):
			item = self.model_data.item(row)
			self.choices.append(item.text())
			
	def paint(self, painter, option, index):
		#if isinstance(self.parent(), PYQT.QAbstractItemView):
			#self.parent().openPersistentEditor(self.parent().itemFromIndex(index))
		super(Delegate, self).paint(painter, option, index)

	def createEditor(self, parent, option, index):
		self._first_run = True
		self._current_editor_value = None
		self._old_editor_value = None
		editor = Custom_Combox(parent=parent)
		editor.setModel(self.model_data)
		#editor.currentIndexChanged.connect(self.commit_editor)
		return editor

	def commit_editor(self):
		editor = self.sender()
		#self.commitData.emit(editor)
		editor

	def setEditorData(self, editor, index):
		value = index.data(PYQT.Qt.DisplayRole)
		num = self.choices.index(value)
		editor.setCurrentIndex(num)
		if not self._first_run:
			if not self._current_editor_value == editor.itemText(num):
				print("Active Value Has Been Changed To {}".format(editor.itemText(num)))
				self._current_editor_value = editor.itemText(num)
		else:
			self._first_run = False
			self._current_editor_value = editor.itemText(num)
			self._old_editor_value = editor.itemText(num)

	def setModelData(self, editor, model, index):
		value = editor.currentText()
		model.setData(index, value, PYQT.Qt.EditRole)
		if self._old_editor_value != self._current_editor_value:
			self.model_data.Update_Association_Data(self._old_editor_value,self._current_editor_value,index.sibling(index.row(),1).data(PYQT.Qt.DisplayRole))

	def updateEditorGeometry(self, editor, option, index):
		editor.setGeometry(option.rect)

########################################################################
class Custom_Combox(PYQT.QComboBox):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,parent=None):
		"""Constructor"""
		super(Custom_Combox,self).__init__(parent=parent)
		#self.currentIndexChanged.connect(self.onChanged)
		#self.activated.connect(self.do_activated)
		self._old_index = 0
		#self._options_visable = False
		
	#----------------------------------------------------------------------
	def onChanged(self,val):
		""""""
		print("Active Value Has Been Changed To {}".format(self.itemText(val)))
	##----------------------------------------------------------------------
	#def setCurrentIndex(self,index):
		#""""""
		#if self._options_visable:
			#if not self._old_index == index:
				#print("old index = {}, new index = {}".format(self._old_index,index))
				#self._old_index = index
		#super(Custom_Combox,self).setCurrentIndex(index)
	#----------------------------------------------------------------------
	def do_activated(self,index):
		""""""
		print("Active Value Has Been Changed To {}".format(self.itemText(index)))
	
########################################################################
class Custom_TableWidget(PYQT.QTableWidget):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,parent=None):
		"""Constructor"""
		super(Custom_TableWidget,self).__init__(parent=parent)
	#----------------------------------------------------------------------
	def setupTable(self,model_data):
		""""""
		self.setSortingEnabled(True)
		nissan_material_codes = get_Nissan_Material_Codes()
		self.setRowCount(len(nissan_material_codes))
		
		for index,item in enumerate(nissan_material_codes):
			tableitem = PYQT.QTableWidgetItem(item)
			tableitem.setFlags(PYQT.Qt.ItemFlag.ItemIsEnabled | PYQT.Qt.ItemFlag.ItemIsSelectable)
			self.setItem(index,1,tableitem)
			
			lookup = model_data.Find_Key_Name_For_Association(item)
			try:
				tableitem = PYQT.QTableWidgetItem(lookup.data())
			except:
				tableitem = PYQT.QTableWidgetItem("None")
				
			self.setItem(index,0,tableitem)
			
		self.setItemDelegateForColumn(0,Delegate(self, model_data))
		#self.sortByColumn(0,PYQT.Qt.SortOrder.AscendingOrder)
		
GUI_Loader.registerCustomWidget(Custom_TableWidget)

########################################################################
class Name_Association_Standered_Item(PYQT.QStandardItem):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,name):
		"""Constructor"""
		super(Name_Association_Standered_Item,self).__init__(name)
	#----------------------------------------------------------------------
	def data(self,role=PYQT.Qt.ItemDataRole.DisplayRole):
		""""""
		if role == PYQT.Qt.ItemDataRole.UserRole:
			return self
		else:
			return super(Name_Association_Standered_Item,self).data(role)
########################################################################
class Name_Key_Standered_Item(PYQT.QStandardItem):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,name_association):
		"""Constructor"""
		if not isinstance(name_association,Data_Structures.Name_Association):
			raise ValueError("name_association input be and instance of Data_Structures.Name_Association and a {} was found".format(type(name_association)))
		super(Name_Key_Standered_Item,self).__init__("")
		self._data = name_association
		for child in self._data:
			child_item = Name_Association_Standered_Item(child)
			self.appendRow(child_item)
		
	#----------------------------------------------------------------------
	def data(self,role=PYQT.Qt.ItemDataRole.DisplayRole):
		""""""
		if role == PYQT.Qt.ItemDataRole.UserRole:
			return self
		elif role in [PYQT.Qt.ItemDataRole.DisplayRole,PYQT.Qt.ItemDataRole.EditRole]:
			return self._data.name
		else:
			return super(Name_Key_Standered_Item,self).data(role)
	#----------------------------------------------------------------------
	def setData(self,value,role=PYQT.Qt.ItemDataRole.EditRole):
		""""""
		if role == PYQT.Qt.ItemDataRole.EditRole:
			self._data.name = value
		else:
			super(Name_Key_Standered_Item,self).setData(value,role)
			
########################################################################
class Name_Associations_Standered_Item_Model(PYQT.QStandardItemModel):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,rows=1, columns=1):
		"""Constructor"""
		super(Name_Associations_Standered_Item_Model,self).__init__()
		#parentItem = self.invisibleRootItem()
		#data = Data_Structures.Name_Associations_Data(file_location=r"D:\aw_config\Git_Live_Code\Global_Systems\DML_Tools\DML_Applications\Auto_Shader_Assignment\TestData.csv", label="Name Associations")
		#self._data = data
		#for item in data.data:
			#name_item = Name_Key_Standered_Item(item)
			#parentItem.appendRow(name_item)
	#----------------------------------------------------------------------
	def _rebuild(self,file_path):
		""""""
		self.clear()
		parentItem = self.invisibleRootItem()
		data = Data_Structures.Name_Associations_Data(file_location=file_path, label="Name Associations")
		self._data = data
		for item in data.data:
			name_item = Name_Key_Standered_Item(item)
			parentItem.appendRow(name_item)
	#----------------------------------------------------------------------
	def Find_Key_Name_For_Association(self,val):
		""""""
		for row in range(self.rowCount()):
			item = self.item(row)
			for child_row in range(item.rowCount()):
				child_item = item.child(child_row)
				if child_item.text() == val:
					return item
		return None
	#----------------------------------------------------------------------
	def Update_Association_Data(self,oldKeyName,newKeyName,association):
		""""""
		
		if oldKeyName != u'None':
			items = self.findItems(oldKeyName,PYQT.Qt.MatchExactly)
			if len(items):
				oldKeyItem = items[0]
				isinstance(oldKeyItem,Name_Key_Standered_Item)
				for child_row in range(oldKeyItem.rowCount()):
					child_item = oldKeyItem.child(child_row)
					if child_item.text() == association:
						oldKeyItem._data.Remove_Association(association)
						oldKeyItem.removeRow(child_item.row())
						
		if newKeyName != u'None':
			items = self.findItems(newKeyName,PYQT.Qt.MatchExactly)
			if len(items):
				newKeyItem = items[0]
				isinstance(newKeyItem,Name_Key_Standered_Item)
				newKeyItem.appendRow(Name_Association_Standered_Item(association))
				newKeyItem._data.Add_Association(association)
		self._data.Save()
					
########################################################################
class _CODE_COMPLEATION_HELPER(PYQT.QMainWindow):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,parent=None):
		''''''
		super(_CODE_COMPLEATION_HELPER,self).__init__(parent=parent)
		if False:
			self.Main_Window = Name_Associations_Main_Window()
			self.centralwidget = PYQT.QWidget()
			self.tabWidget = PYQT.QTabWidget()
			self.table_view_tab = PYQT.QWidget()
			self.label_2 = PYQT.QLabel()
			self.lineEdit = PYQT.QLineEdit()
			self.label = PYQT.QLabel()
			self.lineEdit_2 = PYQT.QLineEdit()
			self.tableWidget = Custom_TableWidget()
			self.list_view_tab = PYQT.QWidget()
			self.widget_4 = PYQT.QWidget()
			self.Association_Label_2 = PYQT.QLabel()
			self.Add_Association_Button = PYQT.QPushButton()
			self.new_name_association_input = PYQT.QLineEdit()
			self.Remove_Association_Button = PYQT.QPushButton()
			self.Associations_List_View = PYQT.QListView()
			self.widget_2 = PYQT.QWidget()
			self.Name_Label_2 = PYQT.QLabel()
			self.Add_Key_Name_Button = PYQT.QPushButton()
			self.New_Key_Name_Input = PYQT.QLineEdit()
			self.Remove_Key_Name_Button = PYQT.QPushButton()
			self.Names_List_View = PYQT.QListView()
			self.tab_3 = PYQT.QWidget()
			self.Name_Tab_Association_treeView = PYQT.QTreeView()
			self.menubar = PYQT.QMenuBar()
			self.menuFile = PYQT.QMenu()
			self.menuOptions = PYQT.QMenu()
			self.statusbar = PYQT.QStatusBar()
			self.verticalLayout = PYQT.QVBoxLayout()
			self.verticalLayout_6 = PYQT.QVBoxLayout()
			self.gridLayout_3 = PYQT.QGridLayout()
			self.verticalLayout_4 = PYQT.QVBoxLayout()
			self.gridLayout_2 = PYQT.QGridLayout()
			self.horizontalLayout_5 = PYQT.QHBoxLayout()
			self.horizontalLayout_4 = PYQT.QHBoxLayout()
			self.verticalLayout_5 = PYQT.QVBoxLayout()
			self.actionLoad = PYQT.QAction()
			self.actionSave = PYQT.QAction()
			self.actionSave_As = PYQT.QAction()
			self.actionAuto_Save = PYQT.QAction()

########################################################################
class Name_Associations_Main_Window(_CODE_COMPLEATION_HELPER):
	""""""
	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		super(Name_Associations_Main_Window,self).__init__(parent=None)
		self._model_data = Name_Associations_Standered_Item_Model()
	#----------------------------------------------------------------------
	def _setup_TableWidget(self):
		""""""
		self.tableWidget.setupTable(self._model_data)
		#self.tableWidget.setItemDelegateForColumn(0,Delegate(self, model_data))
		#nissan_material_codes = get_Nissan_Material_Codes()
		#self.tableWidget.setRowCount(len(nissan_material_codes))
		#for index,item in enumerate(nissan_material_codes):
			#tableitem = PYQT.QTableWidgetItem(item)
			#self.tableWidget.setItem(index,1,tableitem)
			
			#combox = Custom_Combox(parent=self)
			#combox.setModel(self._model_data)
			#lookup = self._model_data.Find_Key_Name_For_Association(item)
			#try:
				#combox.setCurrentIndex(lookup.row())
			#except:
				#pass
			#self.tableWidget.setCellWidget(index,0,combox)
	#----------------------------------------------------------------------
	def _run_init(self):
		""""""
		self.Name_Tab_Association_treeView.setModel(self._model_data)
		self.Names_List_View.setModel(self._model_data)
		self.Associations_List_View.setModel(self._model_data)
		self._setup_TableWidget()
		self.Add_Key_Name_Button.clicked.connect(self.Add_Key_Name)
		self.Remove_Key_Name_Button.clicked.connect(self.Remove_Selected_Key_Names)
		self.Add_Association_Button.clicked.connect(self.Add_Name_Association)
		self.Remove_Association_Button.clicked.connect(self.Remove_Selected_Name_Associations)
		self.actionSave.activated.connect(self.Save_File)
		self.actionSave_As.activated.connect(self.Save_File_As)
		self.actionLoad.activated.connect(self.Load_File)
	#----------------------------------------------------------------------
	def Add_Key_Name(self,name=None):
		""""""
		if name == None:
			name = self.New_Key_Name_Input.text()
		if not name in self._model_data._data._data and len(name):
			key_name_association = self._model_data._data.Add_Name_Association(name, associations=[])
			self._model_data.invisibleRootItem().appendRow(Name_Key_Standered_Item(key_name_association))
	#----------------------------------------------------------------------
	def Remove_Selected_Key_Names(self):
		""""""
		if len(self.Names_List_View.selectedIndexes()):
			for index in reversed(self.Names_List_View.selectedIndexes()):
				self._model_data._data.Remove_Name_Association(index.data())
				lookup = self._model_data.findItems(index.data(),PYQT.Qt.MatchExactly)
				if len(lookup):
					for item in lookup:
						self._model_data.invisibleRootItem().removeRow(item.row())
	#----------------------------------------------------------------------
	def Add_Name_Association(self,name=None):
		""""""
		if name == None:
			name = self.new_name_association_input.text()
		if not name in self._model_data._data._data and len(name):
			selected_items = self.Names_List_View.selectedIndexes()
			if len(selected_items) == 1:
				selected_item = self._model_data.item(selected_items[0].row())
				isinstance(selected_item,Name_Key_Standered_Item)
				if not name in selected_item._data:
					selected_item._data.Add_Association(name)
					selected_item.appendRow(Name_Association_Standered_Item(name))
	#----------------------------------------------------------------------
	def Remove_Selected_Name_Associations(self):
		""""""
		selected_indices = self.Associations_List_View.selectedIndexes()
		if len(selected_indices):
			root_item = self.Associations_List_View.model().item(self.Associations_List_View.rootIndex().row()).data(32)
			selected_items = [root_item.child(item.row()) for item in selected_indices]
			for selected_item in reversed(selected_items):
				isinstance(selected_item,Name_Association_Standered_Item)
				root_item._data.Remove_Association(selected_item.text())
				root_item.removeRow(selected_item.row())
				
	#----------------------------------------------------------------------
	def Load_File(self):
		""""""
		file_path = openFileName(self,native=False, startFolder=None)
		if file_path is not None:
			self._model_data._rebuild(file_path)
			self._setup_TableWidget()
	#----------------------------------------------------------------------
	def Save_File(self):
		""""""
		success = self._model_data._data.Save()
		if not success:
			pass
	#----------------------------------------------------------------------
	def Save_File_As(self):
		""""""
		file_path = saveFileName(self, native=False,startFolder=os.path.dirname(self._model_data._data.file_location))
		if file_path is not None:
			success = self._model_data._data.Save(fp=file_path)
			if not success:
				pass

GUI_Loader.registerCustomWidget(Name_Associations_Main_Window)


if __name__ == '__main__':
	import sys
	app = PYQT.QApplication(sys.argv)
	wig = GUI_Loader.load_file(os.path.join(os.path.dirname(__file__),"UI","Main_Window.ui"))
	isinstance(wig,Name_Associations_Main_Window)
	wig._run_init()
	wig.show()
	sys.exit(app.exec_())


