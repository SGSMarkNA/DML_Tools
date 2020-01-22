

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class LoadUI(UI_Object.UI):
	"""
	loadUI command allows loading of a user interface created in Trolltech 
	Some Qt classes have equivalents in Maya.  If a widget's class is recognized, the Maya-equivelent will be created instead.
	
	Any dynamic properties on a widget which start with a '-' character will be treated as a MEL flag/value pair.  Similarly, any which start with a '+' will be treated as a Python flag/value pair.  Such pairs will be applied to the widget upon creation.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.loadUI(**kwargs)
			super(LoadUI, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.loadUI(name, exists=True):
				super(LoadUI, self).__init__(name)
			else:
				name = cmds.loadUI(name, **kwargs)
				super(LoadUI, self).__init__(name, **dict(qtParent=parent))