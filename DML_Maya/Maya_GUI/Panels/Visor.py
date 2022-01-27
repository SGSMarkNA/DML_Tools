

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class Visor(UI_Object.UI):
	"""
	Command for the creation and manipulation of a Visor UI element. The Visor is
	used to display the contents of a scene (rendering related nodes in
	particular), as well as files on disk which the user may wish to bring into
	the scene (shader and texture libraries for example).
		  
	      render, hypergraph, shader, hypershade
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.visor(**kwargs)
			super(Visor, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.visor(name, exists=True):
				super(Visor, self).__init__(name)
			else:
				name = cmds.visor(name, **kwargs)
				super(Visor, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def addFolder(self):
		"""
		
				Add a new folder to the current visual browser
				
		"""
		return self.query(addFolder=True)
	#----------------------------------------------------------------------
	@property
	def addNodes(self):
		"""
		
				Add dependency graph nodes by name to a user defined custom folder.  The
				argument is a string encolsed in quotes with 1 one more node names
				seperated by blanks
				
		"""
		return self.query(addNodes=True)
	#----------------------------------------------------------------------
	@property
	def allowPanningInX(self):
		"""
		
				Specifies whether or not the user should be able to pan the contents of the
				visor horizontally. Default is true.
				
		"""
		return self.query(allowPanningInX=True)
	#----------------------------------------------------------------------
	@property
	def allowPanningInY(self):
		"""
		
				Specifies whether or not the user should be able to pan the contents of the
				visor vertically. Default is true.
				
		"""
		return self.query(allowPanningInY=True)
	#----------------------------------------------------------------------
	@property
	def allowZooming(self):
		"""
		
				Specifies whether or not the user should be able to zoom the contents of the
				visor. Default is true.
				
		"""
		return self.query(allowZooming=True)
	#----------------------------------------------------------------------
	@property
	def command(self):
		"""
		
				Mel command which will return a list of nodes to add to a folder
				
		"""
		return self.query(command=True)
	#----------------------------------------------------------------------
	@property
	def deleteFolder(self):
		"""
		
				Delete the specified folder and all of its children
				
		"""
		return self.query(deleteFolder=True)
	#----------------------------------------------------------------------
	@property
	def editFolder(self):
		"""
		
				Edit the name and MEL command for an existing folder
				
		"""
		return self.query(editFolder=True)
	#----------------------------------------------------------------------
	@property
	def folderList(self):
		"""
		
				Return a string array of the folders in the visor.
				
		"""
		return self.query(folderList=True)
	#----------------------------------------------------------------------
	@property
	def menu(self):
		"""
		
				Set the name of the script to run to get a popup menu
				
		"""
		return self.query(menu=True)
	#----------------------------------------------------------------------
	@property
	def name(self):
		"""
		
				Name of the new folder
				
		"""
		return self.query(name=True)
	#----------------------------------------------------------------------
	@property
	def nodeType(self):
		"""
		
				A node type used by folders of type nodeTypeInDAG
				
		"""
		return self.query(nodeType=True)
	#----------------------------------------------------------------------
	@property
	def openDirectories(self):
		"""
		
				When adding a new folder indicate if it sub directories will be show.
				The default is to not show sub directories.
				
		"""
		return self.query(openDirectories=True)
	#----------------------------------------------------------------------
	@property
	def openFolder(self):
		"""
		
				When adding a new folder indicate if it will be open or closed by default.
				The default is closed.
				
		"""
		return self.query(openFolder=True)
	#----------------------------------------------------------------------
	@property
	def parent(self):
		"""
		
				Parent folder of this folder
				
		"""
		return self.query(parent=True)
	#----------------------------------------------------------------------
	@property
	def path(self):
		"""
		
				Path to a file system directory to be displayed in the folder
				
		"""
		return self.query(path=True)
	#----------------------------------------------------------------------
	@property
	def popupMenuScript(self):
		"""
		
				Specifies the script to be called when the right mouse button is pressed in
				the visor. The name of the editor in which the right mouse button was pressed
				will be appended to the script at the time the script is called.
				
		"""
		return self.query(popupMenuScript=True)
	#----------------------------------------------------------------------
	@property
	def rebuild(self):
		"""
		
				Rebuild the visor after interactively adding a folder
				
		"""
		return self.query(rebuild=True)
	#----------------------------------------------------------------------
	@property
	def refreshAllSwatches(self):
		"""
		
				Refresh the swatches of all files currently displayed in this visor.
				
		"""
		return self.query(refreshAllSwatches=True)
	#----------------------------------------------------------------------
	@property
	def refreshSelectedSwatches(self):
		"""
		
				Refresh the swatches of all files currently selected in any visor.
				
		"""
		return self.query(refreshSelectedSwatches=True)
	#----------------------------------------------------------------------
	@property
	def refreshSwatch(self):
		"""
		
				Refresh the swatch of the file with the specified path.
				
		"""
		return self.query(refreshSwatch=True)
	#----------------------------------------------------------------------
	@property
	def reset(self):
		"""
		
				Clear all previously loaded folder descriptions in preperation for
				building a new visual browser
				
		"""
		return self.query(reset=True)
	#----------------------------------------------------------------------
	@property
	def restrictPanAndZoom(self):
		"""
		
				Specifies whether the panning and zooming of the visor should be
				restricted to keep the contents in the top left corner of the
				visor when they are smaller than the visible area within the visor.
				Default is true.
				
		"""
		return self.query(restrictPanAndZoom=True)
	#----------------------------------------------------------------------
	@property
	def saveSwatches(self):
		"""
		
				Save swatches to disk for currently displayed image files.
				
		"""
		return self.query(saveSwatches=True)
	#----------------------------------------------------------------------
	@property
	def scrollBar(self):
		"""
		
				Set the name of the scroll bar associated with visor
				
		"""
		return self.query(scrollBar=True)
	#----------------------------------------------------------------------
	@property
	def scrollPercent(self):
		"""
		
				Set the percentage value for the scroll bar.  Typically called from a
				a scroll bars callback.
				
		"""
		return self.query(scrollPercent=True)
	#----------------------------------------------------------------------
	@property
	def selectedGadgets(self):
		"""
		
				Return a string array of the currently selected gadgets (files, folders, nodes)
				in the visor.
				
		"""
		return self.query(selectedGadgets=True)
	#----------------------------------------------------------------------
	@property
	def showDividers(self):
		"""
		
				Specifies whether or not the visor should show dividers. The default is true.
				If -showDividers is set to false, dividers will be drawn as folders instead.
				
		"""
		return self.query(showDividers=True)
	#----------------------------------------------------------------------
	@property
	def showFiles(self):
		"""
		
				Specifies whether or not the visor should show files. The default is true.
				
		"""
		return self.query(showFiles=True)
	#----------------------------------------------------------------------
	@property
	def showFolders(self):
		"""
		
				Specifies whether or not the visor should show folders. The default is true.
				
		"""
		return self.query(showFolders=True)
	#----------------------------------------------------------------------
	@property
	def showNodes(self):
		"""
		
				Specifies whether or not the visor should show nodes. The default is true.
				
		"""
		return self.query(showNodes=True)
	#----------------------------------------------------------------------
	@property
	def stateString(self):
		"""
		
				Return the MEL command string to save the folder setup in visor
				
		"""
		return self.query(stateString=True)
	#----------------------------------------------------------------------
	@property
	def style(self):
		"""
		
				Set display style for the browser.  Options are:
				    outliner
				         A single column with an outliner style icon and a text label
				    singleColumn
				         A single column with an image style icon and a text label
				    multiColumn
				         A multiple column grid of swatches with the text label below the swatch
				
		"""
		return self.query(style=True)
	#----------------------------------------------------------------------
	@property
	def transform(self):
		"""
		
				Name of a transform node used by folders of type nodeTypeInDAG
				
		"""
		return self.query(transform=True)
	#----------------------------------------------------------------------
	@property
	def type(self):
		"""
		
				Type of the new folder.  Options are: 
				
				    command 
				         A mel command that will return a list of depend nodes that will
				         be displayed in the folder
				    connectedNodes 
				         The nodes connected to the specified node name will be displayed
				         in the folder
				    defaultNodes 
				         A mel command that will generate default node types.  These nodes
				         will not be part of the scene and are used for drag and drop
				         creation of new nodes that are in the scene.  The mel command
				         use with this type is usually "listNodetypes".
				    directory 
				        A directory name in the file system
				    directoryCommand 
				        A mel command that will return a directory name in the file system
				    folder 
				        An empty folder(the default value).  Empty folders can be used
				        as user defined folders by dropping dependency graph nodes in to them
				        nodeTypeInDAG 
				                List all nodes of a given type under a specified transforms in the
				                DAG.  For example list all the shaders for a character by specifying
				        the top transform of the character
				    shelfItems 
				        A directory containing mel files to use as shelf items
				
		"""
		return self.query(type=True)