

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class ComponentEditor(UI_Object.UI):
	"""
	This command creates a new component editor
	in the current layout.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.componentEditor(**kwargs)
			super(ComponentEditor, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.componentEditor(name, exists=True):
				super(ComponentEditor, self).__init__(name)
			else:
				name = cmds.componentEditor(name, **kwargs)
				super(ComponentEditor, self).__init__(name, **dict(qtParent=parent))
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
	def get_floatField(self):
		"""
		
				assigns a float field that the component editor will
				use for editing groups of values.
				
		"""
		return self.query(floatField=True)
	#----------------------------------------------------------------------
	def set_floatField(self, value):
		"""
		
				assigns a float field that the component editor will
				use for editing groups of values.
				
		"""
		self.edit(floatField=value)
	#----------------------------------------------------------------------
	floatField = property(get_floatField, set_floatField)
	#----------------------------------------------------------------------
	def get_floatSlider(self):
		"""
		
				assigns a float slider that the component editor will
				use for editing groups of values.
				
		"""
		return self.query(floatSlider=True)
	#----------------------------------------------------------------------
	def set_floatSlider(self, value):
		"""
		
				assigns a float slider that the component editor will
				use for editing groups of values.
				
		"""
		self.edit(floatSlider=value)
	#----------------------------------------------------------------------
	floatSlider = property(get_floatSlider, set_floatSlider)
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
	def get_hidePathName(self):
		"""
		
				Hides path name of displayed element.  By default
				this flag is set to false.
				
		"""
		return self.query(hidePathName=True)
	#----------------------------------------------------------------------
	def set_hidePathName(self, value):
		"""
		
				Hides path name of displayed element.  By default
				this flag is set to false.
				
		"""
		self.edit(hidePathName=value)
	#----------------------------------------------------------------------
	hidePathName = property(get_hidePathName, set_hidePathName)
	#----------------------------------------------------------------------
	def get_hideZeroColumns(self):
		"""
		
				Hides columns whose elements are all zero.  By default
				this flag is set to false.
				
		"""
		return self.query(hideZeroColumns=True)
	#----------------------------------------------------------------------
	def set_hideZeroColumns(self, value):
		"""
		
				Hides columns whose elements are all zero.  By default
				this flag is set to false.
				
		"""
		self.edit(hideZeroColumns=value)
	#----------------------------------------------------------------------
	hideZeroColumns = property(get_hideZeroColumns, set_hideZeroColumns)
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
	def get_lockInput(self):
		"""
		
				Prevents the editor from responding to changes in
				the active list. Independent of selection connection.
				
		"""
		return self.query(lockInput=True)
	#----------------------------------------------------------------------
	def set_lockInput(self, value):
		"""
		
				Prevents the editor from responding to changes in
				the active list. Independent of selection connection.
				
		"""
		self.edit(lockInput=value)
	#----------------------------------------------------------------------
	lockInput = property(get_lockInput, set_lockInput)
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
	def newTab(self,value):
		"""
		
				Creates a new tab, named by the first argument, based on an existing tab, given as the second argument
				using elements from a set, given in the third argument
				
		"""
		self.edit(newTab=value)
	#----------------------------------------------------------------------
	@property
	def operationCount(self):
		"""
		
				returns the total number of operation types
				known to the component editor.
				
		"""
		return self.query(operationCount=True)
	#----------------------------------------------------------------------
	@property
	def operationLabels(self):
		"""
		
				returns a string array containing the names for all
				operation types known to the editor.
				
		"""
		return self.query(operationLabels=True)
	#----------------------------------------------------------------------
	def get_operationType(self):
		"""
		
				Tells the editor which of its known operation types
				it should be performing. This is a 0-based index.
				
		"""
		return self.query(operationType=True)
	#----------------------------------------------------------------------
	def set_operationType(self, value):
		"""
		
				Tells the editor which of its known operation types
				it should be performing. This is a 0-based index.
				
		"""
		self.edit(operationType=value)
	#----------------------------------------------------------------------
	operationType = property(get_operationType, set_operationType)
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
	def get_precision(self):
		"""
		
				Specifies the maximum number of digits displayed to the right
				of the decimal place.  Can be 0 to 20.
				
		"""
		return self.query(precision=True)
	#----------------------------------------------------------------------
	def set_precision(self, value):
		"""
		
				Specifies the maximum number of digits displayed to the right
				of the decimal place.  Can be 0 to 20.
				
		"""
		self.edit(precision=value)
	#----------------------------------------------------------------------
	precision = property(get_precision, set_precision)
	#----------------------------------------------------------------------
	def removeTab(self,value):
		"""
		
				Removes the tab based on the set provided
				
		"""
		self.edit(removeTab=value)
	#----------------------------------------------------------------------
	@property
	def selected(self):
		"""
		
				Returns a list of strings, containing the labels of the currently selected columns
				
		"""
		return self.query(selected=True)
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
	def setOperationLabel(self,value):
		"""
		
				uses the string as the new name for the existing operation type
				specified by the integer index. Note that there is no messaging
				system which allows UI to be informed of changes made by this flag.
				
		"""
		self.edit(setOperationLabel=value)
	#----------------------------------------------------------------------
	def showSelected(self,value):
		"""
		
				Restricts the display to those columns which are currently selected. By default
				this flag is set to false, so all columns are selected. The results from this flag
				obey the current -hideZeroColumns setting.
				
		"""
		self.edit(showSelected=value)
	#----------------------------------------------------------------------
	def get_sortAlpha(self):
		"""
		
				Controls alphabetical (true), or hierarchical sorting of columns
				
		"""
		return self.query(sortAlpha=True)
	#----------------------------------------------------------------------
	def set_sortAlpha(self, value):
		"""
		
				Controls alphabetical (true), or hierarchical sorting of columns
				
		"""
		self.edit(sortAlpha=value)
	#----------------------------------------------------------------------
	sortAlpha = property(get_sortAlpha, set_sortAlpha)
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