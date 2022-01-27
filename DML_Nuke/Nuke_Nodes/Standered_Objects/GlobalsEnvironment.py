
import nuke
from ..Base_Nodes import DML_Nuke_Object

################################################################################
class GlobalsEnvironment(DML_Nuke_Object):
	#----------------------------------------------------------------------
	def __delitem__(self,y):
		"""x.__delitem__(y) <==> del x[y]"""
		return self.nuke_object.__delitem__(y)
	#----------------------------------------------------------------------
	def __getitem__(self,y):
		"""x.__getitem__(y) <==> x[y]"""
		return self.nuke_object.__getitem__(y)
	#----------------------------------------------------------------------
	def __contains__(self):
		""""""
		return self.nuke_object.__contains__()
	#----------------------------------------------------------------------
	def keys(self):
		""""""
		return list(self.nuke_object.keys())
	#----------------------------------------------------------------------
	def items(self):
		""""""
		return list(self.nuke_object.items())
	#----------------------------------------------------------------------
	def get(self):
		""""""
		return self.nuke_object.get()
	#----------------------------------------------------------------------
	def __setitem__(self):
		"""x.__setitem__(i, y) <==> x[i]=y"""
		return self.nuke_object.__setitem__()
	#----------------------------------------------------------------------
	def has_key(self):
		""""""
		return self.nuke_object.has_key()
	#----------------------------------------------------------------------
	def values(self):
		""""""
		return list(self.nuke_object.values())
	#----------------------------------------------------------------------
	def __repr__(self):
		"""x.__repr__() <==> repr(x)"""
		return self.nuke_object.__repr__()
	#----------------------------------------------------------------------
	def __len__(self):
		"""x.__len__() <==> len(x)"""
		return self.nuke_object.__len__()
