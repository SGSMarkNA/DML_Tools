
from ... import QT
userRole_generator = QT.userRole_generator
Constants = QT.Constants
########################################################################
class Base_Item_Data_Roles(Constants.ItemDataRole):
	""""""
	USER                 = userRole_generator()
	ICON_COLOR           = userRole_generator()
	ICON_VISABLE         = userRole_generator()
	FONT_SIZE            = userRole_generator()
	FONT_FAMILY          = userRole_generator()
	FONT_WEIGHT          = userRole_generator()
	FONT_CAPITALIZATION  = userRole_generator()
	SELECTABLE           = userRole_generator()
	ENABLED              = userRole_generator()
	EDITABLE             = userRole_generator()
	DRAGABLE             = userRole_generator()
	DROPABLE             = userRole_generator()
	CHECKABLE            = userRole_generator()
	TRISTATE             = userRole_generator()
	HORIZONTAL_ALIGNMENT = userRole_generator()
	VERTICAL_ALIGNMENT   = userRole_generator()
	INTERNAL_DATA        = userRole_generator()
	TREE_OBJECT          = userRole_generator()
	INTERNAL_EDITOR      = userRole_generator()
	INTERNAL_ID          = userRole_generator()