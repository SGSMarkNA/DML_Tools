
import nuke
from ..Base_Nodes import DML_Nuke_Object

################################################################################
class ProgressTask(DML_Nuke_Object):
	#----------------------------------------------------------------------
	def setProgress(self,i):
		"""self.setProgress(i) -> None.  i is an integer representing the current progress"""
		return self.nuke_object.setProgress(i)
	#----------------------------------------------------------------------
	def isCancelled(self):
		"""self.isCancelled() -> True if the user has requested the task to be cancelled. """
		return self.nuke_object.isCancelled()
	#----------------------------------------------------------------------
	def setMessage(self,s):
		"""self.setMessage(s) -> None.  set the message for the progress task"""
		return self.nuke_object.setMessage(s)
