

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class HyperGraph(UI_Object.UI):
	"""
	The following is an overview of the basic features of the hypergraph.
	A more detailed description is given in the user manuals.
	
	The hypergraph provides the user with the ability to view and edit
	the maya scene graph.  The hypergraph supports two types of graphs:
	the DAG or scene hierarchy and the dependency graph.
	
	The default view of the hypergraph editor is the DAG view.
	The user can show the dependency graph for a collection of nodes by
	first selecting the nodes and navigating to the dependency graph using one
	of the graph options.  The user can save any view by setting a
	bookmark to that view.  The user can also show previous views using
	the view options provided.
	
	The hypergraph supports a simple editing mechanism for editing hierarchy
	in the DAG view and connections in dependency graph view.
	In the DAG  view, the user can reparent or reorder nodes in the graph
	using drag-and-drop. In the dependency graph view, the user can select
	connections and delete them or make new connections by dragging and
	dropping nodes or existing connections.
	
	The hypergraph supports two layout modes in the DAG view: automatic and
	freeform.  In automatic mode, the graph nodes are automatically
	positioned according to the layout preferences.  In freeform mode, the
	user can position nodes manually.  The node position is saved in the scene.
	A background image can be placed behind DG or DAG in freeform mode.
	This can be used as a template for positioning nodes in a user-defined
	layout.
	
	Nodes in the DAG view can be expanded or collapsed.  The state is saved
	in the scene.  The performance of the graph drawing will increase
	as hierarchies are collapsed.
	
	In addition to hierachy relationships, the hypergraph can show
	expression, constraint and deformation relationships in the DAG.
	These can be enabled/disabled through the options provided.  There
	are also additional filters for showing shape nodes and invisible
	nodes.  The amount of detail show may affect the speed of the display
	of the graph.
	
	Most of the UI features of the hypergraph are addressable through the
	hypergraph command-line interface.  The available command-line
	options are described in the next section.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.hyperGraph(**kwargs)
			super(HyperGraph, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.hyperGraph(name, exists=True):
				super(HyperGraph, self).__init__(name)
			else:
				name = cmds.hyperGraph(name, **kwargs)
				super(HyperGraph, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def addBookmark(self,value):
		"""
		
				Create a bookmark for the current hypergraph view.
				
		"""
		self.edit(addBookmark=value)
	#----------------------------------------------------------------------
	def addDependGraph(self,value):
		"""
		
				Add a dependency graph starting at the named node to the view
				
		"""
		self.edit(addDependGraph=value)
	#----------------------------------------------------------------------
	def addDependNode(self,value):
		"""
		
				Add a dependency node to the dependency graph view
				
		"""
		self.edit(addDependNode=value)
	#----------------------------------------------------------------------
	def get_animateTransition(self):
		"""
		
				Turns animate transitions off and on.
				
		"""
		return self.query(animateTransition=True)
	#----------------------------------------------------------------------
	def set_animateTransition(self, value):
		"""
		
				Turns animate transitions off and on.
				
		"""
		self.edit(animateTransition=value)
	#----------------------------------------------------------------------
	animateTransition = property(get_animateTransition, set_animateTransition)
	#----------------------------------------------------------------------
	def attributeEditor(self,value):
		"""
		
				Launches attribute editor on selected node.
				
		"""
		self.edit(attributeEditor=value)
	#----------------------------------------------------------------------
	def backward(self,value):
		"""
		
				Navigate backward one step.
				
		"""
		self.edit(backward=value)
	#----------------------------------------------------------------------
	@property
	def bookmarkName(self):
		"""
		
				Returns the bookmark name for the most recently created bookmark.
				
		"""
		return self.query(bookmarkName=True)
	#----------------------------------------------------------------------
	def get_breakConnectionCommand(self):
		"""
		
				Specify the command to call when a connection is broken.
				
		"""
		return self.query(breakConnectionCommand=True)
	#----------------------------------------------------------------------
	def set_breakConnectionCommand(self, value):
		"""
		
				Specify the command to call when a connection is broken.
				
		"""
		self.edit(breakConnectionCommand=value)
	#----------------------------------------------------------------------
	breakConnectionCommand = property(get_breakConnectionCommand, set_breakConnectionCommand)
	#----------------------------------------------------------------------
	def clear(self,value):
		"""
		
				Clears the current hypergraph view and deletes the graph UI.
				(see also -rebuild flag)
				
		"""
		self.edit(clear=value)
	#----------------------------------------------------------------------
	def collapseContainer(self,value):
		"""
		
				Collapses containers selected in DG graph.
				
		"""
		self.edit(collapseContainer=value)
	#----------------------------------------------------------------------
	def connectionDrawStyle(self,value):
		"""
		
				Specify how connections between nodes should be drawn. Valid
				values are "center" (draws connection lines from the center of one node
				to the center of the other) and "side" (draws connection lines from the
				right side of the source node to the left side of the destination
				node). The default is "center". This flag does not apply to Hypershade
				graphs, which are always drawn with the "side" connection draw style.
				
		"""
		self.edit(connectionDrawStyle=value)
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
	def get_currentEdge(self):
		"""
		
				Return the current edge name.
				
		"""
		return self.query(currentEdge=True)
	#----------------------------------------------------------------------
	def set_currentEdge(self, value):
		"""
		
				Return the current edge name.
				
		"""
		self.edit(currentEdge=value)
	#----------------------------------------------------------------------
	currentEdge = property(get_currentEdge, set_currentEdge)
	#----------------------------------------------------------------------
	def get_currentNode(self):
		"""
		
				Return the current node name.
				
		"""
		return self.query(currentNode=True)
	#----------------------------------------------------------------------
	def set_currentNode(self, value):
		"""
		
				Return the current node name.
				
		"""
		self.edit(currentNode=value)
	#----------------------------------------------------------------------
	currentNode = property(get_currentNode, set_currentNode)
	#----------------------------------------------------------------------
	def debug(self,value):
		"""
		
				Run a debug method on the graph
				
		"""
		self.edit(debug=value)
	#----------------------------------------------------------------------
	def deleteBookmark(self,value):
		"""
		
				Delete the bookmark with the corresponding node name.
				
		"""
		self.edit(deleteBookmark=value)
	#----------------------------------------------------------------------
	def dependGraph(self,value):
		"""
		
				Displays dependency graph iterated from specified node.
				
		"""
		self.edit(dependGraph=value)
	#----------------------------------------------------------------------
	def dependNode(self,value):
		"""
		
				Displays dependency node in view.
				
		"""
		self.edit(dependNode=value)
	#----------------------------------------------------------------------
	def directoryPressCommand(self,value):
		"""
		
				Specify a command to run when a directory is pressed.
				
		"""
		self.edit(directoryPressCommand=value)
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
	def down(self,value):
		"""
		
				Navigate down to the dependency graph containing the current selection.
				Shows upstream and downstream connections.
				
		"""
		self.edit(down=value)
	#----------------------------------------------------------------------
	def downstream(self,value):
		"""
		
				Show downstream dependency graph of selected node(s).
				
		"""
		self.edit(downstream=value)
	#----------------------------------------------------------------------
	def dragAndDropBehaviorCommand(self,value):
		"""
		
				Mel proc called when a drag and drop onto a hyperGraph
				node has occurred. Proc signature is
				procName (string $editor, string $sourceNode, string $destinationNode).
				
		"""
		self.edit(dragAndDropBehaviorCommand=value)
	#----------------------------------------------------------------------
	@property
	def dropNode(self):
		"""
		
				Returns the name of the source node in a drag and drop connection,
				when called during processing of a drop.
				
		"""
		return self.query(dropNode=True)
	#----------------------------------------------------------------------
	@property
	def dropTargetNode(self):
		"""
		
				Returns the name of the destination node in a drag and drop
				connection, when called during processing of a drop.
				
		"""
		return self.query(dropTargetNode=True)
	#----------------------------------------------------------------------
	def edgeDblClickCommand(self,value):
		"""
		
				Mel proc called when an edge is double clicked.  Proc signature is
				procName (string $editor, string $edge).
				
		"""
		self.edit(edgeDblClickCommand=value)
	#----------------------------------------------------------------------
	def edgeDimmedDblClickCommand(self,value):
		"""
		
				Mel proc called when a dimmed edge is double clicked.  Proc signature is
				procName (string $editor, string $edge).
				
		"""
		self.edit(edgeDimmedDblClickCommand=value)
	#----------------------------------------------------------------------
	def edgeDropCommand(self,value):
		"""
		
				Command to execute when an edge drop occurs.
				
		"""
		self.edit(edgeDropCommand=value)
	#----------------------------------------------------------------------
	def edgePressCommand(self,value):
		"""
		
				Command to execute when an edge press occurs.
				
		"""
		self.edit(edgePressCommand=value)
	#----------------------------------------------------------------------
	def edgeReleaseCommand(self,value):
		"""
		
				Command to execute when an edge release occurs.
				
		"""
		self.edit(edgeReleaseCommand=value)
	#----------------------------------------------------------------------
	def enableAutomaticLayout(self,value):
		"""
		
				Rebuild the graph if a node is added or removed from the graph
				via drag and drop or dg messages. Default is true.
				
		"""
		self.edit(enableAutomaticLayout=value)
	#----------------------------------------------------------------------
	def expandContainer(self,value):
		"""
		
				Expands containers selected in DG graph.
				
		"""
		self.edit(expandContainer=value)
	#----------------------------------------------------------------------
	@property
	def feedbackGadget(self):
		"""
		
				Returns the name of the current gadget.
				
		"""
		return self.query(feedbackGadget=True)
	#----------------------------------------------------------------------
	@property
	def feedbackNode(self):
		"""
		
				Returns the name of the current feedback or highlight node.
				
		"""
		return self.query(feedbackNode=True)
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
	def filterDetail(self,value):
		"""
		
				This flag is obsolete. Use the showConstraints, showExpressions,
				showDeformer, showInvisible, showShapes and showUnderworld flags
				instead.
				
		"""
		self.edit(filterDetail=value)
	#----------------------------------------------------------------------
	def focusCommand(self,value):
		"""
		
				Mel proc to be run when the mouse is clicked in the hyper
				graph. Primarily of use in setting the window focus.
				
		"""
		self.edit(focusCommand=value)
	#----------------------------------------------------------------------
	def fold(self,value):
		"""
		
				Folds (Collapses) selected object.
				
		"""
		self.edit(fold=value)
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
	def forceRefresh(self,value):
		"""
		
				Forces the hypergraph to refresh (redraw) its contents.
				
		"""
		self.edit(forceRefresh=value)
	#----------------------------------------------------------------------
	def forward(self,value):
		"""
		
				Navigate forward one step.
				
		"""
		self.edit(forward=value)
	#----------------------------------------------------------------------
	def frame(self,value):
		"""
		
				Frames the selected objects
				
		"""
		self.edit(frame=value)
	#----------------------------------------------------------------------
	def frameBranch(self,value):
		"""
		
				Frames the the branch from the selected node on downward.
				
		"""
		self.edit(frameBranch=value)
	#----------------------------------------------------------------------
	def frameGraph(self,value):
		"""
		
				Frames the entire graph.
				
		"""
		self.edit(frameGraph=value)
	#----------------------------------------------------------------------
	def frameGraphNoRebuild(self,value):
		"""
		
				Specify that on zoom out the graph should not rebuild; for efficiency.
				
		"""
		self.edit(frameGraphNoRebuild=value)
	#----------------------------------------------------------------------
	def frameHierarchy(self,value):
		"""
		
				Frames the hierarchy that contains the selected node.
				
		"""
		self.edit(frameHierarchy=value)
	#----------------------------------------------------------------------
	def get_freeform(self):
		"""
		
				Enable freeform layout mode.
				
		"""
		return self.query(freeform=True)
	#----------------------------------------------------------------------
	def set_freeform(self, value):
		"""
		
				Enable freeform layout mode.
				
		"""
		self.edit(freeform=value)
	#----------------------------------------------------------------------
	freeform = property(get_freeform, set_freeform)
	#----------------------------------------------------------------------
	@property
	def fromAttr(self):
		"""
		
				Returns the name of the source attribute in a drag and drop
				connection, when called during processing of a drop.
				
		"""
		return self.query(fromAttr=True)
	#----------------------------------------------------------------------
	@property
	def fromNode(self):
		"""
		
				Returns the name of the source node in a drag and drop
				connection, when called during processing of a drop.
				
		"""
		return self.query(fromNode=True)
	#----------------------------------------------------------------------
	@property
	def getNodeList(self):
		"""
		
				Returns a string array that represents a list
				of all the nodes in the graph.
				
		"""
		return self.query(getNodeList=True)
	#----------------------------------------------------------------------
	@property
	def getNodePosition(self):
		"""
		
				Returns the position of a specified node in x,y graph coords.
				This flag and its argument must be passed to the command before the
				-q flag (see examples).
				      In query mode, this flag can accept a value.
				
		"""
		return self.query(getNodePosition=True)
	#----------------------------------------------------------------------
	def graphDescription(self,value):
		"""
		
				When used, return a description of the current graph.
				
		"""
		self.edit(graphDescription=value)
	#----------------------------------------------------------------------
	def get_graphLayoutStyle(self):
		"""
		
				This flag is obsolete.  The only supported graph layout style is "hierarchicalLayout".
				Use of any other style will trigger a warning.
				
		"""
		return self.query(graphLayoutStyle=True)
	#----------------------------------------------------------------------
	def set_graphLayoutStyle(self, value):
		"""
		
				This flag is obsolete.  The only supported graph layout style is "hierarchicalLayout".
				Use of any other style will trigger a warning.
				
		"""
		self.edit(graphLayoutStyle=value)
	#----------------------------------------------------------------------
	graphLayoutStyle = property(get_graphLayoutStyle, set_graphLayoutStyle)
	#----------------------------------------------------------------------
	@property
	def graphType(self):
		"""
		
				Returns the type name of the current graph in the view
				(either DAG or DG).
				
		"""
		return self.query(graphType=True)
	#----------------------------------------------------------------------
	def get_heatMapDisplay(self):
		"""
		
				Specify whether the heat map should be shown or not.
				
		"""
		return self.query(heatMapDisplay=True)
	#----------------------------------------------------------------------
	def set_heatMapDisplay(self, value):
		"""
		
				Specify whether the heat map should be shown or not.
				
		"""
		self.edit(heatMapDisplay=value)
	#----------------------------------------------------------------------
	heatMapDisplay = property(get_heatMapDisplay, set_heatMapDisplay)
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
	def get_iconSize(self):
		"""
		
				Set or query the icon size for this hyper graph editor.
				The currently allowed icon sizes are "smallIcons", "mediumIcons",
				"largeIcons" and "superIcons".
				
		"""
		return self.query(iconSize=True)
	#----------------------------------------------------------------------
	def set_iconSize(self, value):
		"""
		
				Set or query the icon size for this hyper graph editor.
				The currently allowed icon sizes are "smallIcons", "mediumIcons",
				"largeIcons" and "superIcons".
				
		"""
		self.edit(iconSize=value)
	#----------------------------------------------------------------------
	iconSize = property(get_iconSize, set_iconSize)
	#----------------------------------------------------------------------
	def get_image(self):
		"""
		
				Specify background image to be loaded from the project image directory.
				
		"""
		return self.query(image=True)
	#----------------------------------------------------------------------
	def set_image(self, value):
		"""
		
				Specify background image to be loaded from the project image directory.
				
		"""
		self.edit(image=value)
	#----------------------------------------------------------------------
	image = property(get_image, set_image)
	#----------------------------------------------------------------------
	def get_imageEnabled(self):
		"""
		
				Enable display of a loaded background image (Freeform DAG view or DG view)
				
		"""
		return self.query(imageEnabled=True)
	#----------------------------------------------------------------------
	def set_imageEnabled(self, value):
		"""
		
				Enable display of a loaded background image (Freeform DAG view or DG view)
				
		"""
		self.edit(imageEnabled=value)
	#----------------------------------------------------------------------
	imageEnabled = property(get_imageEnabled, set_imageEnabled)
	#----------------------------------------------------------------------
	def get_imageForContainer(self):
		"""
		
				Specify that the following flags work on selected containers instead of the whole image:
				-imageScale,-imagePosition, fitImageToWidth, -fitImageToHeight, -image
				
		"""
		return self.query(imageForContainer=True)
	#----------------------------------------------------------------------
	def set_imageForContainer(self, value):
		"""
		
				Specify that the following flags work on selected containers instead of the whole image:
				-imageScale,-imagePosition, fitImageToWidth, -fitImageToHeight, -image
				
		"""
		self.edit(imageForContainer=value)
	#----------------------------------------------------------------------
	imageForContainer = property(get_imageForContainer, set_imageForContainer)
	#----------------------------------------------------------------------
	def get_imagePosition(self):
		"""
		
				Position of the background image.
				
		"""
		return self.query(imagePosition=True)
	#----------------------------------------------------------------------
	def set_imagePosition(self, value):
		"""
		
				Position of the background image.
				
		"""
		self.edit(imagePosition=value)
	#----------------------------------------------------------------------
	imagePosition = property(get_imagePosition, set_imagePosition)
	#----------------------------------------------------------------------
	def get_imageScale(self):
		"""
		
				Uniform scale of the background image.
				
		"""
		return self.query(imageScale=True)
	#----------------------------------------------------------------------
	def set_imageScale(self, value):
		"""
		
				Uniform scale of the background image.
				
		"""
		self.edit(imageScale=value)
	#----------------------------------------------------------------------
	imageScale = property(get_imageScale, set_imageScale)
	#----------------------------------------------------------------------
	def initializeScript(self,value):
		"""
		
				Script to call when the graph is initialized.
				
		"""
		self.edit(initializeScript=value)
	#----------------------------------------------------------------------
	@property
	def isHotkeyTarget(self):
		"""
		
				For internal use.
				
		"""
		return self.query(isHotkeyTarget=True)
	#----------------------------------------------------------------------
	def layout(self,value):
		"""
		
				Perform an automatic layout on the graph.
				
		"""
		self.edit(layout=value)
	#----------------------------------------------------------------------
	def layoutSelected(self,value):
		"""
		
				This flag is obsolete.  The only supported graph layout style is "hierarchicalLayout".
				Use of any other style will trigger a warning.
				
		"""
		self.edit(layoutSelected=value)
	#----------------------------------------------------------------------
	def limitGraphTraversal(self,value):
		"""
		
				Limit the graph traversal to a certain number of levels.
				
		"""
		self.edit(limitGraphTraversal=value)
	#----------------------------------------------------------------------
	def lockMainConnection(self,value):
		"""
		
				Locks the current list of objects within the mainConnection,
				so that only those objects are displayed within the editor.
				Further changes to the original mainConnection are ignored.
				
		"""
		self.edit(lockMainConnection=value)
	#----------------------------------------------------------------------
	def look(self,value):
		"""
		
				Look at a coordinate in the graph view
				
		"""
		self.edit(look=value)
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
	def get_mergeConnections(self):
		"""
		
				Merge groups of connections into 'fat' connections.
				
		"""
		return self.query(mergeConnections=True)
	#----------------------------------------------------------------------
	def set_mergeConnections(self, value):
		"""
		
				Merge groups of connections into 'fat' connections.
				
		"""
		self.edit(mergeConnections=value)
	#----------------------------------------------------------------------
	mergeConnections = property(get_mergeConnections, set_mergeConnections)
	#----------------------------------------------------------------------
	def navigateHome(self,value):
		"""
		
				Navigate to the home (DAG) view.
				
		"""
		self.edit(navigateHome=value)
	#----------------------------------------------------------------------
	def navup(self,value):
		"""
		
				Navigate up to the dependency graph containing the current selection.
				Shows upstream and downstream connections.
				
		"""
		self.edit(navup=value)
	#----------------------------------------------------------------------
	def newInputConnection(self,value):
		"""
		
				Specify a new connection, input side
				
		"""
		self.edit(newInputConnection=value)
	#----------------------------------------------------------------------
	def newOutputConnection(self,value):
		"""
		
				Specify a new connection, output side
				
		"""
		self.edit(newOutputConnection=value)
	#----------------------------------------------------------------------
	def nextView(self,value):
		"""
		
				Changes the view to the next DAG view.
				
		"""
		self.edit(nextView=value)
	#----------------------------------------------------------------------
	def nodeConnectCommand(self,value):
		"""
		
				Command to call when a node is connected.
				
		"""
		self.edit(nodeConnectCommand=value)
	#----------------------------------------------------------------------
	def nodeDblClickCommand(self,value):
		"""
		
				Command to call when a node is double-clicked.
				
		"""
		self.edit(nodeDblClickCommand=value)
	#----------------------------------------------------------------------
	def nodeDropCommand(self,value):
		"""
		
				Set the command to be called when a node is dropped in the
				hypergraph window.
				
		"""
		self.edit(nodeDropCommand=value)
	#----------------------------------------------------------------------
	def nodeMenuCommand(self,value):
		"""
		
				Command to call when a node menu is activated.
				
		"""
		self.edit(nodeMenuCommand=value)
	#----------------------------------------------------------------------
	def nodePressCommand(self,value):
		"""
		
				Set the command to be called when the user presses a mouse button
				while the cursor is over a node in the hypergraph window.
				
		"""
		self.edit(nodePressCommand=value)
	#----------------------------------------------------------------------
	def nodeReleaseCommand(self,value):
		"""
		
				Set the command to be called when the user releases a mouse button
				while the cursor is over a node in the hypergraph window.
				
		"""
		self.edit(nodeReleaseCommand=value)
	#----------------------------------------------------------------------
	def get_opaqueContainers(self):
		"""
		
				Sets expanded container background opacity.
				
		"""
		return self.query(opaqueContainers=True)
	#----------------------------------------------------------------------
	def set_opaqueContainers(self, value):
		"""
		
				Sets expanded container background opacity.
				
		"""
		self.edit(opaqueContainers=value)
	#----------------------------------------------------------------------
	opaqueContainers = property(get_opaqueContainers, set_opaqueContainers)
	#----------------------------------------------------------------------
	def get_orientation(self):
		"""
		
				Selects orientation style of graph: "horiz"|"vert"
				
		"""
		return self.query(orientation=True)
	#----------------------------------------------------------------------
	def set_orientation(self, value):
		"""
		
				Selects orientation style of graph: "horiz"|"vert"
				
		"""
		self.edit(orientation=value)
	#----------------------------------------------------------------------
	orientation = property(get_orientation, set_orientation)
	#----------------------------------------------------------------------
	def panView(self,value):
		"""
		
				Pan the view to a new center.
				
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
	def popupMenuScript(self,value):
		"""
		
				Set the script to be called to register the popup menu with the
				control for this hypergraph. The script will be called with a string
				argument which gives the name of the hypergraph whose control the popup
				menu should be parented to.
				
		"""
		self.edit(popupMenuScript=value)
	#----------------------------------------------------------------------
	def previousView(self,value):
		"""
		
				Changes the view back to the previous DAG view.
				
		"""
		self.edit(previousView=value)
	#----------------------------------------------------------------------
	def get_range(self):
		"""
		
				Limits the display of nodes to only those within the range.
				There are two float values expected, the first the lower threshold
				of the range and the second the upper threshold of the range.
				The values are absolute timing values, not percentages.
				
		"""
		return self.query(range=True)
	#----------------------------------------------------------------------
	def set_range(self, value):
		"""
		
				Limits the display of nodes to only those within the range.
				There are two float values expected, the first the lower threshold
				of the range and the second the upper threshold of the range.
				The values are absolute timing values, not percentages.
				
		"""
		self.edit(range=value)
	#----------------------------------------------------------------------
	range = property(get_range, set_range)
	#----------------------------------------------------------------------
	def rebuild(self,value):
		"""
		
				Rebuilds graph
				
		"""
		self.edit(rebuild=value)
	#----------------------------------------------------------------------
	def removeNode(self,value):
		"""
		
				Removes the node identified by string from the graph.
				
		"""
		self.edit(removeNode=value)
	#----------------------------------------------------------------------
	def rename(self,value):
		"""
		
				Pops up text field over selected object for renaming
				
		"""
		self.edit(rename=value)
	#----------------------------------------------------------------------
	def resetFreeform(self,value):
		"""
		
				Resets freeform position on all nodes.
				
		"""
		self.edit(resetFreeform=value)
	#----------------------------------------------------------------------
	def restoreBookmark(self,value):
		"""
		
				Restore the view corresponding to the bookmark.
				
		"""
		self.edit(restoreBookmark=value)
	#----------------------------------------------------------------------
	def scrollUpDownNoZoom(self,value):
		"""
		
				Specify if we want to be in the
				scroll along y only with no free zooming mode.
				By default, hyper graph editor allows user to
				pan left and right.
				
		"""
		self.edit(scrollUpDownNoZoom=value)
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
	def setNodePosition(self,value):
		"""
		
				Sets the node identified by string to the (x,y) position
				in the window specified by the two floats. If
				the node is not in the graph than it will be added to the
				graph and then moved to the new position.
				
		"""
		self.edit(setNodePosition=value)
	#----------------------------------------------------------------------
	def showCachedConnections(self,value):
		"""
		
				Specify whether cached connections should be shown.
				
		"""
		self.edit(showCachedConnections=value)
	#----------------------------------------------------------------------
	def get_showConnectionFromSelected(self):
		"""
		
				Show the connects (constraints, expresions, and deformers - see showConstraints for example)
				leaving from selected nodes. This can be combined with showConnectionToSelected to show both
				arrive and leaving connects. If both flags are false then all the connections will be shown.
				
		"""
		return self.query(showConnectionFromSelected=True)
	#----------------------------------------------------------------------
	def set_showConnectionFromSelected(self, value):
		"""
		
				Show the connects (constraints, expresions, and deformers - see showConstraints for example)
				leaving from selected nodes. This can be combined with showConnectionToSelected to show both
				arrive and leaving connects. If both flags are false then all the connections will be shown.
				
		"""
		self.edit(showConnectionFromSelected=value)
	#----------------------------------------------------------------------
	showConnectionFromSelected = property(get_showConnectionFromSelected, set_showConnectionFromSelected)
	#----------------------------------------------------------------------
	def get_showConnectionToSelected(self):
		"""
		
				Show the connects (constraints, expresions, and deformers - see showConstraints for example)
				arriving at selected nodes. This can be combined with
				showConnectionFromSelected to show both arrive and leaving connects. If both flags
				are false then all the connections will be shown.
				
		"""
		return self.query(showConnectionToSelected=True)
	#----------------------------------------------------------------------
	def set_showConnectionToSelected(self, value):
		"""
		
				Show the connects (constraints, expresions, and deformers - see showConstraints for example)
				arriving at selected nodes. This can be combined with
				showConnectionFromSelected to show both arrive and leaving connects. If both flags
				are false then all the connections will be shown.
				
		"""
		self.edit(showConnectionToSelected=value)
	#----------------------------------------------------------------------
	showConnectionToSelected = property(get_showConnectionToSelected, set_showConnectionToSelected)
	#----------------------------------------------------------------------
	def showConstraintLabels(self,value):
		"""
		
				Specify whether constraint labels should be shown.
				
		"""
		self.edit(showConstraintLabels=value)
	#----------------------------------------------------------------------
	def get_showConstraints(self):
		"""
		
				Show constraint relationships in the DAG.
				
		"""
		return self.query(showConstraints=True)
	#----------------------------------------------------------------------
	def set_showConstraints(self, value):
		"""
		
				Show constraint relationships in the DAG.
				
		"""
		self.edit(showConstraints=value)
	#----------------------------------------------------------------------
	showConstraints = property(get_showConstraints, set_showConstraints)
	#----------------------------------------------------------------------
	def get_showDeformers(self):
		"""
		
				Show deformer or geometry filter relationships in the DAG.
				
		"""
		return self.query(showDeformers=True)
	#----------------------------------------------------------------------
	def set_showDeformers(self, value):
		"""
		
				Show deformer or geometry filter relationships in the DAG.
				
		"""
		self.edit(showDeformers=value)
	#----------------------------------------------------------------------
	showDeformers = property(get_showDeformers, set_showDeformers)
	#----------------------------------------------------------------------
	def get_showExpressions(self):
		"""
		
				Show expression relationships in the DAG.
				
		"""
		return self.query(showExpressions=True)
	#----------------------------------------------------------------------
	def set_showExpressions(self, value):
		"""
		
				Show expression relationships in the DAG.
				
		"""
		self.edit(showExpressions=value)
	#----------------------------------------------------------------------
	showExpressions = property(get_showExpressions, set_showExpressions)
	#----------------------------------------------------------------------
	def get_showInvisible(self):
		"""
		
				Show invisible nodes in the DAG.
				
		"""
		return self.query(showInvisible=True)
	#----------------------------------------------------------------------
	def set_showInvisible(self, value):
		"""
		
				Show invisible nodes in the DAG.
				
		"""
		self.edit(showInvisible=value)
	#----------------------------------------------------------------------
	showInvisible = property(get_showInvisible, set_showInvisible)
	#----------------------------------------------------------------------
	def get_showRelationships(self):
		"""
		
				Show relationship (message) connections.
				
		"""
		return self.query(showRelationships=True)
	#----------------------------------------------------------------------
	def set_showRelationships(self, value):
		"""
		
				Show relationship (message) connections.
				
		"""
		self.edit(showRelationships=value)
	#----------------------------------------------------------------------
	showRelationships = property(get_showRelationships, set_showRelationships)
	#----------------------------------------------------------------------
	def get_showShapes(self):
		"""
		
				Show shape nodes in the DAG.
				
		"""
		return self.query(showShapes=True)
	#----------------------------------------------------------------------
	def set_showShapes(self, value):
		"""
		
				Show shape nodes in the DAG.
				
		"""
		self.edit(showShapes=value)
	#----------------------------------------------------------------------
	showShapes = property(get_showShapes, set_showShapes)
	#----------------------------------------------------------------------
	def get_showUnderworld(self):
		"""
		
				Show underworld graphs in the DAG.
				
		"""
		return self.query(showUnderworld=True)
	#----------------------------------------------------------------------
	def set_showUnderworld(self, value):
		"""
		
				Show underworld graphs in the DAG.
				
		"""
		self.edit(showUnderworld=value)
	#----------------------------------------------------------------------
	showUnderworld = property(get_showUnderworld, set_showUnderworld)
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
	@property
	def toAttr(self):
		"""
		
				Returns the name of the destination attribute in a drag and drop
				connection, when called during processing of a drop.
				
		"""
		return self.query(toAttr=True)
	#----------------------------------------------------------------------
	@property
	def toNode(self):
		"""
		
				Returns the name of the destination node in a drag and drop
				connection, when called during processing of a drop.
				
		"""
		return self.query(toNode=True)
	#----------------------------------------------------------------------
	def get_transitionFrames(self):
		"""
		
				Specify te number of transition frames for animate transitions.
				
		"""
		return self.query(transitionFrames=True)
	#----------------------------------------------------------------------
	def set_transitionFrames(self, value):
		"""
		
				Specify te number of transition frames for animate transitions.
				
		"""
		self.edit(transitionFrames=value)
	#----------------------------------------------------------------------
	transitionFrames = property(get_transitionFrames, set_transitionFrames)
	#----------------------------------------------------------------------
	def unParent(self,value):
		"""
		
				Specifies that the editor should be removed from its layout.
				This cannot be used in query mode.
				
		"""
		self.edit(unParent=value)
	#----------------------------------------------------------------------
	def unfold(self,value):
		"""
		
				Unfolds (expands) selected object.
				
		"""
		self.edit(unfold=value)
	#----------------------------------------------------------------------
	def unfoldAll(self,value):
		"""
		
				Unfolds everything under selected object.
				
		"""
		self.edit(unfoldAll=value)
	#----------------------------------------------------------------------
	def unfoldAllShapes(self,value):
		"""
		
				Unfolds all shapes.
				
		"""
		self.edit(unfoldAllShapes=value)
	#----------------------------------------------------------------------
	def unfoldHidden(self,value):
		"""
		
				Unfolds all hidden objects.
				
		"""
		self.edit(unfoldHidden=value)
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
	def get_updateNodeAdded(self):
		"""
		
				Update graph when a new node is added to the database
				
		"""
		return self.query(updateNodeAdded=True)
	#----------------------------------------------------------------------
	def set_updateNodeAdded(self, value):
		"""
		
				Update graph when a new node is added to the database
				
		"""
		self.edit(updateNodeAdded=value)
	#----------------------------------------------------------------------
	updateNodeAdded = property(get_updateNodeAdded, set_updateNodeAdded)
	#----------------------------------------------------------------------
	def get_updateSelection(self):
		"""
		
				Update selection state in the graph when the selection state of
				database changes.
				
		"""
		return self.query(updateSelection=True)
	#----------------------------------------------------------------------
	def set_updateSelection(self, value):
		"""
		
				Update selection state in the graph when the selection state of
				database changes.
				
		"""
		self.edit(updateSelection=value)
	#----------------------------------------------------------------------
	updateSelection = property(get_updateSelection, set_updateSelection)
	#----------------------------------------------------------------------
	def upstream(self,value):
		"""
		
				Show upstream dependency graph of selected node(s).
				
		"""
		self.edit(upstream=value)
	#----------------------------------------------------------------------
	def useDrawOverrideColor(self,value):
		"""
		
				Specify whether or not to use draw override coloring.
				
		"""
		self.edit(useDrawOverrideColor=value)
	#----------------------------------------------------------------------
	def get_useFeedbackList(self):
		"""
		
				Use feedback or highlight list as the target selection when
				processing other hypergraph command-line options.
				
		"""
		return self.query(useFeedbackList=True)
	#----------------------------------------------------------------------
	def set_useFeedbackList(self, value):
		"""
		
				Use feedback or highlight list as the target selection when
				processing other hypergraph command-line options.
				
		"""
		self.edit(useFeedbackList=value)
	#----------------------------------------------------------------------
	useFeedbackList = property(get_useFeedbackList, set_useFeedbackList)
	#----------------------------------------------------------------------
	def get_viewOption(self):
		"""
		
				Set or query the view option for this hyper graph editor.
				The currently allowed views are "asIcons" and "asList".
				
		"""
		return self.query(viewOption=True)
	#----------------------------------------------------------------------
	def set_viewOption(self, value):
		"""
		
				Set or query the view option for this hyper graph editor.
				The currently allowed views are "asIcons" and "asList".
				
		"""
		self.edit(viewOption=value)
	#----------------------------------------------------------------------
	viewOption = property(get_viewOption, set_viewOption)
	#----------------------------------------------------------------------
	def visibility(self,value):
		"""
		
				Set the visible state of the selected node(s).
				
		"""
		self.edit(visibility=value)
	#----------------------------------------------------------------------
	def zoom(self,value):
		"""
		
				Specify the zoom factor for animating transitions
				
		"""
		self.edit(zoom=value)