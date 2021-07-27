from __future__ import print_function
import DML_Tools.DML_PYQT as PYQT
import DML_Tools.DML_Maya as DML_Maya
import maya.cmds as cmds
import mayaMixin
import Main_Window

################ Maya Functions
#----------------------------------------------------------------------
def get_Shaders_In_Namespace(nameSpace):
	""""""
	def flatten(x):
		result = []
		for el in x:
			if hasattr(el, "__iter__") and not isinstance(el, basestring):
				result.extend(flatten(el))
			else:
				result.append(el)
		return result
	
	shader_engine_names = [sg for sg in cmds.ls(typ="shadingEngine") if not sg.startswith("initial")]
	shader_names = list(set(flatten([cmds.listConnections(sg+".surfaceShader") for sg in shader_engine_names])))
	shader_names = [str(shader_name) for shader_name in shader_names]
	if len(nameSpace):
		nameSpace = nameSpace+":"
		shader_names = sorted([shader_name for shader_name in shader_names if nameSpace in shader_name])
	else:
		shader_names = sorted([shader_name for shader_name in shader_names if not ":" in shader_name])
	return shader_names
	
#----------------------------------------------------------------------
def replace_Shader(shaderToReplace,shaderToUse):
	""""""
	isinstance(shaderToReplace,DML_Maya.Maya_Nodes.Shading_Node)
	isinstance(shaderToUse,DML_Maya.Maya_Nodes.Shading_Node)
	shaderToReplace_name = shaderToReplace.name
	shaderToReplace.rename(shaderToReplace_name+"_Replaced")
	newShader = shaderToUse.duplicate_upstreamNodes(name=shaderToReplace_name,singleReturn=True)
	newShader.addAttr("AwOriginalShaderName",dataType="string").value = shaderToUse.nice_name
	isinstance(newShader,DML_Maya.Maya_Nodes.Shading_Node)
	sg = shaderToReplace.shading_engine()
	if not sg == None:
		sg = DML_Maya.Maya_Nodes.Shading_Engine(name=newShader.nice_name + "SG")
	else:
		sg.rename(newShader.nice_name + "SG")
	sg.Assine_To_Material(newShader)
	
	vray_switch_mtl_check = shaderToReplace.listConnections(s=False,d=True,p=True,type="VRaySwitchMtl")
	
	if len(vray_switch_mtl_check):
		for plg in vray_switch_mtl_check:
			newShader.outColor.connect(plg)
	
	ignored_nodes = cmds.ls( undeletable=True, defaultNodes=True)
	cleanup_nodes = [shaderToReplace]+[node for node in shaderToReplace.listSourceConnectionsRecursively() if not node in ignored_nodes]
	if len(cleanup_nodes):
		cmds.delete(cleanup_nodes)

#----------------------------------------------------------------------
def find_Shader_Within_Namespaces(name,namespaces=[]):
	""""""
	for ns in namespaces:
		scan = cmds.ls("{}:{}".format(ns,name))
		if len(scan):
			res = DML_Maya.dml.to_DML_Node(scan[0])
			isinstance(res,DML_Maya.Maya_Nodes.Shading_Node)
			return res

########################################################################
class Name_Associations_Main_Window(mayaMixin.MayaQWidgetBaseMixin,Main_Window.Name_Associations_Main_Window):
	""""""
	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		super(Name_Associations_Main_Window,self).__init__()
	#----------------------------------------------------------------------
	def _run_init(self):
		""""""
		super(Name_Associations_Main_Window, self)._run_init()
		self.Lookup_Name_Space_Scan_Button.clicked.connect(self.Run_Name_Space_Scan_For_Names)
		self.Association_Name_Space_Scan_Button.clicked.connect(self.Run_Name_Space_Scan_For_Associations)
		self.Name_Space_Scanning_Frame.setHidden(False)
		self.Add_Association_Widget.setHidden(True)
		self.Add_Name_Widget.setHidden(True)
		self.Add_Remove_Names_Frame.setHidden(True)
		
	#----------------------------------------------------------------------
	def showEvent(self,event):
		""""""
		for child in self.findChildren(PYQT.QWidget):
			if not child.objectName() == "":
				setattr(self,child.objectName(),child)
	#----------------------------------------------------------------------
	def Run_Name_Space_Scan_For_Names(self):
		""""""
		text_val = self.Names_Name_Space_Input.text()
		if len(text_val):
			names = [name.strip() for name in text_val.split(",")]
			shaders_names = []
			for name in names:
				shaders_names.extend(get_Shaders_In_Namespace(name))
			shader_nice_names = [name.split(":")[-1] for name in shaders_names]
			self._internal_data.name_list._data = shader_nice_names
			self.tableWidget._rebuild_Name_List()
	#----------------------------------------------------------------------
	def Run_Name_Space_Scan_For_Associations(self):
		""""""
		text_val = self.Association_Name_Space_Input.text()
		if len(text_val):
			shaders_names = get_Shaders_In_Namespace(text_val)
			shader_nice_names = [name.split(":")[-1] for name in shaders_names]
			current_list_of_key_names = [item.text() for item in self._model_data.Get_Child_Items()]
			for nice_name in shader_nice_names:
				if not nice_name in current_list_of_key_names:
					self.Add_Key_Name(name=nice_name)
	
	#----------------------------------------------------------------------
	def Apply_Associations(self):
		""""""
		with DML_Maya.MayaUndoChunk():
			association_name_spaces = self.Association_Name_Space_Input.text().split(",")
			names_name_spaces       = self.Names_Name_Space_Input.text().split(",")
			for item in self._model_data.iterate_Names_With_Associations():
				shaderToUse = find_Shader_Within_Namespaces(item.name, namespaces=association_name_spaces)
				for shaderToReplace in item.associations:
					shaderToReplace = find_Shader_Within_Namespaces(shaderToReplace,names_name_spaces)
					replace_Shader(shaderToReplace, shaderToUse)
					
	#----------------------------------------------------------------------
	def contextMenuEvent(self, event):
		focus_wig = self.focusWidget()
		if isinstance(focus_wig,Main_Window.Custom_TableWidget):
			selectedItems = focus_wig.selectedItems()
			if len(selectedItems):
				item = selectedItems[0]
				if item.column() == 1:
					print(item.text())
					shader = find_Shader_Within_Namespaces(item.text(), namespaces=self.Names_Name_Space_Input.text().split(","))
					sg = shader.shading_engine()
					def select_shader_members():
						cmds.select(sg.members())
					def select_shader():
						shader.select()
						
					if isinstance(shader,DML_Maya.Maya_Nodes.Shading_Node):
						menu = PYQT.QMenu(self)
						action = PYQT.QAction("Select Members",menu)
						action.triggered.connect(select_shader_members)
						menu.addAction(action)
						action = PYQT.QAction("Select Shader",menu)
						action.triggered.connect(select_shader)
						menu.addAction(action)
						menu.exec_(event.globalPos())
						
		#index = self.indexAt(event.pos())
		#item  = self.item_From_Index(index)
		#menu = QT.QMenu(self)
		#menu.addAction(win.actionAdd_Part_Set)
		#menu.addAction(win.actionDelete_Parts)
		#if index.isValid():
			#if _maya_check:
				#item.contextMenuActions(menu)
		#menu.exec_(event.globalPos())
		#event.pos