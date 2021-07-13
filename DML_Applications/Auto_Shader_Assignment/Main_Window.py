from __future__ import print_function
import logging
import os
import sys
os.sys.path.append(r"V:\aw_config\Git_Live_Code\Global_Systems")
_log_file_path = os.path.join(os.environ["Temp"],"Auto_Shader_Assingment_Debug_Log.txt")

try:
	if os.path.exists(_log_file_path):
		os.remove(_log_file_path)
except:
	pass

logging.basicConfig(filename=os.path.join(os.environ["Temp"],"Auto_Shader_Assingment_Debug_Log.txt"),
					level=logging.DEBUG,
					format='%(levelname)s - %(lineno)d - "%(message)s"')

logging.debug('Logger Started')


logging.debug('Importing DML_Tools.DML_PYQT')

try:
	import DML_Tools.DML_PYQT as PYQT
	logging.debug('DML_Tools.DML_PYQT Imported Successfully')
except:
	logging.warn('Failed To Import DML_Tools.DML_PYQT')
	
	logging.warn('Adding "V:\aw_config\Git_Live_Code\Global_Systems" to the system paths')
	
	os.sys.path.append(r"V:\aw_config\Git_Live_Code\Global_Systems")
	
	logging.debug('Retrying Import Of DML_Tools.DML_PYQT')
	
	try:
		import DML_Tools.DML_PYQT as PYQT
	except Exception as e:
		e.message
		logging.error('Failed To Import DML_Tools.DML_PYQT with error {}'.format(e.message))
		sys.exit()

GUI_Loader = PYQT.GUI.UI_Loader.GUI_Loader

import Data_Structures

try:
	logging.debug('Attempting To Import Maya')
	import maya.cmds as cmds
	cmds.about( version=True)
	_in_maya = True
	logging.debug('Import Successfully Maya is running')
except:
	logging.debug('Import Falid Running In Standalone Version')
	_in_maya = False
	
#----------------------------------------------------------------------
def get_Nissan_Material_Codes():
	""""""
	Nissan_Material_Codes = os.path.join(os.path.dirname(__file__),"Nissan_Material_Codes.csv")
	with open(Nissan_Material_Codes,"r") as f:
		data = f.read()
	return data.splitlines()
	

################ Maya Functions
#----------------------------------------------------------------------
def get_Shader_In_Namespace(nameSpace):
	""""""
	def flatten(x):
		result = []
		for el in x:
			if hasattr(el, "__iter__") and not isinstance(el, basestring):
				result.extend(flatten(el))
			else:
				result.append(el)
		return result
	if _in_maya:
		shader_names = sorted(list(set(flatten([shaders for shaders in [cmds.listConnections(sg+".surfaceShader") for sg in [sg for sg in cmds.ls(nameSpace+":*",typ="shadingEngine") if not sg.startswith("initial")]] if len(shaders) >= 1]))))
		return shader_names



def openFileName(parent,native=False,startFolder=None,filterExt="csv",title="Load File"):
	options = PYQT.QFileDialog.Options()
	if startFolder == None:
		startFolder == os.environ["USERPROFILE"]
	if not native:
		options |= PYQT.QFileDialog.DontUseNativeDialog
	fileName, filtr = PYQT.QFileDialog.getOpenFileName(parent,title,startFolder,"All Files (*);;CSV Files (*.{})".format(filterExt), "", options)
	if fileName:
		return fileName
	
def saveFileName(parent,native=False,startFolder=None,filterExt="csv",title="Save File"):
	options = PYQT.QFileDialog.Options()
	if startFolder == None:
		startFolder == os.environ["USERPROFILE"]
		
	if not native:
		options |= PYQT.QFileDialog.DontUseNativeDialog
		
	fileName, filtr = PYQT.QFileDialog.getSaveFileName(parent,title,startFolder,"Text Files (*.{})".format(filterExt), "", options)
	
	if fileName:
		fileName = os.path.splitext(fileName)[0]+".{}".format(filterExt)
		return fileName

class Delegate(PYQT.QStyledItemDelegate):
	def __init__(self, owner, model_data):
		super(Delegate,self).__init__(owner)
		self.model_data = model_data
		#for row in range(self.model_data.rowCount()):
			#item = self.model_data.item(row)
			#self.choices.append(item.text())
		#if not len(self.choices):
			#self.choices.append("None")
	#----------------------------------------------------------------------
	@property
	def choices(self):
		""""""
		choices = []
		for row in range(self.model_data.rowCount()):
			item = self.model_data.item(row)
			choices.append(item.text())
		return choices
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
		if len(self.choices):
			num = self.choices.index(value)
			editor.setCurrentIndex(num)
			if not self._first_run:
				if not self._current_editor_value == editor.itemText(num):
					#print("Active Value Has Been Changed To {}".format(editor.itemText(num)))
					self._current_editor_value = editor.itemText(num)
			else:
				self._first_run = False
				self._current_editor_value = editor.itemText(num)
				self._old_editor_value = editor.itemText(num)

	def setModelData(self, editor, model, index):
		if len(self.choices):
			value = editor.currentText()
			model.setData(index, value, PYQT.Qt.EditRole)
			if self._old_editor_value != self._current_editor_value:
				self.model_data.Update_Association_Data(self._old_editor_value,self._current_editor_value,index.sibling(index.row(),1).data(PYQT.Qt.DisplayRole))
		else:
			model.setData(index, "None", PYQT.Qt.EditRole)
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
		self._last_loaded_file_path = None
		self._loaded_names = []
	#----------------------------------------------------------------------
	def setupTable(self,model_data):
		""""""
		#self.setSortingEnabled(True)
		#nissan_material_codes = get_Nissan_Material_Codes()
		#self.setRowCount(len(nissan_material_codes))
		self.setItemDelegateForColumn(0,Delegate(self, model_data))
		self.setColumnWidth(0,400)
	#----------------------------------------------------------------------
	def _rebuild_Name_List(self):
		""""""
		if len(self._loaded_names):
			for row in range(self.rowCount()):
				self.removeRow(0)
			#self.setRowCount(len(self._loaded_names))
			for index,item in enumerate(self._loaded_names):
				self.Add_Name(item)	
	#----------------------------------------------------------------------
	def Load_Names_Files(self):
		""""""
		file_path = openFileName(self, native=False, startFolder=self._last_loaded_file_path, filterExt="txt")
		
		if file_path:
			if not os.path.exists(file_path):
				raise OSError("The file location for this This Name List does not exist")
		
			with open(file_path,"r") as f:
				data = f.read()
			
			self._last_loaded_file_path = file_path
			
			self._loaded_names = data.splitlines()
			
			self._rebuild_Name_List()
	#----------------------------------------------------------------------
	def Build_Names_From_List(self,names=[]):
		""""""
		if len(names):
			self._loaded_names = names
			self._rebuild_Name_List()
				
	#----------------------------------------------------------------------
	def Add_Name(self,name):
		""""""
		current_row_count = self.rowCount()
		self.setRowCount(current_row_count+1)
		tableitem = PYQT.QTableWidgetItem(name)
		self.setItem(current_row_count,1,tableitem)
		lookup = self.window()._model_data.Find_Key_Name_For_Association(name)
		try:
			tableitem = PYQT.QTableWidgetItem(lookup.data())
		except:
			tableitem = PYQT.QTableWidgetItem("None")
		self.setItem(current_row_count,0,tableitem)
		if not name in self._loaded_names:
			self._loaded_names.append(name)
		
	#----------------------------------------------------------------------
	def Remove_Selected_Names(self):
		""""""
		selected_indexes = self.selectedIndexes()
		for index in reversed(selected_indexes):
			self._loaded_names.remove(index.data())
			self.removeRow(index.row())
	#----------------------------------------------------------------------
	def Save_Names_File(self,file_path=None):
		""""""
		if file_path == None:
			if self._last_loaded_file_path == None:
				file_path = saveFileName(self, native=False, startFolder=None, filterExt="txt")
			else:
				file_path = self._last_loaded_file_path
		
		if file_path is not None:
			try:
				with open(file_path,"w") as fp:
					fp.write("\n".join(self._loaded_names))
				self._last_loaded_file_path = file_path
				return True
			except:
				return False
					
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
		parentItem = self.invisibleRootItem()
		data = Data_Structures.Name_Associations_Data()
		data._data.Add_Name_Association("None")
		self._data = data
		for item in data.data:
			name_item = Name_Key_Standered_Item(item)
			parentItem.appendRow(name_item)
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
	def Get_Child_Items(self):
		""""""
		res = []
		for row in range(self.rowCount()):
			item = self.item(row)
			res.append(item)
		return res
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
			self.Association_Name_Space_Input = PYQT.QLineEdit()
			self.Names_Name_Space_Input = PYQT.QLineEdit()
			self.label_2 = PYQT.QLabel()
			self.label = PYQT.QLabel()
			self.Lookup_Name_Space_Scan_Button = PYQT.QPushButton()
			self.Association_Name_Space_Scan_Button = PYQT.QPushButton()
			self.Add_Name_Button = PYQT.QPushButton()
			self.New_Name_Input = PYQT.QLineEdit()
			self.Remove_Selected_Names_Button = PYQT.QPushButton()
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
			self.gridLayout = PYQT.QGridLayout()
			self.horizontalLayout = PYQT.QHBoxLayout()
			self.verticalLayout_4 = PYQT.QVBoxLayout()
			self.gridLayout_2 = PYQT.QGridLayout()
			self.horizontalLayout_5 = PYQT.QHBoxLayout()
			self.horizontalLayout_4 = PYQT.QHBoxLayout()
			self.verticalLayout_5 = PYQT.QVBoxLayout()
			self.action_Load_Associations = PYQT.QAction()
			self.action_Save_Associations = PYQT.QAction()
			self.action_Save_Associations_As = PYQT.QAction()
			self.actionAuto_Save = PYQT.QAction()
			self.action_Load_Names = PYQT.QAction()
			self.action_Save_Names = PYQT.QAction()
			self.action_Save_Names_As = PYQT.QAction()

########################################################################
class Name_Associations_Main_Window(_CODE_COMPLEATION_HELPER):
	""""""
	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		super(Name_Associations_Main_Window,self).__init__(parent=None)
		self._model_data = Name_Associations_Standered_Item_Model()
	#----------------------------------------------------------------------
	def _run_init(self):
		""""""
		self.Name_Tab_Association_treeView.setModel(self._model_data)
		self.Names_List_View.setModel(self._model_data)
		self.Associations_List_View.setModel(self._model_data)
		self.tableWidget.setupTable(self._model_data)
		self.Add_Key_Name_Button.clicked.connect(self.Add_Key_Name)
		self.Remove_Key_Name_Button.clicked.connect(self.Remove_Selected_Key_Names)
		self.Add_Association_Button.clicked.connect(self.Add_Name_Association)
		self.Remove_Association_Button.clicked.connect(self.Remove_Selected_Name_Associations)
		self.Add_Name_Button.clicked.connect(self.Add_Name)
		self.Remove_Selected_Names_Button.clicked.connect(self.tableWidget.Remove_Selected_Names)
		self.New_Name_Input.returnPressed.connect(self.Add_Name)
		self.New_Key_Name_Input.returnPressed.connect(self.Add_Key_Name)
		self.new_name_association_input.returnPressed.connect(self.Add_Name_Association)
		self.Lookup_Name_Space_Scan_Button.clicked.connect(self.Run_Name_Space_Scan_For_Names)
		self.Association_Name_Space_Scan_Button.clicked.connect(self.Run_Name_Space_Scan_For_Associations)
		try:
			self.action_Save_Associations.activated.connect(self.Save_File)
			self.action_Save_Associations_As.activated.connect(self.Save_File_As)
			self.action_Load_Associations.activated.connect(self.Load_File)		
			self.action_Load_Names.activated.connect(self.tableWidget.Load_Names_Files)
			self.action_Save_Names.activated.connect(self.Save_Names_File)
			self.action_Save_Names_As.activated.connect(self.Save_Names_File_As)
		except:
			self.action_Save_Associations.triggered.connect(self.Save_File)
			self.action_Save_Associations_As.triggered.connect(self.Save_File_As)
			self.action_Load_Associations.triggered.connect(self.Load_File)		
			self.action_Load_Names.triggered.connect(self.tableWidget.Load_Names_Files)
			self.action_Save_Names.triggered.connect(self.Save_Names_File)
			self.action_Save_Names_As.triggered.connect(self.Save_Names_File_As)
		
	#----------------------------------------------------------------------
	def Run_Name_Space_Scan_For_Names(self):
		""""""
		if _in_maya:
			text_val = self.Names_Name_Space_Input.text()
			if len(text_val):
				shaders_names = get_Shader_In_Namespace(text_val)
				shader_nice_names = [name.split(":")[-1] for name in shaders_names]
				self.tableWidget.Build_Names_From_List(shader_nice_names)
	#----------------------------------------------------------------------
	def Run_Name_Space_Scan_For_Associations(self):
		""""""
		if _in_maya:
			text_val = self.Association_Name_Space_Input.text()
			if len(text_val):
				shaders_names = get_Shader_In_Namespace(text_val)
				shader_nice_names = [name.split(":")[-1] for name in shaders_names]
				current_list_of_key_names = [item.text() for item in self._model_data.Get_Child_Items()]
				for nice_name in shader_nice_names:
					if not nice_name in current_list_of_key_names:
						self.Add_Key_Name(name=nice_name)
	#----------------------------------------------------------------------
	def Add_Name(self,name=None):
		""""""
		if name == None:
			name = self.New_Name_Input.text()
		names = name.split(",")
		for name in names:
			name = name.strip()
			item_search = self.tableWidget.findItems(name,PYQT.Qt.MatchExactly)
			if not len(item_search):
				self.tableWidget.Add_Name(name)
	#----------------------------------------------------------------------
	def Add_Key_Name(self,name=None):
		""""""
		if name == None:
			name = self.New_Key_Name_Input.text()
		names = name.split(",")
		for name in names:
			name = name.strip()
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
			
		names = name.split(",")
		for name in names:
			name = name.strip()
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
			#self.tableWidget.setupTable(self._model_data)
			self.tableWidget._rebuild_Name_List()
	
	#----------------------------------------------------------------------
	def Save_File(self):
		""""""
		if self._model_data._data.file_location == None:
			self.Save_File_As()
		else:
			success = self._model_data._data.Save()
			if not success:
				pass
	#----------------------------------------------------------------------
	def Save_File_As(self):
		""""""
		if self._model_data._data.file_location == None:
			file_path = saveFileName(self, native=False)
		else:
			file_path = saveFileName(self, native=False,startFolder=os.path.dirname(self._model_data._data.file_location))
		if file_path is not None:
			success = self._model_data._data.Save(fp=file_path)
			if not success:
				pass
	#----------------------------------------------------------------------
	def Save_Names_File(self):
		""""""
		self.tableWidget.Save_Names_File()
	#----------------------------------------------------------------------
	def Save_Names_File_As(self):
		""""""
		file_path = saveFileName(self, native=False,startFolder=os.path.dirname(self._model_data._data.file_location))
		if file_path:
			self.tableWidget.Save_Names_File(file_path=file_path)
			
GUI_Loader.registerCustomWidget(Name_Associations_Main_Window)


#----------------------------------------------------------------------
def show_Main_Window():
	""""""
	main_window_ui_file = "\\\\isln-smb\\aw_config\\Git_Live_Code\\Global_Systems\\DML_Tools\\DML_Applications\\Main_Window.ui" #os.path.join(os.path.dirname(__file__),"UI","Main_Window.ui")
	logging.debug('Loading Main Window UI File At Location {}'.format(main_window_ui_file))
	
	logging.debug('Building Main Window')
	try:
		wig = GUI_Loader.load_file(main_window_ui_file)
	except Exception as e:
		logging.error('Main Did Not Built')
		logging.error(e.message)
		sys.exit()
	logging.debug('Main Window Built')
	
	isinstance(wig,Name_Associations_Main_Window)
	logging.debug('running Main Window Post Creation Setup')
	wig._run_init()
	logging.debug('Post Creation Setup Ran Successfully')
	logging.debug('Showing Main Window')
	wig.show()
	logging.debug('Main Window Shown Successfully')

if __name__ == '__main__':
	import sys
	logging.debug('Starting QApplication Main Run Loop')
	try:
		app = PYQT.QApplication(sys.argv)
		#wig = GUI_Loader.load_file(os.path.join(os.path.dirname(__file__),"UI","Main_Window.ui"))
		#isinstance(wig,Name_Associations_Main_Window)
		#wig._run_init()
		#wig.show()
		logging.debug('Loading Main Window')
		show_Main_Window()
	except Exception as e:
		logging.error('Could Not Create Tool')
		logging.error(e.message)
		sys.exit()
	sys.exit(app.exec_())


