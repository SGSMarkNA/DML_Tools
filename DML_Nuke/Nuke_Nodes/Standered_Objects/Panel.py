import nuke
from ..Base_Nodes import DML_Nuke_Object

################################################################################
class Panel(DML_Nuke_Object):
	#----------------------------------------------------------------------
	def addEnumerationPulldown(self):
		"""self.addEnumerationPulldown(name, value) -> True if successful. Add a pulldown menu to the panel. @param name: The name for the new knob. @param value: The initial value for the new knob. @return: True if successful."""
		return self.nuke_object.addEnumerationPulldown()
	#----------------------------------------------------------------------
	def show(self):
		"""self.show() -> An int value indicating how the dialog was closed (normally, or cancelled). Display the panel. @return: An int value indicating how the dialog was closed (normally, or cancelled)."""
		return self.nuke_object.show()
	#----------------------------------------------------------------------
	def setTitle(self,val):
		"""self.setTitle(val) -> True if successful. Set the current title for the panel. @param val: The title as a string. @return: True if successful."""
		return self.nuke_object.setTitle(val)
	#----------------------------------------------------------------------
	def addButton(self):
		"""self.addButton(name, value) -> True if successful. Add a button to the panel. @param name: The name for the new knob. @param value: The initial value for the new knob. @return: True if successful."""
		return self.nuke_object.addButton()
	#----------------------------------------------------------------------
	def addPasswordInput(self):
		"""self.addPasswordInput(name, value) -> True if successful. Add a password input knob to the panel. @param name: The name for the new knob. @param value: The initial value for the new knob. @return: True if successful."""
		return self.nuke_object.addPasswordInput()
	#----------------------------------------------------------------------
	def value(self,name):
		"""self.value(name) -> The value for the field if any, otherwise None. Get the value of a particular control in the panel. @param name: The name of the knob to get a value from. @return: The value for the field if any, otherwise None."""
		return self.nuke_object.value(name)
	#----------------------------------------------------------------------
	def setWidth(self,val):
		"""self.setWidth(val) -> True if successful. Set the width of the panel. @param val: The width as an int. @return: True if successful."""
		return self.nuke_object.setWidth(val)
	#----------------------------------------------------------------------
	def title(self):
		"""self.title() -> The title as a string. Get the current title for the panel. @return: The title as a string."""
		return self.nuke_object.title()
	#----------------------------------------------------------------------
	def addMultilineTextInput(self):
		"""self.addMultilineTextInput(name, value) -> True if successful. Add a multi-line text knob to the panel. @param name: The name for the new knob. @param value: The initial value for the new knob. @return: True if successful."""
		return self.nuke_object.addMultilineTextInput()
	#----------------------------------------------------------------------
	def width(self):
		"""self.width() -> The width as an int. Get the width of the panel. @return: The width as an int."""
		return self.nuke_object.width()
	#----------------------------------------------------------------------
	def addRGBColorChip(self):
		"""self.addRGBColorChip(name, value) -> True if successful. Add a color chooser to the panel. @param name: The name for the new knob. @param value: The initial value for the new knob. @return: True if successful."""
		return self.nuke_object.addRGBColorChip()
	#----------------------------------------------------------------------
	def addClipnameSearch(self):
		"""self.addClipnameSearch(name, value) -> True if successful. Add a clipname search knob to the panel. @param name: The name for the new knob. @param value: The initial value for the new knob. @return: True if successful."""
		return self.nuke_object.addClipnameSearch()
	#----------------------------------------------------------------------
	def addNotepad(self):
		"""self.addNotepad(name, value) -> True if successful. Add a text edit widget to the panel. @param name: The name for the new knob. @param value: The initial value for the new knob. @return: True if successful."""
		return self.nuke_object.addNotepad()
	#----------------------------------------------------------------------
	def addScriptCommand(self):
		"""self.addScriptCommand(name, value) -> True if successful. Add a script command evaluator to the panel. @param name: The name for the new knob. @param value: The initial value for the new knob. @return: True if successful."""
		return self.nuke_object.addScriptCommand()
	#----------------------------------------------------------------------
	def addSingleLineInput(self):
		"""self.addSingleLineInput(name, value) -> True if successful. Add a single-line input knob to the panel. @param name: The name for the new knob. @param value: The initial value for the new knob. @return: True if successful."""
		return self.nuke_object.addSingleLineInput()
	#----------------------------------------------------------------------
	def addTextFontPulldown(self):
		"""self.addTextFontPulldown(name, value) -> True if successful. Add a font chooser to the panel. @param name: The name for the new knob. @param value: The initial value for the new knob. @return: True if successful."""
		return self.nuke_object.addTextFontPulldown()
	#----------------------------------------------------------------------
	def execute(self,name):
		"""self.execute(name) -> The result of the script as a string, or None if it fails. Execute the script command associated with a particular label and return the result as a string. @param name: The name of the script field to execute. @return: The result of the script as a string, or None if it fails."""
		return self.nuke_object.execute(name)
	#----------------------------------------------------------------------
	def clear(self):
		"""self.clear() -> None Clear all panel attributes."""
		return self.nuke_object.clear()
	#----------------------------------------------------------------------
	def addFilenameSearch(self):
		"""self.addFilenameSearch(name, value) -> True if successful. Add a filename search knob to the panel. @param name: The name for the new knob. @param value: The initial value for the new knob. @return: True if successful."""
		return self.nuke_object.addFilenameSearch()
	#----------------------------------------------------------------------
	def addBooleanCheckBox(self):
		"""self.addBooleanCheckBox(name, value) -> True if successful. Add a boolean check box knob to the panel. @param name: The name for the new knob. @param value: The initial value for the new knob. @return: True if successful."""
		return self.nuke_object.addBooleanCheckBox()
	#----------------------------------------------------------------------
	def addExpressionInput(self):
		"""self.addExpressionInput(name, value) -> True if successful. Add an expression evaluator to the panel. @param name: The name for the new knob. @param value: The initial value for the new knob. @return: True if successful."""
		return self.nuke_object.addExpressionInput()
