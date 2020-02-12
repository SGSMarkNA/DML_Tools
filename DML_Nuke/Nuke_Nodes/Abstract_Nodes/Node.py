
import nuke
from ..Vec2 import Vector2
from ..Base_Nodes.API_Node import DML_Node
from ...Decorators.Node_Wraper_Manager import node_Return_Wrapper,nuke_Object_Return_Wrapper,knob_Return_Wrapper,standerdized_item_list

########################################################################
class Node_Connection_Types(object):
	""""""		
	expressions    = nuke.EXPRESSIONS
	visible_inputs = nuke.INPUTS
	hidden_inputs  = nuke.HIDDEN_INPUTS

##----------------------------------------------------------------------
#def maximumInputs(self):
	#"""
		#self.maximumInputs() -> Maximum number of inputs this node can have.

		#@return: Maximum number of inputs this node can have.

	#"""
	#return self.nuke_node.maximumInputs()
	
#----------------------------------------------------------------------
def down_stream_nodes(node,matchclass=None,nlist=None):
	if nlist == None:
		nlist = []
	if matchclass is not None:
		if node.Class() == matchclass:
			nlist.append(node)
	else:
		nlist.append(node)
	if node.Class() == "Group":
		dependent = nuke.allNodes("Input",node)
	else:
		dependent = node.dependent()
	for n in dependent:
		down_stream_nodes(n,matchclass,nlist)
	return nlist
	
#===============================================================================
def find_upstream_node(startnode,matchclass):
	"""
	In the simplest way possible, this function will go upstream and find
	the first node matching the specified class.
	"""
	isinstance(startnode,nuke.Node)
	if  startnode.Class() == matchclass:
		return startnode
	else:
		if startnode.Class() == 'Input':
			try:
				grp = nuke.toNode(startnode.fullName().split(".",1)[0])
				startnode = grp
			except:
				pass
		for node in startnode.dependencies(nuke.INPUTS):
			scan = find_upstream_node(node,matchclass)
			if scan != None:
				return scan
	return None
########################################################################
class Node(DML_Node):
	NODE_TYPE_RELATION        = "default"
	NODE_CONNECTION_TYPES     = Node_Connection_Types
	#----------------------------------------------------------------------
	def delete(self):
		"""delete this node"""
		nuke.delete(self.nuke_object)
	#----------------------------------------------------------------------
	def Disconnect_All_Dependencies(self):
		""""""
		while len(self.nuke_object.dependencies()):
			for i in range(self.inputs):
				self.setInput(i, None)
	#----------------------------------------------------------------------
	def Disconnect_All_Dependent(self):
		for n in self.dependent():
			for i in range(n.inputs):
				if n.input(i) == n:
					n.setInput(i,None)
	#----------------------------------------------------------------------
	def hasKnob(self,name):
		"""
			self.hasKnob(name) -> bool.

			check if this node has a knob with name.

			@param name: string.

			@return: bool.

		"""
		return name in self.nuke_object.knobs()
	#----------------------------------------------------------------------
	def addKnob(self,*args,**kwargs):
		"""
			self.addKnob(k) -> None.

			Add knob k to this node or panel.

			@param k: Knob.

			@return: None.

		"""
		return self.nuke_object.addKnob(*args,**kwargs)
	#----------------------------------------------------------------------
	@knob_Return_Wrapper
	def allKnobs(self):
		"""
			self.allKnobs() -> list

			Get a list of all knobs in this node, including nameless knobs.

			For example:

			   >>> b = nuke.nodes.Blur()

			   >>> b.allKnobs()

			@return: List of all knobs.

			Note that this doesn't follow the links for Link_Knobs

		"""
		return self.nuke_object.allKnobs()
	#----------------------------------------------------------------------
	def autoplace(self):
		"""
			self.autoplace() -> None.

			Automatically place nodes, so they do not overlap.

			@return: None.

		"""
		return self.nuke_object.autoplace()
	#----------------------------------------------------------------------
	@nuke_Object_Return_Wrapper
	def bbox(self):
		"""
			self.bbox() -> List of x, y, w, h.

			Bounding box of the node.

			@return: List of x, y, w, h.

		"""
		return self.nuke_object.bbox()
	#----------------------------------------------------------------------
	def canSetInput(self,i, node):
		"""
			self.canSetInput(i, node) -> bool

			Check whether the output of 'node' can be connected to input i. 

			@param i: Input number.

			@param node: The node to be connected to input i.

			@return: True if node can be connected, False otherwise.

		"""
		return self.nuke_object.canSetInput(i, node)
	#----------------------------------------------------------------------
	def connectInput(self,i, node):
		"""
			self.connectInput(i, node) -> bool

			Connect the output of 'node' to the i'th input or the next available unconnected input. The requested input is tried first, but if it is already set then subsequent inputs are tried until an unconnected one is found, as when you drop a connection arrow onto a node in the GUI.

			@param i: Input number to try first.

			@param node: The node to connect to input i.

			@return: True if a connection is made, False otherwise.

		"""
		return self.nuke_object.connectInput(i, node)
	#----------------------------------------------------------------------
	def deepSample(self,*args,**kwargs):
		"""
			self.deepSample(c, x, y, n) -> Floating point value.

			Return pixel values from a deep image.

			This requires the image to be calculated, so performance may be very bad if this is placed into an expression in

			a control panel.

			@param c: Channel name.

			@param x: Position to sample (X coordinate).

			@param y: Position to sample (Y coordinate).

			@param n: Sample index (between 0 and the number returned by deepSampleCount() for this pixel, or -1 for the frontmost).

			@return: Floating point value.

		"""
		return self.nuke_object.deepSample(*args,**kwargs)
	#----------------------------------------------------------------------
	def deepSampleCount(self,*args,**kwargs):
		"""
			self.deepSampleCount(x, y) -> Integer value.

			Return number of samples for a pixel on a deep image.

			This requires the image to be calculated, so performance may be very bad if this is placed into an expression in

			a control panel.

			@param x: Position to sample (X coordinate).

			@param y: Position to sample (Y coordinate).

			@return: Integer value.

		"""
		return self.nuke_object.deepSampleCount(*args,**kwargs)
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def dependencies(self,what=nuke.EXPRESSIONS | nuke.INPUTS | nuke.HIDDEN_INPUTS):
		"""
			self.dependencies(what) -> List of nodes.

			List all nodes referred to by this node. 'what' is an optional integer (see below).

			You can use the following constants or'ed together to select what types of dependencies are looked for:

			         nuke.EXPRESSIONS = expressions

			         nuke.INPUTS = visible input pipes

			         nuke.HIDDEN_INPUTS = hidden input pipes.

			The default is to look for all types of connections.

			Example:

			nuke.toNode('Blur1').dependencies( nuke.INPUTS | nuke.EXPRESSIONS )

			@param what: Or'ed constant of nuke.EXPRESSIONS, nuke.INPUTS and nuke.HIDDEN_INPUTS to select the types of dependencies. The default is to look for all types of connections.

			@return: List of nodes.

		"""
		return self.nuke_object.dependencies(what)
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def dependent(self,what=nuke.EXPRESSIONS | nuke.INPUTS | nuke.HIDDEN_INPUTS,forceEvaluate=True):
		"""
			self.dependent(what, forceEvaluate) -> List of nodes.

			List all nodes that read information from this node.  'what' is an optional integer:

			         You can use any combination of the following constants or'ed together to select what types of dependent nodes to look for:

			                 nuke.EXPRESSIONS = expressions

			                 nuke.INPUTS = visible input pipes

			                 nuke.HIDDEN_INPUTS = hidden input pipes.

			The default is to look for all types of connections.

			forceEvaluate is an optional boolean defaulting to True. When this parameter is true, it forces a re-evaluation of the entire tree. 

			This can be expensive, but otherwise could give incorrect results if nodes are expression-linked. 

			Example:

			nuke.toNode('Blur1').dependent( nuke.INPUTS | nuke.EXPRESSIONS )

			@param what: Or'ed constant of nuke.EXPRESSIONS, nuke.INPUTS and nuke.HIDDEN_INPUTS to select the types of dependent nodes. The default is to look for all types of connections.

			@param forceEvaluate: Specifies whether a full tree evaluation will take place. Defaults to True.

			@return: List of nodes.

		"""
		return self.nuke_object.dependent(what=what,forceEvaluate=forceEvaluate)
	#----------------------------------------------------------------------
	def error(self):
		"""
			error() -> bool

			True if the node or any in its input tree have an error, or False otherwise.

			Error state of the node and its input tree.  Deprecated; use hasError or treeHasError instead.

			Note that this will always return false for viewers, which cannot generate their input trees.  Instead, choose an input of the viewer (e.g. the active one), and call treeHasError() on that.

		"""
		return self.nuke_object.error()
	#----------------------------------------------------------------------
	def fileDependencies(self,start, end):
		"""
			self.fileDependencies(start, end) -> List of nodes and filenames.

			@param start: first frame

			@param end: last frame

			Returns the list of input file dependencies for this node and all nodes upstream from this node for the given frame range.

			The file dependencies are calcuated by searching for Read ops or ops with a File knob.

			All views are considered and current proxy mode is used to decide on whether full format or proxy files are returned.

			Note that Write nodes files are also included but precomps, gizmos and external plugins are not.

			Any time shifting operation such as frameholds, timeblurs, motionblur etc are taken into consideration.

			@return The return list is a list of nodes and files they require.

			Eg.  [Read1, ['file1.dpx, file2.dpx'] ], [Read2, ['file3.dpx', 'file4.dpx'] ] ]

		"""
		return self.nuke_object.fileDependencies(*args,**kwargs)
	#----------------------------------------------------------------------
	def forceValidate(self):
		"""
			self.forceValidate() -> None

			Force the node to validate itself, updating its hash.

		"""
		return self.nuke_object.forceValidate()
	#----------------------------------------------------------------------
	def hasError(self):
		"""
			hasError() -> bool

			True if the node itself has an error, regardless of the state of the ops in its input tree, or False otherwise.

			Error state of the node itself, regardless of the state of the ops in its input tree.

			Note that an error on a node may not appear if there is an error somewhere in its input tree, because it may not be possible to validate the node itself correctly in that case.

		"""
		return self.nuke_object.hasError()
	#----------------------------------------------------------------------
	def help(self):
		"""
			self.help() -> str

			@return: Help for the node.

		"""
		return self.nuke_object.help()
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def input(self,i):
		"""
			self.input(i) -> The i'th input.

			@param i: Input number.

			@return: The i'th input.

		"""
		return self.nuke_object.input(i)
	#----------------------------------------------------------------------
	@knob_Return_Wrapper
	def knob(self,val):
		"""
			self.knob(p) -> The knob named p or the pth knob.

			@param p: A string or an integer.

			@return: The knob named p or the pth knob.

			Note that this follows the links for Link_Knobs

		"""
		res = self.nuke_object.knobs().get(val,None)
		isinstance(res,nuke.Knob)
		return res
	#----------------------------------------------------------------------
	@knob_Return_Wrapper
	def knobs(self):
		"""
			self.knobs() -> dict

			Get a dictionary of (name, knob) pairs for all knobs in this node.

			For example:

			   >>> b = nuke.nodes.Blur()

			   >>> b.knobs()

			@return: Dictionary of all knobs.

			Note that this doesn't follow the links for Link_Knobs

		"""
		res = self.nuke_object.knobs()
		isinstance(res,dict)
		return res
	#----------------------------------------------------------------------
	def linkableKnobs(self,*args):
		"""
			self.linkableKnobs(knobType) -> List

			Returns a list of any knobs that may be linked to from the node as well as some meta information about the knob. This may include whether the knob is enabled and whether it should be used for absolute or relative values. Not all of these variables may make sense for all knobs..

			@param knobType A KnobType describing the type of knobs you want.@return: A list of LinkableKnobInfo that may be empty .

		"""
		return self.nuke_object.linkableKnobs(*args)
	#----------------------------------------------------------------------
	def metadata(self,**kwargs):
		"""
			self.metadata(key, time, view) -> value or dict

			Return the metadata item for key on this node at current output context, or at optional time and view.

			If key is not specified a dictionary containing all key/value pairs is returned.

			None is returned if key does not exist on this node.

			@param key: Optional name of the metadata key to retrieve.

			@param time: Optional time to evaluate at (default is taken from node's current output context).

			@param view: Optional view to evaluate at (default is taken from node's current output context).

			@return: The requested metadata value, a dictionary containing all keys if a key name is not provided, or None if the specified key is not matched.

		"""
		return self.nuke_object.metadata(**kwargs)
	#----------------------------------------------------------------------
	def opHashes(self):
		"""
			self.opHashes() -> list of int

			Returns a list of hash values, one for each op in this node.

		"""
		return self.nuke_object.opHashes()
	#----------------------------------------------------------------------
	def performanceInfo(self):
		"""
			self.performanceInfo( category ) -> Returns performance information for this node. Performance timing must be enabled.

			@category: performance category ( optional ).A performance category, must be either nuke.PROFILE_STORE, nuke.PROFILE_VALIDATE, nuke.PROFILE_REQUEST or nuke.PROFILE_ENGINE The default is nuke.PROFILE_ENGINE which gives the performance info of the render engine.

			@return: A dictionary containing the cumulative performance info for this category, where:

			callCount = the number of calls made

			timeTakenCPU =  the CPU time spent in microseconds

			timeTakenWall = the actual time ( wall time ) spent in microseconds

		"""
		return self.nuke_object.performanceInfo()
	#----------------------------------------------------------------------
	def readKnobs(self,*args,**kwargs):
		"""
			self.readKnobs(s) -> None.

			Read the knobs from a string (TCL syntax).

			@param s: A string.

			@return: None.

		"""
		return self.nuke_object.readKnobs(*args,**kwargs)
	#----------------------------------------------------------------------
	def redraw(self):
		"""
			self.redraw() -> None.

			Force a redraw of the node.

			@return: None.

		"""
		return self.nuke_object.redraw()
	#----------------------------------------------------------------------
	def removeKnob(self,*args,**kwargs):
		"""
			self.removeKnob(k) -> None.

			Remove knob k from this node or panel. Throws a ValueError exception if k is not found on the node.

			@param k: Knob.

			@return: None.

		"""
		return self.nuke_object.removeKnob(*args,**kwargs)
	#----------------------------------------------------------------------
	def resetKnobsToDefault(self):
		"""
			self.resetKnobsToDefault() -> None

			Reset all the knobs to their default values.

		"""
		return self.nuke_object.resetKnobsToDefault()
	#----------------------------------------------------------------------
	def running(self):
		"""
			self.running() -> Node rendering when paralled threads are running or None.

			Class method.

			@return: Node rendering when paralled threads are running or None.

		"""
		return self.nuke_object.running()
	#----------------------------------------------------------------------
	def sample(self,*args,**kwargs):
		"""
			self.sample(c, x, y, dx, dy) -> Floating point value.

			Return pixel values from an image.

			This requires the image to be calculated, so performance may be very bad if this is placed into an expression in

			a control panel. Produces a cubic filtered result. Any sizes less than 1, including 0, produce the same filtered result,

			this is correct based on sampling theory. Note that integers are at the corners of pixels, to center on a pixel add .5 to both coordinates.

			If the optional dx,dy are not given then the exact value of the square pixel that x,y lands in is returned. This is also called 'impulse filtering'.

			@param c: Channel name.

			@param x: Centre of the area to sample (X coordinate).

			@param y: Centre of the area to sample (Y coordinate).

			@param dx: Optional size of the area to sample (X coordinate).

			@param dy: Optional size of the area to sample (Y coordinate).

			@param frame: Optional frame to sample the node at.

			@return: Floating point value.

		"""
		return self.nuke_object.sample(*args,**kwargs)
	#----------------------------------------------------------------------
	def selectOnly(self):
		"""
			self.selectOnly() -> None.

			Set this node to be the only selection, as if it had been clicked in the DAG.

			@return: None.

		"""
		return self.nuke_object.selectOnly()
	#----------------------------------------------------------------------
	def setInput(self,i, node):
		"""
			self.setInput(i, node) -> bool

			Connect input i to node if canSetInput() returns true.

			@param i: Input number.

			@param node: The node to connect to input i.

			@return: True if canSetInput() returns true, or if the input is already correct.

		"""
		return self.nuke_object.setInput(i, standerdized_item_list(node))
	#----------------------------------------------------------------------
	def setTab(self,tabIndex):
		"""
			self.setTab(tabIndex) -> None

			@param tabIndex: The tab to show (first is 0).

			@return: None

		"""
		return self.nuke_object.setTab(tabIndex)
	#----------------------------------------------------------------------
	def setXYpos(self,*args):
		"""
			self.setXYpos(number, number) -> None.
			self.setXYpos([number, number]) -> None.
			self.setXYpos(Vector2) -> None.

			Set the x, y position of node in node graph.

			@param args: number,number | [number,number] | Vector2

			@return: None.

		"""
		if len(args) == 1:
			if isinstance(args[0],Vector2.__base__):
				x,y = [args[0].x, args[0].y]
			elif isinstance(args[0],(list,tuple)):
				x,y = args[0]
		elif len(args) == 2:
			x,y = args
		self.nuke_object.setXYpos(int(x),int(y))
	#----------------------------------------------------------------------
	def getXYpos(self):
		"""
			self.getXYpos() -> Vector2.
			
			@return: Vector2.

		"""
		return Vector2(self)
	#----------------------------------------------------------------------
	def setXpos(self,x):
		"""
			self.setXpos(x) -> None.

			Set the x position of node in node graph.

			@param x: The x position of node in node graph.

			@return: None.

		"""
		return self.nuke_object.setXpos(int(x))
	#----------------------------------------------------------------------
	def setYpos(self,y):
		"""
			self.setYpos(y) -> None.

			Set the y position of node in node graph.

			@param y: The y position of node in node graph.

			@return: None.

		"""
		return self.nuke_object.setYpos(int(y))
	#----------------------------------------------------------------------
	def showControlPanel(self,*args,**kwargs):
		"""
			self.showControlPanel(forceFloat = false) -> None

			@param forceFloat: Optional python object. If it evaluates to True the control panel will always open as a floating panel. Default is False.

			@return: None

		"""
		return self.nuke_object.showControlPanel(*args,**kwargs)
	#----------------------------------------------------------------------
	def hideControlPanel(self):
		"""
			self.hideControlPanel() -> None

			@return: None

		"""
		return self.nuke_object.hideControlPanel()
	#----------------------------------------------------------------------
	def shown(self):
		"""
			self.shown() -> true if the properties panel is open. This can be used to skip updates that are not visible to the user.

			@return: true if the properties panel is open. This can be used to skip updates that are not visible to the user.

		"""
		return self.nuke_object.shown()	
	#----------------------------------------------------------------------
	def showInfo(self,s):
		"""
			self.showInfo(s) -> None.

			Creates a dialog box showing the result of script s.

			@param s: A string.

			@return: None.

		"""
		return self.nuke_object.showInfo(s)
	#----------------------------------------------------------------------
	def treeHasError(self):
		"""
			treeHasError() -> bool

			True if the node or any in its input tree have an error, or False otherwise.

			Error state of the node and its input tree.

			Note that this will always return false for viewers, which cannot generate their input trees.  Instead, choose an input of the viewer (e.g. the active one), and call treeHasError() on that.

		"""
		return self.nuke_object.treeHasError()
	#----------------------------------------------------------------------
	def upstreamFrameRange(self,*args):
		"""
			self.upstreamFrameRange(i) -> FrameRange

			Frame range for the i'th input of this node.

			@param i: Input number.

			@return: FrameRange. Returns None when querying an invalid input.

		"""
		return self.nuke_object.upstreamFrameRange(*args)
	#----------------------------------------------------------------------
	def writeKnobs(self,i=nuke.TO_SCRIPT | nuke.TO_VALUE):
		"""
			self.writeKnobs(i) -> String in .nk form.

			Return a tcl list. If TO_SCRIPT | TO_VALUE is not on, this is a simple list

			of knob names. If it is on, it is an alternating list of knob names

			and the output of to_script().

			Flags can be any of these or'd together:

			- nuke.TO_SCRIPT produces to_script(0) values

			- nuke.TO_VALUE produces to_script(context) values

			- nuke.WRITE_NON_DEFAULT_ONLY skips knobs with not_default() false

			- nuke.WRITE_USER_KNOB_DEFS writes addUserKnob commands for user knobs

			- nuke.WRITE_ALL writes normally invisible knobs like name, xpos, ypos

			@param i: The set of flags or'd together. Default is TO_SCRIPT | TO_VALUE.

			@return: String in .nk form.

		"""
		return self.nuke_object.writeKnobs(i)
	#----------------------------------------------------------------------
	def xpos(self):
		"""
			self.xpos() -> X position of node in node graph.

			@return: X position of node in node graph.

		"""
		return self.nuke_object.xpos()
	#----------------------------------------------------------------------
	def ypos(self):
		"""
			self.ypos() -> Y position of node in node graph.

			@return: Y position of node in node graph.

		"""
		return self.nuke_object.ypos()
	#----------------------------------------------------------------------
	def view_In_Active_Viewer(self):
		""""""
		active_view = nuke.activeViewer()
		active_view_node = active_view.node()
		active_view_node.setInput(0,self.nuke_object)
		active_view.activateInput(0)
		
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def find_Upstream_Node(self,matchClass):
		""""""
		return find_upstream_node(self.nuke_object, matchClass)
	
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def find_Down_Stream_Nodes(self,matchclass=None):
		""""""
		return down_stream_nodes(self.nuke_object,matchclass=matchclass,nlist=None)

	#----------------------------------------------------------------------
	def __getitem__(self,item):
		""""""
		return self.knobs().get(item,None)
	#----------------------------------------------------------------------
	y  = property(fget=ypos, fset=setYpos)
	x  = property(fget=xpos, fset=setXpos)
	xy = property(fget=getXYpos, fset=setXYpos)
		