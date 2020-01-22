import maya.cmds as cmds
from ..Abstract_Nodes import Dag_Node
from ...General_Utils import flatten
	
########################################################################
class Transform(Dag_Node):
	MAYA_NODE_TYPE_RELATION = "transform"
	#----------------------------------------------------------------------
	def moveIt(self,*args,**kwargs):
		""""""
		args = flatten(args) + [self.name]
		cmds.move(*args,**kwargs)
	#----------------------------------------------------------------------
	def rotateIt(self,*args,**kwargs):
		""""""
		args = flatten(args) + [self.name]
		cmds.rotate(*args,**kwargs)
	#----------------------------------------------------------------------
	def scaleIt(self,*args,**kwargs):
		""""""
		args = flatten(args) + [self.name]
		cmds.scale(*args,**kwargs)
	#----------------------------------------------------------------------
	def freezeTransformations(self,translate=True,rotate=True,scale=True):
		""""""
		cmds.makeIdentity(self,apply=True, rotate=rotate, scale=scale, translate=translate)