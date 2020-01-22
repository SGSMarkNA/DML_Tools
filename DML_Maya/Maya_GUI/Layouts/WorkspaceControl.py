

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class WorkspaceControl(UI_Object.UI):
	"""
	Creates and manages the widget used to host windows in a layout that enables docking and stacking windows together.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.workspaceControl(**kwargs)
			super(WorkspaceControl, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.workspaceControl(name, exists=True):
				super(WorkspaceControl, self).__init__(name)
			else:
				name = cmds.workspaceControl(name, **kwargs)
				super(WorkspaceControl, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def checksPlugins(self,value):
		"""
		
				Sets whether the UI (as defined by the uiScript) checks the loaded state of one or more plug-ins in its code.
				The UI will not be loaded until the auto-loading of plug-ins is complete. Default value is false.
				
		"""
		self.edit(checksPlugins=value)
	#----------------------------------------------------------------------
	def close(self,value):
		"""
		
				Closes the workspace control.
				
		"""
		self.edit(close=value)
	#----------------------------------------------------------------------
	def closeCommand(self,value):
		"""
		
				Command that gets executed when the workspace control is closed.
				
		"""
		self.edit(closeCommand=value)
	#----------------------------------------------------------------------
	def get_collapse(self):
		"""
		
				Collapse or expand the tab widget parent of the workspace control.
				
		"""
		return self.query(collapse=True)
	#----------------------------------------------------------------------
	def set_collapse(self, value):
		"""
		
				Collapse or expand the tab widget parent of the workspace control.
				
		"""
		self.edit(collapse=value)
	#----------------------------------------------------------------------
	collapse = property(get_collapse, set_collapse)
	#----------------------------------------------------------------------
	def dockToControl(self,value):
		"""
		
				Dock this workspace control next to the given control. The first argument is the control name,
				the second is dock position relative to the control (valid values are: "left", "right", "top", "bottom").
				
		"""
		self.edit(dockToControl=value)
	#----------------------------------------------------------------------
	def dockToMainWindow(self,value):
		"""
		
				Dock this workspace control into the main window. The first argument is the dock position along the sides of
				the main window (valid values are: "left", "right", "top", "bottom"), the second specifies whether the
				control should be tabbed into the first control found at the dock position.
				
		"""
		self.edit(dockToMainWindow=value)
	#----------------------------------------------------------------------
	def dockToPanel(self,value):
		"""
		
				Dock this workspace control into the workspace docking panel that the given workspace control is in. The first argument
				is the control name, the second is dock position along the sides of the panel (valid values are: "left", "right", "top",
				"bottom"), the third specifies whether the control should be tabbed into the first control found at the dock position.
				
		"""
		self.edit(dockToPanel=value)
	#----------------------------------------------------------------------
	def get_duplicatable(self):
		"""
		
				Controls whether or not this workspace control can be duplicated.
				
				The default duplicate state is controlled by whether or not the panel is unique. Unique panels cannot be
				duplicated or copied. Workspace controls without a panel also cannot be duplicated, unless specifically
				set as such using this flag.
				
		"""
		return self.query(duplicatable=True)
	#----------------------------------------------------------------------
	def set_duplicatable(self, value):
		"""
		
				Controls whether or not this workspace control can be duplicated.
				
				The default duplicate state is controlled by whether or not the panel is unique. Unique panels cannot be
				duplicated or copied. Workspace controls without a panel also cannot be duplicated, unless specifically
				set as such using this flag.
				
		"""
		self.edit(duplicatable=value)
	#----------------------------------------------------------------------
	duplicatable = property(get_duplicatable, set_duplicatable)
	#----------------------------------------------------------------------
	def get_floating(self):
		"""
		
				Whether the workspace control is floating.
				
		"""
		return self.query(floating=True)
	#----------------------------------------------------------------------
	def set_floating(self, value):
		"""
		
				Whether the workspace control is floating.
				
		"""
		self.edit(floating=value)
	#----------------------------------------------------------------------
	floating = property(get_floating, set_floating)
	#----------------------------------------------------------------------
	@property
	def height(self):
		"""
		
				Query only flag returning the current height of the control.
				
		"""
		return self.query(height=True)
	#----------------------------------------------------------------------
	def get_heightProperty(self):
		"""
		
				Set height property of the workspace control.
				Valid values are:
				
				fixed	  - Cannot be resized manually and will not be given any extra space while maximizing/dynamically resizing
				preferred - Can be resized manually but will not be given any extra space while maximizing/dynamically resizing
				free	  - Can be resized manually and will be given extra space while maximizing/dynamically resizing
				
				Default: free 
				In query mode returns the current height property of the workspace control.
				
		"""
		return self.query(heightProperty=True)
	#----------------------------------------------------------------------
	def set_heightProperty(self, value):
		"""
		
				Set height property of the workspace control.
				Valid values are:
				
				fixed	  - Cannot be resized manually and will not be given any extra space while maximizing/dynamically resizing
				preferred - Can be resized manually but will not be given any extra space while maximizing/dynamically resizing
				free	  - Can be resized manually and will be given extra space while maximizing/dynamically resizing
				
				Default: free 
				In query mode returns the current height property of the workspace control.
				
		"""
		self.edit(heightProperty=value)
	#----------------------------------------------------------------------
	heightProperty = property(get_heightProperty, set_heightProperty)
	#----------------------------------------------------------------------
	def get_horizontal(self):
		"""
		
				Orientation of the control. This flag is true by default, which corresponds to a horizontally oriented widget.
				
				Note: currently only "Toolbox" and "Shelf" support a vertical orientation.
				
		"""
		return self.query(horizontal=True)
	#----------------------------------------------------------------------
	def set_horizontal(self, value):
		"""
		
				Orientation of the control. This flag is true by default, which corresponds to a horizontally oriented widget.
				
				Note: currently only "Toolbox" and "Shelf" support a vertical orientation.
				
		"""
		self.edit(horizontal=value)
	#----------------------------------------------------------------------
	horizontal = property(get_horizontal, set_horizontal)
	#----------------------------------------------------------------------
	def get_initCallback(self):
		"""
		
				Adds a mel command to be executed when the control is added to the layout.
				The command should be a mel proc and it will be called with the workspaceControl name as parameter.
				The mel command should take the form:
				
				global proc callbackName(string $workspaceControlName)
				
				If "save" is appended to the command name, it will be called during the layout save.
				
				global proc callbackNameSave(string $workspaceControlName)
				
		"""
		return self.query(initCallback=True)
	#----------------------------------------------------------------------
	def set_initCallback(self, value):
		"""
		
				Adds a mel command to be executed when the control is added to the layout.
				The command should be a mel proc and it will be called with the workspaceControl name as parameter.
				The mel command should take the form:
				
				global proc callbackName(string $workspaceControlName)
				
				If "save" is appended to the command name, it will be called during the layout save.
				
				global proc callbackNameSave(string $workspaceControlName)
				
		"""
		self.edit(initCallback=value)
	#----------------------------------------------------------------------
	initCallback = property(get_initCallback, set_initCallback)
	#----------------------------------------------------------------------
	def initialHeight(self,value):
		"""
		
				The initial height of the workspace control when first shown.
				
		"""
		self.edit(initialHeight=value)
	#----------------------------------------------------------------------
	def initialWidth(self,value):
		"""
		
				The initial width of the workspace control when first shown.
				
		"""
		self.edit(initialWidth=value)
	#----------------------------------------------------------------------
	def get_label(self):
		"""
		
				The label text. The default label is the name of the workspace control.
				
		"""
		return self.query(label=True)
	#----------------------------------------------------------------------
	def set_label(self, value):
		"""
		
				The label text. The default label is the name of the workspace control.
				
		"""
		self.edit(label=value)
	#----------------------------------------------------------------------
	label = property(get_label, set_label)
	#----------------------------------------------------------------------
	def loadImmediately(self,value):
		"""
		
				Sets whether the UI (as defined by the uiScript) will be built immediately on workspace control
				creation (true) or delayed until the control is actually shown (false). Default value is false.
				
		"""
		self.edit(loadImmediately=value)
	#----------------------------------------------------------------------
	def get_minimumHeight(self):
		"""
		
				Sets the minimum height of control to the given value.
				
				If given value is 0 (False), minimum height is set to 0.
				If given value is 1 (True), minimum height is set to initial height.
				If given value is greater than 1, minimum height is set to the given value.
				
				In query mode returns current minimum height of the control.
				
		"""
		return self.query(minimumHeight=True)
	#----------------------------------------------------------------------
	def set_minimumHeight(self, value):
		"""
		
				Sets the minimum height of control to the given value.
				
				If given value is 0 (False), minimum height is set to 0.
				If given value is 1 (True), minimum height is set to initial height.
				If given value is greater than 1, minimum height is set to the given value.
				
				In query mode returns current minimum height of the control.
				
		"""
		self.edit(minimumHeight=value)
	#----------------------------------------------------------------------
	minimumHeight = property(get_minimumHeight, set_minimumHeight)
	#----------------------------------------------------------------------
	def get_minimumWidth(self):
		"""
		
				Sets the minimum width of control to the given value.
				This flag parameter was changed from bool to int in 2018 and old settings are still respected according to the following.
				
				If given value is 0 (False), minimum width is set to 0.
				If given value is 1 (True), minimum width is set to initial width.
				If given value is greater than 1, minimum width is set to the given value.
				
				In query mode returns current minimum width of the control.
				
		"""
		return self.query(minimumWidth=True)
	#----------------------------------------------------------------------
	def set_minimumWidth(self, value):
		"""
		
				Sets the minimum width of control to the given value.
				This flag parameter was changed from bool to int in 2018 and old settings are still respected according to the following.
				
				If given value is 0 (False), minimum width is set to 0.
				If given value is 1 (True), minimum width is set to initial width.
				If given value is greater than 1, minimum width is set to the given value.
				
				In query mode returns current minimum width of the control.
				
		"""
		self.edit(minimumWidth=value)
	#----------------------------------------------------------------------
	minimumWidth = property(get_minimumWidth, set_minimumWidth)
	#----------------------------------------------------------------------
	def get_r(self):
		"""
		
				Raises a workspace control to the top and makes it active.
				In Query mode, this flag will return whether the workspace control is active or not.
				Note that this flag won't raise a control if is minimized or collapsed. Use the flag -rs/restore instead.
				
		"""
		return self.query(r=True)
	#----------------------------------------------------------------------
	def set_r(self, value):
		"""
		
				Raises a workspace control to the top and makes it active.
				In Query mode, this flag will return whether the workspace control is active or not.
				Note that this flag won't raise a control if is minimized or collapsed. Use the flag -rs/restore instead.
				
		"""
		self.edit(r=value)
	#----------------------------------------------------------------------
	r = property(get_r, set_r)
	#----------------------------------------------------------------------
	def requiredControl(self,value):
		"""
		
				The name of a workspace control that needs to be open in order for this workspace control to properly function.
				This workspace control will not be created if the required control is not open, and will be closed when the
				required control is closed.
				
		"""
		self.edit(requiredControl=value)
	#----------------------------------------------------------------------
	def requiredPlugin(self,value):
		"""
		
				The name of a plug-in that needs to be loaded in order to build the workspace control UI.
				
		"""
		self.edit(requiredPlugin=value)
	#----------------------------------------------------------------------
	def resizeHeight(self,value):
		"""
		
				Resizes a floating workspace control's height to the given value.
				
		"""
		self.edit(resizeHeight=value)
	#----------------------------------------------------------------------
	def resizeWidth(self,value):
		"""
		
				Resizes a floating workspace control's width to the given value.
				
		"""
		self.edit(resizeWidth=value)
	#----------------------------------------------------------------------
	def restore(self,value):
		"""
		
				Restores the control according to the following rules:
				
				If collapsed then the control will be expanded
				If hidden then the control will be shown
				If minimized then the control will be restored
				If the control is an inactive tab into a tab group then it will become the active tab
				
		"""
		self.edit(restore=value)
	#----------------------------------------------------------------------
	def get_stateString(self):
		"""
		
				String containing the state of the control.
				Can be used with the initCallback flag.
				
		"""
		return self.query(stateString=True)
	#----------------------------------------------------------------------
	def set_stateString(self, value):
		"""
		
				String containing the state of the control.
				Can be used with the initCallback flag.
				
		"""
		self.edit(stateString=value)
	#----------------------------------------------------------------------
	stateString = property(get_stateString, set_stateString)
	#----------------------------------------------------------------------
	def get_tabPosition(self):
		"""
		
				Changes the tab position. The possible values are: "north", "east" and "west".
				The boolean value, if set to true, changes the tab positions of all the controls in the parent widget.
				If it is not set, only the current control will get its position changed.
				A control can have a different orientation than the tab widget.
				If the control tab position is different from the tab widget's one, the tab position will be changed when the control becomes the only control in the tab widget.
				On query, only the control's tab position will be returned, not the tab widget's position. They may differ.
				
		"""
		return self.query(tabPosition=True)
	#----------------------------------------------------------------------
	def set_tabPosition(self, value):
		"""
		
				Changes the tab position. The possible values are: "north", "east" and "west".
				The boolean value, if set to true, changes the tab positions of all the controls in the parent widget.
				If it is not set, only the current control will get its position changed.
				A control can have a different orientation than the tab widget.
				If the control tab position is different from the tab widget's one, the tab position will be changed when the control becomes the only control in the tab widget.
				On query, only the control's tab position will be returned, not the tab widget's position. They may differ.
				
		"""
		self.edit(tabPosition=value)
	#----------------------------------------------------------------------
	tabPosition = property(get_tabPosition, set_tabPosition)
	#----------------------------------------------------------------------
	def tabToControl(self,value):
		"""
		
				Tab this workspace control into the given control. The first argument is the control name,
				the second is the index position within the containing tab widget (invalid values mean append).
				
		"""
		self.edit(tabToControl=value)
	#----------------------------------------------------------------------
	def uiScript(self,value):
		"""
		
				The specified script will be invoked to build the UI of the workspaceControl.  This is a required flag.
				
		"""
		self.edit(uiScript=value)
	#----------------------------------------------------------------------
	def get_visible(self):
		"""
		
				The visible state of the workspace control. A control is created visible by default.
				If the control is created as not visible, the control will be created in a closed state.
				To make it appear, edit the control to set the flags floating or the flag visible to true.
				Use -r/raise flag to get the active status of a control as this flag will return true when the control
				is minimized or collapsed.
				
		"""
		return self.query(visible=True)
	#----------------------------------------------------------------------
	def set_visible(self, value):
		"""
		
				The visible state of the workspace control. A control is created visible by default.
				If the control is created as not visible, the control will be created in a closed state.
				To make it appear, edit the control to set the flags floating or the flag visible to true.
				Use -r/raise flag to get the active status of a control as this flag will return true when the control
				is minimized or collapsed.
				
		"""
		self.edit(visible=value)
	#----------------------------------------------------------------------
	visible = property(get_visible, set_visible)
	#----------------------------------------------------------------------
	def visibleChangeCommand(self,value):
		"""
		
				Command that gets executed when visible state of the workspace control changes.
				
		"""
		self.edit(visibleChangeCommand=value)
	#----------------------------------------------------------------------
	@property
	def width(self):
		"""
		
				Query only flag returning the current width of the control.
				
		"""
		return self.query(width=True)
	#----------------------------------------------------------------------
	def get_widthProperty(self):
		"""
		
				Set width property of the workspace control.
				Valid values are:
				
				fixed	  - Cannot be resized manually and will not be given any extra space while maximizing/dynamically resizing
				preferred - Can be resized manually but will not be given any extra space while maximizing/dynamically resizing
				free	  - Can be resized manually and will be given extra space while maximizing/dynamically resizing
				
				Default: free 
				In query mode returns the current width property of the workspace control.
				
		"""
		return self.query(widthProperty=True)
	#----------------------------------------------------------------------
	def set_widthProperty(self, value):
		"""
		
				Set width property of the workspace control.
				Valid values are:
				
				fixed	  - Cannot be resized manually and will not be given any extra space while maximizing/dynamically resizing
				preferred - Can be resized manually but will not be given any extra space while maximizing/dynamically resizing
				free	  - Can be resized manually and will be given extra space while maximizing/dynamically resizing
				
				Default: free 
				In query mode returns the current width property of the workspace control.
				
		"""
		self.edit(widthProperty=value)
	#----------------------------------------------------------------------
	widthProperty = property(get_widthProperty, set_widthProperty)