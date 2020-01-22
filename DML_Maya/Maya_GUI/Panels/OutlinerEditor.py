

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class OutlinerEditor(UI_Object.UI):
	"""
	This command creates an outliner editor which can be used to display a list
	of objects.
	WARNING: some flag combinations may not behave as you expect.  The command
	is really intended for internal use for creating the outliner used by
	the various editors.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.outlinerEditor(**kwargs)
			super(OutlinerEditor, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.outlinerEditor(name, exists=True):
				super(OutlinerEditor, self).__init__(name)
			else:
				name = cmds.outlinerEditor(name, **kwargs)
				super(OutlinerEditor, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def allowMultiSelection(self,value):
		"""
		
				If true then multiple selection will be allowed in the outliner.
				
		"""
		self.edit(allowMultiSelection=value)
	#----------------------------------------------------------------------
	def alwaysToggleSelect(self,value):
		"""
		
				If true, then clicking on an item in the outliner will select or
				deselect it without affecting the selection of other items (unless
				allowMultiSelection is false). If false, clicking on an item in the
				outliner will replace the current selection with the selected item.
				
		"""
		self.edit(alwaysToggleSelect=value)
	#----------------------------------------------------------------------
	def get_animLayerFilterOptions(self):
		"""
		
				Specifies whether a filter is to be applied when displaying animation layers.
				If so, the options can be "allAffecting" (no filter), "active" (only the active
				layers on the object will be displayed) and "animLayerEditor" (the settings will
				be taken from the animation layer editor).
				
		"""
		return self.query(animLayerFilterOptions=True)
	#----------------------------------------------------------------------
	def set_animLayerFilterOptions(self, value):
		"""
		
				Specifies whether a filter is to be applied when displaying animation layers.
				If so, the options can be "allAffecting" (no filter), "active" (only the active
				layers on the object will be displayed) and "animLayerEditor" (the settings will
				be taken from the animation layer editor).
				
		"""
		self.edit(animLayerFilterOptions=value)
	#----------------------------------------------------------------------
	animLayerFilterOptions = property(get_animLayerFilterOptions, set_animLayerFilterOptions)
	#----------------------------------------------------------------------
	def get_attrAlphaOrder(self):
		"""
		
				Specify how attributes are to be sorted. Current recognised values
				are "default" for no sorting and "ascend" to sort attributes from 'a' to ''z' and
				"descend" to sort from 'z' to 'a'.
				Notes: a) this only applies to top level attributes.
				
		"""
		return self.query(attrAlphaOrder=True)
	#----------------------------------------------------------------------
	def set_attrAlphaOrder(self, value):
		"""
		
				Specify how attributes are to be sorted. Current recognised values
				are "default" for no sorting and "ascend" to sort attributes from 'a' to ''z' and
				"descend" to sort from 'z' to 'a'.
				Notes: a) this only applies to top level attributes.
				
		"""
		self.edit(attrAlphaOrder=value)
	#----------------------------------------------------------------------
	attrAlphaOrder = property(get_attrAlphaOrder, set_attrAlphaOrder)
	#----------------------------------------------------------------------
	def get_attrFilter(self):
		"""
		
				Specifies the name of an itemFilter object to be placed on this editor.
				This filters the attributes displayed in the editor.
				
		"""
		return self.query(attrFilter=True)
	#----------------------------------------------------------------------
	def set_attrFilter(self, value):
		"""
		
				Specifies the name of an itemFilter object to be placed on this editor.
				This filters the attributes displayed in the editor.
				
		"""
		self.edit(attrFilter=value)
	#----------------------------------------------------------------------
	attrFilter = property(get_attrFilter, set_attrFilter)
	#----------------------------------------------------------------------
	def get_autoExpand(self):
		"""
		
				This flag specifies whether or not objects that are loaded
				in should have their attributes automatically expanded.
				
		"""
		return self.query(autoExpand=True)
	#----------------------------------------------------------------------
	def set_autoExpand(self, value):
		"""
		
				This flag specifies whether or not objects that are loaded
				in should have their attributes automatically expanded.
				
		"""
		self.edit(autoExpand=value)
	#----------------------------------------------------------------------
	autoExpand = property(get_autoExpand, set_autoExpand)
	#----------------------------------------------------------------------
	def get_autoExpandLayers(self):
		"""
		
				If true then when a node with animation layer is displayed, all
				the animation layers will show up in expanded form.
				
		"""
		return self.query(autoExpandLayers=True)
	#----------------------------------------------------------------------
	def set_autoExpandLayers(self, value):
		"""
		
				If true then when a node with animation layer is displayed, all
				the animation layers will show up in expanded form.
				
		"""
		self.edit(autoExpandLayers=value)
	#----------------------------------------------------------------------
	autoExpandLayers = property(get_autoExpandLayers, set_autoExpandLayers)
	#----------------------------------------------------------------------
	def get_autoSelectNewObjects(self):
		"""
		
				This flag specifies whether or not new objects added to the outliner
				should be automatically selected.
				
		"""
		return self.query(autoSelectNewObjects=True)
	#----------------------------------------------------------------------
	def set_autoSelectNewObjects(self, value):
		"""
		
				This flag specifies whether or not new objects added to the outliner
				should be automatically selected.
				
		"""
		self.edit(autoSelectNewObjects=value)
	#----------------------------------------------------------------------
	autoSelectNewObjects = property(get_autoSelectNewObjects, set_autoSelectNewObjects)
	#----------------------------------------------------------------------
	def get_containersIgnoreFilters(self):
		"""
		
				This flag specifices whether or not filters should be ignored
				when displaying container contents.
				
		"""
		return self.query(containersIgnoreFilters=True)
	#----------------------------------------------------------------------
	def set_containersIgnoreFilters(self, value):
		"""
		
				This flag specifices whether or not filters should be ignored
				when displaying container contents.
				
		"""
		self.edit(containersIgnoreFilters=value)
	#----------------------------------------------------------------------
	containersIgnoreFilters = property(get_containersIgnoreFilters, set_containersIgnoreFilters)
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
	def directSelect(self,value):
		"""
		
				If true then clicking on an item in the outliner will add or
				remove just that item from the selection connection. If false then
				clicking on an item in the outliner causes the selection connection
				to be reloaded with the currently selected items in the outliner.
				
		"""
		self.edit(directSelect=value)
	#----------------------------------------------------------------------
	def get_displayMode(self):
		"""
		
				Affects how the outliner displays when a filter is applied. List mode
				is a non-indented flat list. DAG mode indents to represent the
				hierarchical structure of the model.
				
		"""
		return self.query(displayMode=True)
	#----------------------------------------------------------------------
	def set_displayMode(self, value):
		"""
		
				Affects how the outliner displays when a filter is applied. List mode
				is a non-indented flat list. DAG mode indents to represent the
				hierarchical structure of the model.
				
		"""
		self.edit(displayMode=value)
	#----------------------------------------------------------------------
	displayMode = property(get_displayMode, set_displayMode)
	#----------------------------------------------------------------------
	def get_doNotSelectNewObjects(self):
		"""
		
				If true this flag specifies that new objects added to the outliner
				will not be selected, even if they are active.
				
		"""
		return self.query(doNotSelectNewObjects=True)
	#----------------------------------------------------------------------
	def set_doNotSelectNewObjects(self, value):
		"""
		
				If true this flag specifies that new objects added to the outliner
				will not be selected, even if they are active.
				
		"""
		self.edit(doNotSelectNewObjects=value)
	#----------------------------------------------------------------------
	doNotSelectNewObjects = property(get_doNotSelectNewObjects, set_doNotSelectNewObjects)
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
	def get_dropIsParent(self):
		"""
		
				This flag specifies the mode for drag and drop. If the flag is true,
				dropping items will do a reparent. If it is false, dropping will
				reorder items. By default, the flag is true (parent).
				
		"""
		return self.query(dropIsParent=True)
	#----------------------------------------------------------------------
	def set_dropIsParent(self, value):
		"""
		
				This flag specifies the mode for drag and drop. If the flag is true,
				dropping items will do a reparent. If it is false, dropping will
				reorder items. By default, the flag is true (parent).
				
		"""
		self.edit(dropIsParent=value)
	#----------------------------------------------------------------------
	dropIsParent = property(get_dropIsParent, set_dropIsParent)
	#----------------------------------------------------------------------
	def get_editAttrName(self):
		"""
		
				This flag specifies whether or not attribute names can be edited.
				By default double-clicking on an attribute will open the expression
				editor for that attribute.
				
		"""
		return self.query(editAttrName=True)
	#----------------------------------------------------------------------
	def set_editAttrName(self, value):
		"""
		
				This flag specifies whether or not attribute names can be edited.
				By default double-clicking on an attribute will open the expression
				editor for that attribute.
				
		"""
		self.edit(editAttrName=value)
	#----------------------------------------------------------------------
	editAttrName = property(get_editAttrName, set_editAttrName)
	#----------------------------------------------------------------------
	def expandAllItems(self,value):
		"""
		
				Expand or collapse all items in the outliner.
				
		"""
		self.edit(expandAllItems=value)
	#----------------------------------------------------------------------
	def expandAllSelectedItems(self,value):
		"""
		
				Expand or collapse all selected items in the outliner.
				
		"""
		self.edit(expandAllSelectedItems=value)
	#----------------------------------------------------------------------
	def expandAttribute(self,value):
		"""
		
				Force the outliner to fill the selection list with only attributes.
				
		"""
		self.edit(expandAttribute=value)
	#----------------------------------------------------------------------
	def get_expandConnections(self):
		"""
		
				This flag specifies whether or not attributes should be
				expanded to show their input connections.
				Note: currently the expansion will only show animCurves.
				
		"""
		return self.query(expandConnections=True)
	#----------------------------------------------------------------------
	def set_expandConnections(self, value):
		"""
		
				This flag specifies whether or not attributes should be
				expanded to show their input connections.
				Note: currently the expansion will only show animCurves.
				
		"""
		self.edit(expandConnections=value)
	#----------------------------------------------------------------------
	expandConnections = property(get_expandConnections, set_expandConnections)
	#----------------------------------------------------------------------
	def get_expandObjects(self):
		"""
		
				This flag specifies whether or not objects that are loaded
				in should be automatically expanded.
				
		"""
		return self.query(expandObjects=True)
	#----------------------------------------------------------------------
	def set_expandObjects(self, value):
		"""
		
				This flag specifies whether or not objects that are loaded
				in should be automatically expanded.
				
		"""
		self.edit(expandObjects=value)
	#----------------------------------------------------------------------
	expandObjects = property(get_expandObjects, set_expandObjects)
	#----------------------------------------------------------------------
	@property
	def feedbackItemName(self):
		"""
		
				Returns the outliner item name at the current mouse position, if any.
				
		"""
		return self.query(feedbackItemName=True)
	#----------------------------------------------------------------------
	@property
	def feedbackRowNumber(self):
		"""
		
				Returns the outliner row number at the current mouse position, if any.
				
		"""
		return self.query(feedbackRowNumber=True)
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
	@property
	def getCurrentSetOfItem(self):
		"""
		
				Returns the current set of item at the given row. As an item can belong to number of sets, current set is the set to which the item belongs to currently.
				
		"""
		return self.query(getCurrentSetOfItem=True)
	#----------------------------------------------------------------------
	def get_highlightActive(self):
		"""
		
				This flag specifies whether or not the outliner should highlight
				objects that are active.
				Note: if the outliner is driving the contents of another editor,
				setting highlightActive to true may produce unexpected behavior.
				
		"""
		return self.query(highlightActive=True)
	#----------------------------------------------------------------------
	def set_highlightActive(self, value):
		"""
		
				This flag specifies whether or not the outliner should highlight
				objects that are active.
				Note: if the outliner is driving the contents of another editor,
				setting highlightActive to true may produce unexpected behavior.
				
		"""
		self.edit(highlightActive=value)
	#----------------------------------------------------------------------
	highlightActive = property(get_highlightActive, set_highlightActive)
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
	def get_highlightSecondary(self):
		"""
		
				This flag specifies whether or not the outliner should highlight objects
				that are contained in the highlightConnection.
				
		"""
		return self.query(highlightSecondary=True)
	#----------------------------------------------------------------------
	def set_highlightSecondary(self, value):
		"""
		
				This flag specifies whether or not the outliner should highlight objects
				that are contained in the highlightConnection.
				
		"""
		self.edit(highlightSecondary=value)
	#----------------------------------------------------------------------
	highlightSecondary = property(get_highlightSecondary, set_highlightSecondary)
	#----------------------------------------------------------------------
	def get_ignoreDagHierarchy(self):
		"""
		
				This flag specifies whether or not DAG objects are displayed
				in their DAG hierarchy. Warning: using this flag without
				some other form of sensible filtering will lead to a very
				confusing outliner.
				
		"""
		return self.query(ignoreDagHierarchy=True)
	#----------------------------------------------------------------------
	def set_ignoreDagHierarchy(self, value):
		"""
		
				This flag specifies whether or not DAG objects are displayed
				in their DAG hierarchy. Warning: using this flag without
				some other form of sensible filtering will lead to a very
				confusing outliner.
				
		"""
		self.edit(ignoreDagHierarchy=value)
	#----------------------------------------------------------------------
	ignoreDagHierarchy = property(get_ignoreDagHierarchy, set_ignoreDagHierarchy)
	#----------------------------------------------------------------------
	def get_ignoreHiddenAttribute(self):
		"""
		
				Sets whether or not the outliner ignores the 'hidden in outliner' flag on nodes.
				
		"""
		return self.query(ignoreHiddenAttribute=True)
	#----------------------------------------------------------------------
	def set_ignoreHiddenAttribute(self, value):
		"""
		
				Sets whether or not the outliner ignores the 'hidden in outliner' flag on nodes.
				
		"""
		self.edit(ignoreHiddenAttribute=value)
	#----------------------------------------------------------------------
	ignoreHiddenAttribute = property(get_ignoreHiddenAttribute, set_ignoreHiddenAttribute)
	#----------------------------------------------------------------------
	def get_ignoreOutlinerColor(self):
		"""
		
				Sets whether or not the outliner ignores the 'use outliner color' flag on nodes.
				
		"""
		return self.query(ignoreOutlinerColor=True)
	#----------------------------------------------------------------------
	def set_ignoreOutlinerColor(self, value):
		"""
		
				Sets whether or not the outliner ignores the 'use outliner color' flag on nodes.
				
		"""
		self.edit(ignoreOutlinerColor=value)
	#----------------------------------------------------------------------
	ignoreOutlinerColor = property(get_ignoreOutlinerColor, set_ignoreOutlinerColor)
	#----------------------------------------------------------------------
	@property
	def isChildSelected(self):
		"""
		
				This flag allows you to query if one or more of the children of the
				specified item is selected in the outliner. The item should be
				specified using a unique DAG path. Note that if the specified item
				appears multiple times in the outliner, the result will be true if one
				or more children of any occurrence of the specified item in the
				outliner is/are selected.
				
		"""
		return self.query(isChildSelected=True)
	#----------------------------------------------------------------------
	@property
	def isSet(self):
		"""
		
				Returns true if the item present at the given row is a set.
				
		"""
		return self.query(isSet=True)
	#----------------------------------------------------------------------
	@property
	def isSetMember(self):
		"""
		
				Returns true if the item present at the given row is a set member.
				
		"""
		return self.query(isSetMember=True)
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
		
				Controls whether long or short attribute names will be used
				in the interface.  Note that this flag is ignored if the -niceNames
				flag is set.  Default is short names. Queried, returns a boolean.
				
		"""
		return self.query(longNames=True)
	#----------------------------------------------------------------------
	def set_longNames(self, value):
		"""
		
				Controls whether long or short attribute names will be used
				in the interface.  Note that this flag is ignored if the -niceNames
				flag is set.  Default is short names. Queried, returns a boolean.
				
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
	def get_mapMotionTrails(self):
		"""
		
				Sets whether or not we replace the motion trail in the outliner with the object it is trailing.
				
		"""
		return self.query(mapMotionTrails=True)
	#----------------------------------------------------------------------
	def set_mapMotionTrails(self, value):
		"""
		
				Sets whether or not we replace the motion trail in the outliner with the object it is trailing.
				
		"""
		self.edit(mapMotionTrails=value)
	#----------------------------------------------------------------------
	mapMotionTrails = property(get_mapMotionTrails, set_mapMotionTrails)
	#----------------------------------------------------------------------
	def get_masterOutliner(self):
		"""
		
				This flag is the name of an outliner that this outliner will share the objects
				and state from. When an outliner is shared, all of its state information
				comes from, and is applied to, the master outliner.
				
		"""
		return self.query(masterOutliner=True)
	#----------------------------------------------------------------------
	def set_masterOutliner(self, value):
		"""
		
				This flag is the name of an outliner that this outliner will share the objects
				and state from. When an outliner is shared, all of its state information
				comes from, and is applied to, the master outliner.
				
		"""
		self.edit(masterOutliner=value)
	#----------------------------------------------------------------------
	masterOutliner = property(get_masterOutliner, set_masterOutliner)
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
	def object(self):
		"""
		
				This flags is used together with the parentObject flag to get
				the name of the parent object for the specified object.
				
		"""
		return self.query(object=True)
	#----------------------------------------------------------------------
	def get_organizeByClip(self):
		"""
		
				If true then when a node with Time Editor clips is displayed, attributes
				will be displayed according to the clip(s) it belongs to.
				eg:
				
				Clip1
				Attr1
				Attr2
				Clip2
				Attr1
				
				If it is false then the outliner will be organized primarily by attributes.
				eg:
				
				Attr1
				Clip1
				Clip2
				Attr2
				Clip1
				
		"""
		return self.query(organizeByClip=True)
	#----------------------------------------------------------------------
	def set_organizeByClip(self, value):
		"""
		
				If true then when a node with Time Editor clips is displayed, attributes
				will be displayed according to the clip(s) it belongs to.
				eg:
				
				Clip1
				Attr1
				Attr2
				Clip2
				Attr1
				
				If it is false then the outliner will be organized primarily by attributes.
				eg:
				
				Attr1
				Clip1
				Clip2
				Attr2
				Clip1
				
		"""
		self.edit(organizeByClip=value)
	#----------------------------------------------------------------------
	organizeByClip = property(get_organizeByClip, set_organizeByClip)
	#----------------------------------------------------------------------
	def get_organizeByLayer(self):
		"""
		
				If true then when a node with animation layer is displayed, attributes
				will be displayed according to the layer(s) it belongs to.
				eg:
				
				Layer1
				Attr1
				Attr2
				Layer2
				Attr1
				
				If it is false then the outliner will be organized primarily by attributes.
				eg:
				
				Attr1
				Layer1
				Layer2
				Attr2
				Layer1
				
		"""
		return self.query(organizeByLayer=True)
	#----------------------------------------------------------------------
	def set_organizeByLayer(self, value):
		"""
		
				If true then when a node with animation layer is displayed, attributes
				will be displayed according to the layer(s) it belongs to.
				eg:
				
				Layer1
				Attr1
				Attr2
				Layer2
				Attr1
				
				If it is false then the outliner will be organized primarily by attributes.
				eg:
				
				Attr1
				Layer1
				Layer2
				Attr2
				Layer1
				
		"""
		self.edit(organizeByLayer=value)
	#----------------------------------------------------------------------
	organizeByLayer = property(get_organizeByLayer, set_organizeByLayer)
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
	@property
	def parentObject(self):
		""""""
		return self.query(parentObject=True)
	#----------------------------------------------------------------------
	def get_pinPlug(self):
		"""
		
				Pins the named plug, so it always appears in the outliner, irrespective
				of the incoming selection connection.
				In query mode, returns a list of the pinned plugs.
				
		"""
		return self.query(pinPlug=True)
	#----------------------------------------------------------------------
	def set_pinPlug(self, value):
		"""
		
				Pins the named plug, so it always appears in the outliner, irrespective
				of the incoming selection connection.
				In query mode, returns a list of the pinned plugs.
				
		"""
		self.edit(pinPlug=value)
	#----------------------------------------------------------------------
	pinPlug = property(get_pinPlug, set_pinPlug)
	#----------------------------------------------------------------------
	def refresh(self,value):
		"""
		
				Causes the outliner to refresh itself.
				
		"""
		self.edit(refresh=value)
	#----------------------------------------------------------------------
	def removeFromCurrentSet(self,value):
		"""
		
				Removes selected members of a set from their current set. Current set is the set to which item at the given row belongs to.
				If no selected items, the item at the given row is removed from its current set.
				
		"""
		self.edit(removeFromCurrentSet=value)
	#----------------------------------------------------------------------
	def renameItem(self,value):
		"""
		
				Renames the item at the given row index in the outliner.
				
		"""
		self.edit(renameItem=value)
	#----------------------------------------------------------------------
	def renameSelectedItem(self,value):
		"""
		
				Rename the first selected item in the outliner.
				
		"""
		self.edit(renameSelectedItem=value)
	#----------------------------------------------------------------------
	@property
	def renderFilterActive(self):
		"""
		
				This is a query only flag which returns true if the render setup filter is Active, i.e one of the four render filters (Inside Selected, Outside Selected, Inside All Layers, Outside All Layers)
				is applied on the outliner currently, false otherwise.
				
		"""
		return self.query(renderFilterActive=True)
	#----------------------------------------------------------------------
	def get_renderFilterIndex(self):
		"""
		
				Sets the Render Setup Filter to the index passed. This only works if the filter is visible in outliner and its selection is not locked.
				Valid indices are:
				
				0 - Scene
				2 - Inside Selected
				3 - Outside Selected
				4 - Inside All Layers
				5 - Outside All Layers
				
				Default: Scene  0
				In query mode returns current index of the filter.
				
		"""
		return self.query(renderFilterIndex=True)
	#----------------------------------------------------------------------
	def set_renderFilterIndex(self, value):
		"""
		
				Sets the Render Setup Filter to the index passed. This only works if the filter is visible in outliner and its selection is not locked.
				Valid indices are:
				
				0 - Scene
				2 - Inside Selected
				3 - Outside Selected
				4 - Inside All Layers
				5 - Outside All Layers
				
				Default: Scene  0
				In query mode returns current index of the filter.
				
		"""
		self.edit(renderFilterIndex=value)
	#----------------------------------------------------------------------
	renderFilterIndex = property(get_renderFilterIndex, set_renderFilterIndex)
	#----------------------------------------------------------------------
	def get_renderFilterVisible(self):
		"""
		
				Show/Hide the Render Setup Filter in outliner. In query mode returns whether the Render Setup Filter is visible or not.
				
		"""
		return self.query(renderFilterVisible=True)
	#----------------------------------------------------------------------
	def set_renderFilterVisible(self, value):
		"""
		
				Show/Hide the Render Setup Filter in outliner. In query mode returns whether the Render Setup Filter is visible or not.
				
		"""
		self.edit(renderFilterVisible=value)
	#----------------------------------------------------------------------
	renderFilterVisible = property(get_renderFilterVisible, set_renderFilterVisible)
	#----------------------------------------------------------------------
	def get_selectCommand(self):
		"""
		
				A command to be executed when an item is selected.
				
		"""
		return self.query(selectCommand=True)
	#----------------------------------------------------------------------
	def set_selectCommand(self, value):
		"""
		
				A command to be executed when an item is selected.
				
		"""
		self.edit(selectCommand=value)
	#----------------------------------------------------------------------
	selectCommand = property(get_selectCommand, set_selectCommand)
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
	def selectionOrder(self,value):
		"""
		
				Specify how objects are sorted in selection list. Current recognised values
				are "chronological" for sorting in selection order and "display" to sort objects in the same order that the outliner does.
				
		"""
		self.edit(selectionOrder=value)
	#----------------------------------------------------------------------
	def get_setFilter(self):
		"""
		
				Specifies the name of a filter which is used to filter
				which (if any) sets to display.
				
		"""
		return self.query(setFilter=True)
	#----------------------------------------------------------------------
	def set_setFilter(self, value):
		"""
		
				Specifies the name of a filter which is used to filter
				which (if any) sets to display.
				
		"""
		self.edit(setFilter=value)
	#----------------------------------------------------------------------
	setFilter = property(get_setFilter, set_setFilter)
	#----------------------------------------------------------------------
	def get_setsIgnoreFilters(self):
		"""
		
				This flag specifies whether or not the filter should be ignored
				for expanding sets to show set members (default is true).
				
		"""
		return self.query(setsIgnoreFilters=True)
	#----------------------------------------------------------------------
	def set_setsIgnoreFilters(self, value):
		"""
		
				This flag specifies whether or not the filter should be ignored
				for expanding sets to show set members (default is true).
				
		"""
		self.edit(setsIgnoreFilters=value)
	#----------------------------------------------------------------------
	setsIgnoreFilters = property(get_setsIgnoreFilters, set_setsIgnoreFilters)
	#----------------------------------------------------------------------
	def get_showAnimCurvesOnly(self):
		"""
		
				This flag modifies the showConnected flag.  If showConnected
				is set to true then this flag will cause display of only
				those attributes that are connected to an animCurve. If
				showConnected is set to false then this flag does nothing.
				
		"""
		return self.query(showAnimCurvesOnly=True)
	#----------------------------------------------------------------------
	def set_showAnimCurvesOnly(self, value):
		"""
		
				This flag modifies the showConnected flag.  If showConnected
				is set to true then this flag will cause display of only
				those attributes that are connected to an animCurve. If
				showConnected is set to false then this flag does nothing.
				
		"""
		self.edit(showAnimCurvesOnly=value)
	#----------------------------------------------------------------------
	showAnimCurvesOnly = property(get_showAnimCurvesOnly, set_showAnimCurvesOnly)
	#----------------------------------------------------------------------
	def get_showAnimLayerWeight(self):
		"""
		
				If true then when a node with animation layer is displayed, the
				weight of the layer will be displayed if it is keyed.
				
		"""
		return self.query(showAnimLayerWeight=True)
	#----------------------------------------------------------------------
	def set_showAnimLayerWeight(self, value):
		"""
		
				If true then when a node with animation layer is displayed, the
				weight of the layer will be displayed if it is keyed.
				
		"""
		self.edit(showAnimLayerWeight=value)
	#----------------------------------------------------------------------
	showAnimLayerWeight = property(get_showAnimLayerWeight, set_showAnimLayerWeight)
	#----------------------------------------------------------------------
	def get_showAssets(self):
		"""
		
				This flags specifies whether assets should be shown in the outliner.
				
		"""
		return self.query(showAssets=True)
	#----------------------------------------------------------------------
	def set_showAssets(self, value):
		"""
		
				This flags specifies whether assets should be shown in the outliner.
				
		"""
		self.edit(showAssets=value)
	#----------------------------------------------------------------------
	showAssets = property(get_showAssets, set_showAssets)
	#----------------------------------------------------------------------
	def get_showAssignedMaterials(self):
		"""
		
				Specifies whether to show assigned materials under shapes.
				
		"""
		return self.query(showAssignedMaterials=True)
	#----------------------------------------------------------------------
	def set_showAssignedMaterials(self, value):
		"""
		
				Specifies whether to show assigned materials under shapes.
				
		"""
		self.edit(showAssignedMaterials=value)
	#----------------------------------------------------------------------
	showAssignedMaterials = property(get_showAssignedMaterials, set_showAssignedMaterials)
	#----------------------------------------------------------------------
	def get_showAttrValues(self):
		"""
		
				This flag specifies whether attribute values or attribute names should
				be displayed.
				Note: currently only string attributes can have their values displayed.
				
		"""
		return self.query(showAttrValues=True)
	#----------------------------------------------------------------------
	def set_showAttrValues(self, value):
		"""
		
				This flag specifies whether attribute values or attribute names should
				be displayed.
				Note: currently only string attributes can have their values displayed.
				
		"""
		self.edit(showAttrValues=value)
	#----------------------------------------------------------------------
	showAttrValues = property(get_showAttrValues, set_showAttrValues)
	#----------------------------------------------------------------------
	def get_showAttributes(self):
		"""
		
				Specifies whether to show attributes or not.
				
		"""
		return self.query(showAttributes=True)
	#----------------------------------------------------------------------
	def set_showAttributes(self, value):
		"""
		
				Specifies whether to show attributes or not.
				
		"""
		self.edit(showAttributes=value)
	#----------------------------------------------------------------------
	showAttributes = property(get_showAttributes, set_showAttributes)
	#----------------------------------------------------------------------
	def get_showCompounds(self):
		"""
		
				This flag specifies whether or not compound attributes should be
				displayed, or just the leaf attributes.
				Note: if showConnected is true, and the compound attribute
				is connected, it will still be displayed.
				
		"""
		return self.query(showCompounds=True)
	#----------------------------------------------------------------------
	def set_showCompounds(self, value):
		"""
		
				This flag specifies whether or not compound attributes should be
				displayed, or just the leaf attributes.
				Note: if showConnected is true, and the compound attribute
				is connected, it will still be displayed.
				
		"""
		self.edit(showCompounds=value)
	#----------------------------------------------------------------------
	showCompounds = property(get_showCompounds, set_showCompounds)
	#----------------------------------------------------------------------
	def get_showConnected(self):
		"""
		
				This flag modifies the showAttributes flag.  If showAttributes
				is set to true then this flag will cause display of only
				those attributes that are connected in the dependency graph.
				If showAttributes is set to false then this flag does nothing.
				
		"""
		return self.query(showConnected=True)
	#----------------------------------------------------------------------
	def set_showConnected(self, value):
		"""
		
				This flag modifies the showAttributes flag.  If showAttributes
				is set to true then this flag will cause display of only
				those attributes that are connected in the dependency graph.
				If showAttributes is set to false then this flag does nothing.
				
		"""
		self.edit(showConnected=value)
	#----------------------------------------------------------------------
	showConnected = property(get_showConnected, set_showConnected)
	#----------------------------------------------------------------------
	def get_showContainedOnly(self):
		"""
		
				This flags specifies whether nodes belonging to containers should be show
				under the container node only. Otherwise, it will show up under the world
				as well.
				
		"""
		return self.query(showContainedOnly=True)
	#----------------------------------------------------------------------
	def set_showContainedOnly(self, value):
		"""
		
				This flags specifies whether nodes belonging to containers should be show
				under the container node only. Otherwise, it will show up under the world
				as well.
				
		"""
		self.edit(showContainedOnly=value)
	#----------------------------------------------------------------------
	showContainedOnly = property(get_showContainedOnly, set_showContainedOnly)
	#----------------------------------------------------------------------
	def get_showContainerContents(self):
		"""
		
				This flags specifies whether the contents of the container should be
				shown under the container node in the outliner.
				
		"""
		return self.query(showContainerContents=True)
	#----------------------------------------------------------------------
	def set_showContainerContents(self, value):
		"""
		
				This flags specifies whether the contents of the container should be
				shown under the container node in the outliner.
				
		"""
		self.edit(showContainerContents=value)
	#----------------------------------------------------------------------
	showContainerContents = property(get_showContainerContents, set_showContainerContents)
	#----------------------------------------------------------------------
	def get_showDagOnly(self):
		"""
		
				This flag specifies whether all dependency graph objects will
				be displayed, or just DAG objects.
				
		"""
		return self.query(showDagOnly=True)
	#----------------------------------------------------------------------
	def set_showDagOnly(self, value):
		"""
		
				This flag specifies whether all dependency graph objects will
				be displayed, or just DAG objects.
				
		"""
		self.edit(showDagOnly=value)
	#----------------------------------------------------------------------
	showDagOnly = property(get_showDagOnly, set_showDagOnly)
	#----------------------------------------------------------------------
	def get_showLeafs(self):
		"""
		
				This flag specifies whether or not leaf attributes should be
				displayed, or just the compound attributes.
				Note: if showConnected is true, and the leaf attribute
				is connected, it will still be displayed.
				
		"""
		return self.query(showLeafs=True)
	#----------------------------------------------------------------------
	def set_showLeafs(self, value):
		"""
		
				This flag specifies whether or not leaf attributes should be
				displayed, or just the compound attributes.
				Note: if showConnected is true, and the leaf attribute
				is connected, it will still be displayed.
				
		"""
		self.edit(showLeafs=value)
	#----------------------------------------------------------------------
	showLeafs = property(get_showLeafs, set_showLeafs)
	#----------------------------------------------------------------------
	def get_showMuteInfo(self):
		"""
		
				This flag specifies whether mute information will be displayed
				
		"""
		return self.query(showMuteInfo=True)
	#----------------------------------------------------------------------
	def set_showMuteInfo(self, value):
		"""
		
				This flag specifies whether mute information will be displayed
				
		"""
		self.edit(showMuteInfo=value)
	#----------------------------------------------------------------------
	showMuteInfo = property(get_showMuteInfo, set_showMuteInfo)
	#----------------------------------------------------------------------
	def get_showNamespace(self):
		"""
		
				This flag specifies whether all objects will have their
				namespace displayed, if namespace different than root.
				
		"""
		return self.query(showNamespace=True)
	#----------------------------------------------------------------------
	def set_showNamespace(self, value):
		"""
		
				This flag specifies whether all objects will have their
				namespace displayed, if namespace different than root.
				
		"""
		self.edit(showNamespace=value)
	#----------------------------------------------------------------------
	showNamespace = property(get_showNamespace, set_showNamespace)
	#----------------------------------------------------------------------
	def get_showNumericAttrsOnly(self):
		"""
		
				This flag specifies whether or not all attributes should be
				displayed, or just numeric attributes.
				Note: if showConnected is true, and the attribute
				is connected, it will still be displayed.
				
		"""
		return self.query(showNumericAttrsOnly=True)
	#----------------------------------------------------------------------
	def set_showNumericAttrsOnly(self, value):
		"""
		
				This flag specifies whether or not all attributes should be
				displayed, or just numeric attributes.
				Note: if showConnected is true, and the attribute
				is connected, it will still be displayed.
				
		"""
		self.edit(showNumericAttrsOnly=value)
	#----------------------------------------------------------------------
	showNumericAttrsOnly = property(get_showNumericAttrsOnly, set_showNumericAttrsOnly)
	#----------------------------------------------------------------------
	def get_showParentContainers(self):
		"""
		
				This flags specifies whether nodes belonging to containers/assets should show their
				containers/assets as well in its outliner.
				
		"""
		return self.query(showParentContainers=True)
	#----------------------------------------------------------------------
	def set_showParentContainers(self, value):
		"""
		
				This flags specifies whether nodes belonging to containers/assets should show their
				containers/assets as well in its outliner.
				
		"""
		self.edit(showParentContainers=value)
	#----------------------------------------------------------------------
	showParentContainers = property(get_showParentContainers, set_showParentContainers)
	#----------------------------------------------------------------------
	def get_showPinIcons(self):
		"""
		
				Sets whether pin icons are shown for unpinned plugs.
				
		"""
		return self.query(showPinIcons=True)
	#----------------------------------------------------------------------
	def set_showPinIcons(self, value):
		"""
		
				Sets whether pin icons are shown for unpinned plugs.
				
		"""
		self.edit(showPinIcons=value)
	#----------------------------------------------------------------------
	showPinIcons = property(get_showPinIcons, set_showPinIcons)
	#----------------------------------------------------------------------
	def get_showPublishedAsConnected(self):
		"""
		
				This flags enables attributes that are published to be displayed in italics.
				Otherwise, only attributes connected as a destination are shown in italics.
				
		"""
		return self.query(showPublishedAsConnected=True)
	#----------------------------------------------------------------------
	def set_showPublishedAsConnected(self, value):
		"""
		
				This flags enables attributes that are published to be displayed in italics.
				Otherwise, only attributes connected as a destination are shown in italics.
				
		"""
		self.edit(showPublishedAsConnected=value)
	#----------------------------------------------------------------------
	showPublishedAsConnected = property(get_showPublishedAsConnected, set_showPublishedAsConnected)
	#----------------------------------------------------------------------
	def get_showReferenceMembers(self):
		"""
		
				Specifies whether to show reference node members under the reference node in the outliner.
				
		"""
		return self.query(showReferenceMembers=True)
	#----------------------------------------------------------------------
	def set_showReferenceMembers(self, value):
		"""
		
				Specifies whether to show reference node members under the reference node in the outliner.
				
		"""
		self.edit(showReferenceMembers=value)
	#----------------------------------------------------------------------
	showReferenceMembers = property(get_showReferenceMembers, set_showReferenceMembers)
	#----------------------------------------------------------------------
	def get_showReferenceNodes(self):
		"""
		
				Specifies whether to show reference nodes or not.
				
		"""
		return self.query(showReferenceNodes=True)
	#----------------------------------------------------------------------
	def set_showReferenceNodes(self, value):
		"""
		
				Specifies whether to show reference nodes or not.
				
		"""
		self.edit(showReferenceNodes=value)
	#----------------------------------------------------------------------
	showReferenceNodes = property(get_showReferenceNodes, set_showReferenceNodes)
	#----------------------------------------------------------------------
	def showSelected(self,value):
		"""
		
				If true then the selected items are expanded in the outliner.
				
		"""
		self.edit(showSelected=value)
	#----------------------------------------------------------------------
	def get_showSetMembers(self):
		"""
		
				If true then when a set is expanded, the set members
				will be displayed. If false, then only other sets will be
				displayed.
				
		"""
		return self.query(showSetMembers=True)
	#----------------------------------------------------------------------
	def set_showSetMembers(self, value):
		"""
		
				If true then when a set is expanded, the set members
				will be displayed. If false, then only other sets will be
				displayed.
				
		"""
		self.edit(showSetMembers=value)
	#----------------------------------------------------------------------
	showSetMembers = property(get_showSetMembers, set_showSetMembers)
	#----------------------------------------------------------------------
	def get_showShapes(self):
		"""
		
				Specifies whether to show shapes or not.
				
		"""
		return self.query(showShapes=True)
	#----------------------------------------------------------------------
	def set_showShapes(self, value):
		"""
		
				Specifies whether to show shapes or not.
				
		"""
		self.edit(showShapes=value)
	#----------------------------------------------------------------------
	showShapes = property(get_showShapes, set_showShapes)
	#----------------------------------------------------------------------
	def get_showTextureNodesOnly(self):
		"""
		
				This flag modifies the showConnected flag. If showConnected is set to true then
				this flag will cause display of only those attributes that are connected to a
				texture node. If showConnected is set to false then this flag does nothing.
				
		"""
		return self.query(showTextureNodesOnly=True)
	#----------------------------------------------------------------------
	def set_showTextureNodesOnly(self, value):
		"""
		
				This flag modifies the showConnected flag. If showConnected is set to true then
				this flag will cause display of only those attributes that are connected to a
				texture node. If showConnected is set to false then this flag does nothing.
				
		"""
		self.edit(showTextureNodesOnly=value)
	#----------------------------------------------------------------------
	showTextureNodesOnly = property(get_showTextureNodesOnly, set_showTextureNodesOnly)
	#----------------------------------------------------------------------
	def get_showTimeEditor(self):
		"""
		
				If true, all nodes related to the Time Editor will be
				shown as a hierarchy.
				
		"""
		return self.query(showTimeEditor=True)
	#----------------------------------------------------------------------
	def set_showTimeEditor(self, value):
		"""
		
				If true, all nodes related to the Time Editor will be
				shown as a hierarchy.
				
		"""
		self.edit(showTimeEditor=value)
	#----------------------------------------------------------------------
	showTimeEditor = property(get_showTimeEditor, set_showTimeEditor)
	#----------------------------------------------------------------------
	def get_showUVAttrsOnly(self):
		"""
		
				This flag specifies whether or not all attributes should be displayed, or
				just uv attributes.
				Note: currently the only attribute which will be
				displayed is Shape.uvSet.uvSetName.
				
		"""
		return self.query(showUVAttrsOnly=True)
	#----------------------------------------------------------------------
	def set_showUVAttrsOnly(self, value):
		"""
		
				This flag specifies whether or not all attributes should be displayed, or
				just uv attributes.
				Note: currently the only attribute which will be
				displayed is Shape.uvSet.uvSetName.
				
		"""
		self.edit(showUVAttrsOnly=value)
	#----------------------------------------------------------------------
	showUVAttrsOnly = property(get_showUVAttrsOnly, set_showUVAttrsOnly)
	#----------------------------------------------------------------------
	def get_showUnitlessCurves(self):
		"""
		
				This flag (in combination with -expandConnections) specifies
				whether or not connection expansion should show unitless
				animCurves.
				
		"""
		return self.query(showUnitlessCurves=True)
	#----------------------------------------------------------------------
	def set_showUnitlessCurves(self, value):
		"""
		
				This flag (in combination with -expandConnections) specifies
				whether or not connection expansion should show unitless
				animCurves.
				
		"""
		self.edit(showUnitlessCurves=value)
	#----------------------------------------------------------------------
	showUnitlessCurves = property(get_showUnitlessCurves, set_showUnitlessCurves)
	#----------------------------------------------------------------------
	def get_showUpstreamCurves(self):
		"""
		
				Specifies exactly which attributes are displayed when showAttributes
				and expandConnections are both true.
				If true, the dependency graph is searched upstream for all curves
				that drive the selected plugs (showing multiple curves for example
				in a typical driven key setup, where first the driven key curve is
				encountered, followed by the actual animation curve that drives the
				source object). If false, only the first curves encountered
				will be shown. Note that, even if false, multiple curves can be shown
				if e.g. a blendWeighted node is being used to combine multiple curves.
				
		"""
		return self.query(showUpstreamCurves=True)
	#----------------------------------------------------------------------
	def set_showUpstreamCurves(self, value):
		"""
		
				Specifies exactly which attributes are displayed when showAttributes
				and expandConnections are both true.
				If true, the dependency graph is searched upstream for all curves
				that drive the selected plugs (showing multiple curves for example
				in a typical driven key setup, where first the driven key curve is
				encountered, followed by the actual animation curve that drives the
				source object). If false, only the first curves encountered
				will be shown. Note that, even if false, multiple curves can be shown
				if e.g. a blendWeighted node is being used to combine multiple curves.
				
		"""
		self.edit(showUpstreamCurves=value)
	#----------------------------------------------------------------------
	showUpstreamCurves = property(get_showUpstreamCurves, set_showUpstreamCurves)
	#----------------------------------------------------------------------
	def get_sortOrder(self):
		"""
		
				Specify how objects are to be sorted.  Current recognised values
				are "none" for no sorting and "dagName" to sort DAG objects by name.
				Notes: a) non-DAG objects are always sorted by nodeType and name.
				b) when sortOrder is set to "dagName", objects cannot be reordered
				using drag-and-drop, they can however be reparented.
				
		"""
		return self.query(sortOrder=True)
	#----------------------------------------------------------------------
	def set_sortOrder(self, value):
		"""
		
				Specify how objects are to be sorted.  Current recognised values
				are "none" for no sorting and "dagName" to sort DAG objects by name.
				Notes: a) non-DAG objects are always sorted by nodeType and name.
				b) when sortOrder is set to "dagName", objects cannot be reordered
				using drag-and-drop, they can however be reparented.
				
		"""
		self.edit(sortOrder=value)
	#----------------------------------------------------------------------
	sortOrder = property(get_sortOrder, set_sortOrder)
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
	def get_transmitFilters(self):
		"""
		
				This flag specifies how the selectionConnection is populated
				when attribute filters are enabled.  If this flag is set to
				true, then all the attributes that pass the filter will be
				placed on the selectionConnection.  By default this flag is
				false.
				
		"""
		return self.query(transmitFilters=True)
	#----------------------------------------------------------------------
	def set_transmitFilters(self, value):
		"""
		
				This flag specifies how the selectionConnection is populated
				when attribute filters are enabled.  If this flag is set to
				true, then all the attributes that pass the filter will be
				placed on the selectionConnection.  By default this flag is
				false.
				
		"""
		self.edit(transmitFilters=value)
	#----------------------------------------------------------------------
	transmitFilters = property(get_transmitFilters, set_transmitFilters)
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
	def unpinPlug(self,value):
		"""
		
				Unpins the named plug.
				
		"""
		self.edit(unpinPlug=value)
	#----------------------------------------------------------------------
	def updateMainConnection(self,value):
		"""
		
				Causes a locked mainConnection to be updated from the orginal
				mainConnection, but preserves the lock state.
				
		"""
		self.edit(updateMainConnection=value)