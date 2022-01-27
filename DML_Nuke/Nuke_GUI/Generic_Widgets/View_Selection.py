
import os
from .. import Python_Custom_Widget_Knob
from ... import dml
import DML_Tools.DML_PYQT.BASE_CLASS_DEFINITIONS

DML_PYQT = DML_Tools.DML_PYQT
import nuke
Standered_Item_Data = DML_Tools.DML_PYQT.BASE_CLASS_DEFINITIONS.Standered_Item_Data
Internal_Item_Data = DML_Tools.DML_PYQT.BASE_CLASS_DEFINITIONS.Internal_Item_Data
Base_Model_Item = DML_Tools.DML_PYQT.BASE_CLASS_DEFINITIONS.Base_Model_Item
TreeModel = DML_Tools.DML_PYQT.BASE_CLASS_DEFINITIONS.TreeModel
Standered_List_View = DML_Tools.DML_PYQT.BASE_CLASS_DEFINITIONS.ABSTRACT_ITEM_MODEL_TYPES.DATA_VIEWS.List_Views.Standered_List_View


_use_Image_Name_As_Display_Name = False

#----------------------------------------------------------------------
def get_QColor(arg):
	if isinstance(arg,DML_PYQT.QColor):
		return arg
	elif isinstance(arg,(list,tuple)):
		if len(args)==3:
			r,g,b = arg[0], arg[1], arg[2]
			color = DML_PYQT.QColor(r,g,b)
		else:
			raise ValueError("bad input value")
	elif isinstance(arg,int):
		color = DML_PYQT.QColor.fromRgba(arg)
		return color
	elif isinstance(arg,str):
		if arg == "" or arg == '""':
			return DML_PYQT.QColor(DML_PYQT.Qt.GlobalColor.black)
		else:
			color = DML_PYQT.QColor(*Hex_to_RGB(arg))
		return color
	else:
		raise ValueError("Wrong Type Of Input")
#----------------------------------------------------------------------
def RGB_To_Hex(*args):
	if len(args)==3:
		r,g,b = args[0], args[1], args[2]
		hexCol = '#%02x%02x%02x' % (r,g,b)	
	elif len(args)==1:
		if isinstance(args[0],DML_PYQT.QColor):
			r,g,b = args[0].red(), args[0].green(), args[0].blue()
			hexCol = '#%02x%02x%02x' % (r,g,b)
		elif isinstance(args[0],int):
			color = DML_PYQT.QColor.fromRgb(args[0])
			r,g,b = color.red(), color.green(), color.blue()
			hexCol = '#%02x%02x%02x' % (r,g,b)	
	else:
		raise ValueError("Cound Not Convert {} to hex value".format(args))
	return hexCol

#----------------------------------------------------------------------
def Hex_to_RGB(value):
	value = value.lstrip('#')
	lv = len(value)
	return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))





########################################################################
class DML_Nuke_View_Model_Item(Internal_Item_Data):
	""""""
	def __init__(self,view,checked=False,tree_item=None):
		"""Constructor"""
		super(DML_Nuke_View_Model_Item, self).__init__(internal_data=view,editable=False,checkable=True,checked=checked,tree_item=tree_item)
		
	#----------------------------------------------------------------------
	def _fn_set_checked_value(self, value):
		super(DML_Nuke_View_Model_Item, self)._fn_set_checked_value(value)
		self.tree_item.model.update_Multi_View_Knob()
		self._update_Changed_Data(DML_PYQT.Qt.ItemDataRole.CheckStateRole)
		
	#----------------------------------------------------------------------
	def _fn_get_foreground_color_value(self):
		return self.internal_data.color
	#----------------------------------------------------------------------
	def _fn_get_display_name_value(self):
		if _use_Image_Name_As_Display_Name:
			return self.internal_data.image_name
		else:
			return self.internal_data.name
	
#----------------------------------------------------------------------
def get_Nuke_View_Model_Items(root_item=None,active_views=[]):
	""""""
	isinstance(root_item,Standered_Item_Data)
	res   =[]
	views = nuke.root().knob("views").toScript()
	views = views.replace("{","").replace("}","")
	views = views.splitlines()
	for line in views:
		items = line.split()
		name = items[0]
		color = items[1]
		if name in active_views:
			model_item = DML_Nuke_View_Model_Item(name, color,checked=True,tree_item=root_item)
		else:
			model_item = DML_Nuke_View_Model_Item(name, color,checked=False,tree_item=root_item)
		res.append(model_item)
	return res

########################################################################
class DML_Nuke_View_Selection_Item_Model(DML_Tools.DML_PYQT.BASE_CLASS_DEFINITIONS.ABSTRACT_ITEM_MODEL_TYPES.TreeModel):
	""""""
	def __init__(self,multiview_knob,parent=None, root_item=None):
		"""Constructor"""
		super(DML_Nuke_View_Selection_Item_Model, self).__init__(parent=parent, root_item=root_item, headers=["view"])
		isinstance(multiview_knob,nuke.MultiView_Knob)
		self._nuke_node = dml.to_DML_Node(nuke.thisNode())
		self._multi_view_knob = multiview_knob
		#self._rebuild()
	#----------------------------------------------------------------------
	def _rebuild(self):
		""""""
		if len(self.rootItem.childItems):
			self.rootItem.clear_Children()
		active_views = self._multi_view_knob.value().split()
		# iterate over each layer and create an item for it
		views = nuke.DML_Nuke_View_System.views
		for view in views:
			if view.name in active_views:
				item = Base_Model_Item(model=None, parent_item=self.rootItem, items=[DML_Nuke_View_Model_Item(view, checked=True)], column_count=1)
				#item = DML_Nuke_View_Model_Item(view, checked=True,tree_item=self.rootItem)
			else:
				item = Base_Model_Item(model=None, parent_item=self.rootItem, items=[DML_Nuke_View_Model_Item(view, checked=False)], column_count=1)
				#item = DML_Nuke_View_Model_Item(view, checked=False,tree_item=self.rootItem)
			#self.rootItem.appendChild(item)
		
		
	#----------------------------------------------------------------------
	def update_Multi_View_Knob(self):
		""""""
		active = []
		for item in self.rootItem.childItems:
			if item.column_items.get_item(0).checked:
				active.append(item.get_internal_Data(0).name)
		if not len(active):
			self._multi_view_knob.setValue(" ")
		else:
			self._multi_view_knob.setValue(" ".join(active))


########################################################################
class DML_Nuke_View_Selection_List_View(Standered_List_View):
	""""""
		
		
Python_Custom_Widget_Knob.Default_Ui_Loader.registerCustomWidget(DML_Nuke_View_Selection_List_View)
	

########################################################################
class Nuke_Views_Selector_UI(DML_PYQT.QWidget):
	def __init__(self,parent=None):
		DML_PYQT.QWidget.__init__(self,parent=parent)
		# sort the nuke nuke node that this QWidget is invavled with
		self._nuke_node = dml.to_DML_Node(nuke.thisNode())
		# check if the knob exists that will store the layer order used for persistent data 
		# in order to rebuild the model with the users last settings 
		if self._nuke_node.hasKnob("DML_Nuke_View_Selection"):
			# if so than just get and store it
			self._imbeded_data_View_Selection_knob = self._nuke_node.nuke_object.knob("DML_Nuke_View_Selection")
		else:
			# if not then create it
			self._imbeded_data_View_Selection_knob = nuke.MultiView_Knob("DML_Nuke_View_Selection","Views")
			# hide it so it does not get edited by the user acidently
			#self._imbeded_data_View_Selection_knob.setVisible(False)
			# add it to the node
			self._nuke_node.addKnob(self._imbeded_data_View_Selection_knob)
		
		# build a layout to hold the widget that gets created from ui file that get dinamicly built
		master_Layout = DML_PYQT.QVBoxLayout(self)
		master_Layout.setSpacing(0)
		master_Layout.setContentsMargins(0, 0, 0, 0)
		# read in create the ui file
		file_wig = Python_Custom_Widget_Knob.Default_Ui_Loader.load(os.path.join(os.path.dirname(__file__),"View_Selection.ui"),parent=self)
		# add the widget to the layout
		master_Layout.addWidget(file_wig)
		# iterate over all the children of the file widget
		for child in file_wig.findChildren(DML_PYQT.QObject):
			# get the objects name
			objectName = child.objectName()
			# make sure the object had a name
			if len(objectName):
				# check weather or not this widget has and attribute with that name allready
				if not hasattr(self,objectName):
					# if not than add a attribute to this object using the name of the widget object
					# and assign it to the child for easy access
					self.__dict__[objectName]=child		
		if False:
			self.Nuke_Views_Selector_Widget = DML_PYQT.QWidget()
			self.BNT_Set_To_Filtered        = DML_PYQT.QPushButton()
			self.nuke_view_list_view        = DML_Nuke_View_Selection_List_View()
			self.View_Filter                = DML_PYQT.QLineEdit()
			self.BNT_Toggle_Selected        = DML_PYQT.QPushButton()
			self.BNT_Disable_Selected       = DML_PYQT.QPushButton()
			self.BNT_Enable_Selected        = DML_PYQT.QPushButton()
			self.CHKB_Use_Image_Name        = DML_PYQT.QCheckBox()
			self.gridLayout                 = DML_PYQT.QGridLayout()
		
		self.CHKB_Use_Image_Name.setChecked(_use_Image_Name_As_Display_Name)
		DML_PYQT.QMetaObject.connectSlotsByName(self)
		self._model = DML_Nuke_View_Selection_Item_Model(self._imbeded_data_View_Selection_knob, parent=self)
		self._proxyModel = DML_Tools.DML_PYQT.BASE_CLASS_DEFINITIONS.Sort_Filter_Proxy_Model(parent=self)
		self._proxyModel.setSourceModel(self._model)
		self._proxyModel.setFilterCaseSensitivity(DML_PYQT.Qt.CaseInsensitive)
		self.nuke_view_list_view.setRootIndex(self._model.rootItem.index)
		self.nuke_view_list_view.setModel(self._proxyModel)
		if nuke.GUI:
			nuke.DML_NUKE_VIEWS_CALLBACK_SINGLES.Root_Views_Knob_Chaged.connect(self._model._rebuild)
		self._rebuild()
	#----------------------------------------------------------------------
	def showEvent(self,event):
		""""""
		self._model._rebuild()
		super(Nuke_Views_Selector_UI, self).showEvent(event)
	#----------------------------------------------------------------------
	@DML_PYQT.Slot(bool)
	def on_CHKB_Use_Image_Name_clicked(self,value):
		""""""
		global _use_Image_Name_As_Display_Name
		_use_Image_Name_As_Display_Name = value
		for child in self.nuke_view_list_view.Model.SourceModel.rootItem.all_childern:
			child.column_items.items[0]._update_Changed_Data(DML_PYQT.Qt.ItemDataRole.DisplayRole)
	#----------------------------------------------------------------------
	def _rebuild(self):
		""""""
		self.nuke_view_list_view = self.findChild(DML_PYQT.QListView,"nuke_view_list_view")
		self.CHKB_Use_Image_Name = self.findChild(DML_PYQT.QCheckBox,"CHKB_Use_Image_Name")
	#----------------------------------------------------------------------
	@DML_PYQT.Slot(str)
	def on_View_Filter_textChanged(self,val):
		if not len(val):
			val = "*"
		self._proxyModel.setFilterWildcard(val)
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_BNT_Set_To_Filtered_clicked(self):
		""""""
		rowcount = self._proxyModel.rowCount(DML_PYQT.QModelIndex())
		for child in self._model.rootItem.childItems:
			child.column_items.get_item(0).checked=False
		for i in range(rowcount):
			index = self._proxyModel.index(i, 0, DML_PYQT.QModelIndex())
			item = index.data(DML_PYQT.Qt.ItemDataRole.UserRole)
			item.checked=True
			self._proxyModel.dataChanged.emit(index, index)
		for child in self._model.rootItem.childItems:
			item = child.column_items.get_item(0)
			item._update_Changed_Data(DML_PYQT.Qt.ItemDataRole.CheckStateRole)
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_BNT_Enable_Selected_clicked(self):
		""""""
		for item in self.nuke_view_list_view.iterSelectedItems():
			item.checked = True
			proxy_index = self._proxyModel.mapFromSource(item.index)
			self._proxyModel.dataChanged.emit(proxy_index,proxy_index)
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_BNT_Disable_Selected_clicked(self):
		""""""
		for item in self.nuke_view_list_view.iterSelectedItems():
			item.checked = False
			proxy_index = self._proxyModel.mapFromSource(item.index)
			self._proxyModel.dataChanged.emit(proxy_index,proxy_index)
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_BNT_Toggle_Selected_clicked(self):
		""""""
		for item in self.nuke_view_list_view.iterSelectedItems():
			if item.checked:
				item.checked = False
			else:
				item.checked = True
			proxy_index = self._proxyModel.mapFromSource(item.index)
			self._proxyModel.dataChanged.emit(proxy_index,proxy_index)

Python_Custom_Widget_Knob.Default_Ui_Loader.registerCustomWidget(Nuke_Views_Selector_UI)

########################################################################
class Nuke_Views_Selection_Test_Widget_Knob(Python_Custom_Widget_Knob.External_UI_Base_Widget_Knob):
	_class_knob_name = "dml_nuke_views_selector"
	_class_label_name = ""
	_class_tab_name  = "Nuke_Views_Selector"
	
	def __init__(self,node,parent=None):
		Python_Custom_Widget_Knob.External_UI_Base_Widget_Knob.__init__(self,node,parent)
		if False:
			self.Nuke_Views_Selector_Widget = DML_PYQT.QWidget()
			self.BNT_Set_To_Filtered        = DML_PYQT.QPushButton()
			self.nuke_view_list_view        = DML_Nuke_View_Selection_List_View()
			self.View_Filter                = DML_PYQT.QLineEdit()
			self.BNT_This_Does_Nothing      = DML_PYQT.QPushButton()
			self.BNT_Disable_Selected       = DML_PYQT.QPushButton()
			self.BNT_Enable_Selected        = DML_PYQT.QPushButton()
			self.CHKB_Use_Image_Name        = DML_PYQT.QCheckBox()
			self.gridLayout                 = DML_PYQT.QGridLayout()
		self.CHKB_Use_Image_Name.setChecked(_use_Image_Name_As_Display_Name)
		self.CHKB_Use_Image_Name.clicked.connect(self.on_CHKB_Use_Image_Name_clicked)
		DML_PYQT.QMetaObject.connectSlotsByName(self)
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_CHKB_Use_Image_Name_clicked(self):
		""""""
		global _use_Image_Name_As_Display_Name
		_use_Image_Name_As_Display_Name = self.CHKB_Use_Image_Name.isChecked()
	#----------------------------------------------------------------------
	def _get_ui_file(self):
		""""""
		return os.path.join(os.path.dirname(__file__), "View_Selection_Test_Knob.ui")