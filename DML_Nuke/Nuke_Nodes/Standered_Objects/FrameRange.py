
import nuke
from ..Base_Nodes import DML_Nuke_Object

################################################################################
class FrameRange(DML_Nuke_Object):
	#----------------------------------------------------------------------
	def minFrame(self):
		"""self.minFrame() -> int   return the minimun frame define in the range."""
		return self.nuke_object.minFrame()
	#----------------------------------------------------------------------
	def last(self):
		"""self.last() -> int   return the last frame of the range."""
		return self.nuke_object.last()
	#----------------------------------------------------------------------
	def setLast(self,n):
		"""self.setLast(n) -> None   set the last frame of the range."""
		return self.nuke_object.setLast(n)
	#----------------------------------------------------------------------
	def __str__(self):
		"""x.__str__() <==> str(x)"""
		return self.nuke_object.__str__()
	#----------------------------------------------------------------------
	def getFrame(self,n):
		"""self.getFrame(n) -> int   return the frame according to the index, parameter n must be between 0 and frames()."""
		return self.nuke_object.getFrame(n)
	#----------------------------------------------------------------------
	def stepFrame(self):
		"""self.stepFrame() -> int   return the absolute increment between two frames."""
		return self.nuke_object.stepFrame()
	#----------------------------------------------------------------------
	def setFirst(self,n):
		"""self.setFirst(n) -> None   set the first frame of the range."""
		return self.nuke_object.setFirst(n)
	#----------------------------------------------------------------------
	def __next__(self):
		"""x.next() -> the next value, or raise StopIteration"""
		return next(self.nuke_object)
	#----------------------------------------------------------------------
	def isInRange(self,n):
		"""self.isInRange(n) -> int   return if the frame is inside the range."""
		return self.nuke_object.isInRange(n)
	#----------------------------------------------------------------------
	def maxFrame(self):
		"""self.maxFrame() -> int   return the maximun frame define in the range."""
		return self.nuke_object.maxFrame()
	#----------------------------------------------------------------------
	def __iter__(self):
		"""x.__iter__() <==> iter(x)"""
		return self.nuke_object.__iter__()
	#----------------------------------------------------------------------
	def setIncrement(self,n):
		"""self.setIncrement(n) -> None   set the increment between two frames."""
		return self.nuke_object.setIncrement(n)
	#----------------------------------------------------------------------
	def increment(self):
		"""self.increment() -> int   return the increment between two frames."""
		return self.nuke_object.increment()
	#----------------------------------------------------------------------
	def frames(self):
		"""self.frames() -> int   return the numbers of frames defined in the range."""
		return self.nuke_object.frames()
	#----------------------------------------------------------------------
	def first(self):
		"""self.first() -> int   return the first frame of the range."""
		return self.nuke_object.first()
