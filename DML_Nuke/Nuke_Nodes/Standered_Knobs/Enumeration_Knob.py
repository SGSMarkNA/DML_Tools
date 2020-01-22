import nuke
from .Unsigned_Knob import Unsigned_Knob

################################################################################
class Enumeration_Knob(Unsigned_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "Enumeration_Knob"
	#----------------------------------------------------------------------
	def enumName(self):
		"""
			self.enumName(n) -> string

			Return name of enumeration n. The argument n is an integer and in the range of 0 and numValues. Deprecated.

		"""
		return self.nuke_object.enumName()
	#----------------------------------------------------------------------
	def numValues(self):
		"""
			self.numValues() -> int

			Return number of values. Deprecated.

		"""
		return self.nuke_object.numValues()
	#----------------------------------------------------------------------
	def setValues(self,*args):
		"""
			self.setValues(items) -> None.

			(Re)initialise knob to the supplied list of items.

			@param items: The new list of values.

			@return: None.

			Example:

			w = nuke.nodes.Write()

			k = w['file_type']

			k.setValues(['exr'])

		"""
		return self.nuke_object.setValues(*args)
	#----------------------------------------------------------------------
	def values(self):
		"""
			self.values() -> List of strings.

			Return list of items.

			@return: List of strings.

			Example:

			w = nuke.nodes.Write()

			k = w['file_type']

			k.values()

		"""
		return self.nuke_object.values()

	#----------------------------------------------------------------------
	def setValue(self,val):
		"""
			self.setValue(val) -> bool

			Sets the value 'val'.

			@return: True if successful, False if not.

		"""
		return self.nuke_object.setValue(str(val))
	#----------------------------------------------------------------------
	def value(self):
		"""
			Return the value of this knob.

		"""
		return self.nuke_object.value()