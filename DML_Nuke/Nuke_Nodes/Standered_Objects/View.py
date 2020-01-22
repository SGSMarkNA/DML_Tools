import nuke
from ..Base_Nodes import DML_Nuke_Object

################################################################################
class View(DML_Nuke_Object):
	#----------------------------------------------------------------------
	def __str__(self):
		"""x.__str__() <==> str(x)"""
		return self.nuke_object.__str__()
	#----------------------------------------------------------------------
	def value(self):
		"""self.value() -> Value of view. @return: Value of view."""
		return self.nuke_object.value

	#----------------------------------------------------------------------
	def string(self):
		"""self.string() -> Name of view. @return: Name of view."""
		return self.nuke_object.string()
