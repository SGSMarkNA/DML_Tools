

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class HotkeyCtx(UI_Object.UI):
	"""
	This command sets the hotkey context for the entire application.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.hotkeyCtx(**kwargs)
			super(HotkeyCtx, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.hotkeyCtx(name, exists=True):
				super(HotkeyCtx, self).__init__(name)
			else:
				name = cmds.hotkeyCtx(name, **kwargs)
				super(HotkeyCtx, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def clientArray(self):
		"""
		
				Returns an array of the all context clients associated to the hotkey context type.
				This flag needs to be used with the flag "type" which specifies the context type.
				
		"""
		return self.query(clientArray=True)
	#----------------------------------------------------------------------
	@property
	def currentClient(self):
		"""
		
				Current client for the given hotkey context type.
				This flag needs to be used with the flag "type" which specifies the context type.
				
		"""
		return self.query(currentClient=True)
	#----------------------------------------------------------------------
	@property
	def type(self):
		"""
		
				Specifies the context type. It's used together with the other flags such as
				"currentClient", "addClient", "removeClient" and so on.
				
		"""
		return self.query(type=True)
	#----------------------------------------------------------------------
	@property
	def typeArray(self):
		"""
		
				Returns a string array containing the names of all hotkey context types,
				ordered by priority.
				
		"""
		return self.query(typeArray=True)
	#----------------------------------------------------------------------
	@property
	def typeExists(self):
		"""
		
				Returns true|false depending upon whether the specified hotkey context type
				exists.
				      In query mode, this flag needs a value.
				
		"""
		return self.query(typeExists=True)