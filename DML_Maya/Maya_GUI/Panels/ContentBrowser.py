

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class ContentBrowser(UI_Object.UI):
	"""
	This command is used to edit and query a Content Browser. The Content Browser is
	a unique panel, so only one instance of it can exist at a given time.
	The optional argument is the name of the control.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.contentBrowser(**kwargs)
			super(ContentBrowser, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.contentBrowser(name, exists=True):
				super(ContentBrowser, self).__init__(name)
			else:
				name = cmds.contentBrowser(name, **kwargs)
				super(ContentBrowser, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def addContentPath(self,value):
		"""
		
				Adds the given path(s) to the libraries displayed on the Examples tab.
				Also updates the corresponding MAYA_CONTENT_PATH environment variable.
				
		"""
		self.edit(addContentPath=value)
	#----------------------------------------------------------------------
	def get_context(self):
		"""
		
				Sets the default location for the given context. The two optional arguments
				(Python only) are the category (tab) and location. To clear the content use
				empty strings for category and location.
				
				In query mode, it returns the context of the content browser in an array of 3 strings :
				the name of the context, the default category name, the default location.
				
		"""
		return self.query(context=True)
	#----------------------------------------------------------------------
	def set_context(self, value):
		"""
		
				Sets the default location for the given context. The two optional arguments
				(Python only) are the category (tab) and location. To clear the content use
				empty strings for category and location.
				
				In query mode, it returns the context of the content browser in an array of 3 strings :
				the name of the context, the default category name, the default location.
				
		"""
		self.edit(context=value)
	#----------------------------------------------------------------------
	context = property(get_context, set_context)
	#----------------------------------------------------------------------
	@property
	def control(self):
		"""
		
				Query only. Returns the top level control for this editor.
				Usually used for getting a parent to attach popup menus.
				Caution: It is possible for an editor to exist without a
				control. The query will return "NONE" if no control is present.
				
		"""
		return self.query(control=True)
	#----------------------------------------------------------------------
	def get_docTag(self):
		"""
		
				Attaches a tag to the editor.
				
		"""
		return self.query(docTag=True)
	#----------------------------------------------------------------------
	def set_docTag(self, value):
		"""
		
				Attaches a tag to the editor.
				
		"""
		self.edit(docTag=value)
	#----------------------------------------------------------------------
	docTag = property(get_docTag, set_docTag)
	#----------------------------------------------------------------------
	def get_filter(self):
		"""
		
				Specifies the name of an itemFilter object to be used with this editor.
				This filters the information coming onto the main list
				of the editor.
				
		"""
		return self.query(filter=True)
	#----------------------------------------------------------------------
	def set_filter(self, value):
		"""
		
				Specifies the name of an itemFilter object to be used with this editor.
				This filters the information coming onto the main list
				of the editor.
				
		"""
		self.edit(filter=value)
	#----------------------------------------------------------------------
	filter = property(get_filter, set_filter)
	#----------------------------------------------------------------------
	def get_forceMainConnection(self):
		"""
		
				Specifies the name of a selectionConnection object that the
				editor will use as its source of content. The editor will only
				display items contained in the selectionConnection object. This is
				a variant of the -mainListConnection flag in that it will force a
				change even when the connection is locked. This flag is used to
				reduce the overhead when using the -unlockMainConnection
				, -mainListConnection, -lockMainConnection flags in immediate
				succession.
				
		"""
		return self.query(forceMainConnection=True)
	#----------------------------------------------------------------------
	def set_forceMainConnection(self, value):
		"""
		
				Specifies the name of a selectionConnection object that the
				editor will use as its source of content. The editor will only
				display items contained in the selectionConnection object. This is
				a variant of the -mainListConnection flag in that it will force a
				change even when the connection is locked. This flag is used to
				reduce the overhead when using the -unlockMainConnection
				, -mainListConnection, -lockMainConnection flags in immediate
				succession.
				
		"""
		self.edit(forceMainConnection=value)
	#----------------------------------------------------------------------
	forceMainConnection = property(get_forceMainConnection, set_forceMainConnection)
	#----------------------------------------------------------------------
	def get_highlightConnection(self):
		"""
		
				Specifies the name of a selectionConnection object that
				the editor will synchronize with its highlight list. Not all
				editors have a highlight list. For those that do, it is a secondary
				selection list.
				
		"""
		return self.query(highlightConnection=True)
	#----------------------------------------------------------------------
	def set_highlightConnection(self, value):
		"""
		
				Specifies the name of a selectionConnection object that
				the editor will synchronize with its highlight list. Not all
				editors have a highlight list. For those that do, it is a secondary
				selection list.
				
		"""
		self.edit(highlightConnection=value)
	#----------------------------------------------------------------------
	highlightConnection = property(get_highlightConnection, set_highlightConnection)
	#----------------------------------------------------------------------
	def location(self,value):
		"""
		
				Switches to the Examples tab and selects the given library location.
				
		"""
		self.edit(location=value)
	#----------------------------------------------------------------------
	def lockMainConnection(self,value):
		"""
		
				Locks the current list of objects within the mainConnection,
				so that only those objects are displayed within the editor.
				Further changes to the original mainConnection are ignored.
				
		"""
		self.edit(lockMainConnection=value)
	#----------------------------------------------------------------------
	def get_mainListConnection(self):
		"""
		
				Specifies the name of a selectionConnection object that the
				editor will use as its source of content. The editor will
				only display items contained in the selectionConnection object.
				
		"""
		return self.query(mainListConnection=True)
	#----------------------------------------------------------------------
	def set_mainListConnection(self, value):
		"""
		
				Specifies the name of a selectionConnection object that the
				editor will use as its source of content. The editor will
				only display items contained in the selectionConnection object.
				
		"""
		self.edit(mainListConnection=value)
	#----------------------------------------------------------------------
	mainListConnection = property(get_mainListConnection, set_mainListConnection)
	#----------------------------------------------------------------------
	@property
	def panel(self):
		"""
		
				Specifies the panel for this editor. By default if
				an editor is created in the create callback of a scripted panel it
				will belong to that panel. If an editor does not belong to a panel
				it will be deleted when the window that it is in is deleted.
				
		"""
		return self.query(panel=True)
	#----------------------------------------------------------------------
	def get_parent(self):
		"""
		
				Specifies the parent layout for this editor. This flag will only
				have an effect if the editor is currently un-parented.
				
		"""
		return self.query(parent=True)
	#----------------------------------------------------------------------
	def set_parent(self, value):
		"""
		
				Specifies the parent layout for this editor. This flag will only
				have an effect if the editor is currently un-parented.
				
		"""
		self.edit(parent=value)
	#----------------------------------------------------------------------
	parent = property(get_parent, set_parent)
	#----------------------------------------------------------------------
	def preview(self,value):
		"""
		
				Shows / hides the preview panel.
				Note: this flag will not affect the currently opened Content Browser, but only
				any subsequently opened ones.
				
		"""
		self.edit(preview=value)
	#----------------------------------------------------------------------
	def refreshTreeView(self,value):
		"""
		
				Forces a refresh of the Examples tab tree view pane.
				
		"""
		self.edit(refreshTreeView=value)
	#----------------------------------------------------------------------
	def removeContentPath(self,value):
		"""
		
				Removes the given path(s) from the libraries displayed on the Examples tab.
				Also updates the corresponding MAYA_CONTENT_PATH environment variable.
				
		"""
		self.edit(removeContentPath=value)
	#----------------------------------------------------------------------
	def saveCurrentContext(self,value):
		"""
		
				Saves the context for the current Content Browser tab.
				
		"""
		self.edit(saveCurrentContext=value)
	#----------------------------------------------------------------------
	def get_selectionConnection(self):
		"""
		
				Specifies the name of a selectionConnection object that the
				editor will synchronize with its own selection list. As the user
				selects things in this editor, they will be selected in the
				selectionConnection object. If the object undergoes changes, the
				editor updates to show the changes.
				
		"""
		return self.query(selectionConnection=True)
	#----------------------------------------------------------------------
	def set_selectionConnection(self, value):
		"""
		
				Specifies the name of a selectionConnection object that the
				editor will synchronize with its own selection list. As the user
				selects things in this editor, they will be selected in the
				selectionConnection object. If the object undergoes changes, the
				editor updates to show the changes.
				
		"""
		self.edit(selectionConnection=value)
	#----------------------------------------------------------------------
	selectionConnection = property(get_selectionConnection, set_selectionConnection)
	#----------------------------------------------------------------------
	@property
	def stateString(self):
		"""
		
				Query only flag. Returns the MEL command that will create an
				editor to match the current editor state. The returned command string
				uses the string variable $editorName in place of a specific name.
				
		"""
		return self.query(stateString=True)
	#----------------------------------------------------------------------
	def thumbnailView(self,value):
		"""
		
				Shows / hides the thumbnail panel.
				Note: this flag will not affect the currently opened Content Browser, but only
				any subsequently opened ones.
				
		"""
		self.edit(thumbnailView=value)
	#----------------------------------------------------------------------
	def treeView(self,value):
		"""
		
				Shows / hides the tree view panel.
				Note: this flag will not affect the currently opened Content Browser, but only
				any subsequently opened ones.
				
		"""
		self.edit(treeView=value)
	#----------------------------------------------------------------------
	def unParent(self,value):
		"""
		
				Specifies that the editor should be removed from its layout.
				This cannot be used in query mode.
				
		"""
		self.edit(unParent=value)
	#----------------------------------------------------------------------
	def unlockMainConnection(self,value):
		"""
		
				Unlocks the mainConnection, effectively restoring the original
				mainConnection (if it is still available), and dynamic updates.
				
		"""
		self.edit(unlockMainConnection=value)
	#----------------------------------------------------------------------
	def updateMainConnection(self,value):
		"""
		
				Causes a locked mainConnection to be updated from the orginal
				mainConnection, but preserves the lock state.
				
		"""
		self.edit(updateMainConnection=value)