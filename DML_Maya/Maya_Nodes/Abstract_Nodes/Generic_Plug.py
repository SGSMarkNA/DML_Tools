
import maya.api.OpenMaya as OpenMaya
import maya.cmds as cmds
from ..Base_Nodes.API_Plug import API_Plug
from ...Decorators.Node_Wraper_Manager import node_Return_Wrapper,to_DML_Node,to_DML_Nodes
from ... import General_Utils



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
class Plug(API_Plug):
	MAYA_PLUG_TYPE_RELATION   = None
	RETURN_OVERIDE_CHECK_TYPE = None
	
	##----------------------------------------------------------------------
	#@node_Return_Wrapper
	#def elementByLogicalIndex(self,index):
		#""""""
		#if not self.isArray:
			#raise TypeError("Is Not An Array")
		#return super(MPlug,self).elementByLogicalIndex(index)
	##----------------------------------------------------------------------
	#@node_Return_Wrapper
	#def elementByPhysicalIndex(self,index):
		#""""""
		#if not self.isArray():
			#raise TypeError("Is Not An Array")
		#return super(MPlug,self).elementByPhysicalIndex(index)		
	##----------------------------------------------------------------------
	#def get_Elements(self):
		#num_elements = self.evaluateNumElements()
		#item_list = [self.elementByLogicalIndex(index) for index in range(num_elements)]
		#return item_list
	##----------------------------------------------------------------------
	#def get_Existing_Array_Attribute_Indices(self):
		#""""""
		#indices = OM.MIntArray()
		#if self.isArray():
			#indices = self.getExistingArrayAttributeIndices(indices)
		#return list(indices)
	##----------------------------------------------------------------------
	#def iterate_Element_With_Connections(self):
		#if self.isArray:
			#indices = self.get_Existing_Array_Attribute_Indices()
			#for index in indices:
				#elem = self.elementByPhysicalIndex(index)
				#if elem.isConnected:
					#yield MPlug(elem)
	##----------------------------------------------------------------------
	#def elements_With_Connections(self):
		#if self.isArray:
			#item_list = list(self.iterate_Element_With_Connections())
			#return item_list
		#else:
			#return []
	##----------------------------------------------------------------------
	#def get_Next_Unconneced_Array_Element(self):
		
		#if not self.isArray():
			#raise TypeError("not an Array Plug")
		
		#num_elements = self.evaluateNumElements()
		#indices      = self.get_Existing_Array_Attribute_Indices()
		
		#for index in range(num_elements):
			#if not index == indices[index]:
				#return self.elementByLogicalIndex(index)
			#if not self.elementByLogicalIndex(index).isConnected:
				#return self.elementByLogicalIndex(index)
		#return self.elementByLogicalIndex(num_elements)
	##----------------------------------------------------------------------
	#def get_Element_Source_Objects(self):
		#""""""
		#res = []
		#for elem in self.elements_With_Connections():
			#isinstance(elem,MPlug)
			#s = elem.source()
			#if not s.isNull:
				#res.append(s.node())
		#return res
	##----------------------------------------------------------------------
	#def get_Destinations_Objects_By_TypeId(self,typ):
		#""""""
		#res = []
		#for obj in self.get_Destinations_Object():
			#if is_MObject_Type(obj, typ):
				#res.append(obj)
		#return res
	##----------------------------------------------------------------------
	#def get_Destinations_Object(self):
		#""""""
		#res = []
		#for dest in self.destinations():
			#isinstance(dest,MPlug)
			#n = dest.node()
			#if not n.isNull():
				#res.append(n)
		#return res
	##----------------------------------------------------------------------
	#def is_Object_A_Destination(self,mobject):
		#""""""
		#for obj in self.get_Destinations_Object():
			#if obj == mobject:
				#return True
		#return False
	##----------------------------------------------------------------------
	#def is_Object_A_Source_In_Connected_Elements(self,mobject):
		#""""""
		#for obj in self.get_Element_Source_Objects():
			#if obj == mobject:
				#return True
		#return False
	##----------------------------------------------------------------------
	#def get_Element_Connected_To_Object_As_Source(self,mobject):
		#""""""
		#if self.is_Object_A_Source_In_Connected_Elements(mobject):
			#for elem in self.elements_With_Connections():
				#isinstance(elem,MPlug)
				#if elem.source().node() == mobject:
					#return elem
		#return MPlug()
		