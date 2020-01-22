from .. import General_Utils 
########################################################################
class MDT(object):
	__metaclass__ = General_Utils.Singleton	
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
	__metaclass__ = General_Utils.Singleton
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
	__metaclass__ = General_Utils.Singleton
	DTS = ['Int32Array', 'doubleArray', 'lattice', 'matrix', 'mesh', 'nurbsCurve', 'nurbsSurface', 'pointArray', 'string', 'stringArray', 'vectorArray']
	ATS = ['bool', 'byte', 'char', 'TdataCompound','compound', 'double', 'double2', 'double3', 'doubleAngle', 'doubleLinear', 'enum', 'float', 'float2', 'float3', 'fltMatrix', 'long', 'long2', 'long3', 'message', 'reflectance', 'short', 'short2', 'short3', 'spectrum', 'time']
	NTS = ['bool', 'byte', 'char','double', 'doubleAngle', 'doubleLinear','float','floatLinear','long', 'reflectance', 'short','spectrum','time']
	STS = ['bool', 'byte', 'char','double', 'doubleAngle', 'doubleLinear','float','long', 'reflectance', 'short','spectrum','time']
	CTS = ['double2', 'double3','float2', 'float3','long2', 'long3','short2', 'short3']