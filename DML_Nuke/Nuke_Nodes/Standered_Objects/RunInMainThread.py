
import nuke
from ..Base_Nodes import DML_Nuke_Object

################################################################################
class RunInMainThread(DML_Nuke_Object):
	#----------------------------------------------------------------------
	def request(self):
		""""""
		return self.nuke_object.request()
	#----------------------------------------------------------------------
	def result(self):
		""""""
		return self.nuke_object.result()
