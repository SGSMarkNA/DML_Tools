import nuke
from .Group import Group
	
################################################################################
class Precomp(Group):
	NODE_TYPE_RELATION  = "Precomp"
	#----------------------------------------------------------------------
	def reload(self):
		"""self.reload() -> None Precomp Node reload() @return: None"""
		return self.nuke_object.reload()
