
from ... import QT
from ..ABSTRACT_ITEM_MODEL_TYPES.Item_Data_Roles import Base_Item_Data_Roles

########################################################################
class MimeData(QT.QMimeData):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, indexs=[], copyFrom=None):

		"""Constructor"""
		super(MimeData, self).__init__()
		self.row_items        = []
		self.tree_items       = []
		self.indexs           = indexs
		if len(indexs):
			self.row_items  = [item.data(Base_Item_Data_Roles.USER) for item in self.indexs]
			self.tree_items = [item.tree_item for item in self.row_items]
		self.dest_item        = None
		self.drop_action      = None
		self.drag_source      = None
		self.drop_destination = None
		if isinstance(copyFrom, QMimeData):
			for format in copyFrom.formats():
				self.setData(format, copyFrom.data(format))