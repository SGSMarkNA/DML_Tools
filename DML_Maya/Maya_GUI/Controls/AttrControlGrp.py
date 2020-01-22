

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class AttrControlGrp(UI_Object.UI):
	"""
	This command creates a control of the type most appropriate for the specified
	attribute, and associates the control with the attribute. Any change to the
	control will cause a change in the attribute value, and any change to the
	attribute value will be reflected in the control. Not all attribute types are
	supported.
		  
	      attribute, control
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.attrControlGrp(**kwargs)
			super(AttrControlGrp, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.attrControlGrp(name, exists=True):
				super(AttrControlGrp, self).__init__(name)
			else:
				name = cmds.attrControlGrp(name, **kwargs)
				super(AttrControlGrp, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def get_annotation(self):
		"""
		
				Sets or queries the annotation value of the control group.
				
		"""
		return self.query(annotation=True)
	#----------------------------------------------------------------------
	def set_annotation(self, value):
		"""
		
				Sets or queries the annotation value of the control group.
				
		"""
		self.edit(annotation=value)
	#----------------------------------------------------------------------
	annotation = property(get_annotation, set_annotation)
	#----------------------------------------------------------------------
	def get_attribute(self):
		"""
		
				Sets or queries the attribute the control represents. The name of the attribute
				must be fully specified, including the name of the node. Some types of
				attributes are not supported, but most commonly used attribute types are.
				
		"""
		return self.query(attribute=True)
	#----------------------------------------------------------------------
	def set_attribute(self, value):
		"""
		
				Sets or queries the attribute the control represents. The name of the attribute
				must be fully specified, including the name of the node. Some types of
				attributes are not supported, but most commonly used attribute types are.
				
		"""
		self.edit(attribute=value)
	#----------------------------------------------------------------------
	attribute = property(get_attribute, set_attribute)
	#----------------------------------------------------------------------
	def get_changeCommand(self):
		"""
		
				Sets or queries the change command of the control group. The change
				command will be executed when the control is used to change the value
				of the attribute.
				
		"""
		return self.query(changeCommand=True)
	#----------------------------------------------------------------------
	def set_changeCommand(self, value):
		"""
		
				Sets or queries the change command of the control group. The change
				command will be executed when the control is used to change the value
				of the attribute.
				
		"""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	changeCommand = property(get_changeCommand, set_changeCommand)
	#----------------------------------------------------------------------
	def get_enable(self):
		"""
		
				Sets or queries the enable state of the control group. The control is dimmed if
				the enable state is set to false.
				
		"""
		return self.query(enable=True)
	#----------------------------------------------------------------------
	def set_enable(self, value):
		"""
		
				Sets or queries the enable state of the control group. The control is dimmed if
				the enable state is set to false.
				
		"""
		self.edit(enable=value)
	#----------------------------------------------------------------------
	enable = property(get_enable, set_enable)
	#----------------------------------------------------------------------
	def get_exists(self):
		"""
		
				Returns whether the
				specified object exists or not. Other flags are ignored.
				
		"""
		return self.query(exists=True)
	#----------------------------------------------------------------------
	def set_exists(self, value):
		"""
		
				Returns whether the
				specified object exists or not. Other flags are ignored.
				
		"""
		self.edit(exists=value)
	#----------------------------------------------------------------------
	exists = property(get_exists, set_exists)
	#----------------------------------------------------------------------
	def get_handlesAttribute(self):
		"""
		
				Returns true or false as to whether this command can create a control for the
				specified attribute.
							In query mode, this flag needs a value.
				
		"""
		return self.query(handlesAttribute=True)
	#----------------------------------------------------------------------
	def set_handlesAttribute(self, value):
		"""
		
				Returns true or false as to whether this command can create a control for the
				specified attribute.
							In query mode, this flag needs a value.
				
		"""
		self.edit(handlesAttribute=value)
	#----------------------------------------------------------------------
	handlesAttribute = property(get_handlesAttribute, set_handlesAttribute)
	#----------------------------------------------------------------------
	def get_hideMapButton(self):
		"""
		
				Force the map button to remain hidden for this control.
				
		"""
		return self.query(hideMapButton=True)
	#----------------------------------------------------------------------
	def set_hideMapButton(self, value):
		"""
		
				Force the map button to remain hidden for this control.
				
		"""
		self.edit(hideMapButton=value)
	#----------------------------------------------------------------------
	hideMapButton = property(get_hideMapButton, set_hideMapButton)
	#----------------------------------------------------------------------
	def get_label(self):
		"""
		
				Sets or queries the label of the control group.
				
		"""
		return self.query(label=True)
	#----------------------------------------------------------------------
	def set_label(self, value):
		"""
		
				Sets or queries the label of the control group.
				
		"""
		self.edit(label=value)
	#----------------------------------------------------------------------
	label = property(get_label, set_label)
	#----------------------------------------------------------------------
	def get_preventOverride(self):
		"""
		
				Sets or queries the prevent adjustment state of the control group. If true,
				the RMB menu for the control will not allow adjustments to be made.
				
		"""
		return self.query(preventOverride=True)
	#----------------------------------------------------------------------
	def set_preventOverride(self, value):
		"""
		
				Sets or queries the prevent adjustment state of the control group. If true,
				the RMB menu for the control will not allow adjustments to be made.
				
		"""
		self.edit(preventOverride=value)
	#----------------------------------------------------------------------
	preventOverride = property(get_preventOverride, set_preventOverride)