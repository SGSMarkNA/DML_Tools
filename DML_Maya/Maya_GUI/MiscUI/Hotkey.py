

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class Hotkey(UI_Object.UI):
	"""
	This command sets the single-key hotkeys for the entire application.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.hotkey(**kwargs)
			super(Hotkey, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.hotkey(name, exists=True):
				super(Hotkey, self).__init__(name)
			else:
				name = cmds.hotkey(name, **kwargs)
				super(Hotkey, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def altModifier(self):
		""""""
		return self.query(altModifier=True)
	#----------------------------------------------------------------------
	@property
	def ctrlModifier(self):
		"""
		
				The Ctrl key must be pressed to get the hotkey.
				Note that if menu item accelerator keys are being used
				(menuItem -ke/keyEquivalent), then the accelerator key
				settings override the hotkey settings.
				
		"""
		return self.query(ctrlModifier=True)
	#----------------------------------------------------------------------
	@property
	def ctxClient(self):
		"""
		
				Specifies the hotkey context. It is used together with the other flags to modify or query
				the hotkey for a certain hotkey context. If it is not specified, the global hotkey context will be taken into
				account. Check hotkeyCtx command to see how the hotkeys work with the hotkey contexts.
				
		"""
		return self.query(ctxClient=True)
	#----------------------------------------------------------------------
	@property
	def name(self):
		"""
		
				The name of the namedCommand object that will be executed when the key is pressed.
				
		"""
		return self.query(name=True)
	#----------------------------------------------------------------------
	@property
	def releaseName(self):
		"""
		
				The name of the namedCommand object that will be executed when the key is released.
				
		"""
		return self.query(releaseName=True)
	#----------------------------------------------------------------------
	@property
	def shiftModifier(self):
		"""
		
				The Shift key must be pressed to get the hotkey.
				
		"""
		return self.query(shiftModifier=True)