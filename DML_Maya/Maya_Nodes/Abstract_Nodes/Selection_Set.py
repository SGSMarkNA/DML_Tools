import maya.cmds as cmds
from ... import General_Utils
from ..Abstract_Nodes.Dependency_Node import Dependency_Node
from ...Decorators.Node_Wraper_Manager import node_Return_Wrapper
from ...Decorators.Node_Lock_Manager import locked_Node_Management


########################################################################
class Selection_Set(Dependency_Node):
	#----------------------------------------------------------------------
	def __init__(self,nodeName):
		super(Selection_Set,self).__init__(nodeName)
		#if False:
			#self.dagSetMembers = Base_Classes.Named_Plug
	#----------------------------------------------------------------------
	def select(self,**kwargs):
		kwargs["noExpand"] = kwargs.pop("noExpand",kwargs.pop("ne", True))
		cmds.select(self,**kwargs)
	#----------------------------------------------------------------------
	@locked_Node_Management
	def clear(self):
		cmds.sets(clear=self)
	#----------------------------------------------------------------------
	def size(self):
		cmds.sets(self,q=True,size=True)
	#----------------------------------------------------------------------
	@locked_Node_Management
	def remove(self,*items):
		items = General_Utils.flatten(items)
		if len(items):
			cmds.sets( items, remove=self)
	#----------------------------------------------------------------------
	@locked_Node_Management
	def add(self,*items,**kwargs):
		items = General_Utils.flatten(items)
		if len(items):
			cmds.sets( items, **kwargs)
	#----------------------------------------------------------------------
	def forceElement(self,*items):
		self.add(*items,forceElement=self)
	#----------------------------------------------------------------------
	def include(self,*items):
		self.add(*items,include=self)
	#----------------------------------------------------------------------
	def addElement(self,*items):
		self.add(*items,addElement=self)
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def intersecting(self,*items):
		items = General_Utils.flatten(items)
		return cmds.sets(items, intersection=self)
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def members(self):
		return cmds.sets(self,q=True)
	#----------------------------------------------------------------------
	def isMember(self, items):
		""""""
		return cmds.sets(items, isMember=self)
	#----------------------------------------------------------------------
	def __contains__(self,item):
		return cmds.sets(item,isMember=self)
