

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class Window(UI_Object.UI):
	"""
	This command creates a new window but leaves it invisible. It is most
	efficient to add the window's elements and then make it visible with
	the showWindow command. The window can have an optional menu bar. Also,
	the title bar and minimize/maximize buttons can be turned on or off. If the
	title bar is off, then you cannot have minimize or maximize buttons.
	
	Note: The window will require a control layout of some kind
	to arrange the controls (buttons, sliders, fields, etc.).  Examples of
	control layouts are columnLayout, formLayout, rowLayout, etc.
	
	Note: This command will clear the uiTemplate stack.  Templates for
	a window need to be set after the window cmd.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.window(**kwargs)
			super(Window, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.window(name, exists=True):
				super(Window, self).__init__(name)
			else:
				name = cmds.window(name, **kwargs)
				super(Window, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def backgroundColor(self,value):
		"""
		
				The background color of the window. The arguments correspond
				to the red, green, and blue color components. Each component ranges
				in value from 0.0 to 1.0.
				
		"""
		self.edit(backgroundColor=value)
	#----------------------------------------------------------------------
	def closeCommand(self,value):
		"""
		
				Script executed after the window is closed.
				
		"""
		self.edit(closeCommand=value)
	#----------------------------------------------------------------------
	def get_docTag(self):
		"""
		
				Attach a tag to the window.
				
		"""
		return self.query(docTag=True)
	#----------------------------------------------------------------------
	def set_docTag(self, value):
		"""
		
				Attach a tag to the window.
				
		"""
		self.edit(docTag=value)
	#----------------------------------------------------------------------
	docTag = property(get_docTag, set_docTag)
	#----------------------------------------------------------------------
	def get_dockingLayout(self):
		"""
		
				When queried this flag will return a string holding the docking layout information.
				This string can be set when creating or editing a docking station to restore the previous docking layout.
				This string is a hexadecimal representation of a binary string and is not meant to be humanly readable,
				but can be saved and loaded using the optionVar command to restore layouts across sessions of Maya.
				
		"""
		return self.query(dockingLayout=True)
	#----------------------------------------------------------------------
	def set_dockingLayout(self, value):
		"""
		
				When queried this flag will return a string holding the docking layout information.
				This string can be set when creating or editing a docking station to restore the previous docking layout.
				This string is a hexadecimal representation of a binary string and is not meant to be humanly readable,
				but can be saved and loaded using the optionVar command to restore layouts across sessions of Maya.
				
		"""
		self.edit(dockingLayout=value)
	#----------------------------------------------------------------------
	dockingLayout = property(get_dockingLayout, set_dockingLayout)
	#----------------------------------------------------------------------
	@property
	def frontWindow(self):
		"""
		
				Return the name of the front window.  Note: you must supply
				the name of any window (the window does not need to exist).
				Returns "unknown" if the front window cannot be determined.
				
		"""
		return self.query(frontWindow=True)
	#----------------------------------------------------------------------
	def get_height(self):
		"""
		
				Height of the window excluding any window frame in pixels.
				
		"""
		return self.query(height=True)
	#----------------------------------------------------------------------
	def set_height(self, value):
		"""
		
				Height of the window excluding any window frame in pixels.
				
		"""
		self.edit(height=value)
	#----------------------------------------------------------------------
	height = property(get_height, set_height)
	#----------------------------------------------------------------------
	def get_iconName(self):
		"""
		
				The window's icon title.  By default it is the same as the
				window's title.
				
		"""
		return self.query(iconName=True)
	#----------------------------------------------------------------------
	def set_iconName(self, value):
		"""
		
				The window's icon title.  By default it is the same as the
				window's title.
				
		"""
		self.edit(iconName=value)
	#----------------------------------------------------------------------
	iconName = property(get_iconName, set_iconName)
	#----------------------------------------------------------------------
	def get_iconify(self):
		"""
		
				Icon state of the window.
				
		"""
		return self.query(iconify=True)
	#----------------------------------------------------------------------
	def set_iconify(self, value):
		"""
		
				Icon state of the window.
				
		"""
		self.edit(iconify=value)
	#----------------------------------------------------------------------
	iconify = property(get_iconify, set_iconify)
	#----------------------------------------------------------------------
	def get_leftEdge(self):
		"""
		
				Position of the left edge of the window.
				
		"""
		return self.query(leftEdge=True)
	#----------------------------------------------------------------------
	def set_leftEdge(self, value):
		"""
		
				Position of the left edge of the window.
				
		"""
		self.edit(leftEdge=value)
	#----------------------------------------------------------------------
	leftEdge = property(get_leftEdge, set_leftEdge)
	#----------------------------------------------------------------------
	def get_mainMenuBar(self):
		"""
		
				If this flag is used then the main menu bar will be enabled.
				
		"""
		return self.query(mainMenuBar=True)
	#----------------------------------------------------------------------
	def set_mainMenuBar(self, value):
		"""
		
				If this flag is used then the main menu bar will be enabled.
				
		"""
		self.edit(mainMenuBar=value)
	#----------------------------------------------------------------------
	mainMenuBar = property(get_mainMenuBar, set_mainMenuBar)
	#----------------------------------------------------------------------
	def get_mainWindow(self):
		"""
		
				Main window for the application.  The main window
				has an 'Exit' item in the Window Manager menu.  By default, the
				first created window becomes the main window.
				
		"""
		return self.query(mainWindow=True)
	#----------------------------------------------------------------------
	def set_mainWindow(self, value):
		"""
		
				Main window for the application.  The main window
				has an 'Exit' item in the Window Manager menu.  By default, the
				first created window becomes the main window.
				
		"""
		self.edit(mainWindow=value)
	#----------------------------------------------------------------------
	mainWindow = property(get_mainWindow, set_mainWindow)
	#----------------------------------------------------------------------
	def get_maximizeButton(self):
		"""
		
				Turns the window's maximize button on or off.
				
		"""
		return self.query(maximizeButton=True)
	#----------------------------------------------------------------------
	def set_maximizeButton(self, value):
		"""
		
				Turns the window's maximize button on or off.
				
		"""
		self.edit(maximizeButton=value)
	#----------------------------------------------------------------------
	maximizeButton = property(get_maximizeButton, set_maximizeButton)
	#----------------------------------------------------------------------
	@property
	def menuArray(self):
		"""
		
				Return a string array containing the names of the menus in
				the window's menu bar.
				
		"""
		return self.query(menuArray=True)
	#----------------------------------------------------------------------
	@property
	def menuBar(self):
		"""
		
				Adds an empty menu bar to the window.
				The Qt name of the object will be m_menubar_nameOfTheWindow.
				
		"""
		return self.query(menuBar=True)
	#----------------------------------------------------------------------
	def get_menuBarCornerWidget(self):
		"""
		
				This flag specifies a widget to add to a corner of the parent window.
				The first argument corresponds to the widget name and the second to the position of the widget.
				Possible values for widget position are "topLeft", "topRight", "bottomLeft", "bottomRight".
				In query mode this flag returns all the corner widget names in the following order: topLeft, topRight, bottomLeft, bottomRight.
				Add the -mbr/-menuBarResize flag to the changeCommand of widget passed (first argument) so that it will always have an
				appropriate size.
				
		"""
		return self.query(menuBarCornerWidget=True)
	#----------------------------------------------------------------------
	def set_menuBarCornerWidget(self, value):
		"""
		
				This flag specifies a widget to add to a corner of the parent window.
				The first argument corresponds to the widget name and the second to the position of the widget.
				Possible values for widget position are "topLeft", "topRight", "bottomLeft", "bottomRight".
				In query mode this flag returns all the corner widget names in the following order: topLeft, topRight, bottomLeft, bottomRight.
				Add the -mbr/-menuBarResize flag to the changeCommand of widget passed (first argument) so that it will always have an
				appropriate size.
				
		"""
		self.edit(menuBarCornerWidget=value)
	#----------------------------------------------------------------------
	menuBarCornerWidget = property(get_menuBarCornerWidget, set_menuBarCornerWidget)
	#----------------------------------------------------------------------
	def menuBarResize(self,value):
		"""
		
				This flag should be used with the -mcw/-menuBarCornerWidget flag. This is used to resize the
				menu bar so that the corner widgets are updated.
				
		"""
		self.edit(menuBarResize=value)
	#----------------------------------------------------------------------
	def get_menuBarVisible(self):
		"""
		
				Visibility of the menu bar (if there is one).
				
		"""
		return self.query(menuBarVisible=True)
	#----------------------------------------------------------------------
	def set_menuBarVisible(self, value):
		"""
		
				Visibility of the menu bar (if there is one).
				
		"""
		self.edit(menuBarVisible=value)
	#----------------------------------------------------------------------
	menuBarVisible = property(get_menuBarVisible, set_menuBarVisible)
	#----------------------------------------------------------------------
	def menuIndex(self,value):
		"""
		
				Sets the index of a specified menu.
				
		"""
		self.edit(menuIndex=value)
	#----------------------------------------------------------------------
	def get_minimizeButton(self):
		"""
		
				Turns the window's minimize button on or off.
				
		"""
		return self.query(minimizeButton=True)
	#----------------------------------------------------------------------
	def set_minimizeButton(self, value):
		"""
		
				Turns the window's minimize button on or off.
				
		"""
		self.edit(minimizeButton=value)
	#----------------------------------------------------------------------
	minimizeButton = property(get_minimizeButton, set_minimizeButton)
	#----------------------------------------------------------------------
	def minimizeCommand(self,value):
		"""
		
				Script executed after the window is minimized (iconified).
				
		"""
		self.edit(minimizeCommand=value)
	#----------------------------------------------------------------------
	@property
	def numberOfMenus(self):
		"""
		
				Return the number of menus attached to the window's menu bar.
				
		"""
		return self.query(numberOfMenus=True)
	#----------------------------------------------------------------------
	def get_resizeToFitChildren(self):
		"""
		
				The window will always grow/shrink to just fit
				the controls it contains.
				
		"""
		return self.query(resizeToFitChildren=True)
	#----------------------------------------------------------------------
	def set_resizeToFitChildren(self, value):
		"""
		
				The window will always grow/shrink to just fit
				the controls it contains.
				
		"""
		self.edit(resizeToFitChildren=value)
	#----------------------------------------------------------------------
	resizeToFitChildren = property(get_resizeToFitChildren, set_resizeToFitChildren)
	#----------------------------------------------------------------------
	def restoreCommand(self,value):
		"""
		
				Script executed after the window is restored from
				it's minimized (iconified) state.
				
		"""
		self.edit(restoreCommand=value)
	#----------------------------------------------------------------------
	def get_sizeable(self):
		"""
		
				Whether or not the window may be interactively resized.
				
		"""
		return self.query(sizeable=True)
	#----------------------------------------------------------------------
	def set_sizeable(self, value):
		"""
		
				Whether or not the window may be interactively resized.
				
		"""
		self.edit(sizeable=value)
	#----------------------------------------------------------------------
	sizeable = property(get_sizeable, set_sizeable)
	#----------------------------------------------------------------------
	def get_state(self):
		"""
		
				When queried this flag will return a string holding the window state information.
				This string is a hexadecimal representation of a binary string and is not meant to be humanly readable,
				but can be saved and loaded using the optionVar command to restore window state across sessions of Maya.
				
		"""
		return self.query(state=True)
	#----------------------------------------------------------------------
	def set_state(self, value):
		"""
		
				When queried this flag will return a string holding the window state information.
				This string is a hexadecimal representation of a binary string and is not meant to be humanly readable,
				but can be saved and loaded using the optionVar command to restore window state across sessions of Maya.
				
		"""
		self.edit(state=value)
	#----------------------------------------------------------------------
	state = property(get_state, set_state)
	#----------------------------------------------------------------------
	def get_title(self):
		"""
		
				The window's title.
				
		"""
		return self.query(title=True)
	#----------------------------------------------------------------------
	def set_title(self, value):
		"""
		
				The window's title.
				
		"""
		self.edit(title=value)
	#----------------------------------------------------------------------
	title = property(get_title, set_title)
	#----------------------------------------------------------------------
	def get_titleBar(self):
		"""
		
				Turns the window's title bar on or off.
				
		"""
		return self.query(titleBar=True)
	#----------------------------------------------------------------------
	def set_titleBar(self, value):
		"""
		
				Turns the window's title bar on or off.
				
		"""
		self.edit(titleBar=value)
	#----------------------------------------------------------------------
	titleBar = property(get_titleBar, set_titleBar)
	#----------------------------------------------------------------------
	def get_titleBarMenu(self):
		"""
		
				Controls whether the title bar menu exists in the window
				title bar. Only valid if -tb/titleBar is true. This Windows
				only flag is true by default.
				
		"""
		return self.query(titleBarMenu=True)
	#----------------------------------------------------------------------
	def set_titleBarMenu(self, value):
		"""
		
				Controls whether the title bar menu exists in the window
				title bar. Only valid if -tb/titleBar is true. This Windows
				only flag is true by default.
				
		"""
		self.edit(titleBarMenu=value)
	#----------------------------------------------------------------------
	titleBarMenu = property(get_titleBarMenu, set_titleBarMenu)
	#----------------------------------------------------------------------
	def get_toolbox(self):
		"""
		
				Makes this a toolbox style window.  A Windows only
				flag that makes the title bar smaller and uses a slightly
				different display style.
				
		"""
		return self.query(toolbox=True)
	#----------------------------------------------------------------------
	def set_toolbox(self, value):
		"""
		
				Makes this a toolbox style window.  A Windows only
				flag that makes the title bar smaller and uses a slightly
				different display style.
				
		"""
		self.edit(toolbox=value)
	#----------------------------------------------------------------------
	toolbox = property(get_toolbox, set_toolbox)
	#----------------------------------------------------------------------
	def get_topEdge(self):
		"""
		
				Position of the top edge of the window.
				
		"""
		return self.query(topEdge=True)
	#----------------------------------------------------------------------
	def set_topEdge(self, value):
		"""
		
				Position of the top edge of the window.
				
		"""
		self.edit(topEdge=value)
	#----------------------------------------------------------------------
	topEdge = property(get_topEdge, set_topEdge)
	#----------------------------------------------------------------------
	def get_topLeftCorner(self):
		"""
		
				Position of the window's top left corner.
				
		"""
		return self.query(topLeftCorner=True)
	#----------------------------------------------------------------------
	def set_topLeftCorner(self, value):
		"""
		
				Position of the window's top left corner.
				
		"""
		self.edit(topLeftCorner=value)
	#----------------------------------------------------------------------
	topLeftCorner = property(get_topLeftCorner, set_topLeftCorner)
	#----------------------------------------------------------------------
	def get_visible(self):
		"""
		
				The window's visibility.
				
		"""
		return self.query(visible=True)
	#----------------------------------------------------------------------
	def set_visible(self, value):
		"""
		
				The window's visibility.
				
		"""
		self.edit(visible=value)
	#----------------------------------------------------------------------
	visible = property(get_visible, set_visible)
	#----------------------------------------------------------------------
	def get_width(self):
		"""
		
				Width of the window excluding any window frame in pixels.
				
		"""
		return self.query(width=True)
	#----------------------------------------------------------------------
	def set_width(self, value):
		"""
		
				Width of the window excluding any window frame in pixels.
				
		"""
		self.edit(width=value)
	#----------------------------------------------------------------------
	width = property(get_width, set_width)
	#----------------------------------------------------------------------
	def get_widthHeight(self):
		"""
		
				Window's width and height excluding any window frame in pixels.
				
		"""
		return self.query(widthHeight=True)
	#----------------------------------------------------------------------
	def set_widthHeight(self, value):
		"""
		
				Window's width and height excluding any window frame in pixels.
				
		"""
		self.edit(widthHeight=value)
	#----------------------------------------------------------------------
	widthHeight = property(get_widthHeight, set_widthHeight)