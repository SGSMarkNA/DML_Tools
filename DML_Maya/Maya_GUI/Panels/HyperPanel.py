

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class HyperPanel(UI_Object.UI):
	"""
	This command creates, edit and queries hypergraph panels which contain only
	a hypergraph editor.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.hyperPanel(**kwargs)
			super(HyperPanel, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.hyperPanel(name, exists=True):
				super(HyperPanel, self).__init__(name)
			else:
				name = cmds.hyperPanel(name, **kwargs)
				super(HyperPanel, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def control(self):
		"""
		
				Returns the top level control for this panel.
				Usually used for getting a parent to attach popup menus.
				CAUTION: panels may not have controls at times.  This
				flag can return "" if no control is present.
				
		"""
		return self.query(control=True)
	#----------------------------------------------------------------------
	def copy(self,value):
		"""
		
				Makes this panel a copy of the specified panel.  Both
				panels must be of the same type.
				
		"""
		self.edit(copy=value)
	#----------------------------------------------------------------------
	def createString(self,value):
		"""
		
				Command string used to create a panel
				
		"""
		self.edit(createString=value)
	#----------------------------------------------------------------------
	def get_docTag(self):
		"""
		
				Attaches a tag to the Maya panel.
				
		"""
		return self.query(docTag=True)
	#----------------------------------------------------------------------
	def set_docTag(self, value):
		"""
		
				Attaches a tag to the Maya panel.
				
		"""
		self.edit(docTag=value)
	#----------------------------------------------------------------------
	docTag = property(get_docTag, set_docTag)
	#----------------------------------------------------------------------
	def editString(self,value):
		"""
		
				Command string used to edit a panel
				
		"""
		self.edit(editString=value)
	#----------------------------------------------------------------------
	@property
	def hyperEditor(self):
		"""
		
				This flag returns the name of the hypergraph editor
				contained by the panel.
				
		"""
		return self.query(hyperEditor=True)
	#----------------------------------------------------------------------
	def init(self,value):
		"""
		
				Initializes the panel's default state.  This is usually done
				automatically on file -new and file -open.
				
		"""
		self.edit(init=value)
	#----------------------------------------------------------------------
	@property
	def isUnique(self):
		"""
		
				Returns true if only one instance of this panel type is allowed.
				
		"""
		return self.query(isUnique=True)
	#----------------------------------------------------------------------
	def get_label(self):
		"""
		
				Specifies the user readable label for the panel.
				
		"""
		return self.query(label=True)
	#----------------------------------------------------------------------
	def set_label(self, value):
		"""
		
				Specifies the user readable label for the panel.
				
		"""
		self.edit(label=value)
	#----------------------------------------------------------------------
	label = property(get_label, set_label)
	#----------------------------------------------------------------------
	def get_menuBarRepeatLast(self):
		"""
		
				Controls whether clicking on the menu header with the middle mouse button would repeat the last selected menu item.
				
		"""
		return self.query(menuBarRepeatLast=True)
	#----------------------------------------------------------------------
	def set_menuBarRepeatLast(self, value):
		"""
		
				Controls whether clicking on the menu header with the middle mouse button would repeat the last selected menu item.
				
		"""
		self.edit(menuBarRepeatLast=value)
	#----------------------------------------------------------------------
	menuBarRepeatLast = property(get_menuBarRepeatLast, set_menuBarRepeatLast)
	#----------------------------------------------------------------------
	def get_menuBarVisible(self):
		"""
		
				Controls whether the menu bar for the panel is displayed.
				
		"""
		return self.query(menuBarVisible=True)
	#----------------------------------------------------------------------
	def set_menuBarVisible(self, value):
		"""
		
				Controls whether the menu bar for the panel is displayed.
				
		"""
		self.edit(menuBarVisible=value)
	#----------------------------------------------------------------------
	menuBarVisible = property(get_menuBarVisible, set_menuBarVisible)
	#----------------------------------------------------------------------
	def get_needsInit(self):
		"""
		
				(Internal) On Edit will mark the panel as requiring initialization.
				Query will return whether the panel is marked for initialization.  Used
				during file -new and file -open.
				
		"""
		return self.query(needsInit=True)
	#----------------------------------------------------------------------
	def set_needsInit(self, value):
		"""
		
				(Internal) On Edit will mark the panel as requiring initialization.
				Query will return whether the panel is marked for initialization.  Used
				during file -new and file -open.
				
		"""
		self.edit(needsInit=value)
	#----------------------------------------------------------------------
	needsInit = property(get_needsInit, set_needsInit)
	#----------------------------------------------------------------------
	def get_popupMenuProcedure(self):
		"""
		
				Specifies the procedure called for building the panel's popup menu(s).
				The default value is "buildPanelPopupMenu".  The procedure should take
				one string argument which is the panel's name.
				
		"""
		return self.query(popupMenuProcedure=True)
	#----------------------------------------------------------------------
	def set_popupMenuProcedure(self, value):
		"""
		
				Specifies the procedure called for building the panel's popup menu(s).
				The default value is "buildPanelPopupMenu".  The procedure should take
				one string argument which is the panel's name.
				
		"""
		self.edit(popupMenuProcedure=value)
	#----------------------------------------------------------------------
	popupMenuProcedure = property(get_popupMenuProcedure, set_popupMenuProcedure)
	#----------------------------------------------------------------------
	def replacePanel(self,value):
		"""
		
				Will replace the specified panel with this panel.  If the
				target panel is within the same layout it will perform a swap.
				
		"""
		self.edit(replacePanel=value)
	#----------------------------------------------------------------------
	def get_tearOff(self):
		"""
		
				Will tear off this panel into a separate window with a paneLayout
				as the parent of the panel. When queried this flag will return if the
				panel has been torn off into its own window.
				
		"""
		return self.query(tearOff=True)
	#----------------------------------------------------------------------
	def set_tearOff(self, value):
		"""
		
				Will tear off this panel into a separate window with a paneLayout
				as the parent of the panel. When queried this flag will return if the
				panel has been torn off into its own window.
				
		"""
		self.edit(tearOff=value)
	#----------------------------------------------------------------------
	tearOff = property(get_tearOff, set_tearOff)
	#----------------------------------------------------------------------
	def tearOffRestore(self,value):
		"""
		
				Restores panel if it is torn off and focus is given to it.
				If docked, becomes the active panel in the docked window.
				This should be the default flag that is added to all panels
				instead of -to/-tearOff flag which should only be used to tear off the panel.
				
		"""
		self.edit(tearOffRestore=value)
	#----------------------------------------------------------------------
	def unParent(self,value):
		"""
		
				Specifies that the panel should be removed from its layout.
				This (obviously) cannot be used with query.
				
		"""
		self.edit(unParent=value)