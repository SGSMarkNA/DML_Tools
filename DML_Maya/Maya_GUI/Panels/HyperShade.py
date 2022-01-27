

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class HyperShade(UI_Object.UI):
	"""
	Commands for shader editing in the hypergraph
		  
	      render, hypergraph, shader, hypershade
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.hyperShade(**kwargs)
			super(HyperShade, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.hyperShade(name, exists=True):
				super(HyperShade, self).__init__(name)
			else:
				name = cmds.hyperShade(name, **kwargs)
				super(HyperShade, self).__init__(name, **dict(qtParent=parent))