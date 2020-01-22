
import nuke
import nukescripts
import os

def create_Gimp_Render_Menu_Items():
	if nuke.GUI:
		# Render menu
		import DML_Tools.DML_Nuke.Gizmos_And_Tools.Layers_To_Gimped_PSD.DML_Layers_To_Gimped_PSD_Render_Dialog
		if "DEADLINE_PATH" in os.environ:
			import DML_Tools.DML_Nuke.Gizmos_And_Tools.Layers_To_Gimped_PSD.Submit_Gimped_To_Deadline
			m = nuke.menu("Nuke").menu("Render");
			m.addCommand("Submit PSD Build To Deadline", "DML_Tools.DML_Nuke.Gizmos_And_Tools.Layers_To_Gimped_PSD.Submit_Gimped_To_Deadline.submit_Gimped_To_DeadLine()")

def on_root_created():
	import DML_Tools.DML_Nuke.Gizmos_And_Tools.Nuke_Views_System
	import DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Nuke_Views
	Nuke_Views_modeual = DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Nuke_Views
	#if nuke.GUI:
		#import DML_Tools.DML_Nuke.Gizmos_And_Tools.Nuke_Views_System
		#import DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Nuke_Views
		#Nuke_Views_modeual = DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Nuke_Views
	#else:
		#nuke.executeInMainThread(__import__,"DML_Tools.DML_Nuke.Gizmos_And_Tools.Nuke_Views_System")
		#nuke.executeInMainThread(__import__,"DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Nuke_Views")
		#Nuke_Views_modeual = os.sys.modules["DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Nuke_Views"]
	
	dml_nuke_views = nuke.root().knob("dml_nuke_views")
	if dml_nuke_views == None:
		Nuke_Views_modeual.Nuke_Views_Widget_Knob.add_Widget_Knob(nuke.root())
	if nuke.GUI:
		create_Gimp_Render_Menu_Items()
		#import DML_Tools.DML_Nuke.Gizmos_And_Tools.Layers_To_Gimped_PSD.DML_Layers_To_Gimped_PSD_Render_Dialog
	nuke.removeOnCreate(on_root_created, args=(), kwargs={}, nodeClass="Root")

def on_Nuke_Views_Related_Node_Created():
	if not hasattr(nuke,"DML_Nuke_View_System"):
		try:
			nuke.root().knob("views")
			import DML_Tools.DML_Nuke.Gizmos_And_Tools.Nuke_Views_System
			import DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Nuke_Views
			Nuke_Views_modeual = DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Nuke_Views
			#if nuke.GUI:
				#import DML_Tools.DML_Nuke.Gizmos_And_Tools.Nuke_Views_System
				#import DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Nuke_Views
				#Nuke_Views_modeual = DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Nuke_Views
			#else:
				#nuke.executeInMainThread(__import__,"DML_Tools.DML_Nuke.Gizmos_And_Tools.Nuke_Views_System")
				#nuke.executeInMainThread(__import__,"DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Nuke_Views")
				#Nuke_Views_modeual = os.sys.modules["DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Nuke_Views"]
			if nuke.GUI:
				create_Gimp_Render_Menu_Items()
				#import DML_Tools.DML_Nuke.Gizmos_And_Tools.Layers_To_Gimped_PSD.DML_Layers_To_Gimped_PSD_Render_Dialog
				#nuke.executeInMainThread(__import__,"DML_Tools.DML_Nuke.Gizmos_And_Tools.Layers_To_Gimped_PSD.DML_Layers_To_Gimped_PSD_Render_Dialog")
				
			dml_nuke_views = nuke.root().knob("dml_nuke_views")
			
			if dml_nuke_views == None:
				Nuke_Views_modeual.Nuke_Views_Widget_Knob.add_Widget_Knob(nuke.root())
			for node_cls in ["DML_Layers_To_Gimped_PSD","DML_Nuke_Layer_Merge_Builder","DML_Master_Layer_Order"]:
				nuke.removeOnCreate(on_Nuke_Views_Related_Node_Created, args=(), kwargs={}, nodeClass=node_cls)
		except:
			nuke.addOnCreate(on_root_created, args=(), kwargs={}, nodeClass="Root")
			for node_cls in ["DML_Layers_To_Gimped_PSD","DML_Nuke_Layer_Merge_Builder","DML_Master_Layer_Order"]:
				nuke.removeOnCreate(on_Nuke_Views_Related_Node_Created, args=(), kwargs={}, nodeClass=node_cls)
		
for node_cls in ["DML_Layers_To_Gimped_PSD","DML_Nuke_Layer_Merge_Builder","DML_Master_Layer_Order"]:
	nuke.addOnCreate(on_Nuke_Views_Related_Node_Created, args=(), kwargs={}, nodeClass=node_cls)