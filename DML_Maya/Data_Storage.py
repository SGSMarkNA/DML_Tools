import General_Utils
import Maya_Util_Classes

########################################################################
class Node_Container(dict):
	""""""
	__metaclass__ = General_Utils.Singleton
########################################################################
class Maya_Node_Type_To_Class_Wapper_Container(dict):
	""""""
	__metaclass__ = General_Utils.Singleton

########################################################################
class Maya_Node_Type_Overide_Return_Wapper_Check_Container(dict):
	""""""
	__metaclass__ = General_Utils.Singleton

########################################################################
class Maya_Plug_Type_To_Class_Wapper_Container(dict):
	""""""
	__metaclass__ = General_Utils.Singleton	

########################################################################
class Maya_Plug_Type_Overide_Return_Wapper_Check_Container(dict):
	""""""
	__metaclass__ = General_Utils.Singleton
	
########################################################################
class Maya_Component_Type_To_Class_Wapper_Container(dict):
	""""""
	__metaclass__ = General_Utils.Singleton	

########################################################################
class Maya_Component_Type_Overide_Return_Wapper_Check_Container(dict):
	""""""
	__metaclass__ = General_Utils.Singleton
	
########################################################################
class Maya_Option_Variable_Type_To_Class_Wapper_Container(dict):
	""""""
	__metaclass__ = General_Utils.Singleton
	
Cashed_Nodes_Container          = Node_Container()
Node_Return_Type_Relations      = Maya_Node_Type_To_Class_Wapper_Container()
Node_Return_Type_Overides       = Maya_Node_Type_Overide_Return_Wapper_Check_Container()
Plug_Return_Type_Relations      = Maya_Plug_Type_To_Class_Wapper_Container()
Plug_Return_Type_Overides       = Maya_Plug_Type_Overide_Return_Wapper_Check_Container()
Component_Return_Type_Relations = Maya_Component_Type_To_Class_Wapper_Container()
Component_Return_Type_Overides  = Maya_Component_Type_Overide_Return_Wapper_Check_Container()

Optional_Variable_Types    = Maya_Option_Variable_Type_To_Class_Wapper_Container()

clear_node_cash_on_new_scene_opened_script_job =  Maya_Util_Classes.Maya_Script_Job(event=["NewSceneOpened",Cashed_Nodes_Container.clear])
clear_node_cash_on_scene_opened_script_job =  Maya_Util_Classes.Maya_Script_Job(event=["SceneOpened",Cashed_Nodes_Container.clear])