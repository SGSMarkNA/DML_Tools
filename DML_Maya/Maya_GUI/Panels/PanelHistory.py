

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class PanelHistory(UI_Object.UI):
	"""
	This command creates a panel history object.  The object is targeted on a
	particular paneLayout and thereafter notes changes in panel configurations
	within that paneLayout, building up a history list.  The list can be stepped
	through backwards or forwards.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.panelHistory(**kwargs)
			super(PanelHistory, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.panelHistory(name, exists=True):
				super(PanelHistory, self).__init__(name)
			else:
				name = cmds.panelHistory(name, **kwargs)
				super(PanelHistory, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def back(self,value):
		"""
		
				Go back one level on the history list.
				
		"""
		self.edit(back=value)
	#----------------------------------------------------------------------
	def clear(self,value):
		"""
		
				Clear the history stack
				
		"""
		self.edit(clear=value)
	#----------------------------------------------------------------------
	def forward(self,value):
		"""
		
				Go forward one level on the history list.
				
		"""
		self.edit(forward=value)
	#----------------------------------------------------------------------
	def get_historyDepth(self):
		"""
		
				Specifies how many levels of history are maintained.
				
		"""
		return self.query(historyDepth=True)
	#----------------------------------------------------------------------
	def set_historyDepth(self, value):
		"""
		
				Specifies how many levels of history are maintained.
				
		"""
		self.edit(historyDepth=value)
	#----------------------------------------------------------------------
	historyDepth = property(get_historyDepth, set_historyDepth)
	#----------------------------------------------------------------------
	@property
	def isEmpty(self):
		"""
		
				Returns true if there is currently no panel history.
				
		"""
		return self.query(isEmpty=True)
	#----------------------------------------------------------------------
	def suspend(self,value):
		"""
		
				Specifies whether to suspend or resume updates to the panel history.
				Useful for chunking a number of changes into one history event.
				
		"""
		self.edit(suspend=value)
	#----------------------------------------------------------------------
	@property
	def targetPane(self):
		"""
		
				Specifies which paneLayout the history will be maintained for.
				
		"""
		return self.query(targetPane=True)
	#----------------------------------------------------------------------
	def get_wrap(self):
		"""
		
				Specifies whether the history will wrap at the end and
				beginning.  This value is true by default.
				
		"""
		return self.query(wrap=True)
	#----------------------------------------------------------------------
	def set_wrap(self, value):
		"""
		
				Specifies whether the history will wrap at the end and
				beginning.  This value is true by default.
				
		"""
		self.edit(wrap=value)
	#----------------------------------------------------------------------
	wrap = property(get_wrap, set_wrap)