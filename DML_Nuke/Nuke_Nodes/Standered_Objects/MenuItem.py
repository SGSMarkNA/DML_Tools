
import nuke
from ..Base_Nodes import DML_Nuke_Object

################################################################################
class MenuItem(DML_Nuke_Object):
	#----------------------------------------------------------------------
	def setEnabled(self,enabled):
		"""self.setEnabled(enabled) -> None Enable or disable the item. @param enabled: True to enable the object; False to disable it."""
		return self.nuke_object.setEnabled(enabled)
	#----------------------------------------------------------------------
	def name(self):
		"""self.name() -> String Returns the name of the menu item."""
		return self.nuke_object.name()
	#----------------------------------------------------------------------
	def invoke(self):
		"""self.invoke() -> None Perform the action associated with this menu item."""
		return self.nuke_object.invoke()
	#----------------------------------------------------------------------
	def script(self):
		"""self.script() -> String Returns the script that gets executed for this menu item."""
		return self.nuke_object.script()
	#----------------------------------------------------------------------
	def setScript(self,script):
		"""self.setScript(script) -> None Set the script to be executed for this menu item. Note: To call a python script file, you can use the execfile() function. i.e: menu.setScript("execfile('script.py')")"""
		return self.nuke_object.setScript(script)
	#----------------------------------------------------------------------
	def setShortcut(self,keySequence):
		"""self.setShortcut(keySequence) -> None Set the keyboard shortcut on this menu item. @param keySequence: the new shortcut in PortableText format, e.g. "Ctrl+Shift+P"""
		return self.nuke_object.setShortcut(keySequence)
	#----------------------------------------------------------------------
	def shortcut(self):
		"""self.shortcut() -> String Returns the keyboard shortcut on this menu item. The format of this is the PortableText format. It will return a string such as "Ctrl+Shift+P". Note that on Mac OS X the Command key is equivalent to Ctrl."""
		return self.nuke_object.shortcut()
	#----------------------------------------------------------------------
	def setIcon(self,icon):
		"""self.setIcon(icon) -> None Set the icon on this menu item. @param icon: the new icon as a path"""
		return self.nuke_object.setIcon(icon)
	#----------------------------------------------------------------------
	def icon(self):
		"""self.icon() -> String Returns the name of the icon on this menu item as path of the icon."""
		return self.nuke_object.icon()
