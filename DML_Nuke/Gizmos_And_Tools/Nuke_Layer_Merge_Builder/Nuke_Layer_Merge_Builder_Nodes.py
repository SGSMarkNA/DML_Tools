import DML_Tools
import DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Generic_Widgets_Nodes
DML_Nuke = DML_Tools.DML_Nuke

################################################################################
class DML_Layer_Order_Builder(DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Generic_Widgets_Nodes.Layer_Order_Output_Builder_Node):
	NODE_TYPE_RELATION  = "DML_Layer_Order_Builder"
	
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		""""""
		DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Generic_Widgets_Nodes.Layer_Order_Output_Builder_Node.__init__(self,*args,**kwargs)
