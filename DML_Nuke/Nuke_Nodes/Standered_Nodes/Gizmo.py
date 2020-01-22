import nuke
from .Group import Group
	
################################################################################
class Gizmo(Group):
	NODE_TYPE_RELATION  = "Gizmo"
	def filename(self):
		"""self.filename() -> String. Gizmo filename. @return: String."""
		return self.nuke_object.filename()
	#----------------------------------------------------------------------
	def command(self):
		"""self.command() -> String. Gizmo command. @return: String."""
		return self.nuke_object.command()
	#----------------------------------------------------------------------
	def makeGroup(self):
		"""self.makeGroup() -> Group Creates a Group node copy of the Gizmo node. @return: Group."""
		return self.nuke_object.makeGroup()
