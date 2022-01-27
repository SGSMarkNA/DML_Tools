

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class HotkeySet(UI_Object.UI):
	"""
	Manages hotkey sets in Maya. A hotkey set holds hotkey to command mapping information.
	Default hotkey sets are hotkey sets that are shipped together with Maya. They are locked and cannot be altered.
	
	A new hotkey set is always duplicated from an existing hotkey set. In create mode, users can choose to specify
	which hotkey set to duplicate by using the -source flag. A duplicated hotkey set is independent from the source
	hotkey set.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.hotkeySet(**kwargs)
			super(HotkeySet, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.hotkeySet(name, exists=True):
				super(HotkeySet, self).__init__(name)
			else:
				name = cmds.hotkeySet(name, **kwargs)
				super(HotkeySet, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def get_current(self):
		"""
		
				Sets the hotkey set as the current active hotkey set. In query mode, returns the name of
				the current hotkey set.
				
		"""
		return self.query(current=True)
	#----------------------------------------------------------------------
	def set_current(self, value):
		"""
		
				Sets the hotkey set as the current active hotkey set. In query mode, returns the name of
				the current hotkey set.
				
		"""
		self.edit(current=value)
	#----------------------------------------------------------------------
	current = property(get_current, set_current)
	#----------------------------------------------------------------------
	def delete(self,value):
		"""
		
				Deletes the hotkey set if it exists. Other flags are ignored.
				Returns true|false depending on the delete operation.
				
		"""
		self.edit(delete=value)
	#----------------------------------------------------------------------
	def export(self,value):
		"""
		
				Exports a hotkey set. The argument is used to specify a full path of the output file.
				
		"""
		self.edit(export=value)
	#----------------------------------------------------------------------
	@property
	def hotkeySetArray(self):
		"""
		
				Returns a string array of all existing hotkey set names.
				
		"""
		return self.query(hotkeySetArray=True)
	#----------------------------------------------------------------------
	def ip(self,value):
		"""
		
				Imports a hotkey set. The argument is used to specify a full path of the hotkey set file to import.
				
		"""
		self.edit(ip=value)
	#----------------------------------------------------------------------
	def rename(self,value):
		"""
		
				Renames an existing hotkey set. All white spaces will be replaced with '_' during operation.
				
		"""
		self.edit(rename=value)