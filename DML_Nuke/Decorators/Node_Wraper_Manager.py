
import nuke
from ..Mata_Classes import Data_Storage
from ..Nuke_Nodes import Node_List
import functools
import sys

if False:
	from ..Nuke_Nodes import Abstract_Nodes	
#----------------------------------------------------------------------
def flatten(x):
	result = []
	for el in x:
		if hasattr(el, "__iter__") and not isinstance(el, basestring):
			result.extend(flatten(el))
		else:
			result.append(el)
	return result

#----------------------------------------------------------------------
def to_DML_Nuke_Object(node):
	"""Takes the input node and converts it to a DML_Node"""
	# check if the input has a _is_dml_object attribute
	if hasattr(node,"_is_dml_object"):
		# if so than just return it
		return node
	if node.__class__.__name__ in Data_Storage.Object_Return_Type_Relations:
		cls = Data_Storage.Object_Return_Type_Relations[node.__class__.__name__]
		return cls(node)
	else:
		return node
#----------------------------------------------------------------------
def to_DML_Nuke_Objects(*args):
	return [to_DML_Nuke_Object(arg) for arg in flatten(args)]

#----------------------------------------------------------------------
def nuke_Object_Return_Wrapper(func):
	''' '''
	@functools.wraps(func)
	def wrapper(*args, **kws):
		err = None
		try:
			res = func(*args, **kws)
			if isinstance(res,list):
				res = to_DML_Nuke_Objects(res)
			elif isinstance(res,dict):
				buffer_res = dict()
				for k,val in res.iteritems():
					buffer_res[k]=to_DML_Nuke_Object(val)
				res = buffer_res
			elif hasattr(res,"_is_dml_object"):
				return res
			else:
				res = to_DML_Nuke_Object(res)
		except Exception, error:
			err=error
		finally:
			if err:
				traceback = sys.exc_info()[2]  # get the full traceback
				raise Exception(err, traceback)
			return res
	return wrapper


#----------------------------------------------------------------------
def to_DML_Node(node):
	"""Takes the input node and converts it to a DML_Node"""
	res = None
	if False:
		isinstance(res,Abstract_Nodes.Node)
	# check if the input has a _is_dml_object attribute
	if hasattr(node,"_is_dml_object"):
		# if so than just return it
		res = node
		return res
	else:
		if isinstance(node,basestring):
			if nuke.exists(node):
				node = nuke.toNode(node)
			else:
				raise LookupError("node node exists with the name {}".format(node))
		isinstance(node,nuke.Node)
		# get the type of node
		typ = node.Class()
		# using the type of node check if this type has possible overide checks
		if Data_Storage.Node_Return_Type_Overides.has_key(typ):
			# if so start scanning over them and see if the check returns true
			# if so then return that instead of the class related to the type
			for cls in Data_Storage.Node_Return_Type_Overides[typ]:
				if cls._overide_Return_Check(node):
					res = cls(nuke_node=node)
					return res
		# check if the type has a designated class related to it
		if Data_Storage.Node_Return_Type_Relations.has_key(typ):
			# if so return it
			cls = Data_Storage.Node_Return_Type_Relations.get(typ)
			res = cls(nuke_node=node)
			return res
		else:
			cls = Data_Storage.Node_Return_Type_Relations.get("default")
			res = cls(nuke_node=node)
			return res
	
#----------------------------------------------------------------------
def to_DML_Nodes(*args):
	return Node_List([to_DML_Node(arg) for arg in flatten(args)])
#----------------------------------------------------------------------
def node_Return_Wrapper(func):
	''''''
	@functools.wraps(func)
	def wrapper(*args, **kws):
		err = None
		try:
			res = func(*args, **kws)
			if isinstance(res,list):
				res = Node_List([to_DML_Node(name) for name in res])
			elif isinstance(res,basestring):
				res = to_DML_Node(res)
			elif isinstance(res,nuke.Node):
				res = to_DML_Node(res)
			else:
				res = None
		except Exception, error:
			err=error
		finally:
			if err:
				traceback = sys.exc_info()[2]  # get the full traceback
				raise Exception(err, traceback)
			return res
	return wrapper

#----------------------------------------------------------------------
def Dml_Node_Arg_Wrapper(func):
	''''''
	@functools.wraps(func)
	def wrapper(*args, **kws):
		err = None
		try:
			if len(args)==1:
				args = to_DML_Node(args)
				res = func(args, **kws)
			else:
				args = to_DML_Nodes(args)
				res = func(*args, **kws)
		except Exception, error:
			err=error
		finally:
			if err:
				traceback = sys.exc_info()[2]  # get the full traceback
				raise Exception(err, traceback)
			return res
	return wrapper


#----------------------------------------------------------------------
def to_DML_Knob(knob,node=None):
	"""Takes the input node and converts it to a DML_Knob"""
	# check if the knob is allrady wrapped
	if hasattr(knob,"_is_dml_object"):
		return knob
	# check if the knob is a name and not the knob itself
	# and that the node was give to get the knob from
	if isinstance(knob,basestring) and node is not None:
		# check if the node is the name and not the node itself
		if isinstance(node,basestring):
			# make sure the node exists
			if not nuke.exists(node):
				raise LookupError("The node name given does not exist {}".format(node))
			# aquaire the node
			node = nuke.toNode(node)
			# make sure a node was found
			if node == None:
				raise LookupError("The node name give was not a nuke node")
		# check if the node has a knob with knob name given
		if node.knobs().has_key(knob):
			# aquaire the knob
			knob = node.knob(knob)
		else:
			raise LookupError("the name of knob given does not exist on the node give {},{}".format(node.name(),knob))
	elif isinstance(knob,basestring) and node is None:
		raise Exception("node must be given when knob is a name")
	
	# make sure the knob is wrapperable
	if isinstance(knob,nuke.Knob):
		# the knob type
		typ = knob.Class()
		# using the type of knob check if this type has possible overide checks
		if Data_Storage.Knob_Return_Type_Overides.has_key(typ):
			# if so start scanning over them and see if the check returns true
			# if so then return that instead of the class related to the type
			for cls in Data_Storage.Knob_Return_Type_Overides[typ]:
				if cls._overide_Return_Check(knob):
					return cls(knob)
		# check if the there is a wrapper for this type of know
		if Data_Storage.Knob_Return_Type_Relations.has_key(typ):
			cls = Data_Storage.Knob_Return_Type_Relations.get(typ)
		# if not use the default one
		else:
			cls = Data_Storage.Knob_Return_Type_Relations.get("default")
		# return the wrapped knob
		return cls(knob)
	else:
		raise LookupError("the input knob could not be wrapped")
#----------------------------------------------------------------------
def to_DML_Knobs(*args):
	return [to_DML_Knob(arg) for arg in flatten(args)]
#----------------------------------------------------------------------
def knob_Return_Wrapper(func):
	''''''
	@functools.wraps(func)
	def wrapper(*args, **kws):
		err = None
		try:
			res = func(*args, **kws)
			if isinstance(res,list):
				res = [to_DML_Knob(name) for name in res]
			elif isinstance(res,dict):
				buffer_res = dict()
				for k,val in res.iteritems():
					buffer_res[k]=to_DML_Knob(val)
				res = buffer_res
			elif isinstance(res,nuke.Knob):
				res = to_DML_Knob(res)
			elif hasattr(res,"_is_dml_object"):
				return res
			else:
				res = []
		except Exception, error:
			err=error
		finally:
			if err:
				traceback = sys.exc_info()[2]  # get the full traceback
				raise Exception(err, traceback)
			return res
	return wrapper

#----------------------------------------------------------------------
def to_Real_Nuke_Node(node):
	"""Takes the input node and converts it to a DML_Node"""
	if node == None:
		return node
	# check if the input has a _is_dml_object attribute
	if hasattr(node,"_is_dml_object"):
		# if so than just return it
		return node.nuke_object
	elif isinstance(node,(nuke.Node,nuke.Knob)):
		return node
	elif isinstance(node,Data_Storage.Object_Return_Type_Relations.values()):
		return node.nuke_object
	else:
		raise LookupError("node could not be converted {}".format(node))
#----------------------------------------------------------------------
def to_Real_Nuke_Nodes(*args):
	return [to_Real_Nuke_Node(arg) for arg in flatten(args)]
#----------------------------------------------------------------------
def standerdized_item_list(item_list):
	""""""
	if isinstance(item_list,(list,tuple)):
		new_item_list = to_Real_Nuke_Nodes(item_list)
		return new_item_list
	else:
		new_item = to_Real_Nuke_Node(item_list)
		return new_item
#----------------------------------------------------------------------
def nuke_Node_Return_Wrapper(func):
	''' '''
	@functools.wraps(func)
	def wrapper(*args, **kws):
		err = None
		new_args = [args[0]]
		new_kwargs = dict()
		try:
			for k,v in kws:
				new_value = standerdized_item_list(v)
				new_kwargs[k]=new_value
			new_args.extend(standerdized_item_list(args[1:]))
			res=func(*new_args, **new_kwargs)
		except Exception, error:
			err=error
		finally:
			if err:
				traceback = sys.exc_info()[2]  # get the full traceback
				raise StandardError(Exception(err), traceback)
			return res
	return wrapper

