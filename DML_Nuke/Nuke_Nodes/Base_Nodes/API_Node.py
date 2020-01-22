
from ...Mata_Classes.Node_Return_Type_Publication_Metaclass import Node_Return_Type_Publication 
import nuke



#----------------------------------------------------------------------
def get_nuke_node(self):
	return self._nuke_object
#----------------------------------------------------------------------
def set_nuke_node(self, value):
	self.__dict__["_nuke_object"] = value
	
#----------------------------------------------------------------------
def get_nuke_node_name(self):
	return self.nuke_object.name()
#----------------------------------------------------------------------
def set_nuke_node_name(self, value):
	self.nuke_object.setName(value)
	
#----------------------------------------------------------------------
def get_nuke_node_fullName(self):
	return self.nuke_object.fullName()

#----------------------------------------------------------------------
def get_nuke_node_clones(self):
	return self.nuke_object.clones()

#----------------------------------------------------------------------
def get_nuke_node_channels(self):
	return self.nuke_object.channels()

#----------------------------------------------------------------------
def get_nuke_node_layers(self):
	return sorted(list(set([channel.split(".")[0] for channel in self.nuke_object.channels()])))

#----------------------------------------------------------------------
def get_nuke_node_firstFrame(self):
	return self.nuke_object.firstFrame()

#----------------------------------------------------------------------
def get_nuke_node_lastFrame(self):
	return self.nuke_object.lastFrame()

#----------------------------------------------------------------------
def get_nuke_node_maxInputs(self):
	return self.nuke_object.maxInputs()

#----------------------------------------------------------------------
def get_nuke_node_maxOutputs(self):
	return self.nuke_object.maxOutputs()

#----------------------------------------------------------------------
def get_nuke_node_minInputs(self):
	return self.nuke_object.minInputs()

#----------------------------------------------------------------------
def get_nuke_node_screenHeight(self):
	return self.nuke_object.screenHeight()

#----------------------------------------------------------------------
def get_nuke_node_screenWidth(self):
	return self.nuke_object.screenWidth()

#----------------------------------------------------------------------
def get_nuke_node_height(self):
	return self.nuke_object.height()

#----------------------------------------------------------------------
def get_nuke_node_width(self):
	return self.nuke_object.width()

#----------------------------------------------------------------------
def get_nuke_node_pixelAspect(self):
	return self.nuke_object.pixelAspect()

#----------------------------------------------------------------------
def get_nuke_node_inputs(self):
	return self.nuke_object.inputs()

#----------------------------------------------------------------------
def get_nuke_node_optionalInput(self):
	return self.nuke_object.optionalInput()

#----------------------------------------------------------------------
def get_nuke_node_numKnobs(self):
	return self.nuke_object.numKnobs()

#----------------------------------------------------------------------
def get_nuke_node_Selected(self):
	return self.nuke_object.isSelected()
#----------------------------------------------------------------------
def set_nuke_node_Selected(self,val):
	return self.nuke_object.setSelected(val)

#----------------------------------------------------------------------
def get_nuke_node_frameRange(self):
	return self.nuke_object.frameRange()

#----------------------------------------------------------------------
def get_nuke_node_format(self):
	return self.nuke_object.format()

#----------------------------------------------------------------------
def get_nuke_node_proxy(self):
	return self.nuke_object.proxy()

########################################################################
class DML_Node(object):
	__metaclass__             = Node_Return_Type_Publication
	NODE_TYPE_RELATION        = None
	NODE_CLASS_NAME           = None
	RETURN_OVERIDE_CHECK_TYPE = None
	IS_CREATABLE              = False
	CREATE_COMMAND            = None
	_is_dml_object            = None
	nuke_object               = property(fget=get_nuke_node, fset=set_nuke_node, doc="The Wraped Nuke Node")
	name                      = property(fget=get_nuke_node_name, fset=set_nuke_node_name, doc="The name of the node")
	fullName                  = property(fget=get_nuke_node_fullName, doc="full path to the node")
	clones                    = property(fget=get_nuke_node_clones, doc="number of clones")
	channels                  = property(fget=get_nuke_node_channels, doc="List channels output by this node.")
	layers                    = property(fget=get_nuke_node_layers, doc="List of channel layers output by this node.")
	firstFrame                = property(fget=get_nuke_node_firstFrame, doc="First frame in frame range for this node.")
	lastFrame                 = property(fget=get_nuke_node_lastFrame, doc="Last frame in frame range for this node.")
	maxInputs                 = property(fget=get_nuke_node_maxInputs, doc="Maximum number of inputs this node can have.")
	maxOutputs                = property(fget=get_nuke_node_maxOutputs, doc="Maximum number of outputs this node can have")
	minInputs                 = property(fget=get_nuke_node_minInputs, doc="Minimum number of inputs this node can have")
	width                     = property(fget=get_nuke_node_width, doc="Width of the node.")
	height                    = property(fget=get_nuke_node_height, doc="Height of the node.")
	screenWidth               = property(fget=get_nuke_node_screenWidth, doc="Width of the node when displayed on screen in the DAG, at 1:1 zoom, in pixels.")
	screenHeight              = property(fget=get_nuke_node_screenHeight, doc="Height of the node when displayed on screen in the DAG, at 1:1 zoom, in pixels.")
	pixelAspect               = property(fget=get_nuke_node_pixelAspect, doc="Pixel Aspect ratio of the node.")
	optionalInput             = property(fget=get_nuke_node_optionalInput, doc="Number of first optional input.")
	inputs                    = property(fget=get_nuke_node_inputs, doc="Number of the highest connected input + 1. If inputs 0, 1, and 3 are connected, this will return 4.")
	numKnobs                  = property(fget=get_nuke_node_numKnobs, doc="The number of knobs.")
	selected                  = property(fget=get_nuke_node_Selected, fset=set_nuke_node_Selected, doc="Returns the current selection state of the node.  This is the same as checking the 'selected' knob.\nSet the selection state of the node.  This is the same as changing the 'selected' knob.")
	frameRange                = property(fget=get_nuke_node_frameRange, doc="Frame range for this node : FrameRange.")
	format                    = property(fget=get_nuke_node_format, doc="Format of the node.")
	proxy                     = property(fget=get_nuke_node_proxy, doc="return: True if proxy is enabled, False otherwise.")
	#----------------------------------------------------------------------
	def __new__(cls,*args,**kwargs):
		# get the nuke node if was given in the kwargs
		arg_count   = len(args)
		nuke_node   = kwargs.get("nuke_node",None)
		node_knobs  = kwargs.pop("knobs", None)
		inpanel     = kwargs.pop("inpanel",False)
		post_kwargs = kwargs.pop("post_kwargs",None)
		maintain_current_selection = kwargs.pop("keepSelection",False)
		clear_current_selection    = kwargs.pop("clear",False)
		select_Before_Create       = kwargs.pop("selectBeforeCreate",[])
		
		tcl_parts  = []
		# if node_knobs was given then split the tcl stype arguments apart
		if isinstance(node_knobs,basestring):
			tcl_parts = node_knobs.split()
		# if arg count is 1 and spliting it gives a len greater then 1 then split the tcl stype arguments apart
		elif arg_count == 1 and len(args[0].split()) > 1:
			tcl_parts = args[0].split()
		
		# check if the nuke_node is None and the number of args given is 1
		if (nuke_node is None and arg_count == 1):
			# then check if the input arg is valid
			# this check might be changed to
			# if ( isinstance(args[0],nuke.Node) or hasattr(args[0],"_is_dml_object") ):
			if isinstance(args[0],(nuke.Node,DML_Node)):
				nuke_node = args[0]
			
		# check if nuke node was not given
		# if not start checking for a name
		if nuke_node is None:
			# check if the name was given in the key words and if the node exists
			if kwargs.has_key("name") and nuke.exists(kwargs.get("name")):
				nuke_node = nuke.toNode(kwargs.get("name"))
			
			# check if there are tcl_parts and the word name is in the tcl style arguments and if the node exists
			elif len(tcl_parts) and "name" in tcl_parts and nuke.exists(tcl_parts[ tcl_parts.index("name")+1 ]):
				nuke_node = nuke.toNode(tcl_parts[ tcl_parts.index("name")+1 ])
			# check if there is 1 arg and that the arg is a string and the input arg exists in the nuke scene
			elif arg_count == 1 and isinstance(args[0],basestring) and nuke.exists(args[0].strip()):
				nuke_node = nuke.toNode(args[0].strip())
			
		# check for the nuke_node
		if nuke_node is not None:
			# then check if the input nuke_node is valid
			# to be valid it must be an instance of nuke.Node or DML_Node
			if not isinstance(nuke_node,(nuke.Node,DML_Node)):
				# if not raise and Error 
				raise ValueError("The input nuke_node {} was not valid".format(type(nuke_node)))
			
			# check if nuke node is a dml wrapper node
			# if so than just return it
			elif hasattr(nuke_node,"_is_dml_object"):
				return nuke_node
			
			# generate this wrapper class 
			# assign it to the nuke node
			# and return the wrapper class
			else:
				obj = object.__new__(cls)
				obj.nuke_object = nuke_node
				return obj
		# if no nuke node given or found enter create mode
		else:
			# make sure this wrapper class has a node type Relation
			if cls.NODE_TYPE_RELATION is None:
				raise LookupError("This Wrapper Class Has No Node Type Relation can not be constructed {}".format(cls.__name__))
			else:
				# check if there are kwargs
				# if so then use the node constructer
				if len(kwargs.keys()):
					fn = getattr(nuke.nodes,cls.NODE_TYPE_RELATION)
					nuke_node = fn(**kwargs)
				# else use the createNode function
				else:
					# check of knob values exist
					if node_knobs is None:
						# if not check of knob values were input
						# if so use them else make it empty string
						if arg_count:
							node_knobs = args[0]
						else:
							node_knobs = ""
					if maintain_current_selection or clear_current_selection:
						current_selection = nuke.selectedNodes()
						
					if clear_current_selection:
						[n.setSelected(True) for n in current_selection]
						
					nuke_node = nuke.createNode(cls.NODE_TYPE_RELATION,node_knobs,inpanel)
					
					if maintain_current_selection:
						nuke_node.setSelected(False)
						[n.setSelected(True) for n in current_selection]
				
				if hasattr(nuke_node,"_is_dml_object"):
						return nuke_node
				if isinstance(post_kwargs,dict):
					kwargs = post_kwargs
				obj = object.__new__(cls)
				obj.nuke_object = nuke_node
				return obj				
	#----------------------------------------------------------------------
	def __str__(self):
		return str(self.nuke_object)
	#----------------------------------------------------------------------
	def __repr__(self):
		return '{}.{}("{}")'.format(self.__module__,self.__class__.__name__,self.fullName)
	#----------------------------------------------------------------------
	def __ne__(self, other):
		if isinstance(other,basestring):
			return self.fullName != other
		elif isinstance(other,nuke.Node):
			return self.nuke_object != other
		elif isinstance(other,DML_Node):
			return str(self.nuke_object) != other.nuke_object
		else:
			return True
	#----------------------------------------------------------------------
	def __eq__(self,other):
		""""""
		if isinstance(other,basestring):
			return self.fullName == other
		elif isinstance(other,nuke.Node):
			return self.nuke_object == other
		elif isinstance(other,DML_Node):
			return str(self.nuke_object) == other.nuke_object
		else:
			return False
	#----------------------------------------------------------------------
	def __getattribute__(self,name):
		try:
			return object.__getattribute__(self,name)
		except AttributeError:
			nuke_node = object.__getattribute__(self,"_nuke_object")
			if hasattr(nuke_node,name):
				return getattr(nuke_node,name)
			else:
				raise AttributeError("object has no attribute '{}'".format(name))
	#----------------------------------------------------------------------
	def __hash__(self):
		""""""
		return hash(self.nuke_object)
	#----------------------------------------------------------------------
	@classmethod
	def _overide_Return_Check(cls,node):
		""""""
		return False
		
if False:
	isinstance(DML_Node.name,str)
	isinstance(DML_Node.fullName,str)
	isinstance(DML_Node.nuke_object,nuke.Node)