
import maya.api.OpenMaya as OM
import functools
import sys

#----------------------------------------------------------------------
def DML_Plug_Return_Wrapper(func):
	''''''
	@functools.wraps(func)
	def wrapper(*args, **kws):
		err = None
		try:
			res = func(*args, **kws)
			if isinstance(res,(list,OM.MPlugArray)):
				res = [MPlug(plg) for plg in res]
			elif isinstance(res,OM.MPlug):
				res = MPlug(res)
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
def acquire_MFnDependencyNode(arg):
	""""""
	if isinstance(arg,OM.MObject):
		res = OM.MFnDependencyNode(arg)
	elif isinstance(arg,OM.MFnDependencyNode):
		res = arg
	else:
		raise ValueError("Can not create an MFnDependencyNode from givein input")
	return res

#----------------------------------------------------------------------
def MObjects_To_MSelectionList(objects):
	"""Converts A List Of MObjects Into A MSelectionList"""
	sellist = OM.MSelectionList()
	for obj in objects:
		try:
			sellist.add(obj)
		except:
			pass
	return sellist

#----------------------------------------------------------------------
def is_MObject_Type(obj,typ):
	""""""
	try:
		depend_fn = acquire_MFnDependencyNode(obj)
	except ValueError:
		raise ValueError("arg 1 must be a MObject or MFnDependencyNode")
	
	if not isinstance(typ,(int,str,list,OM.MTypeId)):
		raise ValueError("arg 2 must be a type int,str,MTypeId or a list containg ints,strings,MTypeIds")
	
	if isinstance(typ,list):
		if not all([isinstance(val,(int,str,OM.MTypeId)) for val in typ]):
			raise ValueError("arg 2 list can only contain ints,strings and MTypeIds")
	else:
		typ = [typ]
		
	for t in typ:
		if isinstance(t,OM.MTypeId):
			t=t.id()
		if depend_fn.typeId().id() == t or depend_fn.typeName() == t:
			return True
	return False

########################################################################
class MPlug(OM.MPlug):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,*args):
		""""""
		if not len(args):
			super(MPlug,self).__init__()
		elif len(args) == 1:
			arg = args[0]
			if isinstance(arg,basestring):
				selList = OM.MGlobal.getSelectionListByName(arg)
				if not selList.length():
					raise LookupError("input was not found {}".format(arg))
				plg = selList.getPlug(0)
				arg = plg
			super(MPlug,self).__init__(arg)
		else:
			super(MPlug,self).__init__(*args)
		## WING IDE CODE COMPLEASHION ##
		#if False:
			#isinstance(self.parentProp,MPlug)
			#isinstance(self.sourceProp,MPlug)
			#isinstance(self.arrayProp,MPlug)
	#----------------------------------------------------------------------
	def _wrap_Return(self, arg):
		""""""
		return MPlug(arg)
	#----------------------------------------------------------------------
	def _wrap_Element_Return(self, arg):
		""""""
		return self._wrap_Return(arg)
	#----------------------------------------------------------------------
	def _wrap_Child_Return(self, plg, index):
		""""""
		return self._wrap_Return(plg)
	#----------------------------------------------------------------------
	def _wrap_Parent_Return(self, arg):
		""""""
		return self._wrap_Return(arg)
	#----------------------------------------------------------------------
	def _wrap_Array_Return(self, arg):
		""""""
		return self._wrap_Return(arg)
	#----------------------------------------------------------------------
	def _wrap_Source_Return(self, arg):
		""""""
		return self._wrap_Return(arg)
	#----------------------------------------------------------------------
	@DML_Plug_Return_Wrapper
	def child(self,index):
		""""""
		if not self.isCompound:
			raise TypeError("Is Not A Compound Plug")
		return super(MPlug,self).child(index)
	
	#----------------------------------------------------------------------
	@DML_Plug_Return_Wrapper
	def parent(self):
		""""""
		if not self.isChild:
			raise TypeError("Is Not A Child Plug")
		return super(MPlug,self).parent()
	#----------------------------------------------------------------------
	@DML_Plug_Return_Wrapper
	def array(self):
		""""""
		if not self.isArray:
			raise TypeError("Is Not An Array")
		return super(MPlug,self).array()
	#----------------------------------------------------------------------
	@DML_Plug_Return_Wrapper
	def destinations(self):
		""""""
		res = []
		plug_array = super(MPlug,self).destinations()
		if plug_array.length():
			for plug in plug_array:
				if not plug.isNull:
					res.append(plug)
		return res
	#----------------------------------------------------------------------
	@DML_Plug_Return_Wrapper
	def source(self):
		""""""
		res = super(MPlug,self).source()
		isinstance(res,MPlug)
		return res
	#----------------------------------------------------------------------
	@DML_Plug_Return_Wrapper
	def elementByLogicalIndex(self,index):
		""""""
		if not self.isArray:
			raise TypeError("Is Not An Array")
		return super(MPlug,self).elementByLogicalIndex(index)
	#----------------------------------------------------------------------
	@DML_Plug_Return_Wrapper
	def elementByPhysicalIndex(self,index):
		""""""
		if not self.isArray():
			raise TypeError("Is Not An Array")
		return super(MPlug,self).elementByPhysicalIndex(index)		
	#----------------------------------------------------------------------
	def get_Elements(self):
		num_elements = self.evaluateNumElements()
		item_list = [self.elementByLogicalIndex(index) for index in range(num_elements)]
		return item_list
	#----------------------------------------------------------------------
	def get_Existing_Array_Attribute_Indices(self):
		""""""
		indices = OM.MIntArray()
		if self.isArray():
			indices = self.getExistingArrayAttributeIndices(indices)
		return list(indices)
	#----------------------------------------------------------------------
	def iterate_Element_With_Connections(self):
		if self.isArray:
			indices = self.get_Existing_Array_Attribute_Indices()
			for index in indices:
				elem = self.elementByPhysicalIndex(index)
				if elem.isConnected:
					yield MPlug(elem)
	#----------------------------------------------------------------------
	def elements_With_Connections(self):
		if self.isArray:
			item_list = list(self.iterate_Element_With_Connections())
			return item_list
		else:
			return []
	#----------------------------------------------------------------------
	def get_Next_Unconneced_Array_Element(self):
		
		if not self.isArray():
			raise TypeError("not an Array Plug")
		
		num_elements = self.evaluateNumElements()
		indices      = self.get_Existing_Array_Attribute_Indices()
		
		for index in range(num_elements):
			if not index == indices[index]:
				return self.elementByLogicalIndex(index)
			if not self.elementByLogicalIndex(index).isConnected:
				return self.elementByLogicalIndex(index)
		return self.elementByLogicalIndex(num_elements)
	#----------------------------------------------------------------------
	def get_Element_Source_Objects(self):
		""""""
		res = []
		for elem in self.elements_With_Connections():
			isinstance(elem,MPlug)
			s = elem.source()
			if not s.isNull:
				res.append(s.node())
		return res
	#----------------------------------------------------------------------
	def get_Destinations_Objects_By_TypeId(self,typ):
		""""""
		res = []
		for obj in self.get_Destinations_Object():
			if is_MObject_Type(obj, typ):
				res.append(obj)
		return res
	#----------------------------------------------------------------------
	def get_Destinations_Object(self):
		""""""
		res = []
		for dest in self.destinations():
			isinstance(dest,MPlug)
			n = dest.node()
			if not n.isNull():
				res.append(n)
		return res
	#----------------------------------------------------------------------
	def is_Object_A_Destination(self,mobject):
		""""""
		for obj in self.get_Destinations_Object():
			if obj == mobject:
				return True
		return False
	#----------------------------------------------------------------------
	def is_Object_A_Source_In_Connected_Elements(self,mobject):
		""""""
		for obj in self.get_Element_Source_Objects():
			if obj == mobject:
				return True
		return False
	#----------------------------------------------------------------------
	def get_Element_Connected_To_Object_As_Source(self,mobject):
		""""""
		if self.is_Object_A_Source_In_Connected_Elements(mobject):
			for elem in self.elements_With_Connections():
				isinstance(elem,MPlug)
				if elem.source().node() == mobject:
					return elem
		return MPlug()
	#----------------------------------------------------------------------
	def __getitem__(self, key):
		""""""
		if self.isArray:
			return self.elementByLogicalIndex(key)
		elif self.isCompound():
			return self.child(key)
		else:
			raise TypeError("Is Not An Array or Compound")
	#----------------------------------------------------------------------
	def __getslice__(self, i, j):
		""""""
		if self.isArray:
			return [self.elementByLogicalIndex(index) for index in range(i, j)]
		else:
			raise TypeError("Is Not An Array")
	#----------------------------------------------------------------------
	def __iter__(self):
		""""""
		if self.isArray:
			num_elements = self.numElements()
			for index in range(num_elements):
				yield self.elementByPhysicalIndex(index)
		else:
			raise TypeError("Is Not An Array")
	#----------------------------------------------------------------------
	def __repr__(self):
		""""""
		return '{}("{}")'.format(self.__class__.__name__,self.info)
	#----------------------------------------------------------------------
	def __str__(self):
		""""""
		return self.info()

