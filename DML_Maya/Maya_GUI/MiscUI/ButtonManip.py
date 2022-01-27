

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class ButtonManip(UI_Object.UI):
	"""
	This creates a button manipulator. This manipulator has a position in
	space and a triad manip for positioning. When you click on the top
	part of the manip, the command defined by the first argument is
	executed. The command is associated with the manipulator when it is
	created.
	
	If a dag object is included on the command line, the manip will be
	parented to the object. This means moving the object will move the
	manip. You can move the manip independently of the object using its
	triad.
	
	Note that a buttonManip may not be parented to more than one object.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.buttonManip(**kwargs)
			super(ButtonManip, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.buttonManip(name, exists=True):
				super(ButtonManip, self).__init__(name)
			else:
				name = cmds.buttonManip(name, **kwargs)
				super(ButtonManip, self).__init__(name, **dict(qtParent=parent))