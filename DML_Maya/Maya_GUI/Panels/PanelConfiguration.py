

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class PanelConfiguration(UI_Object.UI):
	"""
	This command creates a panel configuration object. Typically you would
	not call this method command directly. Instead use the Panel Editor.
	
	Once a panel configuration is created you can make it appear in the
	main Maya window by selecting it from any panel's "Panels->Saved Layouts"
	menu.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.panelConfiguration(**kwargs)
			super(PanelConfiguration, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.panelConfiguration(name, exists=True):
				super(PanelConfiguration, self).__init__(name)
			else:
				name = cmds.panelConfiguration(name, **kwargs)
				super(PanelConfiguration, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def addPanel(self,value):
		"""
		
				Adds the specified panel to the configuration.  Arguments are:
				isFixed, label string, type string, create string, edit string.
				
		"""
		self.edit(addPanel=value)
	#----------------------------------------------------------------------
	def get_configString(self):
		"""
		
				Specifies the string that arranges the panels.
				
		"""
		return self.query(configString=True)
	#----------------------------------------------------------------------
	def set_configString(self, value):
		"""
		
				Specifies the string that arranges the panels.
				
		"""
		self.edit(configString=value)
	#----------------------------------------------------------------------
	configString = property(get_configString, set_configString)
	#----------------------------------------------------------------------
	@property
	def createStrings(self):
		"""
		
				Returns an string array of the panel creation strings.
				
		"""
		return self.query(createStrings=True)
	#----------------------------------------------------------------------
	@property
	def defaultImage(self):
		"""
		
				The default image for this configuration. Once the default image
				is set it may not be changed. If an image is set with the -i/image
				flag then it's value will take precedence.
				
		"""
		return self.query(defaultImage=True)
	#----------------------------------------------------------------------
	@property
	def editStrings(self):
		"""
		
				Returns an string array of the panel edit strings.
				
		"""
		return self.query(editStrings=True)
	#----------------------------------------------------------------------
	def get_image(self):
		"""
		
				The user specified image for this configuration. Use this flag
				to override the default image.
				
		"""
		return self.query(image=True)
	#----------------------------------------------------------------------
	def set_image(self, value):
		"""
		
				The user specified image for this configuration. Use this flag
				to override the default image.
				
		"""
		self.edit(image=value)
	#----------------------------------------------------------------------
	image = property(get_image, set_image)
	#----------------------------------------------------------------------
	@property
	def isFixedState(self):
		"""
		
				Returns an integer array of whether the panels have fixed states or not.
				
		"""
		return self.query(isFixedState=True)
	#----------------------------------------------------------------------
	def get_label(self):
		"""
		
				Configuration label.
				
		"""
		return self.query(label=True)
	#----------------------------------------------------------------------
	def set_label(self, value):
		"""
		
				Configuration label.
				
		"""
		self.edit(label=value)
	#----------------------------------------------------------------------
	label = property(get_label, set_label)
	#----------------------------------------------------------------------
	@property
	def labelStrings(self):
		"""
		
				Returns an string array of the panel labels.
				
		"""
		return self.query(labelStrings=True)
	#----------------------------------------------------------------------
	@property
	def numberOfPanels(self):
		"""
		
				Returns the number of panels in the configuration.
				
		"""
		return self.query(numberOfPanels=True)
	#----------------------------------------------------------------------
	def removeAllPanels(self,value):
		"""
		
				Removes the last panel in the config.
				
		"""
		self.edit(removeAllPanels=value)
	#----------------------------------------------------------------------
	def removeLastPanel(self,value):
		"""
		
				Removes the last panel in the config.
				
		"""
		self.edit(removeLastPanel=value)
	#----------------------------------------------------------------------
	def replaceCreateString(self,value):
		"""
		
				Replaces the specified create string.  The index is 1 based.
				
		"""
		self.edit(replaceCreateString=value)
	#----------------------------------------------------------------------
	def replaceEditString(self,value):
		"""
		
				Replaces the specified edit string.  The index is 1 based.
				
		"""
		self.edit(replaceEditString=value)
	#----------------------------------------------------------------------
	def replaceFixedState(self,value):
		"""
		
				Replaces the specified fixed state value (true|false).  The index is 1 based.
				
		"""
		self.edit(replaceFixedState=value)
	#----------------------------------------------------------------------
	def replaceLabel(self,value):
		"""
		
				Replaces the specified label.  The index is 1 based.
				
		"""
		self.edit(replaceLabel=value)
	#----------------------------------------------------------------------
	def replacePanel(self,value):
		"""
		
				Replaces the specified panel in the configuration.  Arguments are:
				index, isFixed, label string, type string, create string, edit string.
				The index is 1 based.
				
		"""
		self.edit(replacePanel=value)
	#----------------------------------------------------------------------
	def replaceTypeString(self,value):
		"""
		
				Replaces the specified type string.  The index is 1 based.
				
		"""
		self.edit(replaceTypeString=value)
	#----------------------------------------------------------------------
	def get_sceneConfig(self):
		"""
		
				Specifies whether the configuration is associated with the scene.
				Scene configurations are created when the scene is opened and deleted when
				the scene is closed.
				
		"""
		return self.query(sceneConfig=True)
	#----------------------------------------------------------------------
	def set_sceneConfig(self, value):
		"""
		
				Specifies whether the configuration is associated with the scene.
				Scene configurations are created when the scene is opened and deleted when
				the scene is closed.
				
		"""
		self.edit(sceneConfig=value)
	#----------------------------------------------------------------------
	sceneConfig = property(get_sceneConfig, set_sceneConfig)
	#----------------------------------------------------------------------
	@property
	def typeStrings(self):
		"""
		
				Returns an string array of the panel types.
				
		"""
		return self.query(typeStrings=True)
	#----------------------------------------------------------------------
	def get_userCreated(self):
		"""
		
				Returns true if the configuration was created by the user. If it is user created, the configuration will show up in the RMB menu in the toolbox's saved layouts.
				
		"""
		return self.query(userCreated=True)
	#----------------------------------------------------------------------
	def set_userCreated(self, value):
		"""
		
				Returns true if the configuration was created by the user. If it is user created, the configuration will show up in the RMB menu in the toolbox's saved layouts.
				
		"""
		self.edit(userCreated=value)
	#----------------------------------------------------------------------
	userCreated = property(get_userCreated, set_userCreated)