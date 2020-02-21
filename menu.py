import nuke

from DML_Tools.DML_Nuke.Nuke_Scripts import W_hotbox,W_hotboxManager

AW_TOOLS_MENU = nuke.menu("Nuke").addMenu("AW Tools")
Gimp_menu = AW_TOOLS_MENU.addMenu("PSD System Nodes")
Gimp_menu.addCommand("Master Layer Order",'nuke.createNode("DML_Master_Layer_Order","name Master_Layer_Order",inpanel=False)')
Gimp_menu.addCommand("PSD Builder",'nuke.createNode("DML_Layers_To_Gimped_PSD","name PSD_Builder",inpanel=False)')
Gimp_menu.addCommand("Layer Merger",'nuke.createNode("DML_Layer_Order_Builder","name Layer_Merger",inpanel=False)')
del Gimp_menu