
import maya.cmds as cmds
from .Dependency_Node import Dependency_Node
from ...Decorators.Node_Lock_Manager import locked_Node_Management
from ...Decorators.Node_Wraper_Manager import node_Return_Wrapper,to_DML_Node
import maya.api.OpenMaya as OpenMaya

########################################################################
class Dag_Node(Dependency_Node):
	MAYA_NODE_TYPE_RELATION = "dagNode"
	##----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		if False:
			isinstance(self.apiFn,OpenMaya.MFnDagNode)
	#----------------------------------------------------------------------
	def has_parent(self):
		""""""
		return False if cmds.listRelatives(self, parent=True, path=True) is None else True
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def listRelatives(self,**kwargs):
		""""""
		return cmds.listRelatives(self,**kwargs)
	#----------------------------------------------------------------------
	def get_Parent(self):
		""""""
		res = self.listRelatives(parent=True, path=True)
		if len(res):
			return res[0]
		else:
			return None
	#----------------------------------------------------------------------
	def set_Parent(self,obj):
		""""""
		try:
			if not obj == self.get_Parent():
				cmds.parent(self,obj)
		except:
			pass
	#----------------------------------------------------------------------
	def get_All_Parents(self):
		"""Returns all the parents of this dag node. Normally, this only returns the parent corresponding to the first instance of the object"""
		res = self.listRelatives(allParents=True,path=True)
		return res
	#----------------------------------------------------------------------
	def get_Children(self):
		""""""
		return self.listRelatives(children=True, path=True)
	#----------------------------------------------------------------------
	def add_Children(self,objects):
		""""""
		childern = self.get_Children()
		objects = [obj for obj in objects if not obj in childern]
		if len(objects):
			return cmds.parent(objects,self)
	#----------------------------------------------------------------------
	def get_Child_Shapes(self):
		""""""
		return self.listRelatives(children=True, path=True, shapes=True)
	#----------------------------------------------------------------------
	def has_child_transforms(self):
		""""""
		return cmds.listRelatives(self, children=True, path=True, type="transform") != None
	#----------------------------------------------------------------------
	def find_child(self,name):
		""""""
		res = None
		for child in self.get_Children():
			if child.nice_name == name:
				res = child
				break
		isinstance(res,Dag_Node)
		return res
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def child_transforms(self):
		""""""
		return cmds.ls(cmds.listRelatives(self, children=True, path=True),type='transform')
	#----------------------------------------------------------------------
	def all_transform_Descendents(self):
		""""""
		return self.listRelatives(allDescendents=True, path=True, type='transform')
	#----------------------------------------------------------------------
	def numberOfChildern(self):
		"""Returns A list of child nodes for the given node if node is not given the first item in the selection list is use"""
		childCount = len(self.get_Children())
		return childCount
	#----------------------------------------------------------------------
	def allDescendents(self):
		"""all the children, grand-children etc. of this dag node. If a descendent is instanced, it will appear only once on the list returned. Note that it lists grand-children before childre"""
		return self.listRelatives(allDescendents=True,fullPath=True)
	#----------------------------------------------------------------------
	def get_Object_Center(self,asVector=False):
		res = cmds.objectCenter(self,gl=True)
		if asVector:
			res = OpenMaya.MVector(res)
		return res