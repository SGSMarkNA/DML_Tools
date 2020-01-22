import nuke
from ..Base_Nodes import DML_Nuke_Object

################################################################################
class OutputContext(DML_Nuke_Object):
	#----------------------------------------------------------------------
	def viewcount(self):
		"""viewcount() -> int  Return number of views."""
		return self.nuke_object.viewcount()
	#----------------------------------------------------------------------
	def viewname(self,n):
		"""viewname(n) -> string  Return name of the view. The n argument is an integer in the range of 0 to number of views."""
		return self.nuke_object.viewname(n)
	#----------------------------------------------------------------------
	def setFrame(self,f):
		"""setFrame(f) -> True  Set frame value. The f argument is a float."""
		return self.nuke_object.setFrame(f)
	#----------------------------------------------------------------------
	def frame(self):
		"""frame() -> float  Return frame value."""
		return self.nuke_object.frame()
	#----------------------------------------------------------------------
	def setView(self,n):
		"""setView(n) -> True  Set view number. The n argument is an integer in the range of 0 to number of views."""
		return self.nuke_object.setView(n)
	#----------------------------------------------------------------------
	def viewshort(self,n):
		"""viewshort(n) -> string  Return short name of the view. The n argument is an integer in the range of 0 to number of views."""
		return self.nuke_object.viewshort(n)
	#----------------------------------------------------------------------
	def view(self):
		"""view() -> int  Return view number."""
		return self.nuke_object.view()
