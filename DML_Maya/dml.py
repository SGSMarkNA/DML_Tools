import maya.cmds as cmds
import General_Utils
from Data_Storage import Cashed_Nodes_Container
__all__ = ["ls","selectedNodes","listConnections"]

from Decorators.Node_Wraper_Manager import node_Return_Wrapper,to_DML_Node,to_DML_Nodes

#----------------------------------------------------------------------
def clear_Node_Cash():
	""""""
	Cashed_Nodes_Container.clear()
#----------------------------------------------------------------------
@node_Return_Wrapper
def ls(*args,**kwargs):
	""""""
	#kwargs.pop("o",kwargs.pop("objectsOnly"))
	#kwargs["objectsOnly"]=True
	return cmds.ls(*args,**kwargs)
#----------------------------------------------------------------------
@node_Return_Wrapper
def selectedNodes():
	""""""
	return General_Utils.none_To_List(cmds.selectedNodes())
#----------------------------------------------------------------------
@node_Return_Wrapper
def listConnections(*args,**kwargs):
	""""""
	kwargs.pop("p",kwargs.pop("plugs"))
	kwargs["plugs"]=False
	return  General_Utils.none_To_List(cmds.listConnections( *args,**kwargs))