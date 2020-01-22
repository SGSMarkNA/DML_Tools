import nuke
from ..Base_Nodes import DML_Nuke_Object

################################################################################
class Lut(DML_Nuke_Object):
	#----------------------------------------------------------------------
	def toByte(self,float):
		"""self.toByte(float) -> float.  Converts floating point values to byte values in the range 0-255."""
		return self.nuke_object.toByte(float)
	#----------------------------------------------------------------------
	def fromByteSingle(self,float):
		"""self.fromByte(float) -> float.  Converts byte values in the range 0-255 to floating point."""
		return self.nuke_object.fromByteSingle(float)
	#----------------------------------------------------------------------
	def fromFloat(self):
		"""fromFloat(src, alpha) -> float list.  Convert a sequence of floating-point values to from_byte(x*255). Alpha is an optional argument and if present unpremultiply by alpha, convert, and then multiply back."""
		return self.nuke_object.fromFloat()
	#----------------------------------------------------------------------
	def toFloat(self):
		"""toFloat(src, alpha) -> float list.  Convert a sequence of floating-point values to to_byte(x)/255. Alpha is an optional argument and if present unpremultiply by alpha, convert, and then multiply back."""
		return self.nuke_object.toFloat()
	#----------------------------------------------------------------------
	def isLinear(self):
		"""self.isLinear() -> True if toByte(x) appears to return x*255, False otherwise."""
		return self.nuke_object.isLinear()
	#----------------------------------------------------------------------
	def toByteSingle(self,float):
		"""self.toByte(float) -> float.  Converts floating point values to byte values in the range 0-255."""
		return self.nuke_object.toByteSingle(float)
	#----------------------------------------------------------------------
	def fromByte(self,float):
		"""self.fromByte(float) -> float.  Converts byte values in the range 0-255 to floating point."""
		return self.nuke_object.fromByte(float)
	#----------------------------------------------------------------------
	def isZero(self):
		"""self.isZero() -> True if toByte(0) returns a value <= 0, False otherwise."""
		return self.nuke_object.isZero()
