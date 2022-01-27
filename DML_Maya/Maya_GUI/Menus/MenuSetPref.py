

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class MenuSetPref(UI_Object.UI):
	"""
	Provides the functionality to save and load menuSets between sessions of Maya.
	For Internal Use Only!
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.menuSetPref(**kwargs)
			super(MenuSetPref, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.menuSetPref(name, exists=True):
				super(MenuSetPref, self).__init__(name)
			else:
				name = cmds.menuSetPref(name, **kwargs)
				super(MenuSetPref, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def exists(self):
		"""
		
				Returns whether the menuSet preferences file exists or not.
				
		"""
		return self.query(exists=True)
	#----------------------------------------------------------------------
	def force(self,value):
		"""
		
				Forces a specified operation to continue even if errors are encountered (such as invalid
				preferences).
				
		"""
		self.edit(force=value)
	#----------------------------------------------------------------------
	@property
	def version(self):
		"""
		
				The base version string which is saved out to file. It is also checked upon loading
				in order to indicate changes in the default prefs since the prefs were last saved out.
				
		"""
		return self.query(version=True)