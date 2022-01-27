import nuke
from ..Abstract_Nodes import Knob
from ..Abstract_Nodes import Node
from ...Decorators.Node_Wraper_Manager import node_Return_Wrapper,nuke_Object_Return_Wrapper,knob_Return_Wrapper
################################################################################
class Link_Knob(Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "Link_Knob"
	#----------------------------------------------------------------------
	def setValue(self):
		"""setValue() -> None  Set value of knob."""
		return self.nuke_object.setValue()
	#----------------------------------------------------------------------
	@knob_Return_Wrapper
	def getLinkedKnob(self):
		"""getLinkedKnob() -> knob """
		return self.nuke_object.getLinkedKnob()
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def getLinkedNode(self):
		"""getLinkedKnob() -> knob """
		return self.nuke_object.getLinkedKnob().node()
	#----------------------------------------------------------------------
	def value(self):
		"""value() -> string  Return value of knob."""
		return self.nuke_object.value()
	#----------------------------------------------------------------------
	def getLink(self):
		"""getLink() -> s """
		return self.nuke_object.getLink()
	#----------------------------------------------------------------------
	def setLink(self,s):
		"""setLink(s) -> None """
		if isinstance(s,str):
			self.nuke_object.setLink(s)
		elif isinstance(s,Knob):
			self.nuke_object.setLink(s.fullName)
		elif isinstance(s,nuke.Knob):
			self.nuke_object.setLink(s.fullyQualifiedName())
		else:
			raise ValueError("Input Must be a string or nuke Knob")
	#----------------------------------------------------------------------
	def makeLink(self,node,knob):
		"""makeLink(node, knob) -> None """
		if not isinstance(node,str):
			if isinstance(node,Node):
				node = node.fullName
			elif isinstance(s,nuke.Node):
				node = node.fullName()
			else:
				raise ValueError("node Must be a string or nuke Node")
		
		if not isinstance(knob,str):
			if isinstance(knob,Knob):
				knob = knob.name
			elif isinstance(knob,nuke.Knob):
				knob = knob.name()
			else:
				raise ValueError("knob Must be a string or nuke Knob")
		return self.nuke_object.makeLink(node,knob)
