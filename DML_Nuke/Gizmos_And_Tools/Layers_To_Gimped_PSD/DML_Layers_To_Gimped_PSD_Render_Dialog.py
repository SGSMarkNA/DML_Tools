
import nuke
import nukescripts
import os
import Layers_To_Gimped_PSD_Utils

########################################################################
class DML_Nuke_RenderDialog(nukescripts.RenderDialog):
	
	#----------------------------------------------------------------------
	def _titleString(self):
		return "Render PSD Builder"

	#----------------------------------------------------------------------
	def _idString(self):
		return "uk.co.thefoundry.RenderPSDBuilder"
	
	#----------------------------------------------------------------------
	def _build_render_values(self):
		""""""
		self.all_write_nodes = []
		self.all_psd_nodes   = []
		self.all_gimp_groups = []
		self.views_to_render = []
		
		self.gimped_psd_node_data = Layers_To_Gimped_PSD_Utils.get_Enabled_DML_Layers_To_Gimped_PSD_Dict()
		
		for item_data in self.gimped_psd_node_data:
			
			psd,grp,wrnds = item_data["psd"],item_data["grp"],item_data["allwrns"]
			
			self.all_write_nodes.extend(wrnds)
			self.all_gimp_groups.append(grp)
			self.all_psd_nodes.append(psd)
			
			for view in psd.knob("DML_Nuke_View_Selection").value().split():
				if not view in self.views_to_render:
					self.views_to_render.append(view)
			
	def _addViewKnob(self):
		"""Add knobs for view selection."""
		oc = nuke.OutputContext()
		if (oc.viewcount() > 2):
			self._viewSelection = nuke.MultiView_Knob("multi_view", "Views")
			self._viewSelection.fromScript(" ".join(self.views_to_render))
			self.addKnob(self._viewSelection)
			self._viewSelection.clearFlag(nuke.NO_MULTIVIEW)
			self._viewSelection.setVisible(False)
	
	#----------------------------------------------------------------------
	def __init__(self,dialogState, exceptOnError = True):
		""""""
		self._build_render_values()
		nukescripts.RenderDialog.__init__(self, dialogState, nuke.root(), [], exceptOnError)
		
	def knobChanged( self, knob ):
		nukescripts.RenderDialog.knobChanged(self, knob)
		self._useProxy.setVisible(False)
		self._bgRender.setVisible(False)
		
	def run(self):
		
		frame_ranges = nuke.FrameRanges(self._frameRange.value().split(','))
		
		psd_build_data = Layers_To_Gimped_PSD_Utils.create_PSD_Build_Info_V2(frame_ranges.toFrameList())
		Layers_To_Gimped_PSD_Utils.Bake_PSD_Build_Info(psd_build_data)
		try:
			#nuke.executeMultiple([n.nuke_object for n in self.all_write_nodes], frame_ranges, self.views_to_render, continueOnError = self._continueOnError.value())
			rendered_check = True
		except RuntimeError, e:
			rendered_check = False
			if self._exceptOnError or e.args[0][0:9] != "Cancelled":   # TO DO: change this to an exception type
				raise
		if rendered_check:
			pass
			#Layers_To_Gimped_PSD_Utils.run_Json_Build_Data(psd_build_data)
			#threading.Thread( None, target=run_Json_Build_Data ,args=[psd_build_data]).start()
		
def showRenderDialog(exceptOnError = True):
	"""Present a dialog that renders the given list of nodes."""
	d = DML_Nuke_RenderDialog(nukescripts.renderdialog._gRenderDialogState, exceptOnError)
	nukescripts.renderdialog._showDialog(d)
	
if nuke.GUI:
	# Render menu
	m = nuke.menu("Nuke").menu("Render");
	m.addCommand("PSD Render", "os.sys.modules.get('{}').showRenderDialog(False)".format(__name__), "^F5")