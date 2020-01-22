

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class SpreadSheetEditor(UI_Object.UI):
	"""
	This command creates a new spread sheet editor in the
	current layout.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.spreadSheetEditor(**kwargs)
			super(SpreadSheetEditor, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.spreadSheetEditor(name, exists=True):
				super(SpreadSheetEditor, self).__init__(name)
			else:
				name = cmds.spreadSheetEditor(name, **kwargs)
				super(SpreadSheetEditor, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def allAttr(self):
		"""
		
				Returns a list of all the attribute names
				currently being displayed.  This flag is ignored when not being queried.
				
		"""
		return self.query(allAttr=True)
	#----------------------------------------------------------------------
	def get_attrRegExp(self):
		"""
		
				Filter the current displayed attribute names.
				This expression matches the case-insensitive substring of attribute names.
				
		"""
		return self.query(attrRegExp=True)
	#----------------------------------------------------------------------
	def set_attrRegExp(self, value):
		"""
		
				Filter the current displayed attribute names.
				This expression matches the case-insensitive substring of attribute names.
				
		"""
		self.edit(attrRegExp=value)
	#----------------------------------------------------------------------
	attrRegExp = property(get_attrRegExp, set_attrRegExp)
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
	def execute(self,value):
		"""
		
				Immediately executes the command string once for every selected
				cell in the spreadSheet.  Before the command is executed, "#A" is
				substituted with the name of the cell's attribute, "#N" is substituted
				with the name of the cell's node, and "#P" is substituted with the
				full path name of the node.
				
		"""
		self.edit(execute=value)
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
	def get_fixedAttrList(self):
		"""
		
				Forces the editor to only display attributes with the
				specified names.
				
		"""
		return self.query(fixedAttrList=True)
	#----------------------------------------------------------------------
	def set_fixedAttrList(self, value):
		"""
		
				Forces the editor to only display attributes with the
				specified names.
				
		"""
		self.edit(fixedAttrList=value)
	#----------------------------------------------------------------------
	fixedAttrList = property(get_fixedAttrList, set_fixedAttrList)
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
	def get_keyableOnly(self):
		"""
		
				Limits the displayed attributes to be those that are keyable.
				True by default
				
		"""
		return self.query(keyableOnly=True)
	#----------------------------------------------------------------------
	def set_keyableOnly(self, value):
		"""
		
				Limits the displayed attributes to be those that are keyable.
				True by default
				
		"""
		self.edit(keyableOnly=value)
	#----------------------------------------------------------------------
	keyableOnly = property(get_keyableOnly, set_keyableOnly)
	#----------------------------------------------------------------------
	def lockMainConnection(self,value):
		"""
		
				Locks the current list of objects within the mainConnection,
				so that only those objects are displayed within the editor.
				Further changes to the original mainConnection are ignored.
				
		"""
		self.edit(lockMainConnection=value)
	#----------------------------------------------------------------------
	def get_longNames(self):
		"""
		
				Controls whether the attributes are displayed using their
				long names or their short names.
				
		"""
		return self.query(longNames=True)
	#----------------------------------------------------------------------
	def set_longNames(self, value):
		"""
		
				Controls whether the attributes are displayed using their
				long names or their short names.
				
		"""
		self.edit(longNames=value)
	#----------------------------------------------------------------------
	longNames = property(get_longNames, set_longNames)
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
	def get_niceNames(self):
		"""
		
				Controls whether the attribute names will be displayed in
				a more user-friendly, readable way.  When this is on, the longNames
				flag is ignored.  When this is off, attribute names will be displayed
				either long or short, according to the longNames flag.
				Default is on. Queried, returns a boolean.
				
		"""
		return self.query(niceNames=True)
	#----------------------------------------------------------------------
	def set_niceNames(self, value):
		"""
		
				Controls whether the attribute names will be displayed in
				a more user-friendly, readable way.  When this is on, the longNames
				flag is ignored.  When this is off, attribute names will be displayed
				either long or short, according to the longNames flag.
				Default is on. Queried, returns a boolean.
				
		"""
		self.edit(niceNames=value)
	#----------------------------------------------------------------------
	niceNames = property(get_niceNames, set_niceNames)
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
	@property
	def selectedAttr(self):
		"""
		
				Returns a list of all the attribute names
				that are selected.  This flag is ignored when not being queried.
				
		"""
		return self.query(selectedAttr=True)
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
	def get_showShapes(self):
		"""
		
				If true, when transforms are selected their shapes will
				be displayed instead.
				
		"""
		return self.query(showShapes=True)
	#----------------------------------------------------------------------
	def set_showShapes(self, value):
		"""
		
				If true, when transforms are selected their shapes will
				be displayed instead.
				
		"""
		self.edit(showShapes=value)
	#----------------------------------------------------------------------
	showShapes = property(get_showShapes, set_showShapes)
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