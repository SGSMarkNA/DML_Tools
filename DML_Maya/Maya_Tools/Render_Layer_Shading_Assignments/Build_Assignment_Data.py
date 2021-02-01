
import maya.cmds as cmds
#import uuid
import DML_Tools.DML_Maya as DML_Maya
import Shader_Switch_Data

cmds.loadPlugin("vrayformaya",qt=True)
if not cmds.pluginInfo("vrayformaya",q=True,loaded=True):
	raise LookupError("vrayformaya Could Not Be Loaded")

check_If_AW_Shader_Switch_ID_Exists                   = lambda node:cmds.attributeQuery( "AW_Shader_Switch_ID", node=node, exists=True )
add_AW_Shader_Switch_ID                               = lambda node:cmds.addAttr(node, longName="AW_Shader_Switch_ID",attributeType="long")
get_AW_Shader_Switch_ID                               = lambda node:cmds.getAttr(node+".AW_Shader_Switch_ID")
set_AW_Shader_Switch_ID                               = lambda node,val:cmds.setAttr(node+".AW_Shader_Switch_ID", val)

_Geo_Node_Attribute_Tracking_Name = "AW_Geo_Tracking_ID"

########################################################################
class Geo_Node(object):
	""""""
	def __init__(self,name):
		"""Constructor"""
		self.node = name
		self.uid  = cmds.ls(self.node,uuid=True)[0]
	#----------------------------------------------------------------------
	def get_Assigned_Shader_Engine(self):
		""""""
		res = cmds.listConnections(self.node,t="shadingEngine")
		if res == None:
			raise LookupError("The input Geo {} Is Not Connected To A Shader Engine".format(self.node.name))
		if res == "":
			raise LookupError("The input Geo {} Is Not Connected To A Shader Engine".format(self.node.name))
		if len(res):
			res = res[0]
			res = cmds.listConnections(res+".surfaceShader")[0]
			return res
		else:
			raise LookupError("The input Geo {} Is Not Connected To A Shader Engine".format(self.node.name))
	#----------------------------------------------------------------------
	def add_Geo_Tracking_ID(self):
		""""""
		if not cmds.attributeQuery(_Geo_Node_Attribute_Tracking_Name,exists=True, node=self.node):
			cmds.addAttr(self.node,dataType="string", longName=_Geo_Node_Attribute_Tracking_Name, shortName="AWGTD")
			cmds.setAttr(self.node+"."+_Geo_Node_Attribute_Tracking_Name,self.uid,typ="string")

#----------------------------------------------------------------------
def collect_Render_Layers_Geo_Switch_Data():
	tracked_geo      = []
	tracked_geo_dict = dict()
	switch_options   = []
	#render_layers    = [layer for layer in cmds.ls(type="renderLayer") if not layer == "defaultRenderLayer"]
	render_layers    = list(reversed([layer for layer in cmds.listConnections("renderLayerManager.renderLayerId") if not layer.startswith("defaultRenderLayer")]))
	
	all_geo_nodes = cmds.ls(typ=["mesh","nurbsSurface"],noIntermediate=True)
	for geo_node in all_geo_nodes:
		geo_node = Geo_Node(geo_node)
		geo_node.add_Geo_Tracking_ID()
		tracked_geo.append(geo_node)
	
	for index,render_layer in enumerate(render_layers):
		option = Shader_Switch_Data.Switch_Option(name=render_layer, index=index)
		switch_options.append(option)
		
	count = len(tracked_geo) * len(switch_options)
	if count:
		cmds.progressWindow(title="Applying State To Layer",progress=0, maxValue = count, status="Smile", isInterruptable=False)
		try:
			for option in switch_options:
				cmds.editRenderLayerGlobals( currentRenderLayer=option.name)
				for geo in tracked_geo:
					isinstance(geo,Geo_Node)
					if not geo in tracked_geo_dict:
						tracked_geo_dict[geo]=[]
					cmds.progressWindow( edit=True, step=1)
					try:
						if geo in tracked_geo_dict:
							sg = geo.get_Assigned_Shader_Engine()
							tracked_geo_dict[geo].append(sg)
					except LookupError:
						pass
		except:
			print "Error"
		finally:
			cmds.progressWindow(endProgress=1)
			
		for key in dict(tracked_geo_dict):
			sgs = list(set(tracked_geo_dict[key]))
			if len(sgs) == 1:
				del tracked_geo_dict[key]
				
		unique_lists = dict()
		
		for key in tracked_geo_dict:
			shaders = tracked_geo_dict[key]
			pattern =  ",".join([shader for shader in shaders])
			if not pattern in unique_lists.keys():
				unique_lists[pattern] = []
			unique_lists[pattern].append(key)
					
		switch_data = Shader_Switch_Data.Switchs()
		
		for pattern in unique_lists:
			pattern_data  = Shader_Switch_Data.Shader_Pattern(pattern=pattern)
			geo_nodes     = Shader_Switch_Data.Geo_Collection([Shader_Switch_Data.Geo_Node(name=geo.node.split("|")[0], uid=geo.uid) for geo in unique_lists.get(pattern)])
			shader_switch = Shader_Switch_Data.Shader_Switch(shaderPattern=pattern_data, geoNodes=geo_nodes)
			
			switch_data.shader_switches.append(shader_switch)
			
		master_ctrl = Shader_Switch_Data.Switch_Shader_Master_Control(switches=switch_data, options=switch_options)
		Shader_Switch_Data.Encode_Temp_File(master_ctrl)
		return master_ctrl

#----------------------------------------------------------------------
def Apply_Switch_Data():
	""""""
	new_data = Shader_Switch_Data.Decode_Temp_File()
	new_data.switches.create_Non_Existing_Shaders()
	new_data.switches.create_VRay_Switch_Materials()
	for sdswch in new_data.switches.shader_switches:
		shaders = sdswch.shader_pattern.pattern.split(",")
		switch  = "sw_"+"_".join(shaders)
		if not cmds.objExists(switch):
			scan = cmds.ls("*:"+switch)
			if len(scan) == 1:
				switch = scan[0]
				
		if cmds.objExists(switch):
			switch  = DML_Maya.dml.to_DML_Node(switch)
			members = [geo.node for geo in sdswch.geoNodes]
			cmds.sets(members, edit=True, forceElement=switch.shading_engine()[0])
		else:
			print "obect did not exits {}".format(switch)