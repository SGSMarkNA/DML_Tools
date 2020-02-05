
import os
from .. import Python_Custom_Widget_Knob
from ... import dml
import DML_Tools
DML_PYQT = DML_Tools.DML_PYQT
import nuke
import base64

#----------------------------------------------------------------------
def generate_Layer_Thumbnail(node,layer='rgba',size=32,prgsbar=None):
	""""""
	root     = nuke.root()
	comp_w   = root.width()
	comp_h   = root.height()
	division = comp_w / size
	
	icon_w = comp_w/division
	icon_h = comp_h/division
	color         = DML_PYQT.QColor()
	pix_colors    = []
	red_channel   = "{}.red".format(layer)
	green_channel = "{}.green".format(layer)
	blue_channel  = "{}.blue".format(layer)
	alpha_channel = "{}.alpha".format(layer)
	total_count = (icon_w*icon_h)*2
	if isinstance(prgsbar,DML_PYQT.QProgressBar):
		prgsbar.setValue(0)
		prgsbar.setMaximum(total_count)
	for w in range(icon_w):
		for h in range(icon_h):
			color.setRedF(float(node.sample(red_channel,w*division,h*division,division,division)))
			color.setGreenF(float(node.sample(green_channel,w*division,h*division,division,division)))
			color.setBlueF(float(node.sample(blue_channel,w*division,h*division,division,division)))
			color.setAlphaF(float(node.sample(alpha_channel,w*division,h*division,division,division)))
			pix_colors.append(color.rgba())
			if isinstance(prgsbar,DML_PYQT.QProgressBar):
				prgsbar.setValue(prgsbar.value()+1)
			
	i = 0
	image = DML_PYQT.QImage(icon_w, icon_h, DML_PYQT.QImage.Format_ARGB32_Premultiplied)
	for w_pixal in range(icon_w):
		for h_pixal in reversed(range(icon_h)):
			image.setPixel(w_pixal, h_pixal, pix_colors[i])
			i+=1
			if isinstance(prgsbar,DML_PYQT.QProgressBar):
				prgsbar.setValue(prgsbar.value()+1)
	image_path = os.path.join(os.environ['TEMP'],"nuke_layer_temp_icon.png")
	image.save(image_path, "PNG") # writes image into ba in PNG format
	with file(image_path,"r b") as f:
		f_data = f.read()
		incoded_data = base64.b64encode(f_data)
	decoded_data = base64.b64decode(incoded_data)
	pixmap = DML_PYQT.QPixmap(image)
	icon = DML_PYQT.QIcon(pixmap)
	return icon,decoded_data
		
		
    
########################################################################
class DML_Nuke_Layer_Order_List_Widget(DML_PYQT.QListWidget):
	""""""
	ItemMoved = DML_PYQT.Signal()
	def __init__(self,parent=None):
		"""Constructor"""
		super(DML_Nuke_Layer_Order_List_Widget, self).__init__(parent=parent)
		self._nuke_node = dml.to_DML_Node(nuke.thisNode())
		
		# check if the knob exists that will store the layer order used for persistent data 
		# in order to rebuild the QListWidget with the users last settings 
		if self._nuke_node.hasKnob("DML_Layer_Order_layers"):
			# if so than just get and store it
			self._imbeded_data_layer_Order_knob = self._nuke_node.nuke_object.knob("DML_Layer_Order_layers")
		else:
			# if not then create it
			self._imbeded_data_layer_Order_knob = nuke.String_Knob("DML_Layer_Order_layers","layer Order")
			# hide it so it does not get edited by the user acidently
			self._imbeded_data_layer_Order_knob.setVisible(False)
			# add it to the node
			self._nuke_node.addKnob(self._imbeded_data_layer_Order_knob)
			# set a default value of an empty list
			self._imbeded_data_layer_Order_knob.setValue("[]")
			
		# check if the knob exists that will store the layer thumbnails used for persistent data 
		# in order to rebuild the QListWidget with the users last settings 
		if self._nuke_node.hasKnob("DML_Layer_Order_Layer_Icons"):
			self._imbeded_data_layer_Icons_knob = self._nuke_node.nuke_object.knob("DML_Layer_Order_Layer_Icons")
			if self._imbeded_data_layer_Icons_knob.getText()=="":
				self.imbeded_data_layer_icons = dict()
		else:
			self._imbeded_data_layer_Icons_knob = nuke.String_Knob("DML_Layer_Order_Layer_Icons","layer Icons")
			self._imbeded_data_layer_Icons_knob.setVisible(False)
			self._nuke_node.addKnob(self._imbeded_data_layer_Icons_knob)
			# set a default value of a empty dict
			self.imbeded_data_layer_icons = dict()
		#self.rebuild_Items()
	
	#----------------------------------------------------------------------
	@property
	def imbeded_data_layer_icons(self):
		""""""
		try:
			return self._nuke_node.imbeded_data_layer_icons
		except:
			return {}
	#----------------------------------------------------------------------
	@imbeded_data_layer_icons.setter
	def imbeded_data_layer_icons(self,data):
		""""""
		self._nuke_node.imbeded_data_layer_icons = data
	
	#----------------------------------------------------------------------
	@property
	def imbeded_data_layer_order(self):
		""""""
		try:
			return self._nuke_node.imbeded_data_layer_order
		except:
			return []
	#----------------------------------------------------------------------
	@imbeded_data_layer_order.setter
	def imbeded_data_layer_order(self,data):
		""""""
		self._nuke_node.imbeded_data_layer_order = data
	
	#----------------------------------------------------------------------
	def rebuild_Items(self):
		""""""
		# clear the current item list
		self.clear()
		# get the imbeded layer order data
		layers = self.imbeded_data_layer_order
		# get the imbeded layer icon data
		icons  = self.imbeded_data_layer_icons
		# check if both imbeded data items are empty
		if len(layers) == 0:
			# if so set it to a master layer order and check if it was set
			check = self.set_Layer_Data_From_Master_Layer_Order()
			# if so reaquire the imbeded information
			if check:
				layers = self.imbeded_data_layer_order
				icons  = self.imbeded_data_layer_icons
			# if not then just use the layers as is
			else:
				layers = self._nuke_node.layers
				
		if len(layers) != len(self._nuke_node.layers):
			nuke_node_layers = self._nuke_node.layers
			for layer in nuke_node_layers:
				if not layer in layers:
					layers.insert(0, layer)
					
			for layer in layers:
				if not layer in nuke_node_layers:
					layers.remove(layer)
			
		# iterate over each layer and create an item for it
		for layer in layers:
			item = DML_PYQT.QListWidgetItem(layer,self)
			item.setFlags(DML_PYQT.Qt.ItemFlag.ItemIsSelectable|DML_PYQT.Qt.ItemFlag.ItemIsEnabled)
			# check if this layer has an icon
			if layer in icons:
				decoded_pixmap = icons[layer]
				pixmap = DML_PYQT.QPixmap()
				pixmap.loadFromData(decoded_pixmap)
				icon = DML_PYQT.QIcon(pixmap)
				item.setIcon(icon)
	#----------------------------------------------------------------------
	def set_Layer_Data_From_Master_Layer_Order(self):
		""""""
		match = self._nuke_node.find_Upstream_Node("DML_Master_Layer_Order")
		if match is not None:
			if not match.name == self._nuke_node.name:
				knob = match.knob("dml_master_layer_order")
				if not knob == None:
					layer_order_knob = match.knob("DML_Layer_Order_layers")
					layer_icons_knob = match.knob("DML_Layer_Order_Layer_Icons")
					if layer_order_knob != None and layer_icons_knob != None:
						layers = eval(layer_order_knob.getText())
						icons  = eval(layer_icons_knob.getText())
						
						nuke_node_layers = self._nuke_node.layers
						nuke_node_icons  = self.imbeded_data_layer_icons
						
						for icon in nuke_node_icons:
							if not icon in icons:
								icons[icon] = nuke_node_icons[icon]
								
						for layer in nuke_node_layers:
							if not layer in layers:
								layers.insert(0, layer)
								
						for layer in layers:
							if not layer in nuke_node_layers:
								layers.remove(layer)
						
						self.imbeded_data_layer_order = layers
						self.imbeded_data_layer_icons = icons
						return True
		return False
	#----------------------------------------------------------------------
	def sync_To_Master_Layer_Order(self):
		""""""
		if self.set_Layer_Data_From_Master_Layer_Order():
			self.rebuild_Items()
	#----------------------------------------------------------------------
	def _update_Imbeded_Data_Layer_Order(self):
		""""""
		data = []
		for index in range(self.count()):
			item = self.item(index)
			data.append(item.text())
		self.imbeded_data_layer_order = data
	#----------------------------------------------------------------------
	def get_Layer_Names(self):
		""""""
		data = []
		for index in range(self.count()):
			item = self.item(index)
			data.append(item.text())
		return data
	#----------------------------------------------------------------------
	def move_Selected_Up(self):
		"""Move The Currently Selcted Item Up One Item"""
		# get the current QModelIndex 
		current_index = self.currentIndex()
		# Make Sure The Index Is Valid If Not Then Nothing was selected
		if current_index.isValid():
			# Get the Row For The Current Index
			current_row = current_index.row()
			# Check if the row is not the item at the very top
			if current_row != 0:
				# take the item at the row index
				current_item = self.takeItem(current_row)
				# insert the item at the row it was was subtarct 1
				self.insertItem(current_row-1,current_item)
				# make the item the current selected so that the user can keep moveing it easly
				self.setCurrentItem(current_item)
				# emit a notification that an item has moved
				self._update_Imbeded_Data_Layer_Order()
	#----------------------------------------------------------------------
	def move_Selected_Down(self):
		"""Move The Currently Selcted Item Down One Item"""
		# get the current QModelIndex 
		current_index = self.currentIndex()
		# Make Sure The Index Is Valid If Not Then Nothing was selected
		if current_index.isValid():
			# Get the Row For The Current Index
			current_row = current_index.row()
			# Check if the row is not the item at the very bottom
			if current_row != self.count():
				# take the item at the row index
				current_item = self.takeItem(current_row)
				# insert the item at the row it was was plus 1
				self.insertItem(current_row+1,current_item)
				# make the item the current selected so that the user can keep moveing it easly
				self.setCurrentItem(current_item)
				# emit a notification that an item has moved
				self._update_Imbeded_Data_Layer_Order()
	#----------------------------------------------------------------------
	def hideEvent(self,event):
		""""""
		self._update_Imbeded_Data_Layer_Order()
		super(DML_Nuke_Layer_Order_List_Widget, self).hideEvent(event)
	#----------------------------------------------------------------------
	def showEvent(self,event):
		""""""
		self.rebuild_Items()
		super(DML_Nuke_Layer_Order_List_Widget, self).showEvent(event)
Python_Custom_Widget_Knob.Default_Ui_Loader.registerCustomWidget(DML_Nuke_Layer_Order_List_Widget)

########################################################################
class Layer_Order_UI(DML_PYQT.QWidget):
	def __init__(self,parent=None):
		DML_PYQT.QWidget.__init__(self,parent=parent)
		# sort the nuke nuke node that this QWidget is invavled with
		self._nuke_node = dml.to_DML_Node(nuke.thisNode())
			
		# build a layout to hold the widget that gets created from ui file that get dinamicly built
		master_Layout = DML_PYQT.QVBoxLayout(self)
		master_Layout.setSpacing(0)
		master_Layout.setContentsMargins(0, 0, 0, 0)
		# read in create the ui file
		file_wig = Python_Custom_Widget_Knob.Default_Ui_Loader.load(os.path.join(os.path.dirname(__file__),"Layer_Order.ui"),parent=self)
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
			self.channel_layers_list      = DML_Nuke_Layer_Order_List_Widget()
			self.move_layer_down_button   = DML_PYQT.QPushButton() 
			self.move_layer_up_button     = DML_PYQT.QPushButton()
			self.build_icons_button       = DML_PYQT.QPushButton()
			self.BNT_Set_To_Active_Viewer = DML_PYQT.QPushButton()
			self.BNT_Sync_To_Master       = DML_PYQT.QPushButton()
			self.CBBX_Icon_Size           = DML_PYQT.QComboBox()
			self.PGSB_Icon_builder_Layer_Progress  = DML_PYQT.QProgressBar()
			self.PGSB_Icon_builder_Total_Progress  = DML_PYQT.QProgressBar()
			
		DML_PYQT.QMetaObject.connectSlotsByName(self)
		self.build_icons_button.clicked.connect(self.build_Icons)
		self.move_layer_down_button.clicked.connect(self.channel_layers_list.move_Selected_Down)
		self.move_layer_up_button.clicked.connect(self.channel_layers_list.move_Selected_Up)
		self.BNT_Sync_To_Master.clicked.connect(self.channel_layers_list.sync_To_Master_Layer_Order)
	#----------------------------------------------------------------------
	def _rebuild(self):
		""""""
		self.channel_layers_list = self.findChild(DML_PYQT.QListWidget,"channel_layers_list")
		self.CBBX_Icon_Size      = self.findChild(DML_PYQT.QComboBox,"CBBX_Icon_Size")
		self.PGSB_Icon_builder_Layer_Progress = self.findChild(DML_PYQT.QProgressBar,"PGSB_Icon_builder_Layer_Progress")
		self.PGSB_Icon_builder_Total_Progress = self.findChild(DML_PYQT.QProgressBar,"PGSB_Icon_builder_Total_Progress")
		self.PGSB_Icon_builder_Layer_Progress.setVisible(False)
		self.PGSB_Icon_builder_Total_Progress.setVisible(False)
	#----------------------------------------------------------------------
	def build_Icons(self):
		""""""
		layer_count = self.channel_layers_list.count()
		
		self.PGSB_Icon_builder_Total_Progress.setMaximum(layer_count)
		self.PGSB_Icon_builder_Total_Progress.setValue(0)
		self.PGSB_Icon_builder_Layer_Progress.setValue(0)
		
		self.PGSB_Icon_builder_Layer_Progress.setVisible(True)
		self.PGSB_Icon_builder_Total_Progress.setVisible(True)
		icon_size = int(self.CBBX_Icon_Size.currentText())
		icon_data = dict()
		self.channel_layers_list.setIconSize(DML_PYQT.QSize(icon_size,icon_size))
		for index in range(self.channel_layers_list.count()):
			item = self.channel_layers_list.item(index)
			icon,decoded_data = generate_Layer_Thumbnail(self.channel_layers_list._nuke_node, layer=item.text(), size=icon_size,prgsbar=self.PGSB_Icon_builder_Layer_Progress)
			item.setIcon(icon)
			icon_data[item.text()]=decoded_data
			self.PGSB_Icon_builder_Total_Progress.setValue(index+1)
			self.PGSB_Icon_builder_Layer_Progress.setValue(0)			
		self.channel_layers_list.imbeded_data_layer_icons = icon_data
		
		self.PGSB_Icon_builder_Layer_Progress.setVisible(False)
		self.PGSB_Icon_builder_Total_Progress.setVisible(False)
		
Python_Custom_Widget_Knob.Default_Ui_Loader.registerCustomWidget(Layer_Order_UI)