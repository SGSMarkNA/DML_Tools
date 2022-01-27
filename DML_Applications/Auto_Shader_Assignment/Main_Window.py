
import logging
import os
import sys

_log_file_path = os.path.join(os.environ["Temp"],"Auto_Shader_Assingment_Debug_Log.txt")

try:
	if os.path.exists(_log_file_path):
		os.remove(_log_file_path)
except:
	pass

#logging.basicConfig(filename=os.path.join(os.environ["Temp"],"Auto_Shader_Assingment_Debug_Log.txt"),
#					level=logging.DEBUG,
#					format='%(levelname)s - %(lineno)d - "%(message)s"')

#logging.debug('Logger Started')


#logging.debug('Importing DML_Tools.DML_PYQT')

try:
	import DML_Tools.DML_PYQT as PYQT
	#logging.debug('DML_Tools.DML_PYQT Imported Successfully')
except:
	#logging.warn('Failed To Import DML_Tools.DML_PYQT')
	
	#logging.warn('Adding "V:\aw_config\Git_Live_Code\Global_Systems" to the system paths')
	
	os.sys.path.append(r"V:\aw_config\Git_Live_Code\Global_Systems")
	
	#logging.debug('Retrying Import Of DML_Tools.DML_PYQT')
	
	try:
		import DML_Tools.DML_PYQT as PYQT
	except Exception as e:
		e.message
		#logging.error('Failed To Import DML_Tools.DML_PYQT with error {}'.format(e.message))
		sys.exit()

#GUI_Loader = PYQT.GUI.UI_Loader.GUI_Loader

from . import Data_Structures

try:
	#logging.debug('Attempting To Import Maya')
	import maya.cmds as cmds
	cmds.about( version=True)
	_in_maya = True
	#logging.debug('Import Successfully Maya is running')
except:
	#logging.debug('Import Falid Running In Standalone Version')
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
			if hasattr(el, "__iter__") and not isinstance(el, str):
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
	fileName, filtr = PYQT.QFileDialog.getOpenFileName(parent,title,startFolder,"{} Files (*.{});;All Files (*)".format(filterExt.upper(),filterExt), "", options)
	if fileName:
		return fileName
	
def saveFileName(parent,native=False,startFolder=None,filterExt="csv",title="Save File"):
	options = PYQT.QFileDialog.Options()
	if startFolder == None:
		startFolder == os.environ["USERPROFILE"]
		
	if not native:
		options |= PYQT.QFileDialog.DontUseNativeDialog
		
	fileName, filtr = PYQT.QFileDialog.getSaveFileName(parent,title,startFolder,"{} Files (*.{});;All Files (*)".format(filterExt.upper(),filterExt), "", options)
	
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
		print(("Active Value Has Been Changed To {}".format(self.itemText(val))))
	#----------------------------------------------------------------------
	def do_activated(self,index):
		""""""
		print(("Active Value Has Been Changed To {}".format(self.itemText(index))))
	
########################################################################
class Custom_TableWidget(PYQT.QTableWidget):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,parent=None):
		"""Constructor"""
		super(Custom_TableWidget,self).__init__(parent=parent)
		self._last_loaded_file_path = None
		#self._loaded_names = []
	#----------------------------------------------------------------------
	def setupTable(self,model_data,name_list_data):
		""""""
		isinstance(name_list_data,Data_Structures.Name_List_Data)
		#self.setSortingEnabled(True)
		#nissan_material_codes = get_Nissan_Material_Codes()
		#self.setRowCount(len(nissan_material_codes))
		self._internal_data = name_list_data
		self.setItemDelegateForColumn(0,Delegate(self, model_data))
		self.setColumnWidth(0,400)
	#----------------------------------------------------------------------
	def _rebuild_Name_List(self):
		""""""
		if self.rowCount():
			for row in range(self.rowCount()):
				self.removeRow(0)
		for index,name in enumerate(self._internal_data.data):
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
	#----------------------------------------------------------------------
	def Build_Names_From_List(self,names=[]):
		""""""
		if len(names):
			for name in names:
				self.Add_Name(name)
	#----------------------------------------------------------------------
	def Add_Name(self,name):
		""""""
		if self._internal_data.Add_Name(name):
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
	#----------------------------------------------------------------------
	def Remove_Selected_Names(self):
		""""""
		selected_indexes = self.selectedIndexes()
		for index in reversed(selected_indexes):
			if self._internal_data.Remove_Name(index.data()):
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

		
#GUI_Loader.registerCustomWidget(Custom_TableWidget)
INTERNAL_ITEM_DATA = PYQT.Qt.ItemDataRole.UserRole+1


########################################################################
class _Standered_Item_Base(PYQT.QStandardItem):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,name=""):
		"""Constructor"""
		super(_Standered_Item_Base,self).__init__(name)
		self._data = None
	#----------------------------------------------------------------------
	def data(self,role=PYQT.Qt.ItemDataRole.DisplayRole):
		""""""
		if role == PYQT.Qt.ItemDataRole.UserRole:
			return self
		elif role == INTERNAL_ITEM_DATA:
			return self._data
		else:
			return super(_Standered_Item_Base,self).data(role)

########################################################################
class Name_Association_Standered_Item(_Standered_Item_Base):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,name):
		"""Constructor"""
		super(Name_Association_Standered_Item,self).__init__(name)
########################################################################
class Name_Key_Standered_Item(_Standered_Item_Base):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,name_association):
		"""Constructor"""
		if not isinstance(name_association,Data_Structures.Name_Association):
			raise ValueError("name_association input be and instance of Data_Structures.Name_Association and a {} was found".format(type(name_association)))
		super(Name_Key_Standered_Item,self).__init__()
		self._data = name_association
		for child in self._data:
			child_item = Name_Association_Standered_Item(child)
			self.appendRow(child_item)
		
	#----------------------------------------------------------------------
	def data(self,role=PYQT.Qt.ItemDataRole.DisplayRole):
		""""""
		if role in [PYQT.Qt.ItemDataRole.DisplayRole,PYQT.Qt.ItemDataRole.EditRole]:
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
	def __init__(self,name_associations_data):
		"""Constructor"""
		isinstance(name_associations_data,Data_Structures.Name_Associations_Data)
		super(Name_Associations_Standered_Item_Model,self).__init__()
		parentItem = self.invisibleRootItem()
		self._internal_data = name_associations_data
		for item in self._internal_data.data:
			name_item = Name_Key_Standered_Item(item)
			parentItem.appendRow(name_item)
	#----------------------------------------------------------------------
	def _rebuild(self):
		""""""
		self.clear()
		parentItem = self.invisibleRootItem()
		for item in self._internal_data.data:
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
		
		if oldKeyName != 'None':
			items = self.findItems(oldKeyName,PYQT.Qt.MatchExactly)
			
			if len(items):
				oldKeyItem = items[0]
				isinstance(oldKeyItem,Name_Key_Standered_Item)
				
				for child_row in range(oldKeyItem.rowCount()):
					child_item = oldKeyItem.child(child_row)
					
					if child_item.text() == association:
						oldKeyItem._data.Remove_Association(association)
						oldKeyItem.removeRow(child_item.row())
						break
					
		if newKeyName != 'None':
			items = self.findItems(newKeyName,PYQT.Qt.MatchExactly)
			if len(items):
				newKeyItem = items[0]
				isinstance(newKeyItem,Name_Key_Standered_Item)
				newKeyItem.appendRow(Name_Association_Standered_Item(association))
				newKeyItem._data.Add_Association(association)
	#----------------------------------------------------------------------
	def iterate_Names_With_Associations(self):
		""""""
		for row in range(self.rowCount()):
			item = self.item(row)
			data = item.data(role=INTERNAL_ITEM_DATA)
			if len(data.associations):
				yield data
	#----------------------------------------------------------------------
	def Add_Key_Name(self,name=None):
		""""""
		if name == None:
			name = self.parent().New_Key_Name_Input.text()
		names = name.split(",")
		for name in names:
			name = name.strip()
			key_name_association = self._internal_data.data.Add_Name_Association(name, associations=[])
			if key_name_association is not False:
				self.invisibleRootItem().appendRow(Name_Key_Standered_Item(key_name_association))
	#----------------------------------------------------------------------
	def Remove_Key_Name(self,name):
		""""""
		if self._internal_data.data.Remove_Name_Association(name):
			lookup = self.findItems(name,PYQT.Qt.MatchExactly)
			if len(lookup):
				for item in lookup:
					self.invisibleRootItem().removeRow(item.row())
	#----------------------------------------------------------------------
	def Add_Name_Association(self,association_name,key_name):
		""""""
		lookup = self.findItems(key_name,PYQT.Qt.MatchExactly)
		if len(lookup):
			key_item = lookup[0]
			isinstance(key_item,Name_Key_Standered_Item)
			association_names = association_name.split(",")
			for association_name in association_names:
				association_name = association_name.strip()
				if len(association_name):
					if key_item._data.Add_Association(association_name):
						key_item.appendRow(Name_Association_Standered_Item(association_name))
	#----------------------------------------------------------------------
	def Remove_Name_Associations(self,association_names,key_name):
		""""""
		lookup = self.findItems(key_name,PYQT.Qt.MatchExactly)
		if len(lookup):
			key_item = lookup[0]
			isinstance(key_item,Name_Key_Standered_Item)
			
			if len(association_names):
				for name in association_names:
					if key_item._data.Remove_Association(name):
						for row in range(key_item.rowCount()):
							child = key_item.child(row)
							if child.text() == name:
								key_item.removeRow(row)
								break

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
			self.centralwidget = PYQT.QWidget()
			self.tabWidget = PYQT.QTabWidget()
			self.table_view_tab = PYQT.QWidget()
			self.Name_Space_Scanning_Frame = PYQT.QFrame()
			self.Association_Name_Space_Input = PYQT.QLineEdit()
			self.Names_Name_Space_Input = PYQT.QLineEdit()
			self.label_2 = PYQT.QLabel()
			self.label = PYQT.QLabel()
			self.Lookup_Name_Space_Scan_Button = PYQT.QPushButton()
			self.Association_Name_Space_Scan_Button = PYQT.QPushButton()
			self.tableWidget = Custom_TableWidget()
			self.Add_Remove_Names_Frame = PYQT.QFrame()
			self.Add_Name_Button = PYQT.QPushButton()
			self.New_Name_Input = PYQT.QLineEdit()
			self.Remove_Selected_Names_Button = PYQT.QPushButton()
			self.Apply_Associations_Button = PYQT.QPushButton()
			self.list_view_tab = PYQT.QWidget()
			self.Add_Association_Widget = PYQT.QWidget()
			self.Add_Association_Button = PYQT.QPushButton()
			self.new_name_association_input = PYQT.QLineEdit()
			self.Remove_Association_Button = PYQT.QPushButton()
			self.Names_List_View = PYQT.QListView()
			self.Add_Name_Widget = PYQT.QWidget()
			self.Add_Key_Name_Button = PYQT.QPushButton()
			self.New_Key_Name_Input = PYQT.QLineEdit()
			self.Remove_Key_Name_Button = PYQT.QPushButton()
			self.Associations_List_View = PYQT.QListView()
			self.Name_Label_2 = PYQT.QLabel()
			self.Association_Label_2 = PYQT.QLabel()
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
			self.action_Load_Name_Assocations = PYQT.QAction()
			self.action_Save_Name_Assocations = PYQT.QAction()
			self.action_Save_Name_Assocations_As = PYQT.QAction()

########################################################################
class Name_Associations_Main_Window(_CODE_COMPLEATION_HELPER):
	""""""
	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		super(Name_Associations_Main_Window,self).__init__(parent=None)
		self._internal_data = Data_Structures.Name_Associations_Data_Location_Manager()
		self._model_data = Name_Associations_Standered_Item_Model(self._internal_data.name_associations)
	#----------------------------------------------------------------------
	def _run_init(self):
		""""""
		self._model_data.setParent(self)
		self.Name_Tab_Association_treeView.setModel(self._model_data)
		self.Names_List_View.setModel(self._model_data)
		self.Associations_List_View.setModel(self._model_data)
		self.tableWidget.setupTable(self._model_data,self._internal_data.name_list)
		self.Add_Key_Name_Button.clicked.connect(self.Add_Key_Name)
		self.Remove_Key_Name_Button.clicked.connect(self.Remove_Selected_Key_Names)
		self.Add_Association_Button.clicked.connect(self.Add_Name_Association)
		self.Remove_Association_Button.clicked.connect(self.Remove_Selected_Name_Associations)
		self.Add_Name_Button.clicked.connect(self.Add_Name)
		self.Remove_Selected_Names_Button.clicked.connect(self.tableWidget.Remove_Selected_Names)
		self.New_Name_Input.returnPressed.connect(self.Add_Name)
		self.New_Key_Name_Input.returnPressed.connect(self.Add_Key_Name)
		self.new_name_association_input.returnPressed.connect(self.Add_Name_Association)
		#self.Apply_Associations_Button.setHidden(True)
		self.Name_Space_Scanning_Frame.setHidden(True)
		self.Apply_Associations_Button.clicked.connect(self._run_Apply_Associations)
		try:
			self.action_Save_Associations.activated.connect(self.Save_Associations_File)
			self.action_Save_Associations_As.activated.connect(self.Save_Associations_File_As)
			self.action_Load_Associations.activated.connect(self.Load_Associations_File)		
			self.action_Load_Names.activated.connect(self.Load_Names_Files)
			self.action_Save_Names.activated.connect(self.Save_Names_File)
			self.action_Save_Names_As.activated.connect(self.Save_Names_File_As)
			self.action_Save_Name_Assocations.activated.connect(self.Save_Name_Associations_File)
			self.action_Save_Name_Assocations_As.activated.connect(self.Save_Name_Associations_File_As)
			self.action_Load_Name_Assocations.activated.connect(self.Load_Name_Associations_File)
		except:
			self.action_Save_Associations.triggered.connect(self.Save_Associations_File)
			self.action_Save_Associations_As.triggered.connect(self.Save_Associations_File_As)
			self.action_Load_Associations.triggered.connect(self.Load_Associations_File)		
			self.action_Load_Names.triggered.connect(self.Load_Names_Files)
			self.action_Save_Names.triggered.connect(self.Save_Names_File)
			self.action_Save_Names_As.triggered.connect(self.Save_Names_File_As)
			self.action_Save_Name_Assocations.triggered.connect(self.Save_Name_Associations_File)
			self.action_Save_Name_Assocations_As.triggered.connect(self.Save_Name_Associations_File_As)
			self.action_Load_Name_Assocations.triggered.connect(self.Load_Name_Associations_File)
	#----------------------------------------------------------------------
	def Add_Name(self,name=None):
		""""""
		if name == None:
			name = self.New_Name_Input.text()
		names = name.split(",")
		for name in names:
			self.tableWidget.Add_Name(name)
			#name = name.strip()
			#item_search = self.tableWidget.findItems(name,PYQT.Qt.MatchExactly)
			#if not len(item_search):
				#self.tableWidget.Add_Name(name)
	#----------------------------------------------------------------------
	def Add_Key_Name(self,name=None):
		""""""
		if name == None:
			name = self.New_Key_Name_Input.text()
		self._model_data.Add_Key_Name(name)
	#----------------------------------------------------------------------
	def Remove_Selected_Key_Names(self):
		""""""
		if len(self.Names_List_View.selectedIndexes()):
			for index in reversed(self.Names_List_View.selectedIndexes()):
				self._model_data.Remove_Key_Name(index.data())
	#----------------------------------------------------------------------
	def Add_Name_Association(self,name=None):
		""""""
		if name == None:
			name = self.new_name_association_input.text()
		
		selected_items = self.Names_List_View.selectedIndexes()
		if len(selected_items) == 1:
			key_name = selected_items[0].data()
			self._model_data.Add_Name_Association(name, key_name)
	#----------------------------------------------------------------------
	def Remove_Selected_Name_Associations(self):
		""""""
		selected_indices = self.Associations_List_View.selectedIndexes()
		if len(selected_indices):
			association_names = [index.data() for index in selected_indices]
			key_name = self.Associations_List_View.model().item(self.Associations_List_View.rootIndex().row()).data()
			self._model_data.Remove_Name_Associations(association_names, key_name)
	#----------------------------------------------------------------------
	def Load_Associations_File(self):
		""""""
		if self._internal_data.name_associations.file_location == None:
			file_path = openFileName(self,native=False,title="Load Associations")
		else:
			file_path = openFileName(self,native=False,startFolder=os.path.dirname(self._internal_data.name_associations.file_location),title="Load Associations")
		if file_path is not None:
			if not os.path.exists(file_path):
				raise OSError("The file location for this This Name List does not exist")
			self._internal_data.name_associations.Load(fp=file_path)
			self._model_data._rebuild()
			self.tableWidget._rebuild_Name_List()
	#----------------------------------------------------------------------
	def Save_Associations_File(self):
		""""""
		if self._internal_data.name_associations.file_location == None:
			self.Save_Associations_File_As()
		else:
			success = self._internal_data.name_associations.Save()
			if not success:
				pass
	#----------------------------------------------------------------------
	def Save_Associations_File_As(self):
		""""""
		if self._internal_data.name_associations.file_location == None:
			file_path = saveFileName(self, native=False,title="Save Associations")
		else:
			file_path = saveFileName(self, native=False,startFolder=os.path.dirname(self._internal_data.name_associations.file_location),title="Save Associations")
		if file_path is not None:
			success = self._internal_data.name_associations.Save(fp=file_path)
			if not success:
				pass
	#----------------------------------------------------------------------
	def Load_Names_Files(self):
		""""""
		if self._internal_data.name_list.file_location == None:
			file_path = openFileName(self,native=False,filterExt="txt",title="Load Names")
		else:
			file_path = openFileName(self,native=False,startFolder=os.path.dirname(self._internal_data.name_list.file_location),filterExt="txt",title="Load Names")
		
		if file_path:
			if not os.path.exists(file_path):
				raise OSError("The file location for this This Name List does not exist")
			self._internal_data.name_list.Load(fp=file_path)
			self.tableWidget._rebuild_Name_List()
	#----------------------------------------------------------------------
	def Save_Names_File(self):
		""""""
		if self._internal_data.name_list.file_location == None:
			self.Save_Names_File_As()
		else:
			self._internal_data.name_list.Save()
	#----------------------------------------------------------------------
	def Save_Names_File_As(self):
		""""""
		if self._internal_data.name_associations.file_location == None:
			file_path = saveFileName(self, native=False,filterExt="txt",title="Save Names")
		else:
			file_path = saveFileName(self, native=False,startFolder=os.path.dirname(self._internal_data.name_list.file_location),filterExt="txt",title="Save Names")
			
		if file_path:
			self._internal_data.name_list.Save(fp=file_path)
	#----------------------------------------------------------------------
	def Load_Name_Associations_File(self):
		""""""
		if self._internal_data._file_location == None:
			file_path = openFileName(self,native=False,filterExt="nadlm",title="Load Name Associations")
		else:
			file_path = openFileName(self,native=False,startFolder=os.path.dirname(self._internal_data._file_location),filterExt="nadlm",title="Load Name Associations")
		
		if file_path:
			if not os.path.exists(file_path):
				raise OSError("The file location for this This Name List does not exist")
			self._internal_data.Load(fp=file_path)
			self._model_data._rebuild()
			self.tableWidget._rebuild_Name_List()
	#----------------------------------------------------------------------
	def Save_Name_Associations_File(self):
		""""""
		if self._internal_data._file_location == None:
			self.Save_Name_Associations_File_As()
		else:
			self._internal_data.Save()
	#----------------------------------------------------------------------
	def Save_Name_Associations_File_As(self):
		""""""
		if self._internal_data._file_location == None:
			file_path = saveFileName(self, native=False,filterExt="nadlm",title="Save Name Associations")
		else:
			file_path = saveFileName(self, native=False,startFolder=os.path.dirname(self._internal_data._file_location),filterExt="nadlm",title="Save Name Associations")
			
		if file_path:
			self._internal_data.Save(fp=file_path)	
	#----------------------------------------------------------------------
	def _run_Apply_Associations(self):
		""""""
		self.Apply_Associations()
	#----------------------------------------------------------------------
	def Apply_Associations(self):
		""""""
		for item in self._model_data.iterate_Names_With_Associations():
			print(("{} = {}".format(item.name,",".join(item.associations))))


