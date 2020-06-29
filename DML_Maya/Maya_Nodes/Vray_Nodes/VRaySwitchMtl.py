import maya.cmds as cmds
from .. import Shading_Node

__all__ = ["VRaySwitchMtl"]
########################################################################
class VRaySwitchMtl(Shading_Node):
	MAYA_NODE_TYPE_RELATION = "VRaySwitchMtl"
	#----------------------------------------------------------------------
	@classmethod
	def createNode(cls,**kwargs):
		""""""
		return Shading_Node.createNode("VRaySwitchMtl",**kwargs)
	#----------------------------------------------------------------------
	def Attach_Material(self,material,index):
		""""""
		cmds.connectAttr("{}.outColor".format(material),"{}.material_{}".format(self.name,index),force=True)
		
	#----------------------------------------------------------------------
	def set_Switch_Index(self,index):
		""""""
		self.materialsSwitch.value = float(index)
	#----------------------------------------------------------------------
	def get_Switch_Index(self):
		""""""
		return int(self.materialsSwitch.value)