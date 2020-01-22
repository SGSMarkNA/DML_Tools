

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class HotBox(UI_Object.UI):
	"""
	This command controls parameters related to the hotBox menubar palette.
	When the command is invoked with no flags, the hotBox is popped up.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.hotBox(**kwargs)
			super(HotBox, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.hotBox(name, exists=True):
				super(HotBox, self).__init__(name)
			else:
				name = cmds.hotBox(name, **kwargs)
				super(HotBox, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def PaneToggleMenus(self):
		"""
		
				Sets the visibilty of a row of menus to on or off.
				
		"""
		return self.query(PaneToggleMenus=True)
	#----------------------------------------------------------------------
	@property
	def animationOnlyMenus(self):
		""""""
		return self.query(animationOnlyMenus=True)
	#----------------------------------------------------------------------
	@property
	def animationToggleMenus(self):
		""""""
		return self.query(animationToggleMenus=True)
	#----------------------------------------------------------------------
	@property
	def clothOnlyMenus(self):
		""""""
		return self.query(clothOnlyMenus=True)
	#----------------------------------------------------------------------
	@property
	def clothToggleMenus(self):
		""""""
		return self.query(clothToggleMenus=True)
	#----------------------------------------------------------------------
	@property
	def commonOnlyMenus(self):
		""""""
		return self.query(commonOnlyMenus=True)
	#----------------------------------------------------------------------
	@property
	def commonToggleMenus(self):
		""""""
		return self.query(commonToggleMenus=True)
	#----------------------------------------------------------------------
	@property
	def customMenuSetsToggleMenus(self):
		""""""
		return self.query(customMenuSetsToggleMenus=True)
	#----------------------------------------------------------------------
	@property
	def displayHotbox(self):
		""""""
		return self.query(displayHotbox=True)
	#----------------------------------------------------------------------
	@property
	def displayStyle(self):
		"""
		
				Returns a string that identifies the flag used to set the current
				display style. The results can be dh, dzo, or
				dco, depending on  which style the hotBox is using at the moment.
				
		"""
		return self.query(displayStyle=True)
	#----------------------------------------------------------------------
	@property
	def displayZonesOnly(self):
		""""""
		return self.query(displayZonesOnly=True)
	#----------------------------------------------------------------------
	@property
	def dynamicsOnlyMenus(self):
		""""""
		return self.query(dynamicsOnlyMenus=True)
	#----------------------------------------------------------------------
	@property
	def dynamicsToggleMenus(self):
		""""""
		return self.query(dynamicsToggleMenus=True)
	#----------------------------------------------------------------------
	@property
	def liveOnlyMenus(self):
		""""""
		return self.query(liveOnlyMenus=True)
	#----------------------------------------------------------------------
	@property
	def liveToggleMenus(self):
		""""""
		return self.query(liveToggleMenus=True)
	#----------------------------------------------------------------------
	@property
	def modelingOnlyMenus(self):
		""""""
		return self.query(modelingOnlyMenus=True)
	#----------------------------------------------------------------------
	@property
	def modelingToggleMenus(self):
		""""""
		return self.query(modelingToggleMenus=True)
	#----------------------------------------------------------------------
	@property
	def noKeyPress(self):
		"""
		
				Normally the hotbox is popped by a pressing a keyboard key. Use the
				nkp flag to pop the hotbox from a device other than the keyboard
				(still use the rl flag to unpop the hotbox).
				
		"""
		return self.query(noKeyPress=True)
	#----------------------------------------------------------------------
	@property
	def polygonsOnlyMenus(self):
		""""""
		return self.query(polygonsOnlyMenus=True)
	#----------------------------------------------------------------------
	@property
	def polygonsToggleMenus(self):
		""""""
		return self.query(polygonsToggleMenus=True)
	#----------------------------------------------------------------------
	@property
	def release(self):
		"""
		
				Action to be called on the release of the key which invoked the hotbox
				
		"""
		return self.query(release=True)
	#----------------------------------------------------------------------
	@property
	def renderingOnlyMenus(self):
		""""""
		return self.query(renderingOnlyMenus=True)
	#----------------------------------------------------------------------
	@property
	def renderingToggleMenus(self):
		""""""
		return self.query(renderingToggleMenus=True)
	#----------------------------------------------------------------------
	@property
	def riggingOnlyMenus(self):
		""""""
		return self.query(riggingOnlyMenus=True)
	#----------------------------------------------------------------------
	@property
	def riggingToggleMenus(self):
		""""""
		return self.query(riggingToggleMenus=True)
	#----------------------------------------------------------------------
	@property
	def rmbPopups(self):
		"""
		
				Enables/Disables a popup menu of the current function set.
				This popup menu appear when the right mouse button is pressed
				in the center zone of the hotbox.
				
		"""
		return self.query(rmbPopups=True)
	#----------------------------------------------------------------------
	@property
	def showAllToggleMenus(self):
		"""
		
				Sets the visibility of all menus to on or off.
				When queried, will only return true if all menu rows are visible.
				
		"""
		return self.query(showAllToggleMenus=True)
	#----------------------------------------------------------------------
	@property
	def surfacesOnlyMenus(self):
		""""""
		return self.query(surfacesOnlyMenus=True)
	#----------------------------------------------------------------------
	@property
	def surfacesToggleMenus(self):
		""""""
		return self.query(surfacesToggleMenus=True)
	#----------------------------------------------------------------------
	@property
	def transparenyLevel(self):
		"""
		
				The percentage of transparency, from 0 to 100.
				Currently, only the values 0, 25, 50, 75 and 100 are
				supported.  Any other values will be rounded off
				to the nearest supported value.
				
		"""
		return self.query(transparenyLevel=True)