import nuke
import Nuke_Scripts
import nukescripts
from Mata_Classes import Data_Storage
from Mata_Classes import Node_Return_Type_Publication_Metaclass
from Mata_Classes import Knob_Return_Type_Publication_Metaclass
import Nuke_Nodes
import dml
import Decorators
import Nuke_GUI
import Gizmos_And_Tools
import callbacks

def create_menus():
	if nuke.GUI:
		AW_TOOLS_MENU = nuke.menu("Nuke").addMenu("AW Tools")
		Gimp_menu = AW_TOOLS_MENU.addMenu("Gimped To PSD Nodes")
		Gimp_menu.addCommand("Master Layer Order",'nuke.createNode("DML_Master_Layer_Order")')
		Gimp_menu.addCommand("Layers To PSD",'nuke.createNode("DML_Layers_To_Gimped_PSD")')
		Gimp_menu.addCommand("Layer Order Builder",'nuke.createNode("DML_Layer_Order_Builder")')
		
