import maya.cmds as cmds
from . import Transform 
#from ...General_Utils import flatten

########################################################################
class Group(Transform):
	MAYA_NODE_TYPE_RELATION = None
	#----------------------------------------------------------------------
	@classmethod
	def createNode(cls,*args,**kwargs):
		""""""
		name = kwargs.get("n",kwargs.get("name",None))
		if not name is None:
			if cmds.objExists(name):
				return name
		if len(args):
			res = cmds.group(*args,**kwargs)
		else:
			res = cmds.group(**kwargs)
		return res