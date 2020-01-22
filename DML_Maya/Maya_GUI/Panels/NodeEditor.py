

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class NodeEditor(UI_Object.UI):
	"""
	This command creates/edits/queries a nodeEditor editor.
	The optional argument is the name of the control.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.nodeEditor(**kwargs)
			super(NodeEditor, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.nodeEditor(name, exists=True):
				super(NodeEditor, self).__init__(name)
			else:
				name = cmds.nodeEditor(name, **kwargs)
				super(NodeEditor, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def get_activeTab(self):
		"""
		
				Gets/sets the index of the tab widget's (active) visible tab. Note: the index is
				zero-based.
				
		"""
		return self.query(activeTab=True)
	#----------------------------------------------------------------------
	def set_activeTab(self, value):
		"""
		
				Gets/sets the index of the tab widget's (active) visible tab. Note: the index is
				zero-based.
				
		"""
		self.edit(activeTab=value)
	#----------------------------------------------------------------------
	activeTab = property(get_activeTab, set_activeTab)
	#----------------------------------------------------------------------
	def get_addNewNodes(self):
		"""
		
				New nodes should be added to the graph, default is on.
				
		"""
		return self.query(addNewNodes=True)
	#----------------------------------------------------------------------
	def set_addNewNodes(self, value):
		"""
		
				New nodes should be added to the graph, default is on.
				
		"""
		self.edit(addNewNodes=value)
	#----------------------------------------------------------------------
	addNewNodes = property(get_addNewNodes, set_addNewNodes)
	#----------------------------------------------------------------------
	def addNode(self,value):
		"""
		
				Adds a specified node to the graph. Passing an empty string means the current model
				selection will be added to the graph.
				
		"""
		self.edit(addNode=value)
	#----------------------------------------------------------------------
	def get_additiveGraphingMode(self):
		"""
		
				When enabled, the graphing will add node networks to the existing graph instead of replacing it.
				
		"""
		return self.query(additiveGraphingMode=True)
	#----------------------------------------------------------------------
	def set_additiveGraphingMode(self, value):
		"""
		
				When enabled, the graphing will add node networks to the existing graph instead of replacing it.
				
		"""
		self.edit(additiveGraphingMode=value)
	#----------------------------------------------------------------------
	additiveGraphingMode = property(get_additiveGraphingMode, set_additiveGraphingMode)
	#----------------------------------------------------------------------
	def get_allAttributes(self):
		"""
		
				Attributes should not be filtered out of the graph, default is off.
				
		"""
		return self.query(allAttributes=True)
	#----------------------------------------------------------------------
	def set_allAttributes(self, value):
		"""
		
				Attributes should not be filtered out of the graph, default is off.
				
		"""
		self.edit(allAttributes=value)
	#----------------------------------------------------------------------
	allAttributes = property(get_allAttributes, set_allAttributes)
	#----------------------------------------------------------------------
	def get_allNodes(self):
		"""
		
				Nodes should not be filtered out of the graph, default is off.
				
		"""
		return self.query(allNodes=True)
	#----------------------------------------------------------------------
	def set_allNodes(self, value):
		"""
		
				Nodes should not be filtered out of the graph, default is off.
				
		"""
		self.edit(allNodes=value)
	#----------------------------------------------------------------------
	allNodes = property(get_allNodes, set_allNodes)
	#----------------------------------------------------------------------
	@property
	def allowNewTabs(self):
		"""
		
				Query only. Returns whether this Node Editor is allowed to have new tabs added,
				either by creating a new tab or duplicating an existing one.
				
		"""
		return self.query(allowNewTabs=True)
	#----------------------------------------------------------------------
	def allowTabTearoff(self,value):
		"""
		
				Control whether or not the tabs can be torn off and floated.
				Defaults to true.
				
		"""
		self.edit(allowTabTearoff=value)
	#----------------------------------------------------------------------
	def get_autoSizeNodes(self):
		"""
		
				When enabled, default node widths will be dynamically determined by the node name length, default is on.
				
		"""
		return self.query(autoSizeNodes=True)
	#----------------------------------------------------------------------
	def set_autoSizeNodes(self, value):
		"""
		
				When enabled, default node widths will be dynamically determined by the node name length, default is on.
				
		"""
		self.edit(autoSizeNodes=value)
	#----------------------------------------------------------------------
	autoSizeNodes = property(get_autoSizeNodes, set_autoSizeNodes)
	#----------------------------------------------------------------------
	def beginCreateNode(self,value):
		"""
		
				Begin interactive node-creation at the mouse position. This will create
				a control which allows quick creation of a node in the editor.
				The actual creation is delegated to the createNodeCommand.
				
		"""
		self.edit(beginCreateNode=value)
	#----------------------------------------------------------------------
	def beginNewConnection(self,value):
		"""
		
				Begin a new interactive connection at the given attribute.
				
		"""
		self.edit(beginNewConnection=value)
	#----------------------------------------------------------------------
	def breakSelectedConnections(self,value):
		"""
		
				Break the selected attribute connections.
				
		"""
		self.edit(breakSelectedConnections=value)
	#----------------------------------------------------------------------
	def closeAllTabs(self,value):
		"""
		
				Close all tabs on the tab widget.
				
		"""
		self.edit(closeAllTabs=value)
	#----------------------------------------------------------------------
	def closeTab(self,value):
		"""
		
				Closes the tab on the tab widget at the specified index. Note: using this flag
				on a torn-off tab will close the node editor since there can be only a single tab.
				In this case the index argument is ignored.
				
		"""
		self.edit(closeTab=value)
	#----------------------------------------------------------------------
	def connectSelectedNodes(self,value):
		"""
		
				Creates a connection between all selected nodes in the editor. The default output
				port of one node is connected to the default input port of the next node in the
				selection order.
				
		"""
		self.edit(connectSelectedNodes=value)
	#----------------------------------------------------------------------
	def get_connectionMinSegment(self):
		"""
		
				Sets the minimum segment length ratio of the connection leaving an output port.
				Applies to "straight", "corner" and "s-shape" connection styles.
				Value must be between 0.0 and 1.0.
				
		"""
		return self.query(connectionMinSegment=True)
	#----------------------------------------------------------------------
	def set_connectionMinSegment(self, value):
		"""
		
				Sets the minimum segment length ratio of the connection leaving an output port.
				Applies to "straight", "corner" and "s-shape" connection styles.
				Value must be between 0.0 and 1.0.
				
		"""
		self.edit(connectionMinSegment=value)
	#----------------------------------------------------------------------
	connectionMinSegment = property(get_connectionMinSegment, set_connectionMinSegment)
	#----------------------------------------------------------------------
	def get_connectionOffset(self):
		"""
		
				Sets the offset length for each connection edges.
				Applies to "corner" and "s-shape" connection styles.
				Value must be between 0.0 and 1.0.
				
		"""
		return self.query(connectionOffset=True)
	#----------------------------------------------------------------------
	def set_connectionOffset(self, value):
		"""
		
				Sets the offset length for each connection edges.
				Applies to "corner" and "s-shape" connection styles.
				Value must be between 0.0 and 1.0.
				
		"""
		self.edit(connectionOffset=value)
	#----------------------------------------------------------------------
	connectionOffset = property(get_connectionOffset, set_connectionOffset)
	#----------------------------------------------------------------------
	def get_connectionRoundness(self):
		"""
		
				Sets the roundness factor for each connection edges.
				Applies only to "s-shape" connection style.
				Value must be between 0.5 and 1.0.
				
		"""
		return self.query(connectionRoundness=True)
	#----------------------------------------------------------------------
	def set_connectionRoundness(self, value):
		"""
		
				Sets the roundness factor for each connection edges.
				Applies only to "s-shape" connection style.
				Value must be between 0.5 and 1.0.
				
		"""
		self.edit(connectionRoundness=value)
	#----------------------------------------------------------------------
	connectionRoundness = property(get_connectionRoundness, set_connectionRoundness)
	#----------------------------------------------------------------------
	def get_connectionStyle(self):
		"""
		
				Sets how the connection between nodes are drawn.
				Mode values are: "bezier", "straight", "corner" and "s-shape".
				In query mode, returns current connection style.
				
		"""
		return self.query(connectionStyle=True)
	#----------------------------------------------------------------------
	def set_connectionStyle(self, value):
		"""
		
				Sets how the connection between nodes are drawn.
				Mode values are: "bezier", "straight", "corner" and "s-shape".
				In query mode, returns current connection style.
				
		"""
		self.edit(connectionStyle=value)
	#----------------------------------------------------------------------
	connectionStyle = property(get_connectionStyle, set_connectionStyle)
	#----------------------------------------------------------------------
	def get_connectionTension(self):
		"""
		
				Sets where the vertical line should be drawn on connection edge, 0 being in the middle.
				Applies to "corner" and "s-shape" connection styles.
				Value must be between -100 and 100.
				
		"""
		return self.query(connectionTension=True)
	#----------------------------------------------------------------------
	def set_connectionTension(self, value):
		"""
		
				Sets where the vertical line should be drawn on connection edge, 0 being in the middle.
				Applies to "corner" and "s-shape" connection styles.
				Value must be between -100 and 100.
				
		"""
		self.edit(connectionTension=value)
	#----------------------------------------------------------------------
	connectionTension = property(get_connectionTension, set_connectionTension)
	#----------------------------------------------------------------------
	def get_consistentNameSize(self):
		"""
		
				When enabled, the size of the node name will consistently match the current zoom
				level. When disabled, the node name size will remain the same after zooming out
				past a certain level. Default is on.
				
		"""
		return self.query(consistentNameSize=True)
	#----------------------------------------------------------------------
	def set_consistentNameSize(self, value):
		"""
		
				When enabled, the size of the node name will consistently match the current zoom
				level. When disabled, the node name size will remain the same after zooming out
				past a certain level. Default is on.
				
		"""
		self.edit(consistentNameSize=value)
	#----------------------------------------------------------------------
	consistentNameSize = property(get_consistentNameSize, set_consistentNameSize)
	#----------------------------------------------------------------------
	def get_contentsChangedCommand(self):
		"""
		
				Specifies a function to be called whenever the contents of the node editor changes.
				
		"""
		return self.query(contentsChangedCommand=True)
	#----------------------------------------------------------------------
	def set_contentsChangedCommand(self, value):
		"""
		
				Specifies a function to be called whenever the contents of the node editor changes.
				
		"""
		self.edit(contentsChangedCommand=value)
	#----------------------------------------------------------------------
	contentsChangedCommand = property(get_contentsChangedCommand, set_contentsChangedCommand)
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
	def createInfo(self,value):
		"""
		
				Creates or modifies a hyperGraphInfo network to save the state of the editor.
				
		"""
		self.edit(createInfo=value)
	#----------------------------------------------------------------------
	def get_createNodeCommand(self):
		"""
		
				Specifies a function to be used to create nodes through the editor. The function will
				be passed the name of the chosen node type. This is used by the tab-create workflow.
				By default createNode is used.
				
		"""
		return self.query(createNodeCommand=True)
	#----------------------------------------------------------------------
	def set_createNodeCommand(self, value):
		"""
		
				Specifies a function to be used to create nodes through the editor. The function will
				be passed the name of the chosen node type. This is used by the tab-create workflow.
				By default createNode is used.
				
		"""
		self.edit(createNodeCommand=value)
	#----------------------------------------------------------------------
	createNodeCommand = property(get_createNodeCommand, set_createNodeCommand)
	#----------------------------------------------------------------------
	def createTab(self,value):
		"""
		
				Create a new tab inserting it into the tab widget at the specified index. If
				index is out of range (such as -1), the tab is simply appended. You can
				optionally (Python only) specify a tab label, otherwise it will be set with a
				default name. In Mel using an empty string ("") for the tab label will set it
				with a default name. The new tab becomes the current (active) tab.
				Note: Only certain Node Editors are allowed to create new tabs, which can
				be checked by using the -allowNewTabs flag.
				
		"""
		self.edit(createTab=value)
	#----------------------------------------------------------------------
	def get_crosshairOnEdgeDragging(self):
		"""
		
				Toggle crosshair cursor during edge dragging on/off.
				
		"""
		return self.query(crosshairOnEdgeDragging=True)
	#----------------------------------------------------------------------
	def set_crosshairOnEdgeDragging(self, value):
		"""
		
				Toggle crosshair cursor during edge dragging on/off.
				
		"""
		self.edit(crosshairOnEdgeDragging=value)
	#----------------------------------------------------------------------
	crosshairOnEdgeDragging = property(get_crosshairOnEdgeDragging, set_crosshairOnEdgeDragging)
	#----------------------------------------------------------------------
	def get_customAttributeListEdit(self):
		"""
		
				Create/Edit the custom attribute list for the given node by entering
				a special "Edit Mode" for the node. Note: only one node in the node
				editor can be in this edit mode at a time. If another node is selected
				the edit mode will end automatically. To end the edit mode use an empty
				string for node.
				Takes an optional edit mode command which accepts: "hideall" (sets all
				the attributes to hidden), "showall" (sets all the attributes to visible),
				"preview" (temporarily shows only the visible attributes), "revert"
				(restores the visibility settings of the attributes to what they were
				before edit mode) and "reset" (the visible attributes are reset so that
				only the interesting attributes are displayed).
				In query mode returns the name of the node, if any, in edit mode.
				Note: the optional string argument is ignored in query mode.
				
		"""
		return self.query(customAttributeListEdit=True)
	#----------------------------------------------------------------------
	def set_customAttributeListEdit(self, value):
		"""
		
				Create/Edit the custom attribute list for the given node by entering
				a special "Edit Mode" for the node. Note: only one node in the node
				editor can be in this edit mode at a time. If another node is selected
				the edit mode will end automatically. To end the edit mode use an empty
				string for node.
				Takes an optional edit mode command which accepts: "hideall" (sets all
				the attributes to hidden), "showall" (sets all the attributes to visible),
				"preview" (temporarily shows only the visible attributes), "revert"
				(restores the visibility settings of the attributes to what they were
				before edit mode) and "reset" (the visible attributes are reset so that
				only the interesting attributes are displayed).
				In query mode returns the name of the node, if any, in edit mode.
				Note: the optional string argument is ignored in query mode.
				
		"""
		self.edit(customAttributeListEdit=value)
	#----------------------------------------------------------------------
	customAttributeListEdit = property(get_customAttributeListEdit, set_customAttributeListEdit)
	#----------------------------------------------------------------------
	def cycleHUD(self,value):
		"""
		
				Change the HUD to the next state.
				
		"""
		self.edit(cycleHUD=value)
	#----------------------------------------------------------------------
	def get_defaultPinnedState(self):
		"""
		
				Sets default pinned state of all nodes, 1 for pinned, 0 for unpinned. default value 0
				
		"""
		return self.query(defaultPinnedState=True)
	#----------------------------------------------------------------------
	def set_defaultPinnedState(self, value):
		"""
		
				Sets default pinned state of all nodes, 1 for pinned, 0 for unpinned. default value 0
				
		"""
		self.edit(defaultPinnedState=value)
	#----------------------------------------------------------------------
	defaultPinnedState = property(get_defaultPinnedState, set_defaultPinnedState)
	#----------------------------------------------------------------------
	def deleteSelected(self,value):
		"""
		
				Delete the selected nodes and break the selected connections.
				
		"""
		self.edit(deleteSelected=value)
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
	def get_dotFormat(self):
		"""
		
				In query mode:
				Get the graph information in DOT format. The flag argument specifies a file path to write to.
				If "-" is supplied, the data is returned as a string, otherwise the size in bytes of the written
				file is returned.
				In edit mode:
				Sets the positions of nodes in the graph from a Graphviz output file in plain format. Only the
				node position, width and height information is used.
				If the argument starts with "graph ", it will be treated as the plain data instead of a filename.
				      In query mode, this flag needs a value.
				
		"""
		return self.query(dotFormat=True)
	#----------------------------------------------------------------------
	def set_dotFormat(self, value):
		"""
		
				In query mode:
				Get the graph information in DOT format. The flag argument specifies a file path to write to.
				If "-" is supplied, the data is returned as a string, otherwise the size in bytes of the written
				file is returned.
				In edit mode:
				Sets the positions of nodes in the graph from a Graphviz output file in plain format. Only the
				node position, width and height information is used.
				If the argument starts with "graph ", it will be treated as the plain data instead of a filename.
				      In query mode, this flag needs a value.
				
		"""
		self.edit(dotFormat=value)
	#----------------------------------------------------------------------
	dotFormat = property(get_dotFormat, set_dotFormat)
	#----------------------------------------------------------------------
	def downstream(self,value):
		"""
		
				Include nodes that are downstream of the root nodes.
				
		"""
		self.edit(downstream=value)
	#----------------------------------------------------------------------
	def duplicateTab(self,value):
		"""
		
				Duplicates the tab at the specified index, placing it at the second optional
				(Python only) specified index. To place duplicated tab at the end use -1.
				The duplicated tab becomes the current (active) tab.
				Note: Only certain Node Editors are allowed to duplicate tabs, which can
				be checked by using the -allowNewTabs flag.
				
		"""
		self.edit(duplicateTab=value)
	#----------------------------------------------------------------------
	def get_enableOpenGL(self):
		"""
		
				Specifies if OpenGL should be used to render the node editor view.
				When enabled this will greatly improve performance but is still a work in progress.
				
		"""
		return self.query(enableOpenGL=True)
	#----------------------------------------------------------------------
	def set_enableOpenGL(self, value):
		"""
		
				Specifies if OpenGL should be used to render the node editor view.
				When enabled this will greatly improve performance but is still a work in progress.
				
		"""
		self.edit(enableOpenGL=value)
	#----------------------------------------------------------------------
	enableOpenGL = property(get_enableOpenGL, set_enableOpenGL)
	#----------------------------------------------------------------------
	def get_extendToShapes(self):
		"""
		
				Include child shapes for each selected transform.
				
		"""
		return self.query(extendToShapes=True)
	#----------------------------------------------------------------------
	def set_extendToShapes(self, value):
		"""
		
				Include child shapes for each selected transform.
				
		"""
		self.edit(extendToShapes=value)
	#----------------------------------------------------------------------
	extendToShapes = property(get_extendToShapes, set_extendToShapes)
	#----------------------------------------------------------------------
	@property
	def feedbackConnection(self):
		"""
		
				Returns a description of the connection(s) at the current mouse position in the
				editor view, if any.
				The connection(s) will be returned as a list of strings, which are
				pairs of plugs for each connection.
				
		"""
		return self.query(feedbackConnection=True)
	#----------------------------------------------------------------------
	@property
	def feedbackNode(self):
		"""
		
				Returns the name of the node at the current mouse position in the editor view,
				if any.
				
		"""
		return self.query(feedbackNode=True)
	#----------------------------------------------------------------------
	@property
	def feedbackPlug(self):
		"""
		
				Returns the name of the plug (attribute) at the current mouse position
				in the editor view, if any.
				
		"""
		return self.query(feedbackPlug=True)
	#----------------------------------------------------------------------
	@property
	def feedbackTabIndex(self):
		"""
		
				Returns the index of the tab at the current mouse position in the editor view,
				if any.
				
		"""
		return self.query(feedbackTabIndex=True)
	#----------------------------------------------------------------------
	@property
	def feedbackType(self):
		"""
		
				Returns the most specific type of the feedback item (item at the current mouse
				position) in the editor view, if any.
				Will be one of "plug", "node", "tab", "connection" or an empty string.
				Use the other feedback* flags to query the item description.
				
		"""
		return self.query(feedbackType=True)
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
	def get_filterCreateNodeTypes(self):
		"""
		
				Specifies a function to be used to filter the list of node types which
				appear in the inline-creation menu (tab key). The function should accept
				one string array argument and return a string array.
				
		"""
		return self.query(filterCreateNodeTypes=True)
	#----------------------------------------------------------------------
	def set_filterCreateNodeTypes(self, value):
		"""
		
				Specifies a function to be used to filter the list of node types which
				appear in the inline-creation menu (tab key). The function should accept
				one string array argument and return a string array.
				
		"""
		self.edit(filterCreateNodeTypes=value)
	#----------------------------------------------------------------------
	filterCreateNodeTypes = property(get_filterCreateNodeTypes, set_filterCreateNodeTypes)
	#----------------------------------------------------------------------
	def get_focusCommand(self):
		"""
		
				Specifies a function to be called whenever focus changes for the node editor.
				
		"""
		return self.query(focusCommand=True)
	#----------------------------------------------------------------------
	def set_focusCommand(self, value):
		"""
		
				Specifies a function to be called whenever focus changes for the node editor.
				
		"""
		self.edit(focusCommand=value)
	#----------------------------------------------------------------------
	focusCommand = property(get_focusCommand, set_focusCommand)
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
	def frameAll(self,value):
		"""
		
				Frame all the contents of the node editor.
				
		"""
		self.edit(frameAll=value)
	#----------------------------------------------------------------------
	def frameModelSelection(self,value):
		"""
		
				Frame the current model selection.
				
		"""
		self.edit(frameModelSelection=value)
	#----------------------------------------------------------------------
	def frameSelected(self,value):
		"""
		
				Frame the selected contents of the node editor.
				
		"""
		self.edit(frameSelected=value)
	#----------------------------------------------------------------------
	@property
	def getNodeList(self):
		"""
		
				Returns a list of all nodes displayed in the editor.
				
		"""
		return self.query(getNodeList=True)
	#----------------------------------------------------------------------
	def graphSelectedConnections(self,value):
		"""
		
				Graph the nodes connected by the selected attribute connections.
				
		"""
		self.edit(graphSelectedConnections=value)
	#----------------------------------------------------------------------
	def graphSelection(self,value):
		"""
		
				Graph the nodes that are currently selected.
				
		"""
		self.edit(graphSelection=value)
	#----------------------------------------------------------------------
	def get_gridSnap(self):
		"""
		
				Toggle grid snapping on/off.
				
		"""
		return self.query(gridSnap=True)
	#----------------------------------------------------------------------
	def set_gridSnap(self, value):
		"""
		
				Toggle grid snapping on/off.
				
		"""
		self.edit(gridSnap=value)
	#----------------------------------------------------------------------
	gridSnap = property(get_gridSnap, set_gridSnap)
	#----------------------------------------------------------------------
	def get_gridVisibility(self):
		"""
		
				Toggle grid visiblity on/off.
				
		"""
		return self.query(gridVisibility=True)
	#----------------------------------------------------------------------
	def set_gridVisibility(self, value):
		"""
		
				Toggle grid visiblity on/off.
				
		"""
		self.edit(gridVisibility=value)
	#----------------------------------------------------------------------
	gridVisibility = property(get_gridVisibility, set_gridVisibility)
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
	def get_highlightConnections(self):
		"""
		
				Sets if selecting a node should highlight its connections for the specified editor,
				which can be "regular" or "bifrost".
				
		"""
		return self.query(highlightConnections=True)
	#----------------------------------------------------------------------
	def set_highlightConnections(self, value):
		"""
		
				Sets if selecting a node should highlight its connections for the specified editor,
				which can be "regular" or "bifrost".
				
		"""
		self.edit(highlightConnections=value)
	#----------------------------------------------------------------------
	highlightConnections = property(get_highlightConnections, set_highlightConnections)
	#----------------------------------------------------------------------
	def hudMessage(self,value):
		"""
		
				Display the given message on the editor HUD.
				The flag arguments are (message, type, duration), where type is:
				
				upper-left corner.
				top center.
				upper-right corner.
				center.
				
				Duration 0 means the message stays until removed. Duration > 0 means it stays for that number of seconds.
				An empty message erases whatever is currently displayed for the given type.
				
		"""
		self.edit(hudMessage=value)
	#----------------------------------------------------------------------
	def get_ignoreAssets(self):
		"""
		
				Deprecated. Do not use in scripts.
				
		"""
		return self.query(ignoreAssets=True)
	#----------------------------------------------------------------------
	def set_ignoreAssets(self, value):
		"""
		
				Deprecated. Do not use in scripts.
				
		"""
		self.edit(ignoreAssets=value)
	#----------------------------------------------------------------------
	ignoreAssets = property(get_ignoreAssets, set_ignoreAssets)
	#----------------------------------------------------------------------
	def get_island(self):
		"""
		
				Deprecated. Do not use in scripts.
				
		"""
		return self.query(island=True)
	#----------------------------------------------------------------------
	def set_island(self, value):
		"""
		
				Deprecated. Do not use in scripts.
				
		"""
		self.edit(island=value)
	#----------------------------------------------------------------------
	island = property(get_island, set_island)
	#----------------------------------------------------------------------
	def get_keyPressCommand(self):
		"""
		
				Specifies a function to be called when a key is pressed and the editor has focus.
				
				The function will be passed the name of the editor and an (uppercase) string representation of the key that was pressed, and should return true if the key was handled, and false if it was not.
				
				Note: `getModifiers` can be used to query the current state of key modifiers.
				
		"""
		return self.query(keyPressCommand=True)
	#----------------------------------------------------------------------
	def set_keyPressCommand(self, value):
		"""
		
				Specifies a function to be called when a key is pressed and the editor has focus.
				
				The function will be passed the name of the editor and an (uppercase) string representation of the key that was pressed, and should return true if the key was handled, and false if it was not.
				
				Note: `getModifiers` can be used to query the current state of key modifiers.
				
		"""
		self.edit(keyPressCommand=value)
	#----------------------------------------------------------------------
	keyPressCommand = property(get_keyPressCommand, set_keyPressCommand)
	#----------------------------------------------------------------------
	def get_keyReleaseCommand(self):
		"""
		
				Specifies a function to be called when a key is released and the editor has focus.
				
				The function will be passed the name of the editor and an (uppercase) string representation of the key that was released, and should return true if the key was handled, and false if it was not.
				
				Note: `getModifiers` can be used to query the current state of key modifiers.
				
		"""
		return self.query(keyReleaseCommand=True)
	#----------------------------------------------------------------------
	def set_keyReleaseCommand(self, value):
		"""
		
				Specifies a function to be called when a key is released and the editor has focus.
				
				The function will be passed the name of the editor and an (uppercase) string representation of the key that was released, and should return true if the key was handled, and false if it was not.
				
				Note: `getModifiers` can be used to query the current state of key modifiers.
				
		"""
		self.edit(keyReleaseCommand=value)
	#----------------------------------------------------------------------
	keyReleaseCommand = property(get_keyReleaseCommand, set_keyReleaseCommand)
	#----------------------------------------------------------------------
	def layout(self,value):
		"""
		
				Perform an automatic layout of the graph.
				
		"""
		self.edit(layout=value)
	#----------------------------------------------------------------------
	def get_layoutCommand(self):
		"""
		
				Specifies a function to override the default action when a graph layout is required. The function will
				be passed the name of editor. The function should arrange the nodes in the graph.
				
		"""
		return self.query(layoutCommand=True)
	#----------------------------------------------------------------------
	def set_layoutCommand(self, value):
		"""
		
				Specifies a function to override the default action when a graph layout is required. The function will
				be passed the name of editor. The function should arrange the nodes in the graph.
				
		"""
		self.edit(layoutCommand=value)
	#----------------------------------------------------------------------
	layoutCommand = property(get_layoutCommand, set_layoutCommand)
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
	def nodeSwatchSize(self,value):
		"""
		
				Sets the icon swatch size of selected nodes in the active scene (all nodes if none are selected).
				Size values are "small" and "large".
				
		"""
		self.edit(nodeSwatchSize=value)
	#----------------------------------------------------------------------
	def get_nodeTitleMode(self):
		"""
		
				Gets/sets the node title display mode of the current scene.
				Mode values are:
				"name" (Display node names),
				"type" (Display node types),
				"none" (Do not display titles)
				
		"""
		return self.query(nodeTitleMode=True)
	#----------------------------------------------------------------------
	def set_nodeTitleMode(self, value):
		"""
		
				Gets/sets the node title display mode of the current scene.
				Mode values are:
				"name" (Display node names),
				"type" (Display node types),
				"none" (Do not display titles)
				
		"""
		self.edit(nodeTitleMode=value)
	#----------------------------------------------------------------------
	nodeTitleMode = property(get_nodeTitleMode, set_nodeTitleMode)
	#----------------------------------------------------------------------
	def nodeViewMode(self,value):
		"""
		
				Sets the attribute view mode of selected nodes in the active scene (all nodes if none are selected).
				Mode values are: "simple" (no attributes displayed), "connected" (connected attributes only), "all"
				(all interesting attributes displayed) and "custom" (use custom attribute view).
				
		"""
		self.edit(nodeViewMode=value)
	#----------------------------------------------------------------------
	def panView(self,value):
		"""
		
				Pan the view by the given amount. Arguments of 0 0 will reset the view translation.
				
		"""
		self.edit(panView=value)
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
	def pinSelectedNodes(self,value):
		"""
		
				Pins or unpins the selected nodes. If no nodes are selected, this will apply to all displayed nodes.
				
		"""
		self.edit(pinSelectedNodes=value)
	#----------------------------------------------------------------------
	def get_popupMenuScript(self):
		"""
		
				Set the script to be called to register the popup menu with the
				control for this editor. The script will be called with a string
				argument which gives the name of the editor whose control the popup
				menu should be parented to.
				
		"""
		return self.query(popupMenuScript=True)
	#----------------------------------------------------------------------
	def set_popupMenuScript(self, value):
		"""
		
				Set the script to be called to register the popup menu with the
				control for this editor. The script will be called with a string
				argument which gives the name of the editor whose control the popup
				menu should be parented to.
				
		"""
		self.edit(popupMenuScript=value)
	#----------------------------------------------------------------------
	popupMenuScript = property(get_popupMenuScript, set_popupMenuScript)
	#----------------------------------------------------------------------
	@property
	def primary(self):
		"""
		
				Query only. Returns whether this node editor is the primary one. The
				primary editor is the only one that will show and allow tabs.
				
		"""
		return self.query(primary=True)
	#----------------------------------------------------------------------
	def get_redockTab(self):
		"""
		
				If this tab was torn-off from the primary node editor, then the tab and all its
				data will be re-docked back into the primary editor and this node editor will
				be closed. In query mode returns whether this tab was torn-off and is available
				to be re-docked.
				
		"""
		return self.query(redockTab=True)
	#----------------------------------------------------------------------
	def set_redockTab(self, value):
		"""
		
				If this tab was torn-off from the primary node editor, then the tab and all its
				data will be re-docked back into the primary editor and this node editor will
				be closed. In query mode returns whether this tab was torn-off and is available
				to be re-docked.
				
		"""
		self.edit(redockTab=value)
	#----------------------------------------------------------------------
	redockTab = property(get_redockTab, set_redockTab)
	#----------------------------------------------------------------------
	def removeDownstream(self,value):
		"""
		
				Removes all items downstream to the currently active selection.
				
		"""
		self.edit(removeDownstream=value)
	#----------------------------------------------------------------------
	def removeNode(self,value):
		"""
		
				Removes a node from the graph. An empty string indicates that currently selected nodes should be removed.
				
		"""
		self.edit(removeNode=value)
	#----------------------------------------------------------------------
	def removeUnselected(self,value):
		"""
		
				Removes unselected nodes from graph.
				
		"""
		self.edit(removeUnselected=value)
	#----------------------------------------------------------------------
	def removeUpstream(self,value):
		"""
		
				Removes all items upstream to the currently active selection.
				
		"""
		self.edit(removeUpstream=value)
	#----------------------------------------------------------------------
	def renameNode(self,value):
		"""
		
				Rename a node in the graph. Depending on the zoom level of the view, an edit field
				will either appear on the node item or in a popup dialog to allow the new name to be
				entered.
				
		"""
		self.edit(renameNode=value)
	#----------------------------------------------------------------------
	def renameTab(self,value):
		"""
		
				Renames the tab at the specified index with the (optional) name. If no name is
				specified (Python only) or an empty string ("") is used then an inline edit field
				is opened to rename the tab.
				
		"""
		self.edit(renameTab=value)
	#----------------------------------------------------------------------
	def restoreInfo(self,value):
		"""
		
				Restores the editor state corresponding to supplied hyperGraphInfo node.
				
		"""
		self.edit(restoreInfo=value)
	#----------------------------------------------------------------------
	def get_restoreLastClosedTab(self):
		"""
		
				If this node editor is the primary one, then restore the last closed tab
				(if any). In query mode returns whether there is a tab available to restore.
				
		"""
		return self.query(restoreLastClosedTab=True)
	#----------------------------------------------------------------------
	def set_restoreLastClosedTab(self, value):
		"""
		
				If this node editor is the primary one, then restore the last closed tab
				(if any). In query mode returns whether there is a tab available to restore.
				
		"""
		self.edit(restoreLastClosedTab=value)
	#----------------------------------------------------------------------
	restoreLastClosedTab = property(get_restoreLastClosedTab, set_restoreLastClosedTab)
	#----------------------------------------------------------------------
	def rootNode(self,value):
		"""
		
				Add a node name as a root node of the graph.
				Passing an empty string clears the current root node list.
				When queried, returns the list of current root nodes.
				
		"""
		self.edit(rootNode=value)
	#----------------------------------------------------------------------
	def rootsFromSelection(self,value):
		"""
		
				Specify that the root nodes for the graph should taken from the currently active selection.
				
		"""
		self.edit(rootsFromSelection=value)
	#----------------------------------------------------------------------
	def scaleView(self,value):
		"""
		
				Scales the graph view by the given factor. An argument of zero means reset to default.
				
		"""
		self.edit(scaleView=value)
	#----------------------------------------------------------------------
	def selectAll(self,value):
		"""
		
				Select all items in the graph.
				
		"""
		self.edit(selectAll=value)
	#----------------------------------------------------------------------
	def selectConnectionNodes(self,value):
		"""
		
				Select the nodes connected by the selected attribute connections.
				
		"""
		self.edit(selectConnectionNodes=value)
	#----------------------------------------------------------------------
	def selectDownstream(self,value):
		"""
		
				Select all items downstream to the currently active selection.
				
		"""
		self.edit(selectDownstream=value)
	#----------------------------------------------------------------------
	def selectFeedbackConnection(self,value):
		"""
		
				Select the feedback connection(s) in the editor view, if any.
				
		"""
		self.edit(selectFeedbackConnection=value)
	#----------------------------------------------------------------------
	def get_selectNode(self):
		"""
		
				Select a node in the graph.
				Passing an empty string clears the current selection.
				When queried, returns the list of currently selected nodes.
				
		"""
		return self.query(selectNode=True)
	#----------------------------------------------------------------------
	def set_selectNode(self, value):
		"""
		
				Select a node in the graph.
				Passing an empty string clears the current selection.
				When queried, returns the list of currently selected nodes.
				
		"""
		self.edit(selectNode=value)
	#----------------------------------------------------------------------
	selectNode = property(get_selectNode, set_selectNode)
	#----------------------------------------------------------------------
	def selectUpstream(self,value):
		"""
		
				Select all items upstream to the currently active selection.
				
		"""
		self.edit(selectUpstream=value)
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
	def get_settingsChangedCallback(self):
		"""
		
				Specifies a function to be called whenever settings for the node editor
				get changed.
				
		"""
		return self.query(settingsChangedCallback=True)
	#----------------------------------------------------------------------
	def set_settingsChangedCallback(self, value):
		"""
		
				Specifies a function to be called whenever settings for the node editor
				get changed.
				
		"""
		self.edit(settingsChangedCallback=value)
	#----------------------------------------------------------------------
	settingsChangedCallback = property(get_settingsChangedCallback, set_settingsChangedCallback)
	#----------------------------------------------------------------------
	def shaderNetworks(self,value):
		"""
		
				Graph the shader network for all the objects on the selection list that have shaders.
				
		"""
		self.edit(shaderNetworks=value)
	#----------------------------------------------------------------------
	def showAllNodeAttributes(self,value):
		"""
		
				Display all attributes for the given node, not just primary attributes.
				Passing an empty string will apply this to all currently selected nodes.
				If no nodes are selected, this will be applied to all displayed nodes in the graph.
				
		"""
		self.edit(showAllNodeAttributes=value)
	#----------------------------------------------------------------------
	def get_showNamespace(self):
		"""
		
				Specifies whether nodes will have their namespace displayed if they are not in the root namespace.
				
		"""
		return self.query(showNamespace=True)
	#----------------------------------------------------------------------
	def set_showNamespace(self, value):
		"""
		
				Specifies whether nodes will have their namespace displayed if they are not in the root namespace.
				
		"""
		self.edit(showNamespace=value)
	#----------------------------------------------------------------------
	showNamespace = property(get_showNamespace, set_showNamespace)
	#----------------------------------------------------------------------
	def get_showSGShapes(self):
		"""
		
				Show shapes that are connected to the network through a shading group.
				
		"""
		return self.query(showSGShapes=True)
	#----------------------------------------------------------------------
	def set_showSGShapes(self, value):
		"""
		
				Show shapes that are connected to the network through a shading group.
				
		"""
		self.edit(showSGShapes=value)
	#----------------------------------------------------------------------
	showSGShapes = property(get_showSGShapes, set_showSGShapes)
	#----------------------------------------------------------------------
	def get_showShapes(self):
		"""
		
				Show shape nodes.
				
		"""
		return self.query(showShapes=True)
	#----------------------------------------------------------------------
	def set_showShapes(self, value):
		"""
		
				Show shape nodes.
				
		"""
		self.edit(showShapes=value)
	#----------------------------------------------------------------------
	showShapes = property(get_showShapes, set_showShapes)
	#----------------------------------------------------------------------
	def get_showTransforms(self):
		"""
		
				Show transforms.
				
		"""
		return self.query(showTransforms=True)
	#----------------------------------------------------------------------
	def set_showTransforms(self, value):
		"""
		
				Show transforms.
				
		"""
		self.edit(showTransforms=value)
	#----------------------------------------------------------------------
	showTransforms = property(get_showTransforms, set_showTransforms)
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
	def get_syncedSelection(self):
		"""
		
				Keep the graph selection in sync with the model selection.
				
		"""
		return self.query(syncedSelection=True)
	#----------------------------------------------------------------------
	def set_syncedSelection(self, value):
		"""
		
				Keep the graph selection in sync with the model selection.
				
		"""
		self.edit(syncedSelection=value)
	#----------------------------------------------------------------------
	syncedSelection = property(get_syncedSelection, set_syncedSelection)
	#----------------------------------------------------------------------
	def tabChangeCommand(self,value):
		"""
		
				Command executed when the current (active) tab is changed.
				Re-selecting the current tab will not invoke this command.
				NOTE: This command will also be executed when switching into,
				out of, and between compound views.
				
		"""
		self.edit(tabChangeCommand=value)
	#----------------------------------------------------------------------
	def toggleAttrFilter(self,value):
		"""
		
				Toggles the display of the attribute filter field on selected nodes. If any of the selected nodes have the field
				displayed, this operation will hide the field for all nodes in the selection. If no nodes are selected, this will
				apply to all displayed nodes.
				
		"""
		self.edit(toggleAttrFilter=value)
	#----------------------------------------------------------------------
	def toggleSelectedPins(self,value):
		"""
		
				Toggles pinned state on selected nodes. If any selected nodes are unpinned, this operation will choose to
				pin all nodes. If no nodes are selected, this will apply to all displayed nodes.
				
		"""
		self.edit(toggleSelectedPins=value)
	#----------------------------------------------------------------------
	def toggleSwatchSize(self,value):
		"""
		
				Toggles the swatch size of the given node between small and large. If supplied node name was empty, this will be applied to selection,
				and if no nodes are selected this is applied to all nodes in editor.
				When selection is a combination of small and large swatch sizes, this will set selection to large swatch mode.
				
		"""
		self.edit(toggleSwatchSize=value)
	#----------------------------------------------------------------------
	def get_toolTipCommand(self):
		"""
		
				Specifies a function to override the tooltip that is displayed for a node. The function will
				be passed the name of the node under the cursor, and should return a text string to be displayed.
				A simple HTML 4 subset is supported.
				
		"""
		return self.query(toolTipCommand=True)
	#----------------------------------------------------------------------
	def set_toolTipCommand(self, value):
		"""
		
				Specifies a function to override the tooltip that is displayed for a node. The function will
				be passed the name of the node under the cursor, and should return a text string to be displayed.
				A simple HTML 4 subset is supported.
				
		"""
		self.edit(toolTipCommand=value)
	#----------------------------------------------------------------------
	toolTipCommand = property(get_toolTipCommand, set_toolTipCommand)
	#----------------------------------------------------------------------
	def get_traversalDepthLimit(self):
		"""
		
				Specify the maximum number of edges which will be followed from any root node
				when building the graph. A negative value means unlimited. Default is unlimited.
				
		"""
		return self.query(traversalDepthLimit=True)
	#----------------------------------------------------------------------
	def set_traversalDepthLimit(self, value):
		"""
		
				Specify the maximum number of edges which will be followed from any root node
				when building the graph. A negative value means unlimited. Default is unlimited.
				
		"""
		self.edit(traversalDepthLimit=value)
	#----------------------------------------------------------------------
	traversalDepthLimit = property(get_traversalDepthLimit, set_traversalDepthLimit)
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
	#----------------------------------------------------------------------
	def upstream(self,value):
		"""
		
				Include nodes that are upstream of the root nodes.
				
		"""
		self.edit(upstream=value)
	#----------------------------------------------------------------------
	def get_useAssets(self):
		"""
		
				Use assets and published attributes instead of contents and actual attributes.
				
		"""
		return self.query(useAssets=True)
	#----------------------------------------------------------------------
	def set_useAssets(self, value):
		"""
		
				Use assets and published attributes instead of contents and actual attributes.
				
		"""
		self.edit(useAssets=value)
	#----------------------------------------------------------------------
	useAssets = property(get_useAssets, set_useAssets)