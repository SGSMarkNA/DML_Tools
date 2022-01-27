import nuke
from ..Base_Nodes import DML_Nuke_Object

################################################################################
class FrameRanges(DML_Nuke_Object):
	#----------------------------------------------------------------------
	def compact(self):
		"""compact() -> None   compact all the frame ranges."""
		return self.nuke_object.compact()
	#----------------------------------------------------------------------
	def getRange(self):
		"""getRange()-> FrameRange   return a range from the list"""
		return self.nuke_object.getRange()
	#----------------------------------------------------------------------
	def toFrameList(self):
		"""toFrameList() -> [int]   return a list of frames in a vector"""
		return self.nuke_object.toFrameList()
	#----------------------------------------------------------------------
	def __str__(self):
		"""x.__str__() <==> str(x)"""
		return self.nuke_object.__str__()
	#----------------------------------------------------------------------
	def minFrame(self):
		"""minFrame() -> int   get minimun frame of all ranges."""
		return self.nuke_object.minFrame()
	#----------------------------------------------------------------------
	def add(self,r):
		"""add(r) -> None   add a new frame range."""
		return self.nuke_object.add(r)
	#----------------------------------------------------------------------
	def __next__(self):
		"""x.next() -> the next value, or raise StopIteration"""
		return next(self.nuke_object)
	#----------------------------------------------------------------------
	def maxFrame(self):
		"""maxFrame() -> int   get maximun frame of all ranges."""
		return self.nuke_object.maxFrame()
	#----------------------------------------------------------------------
	def __iter__(self):
		"""x.__iter__() <==> iter(x)"""
		return self.nuke_object.__iter__()
	#----------------------------------------------------------------------
	def clear(self):
		"""clear() -> None   reset all store frame ranges."""
		return self.nuke_object.clear()
	#----------------------------------------------------------------------
	def size(self):
		"""size() -> int   return the ranges number."""
		return self.nuke_object.size()
