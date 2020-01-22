import nuke
from ..Abstract_Nodes import Knob

################################################################################
class String_Knob(Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "String_Knob"
	#----------------------------------------------------------------------
	def splitView(self,*args):
		"""
			self.splitView(view) -> None.
			
			Split the view away from the current knob value. 
			
			@param view: Optional view. Default is current view.
			
			@return: None.
		"""
		return self.nuke_object.splitView(*args)
	#----------------------------------------------------------------------
	def setValue(self,val,**kwargs):
		"""
			self.setValue(val, view='default') -> None
			
			Set value of knob.
			
			@param val: The new value.
			
			@param view: Optional parameter specifying which view to set the value for. If omitted, the value will be set for the default view.
			
			@return: None
		"""
		return self.nuke_object.setValue(val,**kwargs)
	#----------------------------------------------------------------------
	def setText(self,val,**kwargs):
		"""
			self.setValue(val, view='default') -> None
			
			Set value of knob.
			
			@param val: The new value.
			
			@param view: Optional parameter specifying which view to set the value for. If omitted, the value will be set for the default view.
			
			@return: None
		"""
		return self.nuke_object.setText(val,**kwargs)
	#----------------------------------------------------------------------
	def getText(self,**kwargs):
		"""
			self.value(oc) -> str
			
			Get the value of this knob as a string.
			
			@param oc: Optional parameter specifying the output context.
			
			@return: String value.
		"""
		return self.nuke_object.getText(**kwargs)
	#----------------------------------------------------------------------
	def getValue(self,**kwargs):
		"""
			self.value(oc) -> str
			
			Get the value of this knob as a string.
			
			@param oc: Optional parameter specifying the output context.
			
			@return: String value.
		"""
		return self.nuke_object.getValue(**kwargs)
	#----------------------------------------------------------------------
	def value(self,**kwargs):
		"""
			self.value(oc) -> str 
			
			Get the value of this knob as a string.
			
			@param oc: Optional parameter specifying the output context
			.
			@return: String value.
		"""
		return self.nuke_object.value(**kwargs)
	#----------------------------------------------------------------------
	def unsplitView(self,**kwargs):
		"""
			self.unsplitView(view) -> None.
			
			Unsplit the view so that it shares a value with other views.
			
			@param view: Optional view. Default is current view. 
			
			@return: None.
		"""
		return self.nuke_object.unsplitView(**kwargs)