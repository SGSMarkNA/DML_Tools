

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class WorkspaceControlState(UI_Object.UI):
	"""
	Create or modify preferred window attributes for workspace controls.
	The size and position of a workspace control is retained during application
	sessions (although position only applies to workspace controls that are
	alone in a floating workspace docking panel). A default workspace control
	state is created when a workspace control is closed. Workspace control
	states must be named and, consequently, only affect the workspace control
	with a matching name.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.workspaceControlState(**kwargs)
			super(WorkspaceControlState, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.workspaceControlState(name, exists=True):
				super(WorkspaceControlState, self).__init__(name)
			else:
				name = cmds.workspaceControlState(name, **kwargs)
				super(WorkspaceControlState, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def get_defaultTopLeftCorner(self):
		"""
		
				Top and left edge position that the window will have when "Remember size and position" is off and when the panel is first opened.
				The values will be DPI scaled on edit and the value in query is returned unscaled.
				This value will only be used if the default width and height are also valid.
				
		"""
		return self.query(defaultTopLeftCorner=True)
	#----------------------------------------------------------------------
	def set_defaultTopLeftCorner(self, value):
		"""
		
				Top and left edge position that the window will have when "Remember size and position" is off and when the panel is first opened.
				The values will be DPI scaled on edit and the value in query is returned unscaled.
				This value will only be used if the default width and height are also valid.
				
		"""
		self.edit(defaultTopLeftCorner=value)
	#----------------------------------------------------------------------
	defaultTopLeftCorner = property(get_defaultTopLeftCorner, set_defaultTopLeftCorner)
	#----------------------------------------------------------------------
	def get_defaultWidthHeight(self):
		"""
		
				Width and height that the window will have when "Remember size and position" is off and when the panel is first opened.
				The values will be DPI scaled on edit and the value in query is returned unscaled.
				The position used in that case is defaultTopLeftCorner.
				
		"""
		return self.query(defaultWidthHeight=True)
	#----------------------------------------------------------------------
	def set_defaultWidthHeight(self, value):
		"""
		
				Width and height that the window will have when "Remember size and position" is off and when the panel is first opened.
				The values will be DPI scaled on edit and the value in query is returned unscaled.
				The position used in that case is defaultTopLeftCorner.
				
		"""
		self.edit(defaultWidthHeight=value)
	#----------------------------------------------------------------------
	defaultWidthHeight = property(get_defaultWidthHeight, set_defaultWidthHeight)
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