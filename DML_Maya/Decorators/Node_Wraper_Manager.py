import maya.api.OpenMaya as OpenMaya
import functools
from .. import Data_Storage
import maya.cmds as cmds
import sys
from ..General_Utils import flatten

if False:
	from .. import Maya_Nodes
#----------------------------------------------------------------------
def to_DML_Component(node,attrname):
	"""Takes the input node and converts it to a DML_Node"""	
	cls = Data_Storage.Component_Return_Type_Relations.get("default")
		
	return cls(node,attrname)

#----------------------------------------------------------------------
def get_Plug_Class_Wrapper(plg):
	""""""
	try:
		typ = cmds.getAttr(plg,typ=True)
	except Exception as e:
		if e.message == 'The value for the attribute could not be retrieved.\n':
			raise LookupError(e)
		if e.message == 'Cannot evaluate more than one attribute.\n':
			try:
				sel = OpenMaya.MSelectionList()
				sel.add(plg)
				strings = sel.getSelectionStrings()
				if len(strings) == 1:
					typ = cmds.getAttr(strings[0],typ=True)
			except Exception as e2:
				raise RuntimeError(e2)
		else:
			raise RuntimeError(e)
	
	if typ in Data_Storage.Plug_Return_Type_Overides:
		# if so start scanning over them and see if the check returns true
		# if so then return that instead of the class related to the type
		for cls in Data_Storage.Plug_Return_Type_Overides[typ]:
			if cls._overide_Return_Check(plg):
				return cls
			
	# check if the type has a designated class related to it
	if typ in Data_Storage.Plug_Return_Type_Relations:
		# if so return it
		cls = Data_Storage.Plug_Return_Type_Relations.get(typ)
	else:
		cls = Data_Storage.Plug_Return_Type_Relations.get("default")
	return cls

#----------------------------------------------------------------------
def to_DML_Plug(*args):
	"""Takes the input node and converts it to a DML_Plug"""
	if len(args) == 1:
		if hasattr(args[0],"_is_dml_maya_node"):
			res = args[0]
		elif isinstance(args[0],OpenMaya.MPlug):
			plg = args[0]
			node = cmds.ls(plg,int=True)[0].split(".",1)[0]
			node = to_DML_Node(node)
			wrapper_class = get_Plug_Class_Wrapper(plg)
			res = wrapper_class(node,plg)
	elif len(args) == 2:
		node,attrname = args
		if not hasattr(node,"_is_dml_maya_node"):
			node = to_DML_Node(node)
		try:
			path = str(node)+"."+attrname
			sel = OpenMaya.MSelectionList()
			sel.add(path)
			plg = sel.getPlug(0)
			wrapper_class = get_Plug_Class_Wrapper(plg)
			res = wrapper_class(node,plg)
		except TypeError:
			res = to_DML_Component(node, attrname)
	if False:
		isinstance(res,Maya_Nodes.Abstract_Nodes.Generic_Plug.Plug)
	return res

#----------------------------------------------------------------------
def to_DML_Node(node,**kwargs):
	"""Takes the input node and converts it to a DML_Node"""
	# check if the input has a _is_dml_maya_node attribute
	if hasattr(node,"_is_dml_maya_node"):
		# if so than just return it
		return node
	elif isinstance(node,OpenMaya.MPlug):
		return to_DML_Plug(node)
	elif isinstance(node,OpenMaya.MObject):
		sellist = OpenMaya.MSelectionList()
		sellist.add(node)
		node = sellist.getSelectionStrings()[0]
		return to_DML_Node(node)
	
	elif "." in str(node):
		node_name,attr_name = node.split(".",1)
		node = to_DML_Node(node_name)
		return to_DML_Plug(node,attr_name)
	else:
		# get the type of node
		typ = cmds.objectType(node)
		# using the type of node check if this type has possible overide checks
		if typ in Data_Storage.Node_Return_Type_Overides:
			# if so start scanning over them and see if the check returns true
			# if so then return that instead of the class related to the type
			for cls in reversed(Data_Storage.Node_Return_Type_Overides[typ]):
				if cls._overide_Return_Check(node):
					return cls(node,**kwargs)
		# check if the type has a designated class related to it
		if typ in Data_Storage.Node_Return_Type_Relations:
			# if so return it
			cls = Data_Storage.Node_Return_Type_Relations.get(typ)
			return cls(node,**kwargs)
		# if no check is found and no relation has been set and it is a dag node
		elif 'dagNode' in cmds.nodeType(typ, inherited=True, isTypeName=True):
			cls = Data_Storage.Node_Return_Type_Relations.get('dagNode')
			return cls(node,**kwargs)
		# check if it is a sub type of shader
		elif typ in cmds.listNodeTypes( 'shader', ex='shader/volume/utility:shader/volume/particle'):
			cls = Data_Storage.Node_Return_Type_Relations.get("material")
			return cls(node,**kwargs)
		# by defalut return a base node
		else:
			cls = Data_Storage.Node_Return_Type_Relations.get("default")
			return cls(node,**kwargs)

def to_DML_Nodes(*args):
	return [to_DML_Node(arg) for arg in flatten(args)]

#----------------------------------------------------------------------
def node_Return_Wrapper(func):
	''''''
	@functools.wraps(func)
	def wrapper(*args, **kws):
		err = None
		try:
			res = func(*args, **kws)
			if isinstance(res,list):
				if not len(res):
					res = []
				res = [to_DML_Node(name) for name in res]
			elif isinstance(res,(str,OpenMaya.MPlug)):
				res = to_DML_Node(res)
			else:
				res = []
		except Exception as error:
			err=error
		finally:
			if err:
				traceback = sys.exc_info()[2]  # get the full traceback
				raise Exception(err, traceback)
			return res
	return wrapper