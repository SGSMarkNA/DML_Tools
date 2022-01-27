
import maya.cmds as cmds
#import pymel.core as pm
import maya.api.OpenMaya as OpenMaya
from ...Mata_Classes.Plug_Return_Type_Publication_Metaclass import Plug_Return_Type_Publication
from ...Decorators.Node_Wraper_Manager import node_Return_Wrapper,to_DML_Node,to_DML_Nodes
from ... import Data_Storage
from .DML_MPlug import MPlug
from ... import General_Utils
# This Has Reason Other Then To Compensate For Wing IDS Code Analizer
if False:
	from ....DML_Maya import Data_Storage
	from ....DML_Maya.Maya_Nodes.Abstract_Nodes import Dependency_Node


########################################################################
class MDT(object):
	Int32Array     ='Int32Array'
	doubleArray    ='doubleArray'
	lattice        ='lattice'
	matrix         ='matrix'
	mesh           ='mesh'
	nurbsCurve     ='nurbsCurve'
	nurbsSurface   ='nurbsSurface'
	pointArray     ='pointArray'
	string         ='string'
	stringArray    ='stringArray'
	vectorArray    ='vectorArray'
	#----------------------------------------------------------------------
	@classmethod
	def items(cls):
		return [cls.Int32Array, cls.doubleArray, cls.lattice, cls.matrix, cls.mesh, cls.nurbsCurve, cls.nurbsSurface, cls.pointArray, cls.string, cls.stringArray, cls.vectorArray]
########################################################################
class MAT(object):
	bool           ='bool'
	byte           ='byte'
	char           ='char'
	compound       ='compound'
	double         ='double'
	double2        ='double2'
	double3        ='double3'
	doubleAngle    ='doubleAngle'
	doubleLinear   ='doubleLinear'
	enum           ='enum'
	float          ='float'
	float2         ='float2'
	float3         ='float3'
	floatLinear    ='floatLinear'
	fltMatrix      ='fltMatrix'
	long           ='long'
	long2          ='long2'
	long3          ='long3'
	message        ='message'
	reflectance    ='reflectance'
	short          ='short'
	short2         ='short2'
	short3         ='short3'
	spectrum       ='spectrum'
	time           ='time'
	#----------------------------------------------------------------------
	@classmethod
	def items(cls):
		return [cls.bool, cls.byte, cls.char, cls.compound, cls.double, cls.double2, cls.double3, cls.doubleAngle, cls.doubleLinear, cls.enum, cls.float, cls.float2, cls.float3, cls.fltMatrix, cls.long, cls.long2, cls.long3, cls.message, cls.reflectance, cls.short, cls.short2, cls.short3, cls.spectrum, cls.time]
	#----------------------------------------------------------------------
	@classmethod
	def triples(cls):
		return [cls.double3, cls.float3, cls.short3, cls.long3]
	#----------------------------------------------------------------------
	@classmethod
	def double(cls):
		return [cls.double2, cls.float2, cls.short2, cls.long2]
	#----------------------------------------------------------------------
	@classmethod
	def complex(cls):
		return [cls.double2, cls.double3,cls.float2, cls.float3,cls.long2, cls.long3,cls.short2, cls.short3]
	#----------------------------------------------------------------------
	@classmethod
	def numerical(cls):
		return [cls.bool, cls.byte, cls.char, cls.double, cls.doubleAngle, cls.doubleLinear, cls.float, cls.long, cls.reflectance, cls.short, cls.spectrum, cls.time,cls.floatLinear]
########################################################################
class MTypes(object):
	DTS = ['Int32Array', 'doubleArray', 'lattice', 'matrix', 'mesh', 'nurbsCurve', 'nurbsSurface', 'pointArray', 'string', 'stringArray', 'vectorArray']
	ATS = ['bool', 'byte', 'char', 'TdataCompound','compound', 'double', 'double2', 'double3', 'doubleAngle', 'doubleLinear', 'enum', 'float', 'float2', 'float3', 'fltMatrix', 'long', 'long2', 'long3', 'message', 'reflectance', 'short', 'short2', 'short3', 'spectrum', 'time']
	NTS = ['bool', 'byte', 'char','double', 'doubleAngle', 'doubleLinear','float','floatLinear','long', 'reflectance', 'short','spectrum','time']
	STS = ['bool', 'byte', 'char','double', 'doubleAngle', 'doubleLinear','float','long', 'reflectance', 'short','spectrum','time']
	CTS = ['double2', 'double3','float2', 'float3','long2', 'long3','short2', 'short3']

########################################################################
class API_Plug(object, metaclass=Plug_Return_Type_Publication):
	if False:
		apiPlug = OpenMaya.MPlug()
	_is_dml_maya_node         = None
	MAYA_PLUG_TYPE_RELATION   = "default"
	RETURN_OVERIDE_CHECK_TYPE = None
	##----------------------------------------------------------------------
	def __new__(cls,node,plug):
		
		obj = object.__new__(cls)
		obj._raw_name = plug.name().split(".",1)[1]
		obj.node      = node
		obj._api_plug = plug
		return obj
	#----------------------------------------------------------------------
	def __str__(self):
		return str(self.node.name + "." + self._raw_name)
	#----------------------------------------------------------------------
	def __repr__(self):
		return '{}.{}("{}")'.format(self.__module__,self.__class__.__name__,self.plug_path)
	#----------------------------------------------------------------------
	def __hash__(self):
		return hash(self.node._uuid + self.plug_name)
	#----------------------------------------------------------------------
	def __ne__(self, other):
		return self.plug_path != str(other)
	#----------------------------------------------------------------------
	def __eq__(self,other):
		""""""
		return self.plug_path == str(other)
	#----------------------------------------------------------------------
	def __add__(self,other):
		""""""
		return self.plug_path + str(other)
	#----------------------------------------------------------------------
	def __radd__(self,other):
		""""""
		return str(other) + self.plug_path
	#----------------------------------------------------------------------
	def __rshift__(self,other):
		""""""
		self.connect(other)
	#----------------------------------------------------------------------
	def __lshift__(self,other):
		""""""
		self.disconnect(other)
	#----------------------------------------------------------------------
	@classmethod
	def _overide_Return_Check(self,node):
		""""""
		return False
	#----------------------------------------------------------------------
	@property
	def apiPlug(self):
		return self._api_plug
	#----------------------------------------------------------------------
	@property
	def plug_path(self):
		path = self.node.name + "." + self._raw_name
		return path
	#----------------------------------------------------------------------
	@property
	def plug_name(self):
		return self._raw_name.split(".")[-1].split("[")[0]
	#----------------------------------------------------------------------
	@property
	def children(self):
		res = General_Utils.none_To_List(cmds.attributeQuery( self.plug_name, node=self.node, listChildren=True ))
		return to_DML_Nodes([self.plug_path + "." + child for child in res])
	#----------------------------------------------------------------------
	@property
	def child_count(self):
		val  = General_Utils.none_To_Zero(cmds.attributeQuery( self.plug_name, node=self.node, numberOfChildren=True ))
		return int(val[0]) if isinstance(val,list) else val
	#----------------------------------------------------------------------
	@property
	def parent(self):
		res = General_Utils.none_To_List(cmds.attributeQuery( self.plug_name, node=self.node, listParent=True ))
		if len(res):
			return to_DML_Node(self.node.name + "." + res[0])
		else:
			return None
	#----------------------------------------------------------------------
	@property
	def multiIndices(self):
		if self.isMulti:
			val = General_Utils.none_To_List(cmds.getAttr( self.plug_path, multiIndices=True ))
			val = [int(v) for v in val]
		else:
			val = []
		return val
	#----------------------------------------------------------------------
	@property
	@node_Return_Wrapper
	def multiElements(self):
		val = self.multiIndices
		if len(val):
			return [self.plug_path + "[{}]".format(i) for i in val]
		return val
	#----------------------------------------------------------------------
	@property
	def existingArrayAttributeIndices(self):
		""""""
		if self.isArray:
			return self.apiPlug.getExistingArrayAttributeIndices()
		else:
			return []
	#----------------------------------------------------------------------
	@property
	@node_Return_Wrapper
	def existingArrayAttributeElements(self):
		""""""
		if self.isArray:
			return [self.plug_path + "[{}]".format(i) for i in self.existingArrayAttributeIndices]
		return []
	#----------------------------------------------------------------------
	@property
	def arrayElementsWithConnections(self):
		res = []
		if self.isArray:
			for elem in self.existingArrayAttributeElements:
				if elem.isConnected:
					res.append(elem)
		return res
	#----------------------------------------------------------------------
	def get_Next_Unconneced_Array_Element(self):
		
		if not self.isArray:
			raise TypeError("not an Array Plug")
		
		num_elements = self.apiPlug.evaluateNumElements()
		indices      = self.existingArrayAttributeIndices
		res = None
		for index in range(num_elements):
			if not index == indices[index]:
				res = self.elementByLogicalIndex(index)
				break
			if not self.elementByLogicalIndex(index).isConnected:
				res = self.elementByLogicalIndex(index)
				break
		if res is None:
			res = self.elementByLogicalIndex(num_elements)
		isinstance(res,API_Plug)
		return res
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def get_Element_Source_Nodes(self):
		""""""
		res = []
		for elem in self.arrayElementsWithConnections:
			s = elem.apiPlug.source()
			if not s.isNull:
				res.append(s.node())
		return res
	#----------------------------------------------------------------------
	def get_Element_Connected_To_Node_As_Source(self,node):
		""""""
		if self.is_Node_A_Source_In_Elements(node):
			for elem in self.arrayElementsWithConnections:
				if elem.source_node() == node:
					return elem
		return None
	#----------------------------------------------------------------------
	def is_Node_A_Source_In_Elements(self,node):
		""""""
		node = to_DML_Node(node)
		for obj in self.get_Element_Source_Nodes():
			if obj == node:
				return True
		return False
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def elementByLogicalIndex(self,index):
		""""""
		if not self.isArray:
			raise TypeError("Is Not An Array")
		res = self.apiPlug.elementByLogicalIndex(index)
		isinstance(res,API_Plug)
		return res
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def elementByPhysicalIndex(self,index):
		""""""
		if not self.isArray():
			raise TypeError("Is Not An Array")
		res = self.apiPlug.elementByPhysicalIndex(index)
		isinstance(res,API_Plug)
		return res
	#----------------------------------------------------------------------
	@property
	def listEnums(self):
		res = cmds.attributeQuery( self.plug_name, node=self.node, listEnums=True )
		if len(res) == 1:
			return res[0].replace("None:","").replace("None=1:","").split(":")
		else:
			return None
	#----------------------------------------------------------------------
	@property
	def siblings(self):
		res = to_DML_Nodes([self.node.name + "." + child for child in General_Utils.none_To_List(cmds.attributeQuery( self.plug_name, node=self.node, listSiblings=True ))])	
	#----------------------------------------------------------------------
	@property
	def defaults(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, listDefault=True )
	#----------------------------------------------------------------------
	@property
	def exists(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, exists=True )
	#----------------------------------------------------------------------
	@property
	def isConnectable(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, connectable=True )
	#----------------------------------------------------------------------
	@property
	def isMessage(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, message=True )
	#----------------------------------------------------------------------
	@property
	def isEnum(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, enum=True )
	#----------------------------------------------------------------------
	@property
	def isHidden(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, hidden=True )
	#----------------------------------------------------------------------
	@property
	def indexMatters(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, indexMatters=True )
	#----------------------------------------------------------------------
	@property
	def isReadable(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, readable=True )
	#----------------------------------------------------------------------
	@property
	def isStorable(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, storable=True )
	#----------------------------------------------------------------------
	@property
	def isWritable(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, writable=True )
	#----------------------------------------------------------------------
	@property
	def isMulti(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, multi=True )
	#----------------------------------------------------------------------
	@property
	def softMaxExists(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, softMaxExists=True )
	#----------------------------------------------------------------------
	@property
	def softMax(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, softMax=True )
	#----------------------------------------------------------------------
	@property
	def softMinExists(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, softMinExists=True )
	#----------------------------------------------------------------------
	@property
	def softMin(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, softMin=True )
	#----------------------------------------------------------------------
	@property
	def softRangeExists(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, softRangeExists=True )
	#----------------------------------------------------------------------
	@property
	def softRange(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, softRange=True )
	#----------------------------------------------------------------------
	@property
	def isusedAsColor(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, isusedAsColor=True )
	#----------------------------------------------------------------------
	@property
	def listParent(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, listParent=True )
	#----------------------------------------------------------------------
	@property
	def niceName(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, niceName=True )
	#----------------------------------------------------------------------
	@property
	def longName(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, longName=True )
	#----------------------------------------------------------------------
	@property
	def shortName(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, shortName=True )
	#----------------------------------------------------------------------
	@property
	def rangeExists(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, rangeExists=True )
	#----------------------------------------------------------------------
	@property
	def minExists(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, minExists=True )
	#----------------------------------------------------------------------
	@property
	def minimum(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, minimum=True )
	#----------------------------------------------------------------------
	@property
	def maxExists(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, maxExists=True )
	#----------------------------------------------------------------------
	@property
	def maximum(self):
		return cmds.attributeQuery( self.plug_name, node=self.node, maximum=True )
	#----------------------------------------------------------------------
	@property
	def settable(self):
		return cmds.getAttr(self.plug_path,settable=True)
	#----------------------------------------------------------------------
	@property
	def attributeType(self):
		return cmds.getAttr(self.plug_path,typ=True)
	#----------------------------------------------------------------------
	@property
	def keyable(self):
		return cmds.getAttr(self.plug_path,keyable=True)
	#----------------------------------------------------------------------
	@keyable.setter
	def keyable(self,val):
		cmds.setAttr(self.plug_path,keyable=val)
	#----------------------------------------------------------------------
	@property
	def lock(self):
		return cmds.getAttr(self.plug_path,lock=True)
	#----------------------------------------------------------------------
	@lock.setter
	def lock(self,val):
		cmds.setAttr(self.plug_path,lock=val)
	#----------------------------------------------------------------------
	@property
	def channelBox(self):
		return cmds.getAttr(self.plug_path,channelBox=True)
	#----------------------------------------------------------------------
	@channelBox.setter
	def channelBox(self,val):
		cmds.setAttr(self.plug_path,channelBox=val)	
	#----------------------------------------------------------------------
	@property
	def size(self):
		return cmds.getAttr(self.plug_path,size=True)
	#----------------------------------------------------------------------
	@property
	def info(self):
		return self.apiPlug.info
	#----------------------------------------------------------------------
	@property
	def isArray(self):
		return self.apiPlug.isArray
	#----------------------------------------------------------------------
	@property
	def isCaching(self):
		return self.apiPlug.isCaching
	#----------------------------------------------------------------------
	@property
	def isChannelBox(self):
		return self.apiPlug.isChannelBox
	#----------------------------------------------------------------------
	@property
	def isChild(self):
		return self.apiPlug.isChild
	#----------------------------------------------------------------------
	@property
	def isCompound(self):
		return self.apiPlug.isCompound
	#----------------------------------------------------------------------
	@property
	def isConnected(self):
		return self.apiPlug.isConnected
	#----------------------------------------------------------------------
	@property
	def isDestination(self):
		return self.apiPlug.isDestination
	#----------------------------------------------------------------------
	@property
	def isDynamic(self):
		return self.apiPlug.isDynamic
	#----------------------------------------------------------------------
	@property
	def isElement(self):
		return self.apiPlug.isElement
	#----------------------------------------------------------------------
	@property
	def isFromReferencedFile(self):
		return self.apiPlug.isFromReferencedFile
	#----------------------------------------------------------------------
	@property
	def isIgnoredWhenRendering(self):
		return self.apiPlug.isIgnoredWhenRendering
	#----------------------------------------------------------------------
	@property
	def isKeyable(self):
		return self.apiPlug.isKeyable
	#----------------------------------------------------------------------
	@property
	def isLocked(self):
		return self.apiPlug.isLocked
	#----------------------------------------------------------------------
	@property
	def isNetworked(self):
		return self.apiPlug.isNetworked
	#----------------------------------------------------------------------
	@property
	def isNull(self):
		return self.apiPlug.isNull
	#----------------------------------------------------------------------
	@property
	def isProcedural(self):
		return self.apiPlug.isProcedural
	#----------------------------------------------------------------------
	@property
	def isSource(self):
		return self.apiPlug.isSource
	#----------------------------------------------------------------------
	def connect(self,attr):
		""""""
		cmds.connectAttr(self,attr,force=True)
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def connections(self,**kwargs):
		""""""
		return cmds.listConnections( self,**kwargs)
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def child(self,index):
		""""""
		if not self.isCompound:
			raise TypeError("Is Not A Compound Plug")
		return self.apiPlug.child(index)
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def parent(self):
		""""""
		if not self.isChild:
			raise TypeError("Is Not A Child Plug")
		self.apiPlug.parent()
	##----------------------------------------------------------------------
	@node_Return_Wrapper
	def array(self):
		""""""
		if not self.isArray:
			raise TypeError("Plug is not an element of a plug array")
		return self.apiPlug.array()
	##----------------------------------------------------------------------
	def destination_plugs(self):
		""""""
		return self.connections(destination=True, source=False,plugs=True)
	##----------------------------------------------------------------------
	def destination_nodes(self):
		""""""
		return self.connections(destination=True, source=False,plugs=False)
	#----------------------------------------------------------------------
	def source_plug(self,plugs=False):
		""""""
		res = None
		if not self.isArray:
			if self.isDestination:
				res = self.connections(destination=False, source=True,plugs=True)
				if len(res):
					res = res[0]
		else:
			res = self.connections(destination=False, source=True,plugs=True)
		isinstance(res,API_Plug)
		return res
	#----------------------------------------------------------------------
	def source_node(self,plugs=False):
		""""""
		res = None
		if not self.isArray:
			if self.isDestination:
				res = self.connections(destination=False, source=True,plugs=False)
				if len(res):
					res = res[0]
			if False:
				isinstance(res,Dependency_Node)
		else:
			res = self.connections(destination=False, source=True,plugs=False)
		return res
	#----------------------------------------------------------------------
	def is_Connected_To(self,plug):
		""""""
		if not self.isArray:
			return cmds.isConnected(self,plug)
		else:
			for elem in self.existingArrayAttributeElements:
				if cmds.isConnected(elem,plug) or cmds.isConnected(plug,elem):
					return True
			return False
	#----------------------------------------------------------------------
	def connect(self,plug):
		""""""
		if not self.isArray:
			if not self.is_Connected_To(plug):
				cmds.connectAttr(self,plug,f=True)
	#----------------------------------------------------------------------
	def disconnect(self,plug):
		""""""
		if not self.isArray:
			if self.is_Connected_To(plug):
				cmds.disconnectAttr(self,plug)
	#----------------------------------------------------------------------
	@property
	def value(self):
		if self.attributeType in MAT.numerical() or self.attributeType == MDT.string:
			return cmds.getAttr(self.plug_path)
		elif self.attributeType in MAT.complex():
			return cmds.getAttr(self.plug_path)[0]
		elif self.attributeType == "message":
			nodes = self.connections(source=True, plugs=False, skipConversionNodes=True)
			return nodes
		else:
			return cmds.getAttr(self.plug_path)
	
	#----------------------------------------------------------------------
	@value.setter
	def value(self,val):
		if self.attributeType in MTypes.NTS or self.attributeType == "string" or self.attributeType == "enum":
			if self.attributeType == "string":
				cmds.setAttr(self,val, type=self.attributeType)
			else:
				cmds.setAttr(self,val)				
		elif self.attributeType == "message":
			if not self.is_Connected_To(val):
				cmds.connectAttr(val,self)
		elif self.attributeType in MTypes.CTS:
			if self.attributeType.endswith("2"):
				cmds.setAttr(self,val[0],val[1],type=self.attributeType)
			elif self.attributeType.endswith("3"):
				cmds.setAttr(self,val[0],val[1],val[2],type=self.attributeType)
		else:
			cmds.setAttr(self,val,type=self.attributeType)

if False:
	API_Plug.apiPlug = OpenMaya.MPlug()
	API_Plug._raw_name = ""
	API_Plug.node = Dependency_Node
	API_Plug.plug_path = ""