
import json
import os
import sys
import functools
import Asset_Tracking
try:
	import maya.cmds as cmds
	import DML_Tools.DML_Maya as DML_Maya
	maya_active = 1
except:
	maya_active = 0

#----------------------------------------------------------------------
def maya_Acitve_Return_Wrapper(func):
	''''''
	@functools.wraps(func)
	def wrapper(*args, **kws):
		err = None
		if maya_active:
			try:
				res = func(*args, **kws)
			except Exception, error:
				err=error
			finally:
				if err:
					traceback = sys.exc_info()[2]  # get the full traceback
					raise Exception(err, traceback)
				return res
		else:
			return None
	return wrapper

_Global_UID_TO_MAYA_NODE_DICT = dict()
_GLOBAL_UID_TO_VRAY_SWITCH_MATERIAL_DICT = dict()

########################################################################
class Switch_Option(object):
	""""""
	def __init__(self,name="",index=0):
		"""Constructor"""
		self.name    = name
		self.index   = index
	#----------------------------------------------------------------------
	def toJson(self):
		""""""
		return dict(name=self.name,index=self.index)
		
	
########################################################################
class Geo_Node(object):
	""""""
	def __init__(self,name="",uid="",objData=None):
		"""Constructor"""
		self._node = None
		if isinstance(objData,dict):
			if not "name" in objData or not "uid" in objData:
				raise KeyError("input objData Does not contain a name or uid key")
			else:
				self.name = objData.get("name")
				self.uid  = objData.get("uid")
		else:
			self.name      = str(name)
			self.uid       = str(uid)
		if False:
			isinstance(self.node,DML_Maya.Maya_Nodes.Dag_Node)
	#----------------------------------------------------------------------
	@property
	@maya_Acitve_Return_Wrapper
	def node(self):
		""""""
		if self._node == None:
			self._node = Asset_Tracking._Global_UID_TO_MAYA_NODE_DICT[self.uid]
		return self._node
	#----------------------------------------------------------------------
	def toJson(self):
		""""""
		return dict(name=self.name,uid=self.uid)

########################################################################
class Geo_Collection(list):
	""""""
	def __init__(self,nodes=[]):
		"""Constructor"""
		#input_mode = []
		super(Geo_Collection,self).__init__(nodes)
	#----------------------------------------------------------------------
	def toJson(self):
		""""""
		return [node.toJson() for node in self]
		
########################################################################
class Shader_Pattern(object):
	""""""
	def __init__(self,pattern="",objData=None):
		"""Constructor"""
		if isinstance(objData,dict):
			if not "pattern" in objData:
				raise KeyError("input objData Does not contain a pattern key")
			else:
				self.pattern = objData.get("pattern")
		else:
			self.pattern      = pattern
	#----------------------------------------------------------------------
	def set_Pattern(self,pattern):
		""""""
		self._pattern = pattern
		self._unique_shader_names = []
		for shader_name in self._pattern.split(","):
			if not shader_name in self._unique_shader_names:
				self._unique_shader_names.append(shader_name)
	#----------------------------------------------------------------------
	def get_Pattern(self):
		""""""
		return self._pattern
	
	pattern = property(get_Pattern,set_Pattern)
	
	@property
	#----------------------------------------------------------------------
	def shader_names(self):
		""""""
		return self._pattern.split(",")
	
	@property
	#----------------------------------------------------------------------
	def unique_shader_names(self):
		""""""
		return self._unique_shader_names

	@property
	@maya_Acitve_Return_Wrapper
	#----------------------------------------------------------------------
	def unique_shader_nodes(self):
		""""""
		return DML_Maya.dml.to_DML_Nodes(self.unique_shader_names)
	@property
	@maya_Acitve_Return_Wrapper
	#----------------------------------------------------------------------
	def shader_nodes(self):
		""""""
		return DML_Maya.dml.to_DML_Nodes(self.shader_names)
	#----------------------------------------------------------------------
	def toJson(self):
		""""""
		return dict(pattern=self.pattern)
		
########################################################################
class Shader_Switch(object):
	""""""
	def __init__(self,shaderPattern=None,geoNodes=None,uid="",objData=None):
		"""Constructor"""
		self._node = None
		if isinstance(objData,dict):
			if not "shaderPattern" in objData or not "geoNodes" in objData or not "uid" in objData:
				raise KeyError("input objData Does not contain a shaderPattern or geoNodes or uid key")
			else:
				shaderPattern = Shader_Pattern(objData=objData.get("shaderPattern"))
				geoNodes      = Geo_Collection(nodes=[Geo_Node(objData=data) for data in objData["geoNodes"]])
				uid           = objData.get("uid")
		if not isinstance(shaderPattern,Shader_Pattern):
			raise ValueError("shaderPattern input must be an instances of Shader_Pattern")
		
		if not isinstance(geoNodes,list):
			raise ValueError("geoNodes input must be an list of Geo_Node_Data")
		
		self.shader_pattern = shaderPattern
		self.geoNodes       = geoNodes
		self.uid            = uid
		if False:
			isinstance(self.node,DML_Maya.Maya_Nodes.VRaySwitchMtl)
	#----------------------------------------------------------------------
	@property
	@maya_Acitve_Return_Wrapper
	def node(self):
		""""""
		if self._node == None:
			self._node = Asset_Tracking._GLOBAL_UID_TO_VRAY_SWITCH_MATERIAL_DICT[self.shader_pattern]
		return self._node
	#----------------------------------------------------------------------
	def create_VRay_Switch_Material(self):
		""""""
		if not self.uid in Asset_Tracking._GLOBAL_UID_TO_VRAY_SWITCH_MATERIAL_DICT or self.uid == None:
			vray_switch_material = DML_Maya.Maya_Nodes.VRaySwitchMtl(name="sw_"+"_".join(self.shader_pattern.shader_names));
			self.uid = vray_switch_material.uuid
			Asset_Tracking._GLOBAL_UID_TO_VRAY_SWITCH_MATERIAL_DICT[self.uid]=vray_switch_material
			for index,material in enumerate(self.shader_pattern.shader_names):
				if not cmds.objExists(material):
					material = "DML_Created_Shader:"+material
				vray_switch_material.Attach_Material(material,index)
				members = [geo.node for geo in self.geoNodes]
				cmds.sets(members, edit=True, forceElement=vray_switch_material.shading_engine()[0])
	#----------------------------------------------------------------------
	def toJson(self):
		""""""
		res = dict(shaderPattern=self.shader_pattern.toJson(),geoNodes=self.geoNodes.toJson(),uid=self.uid)
		return res

########################################################################
class Switchs(object):
	""""""
	def __init__(self,shaderSwitches=[],objData=None):
		"""Constructor"""
		if isinstance(objData,list):
			shaderSwitches = [Shader_Switch(objData=data) for data in objData]
		self.shader_switches = shaderSwitches
	#----------------------------------------------------------------------
	@maya_Acitve_Return_Wrapper
	def create_Non_Existing_Shaders(self):
		""""""
		namespace = "DML_Created_Shader"
		try:
			cmds.namespace( addNamespace=namespace)
		except RuntimeError:
			pass
		for switch_shader in self.shader_switches:
			for shader in switch_shader.shader_pattern.shader_names:
				if not cmds.objExists(shader):
					shader = namespace+":"+shader
					if not cmds.objExists(shader):
						DML_Maya.Maya_Nodes.Shading_Node("lambert",name=shader)
	#----------------------------------------------------------------------
	def create_VRay_Switch_Materials(self):
		""""""
		for shader_switch in self.shader_switches:
			shader_switch.create_VRay_Switch_Material()
	#----------------------------------------------------------------------
	def toJson(self):
		""""""
		return [switch.toJson() for switch in self.shader_switches]

########################################################################
class Switch_Shader_Master_Control(object):
	""""""
	def __init__(self,switches=None,options=[],objData=None):
		"""Constructor"""
		if isinstance(objData,dict):
			if not "switches" in objData or not "options" in objData:
				raise KeyError("input objData Does not contain a switches or options key")
			else:
				switches = Switchs(objData=objData["switches"])
				options = [Switch_Option(name=option["name"], index=option["index"]) for option in objData["options"]]
		if not isinstance(switches,Switchs):
			raise ValueError("shaderPattern input must be an instances of Shader_Pattern")
		
		self.switches = switches
		self.options  = options
	#----------------------------------------------------------------------
	def apply_Option(self,value):
		""""""
		if maya_active:
			
			option = None
			for option_item in self.options:
				if isinstance(value,str) and option_item.name == value:
					option=option_item
					break
				elif isinstance(value,int) and option_item.index == value:
					option=option_item
					break
			if not option == None:
				for switch in self.switches.shader_switches:
					isinstance(switch,Shader_Switch)
					switch.node.set_Switch_Index(option.index)
	#----------------------------------------------------------------------
	def toJson(self):
		""""""
		options = [opt.toJson() for opt in self.options]
		return dict(switches=self.switches.toJson(),options=options)
########################################################################
class Shader_Switch_Data_Encoder(json.JSONEncoder):
	def __init__(self, skipkeys=False, ensure_ascii=True,check_circular=True, allow_nan=True, sort_keys=False,indent=8, separators=None, encoding='utf-8', default=None):
		super(Shader_Switch_Data_Encoder, self).__init__(skipkeys, ensure_ascii,check_circular, allow_nan, sort_keys,indent, separators, encoding, default)

	def default(self, asset):
		if hasattr(asset, "toJson"):
			return asset.toJson()
		return super(Shader_Switch_Data_Encoder, self).default(asset)
    
########################################################################
class Shader_Switch_Data_Decoder(json.JSONDecoder):
	def __init__(self, encoding=None, parse_float=None, parse_int=None, parse_constant=None, strict=True):
		super(Shader_Switch_Data_Decoder, self).__init__(encoding=encoding, parse_float=parse_float, parse_int=parse_int, parse_constant=parse_constant, object_hook=self.object_hook, strict=strict)
		
	def object_hook(self, obj):
		if "switches" in obj and "options" in obj:
			return Switch_Shader_Master_Control(objData=obj)
		return obj
	
shader_Switch_Encoder = Shader_Switch_Data_Encoder()
shader_Switch_Decoder = Shader_Switch_Data_Decoder()

#----------------------------------------------------------------------
def Encode_Temp_File(switch_data):
	""""""
	Json_File_Path = os.path.join(os.environ["TEMP"],'shader_switch_build_data.json')
	with file(Json_File_Path, "w") as f:
			json_out = shader_Switch_Encoder.encode(switch_data)
			f.write(json_out)

#----------------------------------------------------------------------
def Decode_Temp_File():
	""""""
	Json_File_Path    = os.path.join(os.environ["TEMP"],'shader_switch_build_data.json')
	
	with file(Json_File_Path, "r") as f:
		data = shader_Switch_Decoder.decode(f.read())
	if maya_active:
		Asset_Tracking.rebuild_Global_Tracking_Data(cmds,DML_Maya)
	return data

#----------------------------------------------------------------------
def Encode_Location_File(switch_data,fp):
	""""""
	Json_File_Path = os.path.join(os.environ["TEMP"],'shader_switch_build_data.json')
	with file(fp, "w") as f:
			json_out = shader_Switch_Encoder.encode(switch_data)
			f.write(json_out)

#----------------------------------------------------------------------
def Decode_Location_File(fp):
	""""""
	with file(fp, "r") as f:
		data = shader_Switch_Decoder.decode(f.read())
	if maya_active:
		Asset_Tracking.rebuild_Global_Tracking_Data(cmds,DML_Maya)
	return data