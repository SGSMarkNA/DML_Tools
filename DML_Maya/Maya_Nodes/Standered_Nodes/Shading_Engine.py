
import maya.cmds as cmds
from ..Abstract_Nodes.Selection_Set import Selection_Set

__all__ = ["Shading_Engine"]
########################################################################
class Shading_Engine(Selection_Set):
	MAYA_NODE_TYPE_RELATION = "shadingEngine"
	#----------------------------------------------------------------------
	@classmethod
	def createNode(self,*args,**kwargs):
		""""""
		name = kwargs.pop("name",None)
		kwargs = dict(renderable=True,noSurfaceShader=True,empty=True)
		if name is not None:
			kwargs['name']=name
		return cmds.sets(**kwargs)
	#----------------------------------------------------------------------
	def include(self,*items):
		#self.__rshift__(items)
		if len(items):
			cmds.sets(*items,forceElement=self)
	##----------------------------------------------------------------------
	def Assine_To_Material(self,shader):
		shader_plug = str(shader)+".outColor"
		try:
			cmds.connectAttr(shader_plug,self.surfaceShader,force=True)
		except:
			pass
