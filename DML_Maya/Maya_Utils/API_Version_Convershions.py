#!/usr/bin/env python
import maya.api.OpenMaya as V2_OM
import maya.OpenMaya as V1_OM
import maya.cmds as cmds
import sys

def __simplafy_Source_Analises(item):
	new_item = item
	return new_item
########################################################################
class Error(Exception):
	"""Base class for exceptions in this module."""
	pass
########################################################################
class NothingSelectedError(Error):
	"""Exception raised When A Selection is Required But Nothing Is Selected."""
	#----------------------------------------------------------------------
	def __init__(self):
		self.message = "There Was Nothing Selected Please Select Somthing And Try Again"
########################################################################
class MObjectCreationError(Error):
	"""Exception raised When The Input Giving Could Not Be Converted To A Valid MObject."""
	#----------------------------------------------------------------------
	def __init__(self, inVal):
		self.message = "The Input Value Giving %r Could Not Be Converted To A Valid MObject" % inVal
########################################################################
class MDagPathCreationError(Error):
	"""Exception raised When The Input Giving Could Not Be Converted To A Valid MDagPath Object."""
	#----------------------------------------------------------------------
	def __init__(self, inVal):
		self.message = "The Input Value Giving %r Could Not Be Converted To A Valid MDagPath" % inVal
########################################################################
class MPlugCreationError(Error):
	"""Exception raised When The Input Giving Could Not Be Converted To A Valid MDagPath Object."""
	#----------------------------------------------------------------------
	def __init__(self, inVal):
		self.message = "The Input Value Giving %r Could Not Be Converted To A Valid MPlug" % inVal

#----------------------------------------------------------------------
def next_active_id():
	""""""
	with file(os.path.join(os.path.dirname(__file__), "Active_id.txt"), "r") as f:
		line = int(f.readline())
	with file(os.path.join(os.path.dirname(__file__), "Active_id.txt"), "w") as f:
		f.write(str(line+1))
	return line
#---------------------------------------------------------------------------------
def find_Node_By_IDkey(key):
	node = [att.split(".")[0] for att in cmds.ls("*.object_id_key") if cmds.getAttr(att) == key]
	if len(node):
		return node[0]
	else:
		return None
# Context Managers and Decorators ---
########################################################################
class HashableMObjectHandle(V1_OM.MObjectHandle):
	'''
	Hashable MObjectHandle referring to an MObject that can be used as a key in a dict.
		:See MObjectHandle documentation for more information.
	'''
	#----------------------------------------------------------------------
	def __hash__(self):
		'''
		Use the proper unique hash value unique to the MObject
		that the MObjectHandle points to
		so this class can be used as a key in a dict.
		:Return:
			MObjectHandle.hasCode()
			unique memory address for the MObject that is hashable
		'''
		return self.hashCode()
	#----------------------------------------------------------------------
	def new_api_object(self):
		""""""
		return toMObject(self.object(),OldApi=False)
		
# MOBJECT Utilty Functions ---
#----------------------------------------------------------------------
def is_Maya_Object(obj):
	""""""
	try:
		return "OpenMaya" in type(obj).__module__
	except:
		return False

#----------------------------------------------------------------------
def is_Old_API(obj):
	""""""
	return type(obj).__module__ == 'maya.OpenMaya'
#----------------------------------------------------------------------
def _isValidMObjectHandle(obj):
	if isinstance(obj, (V1_OM.MObjectHandle, V2_OM.MObjectHandle)) :
		return obj.isValid() and obj.isAlive()
	else :
		return False
#----------------------------------------------------------------------
def _isValidMObject(obj):
	try:
		return not obj.isNull()
	except:
		return False
#----------------------------------------------------------------------
def _isValidMPlug(obj):
	if is_Maya_Object(obj):
		if is_Old_API(obj):
			return not obj.isNull()
		else:
			return not obj.isNull
	else :
		return False
#----------------------------------------------------------------------
def _isValidMDagPath(obj):
	if is_Maya_Object(obj):
		# when the underlying MObject is no longer valid, dag.isValid() will still return true,
		# but obj.fullPathName() will be an empty string
		try:
			return obj.isValid() and obj.fullPathName()
		except:
			return False
	else :
		return False
#----------------------------------------------------------------------
def _isValidMDagNode(obj):
	if _isValidMObject(obj):
		api = V1_OM if is_Old_API(obj) else V2_OM
		return obj.hasFn(api.MFn.kDagNode)
	else :
		return False
#----------------------------------------------------------------------
def _isValid_Object_Or_Plug(obj):
	return _isValidMPlug(obj) or _isValidMObject(obj)

#----------------------------------------------------------------------
def _get_Old_Api_Active_Selection_List():
	"""Gets All The Objects Currently Selected In Maya"""
	# Create A Storage Container For The Active Selection
	selectionList = V1_OM.MSelectionList()
	# Fill The Container With The Active Selection
	V1_OM.MGlobal.getActiveSelectionList(selectionList)
	# Return The Selection List
	return selectionList
#----------------------------------------------------------------------
def _get_New_Api_Active_Selection_List():
	"""Gets All The Objects Currently Selected In Maya"""
	# Get The Active Selection
	selectionList = V2_OM.MGlobal.getActiveSelectionList()
	# Return The Selection List
	return selectionList

#----------------------------------------------------------------------
def get_MObject_Name(obj):
	""""""
	if is_Maya_Object(obj):
		if is_Old_API(obj):
			sel = V1_OM.MSelectionList()
			sel.add(obj)
			names = []
			sel.getSelectionStrings(names)
			res = names[0]
		else:
			sel = V2_OM.MSelectionList()
			sel.add(obj)
			res = sel.getSelectionStrings()[0]
		return res
	
	raise ValueError("input was not a vaild maya object")

#----------------------------------------------------------------------
def get_Active_Selection_List(OldApi=False):
	"""Gets All The Objects Currently Selected In Maya"""
	return _get_Old_Api_Active_Selection_List() if OldApi else _get_New_Api_Active_Selection_List()
#----------------------------------------------------------------------
def get_Active_Selection_List_Names():
	"""Gets All The Objects Currently Selected In Maya"""
	selectionList = _get_New_Api_Active_Selection_List()
	names = selectionList.getSelectionStrings()
	return names
#----------------------------------------------------------------------
def to_New_MObject(nodeName):
	""" Get the API MObject given the name of an existing node """
	#CHECK IF THE INPUT IS ALREADY A MOBJECT
	obj = None
	if _isValidMObject(nodeName):
		if is_Old_API(nodeName):
			nodeName = get_MObject_Name(nodeName)
		else:
			# CHECK IF THE INPUT CANTAINS A FUNCTION TO RETRIVE AN MOBJECT
			if hasattr(nodeName, "object"):
				obj = nodeName.object()
			else:
				obj = nodeName
				
			isinstance(obj,V2_OM.MObject)
			return obj
	# CHECK THE INPUT TO SEE IF IT IS THE OBJECT NAME
	if isinstance(nodeName, str):
		sel = V2_OM.MSelectionList()
		# ADD IT TO STORAGE CONTAINER
		sel.add( nodeName )
		# ASSINE THE ADDED ITEM
		obj = sel.getDependNode(0)
		return obj
	else:
		raise ValueError("input must be a str or MObject and a {} was found".format(type(nodeName)))
#----------------------------------------------------------------------
def to_Old_MObject(nodeName):
	""" Get the API MObject given the name of an existing node """
	obj = None
	#CHECK IF THE INPUT IS ALREADY A MOBJECT
	if _isValidMObject(nodeName):
		if not is_Old_API(nodeName):
			nodeName = get_MObject_Name(nodeName)
		else:
			# CHECK IF THE INPUT CANTAINS A FUNCTION TO RETRIVE AN MOBJECT
			if hasattr(nodeName, "object"):
				obj = nodeName.object()
			else:
				obj = nodeName
			return obj
	# CHECK THE INPUT TO SEE IF IT IS THE OBJECT NAME
	if isinstance(nodeName, str):
		# CREATE A MOBJECT AND A DAGPATH MEMORY OBJECT VARIBLE
		obj = V1_OM.MObject()
		# MAKE A SELECTIONLIST STORAGE CONTAINER
		sel = V1_OM.MSelectionList()
		# ADD IT TO STORAGE CONTAINER
		sel.add( nodeName )
		# ASSINE THE ADDED ITEM
		sel.getDependNode( 0, obj )
		return obj
	else:
		raise ValueError("input must be a str or MObject and a {} was found".format(type(nodeName)))
#----------------------------------------------------------------------
def toMObject(nodeName, OldApi=False):
	""" Get the API MObject given the name of an existing node """
	obj = to_Old_MObject(nodeName) if OldApi else to_New_MObject(nodeName)
	isinstance(obj, V2_OM.MObject)
	return obj
#----------------------------------------------------------------------
def to_New_MPlug(plugName):
	""" Get the API MObject given the name of an existing node """
	plug = None
	#CHECK IF THE INPUT IS ALREADY A MOBJECT
	if _isValidMPlug(plugName):
		if is_Old_API(plugName):
			plugName = get_MObject_Name(plugName)
		else:
			isinstance(plugName,V2_OM.MPlug)
			return plugName
	# CHECK THE INPUT TO SEE IF IT IS THE OBJECT NAME
	if isinstance(plugName, str):
		# MAKE A SELECTIONLIST STORAGE CONTAINER
		sel = V2_OM.MSelectionList()
		# ADD IT TO STORAGE CONTAINER
		sel.add( plugName )
		# ASSINE THE ADDED ITEM
		plug = sel.getPlug(0)
		return plug
	else:
		raise ValueError("input must be a str MObject or MPlug and a {} was found".format(type(plugName)))
#----------------------------------------------------------------------
def to_Old_MPlug(plugName):
	""" Get the API MObject given the name of an existing node """
	plug = None
	#CHECK IF THE INPUT IS ALREADY A MOBJECT
	if _isValidMPlug(plugName):
		if not is_Old_API(plugName):
			plugName = get_MObject_Name(plugName)
		else:
			isinstance(plugName,V1_OM.MPlug)
			return plugName
	# CHECK THE INPUT TO SEE IF IT IS THE OBJECT NAME
	if isinstance(plugName, str):
		# CREATE A MOBJECT AND A DAGPATH MEMORY OBJECT VARIBLE
		plug = V1_OM.MPlug()
		# MAKE A SELECTIONLIST STORAGE CONTAINER
		sel = V1_OM.MSelectionList()
		# ADD IT TO STORAGE CONTAINER
		sel.add( plugName )
		# ASSINE THE ADDED ITEM
		sel.getPlug( 0, plug )
		return plug
	else:
		raise ValueError("input must be a str MObject or MPlug and a {} was found".format(type(plugName)))
#----------------------------------------------------------------------
def toMPlug(plugName, OldApi=False):
	""" Get the API MObject given the name of an existing node """
	
	plug = to_Old_MPlug(plugName) if OldApi else to_New_MPlug(plugName)
	isinstance(plug, V2_OM.MPlug)
	return plug
#----------------------------------------------------------------------
def make_MObjectHandle(obj):
	""" Get the API MObjectHandle"""
	obj    = to_Old_MObject(obj)
	handle = HashableMObjectHandle(obj)
	return handle
#----------------------------------------------------------------------
def to_New_MDagPath(nodeName):
	""" Get the API MObject given the name of an existing node """
	obj = toMObject(nodeName, OldApi=False)
	dagpath =  V2_OM.MDagPath.getAPathTo(obj)
	isinstance(dagpath, V2_OM.MDagPath)
	return dagpath
#----------------------------------------------------------------------
def to_Old_MDagPath(nodeName):
	""" Get the API MObject given the name of an existing node """
	obj = toMObject(nodeName, OldApi=True)
	dagpath = V1_OM.MDagPath.getAPathTo(obj)
	isinstance(dagpath, V1_OM.MDagPath)
	return dagpath
#----------------------------------------------------------------------
def toMDagPath(nodeName, OldApi=False):
	""" Get an API MDagPAth to the node, given the name of an existing dag node """
	if OldApi:
		dagPath = to_Old_MDagPath(nodeName)
	else:
		dagPath = to_New_MDagPath(nodeName)
	return dagPath
#----------------------------------------------------------------------
def get_Function_Set(nodeName, OldApi=False):
	"""Get The Maya Function Set That Is Appropriate For The Givin MObject"""
	if OldApi:
		fnTypes = V1_OM.MFn
		api     = V1_OM
	else:
		fnTypes = V2_OM.MFn
		api     = V2_OM
		
	obj = toMObject(nodeName, OldApi)
	
	if obj.hasFn(fnTypes.kTransform):
		return api.MFnTransform(obj)
	elif obj.hasFn(fnTypes.kMesh):
		return api.MFnMesh(obj)
	elif obj.hasFn(fnTypes.kDagNode):
		return api.MFnDagNode(obj)
	elif obj.hasFn(fnTypes.kDependencyNode):
		return api.MFnDependencyNode(obj)
#----------------------------------------------------------------------
def nameToNode( nodeName=None ,asobj=False, aspath=False, asplug=False, OldApi=False):
	"""function that returns a node object given a name"""
	res = None
	if nodeName is None:
		# IF NOT GET THE CURRENTLY ACTIVE SELECTIONLIST
		names  = get_Active_Selection_List_Names()
		if not len(names):
			V1_OM.MGlobal.displayError("Nothing Currently Selected And No Input was Given")
			raise NothingSelectedError()
		nodeName = names[0]
		
	if asobj:
		res = toMObject(nodeName, OldApi)
	elif aspath:
		res = toMDagPath(nodeName, OldApi)
	elif asplug:
		res = toMPlug(nodeName, OldApi)
	else:
		res = get_Function_Set(nodeName, OldApi)
	return res
#----------------------------------------------------------------------
def nameToPlug( node, attrName=None, OldApi=False):
	"""function that finds a plug given a node object and plug name"""
	# CHECK IF THE INPUT NODE IS NOT AND NODE OBJECT BUT THE NAME OF AN OBJECT
	plug = None
	if isinstance(node, str):
		if node.count("."):
			plug = toMPlug(node, OldApi=OldApi)
		else:
			if isinstance(attrName, str):
				node_fn = nameToNode(node, OldApi=OldApi)
				node_name = ".".join([node_fn.name(), attrName])
				plug = toMPlug(node_name, OldApi=OldApi)
			else:
				raise ValueError("node input was not an attribute and the attrName input was left blank")
			
	elif _isValidMPlug(node):
		plug = node
	elif _isValidMObject(node):
		node_fn = nameToNode(node, OldApi)
		plug = toMPlug(node_fn.name(),OldApi)
	else:
		raise MPlugCreationError(node)
	return plug