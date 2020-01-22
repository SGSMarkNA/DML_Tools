
import nuke
import DML_Tools
DML_PYQT = DML_Tools.DML_PYQT
nuke_QMainWindow_Widget = None

def get_Viewer_Widgets():
	Viewers = []
	for wig in DML_PYQT.qApp.allWidgets():
		if len(wig.objectName()):
			if wig.objectName().startswith("Viewer"):
				Viewers.append(wig)
	return Viewers

def get_Viewer_StereoControl_Widgets():
	res = []
	for wig in DML_PYQT.qApp.allWidgets():
		if len(wig.objectName()):
			if wig.objectName().startswith("StereoControls"):
				res.append(wig)
	return res

def get_Nuke_QMainWindow_Widget():
	main_menu = nuke.menu("Nuke")
	menu_item = main_menu.findItem("File")
	action    = menu_item.action()
	menubar   = action.associatedWidgets()[0]
	wig       = menubar.parent()
	if isinstance(wig,DML_PYQT.QMainWindow):
		nuke_QMainWindow_Widget = wig
	else:
		nuke_QMainWindow_Widget = wig.findChild(DML_PYQT.QMainWindow).parent()
	return nuke_QMainWindow_Widget

class WidgetHierarchyTree(DML_PYQT.QTreeView):
	def __init__(self, rootWidget=None,includeAction=True, *args, **kwargs):
		super(WidgetHierarchyTree, self).__init__(*args, **kwargs)

		# Destroy this widget when closed.  Otherwise it will stay around
		self.setAttribute(DML_PYQT.Qt.WA_DeleteOnClose, True)

		# Determine root widget to scan
		if rootWidget != None:
			self.rootWidget = rootWidget
		else:
			self.rootWidget = get_Nuke_QMainWindow_Widget()
		self._ignored_type = (DML_PYQT.QLayout)
		if includeAction:
			self._ignored_type = (DML_PYQT.QLayout,DML_PYQT.QAction)
		# Create the headers
		self.columnHeaders = ['Class', 'ObjectName', "Text", 'Children']
		self.myModel = DML_PYQT.QStandardItemModel(0,len(self.columnHeaders))
		for col,colName in enumerate(self.columnHeaders):
			self.myModel.setHeaderData(col, DML_PYQT.Qt.Horizontal, colName)
		self.setModel( self.myModel )
		self.populateModel()


	def populateModel(self):
		# Recurse through child widgets
		parentItem = self.myModel.invisibleRootItem();
		self.populateModel_recurseChildren(parentItem, self.rootWidget)

	def populateModel_recurseChildren(self, parentItem, widget):
		# Construct the item data and append the row
		if not isinstance(widget,self._ignored_type):
			classNameStr = str(widget.__class__).split("'")[1]
			classNameStr = classNameStr.replace('PySide.','').replace('QtGui.', '').replace('QtCore.', '').replace('PySide2.','').replace('QtGui.', '').replace('QtCore.', '').replace('QtWidgets.', '')
			class_name_item = DML_PYQT.QStandardItem(classNameStr)
			object_name_item = DML_PYQT.QStandardItem(widget.objectName())
			objText = ""
			icon = DML_PYQT.QIcon()
			class_name_item.setData(widget,DML_PYQT.Qt.ItemDataRole.UserRole)
			if hasattr(widget,"text"):
				objText = widget.text()
			if hasattr(widget,"icon"):
				if widget.icon():
					icon = widget.icon()
			info_item = DML_PYQT.QStandardItem(icon,objText)
			items = [class_name_item, 
			         object_name_item,
			         info_item,
			         DML_PYQT.QStandardItem(str(len(widget.children()))),
			         ]
			parentItem.appendRow(items)

			# Recurse children and perform the same action
			for childWidget in widget.children():
				self.populateModel_recurseChildren(items[0], childWidget)


#----------------------------------------------------------------------
def show_WidgetHierarchyTree(rootWidget=None,includeAction=False):
	ui = WidgetHierarchyTree(rootWidget=rootWidget,includeAction=includeAction)
	ui.show()
	return ui
#----------------------------------------------------------------------
def remove_Tab(node,tab_knob_name):
	"""
	addUserKnob {20 Tab_A l "Tab A"}
	addUserKnob {3 a_number l "A Number"} a_number
	addUserKnob {6 a_check_box l "A Check Box" +STARTLINE} a_check_box
	addUserKnob {20 Tab_B l "Tab B"}
	addUserKnob {3 other_number l "Other Number"} other_number
	"""
	tab_knob = node.knob(tab_knob_name)
	# Make Sure That This Knob Is Attached To A Node
	if node is not None:
		# Make A Variable That Will Tell The Code To Start Looking For The End Of This Tab
		# By Looking For The Next Tab Knob
		in_collection = False
		# Holds The Name Of Tab Knob That Comes After This Tab Knob
		end_tab_name = None
		# Holds The knobs that are associated with this tab
		knb_collection = []
		# Scan Each Line Of User Knobs On The Attaced Node
		for line in node.writeKnobs(nuke.WRITE_USER_KNOB_DEFS).splitlines():
			if len(line):
				if line.startswith("addUserKnob"):
					# Get The Knob Type Number
					user_knob_type = line.split()[1].replace("{","")
					# Get The Knob Name
					line_tab_name  = line.split()[2].replace("}","")
					# Check If We Have Not Found This Tab Knob Yet
					if not in_collection:
						# If Not Check if The Knob Type Is a tab and not a tab group
						if user_knob_type == '20' and not "n 1}" in line and not "n -1}" in line:
							# now check if the name matches this tab
							if line_tab_name == tab_knob.name:
								# We Are Now In This Tab Knob
								in_collection=True
					else:
						# If So Check if The Knob Type Is a tab and not a tab group
						if user_knob_type == '20' and not "n 1}" in line and not "n -1}" in line:
							# If So Then Mark it and stop this scan
							end_tab_name = line_tab_name
							break
				
		# Reset 
		in_collection = False
		# Scan Through All The Knobs On The Attached Node
		for knb in node.allKnobs():
			if knb.Class() == "Tab_Knob" and knb.name() == tab_knob.name:
				in_collection = True
				knb_collection.append(knb)
			elif in_collection:
				if knb.Class() == "Tab_Knob" and knb.name() == end_tab_name:
					in_collection = False
					break
				else:
					knb_collection.append(knb)

		for knb in reversed(knb_collection):
			node.removeKnob(knb)