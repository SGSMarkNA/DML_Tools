

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class WebBrowserPrefs (Obsolete)(UI_Object.UI):
	"""
	This command is obsolete and will be removed in a future version of Maya.
	The internal web browser of Maya has been replaced by a plug-in which allows your own browser to connect with Maya.
	Please refer help for information on how to setup communication of Maya with external web browser application.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.webBrowserPrefs (Obsolete)(**kwargs)
			super(WebBrowserPrefs (Obsolete), self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.webBrowserPrefs (Obsolete)(name, exists=True):
				super(WebBrowserPrefs (Obsolete), self).__init__(name)
			else:
				name = cmds.webBrowserPrefs (Obsolete)(name, **kwargs)
				super(WebBrowserPrefs (Obsolete), self).__init__(name, **dict(qtParent=parent))