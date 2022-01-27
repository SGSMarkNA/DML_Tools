

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class ScriptedPanelType(UI_Object.UI):
	"""
	This command defines the callbacks for a type of scripted panel.  The panel type
	created by this command is then used when creating a scripted panel.  See also
	the 'scriptedPanel' command.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.scriptedPanelType(**kwargs)
			super(ScriptedPanelType, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.scriptedPanelType(name, exists=True):
				super(ScriptedPanelType, self).__init__(name)
			else:
				name = cmds.scriptedPanelType(name, **kwargs)
				super(ScriptedPanelType, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def get_addCallback(self):
		"""
		
				This flag specifies the callback procedure for adding the panel
				to a particular control layout.  The parent layout is guaranteed to be
				the current default layout when the proc is called.  If its name is
				required then it can be queried with 'setParent -q'.  Any editors should
				be parented here.
				global proc procName (string $panelName) { .... }
				
		"""
		return self.query(addCallback=True)
	#----------------------------------------------------------------------
	def set_addCallback(self, value):
		"""
		
				This flag specifies the callback procedure for adding the panel
				to a particular control layout.  The parent layout is guaranteed to be
				the current default layout when the proc is called.  If its name is
				required then it can be queried with 'setParent -q'.  Any editors should
				be parented here.
				global proc procName (string $panelName) { .... }
				
		"""
		self.edit(addCallback=value)
	#----------------------------------------------------------------------
	addCallback = property(get_addCallback, set_addCallback)
	#----------------------------------------------------------------------
	def get_copyStateCallback(self):
		"""
		
				This flag specifies the callback procedure for copying the state of
				the panel when a tear-off copy of the panel is made.  The callback proc has the form:
				global proc procName (string $panelName, string $newPanelName) { .... }
				This procedure will be executed immediately after the addCallback
				procedure has finished executing. At that point, the copied panel will be
				fully created and accessible to facilitate copying of panel settings.
				Note: the addCallback procedure is called after the createCallback
				procedure has been called.
				
		"""
		return self.query(copyStateCallback=True)
	#----------------------------------------------------------------------
	def set_copyStateCallback(self, value):
		"""
		
				This flag specifies the callback procedure for copying the state of
				the panel when a tear-off copy of the panel is made.  The callback proc has the form:
				global proc procName (string $panelName, string $newPanelName) { .... }
				This procedure will be executed immediately after the addCallback
				procedure has finished executing. At that point, the copied panel will be
				fully created and accessible to facilitate copying of panel settings.
				Note: the addCallback procedure is called after the createCallback
				procedure has been called.
				
		"""
		self.edit(copyStateCallback=value)
	#----------------------------------------------------------------------
	copyStateCallback = property(get_copyStateCallback, set_copyStateCallback)
	#----------------------------------------------------------------------
	def get_createCallback(self):
		"""
		
				This flag specifies the callback procedure for initially creating
				the panel object.  No UI should be created here.  Any editors owned
				by the panel should be created here unparented.
				The callback proc has the form:
				global proc procName (string $panelName) { .... }
				
		"""
		return self.query(createCallback=True)
	#----------------------------------------------------------------------
	def set_createCallback(self, value):
		"""
		
				This flag specifies the callback procedure for initially creating
				the panel object.  No UI should be created here.  Any editors owned
				by the panel should be created here unparented.
				The callback proc has the form:
				global proc procName (string $panelName) { .... }
				
		"""
		self.edit(createCallback=value)
	#----------------------------------------------------------------------
	createCallback = property(get_createCallback, set_createCallback)
	#----------------------------------------------------------------------
	def get_customView(self):
		"""
		
				This flag specifies if this view is a custom 3d view for
				MPx3dModelView types. This flag should only be used for
				MPx3dModelView types.
				
		"""
		return self.query(customView=True)
	#----------------------------------------------------------------------
	def set_customView(self, value):
		"""
		
				This flag specifies if this view is a custom 3d view for
				MPx3dModelView types. This flag should only be used for
				MPx3dModelView types.
				
		"""
		self.edit(customView=value)
	#----------------------------------------------------------------------
	customView = property(get_customView, set_customView)
	#----------------------------------------------------------------------
	def get_deleteCallback(self):
		"""
		
				This flag specifies the callback procedure for final deletion of
				the panel.  The callback proc has the form:
				global proc procName (string $panelName) { .... }
				
		"""
		return self.query(deleteCallback=True)
	#----------------------------------------------------------------------
	def set_deleteCallback(self, value):
		"""
		
				This flag specifies the callback procedure for final deletion of
				the panel.  The callback proc has the form:
				global proc procName (string $panelName) { .... }
				
		"""
		self.edit(deleteCallback=value)
	#----------------------------------------------------------------------
	deleteCallback = property(get_deleteCallback, set_deleteCallback)
	#----------------------------------------------------------------------
	def get_hotkeyCtxClient(self):
		"""
		
				This flag is used to specify the name of the hotkey context client for this panel type.
				By default, it is the same as the panel type.
				
		"""
		return self.query(hotkeyCtxClient=True)
	#----------------------------------------------------------------------
	def set_hotkeyCtxClient(self, value):
		"""
		
				This flag is used to specify the name of the hotkey context client for this panel type.
				By default, it is the same as the panel type.
				
		"""
		self.edit(hotkeyCtxClient=value)
	#----------------------------------------------------------------------
	hotkeyCtxClient = property(get_hotkeyCtxClient, set_hotkeyCtxClient)
	#----------------------------------------------------------------------
	def get_initCallback(self):
		"""
		
				This flag specifies the callback procedure for the initialize
				callback.  This will be called on file -new and file -open to give the
				panel an opportunity to re-initialize to a starting state, if required.
				The panel may be parented or unparented at this time.
				The callback proc has the form:
				global proc procName (string $panelName) { .... }
				
		"""
		return self.query(initCallback=True)
	#----------------------------------------------------------------------
	def set_initCallback(self, value):
		"""
		
				This flag specifies the callback procedure for the initialize
				callback.  This will be called on file -new and file -open to give the
				panel an opportunity to re-initialize to a starting state, if required.
				The panel may be parented or unparented at this time.
				The callback proc has the form:
				global proc procName (string $panelName) { .... }
				
		"""
		self.edit(initCallback=value)
	#----------------------------------------------------------------------
	initCallback = property(get_initCallback, set_initCallback)
	#----------------------------------------------------------------------
	def get_label(self):
		"""
		
				Label for the panel
				
		"""
		return self.query(label=True)
	#----------------------------------------------------------------------
	def set_label(self, value):
		"""
		
				Label for the panel
				
		"""
		self.edit(label=value)
	#----------------------------------------------------------------------
	label = property(get_label, set_label)
	#----------------------------------------------------------------------
	def get_obsolete(self):
		"""
		
				This flag specifies that this type is no longer used in Maya.
				
		"""
		return self.query(obsolete=True)
	#----------------------------------------------------------------------
	def set_obsolete(self, value):
		"""
		
				This flag specifies that this type is no longer used in Maya.
				
		"""
		self.edit(obsolete=value)
	#----------------------------------------------------------------------
	obsolete = property(get_obsolete, set_obsolete)
	#----------------------------------------------------------------------
	def get_removeCallback(self):
		"""
		
				This flag specifies the callback procedure for removing the panel
				from its current control layout.  Any editors should be unparented here.
				The callback proc has the form:
				global proc procName (string $panelName) { .... }
				
		"""
		return self.query(removeCallback=True)
	#----------------------------------------------------------------------
	def set_removeCallback(self, value):
		"""
		
				This flag specifies the callback procedure for removing the panel
				from its current control layout.  Any editors should be unparented here.
				The callback proc has the form:
				global proc procName (string $panelName) { .... }
				
		"""
		self.edit(removeCallback=value)
	#----------------------------------------------------------------------
	removeCallback = property(get_removeCallback, set_removeCallback)
	#----------------------------------------------------------------------
	def get_retainOnFileOpen(self):
		"""
		
				This flag specifies if panels of this type should be retained after
				restoring panel cofiguration during file open. Default value is false.
				
		"""
		return self.query(retainOnFileOpen=True)
	#----------------------------------------------------------------------
	def set_retainOnFileOpen(self, value):
		"""
		
				This flag specifies if panels of this type should be retained after
				restoring panel cofiguration during file open. Default value is false.
				
		"""
		self.edit(retainOnFileOpen=value)
	#----------------------------------------------------------------------
	retainOnFileOpen = property(get_retainOnFileOpen, set_retainOnFileOpen)
	#----------------------------------------------------------------------
	def get_saveStateCallback(self):
		"""
		
				This flag specifies the callback procedure for saving the state of
				the panel.  The callback proc has the form:
				global proc string procName (string $panelName) { .... }
				Note that the proc returns a string.  This string will be executed after
				the createCallback has been called to facilitate restoring the panel
				state.
				
		"""
		return self.query(saveStateCallback=True)
	#----------------------------------------------------------------------
	def set_saveStateCallback(self, value):
		"""
		
				This flag specifies the callback procedure for saving the state of
				the panel.  The callback proc has the form:
				global proc string procName (string $panelName) { .... }
				Note that the proc returns a string.  This string will be executed after
				the createCallback has been called to facilitate restoring the panel
				state.
				
		"""
		self.edit(saveStateCallback=value)
	#----------------------------------------------------------------------
	saveStateCallback = property(get_saveStateCallback, set_saveStateCallback)
	#----------------------------------------------------------------------
	def get_unique(self):
		"""
		
				This flag specifies if only one instance of this type of panel can exist
				at a given time.
				
		"""
		return self.query(unique=True)
	#----------------------------------------------------------------------
	def set_unique(self, value):
		"""
		
				This flag specifies if only one instance of this type of panel can exist
				at a given time.
				
		"""
		self.edit(unique=value)
	#----------------------------------------------------------------------
	unique = property(get_unique, set_unique)