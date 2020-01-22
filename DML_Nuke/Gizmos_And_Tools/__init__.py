import nuke
import os
import Layers_To_Gimped_PSD

if not os.path.join(os.path.dirname(__file__),"Master_Layer_Order").replace("\\","/") in nuke.pluginPath():
	nuke.pluginAddPath(os.path.join(os.path.dirname(__file__),"Master_Layer_Order").replace("\\","/"), False)
	
if not os.path.join(os.path.dirname(__file__),"Nuke_Layer_Merge_Builder").replace("\\","/") in nuke.pluginPath():
	nuke.pluginAddPath(os.path.join(os.path.dirname(__file__),"Nuke_Layer_Merge_Builder").replace("\\","/"), False)
	
if not os.path.join(os.path.dirname(__file__),"Layers_To_Gimped_PSD").replace("\\","/") in nuke.pluginPath():
	nuke.pluginAddPath(os.path.join(os.path.dirname(__file__),"Layers_To_Gimped_PSD").replace("\\","/"), False)