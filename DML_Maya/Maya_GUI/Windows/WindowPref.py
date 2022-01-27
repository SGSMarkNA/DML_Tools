

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class WindowPref(UI_Object.UI):
	"""
	Create or modify preferred window attributes.  The size and position
	of a window is retained during and between application sessions.  A
	default window preference is created when a window is closed.  Window
	preferences must be named and, consequently, only affect the window
	with a matching name.
	
	Note that window preferences are not applied to the main Maya window
	nor the Command window.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.windowPref(**kwargs)
			super(WindowPref, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.windowPref(name, exists=True):
				super(WindowPref, self).__init__(name)
			else:
				name = cmds.windowPref(name, **kwargs)
				super(WindowPref, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def enableAll(self):
		"""
		
				Enable/disable all window preferences.  Preferences are enabled
				by default.  Set this flag to false and window's will ignore all
				preference values.
				
		"""
		return self.query(enableAll=True)
	#----------------------------------------------------------------------
	def get_height(self):
		"""
		
				Height of the window.
				
		"""
		return self.query(height=True)
	#----------------------------------------------------------------------
	def set_height(self, value):
		"""
		
				Height of the window.
				
		"""
		self.edit(height=value)
	#----------------------------------------------------------------------
	height = property(get_height, set_height)
	#----------------------------------------------------------------------
	def get_leftEdge(self):
		"""
		
				Left edge position of the window.
				
		"""
		return self.query(leftEdge=True)
	#----------------------------------------------------------------------
	def set_leftEdge(self, value):
		"""
		
				Left edge position of the window.
				
		"""
		self.edit(leftEdge=value)
	#----------------------------------------------------------------------
	leftEdge = property(get_leftEdge, set_leftEdge)
	#----------------------------------------------------------------------
	def get_maximized(self):
		"""
		
				Maximize the window.
				
		"""
		return self.query(maximized=True)
	#----------------------------------------------------------------------
	def set_maximized(self, value):
		"""
		
				Maximize the window.
				
		"""
		self.edit(maximized=value)
	#----------------------------------------------------------------------
	maximized = property(get_maximized, set_maximized)
	#----------------------------------------------------------------------
	@property
	def parentMain(self):
		"""
		
				Set whether window is parented to main application window. Windows only.
				
		"""
		return self.query(parentMain=True)
	#----------------------------------------------------------------------
	def get_topEdge(self):
		"""
		
				Top edge position of the window.
				
		"""
		return self.query(topEdge=True)
	#----------------------------------------------------------------------
	def set_topEdge(self, value):
		"""
		
				Top edge position of the window.
				
		"""
		self.edit(topEdge=value)
	#----------------------------------------------------------------------
	topEdge = property(get_topEdge, set_topEdge)
	#----------------------------------------------------------------------
	def get_topLeftCorner(self):
		"""
		
				Top and left edge position of the window.
				
		"""
		return self.query(topLeftCorner=True)
	#----------------------------------------------------------------------
	def set_topLeftCorner(self, value):
		"""
		
				Top and left edge position of the window.
				
		"""
		self.edit(topLeftCorner=value)
	#----------------------------------------------------------------------
	topLeftCorner = property(get_topLeftCorner, set_topLeftCorner)
	#----------------------------------------------------------------------
	def get_width(self):
		"""
		
				Width of the window.
				
		"""
		return self.query(width=True)
	#----------------------------------------------------------------------
	def set_width(self, value):
		"""
		
				Width of the window.
				
		"""
		self.edit(width=value)
	#----------------------------------------------------------------------
	width = property(get_width, set_width)
	#----------------------------------------------------------------------
	def get_widthHeight(self):
		"""
		
				Width and height of the window.
				
		"""
		return self.query(widthHeight=True)
	#----------------------------------------------------------------------
	def set_widthHeight(self, value):
		"""
		
				Width and height of the window.
				
		"""
		self.edit(widthHeight=value)
	#----------------------------------------------------------------------
	widthHeight = property(get_widthHeight, set_widthHeight)