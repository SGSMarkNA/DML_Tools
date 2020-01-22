import nuke
from ..Abstract_Nodes import Knob

################################################################################
class GeoSelect_Knob(Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "GeoSelect_Knob"
	#----------------------------------------------------------------------
	def getSelection(self):
		"""self.getSelection() -> list of lists of floats Returns the selection weights for each vertex as a float. If you access the result as selection[obj][pt], then obj is the index of the object in the input geometry and pt is the index of the point in that object."""
		return self.nuke_object.getSelection()
	#----------------------------------------------------------------------
	def getGeometry(self):
		"""self.getGeometry() -> _geo.GeometryList Get the geometry which this knob can select from."""
		return self.nuke_object.getGeometry()