import nuke, os
import DML_Tools
DML_PYQT = DML_Tools.DML_PYQT
DML_Nuke = DML_Tools.DML_Nuke
import nukescripts
import json
import time
import nuke
import Layers_To_Gimped_PSD_Utils
import DML_Tools.DML_Deadline.Command_Access
import DML_Tools.DML_Deadline.Deadline_Commands
import DML_Tools.DML_Deadline.Job_Data_Model
import re
Ui_Loader = DML_PYQT.QT.QUiLoader()


#----------------------------------------------------------------------
def build_psd_file_Locations(psd_build_data):
	""""""
	psd_foldes = []
	psd_experssion = []
	for build in psd_build_data["builds"]:
		psd_path = build['PSD_File_Path']
		psd_file = psd_path.split("/")[-1]
		psd_folder = psd_path.replace("/"+psd_file,"")
		search = re.findall("_[0-9]+.psd",psd_file)
		if len(search):
			if not psd_folder in psd_foldes:
				psd_foldes.append(psd_folder)
				search_str = search[0]
				numbers = search_str.replace(".psd","").replace("_","")
				padding = "#" *  len(numbers)
				file_experssion = psd_file.replace(numbers,padding)
				psd_experssion.append([psd_folder.replace("/","\\"),file_experssion])
		else:
			psd_experssion.append([psd_folder.replace("/","\\"),psd_file])
	
	return psd_experssion

########################################################################
class GimpPSD_Plugin_Info(DML_Tools.DML_Deadline.Job_Data_Model.Base_Plugin_Info):
	""""""

	def __init__(self,jsonfile=None,jsondata=None):
		"""
			Options

				--JsonFile
					| The filename to the json file used to build the psd.
					|
					"""
		self.jsonfile = jsonfile
		self.jsondata = jsondata

	def create_Submit_String(self):
		lines = []
		if self.jsonfile == None:
			lines.append(DML_Tools.DML_Deadline.Job_Data_Model.build_Options_Line("JsonData", self.jsondata))
		else:
			lines.append(DML_Tools.DML_Deadline.Job_Data_Model.build_Options_Line("JsonFile", self.jsonfile))
		return "\n".join(lines)


########################################################################
class Submit_Gimped_To_Deadline_Widget(DML_PYQT.QWidget):
	def __init__(self, parent=None):
		DML_PYQT.QWidget.__init__(self, parent=parent)
		master_Layout = DML_PYQT.QVBoxLayout(self)
		master_Layout.setSpacing(0)
		master_Layout.setContentsMargins(0, 0, 0, 0)
		self.file_wig = self._load_ui()
		master_Layout.addWidget(self.file_wig)
		
		for child in self.file_wig.findChildren(DML_PYQT.QObject):
			objectName = child.objectName()
			if len(objectName):
				if not hasattr(self,objectName):
					self.__dict__[objectName]=child
		data = DML_Tools.DML_Deadline.Deadline_Commands.GetSubmissionInfo(["Pools", "Groups"])
		if not data.ok:
			time.sleep(0.5)
			data = DML_Tools.DML_Deadline.Deadline_Commands.GetSubmissionInfo(["Pools", "Groups"])
		if data.ok:
			DML_PYQT.QComboBox.addItems
			self.Deadline_Pool.addItems(data.result.Pools)
			self.Deadline_SecondaryPool.addItems(data.result.Pools)
			self.Deadline_Group.addItems(data.result.Groups)
		DML_PYQT.QMetaObject.connectSlotsByName(self)
		self._build_render_values()
		if False:
			self.Deadline_JobName              = DML_PYQT.QLineEdit()
			self.Deadline_Comment              = DML_PYQT.QLineEdit()
			self.Deadline_Department           = DML_PYQT.QLineEdit()
			self.Deadline_Pool                 = DML_PYQT.QComboBox()
			self.Deadline_SecondaryPool        = DML_PYQT.QComboBox()
			self.Deadline_Group                = DML_PYQT.QComboBox()
			self.Deadline_Priority             = DML_PYQT.QSpinBox()
			self.Deadline_AutoTaskTimeout      = DML_PYQT.QCheckBox()
			self.Deadline_TaskTimeout          = DML_PYQT.QSpinBox()
			self.Deadline_LimitConcurrentTasks = DML_PYQT.QCheckBox()
			self.Deadline_ConcurrentTasks      = DML_PYQT.QSpinBox()
			self.Deadline_MachineLimit         = DML_PYQT.QSpinBox()
			self.Deadline_IsBlacklist          = DML_PYQT.QCheckBox()
			self.Deadline_MachineList          = DML_PYQT.QLineEdit()
			self.Deadline_LimitGroups          = DML_PYQT.QLineEdit()
			self.Deadline_Dependencies         = DML_PYQT.QLineEdit()
			self.Deadline_OnComplete           = DML_PYQT.QComboBox()
			self.Deadline_FrameListMode        = DML_PYQT.QComboBox()
			self.Deadline_FrameList            = DML_PYQT.QLineEdit()
			self.Deadline_ChunkSize            = DML_PYQT.QSpinBox()
			self.Deadline_Threads              = DML_PYQT.QSpinBox()
			self.Deadline_UseGpu               = DML_PYQT.QCheckBox()
			self.Deadline_ChooseGpu            = DML_PYQT.QSpinBox()
			self.Deadline_RenderMode           = DML_PYQT.QComboBox()
			self.Deadline_MemoryUsage          = DML_PYQT.QSpinBox()
			self.Deadline_StackSize            = DML_PYQT.QSpinBox()
			self.Deadline_EnforceRenderOrder   = DML_PYQT.QCheckBox()
			self.Deadline_SubmitSuspended      = DML_PYQT.QCheckBox()
			self.Deadline_ReloadPlugin         = DML_PYQT.QCheckBox()
			self.Deadline_ContinueOnError      = DML_PYQT.QCheckBox()
			self.Deadline_BatchMode            = DML_PYQT.QCheckBox()
			self.Deadline_UseNukeX             = DML_PYQT.QCheckBox()
			
			self.SubmitButton                  = DML_PYQT.QPushButton()
			self.Deadline_MachineListButton    = DML_PYQT.QPushButton()
			self.Deadline_LimitGroupsButton    = DML_PYQT.QPushButton()
			self.Deadline_DependenciesButton   = DML_PYQT.QPushButton()
		self._load_Settings()
		self._make_Save_Settings_Connections()
		self.Deadline_JobName
		self.Deadline_Comment
		self.Deadline_Department
		self.Deadline_Pool
		self.Deadline_SecondaryPool
		self.Deadline_Group
		self.Deadline_Priority
		self.Deadline_AutoTaskTimeout
		self.Deadline_TaskTimeout
		self.Deadline_LimitConcurrentTasks
		self.Deadline_ConcurrentTasks
		self.Deadline_MachineLimit
		self.Deadline_IsBlacklist
		self.Deadline_MachineList
		self.Deadline_LimitGroups
		self.Deadline_Dependencies
		self.Deadline_OnComplete
		self.Deadline_FrameListMode
		self.Deadline_FrameList
		self.Deadline_ChunkSize
		self.Deadline_Threads
		self.Deadline_UseGpu
		self.Deadline_ChooseGpu
		self.Deadline_RenderMode
		self.Deadline_MemoryUsage
		self.Deadline_StackSize
		self.Deadline_EnforceRenderOrder
		self.Deadline_SubmitSuspended
		self.Deadline_ReloadPlugin
		self.Deadline_ContinueOnError
		self.Deadline_BatchMode
		self.Deadline_UseNukeX
	#----------------------------------------------------------------------
	def _load_ui(self):
		""""""
		wig = Ui_Loader.load(self._get_ui_file(), parent_widget=self)
		isinstance(wig,DML_PYQT.QWidget)
		return wig
	#----------------------------------------------------------------------
	def _get_ui_file(self):
		""""""
		return os.path.join(os.path.dirname(__file__), "Submit_Gimped_To_Deadline.ui")
	#----------------------------------------------------------------------
	def _rebuild(self):
		""""""
	#----------------------------------------------------------------------
	def _on_knob_changed(self,nod,knb):
		""""""
		pass
	#----------------------------------------------------------------------
	def on_knob_changed(self,knb):
		""""""
		pass
	#----------------------------------------------------------------------
	def makeUI(self):
		return self
	#----------------------------------------------------------------------
	def updateValue(self):
		return None
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def update_Settings(self):
		""""""
		self._save_Settings()
		
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_Deadline_MachineListButton_clicked(self):
		""""""
		res = DML_Tools.DML_Deadline.Deadline_Commands.SelectMachineList(self.Deadline_MachineList.text())
		if not res == 'Action was cancelled by user':
			self.Deadline_MachineList.setText(res)
			self._save_Settings()
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_Deadline_LimitGroupsButton_clicked(self):
		""""""
		res = DML_Tools.DML_Deadline.Deadline_Commands.SelectLimitGroups(self.Deadline_LimitGroups.text())
		if not res == 'Action was cancelled by user':
			self.Deadline_LimitGroups.setText(res)
			self._save_Settings()
	#----------------------------------------------------------------------
	@DML_PYQT.Slot()
	def on_Deadline_DependenciesButton_clicked(self):
		""""""
		res = DML_Tools.DML_Deadline.Deadline_Commands.SelectDependencies()
		if not res == 'Action was cancelled by user':
			self.Deadline_Dependencies.setText(res)
			self._save_Settings()
			
	#----------------------------------------------------------------------
	def _build_render_values(self):
		""""""
		self._render_data_all_write_nodes = []
		self._render_data_all_psd_nodes   = []
		self._render_data_all_gimp_groups = []
		self._render_data_views_to_render = []

		self._render_data_gimped_psd_node_data = Layers_To_Gimped_PSD_Utils.get_Enabled_DML_Layers_To_Gimped_PSD_Dict()

		for item_data in self._render_data_gimped_psd_node_data:

			psd,grp,wrnds = item_data["psd"],item_data["grp"],item_data["allwrns"]

			self._render_data_all_write_nodes.extend(wrnds)
			self._render_data_all_gimp_groups.append(grp)
			self._render_data_all_psd_nodes.append(psd)

			for view in psd.knob("DML_Nuke_View_Selection").value().split():
				if not view in self._render_data_views_to_render:
					self._render_data_views_to_render.append(view)
	#----------------------------------------------------------------------
	def Submit_To_Deadline(self):
		""""""
		nuke.scriptSave()
		write_node_names = [node.fullName for node in self._render_data_all_write_nodes]
		NukeVersionMajor = int(nuke.env.get( 'NukeVersionMajor', '6' ))
		NukeVersionMinor = int(nuke.env.get( 'NukeVersionMinor', '0' ))
		BatchName = self.Deadline_JobName.text()+" Nuke To PSD"
		
		frame_ranges = nuke.FrameRanges(self.Deadline_FrameList.text())
		
		psd_build_data = Layers_To_Gimped_PSD_Utils.create_PSD_Build_Info_V2(frame_ranges.toFrameList())
		
		OutputFilenames  = []
		OutputDirectorys = []
		for location in build_psd_file_Locations(psd_build_data):
			OutputFilenames.append(location[1])
			OutputDirectorys.append(location[0])
			
		job_info = DML_Tools.DML_Deadline.Job_Data_Model.Job_Info_File(Plugin="Nuke",
														Frames=self.Deadline_FrameList.text(), 
														Name=self.Deadline_JobName.text(),
														Department=self.Deadline_Department.text(),
														Comment=self.Deadline_Comment.text(),
														Group=self.Deadline_Group.currentText(),
														BatchName=BatchName,
														Pool=self.Deadline_Pool.currentText(),
														SecondaryPool=self.Deadline_SecondaryPool.currentText(),
														Priority=self.Deadline_Priority.value(),
														ChunkSize=self.Deadline_ChunkSize.value(),
														ForceReloadPlugin=self.Deadline_ReloadPlugin.isChecked(),
														InitialStatus= "Suspended" if self.Deadline_SubmitSuspended.isChecked() else "Active",
														LimitGroups=self.Deadline_LimitGroups.text(),
														MachineLimit=self.Deadline_MachineLimit.value(),
														Machinelist=self.Deadline_MachineList.text(),
														OnJobComplete=self.Deadline_OnComplete.currentText(),
														ConcurrentTasks=self.Deadline_ConcurrentTasks.value(),
														LimitTasksToNumberOfCpus=self.Deadline_LimitConcurrentTasks.isChecked(),
														JobDependencies=self.Deadline_Dependencies.text(),
														IsBlacklist=self.Deadline_IsBlacklist.isChecked(),
														OutputFilenames=OutputFilenames,
														OutputDirectorys=OutputDirectorys
														)
		job_info.EnvironmentKeyValue["NUKE_PATH"] = "//isln-smb.ad.sgsco.int/aw_config/Git_Live_Code/Software/Nuke"
		
		plugin_info = DML_Tools.DML_Deadline.Job_Data_Model.Nuke_Plugin_Info(SceneFile=nuke.root().name(),
																   Version="{}.{}\n".format( NukeVersionMajor, NukeVersionMinor ) ,
																   NukeX=self.Deadline_UseNukeX.isChecked(),
																   BatchMode=self.Deadline_BatchMode.isChecked(),
																   ContinueOnError=self.Deadline_ContinueOnError.isChecked(),
																   RenderMode="Render Full Resolution",
																   UseGpu=self.Deadline_UseGpu.isChecked(),
																   GpuOverride=self.Deadline_ChooseGpu.value(),
																   Threads=self.Deadline_Threads.value(),
																   RamUse=self.Deadline_MemoryUsage.value(),
																   StackSize=self.Deadline_StackSize.value(),
																   Views=','.join(self._render_data_views_to_render) ,
																   WriteNodes=write_node_names)
		
		nuke_deadline_submiter = DML_Tools.DML_Deadline.Job_Data_Model.Job_Submitter(job_info, plugin_info)
		nuke_deadline_submiter.Submit_the_job_to_Deadline()
			
		build_cont  = len(psd_build_data["builds"])
		psd_build_data = json.dumps(psd_build_data)
			
		job_info = DML_Tools.DML_Deadline.Job_Data_Model.Job_Info_File(Plugin="GimpPSD",
														Frames="0-{}".format(build_cont-1), 
														Name=self.Deadline_JobName.text()+"_Gimped_PSD",
														Department=self.Deadline_Department.text(),
														Comment=self.Deadline_Comment.text(),
														Group=self.Deadline_Group.currentText(),
														BatchName=BatchName,
														Pool=self.Deadline_Pool.currentText(),
														SecondaryPool=self.Deadline_SecondaryPool.currentText(),
														Priority=self.Deadline_Priority.value(),
														ChunkSize=1,
														ForceReloadPlugin=self.Deadline_ReloadPlugin.isChecked(),
														LimitGroups=self.Deadline_LimitGroups.text(),
														MachineLimit=self.Deadline_MachineLimit.value(),
														Machinelist=self.Deadline_MachineList.text(),
														OnJobComplete=self.Deadline_OnComplete.currentText(),
														ConcurrentTasks=1,
														LimitTasksToNumberOfCpus=True,
														JobDependencies=nuke_deadline_submiter.jobId,
														IsBlacklist=self.Deadline_IsBlacklist.isChecked()
														)
		
		plugin_info = GimpPSD_Plugin_Info(jsondata=psd_build_data)
		gimp_deadline_submiter = DML_Tools.DML_Deadline.Job_Data_Model.Job_Submitter(job_info, plugin_info)
		gimp_deadline_submiter.Submit_the_job_to_Deadline()
		nuke.executeInMainThread( nuke.message, "2 Jobs Submissions complete. " + str(nuke_deadline_submiter.jobId) + "," + str(gimp_deadline_submiter.jobId) +" Job submitted to Deadline." )
		
	#----------------------------------------------------------------------
	def _make_Save_Settings_Connections(self):
		""""""
		for child in self.findChildren(DML_PYQT.QLineEdit):
			objectName = child.objectName()
			if objectName.startswith("Deadline_"):
				child.editingFinished.connect(self.update_Settings)
				
		for child in self.findChildren(DML_PYQT.QSpinBox):
			objectName = child.objectName()
			if objectName.startswith("Deadline_"):
				child.valueChanged.connect(self.update_Settings)
				
		for child in self.findChildren(DML_PYQT.QCheckBox):
			objectName = child.objectName()
			if objectName.startswith("Deadline_"):
				child.toggled.connect(self.update_Settings)
				
		for child in self.findChildren(DML_PYQT.QComboBox):
			objectName = child.objectName()
			if objectName.startswith("Deadline_"):
				child.currentIndexChanged.connect(self.update_Settings)
	#----------------------------------------------------------------------
	def _save_Settings(self):
		""""""
		nuke_root = nuke.root()
		
		if not "submit_gimped_to_deadline_settings" in nuke_root.knobs():
			settings_knb = nuke.String_Knob("submit_gimped_to_deadline_settings")
			settings_knb.setVisible(False)
			nuke_root.addKnob(settings_knb)
		else:
			settings_knb = nuke_root.knobs()["submit_gimped_to_deadline_settings"]
			
		LineEdits = {}
		SpinBoxs  = {}
		CheckBoxs = {}
		ComboBoxs = {}
		for child in self.findChildren(DML_PYQT.QLineEdit):
			objectName = child.objectName()
			if objectName.startswith("Deadline_"):
				LineEdits[objectName] = child.text()
				
		for child in self.findChildren(DML_PYQT.QSpinBox):
			objectName = child.objectName()
			if objectName.startswith("Deadline_"):
				SpinBoxs[objectName] = child.value()
				
		for child in self.findChildren(DML_PYQT.QCheckBox):
			objectName = child.objectName()
			if objectName.startswith("Deadline_"):
				CheckBoxs[objectName] = child.isChecked()
				
		for child in self.findChildren(DML_PYQT.QComboBox):
			objectName = child.objectName()
			if objectName.startswith("Deadline_"):
				ComboBoxs[objectName] = child.currentText()
				
		data = dict(LineEdits=LineEdits,SpinBoxs=SpinBoxs,CheckBoxs=CheckBoxs,ComboBoxs=ComboBoxs)
		settings_knb.setText(repr(data))
	#----------------------------------------------------------------------
	def _load_Settings(self):
		""""""
		nuke_root = nuke.root()
		
		if "submit_gimped_to_deadline_settings" in nuke_root.knobs():
			settings_knb = nuke_root.knobs()["submit_gimped_to_deadline_settings"]
			data = settings_knb.getText()
			if data == '':
				data={}
			else:
				data = eval(settings_knb.getText())
			LineEdits = data.get("LineEdits",{})
			SpinBoxs  = data.get("SpinBoxs",{})
			CheckBoxs = data.get("CheckBoxs",{})
			ComboBoxs = data.get("ComboBoxs",{})
			
			for objectName in LineEdits:
				child = self.findChild(DML_PYQT.QLineEdit,objectName)
				if isinstance(child,DML_PYQT.QLineEdit):
					child.setText(LineEdits[objectName])
				
			for objectName in SpinBoxs:
				child = self.findChild(DML_PYQT.QSpinBox,objectName)
				if isinstance(child,DML_PYQT.QSpinBox):
					child.setValue(SpinBoxs[objectName])
				
			for objectName in CheckBoxs:
				child = self.findChild(DML_PYQT.QCheckBox,objectName)
				if isinstance(child,DML_PYQT.QCheckBox):
					child.setChecked(CheckBoxs[objectName])
				
			for objectName in ComboBoxs:
				child = self.findChild(DML_PYQT.QComboBox,objectName)
				if isinstance(child,DML_PYQT.QComboBox):
					val = ComboBoxs[objectName]
					vals = [child.itemText(i) for i in range(child.count())]
					if val in vals:
						child.setCurrentIndex(vals.index(val))
		
class DeadlineDialog( nukescripts.PythonPanel ):
	pools = []
	groups = []

	def __init__( self ):
		super( DeadlineDialog, self).__init__( "Submit To Deadline", "com.dml.tools.gimpedsubmit" )
		cmd = __name__+'.Submit_Gimped_To_Deadline_Widget()'
		knb = nuke.PyCustom_Knob("submit_widget", "", cmd)
		self.addKnob(knb)
		self.setMinimumSize( 625, 550 )
		
	def ShowDialog( self ):
		return nukescripts.PythonPanel.showModalDialog( self )

def submit_Gimped_To_DeadLine():
	dialog = DeadlineDialog()
	# Show the dialog.
	success = dialog.ShowDialog()
	if success:
		wig_knob = dialog.knobs()["submit_widget"]
		wig_obj = wig_knob.getObject()
		wig_obj.Submit_To_Deadline()