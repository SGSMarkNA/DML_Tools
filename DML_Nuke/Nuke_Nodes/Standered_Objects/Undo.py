import nuke
from ..Base_Nodes import DML_Nuke_Object

################################################################################
class Undo(DML_Nuke_Object):
	#----------------------------------------------------------------------
	def disabled(self):
		"""True if disable() has been called"""
		return self.nuke_object.disabled()
	#----------------------------------------------------------------------
	def undoDescribe(self):
		"""Return short description of undo n."""
		return self.nuke_object.undoDescribe()
	#----------------------------------------------------------------------
	def cancel(self):
		"""Undoes any actions recorded in the current set and throws it away."""
		return self.nuke_object.cancel()
	#----------------------------------------------------------------------
	def redo(self):
		"""Redoes 0'th redo."""
		return self.nuke_object.redo()
	#----------------------------------------------------------------------
	def undoSize(self):
		"""Number of undo's that can be done."""
		return self.nuke_object.undoSize()
	#----------------------------------------------------------------------
	def end(self):
		"""Complete current undo set and add it to the undo list."""
		return self.nuke_object.end()
	#----------------------------------------------------------------------
	def redoDescribe(self):
		"""Return short description of redo n."""
		return self.nuke_object.redoDescribe()
	#----------------------------------------------------------------------
	def __enter__(self):
		""""""
		return self.nuke_object.__enter__()
	#----------------------------------------------------------------------
	def redoDescribeFully(self):
		"""Return long description of redo n."""
		return self.nuke_object.redoDescribeFully()
	#----------------------------------------------------------------------
	def new(self):
		"""Same as end();begin()."""
		return self.nuke_object.new()
	#----------------------------------------------------------------------
	def redoTruncate(self):
		"""Destroy any redo's greater or equal to n."""
		return self.nuke_object.redoTruncate()
	#----------------------------------------------------------------------
	def undoTruncate(self):
		"""Destroy any undo's greater or equal to n."""
		return self.nuke_object.undoTruncate()
	#----------------------------------------------------------------------
	def begin(self):
		"""Begin a new user-visible group of undo actions."""
		return self.nuke_object.begin()
	#----------------------------------------------------------------------
	def enable(self):
		"""Undoes the previous disable()"""
		return self.nuke_object.enable()
	#----------------------------------------------------------------------
	def __exit__(self):
		""""""
		return self.nuke_object.__exit__()
	#----------------------------------------------------------------------
	def undo(self):
		"""Undoes 0'th undo."""
		return self.nuke_object.undo()
	#----------------------------------------------------------------------
	def disable(self):
		"""Prevent recording undos until matching enable()"""
		return self.nuke_object.disable()
	#----------------------------------------------------------------------
	def redoSize(self):
		"""Number of redo's that can be done."""
		return self.nuke_object.redoSize()
	#----------------------------------------------------------------------
	def name(self):
		"""Name current undo set."""
		return self.nuke_object.name()
	#----------------------------------------------------------------------
	def undoDescribeFully(self):
		"""Return long description of undo n."""
		return self.nuke_object.undoDescribeFully()
