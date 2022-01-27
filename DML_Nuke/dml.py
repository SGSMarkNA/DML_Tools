import nuke
__all__ = ["ls","selectedNodes","listConnections"]

from .Decorators.Node_Wraper_Manager import node_Return_Wrapper, to_DML_Node,to_DML_Nodes,to_DML_Knob

#----------------------------------------------------------------------
@node_Return_Wrapper
def selectedNodes(filter=None):
	""""""
	if filter is not None:
		return nuke.selectedNodes(filter)
	else:
		return nuke.selectedNodes()
#----------------------------------------------------------------------
@node_Return_Wrapper
def selectedNode():
	""""""
	return nuke.selectedNode()