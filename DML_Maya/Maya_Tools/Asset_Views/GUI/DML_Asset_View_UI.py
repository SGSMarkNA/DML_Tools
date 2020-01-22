
import os
import sys

import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMayaUI as OMUI
import maya.api.OpenMaya as OM
import base64
from .. import DML_Asset_View_Commands
from maya.app.general import mayaMixin

import DML_Tools.DML_PYQT.BASE_CLASS_DEFINITIONS.ABSTRACT_ITEM_MODEL_TYPES
ABSTRACT_ITEM_MODEL_TYPES = DML_Tools.DML_PYQT.BASE_CLASS_DEFINITIONS.ABSTRACT_ITEM_MODEL_TYPES

import DML_Tools.DML_PYQT
DML_PYQT = DML_Tools.DML_PYQT

import DML_Tools.Maya.DML_Maya
DML_Maya = DML_Tools.Maya.DML_Maya

from ..Custom_Nodes.DML_Asset_Views_Manager import Asset_Views_Manager

import ITEM_DATA_TYPES

from ..CallBack_Data_Storage import Callbacks_Collection_Storage

if False:
	import DML_PYQT
	import DML_PYQT.BASE_CLASS_DEFINITIONS.ABSTRACT_ITEM_MODEL_TYPES as ABSTRACT_ITEM_MODEL_TYPES

Item_Data_Roles = ABSTRACT_ITEM_MODEL_TYPES.Item_Data_Roles.Base_Item_Data_Roles

########################################################################
class Tree_Model(ABSTRACT_ITEM_MODEL_TYPES.TreeModel):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, parent=None, root_item=None, headers=[]):
		""""""
		super(Tree_Model,self).__init__(parent=parent, root_item=root_item, headers=headers)
		managers = [plg.node for plg in DML_Maya.dml.ls("*.dmlAssetViewsManager")]
		if len(managers):
			for manager in managers:
				ITEM_DATA_TYPES.View_State_Manager_Item.View_State_Manager_Data_Model_Item(manager, model=self, parent_item=self.rootItem)
		else:
			manager = DML_Asset_View_Commands.view_Manager_Create()
			ITEM_DATA_TYPES.View_State_Manager_Item.View_State_Manager_Data_Model_Item(manager, model=self, parent_item=self.rootItem)
	#----------------------------------------------------------------------
	def create_Child_Item(self,name):
		""""""
		manager = Asset_Views_Manager(name=name)
		child = ITEM_DATA_TYPES.View_State_Manager_Item.View_State_Manager_Data_Model_Item(manager, model=self, parent_item=self.rootItem)
		return child
		
########################################################################
class Standered_List_View(ABSTRACT_ITEM_MODEL_TYPES.Standered_List_View):
	""""""
		
########################################################################
class DML_Asset_View_Objects_List_View(Standered_List_View):
	""""""
	#----------------------------------------------------------------------
	def remove_Highlighted_Items(self):
		""""""
		selected_tree_items = self.selected_Tree_Items()
		root_tree_maya_node = self.Root_Tree_Item.get_internal_Data()
		maya_objects = [tree_item.get_internal_Data() for tree_item in selected_tree_items]
		self.Root_Tree_Item.removeChildren(selected_tree_items)
		root_tree_maya_node.remove_Objects(*maya_objects)
		
DML_PYQT.GUI.UI_Loader.GUI_Loader.registerCustomWidget(DML_Asset_View_Objects_List_View)
	
########################################################################
class DML_Asset_View_Collections_List_View(Standered_List_View):
	""""""

DML_PYQT.GUI.UI_Loader.GUI_Loader.registerCustomWidget(DML_Asset_View_Collections_List_View)
	
########################################################################
class DML_Asset_Views_List_View(Standered_List_View):
	""""""

DML_PYQT.GUI.UI_Loader.GUI_Loader.registerCustomWidget(DML_Asset_Views_List_View)		
	
########################################################################
class Asset_Views_Model_Editor_Widget(DML_PYQT.QWidget):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,parent=None):
		"""Constructor"""
		super(Asset_Views_Model_Editor_Widget,self).__init__(parent=parent)
		self._assigned_object_set = None
		if self.layout() == None:
			self._layout = DML_PYQT.QHBoxLayout()
			self._layout.setContentsMargins(0,0,0,0)
			self._layout.setObjectName('Asset_Views_Model_Editor_Widget_Main_Layout')
			self.setLayout(self._layout)
			self._build_Embeded_Model_Editor_Panel()
			self.model_editor_3dView = OMUI.M3dView.getM3dViewFromModelPanel(self.modeleditor.name)
			isinstance(self.model_editor_3dView,OMUI.M3dView)
			self.model_editor_main_Connection = DML_Maya.Maya_GUI.SelectionConnection(name="DML_Asset_Views_Model_Editor_MainConnection",object="defaultObjectSet",g=True,parent=self.model_editor_window.name)#parent=self.model_editor_window.name
			self.modeleditor.mainListConnection = self.model_editor_main_Connection
			
	#----------------------------------------------------------------------
	def _build_Embeded_Model_Editor_Panel(self):
		""""""
		self.model_editor_window  = DML_Maya.Maya_GUI.Window('DML_Asset_Views_Model_Editor_Maya_Window')
		self.panLayout            = DML_Maya.Maya_GUI.PaneLayout("DML_Asset_Views_Model_Editor_Maya_Panel_Layout")
		
		if not cmds.modelPanel("DML_Asset_Views_Model_Editor_Maya_Model_Panel",q=True,exists=True):
			self.modelPan = DML_Maya.Maya_GUI.ModelPanel("DML_Asset_Views_Model_Editor_Maya_Model_Panel")
			DML_Maya.Maya_GUI.Layout(self.modelPan.barLayout).visible = False
		else:
			cmds.modelPanel("DML_Asset_Views_Model_Editor_Maya_Model_Panel",edit=True, parent=self.panLayout.fullPathName)
			self.modelPan = DML_Maya.Maya_GUI.ModelPanel("DML_Asset_Views_Model_Editor_Maya_Model_Panel")
		
		DML_Maya.Maya_GUI.Layout(self.modelPan.barLayout).visible = False
		self.modeleditor = DML_Maya.Maya_GUI.ModelEditor(self.modelPan.name)
		mel.eval("toggleAutoLoad {} false;".format(self.modeleditor.name))
		mel.eval("setIsolateSelectAutoAdd {} false;".format(self.modeleditor.name))
		self.modeleditor.headsUpDisplay = False
		self.modeleditor.viewSelected = True
		for menu_item in sorted(list(set([gui_item for gui_item in cmds.lsUI( dumpWidgets=True,  ) if "DML_Asset_Views_Model_Editor_Maya_Model_Panel" in gui_item and "menu" in gui_item]))):
			try:
				if cmds.menu(menu_item,q=True, label=True) == 'Show':
					menu_item = DML_Maya.Maya_GUI.Menu(menu_item)
					mel.eval(menu_item.query(postMenuCommand=True))
					cmds.menu(menu_item.itemArray[0],e=True,  visible=False)
			except:
				pass
		self.modeleditor = DML_Maya.Maya_GUI.ModelEditor(self.modelPan.name)
		cmds.showWindow( self.model_editor_window)
		self.layout().addWidget(self.model_editor_window.widget)
		
	#----------------------------------------------------------------------
	def del_model_editor_window(self):
		""""""
		cmds.deleteUI(self.model_editor_window.name,window=True)

	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def refresh_Active_Object_Set(self):
		""""""
		self.model_editor_main_Connection.set_object(self._assigned_object_set)
	#----------------------------------------------------------------------
	@DML_PYQT.Slot(object)
	def set_Active_Object_Set(self,object_set):
		""""""
		self._assigned_object_set = object_set
		self.model_editor_main_Connection.set_object(self._assigned_object_set)
		
	#----------------------------------------------------------------------
	def get_Active_Object_Set(self):
		""""""
		return self._assigned_object_set
	
DML_PYQT.GUI.UI_Loader.GUI_Loader.registerCustomWidget(Asset_Views_Model_Editor_Widget)

########################################################################
class DML_Asset_Views_Main_Window_Widget(mayaMixin.MayaQWidgetBaseMixin,DML_PYQT.QWidget):
	#----------------------------------------------------------------------
	def __init__(self, parent=None):
		super(DML_Asset_Views_Main_Window_Widget, self).__init__(parent=parent)
		self._first_show = True
		if False:
			self.Model_Editor = Asset_Views_Model_Editor_Widget()
			isinstance(self.LV_Collections,DML_Asset_View_Collections_List_View)
			isinstance(self.LV_Views,DML_Asset_Views_List_View)
			isinstance(self.LV_Objects,DML_Asset_View_Objects_List_View)
			isinstance(self.CB_Asset_View_Managers,DML_PYQT.QComboBox)
			
			
			isinstance(self.PB_Add_Asset_View,DML_PYQT.QPushButton)
			isinstance(self.PB_Remove_Asset_View,DML_PYQT.QPushButton)
			
			isinstance(self.PB_Add_Asset_View_Collection,DML_PYQT.QPushButton)
			isinstance(self.PB_Remove_Asset_View_Collection,DML_PYQT.QPushButton)
			
			isinstance(self.PB_Add_Asset_Manager,DML_PYQT.QPushButton)
			isinstance(self.PB_Remove_Asset_Manager,DML_PYQT.QPushButton)
			
			isinstance(self.PB_Activate_View,DML_PYQT.QPushButton)
			isinstance(self.PB_Update_View,DML_PYQT.QPushButton)
			
			isinstance(self.PB_Remove_Hilighted,DML_PYQT.QPushButton)
			isinstance(self.PB_Add_Selected_To_View,DML_PYQT.QPushButton)
			isinstance(self.PB_Select_Hilighted,DML_PYQT.QPushButton)
			isinstance(self.PB_Frame_State_View_Objects,DML_PYQT.QPushButton)
			
			isinstance(self.RB_State_View_Changed_Do_Nothing,DML_PYQT.QRadioButton)
			isinstance(self.RB_State_View_Changed_Auto_View,DML_PYQT.QRadioButton)
			isinstance(self.RB_State_View_Changed_Auto_Frame,DML_PYQT.QRadioButton)
			
			isinstance(self.Auto_State_View_buttonGroup,DML_PYQT.QButtonGroup)
	##----------------------------------------------------------------------
	#def closeEvent(self,event):
		#""""""
		#super(DML_Asset_Views_Main_Window_Widget,self).closeEvent(event)
		#self.destroy()
	#----------------------------------------------------------------------
	def showEvent(self,event):
		""""""
		super(DML_Asset_Views_Main_Window_Widget,self).showEvent(event)
		
		self.LV_Collections               = self.findChild(DML_PYQT.QListView,"LV_Collections")
		self.LV_Views                     = self.findChild(DML_PYQT.QListView,"LV_Views")
		self.LV_Objects                   = self.findChild(DML_PYQT.QListView,"LV_Objects")
				
		self.CB_Asset_View_Managers       = self.findChild(DML_PYQT.QComboBox,"CB_Asset_View_Managers")
		
		self.PB_Add_Asset_View_Collection = self.findChild(DML_PYQT.QPushButton,"PB_Add_Asset_View_Collection")
		self.PB_Remove_Asset_View_Collection = self.findChild(DML_PYQT.QPushButton,"PB_Remove_Asset_View_Collection")
		
		self.PB_Add_Asset_View            = self.findChild(DML_PYQT.QPushButton,"PB_Add_Asset_View")
		self.PB_Remove_Asset_View         = self.findChild(DML_PYQT.QPushButton,"PB_Remove_Asset_View")
		
		self.PB_Add_Asset_Manager         = self.findChild(DML_PYQT.QPushButton,"PB_Add_Asset_Manager")
		self.PB_Remove_Asset_Manager      = self.findChild(DML_PYQT.QPushButton,"PB_Remove_Asset_Manager")
		
		self.PB_Activate_View             = self.findChild(DML_PYQT.QPushButton,"PB_Activate_View")
		self.PB_Update_View               = self.findChild(DML_PYQT.QPushButton,"PB_Update_View")
		self.PB_Remove_Hilighted          = self.findChild(DML_PYQT.QPushButton,"PB_Remove_Hilighted")
		self.PB_Add_Selected_To_View      = self.findChild(DML_PYQT.QPushButton,"PB_Add_Selected_To_View")
		self.PB_Select_Hilighted          = self.findChild(DML_PYQT.QPushButton,"PB_Select_Hilighted")
		self.PB_Remove_Selected_From_View = self.findChild(DML_PYQT.QPushButton,"PB_Remove_Selected_From_View")
		self.PB_Frame_State_View_Objects  = self.findChild(DML_PYQT.QPushButton,"PB_Frame_State_View_Objects")
		self.PB_State_View_Create_Thumbnail = self.findChild(DML_PYQT.QPushButton,"PB_State_View_Create_Thumbnail")
		
		self.RB_State_View_Changed_Auto_Frame = self.findChild(DML_PYQT.QRadioButton,"RB_State_View_Changed_Auto_Frame")
		self.RB_State_View_Changed_Auto_View  = self.findChild(DML_PYQT.QRadioButton,"RB_State_View_Changed_Auto_View")
		self.RB_State_View_Changed_Do_Nothing = self.findChild(DML_PYQT.QRadioButton,"RB_State_View_Changed_Do_Nothing")
		
		self.Auto_State_View_buttonGroup = self.findChild(DML_PYQT.QButtonGroup,"Auto_State_View_buttonGroup")
		
		if self._first_show:
			self._model = Tree_Model(parent=self)
			self._first_show = False
			self._run_setup()
	#----------------------------------------------------------------------
	def _run_setup(self):
		""""""
		self.CB_Asset_View_Managers.setModel(self._model)
		self.LV_Collections.setModel(self._model)
		self.LV_Views.setModel(self._model)
		self.LV_Objects.setModel(self._model)
		self.on_CB_Asset_View_Managers_currentIndexChanged(0)
		model_child = self._model.rootItem.child(0)
		maya_node = model_child.get_Maya_Node()
		self.Model_Editor.modeleditor.set_camera(maya_node.camera)
		
		#self.destroyed.connect(self.Model_Editor.del_model_editor_window)
		for child in self.findChildren(DML_PYQT.QObject):
			if hasattr(child,"_run_setup"):
				child._run_setup()
				if hasattr(child,"_first_show"):
					child._first_show = False
	#----------------------------------------------------------------------
	@DML_PYQT.Slot(DML_PYQT.QModelIndex,DML_PYQT.QModelIndex)
	def on_LV_Collections_DML_CURRENT_CHANGED(self,current,previous):
		""""""
		if not Callbacks_Collection_Storage._SCENE_IS_BEING_CLOSED:
			if current.isValid():
				current_tree_item = current.data((Item_Data_Roles.TREE_OBJECT))
				child_view_tree_item   = current_tree_item.childItems[0]
				self.LV_Views.setRootIndex(current)
				self.LV_Views.setCurrentIndex(child_view_tree_item.index)
	#----------------------------------------------------------------------
	@DML_PYQT.Slot(DML_PYQT.QModelIndex,DML_PYQT.QModelIndex)
	def on_LV_Views_DML_CURRENT_CHANGED(self,current,previous):
		""""""
		if not Callbacks_Collection_Storage._SCENE_IS_BEING_CLOSED:
			if current.isValid():
				item = current.data(Item_Data_Roles.TREE_OBJECT)
				maya_node  = item.get_Maya_Node()
				object_set = maya_node.object_set
				self.Model_Editor.set_Active_Object_Set(object_set)
				self.LV_Objects.setRootIndex(current)
				
				if self.Auto_State_View_buttonGroup.checkedButton() == self.RB_State_View_Changed_Auto_View:
					maya_node.apply_Camera_View(cmds.lookThru(self.Model_Editor.modeleditor.name,q=True))
						
				elif self.Auto_State_View_buttonGroup.checkedButton() == self.RB_State_View_Changed_Auto_Frame:
					self.on_PB_Frame_State_View_Objects_clicked()
				
	#----------------------------------------------------------------------
	@DML_PYQT.Slot(int)
	def on_CB_Asset_View_Managers_currentIndexChanged(self,value):
		""""""
		if not Callbacks_Collection_Storage._SCENE_IS_BEING_CLOSED:
			child = self._model.rootItem.child(value)
			self.LV_Collections.setRootIndex(child.child(0).index)
			try:
				self.LV_Views.setRootIndex(child.child(0).child(0).index)
				self.LV_Objects.setRootIndex(child.child(0).child(0).child(0).index)
				self.LV_Collections.setCurrentIndex(child.child(0).child(0).index)
			except:
				pass
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_PB_Add_Asset_Manager_clicked(self):
		""""""
		manager = DML_Asset_View_Commands.view_Manager_Create()
		ITEM_DATA_TYPES.View_State_Manager_Item.View_State_Manager_Data_Model_Item(manager, model=self._model, parent_item=self._model.rootItem)
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_PB_Remove_Asset_Manager_clicked(self):
		""""""
		child_item = self._model.rootItem.childItems[self.CB_Asset_View_Managers.currentIndex()]
		manager    =  child_item.get_Maya_Node()
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_PB_Add_Asset_View_Collection_clicked(self):
		""""""
		root_item = self.LV_Collections.RootIndex.data(Item_Data_Roles.TREE_OBJECT)
		manager = root_item.get_Maya_Node().plg_manager.source_node()
		DML_Asset_View_Commands.view_Collection_Create(manager)
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_PB_Remove_Asset_View_Collection_clicked(self):
		""""""
		selected_tree_items = self.LV_Collections.selected_Tree_Items()
		if len(selected_tree_items):
			item_to_delete    = selected_tree_items[0]
			item_to_switch_to = self.LV_Collections.Root_Tree_Item.child(0)
			
			if item_to_switch_to == item_to_delete:
				item_to_switch_to = self.LV_Collections.Root_Tree_Item.child(1)
				
			self.LV_Collections.setCurrentIndex(item_to_switch_to.index)
			DML_Asset_View_Commands.view_Collection_Delete(item_to_delete.get_Maya_Node())
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_PB_Add_Asset_View_clicked(self):
		""""""
		state_collection = self.LV_Views.RootIndex.data(Item_Data_Roles.TREE_OBJECT).get_Maya_Node()
		view_state = DML_Asset_View_Commands.view_State_Create(state_collection)
		view_state.update_Camera_View(camera=self.Model_Editor.modeleditor.camera)
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_PB_Remove_Asset_View_clicked(self):
		""""""
		selected = self.LV_Views.selected_Tree_Items()
		if len(selected):
			item_to_delete = selected[0]
			item_to_switch_to = self.LV_Views.Root_Tree_Item.child(0)
			if item_to_switch_to == item_to_delete:
				item_to_switch_to = self.LV_Views.Root_Tree_Item.childItems
			self.LV_Views.setCurrentIndex(item_to_switch_to.index)
			DML_Asset_View_Commands.view_State_Delete(item_to_delete.get_Maya_Node())
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_PB_Add_Selected_To_View_clicked(self):
		""""""
		root_item = self.LV_Objects.rootIndex().data(Item_Data_Roles.TREE_OBJECT)
		root_node = root_item.get_Maya_Node()
		DML_Asset_View_Commands.view_State_Add_Objects(root_node)
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_PB_Remove_Hilighted_clicked(self):
		""""""
		pass
		#self.LV_Objects.remove_Highlighted_Items()
		#object_set = self.LV_Objects.RootIndex.data(Item_Data_Roles.TREE_OBJECT).get_Maya_Node().object_set
		#self.Model_Editor.model_editor_main_Connection.set_object(object_set)
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_PB_Remove_Selected_From_View_clicked(self):
		""""""
		root_item = self.LV_Objects.rootIndex().data(Item_Data_Roles.TREE_OBJECT)
		root_node = root_item.get_Maya_Node()
		DML_Asset_View_Commands.view_State_Remove_Objects(root_node)
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_PB_Frame_State_View_Objects_clicked(self):
		""""""
		cmds.viewFit(cmds.lookThru(self.Model_Editor.modeleditor.name,q=True),animate=True,panel=self.Model_Editor.modeleditor.name)
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_PB_Activate_View_clicked(self):
		""""""
		selected_items = self.LV_Views.selected_Items()
		if len(selected_items):
			maya_node = selected_items[0].internal_data
			cmds.setFocus("DML_Asset_Views_Model_Editor_Maya_Model_Panel")
			maya_node.apply_Camera_View(self.Model_Editor.modeleditor.camera)
			#cmds.lookThru(self.Model_Editor.modeleditor.name,q=True)
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_PB_Update_View_clicked(self):
		""""""
		selected_items = self.LV_Views.selected_Items()
		if len(selected_items):
			maya_node = selected_items[0].internal_data
			maya_node.update_Camera_View(cmds.lookThru(self.Model_Editor.modeleditor.name,q=True))
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_PB_State_View_Create_Thumbnail_clicked(self):
		""""""
		cmds.refresh(f=True, currentView=True)
		self.Model_Editor.refresh_Active_Object_Set()
		icon_image = OM.MImage().create(64, 64, channels=4, type=OM.MImage.kFloat)
		editor_3dView = OMUI.M3dView.getM3dViewFromModelEditor(self.Model_Editor.modeleditor.name)
		editor_3dView.readColorBuffer(icon_image)
		image_path = os.path.join(os.environ['TEMP'],"asset_views_temp_icon.png")
		icon_image.writeToFile(image_path, outputFormat="png")
		with file(image_path) as f:
			f_data = f.read()
			incoded_data = base64.b64encode(f_data)
		
		decoded_data = base64.b64decode(incoded_data)
		
		pix = DML_PYQT.QPixmap()
		pix.loadFromData(decoded_data)
		pix.scaledToHeight(32)
		icon = DML_PYQT.QIcon(pix)
		cur = self.LV_Views.currentItem()
		
		cur.tree_item.setData(True,0,role=cur.ID_ROLE.ICON_VISABLE)
		
		cur.tree_item.setData(icon,role=cur.ID_ROLE.ICON_COLOR)
		maya_node = cur.tree_item.get_Maya_Node()
		with DML_Maya.MayaSkipUndoChunk():
			maya_node.plug_thumbnail_icon.value = incoded_data

DML_PYQT.GUI.UI_Loader.GUI_Loader.registerCustomWidget(DML_Asset_Views_Main_Window_Widget)

_Asset_Views_UI_Widget = None

#----------------------------------------------------------------------
def remove_GUI():
	""""""
	global _Asset_Views_UI_Widget, _Before_Scene_Open, _Before_Scene_new, _After_Scene_Open, _After_Scene_new
	#cmds.scriptJob( kill=_quitApplication_job_id, force=True)
	del _Before_Scene_Open
	del _Before_Scene_new
	Callbacks_Collection_Storage.clear_Per_Node_Callbacks()
	Callbacks_Collection_Storage.clear_Scene_Callback_Ids()
	if cmds.lsUI( dumpWidgets=True).count("DML_Asset_Views"):
		cmds.deleteUI("DML_Asset_Views",window=True)
	try:
		_Asset_Views_UI_Widget.destroy()
	except:
		pass
	_Asset_Views_UI_Widget = None

#----------------------------------------------------------------------
def On_Before_Scene_New_And_Before_Scene_Open(client_data):
	""""""
	global _Asset_Views_UI_Widget, _Before_Scene_Open, _Before_Scene_new, _After_Scene_Open, _After_Scene_new
	
	Callbacks_Collection_Storage._SCENE_IS_BEING_CLOSED = True
	_After_Scene_new       = DML_Maya.API_Callback_Builders.create_Scene_After_New_Message_Callback(On_After_Scene_New)
	_After_Scene_Open      = DML_Maya.API_Callback_Builders.create_Scene_After_Open_Message_Callback(On_After_Scene_Open)
	remove_GUI()
#----------------------------------------------------------------------
def On_After_Scene_New(client_data):
	""""""
	global _Asset_Views_UI_Widget, _Before_Scene_Open, _Before_Scene_new, _After_Scene_Open, _After_Scene_new
	Callbacks_Collection_Storage._SCENE_IS_BEING_CLOSED = False
	del _After_Scene_Open
	del _After_Scene_new

#----------------------------------------------------------------------
def On_After_Scene_Open(client_data):
	""""""
	global _Asset_Views_UI_Widget, _Before_Scene_Open, _Before_Scene_new, _After_Scene_Open, _After_Scene_new
	Callbacks_Collection_Storage._SCENE_IS_BEING_CLOSED = False
	del _After_Scene_Open
	del _After_Scene_new
	if len(DML_Asset_View_Commands.list_View_Managers()):
		build_GUI()
		
#----------------------------------------------------------------------
def quitApplication_script_job_callback():
	""""""
	remove_GUI()

#----------------------------------------------------------------------
def build_GUI():
	""""""
	global _Asset_Views_UI_Widget, _Before_Scene_Open, _Before_Scene_new, _After_Scene_Open, _After_Scene_new
	if _Asset_Views_UI_Widget is not None:
		On_Before_Scene_New_And_Before_Scene_Open()
	_Before_Scene_new       = DML_Maya.API_Callback_Builders.create_Scene_Before_New_Message_Callback(On_Before_Scene_New_And_Before_Scene_Open)
	_Before_Scene_Open      = DML_Maya.API_Callback_Builders.create_Scene_Before_Open_Message_Callback(On_Before_Scene_New_And_Before_Scene_Open)
	folder = os.path.dirname(__file__)
	ui_file = os.path.join(folder,"UI","DML_Asset_Views.ui")
	_Asset_Views_UI_Widget = DML_PYQT.GUI.UI_Loader.GUI_Loader.load_file(ui_file)
	_Asset_Views_UI_Widget.show()
	#_After_Scene_new       = DML_Maya.API_Callback_Builders.create_Scene_After_New_Message_Callback(On_After_Scene_New_And_After_Scene_Open)
	#_After_Scene_Open      = DML_Maya.API_Callback_Builders.create_Scene_After_Open_Message_Callback(On_After_Scene_New_And_After_Scene_Open)
	#cmds.scriptJob(runOnce=True, event= ["deleteAll",deleteAll_script_job_callback])
	#_quitApplication_job_id = cmds.scriptJob(runOnce=True, event= ["quitApplication",remove_GUI])
	DML_PYQT.QMetaObject.connectSlotsByName(_Asset_Views_UI_Widget)
	return _Asset_Views_UI_Widget