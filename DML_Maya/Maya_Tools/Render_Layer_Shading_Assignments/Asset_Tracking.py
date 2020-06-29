
_Shader_Material_Attribute_Tracking_Name = "AW_Material_Tracking_ID"
_Geo_Node_Attribute_Tracking_Name        = "AW_Geo_Tracking_ID"


_Global_UID_TO_MAYA_NODE_DICT = dict()
_GLOBAL_UID_TO_VRAY_SWITCH_MATERIAL_DICT = dict()

#----------------------------------------------------------------------
def add_Geo_Tracking_ID(self,node):
	""""""
	if not node.attributeExists(_Geo_Node_Attribute_Tracking_Name):
		node.addAttr(_Geo_Node_Attribute_Tracking_Name,dataType="string")
		getattr(node,_Geo_Node_Attribute_Tracking_Name).value = self.node.uuid
		
#----------------------------------------------------------------------
def add_Material_Tracking_ID(node,uid=None):
	""""""
	if not node.attributeExists(_Shader_Material_Attribute_Tracking_Name):
		node.addAttr(_Shader_Material_Attribute_Tracking_Name,dataType="string")
		if uid == None:			
			getattr(node,_Shader_Material_Attribute_Tracking_Name).value = node.uuid
		else:
			getattr(node,_Shader_Material_Attribute_Tracking_Name).value = uid
		
def rebuild_Global_Tracking_Data(maya_cmds,dml_maya):
	""""""
	global _Global_UID_TO_MAYA_NODE_DICT,_GLOBAL_UID_TO_VRAY_SWITCH_MATERIAL_DICT
	_Global_UID_TO_MAYA_NODE_DICT = dict()
	_GLOBAL_UID_TO_VRAY_SWITCH_MATERIAL_DICT = {}
	
	geo_node_plugs      = maya_cmds.ls("*.{}".format(_Geo_Node_Attribute_Tracking_Name))
	material_node_plugs = [plug for plug in maya_cmds.ls("*.{}".format(_Shader_Material_Attribute_Tracking_Name)) if maya_cmds.objectType( plug.split(".")[0] ,isType="VRaySwitchMtl") ]
	
	count = len(geo_node_plugs) + len(material_node_plugs)
	try:
		maya_cmds.progressWindow(endProgress=1)
	except:
		pass
	maya_cmds.progressWindow(title="Rebuilding IDS",progress=0, maxValue = count, status="Doing Stuff", isInterruptable=False)
	
	for plug in geo_node_plugs:
		plug = dml_maya.dml.to_DML_Node(plug)
		maya_cmds.progressWindow( edit=True, step=1)
		_Global_UID_TO_MAYA_NODE_DICT[plug.value]=plug.node
	for plug in material_node_plugs:
		plug = dml_maya.dml.to_DML_Node(plug)
		maya_cmds.progressWindow( edit=True, step=1)
		_GLOBAL_UID_TO_VRAY_SWITCH_MATERIAL_DICT[plug.value]=plug.node
	maya_cmds.progressWindow(endProgress=1)