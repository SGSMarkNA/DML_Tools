import nuke
from .Unsigned_Knob import Unsigned_Knob

################################################################################
class SceneView_Knob(Unsigned_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "SceneView_Knob"
	#----------------------------------------------------------------------
	def getAllItems(self):
		"""
			self.getAllItems() -> list

			Returns a list of strings containing all items that the knob can import.

		"""
		return self.nuke_object.getAllItems()
	#----------------------------------------------------------------------
	def getHighlightedItem(self):
		"""
			self.getHighlightedItem() -> string

			Returns a string containing the item which is currently highlighted.

		"""
		return self.nuke_object.getHighlightedItem()
	#----------------------------------------------------------------------
	def getImportedItems(self):
		"""
			self.getImportedItems() -> list

			Returns a list of strings containing all items imported into the knob.

		"""
		return self.nuke_object.getImportedItems()
	#----------------------------------------------------------------------
	def getSelectedItems(self):
		"""
			self.getSelectedItems() -> list

			Returns a list of strings containing all currently selected items in the knob.

		"""
		return self.nuke_object.getSelectedItems()
	#----------------------------------------------------------------------
	def removeItems(self):
		"""
			self.removeItems() -> None

			Removes a list of string items from the knob.

		"""
		return self.nuke_object.removeItems()
	#----------------------------------------------------------------------
	def setAllItems(self,*args,**kwargs):
		"""
			self.setAllItems(items, autoSelect) -> None

			Sets a list of strings containing all items that the knob can import.

			After calling this function, only items from this list can be imported into the nosde.

			@param items: List of imported items.

			@param autoSelect: If True, all items are automatically set as imported and selected.

			@return: None.

		"""
		return self.nuke_object.setAllItems(*args,**kwargs)
	#----------------------------------------------------------------------
	def setImportedItems(self):
		"""
			self.setImportedItems(items) -> None

			Sets a list of strings containing all items imported into the knob. This will overwrite the current imported items list.@param items: List of imported items.

			@return: None.

		"""
		return self.nuke_object.setImportedItems()
	#----------------------------------------------------------------------
	def setSelectedItems(self):
		"""
			self.setSelectedItems() -> None

			Takes a list of strings of items contained in the knob and sets them as selected.

		"""
		return self.nuke_object.setSelectedItems()

