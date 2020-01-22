import nuke
from ..Base_Nodes import DML_Nuke_Object

################################################################################
class PanelNode(DML_Nuke_Object):
	#----------------------------------------------------------------------
	def writeKnobs(self,i):
		"""self.writeKnobs(i) -> String in .nk form. Return a tcl list. If TO_SCRIPT | TO_VALUE is not on, this is a simple list of knob names. If it is on, it is an alternating list of knob names and the output of to_script().  Flags can be any of these or'd together: - nuke.TO_SCRIPT produces to_script(0) values - nuke.TO_VALUE produces to_script(context) values - nuke.WRITE_NON_DEFAULT_ONLY skips knobs with not_default() false - nuke.WRITE_USER_KNOB_DEFS writes addUserKnob commands for user knobs - nuke.WRITE_ALL writes normally invisible knobs like name, xpos, ypos  @param i: The set of flags or'd together. Default is TO_SCRIPT | TO_VALUE. @return: String in .nk form."""
		return self.nuke_object.writeKnobs(i)
	#----------------------------------------------------------------------
	def createWidget(self):
		"""Create the widget for the panel"""
		return self.nuke_object.createWidget()
	#----------------------------------------------------------------------
	def __str__(self):
		"""x.__str__() <==> str(x)"""
		return self.nuke_object.__str__()
	#----------------------------------------------------------------------
	def addKnob(self,k):
		"""self.addKnob(k) -> None. Add knob k to this node or panel. @param k: Knob. @return: None."""
		return self.nuke_object.addKnob(k)
	#----------------------------------------------------------------------
	def removeKnob(self,k):
		"""self.removeKnob(k) -> None. Remove knob k from this node or panel. Throws a ValueError exception if k is not found on the node. @param k: Knob. @return: None."""
		return self.nuke_object.removeKnob(k)
	#----------------------------------------------------------------------
	def knobs(self):
		"""self.knobs() -> dict  Get a dictionary of (name, knob) pairs for all knobs in this node.  For example:     >>> b = nuke.nodes.Blur()    >>> b.knobs()  @return: Dictionary of all knobs.  Note that this doesn't follow the links for Link_Knobs"""
		return self.nuke_object.knobs()
	#----------------------------------------------------------------------
	def readKnobs(self,s):
		"""self.readKnobs(s) -> None. Read the knobs from a string (TCL syntax). @param s: A string. @return: None."""
		return self.nuke_object.readKnobs(s)
