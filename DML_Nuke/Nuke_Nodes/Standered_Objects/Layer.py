import nuke
from ..Base_Nodes import DML_Nuke_Object

################################################################################
class Layer(DML_Nuke_Object):
	#----------------------------------------------------------------------
	def setName(self,newName):
		"""self.setName(newName) -> None Set the name of this layer.  @param newName: The new name for this layer."""
		return self.nuke_object.setName(newName)
	#----------------------------------------------------------------------
	def channels(self):
		"""self.channels() -> [string, ...] Get a list of the channels in this layer.  @return: A list of strings, where each string is the name of a channel in this layer."""
		return self.nuke_object.channels()
	#----------------------------------------------------------------------
	def visible(self):
		"""self.visible() -> bool Check whether the layer is visible.  @return: True if visible, False if not."""
		return self.nuke_object.visible()
	#----------------------------------------------------------------------
	def name(self):
		"""self.name() -> str Get the layer name.  @return: The layer name, as a string."""
		return self.nuke_object.name()
