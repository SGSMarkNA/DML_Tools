import maya.cmds as cmds
from . import Transform 
from ...General_Utils import flatten
	
########################################################################
class SpaceLocator(Transform):
	RETURN_OVERIDE_CHECK_TYPE = "transform"
	#----------------------------------------------------------------------
	@classmethod
	def _overide_Return_Check(cls,node):
		""""""
		return cmds.listRelatives(node,typ="locator", children=True, shapes=True) != None
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		""""""
		self.locator = None
		child_shapes = self.get_Child_Shapes()
		if len(child_shapes):
			self.locator = child_shapes[0]
	#----------------------------------------------------------------------
	def set_Locator_Scale(self,val):
		""""""
		if self.locator is not None:
			self.locator.localScaleX.value = val
			self.locator.localScaleY.value = val
			self.locator.localScaleZ.value = val
	#----------------------------------------------------------------------
	@classmethod
	def createNode(cls,*args,**kwargs):
		""""""
		res = cmds.spaceLocator(**kwargs)
		return res[0]