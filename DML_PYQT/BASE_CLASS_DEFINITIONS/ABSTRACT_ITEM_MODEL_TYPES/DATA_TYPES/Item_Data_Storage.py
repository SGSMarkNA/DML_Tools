import os
from .... import QT
Constants = QT.Constants
from ..Item_Data_Roles import Base_Item_Data_Roles
from ...QT_SUBCLASS import QComboBox,QItemDelegate
if False:
	from .. import DATA_TYPES

#----------------------------------------------------------------------
def is_Convertable_To_QColor(val):
	""""""
	if isinstance(val, (QT.QColor, QT.Qt.GlobalColor)):
		return True
	elif isinstance(val, (tuple, list)) and len(val) == 4 and all([isinstance(i, int) for i in val]):
		return True
	return False
#----------------------------------------------------------------------
def convert_To_QColor(val):
	""""""
	if not is_Convertable_To_QColor(val):
		raise ValueError("input is cannot be converted to a QColor")
	else:
		if isinstance(val, QT.QColor):
			return val
		elif isinstance(val, QT.Qt.GlobalColor):
			return QT.QColor(val)
		else:
			return QT.QColor(*val)
#----------------------------------------------------------------------
def create_Item_Icon(value):
	if isinstance(value, str):
		if value.startswith(":"):
			pixmap = QT.QPixmap(value)
			return QT.QIcon(pixmap)
	pixmap = QT.QPixmap(16, 16)
	painter = QT.QPainter(pixmap)
	painter.setPen(QT.Qt.NoPen)
	#painter.fillRect(QT.QRect(0, 0, 16, 16), color)
	#painter.fillRect(QT.QRect(0, 10, 20, 10), QT.Qt.GlobalColor.green)
	painter.end()
	return QT.QIcon(pixmap)
# ======================================================================
# DATA MODEL STANDERD ITEMS TYPES
# ----------------------------------------------------------------------
# Synopsis:
#     Each Items Constains All The Information Needed To Display Itself
#     In A Column for View such as
#     font size, font color, display name ect.
# ======================================================================

########################################################################
class DATA_DEFAULT_VALUES:
	""""""
	class FONT:
		family          = "Arial"
		pointSize       = 8
		weight          = Constants.Font.Weight.Normal
		capitalization  = Constants.Font.Capitalization.MixedCase
	class DISPLAY:
		background_color = QT.QColor(Constants.Colors.TRANSPARENT)
		foreground_color = QT.QColor(Constants.Colors.BLACK)
		icon_color       = QT.QColor(Constants.Colors.RED)
		brush            = QT.QBrush(Constants.Colors.RED)
		alignment_V      = Constants.AlignmentFlag.Vertical.Center
		alignment_H      = Constants.AlignmentFlag.Horizontal.Justify
	class BRUSH:
		_brush_val = None
		@classmethod
		def value(cls):
			if cls._brush_val is None:
				cls._brush_val = QT.QBrush(Constants.Colors.RED)
			return cls._brush_val
	@classmethod
	def update_Font(cls):
		cls.font = QT.QFont(cls.FONT.family, cls.FONT.pointSize)
		cls.font.setCapitalization(cls.FONT.capitalization)
		cls.font.setWeight(cls.FONT.weight)

	font             = QT.QFont(FONT.family, FONT.pointSize)
	font.setCapitalization(FONT.capitalization)
	font.setWeight(FONT.weight)
	icon             = None

########################################################################
class Item_Data_Delegate(QT.QItemDelegate):
	#----------------------------------------------------------------------
	def createEditor(self, parent, option, index):
		editor = index.data(Base_Item_Data_Roles.INTERNAL_EDITOR)
		if not editor == None:
			return editor.createEditor(parent=parent,index=index)
		else:
			return super(Item_Data_Delegate,self).createEditor(parent, option, index)
	#----------------------------------------------------------------------
	def setEditorData(self, editor, index):
		item_editor = index.data(Base_Item_Data_Roles.INTERNAL_EDITOR)
		if not item_editor == None:
			return item_editor.setEditorData()
		else:
			return super(Item_Data_Delegate,self).setEditorData(editor, index)
	#----------------------------------------------------------------------
	def setModelData(self, editor, model, index):
		item_editor = index.data(Base_Item_Data_Roles.INTERNAL_EDITOR)
		if not item_editor == None:
			return item_editor.setModelData()
		else:
			return super(Item_Data_Delegate,self).setModelData(editor, model, index)
	#----------------------------------------------------------------------
	def paint(self, painter, option, index):
		isinstance(painter,QT.QPainter)
		isinstance(option,QT.QStyleOptionViewItem)
		isinstance(index,QT.QModelIndex)
		super(Item_Data_Delegate, self).paint(painter, option, index)
	#----------------------------------------------------------------------
	def drawDisplay(self, painter, option, rect, text):
		isinstance(painter,QT.QPainter)
		isinstance(option,QT.QStyleOptionViewItem)
		isinstance(rect,QT.QRect)
		super(Item_Data_Delegate, self).drawDisplay(painter, option, rect, text)
	#----------------------------------------------------------------------
	def drawFocus(self, painter, option, rect):
		""""""
		isinstance(painter, QT.QPainter)
		isinstance(option,QT.QStyleOptionViewItem)
		isinstance(rect, QT.QRect)
		super(Item_Data_Delegate, self).drawFocus(painter, option, rect)
	#----------------------------------------------------------------------
	def drawBackground (self, painter, option, index):
		isinstance(painter,QT.QPainter)
		isinstance(option,QT.QStyleOptionViewItem)
		isinstance(index,QT.QModelIndex)
		super(Item_Data_Delegate, self).drawBackground(painter, option, index)

########################################################################
class Item_Data_Editor(object):
	#----------------------------------------------------------------------
	def __init__(self,editor_data):
		""""""
		self._editor_data = editor_data
	#----------------------------------------------------------------------
	@property
	def has_editor(self):
		""""""
		return self._editor != None
	#----------------------------------------------------------------------
	def createEditor(self,parent=None):
		""""""
		return None
	#----------------------------------------------------------------------
	def setEditorData(self):
		""""""
		pass
	#----------------------------------------------------------------------
	def setModelData(self):
		""""""
		pass


########################################################################
class Spin_Box_Data_Editor(Item_Data_Editor):
	#----------------------------------------------------------------------
	def __init__(self,item_data):
		""""""
		super(Spin_Box_Data_Editor,self).__init__(item_data)
	#----------------------------------------------------------------------
	def createEditor(self,parent=None,index=None):
		""""""
		self._editor = QT.QSpinBox(parent=parent)
		return self._editor
	#----------------------------------------------------------------------
	def setEditorData(self):
		""""""
		self._editor.setValue(int(self._editor_data.display_name))
	#----------------------------------------------------------------------
	def setModelData(self):
		""""""
		self._editor_data.display_name = self._editor.value()
		
########################################################################
class Combo_Box_Data_Editor(Item_Data_Editor):
	#----------------------------------------------------------------------
	def __init__(self,item_data):
		""""""
		super(Combo_Box_Data_Editor,self).__init__(item_data)
	#----------------------------------------------------------------------
	def createEditor(self,parent=None,index=None):
		""""""
		self._editor = QT.QComboBox(parent=parent)
		return self._editor
	#----------------------------------------------------------------------
	def setEditorData(self):
		""""""
		self._editor.addItems(["New Name One","New Name 2",self.item_data.display_name])
		self._editor.setCurrentIndex(self._editor.findText(self.item_data.display_name))
	#----------------------------------------------------------------------
	def setModelData(self):
		""""""
		self.item_data.display_name = self._editor.currentText()

########################################################################
class _AUTO_PROPERTIES_METACLASS(type):
	""""""
	#----------------------------------------------------------------------
	def __new__(mcs, name, bases, attdict):
		"""This Is Run Before The Class Is Created. Not An Instance Of The Class But The Creation Of The Class Itself"""
		# Check If The Class Has Been Assigned An Id Number
		# If Not Generate One And Add It The Dict Of Items That Represent The Class Attributes
		# Generate The New Class Type And Return It
		fn_get_prefix = "_fn_get_"
		fn_set_prefix = "_fn_set_"
		fn_end_prefix = "_value"
		fn_get_expr = fn_get_prefix + "{}" + fn_end_prefix
		fn_set_expr = fn_set_prefix + "{}" + fn_end_prefix
		
		def find_base_class_fset(prop_name,bases):
			"""Finds The Setter Function Within All The Base Clases Recursivly"""
			fn_name = fn_set_expr.format(prop_name)
			for base in bases:
				if hasattr(base,fn_name):
					return getattr(base,fn_name)
				else:
					return find_base_class_fget(prop_name, [b for b in base.__bases__ if not type(b) == type])
		def find_base_class_fget(prop_name,bases):
			"""Finds The getter Function Within All The Base Clases Recursivly"""
			fn_name = fn_get_expr.format(prop_name)
			for base in bases:
				if hasattr(base,fn_name):
					return getattr(base,fn_name)
				else:
					return find_base_class_fget(prop_name, [b for b in base.__bases__ if not type(b) == type])
		def get_prop_name(fn_name):
			return key.replace(fn_get_prefix,"").replace(fn_set_prefix,"").replace(fn_end_prefix,"")
			
		collection = dict()
		for key in list(attdict.keys()):
			if key.startswith(fn_get_prefix) or key.startswith(fn_set_prefix):
				if key.endswith(fn_end_prefix):
					prop_name = get_prop_name(key)
					collection[prop_name] = dict()
		
		for prop_name,prop_data in list(collection.items()):
			get_fn = fn_get_expr.format(prop_name)
			set_fn = fn_set_expr.format(prop_name)
			
			if get_fn in attdict:
				prop_data["fget"] = attdict[get_fn]
			else:
				prop_data["fget"] = find_base_class_fget(prop_name, bases)
				
			if set_fn in attdict:
				prop_data["fset"] = attdict[set_fn]
			else:
				prop_data["fset"] = find_base_class_fset(prop_name, bases)
			attdict[prop_name]=property(**prop_data)
			
		res = type.__new__(mcs, name, bases, attdict)
		return res

	#----------------------------------------------------------------------
	def __init__(cls, name, bases, dct):
		return super(_AUTO_PROPERTIES_METACLASS, cls).__init__(name, bases, dct)

	#----------------------------------------------------------------------
	def __call__(cls,*args,**kwargs):
		"""This Is Run Before An Instance Of The Class Created And Allows For The Inspection And Manipulation Of The Values Used To Create The New Instance"""
		# Create The New Class Instance
		
		res = type.__call__(cls,*args,**kwargs)
		return res

# ======================================================================
# DATA MODEL STANDERD ITEM CONTAINERS
# ----------------------------------------------------------------------
# Synopsis:
#     Like A StanderedItem
# ======================================================================

########################################################################
class Standered_Item(object, metaclass=_AUTO_PROPERTIES_METACLASS):
	"""
	Class Info:
	===============
	| This Is The Base Class For Item Data
	| It Stores Data That It Needs To Display Itself
	"""
	DEF_VALS      = DATA_DEFAULT_VALUES
	H_ALIGNMENT   = Constants.AlignmentFlag.Horizontal
	V_ALIGNMENT   = Constants.AlignmentFlag.Vertical
	ID_ROLE       = Base_Item_Data_Roles

	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		"""
		Params: Name: Type: Default
		------------------------------
			| **selectable** : *bool* : True
			| **enabled** : *bool* : True
			| **editable** : *bool* : True
			| **dragable** : *bool* : False
			| **dropable** : *bool* : False
			| **checkable** : *bool* : False
			| **checked** : *bool* : False
			| **font_family** : *str* : None
			| **font_size** : *int* : None
			| **size_hint** : *QSize* : None
			| **status_tip** : *str* : None
			| **tool_tip** : *str* : None
			| **brush** : *QBrush* : None
			| **icon_visable** : *bool* : False
			| **icon_color** : *GlobalColor* : None
			| **display_name** : *str* : None
			| **background_color** : *GlobalColor* : None
			| **foreground_color** : *GlobalColor* : None
		"""
			#raise ValueError("tree_item input must be and instance or subclass of Tree_Item and a %r was found" % type(tree_item))
		self._item_selectable           = kwargs.get("selectable",True)
		self._item_enabled              = kwargs.get("enabled",True)
		self._item_editable             = kwargs.get("editable",True)
		self._item_dragable             = kwargs.get("dragable",False)
		self._item_dropable             = kwargs.get("dropable",False)
		self._item_checkable            = kwargs.get("checkable",False)
		self._item_tristate             = kwargs.get("tristate",False)
		self._item_display_name         = kwargs.get("display_name",None)
		self._item_font_family          = kwargs.get("font_family",None)
		self._item_font_size            = kwargs.get("font_size",None)
		self._item_font_weight          = kwargs.get("font_weight",None)
		self._item_font_capitalization  = kwargs.get("font_capitalization",None)
		self._item_background_color     = kwargs.get("background_color",None)
		self._item_foreground_color     = kwargs.get("foreground_color",None)
		self._item_brush                = kwargs.get("brush",None)
		self._item_icon_visable         = kwargs.get("icon_visable",False)
		self._item_icon_color           = kwargs.get("icon_color",None)
		self._item_size_hint            = kwargs.get("size_hint",None)
		self._item_status_tip           = kwargs.get("status_tip",None)
		self._item_tool_tip             = kwargs.get("tool_tip",None)
		self._item_horizontal_alignment = self.H_ALIGNMENT.Values.get(kwargs.get("horizontal_alignment",None),None)
		self._item_vertical_alignment   = self.V_ALIGNMENT.Values.get(kwargs.get("vertical_alignment",None),None)
		self._data_icon                 = None #create_Item_Icon(":/outliner/group")
		self._data_font                 = None
		if kwargs.get("checked",False):
			self._data_checked          = QT.Qt.CheckState.Checked
		else:
			self._data_checked          = QT.Qt.CheckState.Unchecked
		self._data_foreground_color     = None
		self._data_background_color     = None
		self._data_alignment            = None
		self._data_flags                = QT.Qt.ItemFlags()
		self._update_flags()
		self._update_text_alignment()
		if False:
			self.background_color=QT.QColor
			self.foreground_color=QT.QColor
			self.brush=QT.QBrush
			self.size_hint=QT.QSize
			self.status_tip=str
			self.tool_tip=str
			self.text_font=QT.QFont
			self.icon_visable = None
	#----------------------------------------------------------------------
	def createColorIcon(self, color):
		if isinstance(color, str):
			if color.startswith(":"):
				pixmap = QT.QPixmap(color)
				return QT.QIcon(pixmap)
			elif os.path.exists(color):
				pixmap = QT.QPixmap(color)
				return QT.QIcon(pixmap)
		else:
			pixmap = QT.QPixmap(16, 16)
			painter = QT.QPainter(pixmap)
			painter.setPen(QT.Qt.NoPen)
			painter.fillRect(QT.QRect(0, 0, 16, 16), color)
			#painter.fillRect(QT.QRect(0, 10, 20, 10), QT.Qt.GlobalColor.green)
			painter.end()
			return QT.QIcon(pixmap)
	#----------------------------------------------------------------------
	def get_Current_State(self):
		""""""
		state = dict()
		for key in list(self.__dict__.keys()):
			if key.startswith("_item_"):
				val = getattr(self, key)
				if not val is None:
					key = key.replace("_item_", "")
					if hasattr(val, "name"):
						state[key] = val.name
					else:
						state[key] = val
		return state
	#----------------------------------------------------------------------
	def set_Current_State(self, state):
		""""""
		if not isinstance(state,dict):
			raise ValueError("input state must be a dict and a %r was given" % type(state))
		for key, val in list(state.items()):
			if hasattr(self, "_item_"+key):
				if val is not None:
					try:
						setattr(self, key, val)
					except AttributeError:
						pass
	#----------------------------------------------------------------------
	def _fn_get_icon_visable_value(self):
		"""Returns Weather Or Not The Icon Is Visable"""
		return self._item_icon_visable
	#----------------------------------------------------------------------
	def _fn_set_icon_visable_value(self, value):
		"""Set Weather Or Not The Icon Is Visable"""
		if not isinstance(value,(bool, int)):
			raise ValueError("input value must be of type bool or int and a %r was given" % type(value))
		self._item_icon_visable = value
	#----------------------------------------------------------------------
	def _fn_get_background_color_value(self):
		"""Get The Backround Color Of A Item"""
		if self._data_background_color is None and not self._item_background_color == None:
			self._update_background_color()
		return self._data_background_color
	#----------------------------------------------------------------------
	def _fn_set_background_color_value(self, value):
		if value is None:
			self._item_background_color = value
		elif isinstance(value,QT.QColor):
			self._item_background_color = value.getRgb()
		else:
			raise ValueError("input value must be an instance of QT.QColor and a %r was given" % type(value))
		self._update_background_color()
	#----------------------------------------------------------------------
	def _fn_get_foreground_color_value(self):
		if self._data_foreground_color is None and not self._item_foreground_color == None:
			self._update_foregound_color()
		return self._data_foreground_color
	#----------------------------------------------------------------------
	def _fn_set_foreground_color_value(self, value):
		if value is None:
			self._item_foreground_color = value
		elif isinstance(value,(QT.QColor, QT.Qt.GlobalColor)):
			if isinstance(value,QT.Qt.GlobalColor):
				value = QT.QColor(value)
			self._item_foreground_color = value.getRgb()
		else:
			raise ValueError("input value must be an instance of QT.QColor and a %r was given" % type(value))
		self._update_foregound_color()
	#----------------------------------------------------------------------
	def _fn_get_brush_value(self):
		if self._item_brush is None:
			return self.DEF_VALS.BRUSH.value()
		else:
			return self._item_brush
	#----------------------------------------------------------------------
	def _fn_set_brush_value(self, value):
		if not isinstance(value,QT.QBrush):
			raise ValueError("input value must be an instance of QT.QBrush and a %r was given" % type(value))
		self._item_bush = value
	#----------------------------------------------------------------------
	def _fn_get_size_hint_value(self):
		return self._item_size_hint
	#----------------------------------------------------------------------
	def _fn_set_size_hint_value(self, value):
		if not isinstance(value,QT.QSize):
			raise ValueError("input value must be an instance of QT.QSize and a %r was given" % type(value))
		self._item_size_hint = value	
	#----------------------------------------------------------------------
	def _fn_get_status_tip_value(self):
		if self._item_status_tip is None:
			return ""
		else:
			return self._item_status_tip
	#----------------------------------------------------------------------
	def _fn_set_status_tip_value(self, value):
		if not isinstance(value,str):
			raise ValueError("input value must be an instance of (str,unicode) and a %r was given" % type(value))
		self._item_status_tip = value
	#----------------------------------------------------------------------
	def _fn_get_tool_tip_value(self):
		if self._item_tool_tip is None:
			return ""
		else:
			return self._item_tool_tip
	#----------------------------------------------------------------------
	def _fn_set_tool_tip_value(self, value):
		if not isinstance(value,str):
			raise ValueError("input value must be an instance of (str,unicode) and a %r was given" % type(value))
		self._item_tool_tip = value
	#----------------------------------------------------------------------
	def _fn_get_vertical_alignment_value(self):
		if self._item_vertical_alignment is None:
			return self.DEF_VALS.DISPLAY.alignment_V
		return self._item_vertical_alignment
	#----------------------------------------------------------------------
	def _fn_set_vertical_alignment_value(self, value):
		""""""
		if value is None:
			self._item_vertical_alignment = value
		elif value in list(self.V_ALIGNMENT.Values.keys()):
			self._item_vertical_alignment = self.V_ALIGNMENT.Values[value]
		else:
			raise ValueError("input value must be one of the fallowing (%s) and a %r was given" % (",".join(list(self.V_ALIGNMENT.Values.keys())), value))
		self._update_text_alignment()
	#----------------------------------------------------------------------
	def _fn_get_horizontal_alignment_value(self):
		if self._item_horizontal_alignment is None:
			return self.DEF_VALS.DISPLAY.alignment_H
		return self._item_horizontal_alignment
	#----------------------------------------------------------------------
	def _fn_set_horizontal_alignment_value(self, value):
		if value is None:
			self._item_horizontal_alignment = value
		elif value in list(self.H_ALIGNMENT.Values.keys()):
			self._item_horizontal_alignment = self.H_ALIGNMENT.Values[value]
		else:
			raise ValueError("input value must be one of the fallowing (%s) and a %r was given" % (",".join(list(self.H_ALIGNMENT.Values.keys())), value))
		self._update_text_alignment()
	#----------------------------------------------------------------------
	def _fn_get_text_alignment_value(self):
		if self._data_alignment is None:
			return QT.Qt.AlignmentFlag(self.horizontal_alignment|self.vertical_alignment)
		return self._data_alignment
	#----------------------------------------------------------------------
	def _fn_get_font_family_value(self):
		if self._item_font_family is None:
			return False
		else:
			return self._item_font_family
	#----------------------------------------------------------------------
	def _fn_set_font_family_value(self, value):
		if not isinstance(value,str):
			raise ValueError("input value must be an instance of str, unicode and a %r was given" % type(value))
		self._item_font_family = value
		self._update_font()
	#----------------------------------------------------------------------
	def _fn_get_font_size_value(self):
		if self._item_font_size is None:
			return False
		else:
			return self._item_font_size
	#----------------------------------------------------------------------
	def _fn_set_font_size_value(self, value):
		if not isinstance(value,(int)):
			raise ValueError("input value must be an instance of (int) and a %r was given" % type(value))
		self._item_font_size = value
		self._update_font()
	#----------------------------------------------------------------------
	def _fn_get_font_weight_value(self):
		if self._item_font_weight is None:
			return False
		else:
			return self._item_font_weight
	#----------------------------------------------------------------------
	def _fn_set_font_weight_value(self, value):

		if not isinstance(value,(int)):
			raise ValueError("input value must be an instance of (int) and a %r was given" % type(value))
		if int(value) == 0:
			value = None
		elif not int(value) in [25, 50, 63, 75, 87]:
			raise ValueError("input value must be one of the fallowing values of 25, 50, 63, 75, 87 and %i was given" % int(value))
		self._item_font_weight = value
		self._update_font()
	#----------------------------------------------------------------------
	def _fn_get_font_capitalization_value(self):
		if self._item_font_capitalization is None:
			return False
		else:
			return self._item_font_capitalization
	#----------------------------------------------------------------------
	def _fn_set_font_capitalization_value(self, value):
		if not isinstance(value,(int)):
			raise ValueError("input value must be an instance of (int) and a %r was given" % type(value))
		self._item_font_capitalization = value
		self._update_font()
	#----------------------------------------------------------------------
	def _fn_get_selectable_value(self):
		if self._item_selectable is None:
			return True
		else:
			return self._item_selectable
	#----------------------------------------------------------------------
	def _fn_set_selectable_value(self, value):
		if not isinstance(value,(bool, int)):
			raise ValueError("input value must be an instance of (bool, int) and a %r was given" % type(value))
		self._item_selectable = value
		self._update_flags()
	#----------------------------------------------------------------------
	def _fn_get_checked_value(self):
		if self._item_checkable:
			return self._data_checked
		else:
			return None
	#----------------------------------------------------------------------
	def _fn_set_checked_value(self, value):
		if not self._item_checkable is None and self._item_checkable:
			if value is True or value == QT.Qt.CheckState.Checked:
				self._data_checked = QT.Qt.CheckState.Checked
			else:
				self._data_checked = QT.Qt.CheckState.Unchecked
	#----------------------------------------------------------------------
	def _fn_get_enabled_value(self):
		if self._item_enabled is None:
			return True
		else:
			return self._item_enabled
	#----------------------------------------------------------------------
	def _fn_set_enabled_value(self, value):
		if not isinstance(value,(bool, int)):
			raise ValueError("input value must be an instance of (bool, int) and a %r was given" % type(value))
		self._item_enabled = value
		self._update_flags()
	#----------------------------------------------------------------------
	def _fn_get_editable_value(self):
		if self._item_editable is None:
			return True
		else:
			return self._item_editable 
	#----------------------------------------------------------------------
	def _fn_set_editable_value(self, value):
		if not isinstance(value,(bool, int)):
			raise ValueError("input value must be an instance of (bool, int) and a %r was given" % type(value))
		self._item_editable = value
		self._update_flags()
	#----------------------------------------------------------------------
	def _fn_get_dragable_value(self):
		if self._item_dragable is None:
			return True
		else:
			return self._item_dragable
	#----------------------------------------------------------------------
	def _fn_set_dragable_value(self, value):
		if not isinstance(value,(bool, int)):
			raise ValueError("input value must be an instance of (bool, int) and a %r was given" % type(value))
		self._item_dragable = value
		self._update_flags()
	#----------------------------------------------------------------------
	def _fn_get_dropable_value(self):
		if self._item_dropable is None:
			return True
		else:
			return self._item_dropable 
	#----------------------------------------------------------------------
	def _fn_set_dropable_value(self, value):
		if not isinstance(value,(bool, int)):
			raise ValueError("input value must be an instance of (bool, int) and a %r was given" % type(value))
		self._item_dropable = value
		self._update_flags()
	#----------------------------------------------------------------------
	def _fn_get_checkable_value(self):
		if self._item_checkable is None:
			return False
		else:
			return self._item_checkable
	#----------------------------------------------------------------------
	def _fn_set_checkable_value(self, value):
		if not isinstance(value,(bool, int)):
			raise ValueError("input value must be an instance of (bool, int) and a %r was given" % type(value))
		self._item_checkable = value
		self._update_flags()
	#----------------------------------------------------------------------
	def _fn_get_tristate_value(self):
		if self._item_tristate is None:
			return False
		else:
			if self.checkable:
				return self._item_tristate
			else:
				return False
	#----------------------------------------------------------------------
	def _fn_set_tristate_value(self, value):
		if not isinstance(value,(bool, int)):
			raise ValueError("input value must be an instance of (bool, int) and a %r was given" % type(value))
		self._item_tristate = value
		self._update_flags()
	#----------------------------------------------------------------------
	def _fn_get_display_name_value(self):
		if self._item_display_name is None:
			return None
		else:
			return self._item_display_name
	#----------------------------------------------------------------------
	def _fn_set_display_name_value(self, value):
		if not isinstance(value,(str, bool, int)):
			raise ValueError("input value must be an instance of (str,unicode) and a %r was given" % type(value))
		self._item_display_name = value
	#----------------------------------------------------------------------
	def _fn_get_icon_color_value(self):
		if self._item_icon_color is None:
			return self.DEF_VALS.DISPLAY.icon_color
		else:
			return self._item_icon_color
	#----------------------------------------------------------------------
	def _fn_set_icon_color_value(self, value):
		if not isinstance(value,(QT.QColor, QT.Qt.GlobalColor, str, QT.QIcon)):
			raise ValueError("input value must be an instance of (QT.QColor, QT.Qt.GlobalColor, str) and a %r was given" % type(value))
		self._item_icon_color = value
		if not isinstance(value,QT.QIcon):
			self._data_icon  = self.createColorIcon(self._item_icon_color)
		else:
			self._data_icon = value
	#----------------------------------------------------------------------
	def _fn_get_font_value(self):
		""""""
		if any([val is not False for val in self.font_attributes]):
			return self._data_font
		else:
			return None
	#----------------------------------------------------------------------
	def _fn_get_icon_value(self):
		""""""
		if self.icon_visable:
			if self._data_icon is None:
				if self._item_icon_color is None:
					if self.DEF_VALS.icon is None:
						self.DEF_VALS.icon = self.createColorIcon(QT.QColor(self.DEF_VALS.DISPLAY.icon_color))
					return self.DEF_VALS.icon
			else:
				return self._data_icon
		else:
			return None
	#----------------------------------------------------------------------
	def _fn_set_icon_value(self,value):
		""""""
		self.icon_color = value
	#----------------------------------------------------------------------
	@property
	def flags(self):
		""""""
		return self._data_flags
	@property
	def font_attributes(self):
		return [self.font_family, self.font_size, self.font_weight, self.font_capitalization]
	#----------------------------------------------------------------------
	def _update_font(self):
		""""""
		local_font_atts = self.font_attributes
		global_font_attrs = [self.DEF_VALS.FONT.family, self.DEF_VALS.FONT.pointSize, self.DEF_VALS.FONT.weight, self.DEF_VALS.FONT.capitalization]

		if any([val is not False for val in local_font_atts]):
			if self._data_font is None:
				self._data_font = QT.QFont(self.DEF_VALS.font)
			fn_list = [self._data_font.setFamily, self._data_font.setPointSize, self._data_font.setWeight, self._data_font.setCapitalization]
			self._data_font.setFamily
			for loc, glob, fn in zip(local_font_atts, global_font_attrs, fn_list):
				if not loc is False:
					fn(loc)
				else:
					fn(glob)
	#----------------------------------------------------------------------
	def _update_flags(self):
		""""""
		flgs = QT.Qt.ItemFlags()
		if self.selectable:
			flgs =  flgs | QT.Qt.ItemFlag.ItemIsSelectable
		if self.editable:
			flgs =  flgs | QT.Qt.ItemFlag.ItemIsEditable
		if self.enabled:
			flgs =  flgs | QT.Qt.ItemFlag.ItemIsEnabled
		if self.dragable:
			flgs =  flgs | QT.Qt.ItemFlag.ItemIsDragEnabled
		if self.dropable:
			flgs =  flgs | QT.Qt.ItemFlag.ItemIsDropEnabled
		if self.checkable:
			flgs =  flgs | QT.Qt.ItemFlag.ItemIsUserCheckable
		if self.tristate:
			flgs =  flgs | QT.Qt.ItemFlag.ItemIsTristate
		self._data_flags = flgs
	#----------------------------------------------------------------------
	def _update_text_alignment(self):
		""""""
		self._data_alignment = QT.Qt.AlignmentFlag(self.horizontal_alignment|self.vertical_alignment)
	#----------------------------------------------------------------------
	def _update_foregound_color(self):
		""""""
		if self._item_foreground_color is None:
			self._data_foreground_color = self.DEF_VALS.DISPLAY.foreground_color
		else:
			if isinstance(self._item_foreground_color, (QT.Qt.GlobalColor,QT.QColor)):
				self._data_foreground_color = QT.QColor(self._item_foreground_color)
			else:
				if isinstance(self._item_foreground_color,str):
					self._data_foreground_color = QT.QColor(self._item_foreground_color)
				else:
					self._data_foreground_color = QT.QColor(*self._item_foreground_color)
	#----------------------------------------------------------------------
	def _update_background_color(self):
		""""""
		if self._item_background_color is None:
			self._data_background_color = None
		else:
			if isinstance(self._item_background_color,str):
				self._data_background_color = QT.QColor(self._item_background_color)
			elif isinstance(self._item_background_color,QT.Qt.GlobalColor):
				self._data_background_color = QT.QColor(self._item_background_color)
			else:
				self._data_background_color = QT.QColor(*self._item_background_color)
	#----------------------------------------------------------------------
	def data(self, role=Base_Item_Data_Roles.DISPLAY):
		if   role in Base_Item_Data_Roles.DP_ED:                ## DISPLAY OR EDIT
			return self.display_name
		elif role == Base_Item_Data_Roles.FOREGROUND:           ## FOREGROUND
			return self.foreground_color
		elif role == Base_Item_Data_Roles.BACKGROUND:           ## BACKGROUND
			return self.background_color
		elif role == Base_Item_Data_Roles.SIZEHINT:             ## SIZEHINT
			return self.size_hint
		elif role == Base_Item_Data_Roles.TOOLTIP:              ## TOOLTIP
			return self.tool_tip
		elif role == Base_Item_Data_Roles.STATUSTIP:            ## STATUSTIP
			return self.status_tip
		elif role == Base_Item_Data_Roles.FONT:                 ## FONT
			return self.font
		elif role == Base_Item_Data_Roles.TEXT_ALIGNMENT:       ## TEXT_ALIGNMENT
			return self.text_alignment
		elif role == Base_Item_Data_Roles.DECORATION:           ## DECORATION
			if self.icon_visable:
				return self.icon
			else:
				return None
		elif role == Base_Item_Data_Roles.ICON_COLOR:           ## ICON_COLOR
			return self.icon_color
		elif role == Base_Item_Data_Roles.FONT_SIZE:            ## FONT_SIZE
			return self.text_size
		elif role == Base_Item_Data_Roles.FONT_WEIGHT:          ## FONT_WEIGHT
			return self.font_weight
		elif role == Base_Item_Data_Roles.FONT_FAMILY:          ## FONT_FAMILY
			return self.font_family
		elif role == Base_Item_Data_Roles.FONT_CAPITALIZATION:  ## FONT_CAPITALIZATION
			return self.font_capitalization
		elif role == Base_Item_Data_Roles.SELECTABLE:           ## SELECTABLE
			return self.selectable
		elif role == Base_Item_Data_Roles.ENABLED:              ## ENABLED
			return self.enabled
		elif role == Base_Item_Data_Roles.EDITABLE:             ## EDITABLE
			return self.editable
		elif role == Base_Item_Data_Roles.DRAGABLE:             ## DRAGABLE
			return self.dragable
		elif role == Base_Item_Data_Roles.DROPABLE:             ## DROPABLE
			return self.dropable
		elif role == Base_Item_Data_Roles.CHECKABLE:            ## CHECKABLE
			return self.checkable
		elif role == Base_Item_Data_Roles.CHECKSTATE:           ## CHECKSTATE
			return self.checked
		elif role == Base_Item_Data_Roles.TRISTATE:             ## TRISTATE
			return self.tristate
		elif role == Base_Item_Data_Roles.HORIZONTAL_ALIGNMENT: ## HORIZONTAL_ALIGNMENT
			return self.horizontal_alignment
		elif role == Base_Item_Data_Roles.VERTICAL_ALIGNMENT:   ## VERTICAL_ALIGNMENT
			return self.vertical_alignment
		elif role == Base_Item_Data_Roles.USER:                 ## USER
			return self
		return None
	#----------------------------------------------------------------------
	def setData(self, role, value):
		res = False
		if   role in Base_Item_Data_Roles.DP_ED:                ## DISPLAY OR EDIT
			self.display_name = value
			res = True
		elif role == Base_Item_Data_Roles.FOREGROUND:           ## FOREGROUND
			self.foreground_color = value
			res = True
		elif role == Base_Item_Data_Roles.BACKGROUND:           ## BACKGROUND
			self.background_color = value
			res = True
		elif role == Base_Item_Data_Roles.SIZEHINT:             ## SIZEHINT
			self.size_hint        = value
			res = True
		elif role == Base_Item_Data_Roles.TOOLTIP:              ## TOOLTIP
			self.tool_tip         = value
			res = True
		elif role == Base_Item_Data_Roles.STATUSTIP:            ## STATUSTIP
			self.status_tip       = value
			res = True
		elif role == Base_Item_Data_Roles.FONT:                 ## FONT
			self.text_font        = value
			res = True
		elif role == Base_Item_Data_Roles.TEXT_ALIGNMENT:       ## TEXT_ALIGNMENT
			self.text_alignment   = value
			res = True
		elif role == Base_Item_Data_Roles.DECORATION:           ## DECORATION
			self.brush            = value
			res = True
		elif role == Base_Item_Data_Roles.ICON_COLOR:           ## ICON_COLOR
			self.icon_color       = value
			res = True
		elif role == Base_Item_Data_Roles.FONT_SIZE:            ## FONT_SIZE
			self.text_size        = value
		elif role == Base_Item_Data_Roles.FONT_WEIGHT:          ## FONT_WEIGHT
			self.font_weight      = value
			res = True
		elif role == Base_Item_Data_Roles.FONT_FAMILY:          ## FONT_FAMILY
			self.font_family         = value
			res = True
		elif role == Base_Item_Data_Roles.FONT_CAPITALIZATION:  ## FONT_CAPITALIZATION
			self.font_capitalization = value
			res = True
		elif role == Base_Item_Data_Roles.SELECTABLE:           ## SELECTABLE
			self.selectable        = value
			res = True
		elif role == Base_Item_Data_Roles.ENABLED:              ## ENABLED
			self.enabled =  value
			res = True
		elif role == Base_Item_Data_Roles.EDITABLE:             ## EDITABLE
			self.editable = value
			res = True
		elif role == Base_Item_Data_Roles.DRAGABLE:             ## DRAGABLE
			self.dragable = value
			res = True
		elif role == Base_Item_Data_Roles.DROPABLE:             ## DROPABLE
			self.dropable = value
			res = True
		elif role == Base_Item_Data_Roles.CHECKABLE:            ## CHECKABLE
			self.checkable = value
			res = True
		elif role == Base_Item_Data_Roles.CHECKSTATE:           ## CHECKSTATE
			self.checked = value
			res = True
		elif role == Base_Item_Data_Roles.TRISTATE:             ## TRISTATE
			self.tristate = value
			res = True
		elif role == Base_Item_Data_Roles.HORIZONTAL_ALIGNMENT: ## HORIZONTAL_ALIGNMENT
			self.horizontal_alignment = value
			res = True
		elif role == Base_Item_Data_Roles.VERTICAL_ALIGNMENT:   ## VERTICAL_ALIGNMENT
			self.vertical_alignment = value
			res = True
		elif role == Base_Item_Data_Roles.ICON_VISABLE:         ## ICON_VISABLE
			self.icon_visable = value
			res = True
		return res

########################################################################
class Standered_Item_Data(Standered_Item):
	"""This Is The Base Item Data Class It Only Stores Data That Is Needed To Display Itself"""
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		"""
		Params: Name: Type: Default
		------------------------------
			| **tree_item** : *Base_Model_Item* : None
			| **selectable** : *bool* : True
			| **enabled** : *bool* : True
			| **editable** : *bool* : True
			| **dragable** : *bool* : False
			| **dropable** : *bool* : False
			| **checkable** : *bool* : False
			| **checked** : *bool* : False
			| **font_family** : *str* : None
			| **font_size** : *int* : None
			| **size_hint** : *QSize* : None
			| **status_tip** : *str* : None
			| **tool_tip** : *str* : None
			| **brush** : *QBrush* : None
			| **icon_visable** : *bool* : False
			| **icon_color** : *GlobalColor* : None
			| **display_name** : *str* : None
			| **background_color** : *GlobalColor* : None
			| **foreground_color** : *GlobalColor* : None
		"""
		super(Standered_Item_Data,self).__init__(**kwargs)
		self.tree_item                  = kwargs.get("tree_item",None)
		if False:
			isinstance(self.tree_item, DATA_TYPES.Model_Items.Base_Model_Item)
			#raise ValueError("tree_item input must be and instance or subclass of Tree_Item and a %r was found" % type(tree_item))
		self._internal_editor = None
	#----------------------------------------------------------------------
	@property
	def has_editor(self):
		""""""
		return self._internal_editor is not None
	#----------------------------------------------------------------------
	@property
	def internal_editor(self):
		""""""
		return self._internal_editor
	#----------------------------------------------------------------------
	@internal_editor.setter
	def internal_editor(self,editor):
		""""""
		self._internal_editor = editor
	#----------------------------------------------------------------------
	def _fn_get_column_value(self):
		""""""
		return self.tree_item._column_items.items.index(self)
	#----------------------------------------------------------------------
	def _fn_get_index_value(self):
		""""""
		return self.tree_item.model.indexFromItemData(self)
	#----------------------------------------------------------------------
	def _update_Changed_Data(self, role):
		""""""
		if self.tree_item is not None:
			index =  self.index
			try:
				self.tree_item.model.dataChanged.emit(index, index, role)
			except:
				self.tree_item.model.dataChanged.emit(index, index)
	#----------------------------------------------------------------------
	def data(self, role=Base_Item_Data_Roles.DISPLAY):
		if role == Base_Item_Data_Roles.TREE_OBJECT:
			return self.tree_item
		elif role == Base_Item_Data_Roles.INTERNAL_EDITOR:
			return self.internal_editor
		else:
			return super(Standered_Item_Data,self).data(role=role)

########################################################################
class Standered_Item_List_Combo_Box_Line_Edit(QT.QLineEdit):
	#----------------------------------------------------------------------
	def __init__(self,item_list,parent=None):
		""""""
		super(Standered_Item_List_Combo_Box_Line_Edit,self).__init__(parent=parent)
		self._item_list = item_list
		self.editingFinished.connect(self.on_editing_finished)
	#----------------------------------------------------------------------
	def on_editing_finished(self):
		""""""
		if not self._item_list.active_item.display_name == self.text():
			self._item_list.active_item.display_name = self.text()
########################################################################
class Standered_Item_List_Combo_Box(QComboBox.ComboBox):
	#----------------------------------------------------------------------
	def __init__(self,item_list,parent=None):
		""""""
		super(Standered_Item_List_Combo_Box,self).__init__(parent=parent)
		isinstance(item_list,Standered_Item_List)
		self.setLineEdit(Standered_Item_List_Combo_Box_Line_Edit(item_list, parent=self))
		self._item_list = item_list
		for item in item_list:
			self.addItem(item.display_name,userData=item)
		self.setEditable(True)
		#self.activated.connect(self.myactived)
		self.currentIndexChanged.connect(self.mycurrentIndexChanged)
		self.highlighted.connect(self.myhighlighted)
		#self.editTextChanged.connect(self.myeditTextChanged)
	#----------------------------------------------------------------------
	def itemText(self, index):
		""""""
		res = super(Standered_Item_List_Combo_Box,self).itemText(index)
		return res
	#----------------------------------------------------------------------
	def itemData(self, index, role=Base_Item_Data_Roles.USER):
		""""""
		res = super(Standered_Item_List_Combo_Box,self).itemData(index,role)
		return res
	#----------------------------------------------------------------------
	def setItemData(self, index, value, role=Base_Item_Data_Roles.USER):
		""""""
		super(Standered_Item_List_Combo_Box,self).setItemData(index,value,role)
	#----------------------------------------------------------------------
	def setItemText(self, index, text):
		""""""
		super(Standered_Item_List_Combo_Box,self).setItemText(index,text)
	#----------------------------------------------------------------------
	def setEditText(self,text):
		""""""
		super(Standered_Item_List_Combo_Box,self).setEditText(text)
	#----------------------------------------------------------------------
	def myactived(self,value):
		""""""
		print(("item activated {}".format(value)))
		self._item_list.active_index=value
	#----------------------------------------------------------------------
	def myhighlighted(self,value):
		""""""
		print(("highlighted Changed {}".format(value)))
		#self._item_list.active_index=value
	#----------------------------------------------------------------------
	def mycurrentIndexChanged(self,value):
		""""""
		print(("current Index Changed {}".format(value)))
		self._item_list.active_index=value
	#----------------------------------------------------------------------
	def myeditTextChanged(self,value):
		""""""
		print(("current Text Changed {}".format(value)))
		#self._item_list.active_item.display_name=value
	#----------------------------------------------------------------------
	def showPopup(self):
		""""""
		super(Standered_Item_List_Combo_Box,self).showPopup()
		print("Popup Shown")
		self._item_list.active_index=self.CurrentIndex
	#----------------------------------------------------------------------
	def hidePopup(self):
		""""""
		super(Standered_Item_List_Combo_Box,self).hidePopup()
		print("Popup Hidden")
		self._item_list.active_index=self.CurrentIndex
########################################################################
class Standered_Item_List_Data_Editor(Item_Data_Editor):
	#----------------------------------------------------------------------
	def __init__(self,item_list):
		""""""
		super(Standered_Item_List_Data_Editor,self).__init__(item_list)
		isinstance(self._editor_data,Standered_Item_List)
	#----------------------------------------------------------------------
	def createEditor(self,parent=None,index=None):
		""""""
		self._editor = Standered_Item_List_Combo_Box(self._editor_data,parent=parent)
		return self._editor
	#----------------------------------------------------------------------
	def setEditorData(self):
		""""""
		self._editor.setCurrentIndex(self._editor.findText(self._editor_data.display_name))
		#self._editor.showPopup()
	#----------------------------------------------------------------------
	def setModelData(self):
		""""""
		

######################################################################## 
class Standered_Item_List(list, metaclass=_AUTO_PROPERTIES_METACLASS):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		"""Constructor"""
		super(Standered_Item_List,self).__init__(*args)
		if not len(self):
			self.append(Standered_Item(display_name="A"))
			self.append(Standered_Item(display_name="B"))
			self.append(Standered_Item(display_name="C"))
		self.tree_item        = kwargs.get("tree_item",None)
		self._active_index    = kwargs.get("active_index",None)
		self._internal_editor = Standered_Item_List_Data_Editor(self)
		
		if self._active_index == None:
			self.active_index = 0
			
		if False:
			isinstance(self.tree_item, DATA_TYPES.Model_Items.Base_Model_Item)
			self.active_item = Internal_Item_Data
			self.active_index = 0
	#----------------------------------------------------------------------
	def _fn_get_active_index_value(self):
		""""""
		return self._active_index
	#----------------------------------------------------------------------
	def _fn_set_active_index_value(self,value):
		""""""
		if isinstance(value,int) or value in self:
			if isinstance(value,int):
				try:
					item = self[value]
				except IndexError:
					if value >= len(self):
						item = self[-1]
					elif value < 0:
						item = self[0]
				finally:
					self._active_index = self.get_Index(item)
			else:
				self._active_index = self.get_Index(value)
		else:
			raise ValueError("value input must be an int or an item within this list")
	#----------------------------------------------------------------------
	def get_Index(self,item):
		""""""
		return list.index(self,item)
	#----------------------------------------------------------------------
	def _fn_get_active_item_value(self):
		""""""
		return self[self._active_index]
	#----------------------------------------------------------------------
	@property
	def internal_editor(self):
		""""""
		return self._internal_editor
	#----------------------------------------------------------------------
	@property
	def flags(self):
		""""""
		return self.active_item.flags	
	#----------------------------------------------------------------------
	def _fn_get_column_value(self):
		""""""
		return self.tree_item._column_items.items.index(self)
	#----------------------------------------------------------------------
	def _fn_get_index_value(self):
		""""""
		return self.tree_item.model.indexFromItemData(self)
	#----------------------------------------------------------------------
	def _fn_get_icon_visable_value(self):
		"""Returns Weather Or Not The Icon Is Visable"""
		return self.active_item.icon_visable
	#----------------------------------------------------------------------
	def _fn_set_icon_visable_value(self, value):
		"""Set Weather Or Not The Icon Is Visable"""
		self.active_item.icon_visable = value
	#----------------------------------------------------------------------
	def _fn_get_background_color_value(self):
		"""Get The Backround Color Of A Item"""
		return self.active_item.background_color
	#----------------------------------------------------------------------
	def _fn_set_background_color_value(self, value):
		self.active_item.background_color = value
	#----------------------------------------------------------------------
	def _fn_get_foreground_color_value(self):
		return self.active_item.foreground_color
	#----------------------------------------------------------------------
	def _fn_set_foreground_color_value(self, value):
		self.active_item.foreground_color = value
	#----------------------------------------------------------------------
	def _fn_get_brush_value(self):
		return self.active_item.brush
	#----------------------------------------------------------------------
	def _fn_set_brush_value(self, value):
		self.active_item.brush = value
	#----------------------------------------------------------------------
	def _fn_get_size_hint_value(self):
		return self.active_item.size_hint
	#----------------------------------------------------------------------
	def _fn_set_size_hint_value(self, value):
		self.active_item.size_hint = value
	#----------------------------------------------------------------------
	def _fn_get_status_tip_value(self):
		return self.active_item.status_tip
	#----------------------------------------------------------------------
	def _fn_set_status_tip_value(self, value):
		self.active_item.status_tip = value
	#----------------------------------------------------------------------
	def _fn_get_tool_tip_value(self):
		return self.active_item.tool_tip
	#----------------------------------------------------------------------
	def _fn_set_tool_tip_value(self, value):
		self.active_item.tool_tip = value
	#----------------------------------------------------------------------
	def _fn_get_vertical_alignment_value(self):
		return self.active_item.vertical_alignment
	#----------------------------------------------------------------------
	def _fn_set_vertical_alignment_value(self, value):
		self.active_item.vertical_alignment = value
	#----------------------------------------------------------------------
	def _fn_get_horizontal_alignment_value(self):
		return self.active_item.horizontal_alignment
	#----------------------------------------------------------------------
	def _fn_set_horizontal_alignment_value(self, value):
		self.active_item.horizontal_alignment = value
	#----------------------------------------------------------------------
	def _fn_get_text_alignment_value(self):
		return self.active_item.text_alignment
	#----------------------------------------------------------------------
	def _fn_get_font_family_value(self):
		return self.active_item.font_family
	#----------------------------------------------------------------------
	def _fn_set_font_family_value(self, value):
		self.active_item.font_family = value
	#----------------------------------------------------------------------
	def _fn_get_font_size_value(self):
		return self.active_item.font_size
	#----------------------------------------------------------------------
	def _fn_set_font_size_value(self, value):
		self.active_item.font_size = value
	#----------------------------------------------------------------------
	def _fn_get_font_weight_value(self):
		return self.active_item.font_weight
	#----------------------------------------------------------------------
	def _fn_set_font_weight_value(self, value):
		self.active_item.font_weight = value
	#----------------------------------------------------------------------
	def _fn_get_font_capitalization_value(self):
		return self.active_item.font_capitalization
	#----------------------------------------------------------------------
	def _fn_set_font_capitalization_value(self, value):
		self.active_item.font_capitalization = value
	#----------------------------------------------------------------------
	def _fn_get_selectable_value(self):
		return self.active_item.selectable
	#----------------------------------------------------------------------
	def _fn_set_selectable_value(self, value):
		self.active_item.selectable = value
	#----------------------------------------------------------------------
	def _fn_get_checked_value(self):
		return self.active_item.checked
	#----------------------------------------------------------------------
	def _fn_set_checked_value(self, value):
		self.active_item.checked = value
	#----------------------------------------------------------------------
	def _fn_get_enabled_value(self):
		return self.active_item.enabled
	#----------------------------------------------------------------------
	def _fn_set_enabled_value(self, value):
		self.active_item.enabled = value
	#----------------------------------------------------------------------
	def _fn_get_editable_value(self):
		return self.active_item.editable
	#----------------------------------------------------------------------
	def _fn_set_editable_value(self, value):
		self.active_item.editable = value
	#----------------------------------------------------------------------
	def _fn_get_dragable_value(self):
		return self.active_item.dragable
	#----------------------------------------------------------------------
	def _fn_set_dragable_value(self, value):
		self.active_item.dragable = value
	#----------------------------------------------------------------------
	def _fn_get_dropable_value(self):
		return self.active_item.dropable
	#----------------------------------------------------------------------
	def _fn_set_dropable_value(self, value):
		self.active_item.dropable = value
	#----------------------------------------------------------------------
	def _fn_get_checkable_value(self):
		return self.active_item.checkable
	#----------------------------------------------------------------------
	def _fn_set_checkable_value(self, value):
		self.active_item.checkable = value
	#----------------------------------------------------------------------
	def _fn_get_tristate_value(self):
		return self.active_item.tristate
	#----------------------------------------------------------------------
	def _fn_set_tristate_value(self, value):
		self.active_item.tristate = value
	#----------------------------------------------------------------------
	def _fn_get_display_name_value(self):
		return self.active_item.display_name
	#----------------------------------------------------------------------
	def _fn_set_display_name_value(self, value):
		self.active_item.display_name = value
	#----------------------------------------------------------------------
	def _fn_get_icon_color_value(self):
		return self.active_item.icon_color
	#----------------------------------------------------------------------
	def _fn_set_icon_color_value(self, value):
		self.active_item.icon_color = value
	#----------------------------------------------------------------------
	def _fn_get_font_value(self):
		""""""
		return self.active_item.font
	#----------------------------------------------------------------------
	def _fn_get_icon_value(self):
		""""""
		return self.active_item.icon
	#----------------------------------------------------------------------
	def _fn_set_icon_value(self,value):
		""""""
		self.active_item.icon = value
	#----------------------------------------------------------------------
	def data(self, role=Base_Item_Data_Roles.DISPLAY):
		if role == Base_Item_Data_Roles.TREE_OBJECT:
			return self.tree_item
		elif role == Base_Item_Data_Roles.INTERNAL_EDITOR:
			return self.internal_editor
		else:
			return self.active_item.data(role=role)
	#----------------------------------------------------------------------
	def setData(self, role, value):
		res = self.active_item.setData(role,value)
		if res:
			self._update_Changed_Data(role)
		return res
	#----------------------------------------------------------------------
	def _update_Changed_Data(self, role):
		""""""
		index =  self.index
		try:
			self.tree_item.model.dataChanged.emit(index, index.sibling(0,self.tree_item.column_Count-1), role)
		except:
			self.tree_item.model.dataChanged.emit(index, index.sibling(0,self.tree_item.column_Count-1))
########################################################################
class Internal_Item_Data(Standered_Item_Data):
	"""This Is The Item Data Class For Use If Any Costom Data Needs To Be Accesed This Data Is Contained in the internal_data attribute"""
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		"""
		Params: Name: Type: Default
		------------------------------
			| **internal_data** : *any* : None
			| **tree_item** : *Base_Model_Item* : None
			| **selectable** : *bool* : True
			| **enabled** : *bool* : True
			| **editable** : *bool* : True
			| **dragable** : *bool* : False
			| **dropable** : *bool* : False
			| **checkable** : *bool* : False
			| **checked** : *bool* : False
			| **font_family** : *str* : None
			| **font_size** : *int* : None
			| **size_hint** : *QSize* : None
			| **status_tip** : *str* : None
			| **tool_tip** : *str* : None
			| **brush** : *QBrush* : None
			| **icon_visable** : *bool* : False
			| **icon_color** : *GlobalColor* : None
			| **display_name** : *str* : None
			| **background_color** : *GlobalColor* : None
			| **foreground_color** : *GlobalColor* : None
		"""
		super(Internal_Item_Data, self).__init__(*args,**kwargs)
		self._internal_data = kwargs.get("internal_data",None)
	#----------------------------------------------------------------------
	def data(self, role=Base_Item_Data_Roles.DISPLAY):
		if role == Base_Item_Data_Roles.INTERNAL_DATA:
			return self._internal_data
		return super(Internal_Item_Data, self).data(role)
	#----------------------------------------------------------------------
	def setData(self, role, value):
		if role == Base_Item_Data_Roles.INTERNAL_DATA:
			self.internal_data = value
			res = True
		else:
			res = super(Internal_Item_Data, self).setData(role, value)
		if res:
			self._update_Changed_Data(role)
		return res
	#----------------------------------------------------------------------
	def _fn_get_internal_data_value(self):
		""""""
		return self._internal_data
	#----------------------------------------------------------------------
	def _fn_set_internal_data_value(self, value):
		""""""
		self._internal_data = value
		
########################################################################
class Column_Item_List(object):
	#----------------------------------------------------------------------
	def __init__(self, tree_item):
		""" """
		if not hasattr(tree_item, "root_item"):
			raise TypeError("tree_item %r input does not contain a root_item attribute" % type(tree_item))
		self.tree_item = tree_item
		self.items     = []
	#----------------------------------------------------------------------
	def __iter__(self):
		""""""
		for item in self.items:
			yield item
	#----------------------------------------------------------------------
	def data(self, column=0, role=Base_Item_Data_Roles.DISPLAY):
		try:
			item = self.items[column]
			return item.data(role)
		except IndexError:
			return None
	#----------------------------------------------------------------------
	def setData(self, value, column=0, role=Base_Item_Data_Roles.DISPLAY):
		item = self.get_item(column)
		return item.setData(role, value)
	#----------------------------------------------------------------------
	def get_item(self, column=0):
		if column >= self.column_Count:
			return None
		item = self.items[column]
		isinstance(item, Internal_Item_Data)
		return item
	#----------------------------------------------------------------------
	def get_Item_Flags(self, index):
		item = self.get_item(index)
		if item is None:
			res = QT.Qt.ItemFlag.NoItemFlags
		else:
			res = item.flags
		return res
	#----------------------------------------------------------------------
	@property
	def column_Count(self):
		""""""
		return len(self.items)
	##----------------------------------------------------------------------
	@property
	def model(self):
		""""""
		return self.tree_item.root_item.model
	#----------------------------------------------------------------------
	def _get_Current_State(self):
		""""""
		state = []
		for column in self:
			isinstance(column, Internal_Item_Data)
			column_state = column.get_Current_State()
			state.append(column_state)
		return state
	#----------------------------------------------------------------------
	def get_Icon_Visable(self,column=0):
		"""Returns Weather Or Not The Icon Is Visable"""
		item = self.get_item(column)
		return False if item is None else item.icon_visable
	#----------------------------------------------------------------------
	def set_icon_visable(self, value, column=0):
		"""Set Weather Or Not The Icon Is Visable"""
		item = self.get_item(column)
		if not item is None:
			item.icon_visable = value
	#----------------------------------------------------------------------
	def get_background_color(self,column=0):
		"""Get The Backround Color Of A Item"""
		item = self.get_item(column)
		return None if item is None else item.background_color
	#----------------------------------------------------------------------
	def set_background_color(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.background_color = value
	#----------------------------------------------------------------------
	def get_foreground_color(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.foreground_color
	#----------------------------------------------------------------------
	def set_foreground_color(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.foreground_color = value
	#----------------------------------------------------------------------
	def get_brush(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.brush
	#----------------------------------------------------------------------
	def set_brush(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.brush = value
	#----------------------------------------------------------------------
	def get_size_hint(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.size_hint
	#----------------------------------------------------------------------
	def set_size_hint(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.size_hint = value
	#----------------------------------------------------------------------
	def get_status_tip(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.status_tip
	#----------------------------------------------------------------------
	def set_status_tip(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.status_tip = value
	#----------------------------------------------------------------------
	def get_tool_tip(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.tool_tip
	#----------------------------------------------------------------------
	def set_tool_tip(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.tool_tip = value
	#----------------------------------------------------------------------
	def get_vertical_alignment(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.vertical_alignment
	#----------------------------------------------------------------------
	def set_vertical_alignment(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.vertical_alignment = value
	#----------------------------------------------------------------------
	def get_horizontal_alignment(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.horizontal_alignment
	#----------------------------------------------------------------------
	def set_horizontal_alignment(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.horizontal_alignment = value
	#----------------------------------------------------------------------
	def get_text_alignment(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.text_alignment
	#----------------------------------------------------------------------
	def get_font_family(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.font_family
	#----------------------------------------------------------------------
	def set_font_family(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.font_family = value
	#----------------------------------------------------------------------
	def get_font_size(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.font_size
	#----------------------------------------------------------------------
	def set_font_size(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.font_size = value
	#----------------------------------------------------------------------
	def get_font_weight(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.font_weight
	#----------------------------------------------------------------------
	def set_font_weight(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.font_weight = value
	#----------------------------------------------------------------------
	def get_font_capitalization(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.font_capitalization
	#----------------------------------------------------------------------
	def set_font_capitalization(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.font_capitalization = value
	#----------------------------------------------------------------------
	def get_selectable(self,column=0):
		item = self.get_item(column)
		return False if item is None else item.selectable
	#----------------------------------------------------------------------
	def set_selectable(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.selectable = value
	#----------------------------------------------------------------------
	def get_enabled(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.enabled
	#----------------------------------------------------------------------
	def set_enabled(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.enabled = value
	#----------------------------------------------------------------------
	def get_editable(self,column=0):
		item = self.get_item(column)
		return False if item is None else item.editable
	#----------------------------------------------------------------------
	def set_editable(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.editable = value
	#----------------------------------------------------------------------
	def get_dragable(self,column=0):
		item = self.get_item(column)
		return False if item is None else item.dragable
	#----------------------------------------------------------------------
	def set_dragable(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.dragable = value
	#----------------------------------------------------------------------
	def get_dropable(self,column=0):
		item = self.get_item(column)
		return False if item is None else item.dropable
	#----------------------------------------------------------------------
	def set_dropable(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.dropable = value
	#----------------------------------------------------------------------
	def get_checkable(self,column=0):
		item = self.get_item(column)
		return False if item is None else item.checkable
	#----------------------------------------------------------------------
	def set_checkable(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.checkable = value
	#----------------------------------------------------------------------
	def get_tristate(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.tristate
	#----------------------------------------------------------------------
	def set_tristate(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.tristate = value
	#----------------------------------------------------------------------
	def get_display_name(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.display_name
	#----------------------------------------------------------------------
	def set_display_name(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.display_name = value
	#----------------------------------------------------------------------
	def get_icon_color(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.icon_color
	#----------------------------------------------------------------------
	def set_icon_color(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.icon_color = value
	#----------------------------------------------------------------------
	def get_font(self,column=0):
		""""""
		item = self.get_item(column)
		return False if item is None else item.font
	#----------------------------------------------------------------------
	def get_icon(self,column=0):
		""""""
		item = self.get_item(column)
		return False if item is None else item.icon
