import nuke
from .String_Knob import String_Knob

################################################################################
class Script_Knob(String_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "Script_Knob"
	#----------------------------------------------------------------------
	def execute(self):
		"""self.execute() -> None Execute the command. @return: None."""
		return self.nuke_object.execute()
	#----------------------------------------------------------------------
	def setValue(self,cmd):
		"""self.setValue(cmd) -> None Set the new command for this knob. @param cmd: String containing a TCL command. @return: None."""
		return self.nuke_object.setValue(cmd)
	#----------------------------------------------------------------------
	def value(self):
		"""self.value() -> str  Get the current command. @return: The current command as a string, or None if there is no current command."""
		return self.nuke_object.value()
	#----------------------------------------------------------------------
	def command(self):
		"""self.command() -> str  Get the current command. @return: The current command as a string, or None if there is no current command."""
		return self.nuke_object.command()
	#----------------------------------------------------------------------
	def setCommand(self,cmd):
		"""self.setCommand(cmd) -> None Set the new command for this knob. @param cmd: String containing a TCL command. @return: None."""
		return self.nuke_object.setCommand(cmd)
