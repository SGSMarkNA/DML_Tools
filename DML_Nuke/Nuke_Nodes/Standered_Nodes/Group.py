
import nuke
from ..Abstract_Nodes import Node

################################################################################
class Group(Node):
	NODE_TYPE_RELATION        = "Group"
	#----------------------------------------------------------------------
	def begin(self):
		"""
			self.begin() -> Group.

			All python code that follows will be executed in the context of node. All names are evaluated relative to this object. Must be paired with end.

			@return: Group.

		"""
		return self.nuke_object.begin()
	#----------------------------------------------------------------------
	def connectSelectedNodes(self,*args,**kwargs):
		"""
			self.connectSelectedNodes(backward, inputA) -> None.

			Connect the selected nodes.

			@param backward.

			@param inputA.

			@return: None.

		"""
		return self.nuke_object.connectSelectedNodes(*args,**kwargs)
	#----------------------------------------------------------------------
	def end(self):
		"""
			self.end() -> None.

			All python code that follows will no longer be executed in the context of node. Must be paired with begin.

			@return: None.

		"""
		return self.nuke_object.end()
	#----------------------------------------------------------------------
	def expand(self):
		"""
			self.expand() -> None.

			Moves all nodes from the group node into its parent group, maintaining node input

			and output connections, and deletes the group.

			Returns the nodes that were moved, which will also be selected.

			@return: None.

		"""
		return self.nuke_object.expand()
	#----------------------------------------------------------------------
	def node(self,*args,**kwargs):
		"""
			self.node(s) -> Node with name s or None.

			Locate a node by name.

			@param s: A string.

			@return: Node with name s or None.

		"""
		return self.nuke_object.node(*args,**kwargs)
	#----------------------------------------------------------------------
	def nodes(self):
		"""
			self.nodes() -> List of nodes

			List of nodes in group.

			@return: List of nodes

		"""
		return self.nuke_object.nodes()
	#----------------------------------------------------------------------
	def numNodes(self):
		"""
			self.numNodes() -> Number of nodes

			Number of nodes in group.

			@return: Number of nodes

		"""
		return self.nuke_object.numNodes()
	#----------------------------------------------------------------------
	def output(self):
		"""
			self.output() -> Node or None.

			Return output node of group.

			@return: Node or None.

		"""
		return self.nuke_object.output()
	#----------------------------------------------------------------------
	def run(self,*args,**kwargs):
		"""
			self.run(callable) -> Result of callable.

			Execute in the context of node. All names are evaluated relative to this object.

			@param callable: callable to execute.

			@return: Result of callable.

		"""
		return self.nuke_object.run(*args,**kwargs)
	#----------------------------------------------------------------------
	def selectedNode(self):
		"""
			self.selectedNode() -> Node or None.

			Returns the node the user is most likely thinking about. This is the last node the user clicked on, if it is selected.  Otherwise it is an 'output' (one with no selected outputs) of the set of selected nodes. If no nodes are selected then None is returned.

			@return: Node or None.

		"""
		return self.nuke_object.selectedNode()
	#----------------------------------------------------------------------
	def selectedNodes(self):
		"""
			self.selectedNodes() -> Node or None.

			Selected nodes.

			@return: Node or None.

		"""
		return self.nuke_object.selectedNodes()
	#----------------------------------------------------------------------
	def splaySelectedNodes(self,*args,**kwargs):
		"""
			self.splaySelectedNodes(backward, inputA) -> None.

			Splay the selected nodes.

			@param backward.

			@param inputA.

			@return: None.

		"""
		return self.nuke_object.splaySelectedNodes(*args,**kwargs)

	#----------------------------------------------------------------------
	def __enter__(self):
		""""""
		self.nuke_object.begin()
	#----------------------------------------------------------------------
	def __exit__(self,exc_type, exc_value, traceback):
		""""""
		self.nuke_object.end()