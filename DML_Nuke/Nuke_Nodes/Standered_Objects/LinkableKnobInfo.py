import nuke
from ..Base_Nodes import DML_Nuke_Object

################################################################################
class LinkableKnobInfo(DML_Nuke_Object):
	#----------------------------------------------------------------------
	def knob(self):
		"""self.knob() -> Knob Returns the knob that may be linked to."""
		return self.nuke_object.knob()
	#----------------------------------------------------------------------
	def displayName(self):
		"""self.displayName() -> String Returns the custom display name that will appear in Link-to menus."""
		return self.nuke_object.displayName()
	#----------------------------------------------------------------------
	def enabled(self):
		"""self.enabled() -> Boolean Returns whether the knob is currently enabled or not."""
		return self.nuke_object.enabled()
	#----------------------------------------------------------------------
	def indices(self):
		"""self.indices() -> List Returns a list of the knob channels that should be used with this linkable knob."""
		return self.nuke_object.indices()
	#----------------------------------------------------------------------
	def absolute(self):
		"""self.absolute() -> Boolean Returns whether the values of this knob should be treated as absolute or relative. This may be useful for positions."""
		return self.nuke_object.absolute()
