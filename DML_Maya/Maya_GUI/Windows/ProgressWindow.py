

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class ProgressWindow(UI_Object.UI):
	"""
	The progressWindow command creates a window
	containing a status message, a graphical progress gauge,
	and optionally a "Hit ESC to Cancel" label for interruptable operations.
	Only one progress window is allowed on screen at a time. While the window
	is visible, the busy cursor is shown.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.progressWindow(**kwargs)
			super(ProgressWindow, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.progressWindow(name, exists=True):
				super(ProgressWindow, self).__init__(name)
			else:
				name = cmds.progressWindow(name, **kwargs)
				super(ProgressWindow, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def isCancelled(self):
		"""
		
				Returns true if the user has tried to cancel the operation.
				Returns false otherwise.
				
		"""
		return self.query(isCancelled=True)
	#----------------------------------------------------------------------
	def get_isInterruptable(self):
		"""
		
				Returns true if the progress window should respond to attempts
				to cancel the operation. The cancel button is disabled if this is set
				to true.
				
		"""
		return self.query(isInterruptable=True)
	#----------------------------------------------------------------------
	def set_isInterruptable(self, value):
		"""
		
				Returns true if the progress window should respond to attempts
				to cancel the operation. The cancel button is disabled if this is set
				to true.
				
		"""
		self.edit(isInterruptable=value)
	#----------------------------------------------------------------------
	isInterruptable = property(get_isInterruptable, set_isInterruptable)
	#----------------------------------------------------------------------
	def get_maxValue(self):
		"""
		
				The maximum or "ending" value of the progress indicator.
				If the progress value is greater than the -max/maxValue, the
				progress value will be set to the maximum.
				Default value is 100.
				
		"""
		return self.query(maxValue=True)
	#----------------------------------------------------------------------
	def set_maxValue(self, value):
		"""
		
				The maximum or "ending" value of the progress indicator.
				If the progress value is greater than the -max/maxValue, the
				progress value will be set to the maximum.
				Default value is 100.
				
		"""
		self.edit(maxValue=value)
	#----------------------------------------------------------------------
	maxValue = property(get_maxValue, set_maxValue)
	#----------------------------------------------------------------------
	def get_minValue(self):
		"""
		
				The minimum or "starting" value of the progress indicator.
				If the progress value is less than the -min/minValue, the
				progress value will be set to the minimum.
				Default value is 0.
				
		"""
		return self.query(minValue=True)
	#----------------------------------------------------------------------
	def set_minValue(self, value):
		"""
		
				The minimum or "starting" value of the progress indicator.
				If the progress value is less than the -min/minValue, the
				progress value will be set to the minimum.
				Default value is 0.
				
		"""
		self.edit(minValue=value)
	#----------------------------------------------------------------------
	minValue = property(get_minValue, set_minValue)
	#----------------------------------------------------------------------
	def get_progress(self):
		"""
		
				The amount of progress currently shown on the control.
				The value will always be between min and max.
				Default is equal to the minimum when the control is created.
				
		"""
		return self.query(progress=True)
	#----------------------------------------------------------------------
	def set_progress(self, value):
		"""
		
				The amount of progress currently shown on the control.
				The value will always be between min and max.
				Default is equal to the minimum when the control is created.
				
		"""
		self.edit(progress=value)
	#----------------------------------------------------------------------
	progress = property(get_progress, set_progress)
	#----------------------------------------------------------------------
	def get_status(self):
		"""
		
				The status text appearing above the progress gauge.
				
		"""
		return self.query(status=True)
	#----------------------------------------------------------------------
	def set_status(self, value):
		"""
		
				The status text appearing above the progress gauge.
				
		"""
		self.edit(status=value)
	#----------------------------------------------------------------------
	status = property(get_status, set_status)
	#----------------------------------------------------------------------
	def step(self,value):
		"""
		
				Increments the -pr/progress value by the amount specified.
				
		"""
		self.edit(step=value)
	#----------------------------------------------------------------------
	def get_title(self):
		"""
		
				The window title.
				
		"""
		return self.query(title=True)
	#----------------------------------------------------------------------
	def set_title(self, value):
		"""
		
				The window title.
				
		"""
		self.edit(title=value)
	#----------------------------------------------------------------------
	title = property(get_title, set_title)