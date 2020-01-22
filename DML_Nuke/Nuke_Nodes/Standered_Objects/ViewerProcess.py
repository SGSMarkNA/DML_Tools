import nuke
from ..Base_Nodes import DML_Nuke_Object

################################################################################
class ViewerProcess(DML_Nuke_Object):
	#----------------------------------------------------------------------
	def unregister(self,name):
		"""nuke.ViewerProcess.unregister(name) -> None. Unregister a ViewerProcess. This is a class method. @param name: Menu name. @return: None."""
		return self.nuke_object.unregister(name)
	#----------------------------------------------------------------------
	def node(self):
		"""nuke.ViewerProcess.node(name, viewer) -> Node. Returns a ViewerProcess node. Default is to return the current selected one. This is a class method. @param name: Optional ViewerProcess name. @param viewer: Optional viewer name. @return: Node."""
		return self.nuke_object.node()
	#----------------------------------------------------------------------
	def register(self):
		"""nuke.ViewerProcess.register(name, call, args, kwargs) -> None. Register a ViewerProcess. This is a class method. @param name: Menu name. @param call: Python callable. Must return a Node. @param args: Arguments to call. @param kwargs: Optional named arguments. @return: None."""
		return self.nuke_object.register()
	#----------------------------------------------------------------------
	def registeredNames(self):
		"""nuke.ViewerProcess.registeredNames() -> List. Returns a list containing the names of all currently regisered ViewerProcesses. @return: List."""
		return self.nuke_object.registeredNames()
