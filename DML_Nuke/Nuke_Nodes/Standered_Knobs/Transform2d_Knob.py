import nuke
from ..Abstract_Nodes import Knob

################################################################################
class Transform2d_Knob(Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "Transform2d_Knob"
	#----------------------------------------------------------------------
	def value(self,oc):
		"""value(oc) -> matrix  Return transformation matrix. The argument oc is an OutputContext. Both arguments are optional."""
		return self.nuke_object.value(oc)