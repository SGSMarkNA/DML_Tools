

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class MayaDpiSetting(UI_Object.UI):
	"""
	Provide Maya interface scaling based on system DPI or custom scale setting or no scaling. Please note that the change will only take effect after relaunching Maya.
		  
	      mayaDpiSetting, dpi
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.mayaDpiSetting(**kwargs)
			super(MayaDpiSetting, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.mayaDpiSetting(name, exists=True):
				super(MayaDpiSetting, self).__init__(name)
			else:
				name = cmds.mayaDpiSetting(name, **kwargs)
				super(MayaDpiSetting, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def mode(self):
		"""
		
				Specifies the interface scaling mode:
				
				0 - System Dpi Based Scaling
				1 - Custom Scaling (Must provide the custom scale value with flag "-scaleValue")
				2 - No Scaling
				
		"""
		return self.query(mode=True)
	#----------------------------------------------------------------------
	@property
	def realScaleValue(self):
		"""
		
				This is a query mode only flag which returns the real scale value depending on current scaling mode and defined scale value:
				
				mode 0 - Return the current real scale value which is the ratio of current system dpi to default system dpi
				mode 1 - Return the current real scale value which is the product of the defined scale value and the ratio of current system dpi to default system dpi
				mode 2 - Always return 1.0 which indicates real scale is 100% when the scaling mode is no scaling.
				
		"""
		return self.query(realScaleValue=True)
	#----------------------------------------------------------------------
	@property
	def scaleValue(self):
		"""
		
				Specifies the custom scale of the interface if scaling mode is 1. The allowed values are [1.0, 1.25, 1.5, 2.0].
				In query mode, return the scale value depend on current scaling mode:
				
				mode 0 - Always return 1.0 which indicates 100% scaling
				mode 1 - Return the custom scale value used
				mode 2 - Always return 1.0 which indicates no custom scaling
				
		"""
		return self.query(scaleValue=True)
	#----------------------------------------------------------------------
	@property
	def systemDpi(self):
		"""
		
				This is a query mode only flag which returns the current system dpi value.
				
		"""
		return self.query(systemDpi=True)