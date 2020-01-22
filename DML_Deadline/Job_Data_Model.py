
import os
import Command_Access
import Deadline_Commands

Active = "Active"
Suspended = "Suspended"

class ScheduledTypes():
	none  = "None"
	once  = "Once"
	daily = "Daily"
	
#----------------------------------------------------------------------
def build_Options_Line(optName,optVal):
	""""""
	return "{}={}".format(optName,optVal)

########################################################################
class Job_Info_File(object):
	_counter = 1
	#----------------------------------------------------------------------
	def __init__(self,
				 Plugin="",
				 Frames="",
				 Name="Untitled",
				 Department="",
				 Comment="",
				 Group="none",
				 BatchName="",
	             Pool="none",
	             SecondaryPool="",
	             Priority=50,
	             ChunkSize=1,
	             ForceReloadPlugin=False,
	             SynchronizeAllAuxiliaryFiles=False,
	             InitialStatus="Active",
	             LimitGroups="",
	             MachineLimit=0,
	             MachineLimitProgress=-1.0,
	             Machinelist="",
				 OverrideAutoJobCleanup=False,
				 OverrideJobCleanup=False,
				 OverrideJobCleanupType=None,
				 JobCleanupDays=0,
	             OnJobComplete="Nothing",
	             ConcurrentTasks=1,
	             LimitTasksToNumberOfCpus=True,
	             Sequential=False,
	             Interruptible=False,
	             SuppressEvents=False,
	             MinRenderTimeSeconds=0,
	             MinRenderTimeMinutes=0,
	             TaskTimeoutSeconds=0,
	             TaskTimeoutMinutes=0,
	             OnTaskTimeout="Error",
	             EnableAutoTimeout=False,
	             EnableTimeoutsForScriptTasks=False,
	             JobDependencies='',
	             JobDependencyPercentage=-1,
	             IsFrameDependent=False,
	             FrameDependencyOffsetStart=0,
	             FrameDependencyOffsetEnd=0,
	             ResumeOnCompleteDependencies=True,
	             ResumeOnDeletedDependencies=False,
	             ResumeOnFailedDependencies=False,
	             RequiredAssets='',
	             ScriptDependencies="",
	             ScheduledType=None,
	             ScheduledStartDateTime="dd/MM/yyyy HH:mm",
	             ScheduledDays=1,
	             OutputFilenames=[],
	             OutputDirectorys=[],
	             NotificationTargets="",
	             ClearNotificationTargets=False,
	             NotificationEmails="",
	             OverrideNotificationMethod=False,
	             EmailNotification=False,
	             PopupNotification=False,
	             NotificationNote="",
	             PreJobScript="",
	             PostJobScript="",
	             PreTaskScript="",
	             PostTaskScript="",
	             TileJob=False,
	             TileJobFrame=0,
	             TileJobTilesInX=0,
	             TileJobTilesInY=0,
	             TileJobTileCount=0,
	             OverrideJobFailureDetection=False,
	             FailureDetectionJobErrors=0,
	             OverrideTaskFailureDetection=False,
	             FailureDetectionTaskErrors=0,
	             IgnoreBadJobDetection=False,
	             SendJobErrorWarning=False,
	             ExtraInfo = [],
	             ExtraInfoKeyValues={},
	             IncludeEnvironment=False,
	             UseJobEnvironmentOnly=False,
	             CustomPluginDirectory=False,
	             EnvironmentKeyValue={},
	             useScheduling=False,
	             useNotifications=False,
	             IsBlacklist=False,
	             Submit_To_ShotGun=False,
	             SG_TaskName="", 
	             SG_ProjectName="", 
	             SG_EntityName="", 
	             SG_VersionName="", 
	             SG_Description="", 
	             SG_UserName="", 
	             SG_Path_To_Frames="",
	             SG_Path_To_File="",
	             SG_TaskId=0, 
	             SG_ProjectId=0, 
	             SG_EntityId=0, 
	             SG_EntityType=""):
		
		"""
			General
			
				--Plugin
					| Specifies the plugin to use.
					| Must match an existing plugin in the repository.
					|
				--Frames
					| Specifies the frame range of the render job
					| 
				--Name
					| Specifies the name of the job
					| (default = Untitled).
					| 
				--Comment
					| Specifies a comment for the job
					| (default = blank).
					| 
				--Department
					| Specifies the department that the job belongs to.
					| This is simply a way to group jobs together,
					| and does not affect rendering in any way
					| (default = blank).
					| 
				--BatchName
					| Specifies an optional name to logically group jobs together
					| (default = blank).
					| 
				--UserName
					| Specifies the jobs user.
					| (default = current user).
					| 
				--MachineName
					| Specifies the machine the job was submitted from.
					| (default = current machine).
					|
				--Pool
					| Specifies the pool that the job is being submitted to
					| (default = none).
					| 
				--SecondaryPool
					| Specifies the secondary pool that the job can spread to
					| if machines are available.
					| If not specified, the job will not use a secondary pool.
					| (default = none).
					| 
				--Group
					| Specifies the group that the job is being submitted to
					| (default = none).
					| 
				--Priority
					| Specifies the priority of a job with 0 being the lowest
					| The maximum priority can be configured in the Job Settings
					| of the Repository Options,
					| and defaults to 100.
					| (default = 50). 
					| 
				--ChunkSize
					| Specifies how many frames to render per task
					| (default = 1).
					| 
				--ConcurrentTasks
					| Specifies the maximum number of tasks that a slave can render at a time
					| This is useful for script plugins that support multithreading.
					| (default = 1). 
					| 
				--LimitTasksToNumberOfCpus
					| If ConcurrentTasks is greater than 1, 
					| setting this to true will ensure that a slave will not dequeue more tasks than it has processors 
					| (default = true).
					| 
				--OnJobComplete
					| Specifies what should happen to a job after it completes 
					| (default = Nothing).
					| 
				--SynchronizeAllAuxiliaryFiles
					| If enabled, all job files (as opposed to just the job info and plugin info files) 
					| will be synchronized by the Slave between tasks for this job
					| Note that this can add significant network overhead, 
					| and should only be used if you plan on manually editing any of the files that are being submitted with the job.
					| (default = false). 
					| 
				--ForceReloadPlugin
					| Specifies whether or not to reload the plugin between subsequent frames of a job
					| This deals with memory leaks or applications that do not unload all job aspects properly.
					| (default = false). 
					| 
				--Sequential
					| Sequential rendering forces a slave to render the tasks of a job in order. 
					| If an earlier task is ever requeued, 
					| the slave won't go back to that task until it has finished the remaining tasks in order 
					| (default = false).
					| 
				--SuppressEvents
					| If true, the job will not trigger any event plugins while in the queue
					| (default = false).
					|
				--Protected
					| If enabled, the job can only be deleted by the jobs user, a super user, or a user that belongs to a user group that has permissions to handle protected jobs.
					| Other users will not be able to delete the job, and the job will also not be cleaned up by Deadlines automatic house cleaning.
					| (default = false).
					|
				--InitialStatus
					| Specifies what status the job should be in immediately after submission
					| (default = Active).
					| 
				--NetworkRoot
					| Specifies the repository that the job will be submitted to.
					| This is required if you are using more than one repository.
					| (default = current default repository for the machine from which submission is occurring).
					| 
					
			- Timeout Options
			
				--MinRenderTimeSeconds
					| Specifies the minimum time, in seconds, a slave should render a task for, otherwise an error will be reported
					| Note that if MinRenderTimeSeconds and MinRenderTimeMinutes are both specified, MinRenderTimeSeconds will be ignored.
					| (default = 0, which means no minimum).
					| 
				--MinRenderTimeMinutes
					| Specifies the minimum time, in minutes, a slave should render a task for, otherwise an error will be reported
					| Note that if MinRenderTimeSeconds and MinRenderTimeMinare both specified, MinRenderTimeSeconds will be ignored.
					| (default = 0, which means no minimum). 
					| 
				--TaskTimeoutSeconds
					| Specifies the time, in seconds, a slave has to render a task before it times out
					| Note that if TaskTimeoutSeconds and TaskTimeoutMinutes are both specified, TaskTimeoutSeconds will be ignored.: 
					| (default = 0, which means unlimited).
					| 
				--TaskTimeoutMinutes
					| Specifies the time, in minutes, a slave has to render a task before it times out
					| Note that if TaskTimeoutSeconds and TaskTimeoutMinutes are both specified, TaskTimeoutSeconds will be ignored.
					| (default = 0, which means unlimited).
					| 
				--StartJobTimeoutSeconds
					| Specifies the time, in seconds, a Worker has to start a render job before it times out.
					| Note that if StartJobTimeoutSeconds and StartJobTimeoutMinutes are both specified, StartJobTimeoutSeconds will be ignored.
					| (default = 0, which means unlimited)
					| 
				--StartJobTimeoutMinutes
					| Specifies the time, in minutes, a Worker has to start a render job before it times out.
					| Note that if StartJobTimeoutSeconds and StartJobTimeoutMinutes are both specified, StartJobTimeoutSeconds will be ignored.
					| (default = 0, which means unlimited)
					| 
				--InitializePluginTimeoutSeconds
					| Specifies the maximum time, in seconds, a Worker has to load the application plugin before it times out.
					| (default = 0, which means unlimited)
					| 
				--OnTaskTimeout
					| Specifies what should occur if a task times out
					| (default = Error).
					| 
				--EnableTimeoutsForScriptTasks
					| If true, then the timeouts for this job will also affect its pre/post job scripts,
					| if any are defined
					| (default = false).
					|
				--EnableFrameTimeouts
					| If true, then the timeouts for this job are Frame based instead of Task based.
					|
				--EnableAutoTimeout
					| If true, a slave will automatically figure out if it has been rendering too long
					| based on some Repository Configuration settings and the render times of previously completed tasks
					| (default = false).
					|
			
			- Interruptible Options
			
				--Interruptible
					| Specifies if tasks for a job can be interrupted by a higher priority job during rendering
					| (default = false).
					| 
				--InterruptiblePercentage
					| A task for this job will only be interrupted if the task progress is less than or equal to this value.
					| 
				--RemTimeThreshold
					| The remaining time (in seconds) that this Job must have left more than in order to be interruptible.
					| 
			
			- Notification Options
			
				--NotificationTargets
					| A list of users, separated by commas, who should be notified when the job is completed
					| (default = blank).
					| 
				--ClearNotificationTargets
					| If enabled, all of the job's notification targets will be removed
					| (default = false)
					| 
				--NotificationEmails
					| A list of additional email addresses, separated by commas, to send job notifications to
					| (default = blank).
					| 
				--OverrideNotificationMethod
					| If the job user's notification method should be ignored
					| (default = false).
					| 
				--EmailNotification
					| If overriding the job user's notification method, whether to use email notification
					| (default = false).
					| 
				--PopupNotification
					| If overriding the job user's notification method, whether to use popup notification
					| (default = false).
					| 
				--NotificationNote
					| A note to append to the notification email sent out when the job is complete
					| (default = blank).
					| Separate multiple lines with [EOL] 
					|
			
			- Machine Limit Options
			
				--MachineLimit
					| Specifies the maximum number of machines this job can be rendered on at the same time
					| (default = 0, which means unlimited).
					| 
				--MachineLimitProgress
					| If set, the slave rendering the job will give up its current machine limit lock 
					| when the current task reaches the specified progress.
					| If negative, this feature is disabled
					| The usefulness of this feature is directly related to the progress reporting capabilities of the individual plugins.
					| (default = -1.0). 
					| 
				--Whitelist
					| Specifies which slaves are on the job's whitelist
					| If both a whitelist and a blacklist are specified, only the whitelist is used.
					| (default = blank).
					| 
				--Blacklist
					| Specifies which slaves are on the job's blacklist
					| If both a whitelist and a blacklist are specified, only the whitelist is used.
					| (default = blank). 
					| 
				--NotificationNote
					| A note to append to the notification email sent out when the job is complete
					| (default = blank).
					| Separate multiple lines with [EOL] 
					|	
					
			- Limit Options
			
				--LimitGroups
					| Specifies the limit groups that this job is a member of
					| (default = blank).
					|
					
			- Dependency Options
			
				--JobDependencies
					| Specifies what jobs must finish before this job will resume 
					| These dependency jobs must be identified using their unique job ID, 
					| which is outputted after the job is submitted, 
					| and can be found in the Monitor in the "Job ID" column.
					| (default = blank).
					| 
				--JobDependencyPercentage
					| If between 0 and 100, 
					| this job will resume when all of its job dependencies have completed the specified percentage number of tasks. 
					| If -1, this feature will be disabled 
					| (default = -1).
					| 
				--IsFrameDependent
					| Specifies whether or not the job is frame dependent.0 to 100> :
					| (default = false)
					| 
				--FrameDependencyOffsetStart
					| If the job is frame dependent, this is the start frame offset 
					| (default = 0).
					| 
				--FrameDependencyOffsetEnd
					| If the job is frame dependent, this is the end frame offset 
					| (default = 0).: 
					| 
				--ResumeOnCompleteDependencies
					| Specifies whether or not the dependent job should resume when its dependencies are complete 
					| (default = true)
					| 
				--ResumeOnDeletedDependencies
					| Specifies whether or not the dependent job should resume when its dependencies have been deleted 
					| (default = false).	
					| 
				--ResumeOnFailedDependencies
					| Specifies whether or not the dependent job should resume when its dependencies have failed 
					| (default = false).	
					| 
				--RequiredAssets
					| Specifies what asset files must exist before this job will resume. 
					| These asset paths must be identified using full paths, 
					| and multiple paths can be separated with commas. 
					| If using frame dependencies, you can replace padding in a sequence with the '' characters, 
					| and a task for the job will only be resumed when the required assets for the task's frame) exist.
					| (default = blank)
					| 
				--ScriptDependencies
					| Specifies what Python script files will be executed to determine if a job can resume 
					| These script paths must be identified using full paths, 
					| and multiple paths can be separated with commas. 
					| See the Scripting section of the documentation for more information on script dependencies.
					| (default = blank).
					|
					
			- Failure Detection Options
			
				--OverrideJobFailureDetection
					| If true, the job will ignore the global Job Failure Detection settings and instead use its own.
					| (default = false).
					| 
				--FailureDetectionJobErrors
					| If OverrideJobFailureDetection is true, this sets the number of errors before the job fails. If set to 0, job failure detection will be disabled.
					| (default = false).
					| 
				--OverrideTaskFailureDetection
					| If true, the job will ignore the global Task Failure Detection settings and instead use its own.
					| (default = false).
					| 
				--FailureDetectionTaskErrors
					| If OverrideTaskFailureDetection is true, this sets the number of errors before a task for the job fails. If set to 0, task failure detection will be disabled.
					| 
				--IgnoreBadJobDetection
					| If true, Workers will never mark the job as bad for themselves. 
					| This means that they will continue to make attempts at jobs that often report errors until the job is complete, or until it fails
					| 
				--SendJobErrorWarning
					| If the job should send warning notifications when it reaches a certain number of errors.
					| (default = false)
					| 
					
			
			- Cleanup Options
			
				--DeleteOnComplete
					| Specifies whether or not the job should be automatically deleted after it completes
					| (default = false).
					| 
				--ArchiveOnComplete
					| Specifies whether or not the job should be automatically archived after it completes 
					| (default = false).
					| 
				--OverrideAutoJobCleanup
					| If true, the job will ignore the global Job Cleanup settings and instead use its own.
					| (default = false).
					| 
				--OverrideJobCleanup
					| If OverrideAutoJobCleanup is true, this will determine if the job should be automatically cleaned up or not.
					| (default = false).
					| 
				--JobCleanupDays
					| If OverrideAutoJobCleanup and OverrideJobCleanup are both true, this is the number of days to keep the job before cleaning it up.
					| (default = false).
					| 
				--OverrideJobCleanupType
					| If OverrideAutoJobCleanup and OverrideJobCleanup are both true, this is the job cleanup mode.
					| 
					
			- Scheduling Options
			
				--ScheduledType
					| Specifies whether or not you want to schedule the job 
					| (default = None).
					| 
				--ScheduledStartDateTime
					| The date/time at which the job will run. The start date/time must match the specified format. Here'sxplanation:
					| dd: The day of the month. Single-digit days must have a leading zero.
					| MM: The numeric month. Single-digit months must have a leading zero.
					| yyyy: The year in four digits, including the century.
					| HH: The hour in a 24-hour clock. Single-digit hours must have a leading zero.
					| mm: The minute. Single-digit minutes must have a leading zero.
					| 
				--ScheduledDays
					| If scheduling a Daily job, this is the day interval for when the job runs
					| (default = 1).
					|
				--JobDelay
					| A start time delay. If there is no ScheduledStartDateTime this delay will be applied to the submission date.
					| The delay value is represented by the number of days, hours, minutes, and seconds, all separated by colons.
					|
					
			- Script Options
			
				--PreJobScript
					| Specifies a full path to a python script to execute when the job initially starts rendering
					| (default = blank).
					| 
				--PostJobScript
					| Specifies a full path to a python script to execute when the job completes
					| (default = blank).
					| 
				--PreTaskScript
					| Specifies a full path to a python script to execute before each task starts rendering
					| (default = blank).
					| 
				--PostTaskScript
					| Specifies a full path to a python script to execute after each task completes
					| (default = blank).
					|
			
			- Event Opt-Ins Options
			
				--EventOptIns
					| Specifies which events will trigger for the job if the Event Plugins are configured per job.
					| This is a comma-separated list of all events that you want to trigger for this job. For example
					| EventOptIns=Shotgun,Puppet,FTrack
					|
						
			- Environment Options
			
				--EnvironmentKeyValue
					| Specifies environment variables to set when the job renders. This option is numbered, starting with 0 (EnvironmentKeyValue0),
					| to handle multiple environment variables. For each additional variable, just increase the number (EnvironmentKeyValue1, EnvironmentKeyValue2, etc).
					| Note that these variables are only applied to the rendering process, so they do not persist between jobs.
					|
				--IncludeEnvironment
					| If true, the submission process will automatically grab all the environment variables from the submitters current environment
					| and set them in the jobs environment variables.
					| Note that these variables are only applied to the rendering process, so they do not persist between jobs.
					|
				--UseJobEnvironmentOnly
					| If true, only the jobs environment variables will be used at render time
					| If False, the jobs environment variables will be merged with the Workers current environment
					| with the jobs variables overwriting any existing ones with the same name.
					|
				--CustomPluginDirectory
					| If specified, the job will look for for the plugin it needs to render in this location.
					| If it does not exist in this location, it will fall back on the Repository plugin directory.
					| For example, if you are rendering with a plugin called MyPlugin, and it exists in \server\development\plugins\MyPlugin
					| you would set CustomPluginDirectory=\server\development\plugins.
					|
					
			- Output Options
			
				--OutputFilename#
					| Specifies the output image filenames for each frame. 
					| This allows the Monitor to display the "View Output Image" context menu option in the task list. 
					| There is no minimum or maximum limit to padding length supported. 
					| A padding of 4 x  is very common in many applications. 
					| If the filename is a full path, then the OutputDirectory option is not needed. 
					| This option is numbered, starting with 0 (OutputFilename0), to handle multiple output file names per frame. 
					| For each additional file name, just increase the number (OutputFilename1, OutputFilename2, etc).
					| (default = blank)
					| 
				--OutputFilename#Tile?
					| Specifies the output image filenames for each task of a Tile job (default = blank).
					| This allows the Monitor to display the View Output Imag context menu option in the task list for Tile jobs.
					| The # is used to support multiple outputs per frame (see OutputFilename# above),
					| and the ? is used to specify the output for each task in the Tile job.
					| For example, a Tile job with 2 outputs and 2 tiles would specify OutputFilename0Tile0, OutputFilename0Tile1, OutputFilename1Tile0
					| and OutputFilename1Tile1 (TILE jobs only).
					| 
				--OutputDirectory#
					| Specifies the output image directory for the job. 
					| This allows the Monitor to display the "Explore Output" context menu option in the job list. 
					| This option is numbered, starting with 0 (OutputDirectory0), to handle multiple output directories per frame. 
					| For each additional directory, just increase the number (OutputDirectory1, OutputDirectory2, etc).
					| (default = blank)
					|
					
			- Tile Job Options
			
				--TileJob
					| If this job is a tile job
					| (default = false).
					| 
				--TileJobFrame
					| The frame that the tile job is rendering
					| (default = 0).
					| 
				--TileJobTilesInX
					| The number of tiles in X for a tile job
					| (default = 0).
					| This should be specified with the TileJobTilesInY option below.: 
					| 
				--TileJobTilesInY
					| The number of tiles in Y for a tile job
					| (default = 0).
					| This should be specified with the TileJobTilesInX option above.
					| 
				--TileJobTileCount
					| The number of tiles for a tile job
					| (default = 0).
					| This is an alternative to specifying the TileJobTilesInX and TileJobTilesInY options above.
					| 
		"""
		
		self.Plugin                       = Plugin
		self.Frames                       = Frames
		self.Name                         = Name
		self.Department                   = Department
		self.Comment                      = Comment
		self.Group                        = Group
		self.Pool                         = Pool
		self.BatchName                    = BatchName
		self.SecondaryPool                = SecondaryPool
		self.Priority                     = Priority
		self.ChunkSize                    = ChunkSize
		self.ForceReloadPlugin            = ForceReloadPlugin
		self.SynchronizeAllAuxiliaryFiles = SynchronizeAllAuxiliaryFiles
		self.InitialStatus                = InitialStatus
		self.LimitGroups                  = LimitGroups
		self.MachineLimit                 = MachineLimit
		self.MachineLimitProgress         = MachineLimitProgress
		self.Machinelist                  = Machinelist
		self.OnJobComplete                = OnJobComplete
		self.ConcurrentTasks              = ConcurrentTasks
		self.LimitTasksToNumberOfCpus     = LimitTasksToNumberOfCpus
		self.Sequential                   = Sequential
		self.Interruptible                = Interruptible
		self.SuppressEvents               = SuppressEvents
		self.MinRenderTimeSeconds         = MinRenderTimeSeconds
		self.MinRenderTimeMinutes         = MinRenderTimeMinutes
		self.TaskTimeoutSeconds           = TaskTimeoutSeconds
		self.TaskTimeoutMinutes           = TaskTimeoutMinutes
		self.OnTaskTimeout                = OnTaskTimeout
		self.EnableAutoTimeout            = EnableAutoTimeout
		self.EnableTimeoutsForScriptTasks = EnableTimeoutsForScriptTasks
		self.JobDependencies              = JobDependencies
		self.JobDependencyPercentage      = JobDependencyPercentage
		self.IsFrameDependent             = IsFrameDependent
		self.FrameDependencyOffsetStart   = FrameDependencyOffsetStart
		self.FrameDependencyOffsetEnd     = FrameDependencyOffsetEnd
		self.ResumeOnCompleteDependencies = ResumeOnCompleteDependencies
		self.ResumeOnDeletedDependencies  = ResumeOnDeletedDependencies
		self.ResumeOnFailedDependencies   = ResumeOnFailedDependencies
		self.RequiredAssets               = RequiredAssets
		self.ScriptDependencies           = ScriptDependencies
		self.useScheduling                = useScheduling
		self.useNotifications             = useNotifications
		self.ScheduledType                = ScheduledType
		self.ScheduledStartDateTime       = ScheduledStartDateTime
		self.ScheduledDays                = ScheduledDays
		self.OutputFilenames              = OutputFilenames
		self.OutputDirectorys             = OutputDirectorys
		self.NotificationTargets          = NotificationTargets
		self.ClearNotificationTargets     = ClearNotificationTargets
		self.NotificationEmails           = NotificationEmails
		self.OverrideNotificationMethod   = OverrideNotificationMethod
		self.EmailNotification            = EmailNotification
		self.PopupNotification            = PopupNotification
		self.NotificationNote             = NotificationNote
		self.PreJobScript                 = PreJobScript
		self.PostJobScript                = PostJobScript
		self.PreTaskScript                = PreTaskScript
		self.PostTaskScript               = PostTaskScript
		self.TileJob                      = TileJob
		self.TileJobFrame                 = TileJobFrame
		self.TileJobTilesInX              = TileJobTilesInX
		self.TileJobTilesInY              = TileJobTilesInY
		self.TileJobTileCount             = TileJobTileCount
		self.IsBlacklist                  = IsBlacklist
		self.ExtraInfo                    = ExtraInfo
		self.ExtraInfoKeyValues           = ExtraInfoKeyValues
		self.IncludeEnvironment           = IncludeEnvironment
		self.UseJobEnvironmentOnly        = UseJobEnvironmentOnly
		self.EnvironmentKeyValue          = EnvironmentKeyValue
		self.CustomPluginDirectory        = CustomPluginDirectory
		self.OverrideJobFailureDetection  = OverrideJobFailureDetection
		self.FailureDetectionJobErrors    = FailureDetectionJobErrors
		self.OverrideTaskFailureDetection = OverrideTaskFailureDetection
		self.FailureDetectionTaskErrors   = FailureDetectionTaskErrors
		self.IgnoreBadJobDetection        = IgnoreBadJobDetection
		self.SendJobErrorWarning          = SendJobErrorWarning
		self.OverrideAutoJobCleanup       = OverrideAutoJobCleanup
		self.OverrideJobCleanup           = OverrideJobCleanup
		self.OverrideJobCleanupType       = OverrideJobCleanupType
		self.JobCleanupDays               = JobCleanupDays
		self.Submit_To_ShotGun            = Submit_To_ShotGun
		self.SG_TaskName                  = SG_TaskName
		self.SG_ProjectName               = SG_ProjectName
		self.SG_EntityName                = SG_EntityName 
		self.SG_VersionName               = SG_VersionName 
		self.SG_Description               = SG_Description 
		self.SG_UserName                  = SG_UserName 
		self.SG_Path_To_Frames            = SG_Path_To_Frames
		self.SG_Path_To_File              = SG_Path_To_File
		self.SG_TaskId                    = SG_TaskId
		self.SG_ProjectId                 = SG_ProjectId 
		self.SG_EntityId                  = SG_EntityId 
		self.SG_EntityType                = SG_EntityType

	def create_job_string(self):
		lines = []
		lines.append(build_Options_Line("Plugin", self.Plugin))
		lines.append(build_Options_Line("Frames", self.Frames))
		lines.append(build_Options_Line("Name", self.Name))
		lines.append(build_Options_Line("Department", self.Department))
		lines.append(build_Options_Line("Comment", self.Comment))
		lines.append(build_Options_Line("Group", self.Group))
		lines.append(build_Options_Line("Pool", self.Pool))
		lines.append(build_Options_Line("SecondaryPool", self.SecondaryPool))
		lines.append(build_Options_Line("Priority", self.Priority))
		lines.append(build_Options_Line("InitialStatus", self.InitialStatus))
		lines.append(build_Options_Line("OnJobComplete", self.OnJobComplete))
		
		if len(self.BatchName):
			lines.append(build_Options_Line("BatchName", self.BatchName))
			
		if self.ChunkSize > 1:
			lines.append(build_Options_Line("ChunkSize", self.ChunkSize))
				
		if self.ConcurrentTasks > 1:
			lines.append(build_Options_Line("ConcurrentTasks", self.ConcurrentTasks))
			lines.append(build_Options_Line("LimitTasksToNumberOfCpus", self.LimitTasksToNumberOfCpus))
			
		if self.ForceReloadPlugin:
			lines.append("ForceReloadPlugin=true")
			
		if self.SynchronizeAllAuxiliaryFiles:
			lines.append("SynchronizeAllAuxiliaryFiles=true")
			
		if len(self.LimitGroups):
			lines.append(build_Options_Line("LimitGroups", self.LimitGroups))
			
		if self.MachineLimit:
			lines.append(build_Options_Line("MachineLimit", self.MachineLimit))
			
		if self.MachineLimitProgress:
			lines.append(build_Options_Line("MachineLimitProgress", self.MachineLimitProgress))
			
		if self.Machinelist:
			if self.IsBlacklist:
				lines.append(build_Options_Line("Blacklist", self.Machinelist))
			else:
				lines.append(build_Options_Line("Whitelist", self.Machinelist))
		
		if self.Sequential:
			lines.append("Sequential=true")
		
		if self.Interruptible:
			lines.append("Interruptible=true")
		
		if self.SuppressEvents:
			lines.append("SuppressEvents=true")
					
		if len(self.EnvironmentKeyValue):
			for index, item in enumerate(self.EnvironmentKeyValue.items()):
				lines.append("EnvironmentKeyValue%i=%s=%s" % (index, item[0], str(item[1]) ) )
				
		if self.IncludeEnvironment:
			lines.append("IncludeEnvironment=true")
			
		if self.UseJobEnvironmentOnly:
			lines.append("UseJobEnvironmentOnly=true")
			
		if self.OverrideAutoJobCleanup and self.OverrideJobCleanup:
			if self.JobCleanupDays > 0 or self.OverrideJobCleanupType is not None:
				lines.append("OverrideAutoJobCleanup=true")
				lines.append("OverrideJobCleanup=true")
				
				if self.JobCleanupDays > 0:
					lines.append(build_Options_Line("JobCleanupDays", self.JobCleanupDays))
					
				if self.OverrideJobCleanupType is not None:
					lines.append(build_Options_Line("OverrideJobCleanupType", self.OverrideJobCleanupType))
		
		if self.OverrideJobFailureDetection and self.FailureDetectionJobErrors > 0:
			lines.append("OverrideJobFailureDetection=true")
			lines.append(build_Options_Line("FailureDetectionJobErrors", self.FailureDetectionJobErrors))
			
		if self.OverrideTaskFailureDetection and self.FailureDetectionTaskErrors > 0:
			lines.append("OverrideTaskFailureDetection=true")
			lines.append(build_Options_Line("FailureDetectionTaskErrors", self.FailureDetectionTaskErrors))
			
		if self.IgnoreBadJobDetection:
			lines.append("IgnoreBadJobDetection=true")
		
		if self.SendJobErrorWarning:
			lines.append("SendJobErrorWarning=true")
			
		if self.MinRenderTimeMinutes:
			lines.append(build_Options_Line("MinRenderTimeMinutes", self.MinRenderTimeMinutes))
			
		if self.MinRenderTimeSeconds and not self.MinRenderTimeMinutes:
			lines.append(build_Options_Line("MinRenderTimeSeconds", self.MinRenderTimeSeconds))
		
		if self.TaskTimeoutMinutes:
			lines.append(build_Options_Line("TaskTimeoutMinutes", self.TaskTimeoutMinutes))
			
		if self.TaskTimeoutSeconds and not self.TaskTimeoutMinutes:
			lines.append(build_Options_Line("TaskTimeoutSeconds", self.TaskTimeoutSeconds))
		
		if self.TaskTimeoutSeconds or self.TaskTimeoutMinutes:
			if self.OnTaskTimeout != "Error":
				lines.append(build_Options_Line("OnTaskTimeout", self.OnTaskTimeout))
			
		if self.EnableAutoTimeout:
			lines.append("EnableAutoTimeout=true")
		
		if self.EnableTimeoutsForScriptTasks:
			lines.append("EnableTimeoutsForScriptTasks=true")
			
		if len(self.JobDependencies):
			lines.append(build_Options_Line("JobDependencies", self.JobDependencies))
			
			if self.JobDependencyPercentage:
				lines.append(build_Options_Line("JobDependencyPercentage", self.JobDependencyPercentage))
		
		if self.IsFrameDependent:
			lines.append("IsFrameDependent=true")
			lines.append(build_Options_Line("FrameDependencyOffsetStart", self.FrameDependencyOffsetStart))
			lines.append(build_Options_Line("FrameDependencyOffsetEnd", self.FrameDependencyOffsetEnd))
			
		if not self.ResumeOnCompleteDependencies:
			lines.append("ResumeOnCompleteDependencies=false")
		
		if self.ResumeOnDeletedDependencies:
			lines.append("ResumeOnDeletedDependencies=true")
			
		if self.ResumeOnFailedDependencies:
			lines.append("ResumeOnDeletedDependencies=true")
			
		if len(self.RequiredAssets):
			lines.append(build_Options_Line("RequiredAssets", self.RequiredAssets))
			
		if len(self.ScriptDependencies):
			lines.append(build_Options_Line("ScriptDependencies", self.ScriptDependencies))
		
		#ScheduledType=None
		#ScheduledStartDateTime="dd/MM/yyyy HH:mm"
		#ScheduledDays=1
		
		if len(self.OutputFilenames):
			for index, name in  enumerate(self.OutputFilenames):
				lines.append("OutputFilename%i=%s" % (index, name) )
		if len(self.OutputDirectorys):
			for index, name in  enumerate(self.OutputDirectorys):
				lines.append("OutputDirectory%i=%s" % (index, name) )
		
		#if len(self.NotificationTargets):
			#lines.append("NotificationTargets=%s" % self.NotificationTargets )
		
		#ClearNotificationTargets=False
		#NotificationEmails=""
		#OverrideNotificationMethod=False
		#EmailNotification=False
		#PopupNotification=False
		#NotificationNote=""
		if len(self.PreJobScript):
			lines.append(build_Options_Line("PreJobScript", self.PreJobScript))
			
		if len(self.PostJobScript):
			lines.append(build_Options_Line("PostJobScript", self.PostJobScript))
			
		if len(self.PreTaskScript):
			lines.append(build_Options_Line("PreTaskScript", self.PreTaskScript))
			
		if len(self.PostTaskScript):
			lines.append(build_Options_Line("PostTaskScript", self.PostTaskScript))
		#TileJob=False
		#TileJobFrame=0
		#TileJobTilesInX=0
		#TileJobTilesInY=0
		#TileJobTileCount=0
		
		
		if self.Submit_To_ShotGun:
			lines.append(build_Options_Line("ExtraInfo0", self.SG_TaskName))
			lines.append(build_Options_Line("ExtraInfo1", self.SG_ProjectName))
			lines.append(build_Options_Line("ExtraInfo2", self.SG_EntityName))
			lines.append(build_Options_Line("ExtraInfo3", self.SG_VersionName))
			lines.append(build_Options_Line("ExtraInfo4", self.SG_Description))
			lines.append(build_Options_Line("ExtraInfo5", self.SG_UserName))
			lines.append(build_Options_Line("ExtraInfo6", self.SG_Path_To_File))
			
			lines.append(build_Options_Line("ExtraInfoKeyValue0=VersionName", self.SG_VersionName))
			lines.append(build_Options_Line("ExtraInfoKeyValue1=Description", self.SG_Description))
			lines.append(build_Options_Line("ExtraInfoKeyValue2=TaskId", self.SG_TaskId))
			lines.append(build_Options_Line("ExtraInfoKeyValue3=ProjectId", self.SG_ProjectId))
			lines.append(build_Options_Line("ExtraInfoKeyValue4=EntityId", self.SG_EntityId))
			lines.append(build_Options_Line("ExtraInfoKeyValue5=EntityType", self.SG_EntityType))
			lines.append(build_Options_Line("ExtraInfoKeyValue6=PathToFile", self.SG_Path_To_File))
		else:
			if len(self.ExtraInfo):
				for index, info in enumerate(self.ExtraInfo):
					lines.append("ExtraInfo%i=%s" % (index, str(info)) )
			if len(self.ExtraInfoKeyValues):
				for index, item in enumerate(self.ExtraInfoKeyValues.items()):
					lines.append("ExtraInfoKeyValue%i=%s=%s" % (index, item[0], str(item[1]) ) )
				
		res = "\n".join(lines)
		return res

	#----------------------------------------------------------------------
	def Write_File(self):
		# Get the deadline temp directory.
		submitFilename = os.environ["Temp"] + "/DML_Deadline_Job_info.job"
		lines = self.create_job_string()
		# Create the job info file.
		with file(submitFilename,"w") as fileId:
			fileId.write(lines)
		return submitFilename
	
########################################################################
class Base_Plugin_Info(object):
	""""""

	def __init__(self):
		"""Constructor"""	
    
	def create_Submit_String(self):
		return ""
	
	#----------------------------------------------------------------------
	def Write_File(self):
		# Get the deadline temp directory.
		submitFilename = os.environ["Temp"] + "/DML_Deadline_Plug_info.job"
		lines = self.create_Submit_String()
		# Create the job info file.
		with file(submitFilename,"w") as fileId:
			fileId.write(lines)
		return submitFilename
	
########################################################################
class Nuke_Plugin_Info(Base_Plugin_Info):
	""""""

	def __init__(self,SceneFile=None,
				 Version=None,
				 NukeX=False,
				 BatchMode=False,
				 BatchModeIsMovie=False,
				 ContinueOnError=True,
				 EnforceRenderOrder=False,
				 RenderMode="Render Full Resolution",
				 UseGpu=False,
				 GpuOverride=0,
				 Threads=0,
				 RamUse=0,
				 StackSize=0,
				 Views="",
				 PerformanceProfiler=False,
				 PerformanceProfilerDir="",
				 ScriptJob=False,
				 ScriptFilename="",
				 WriteNodes=[]):
		"""
			Options
			
				--SceneFile
					| The scene filename as it exists on the network.
					|
				--Version
					| The version of Nuke to render with.
					|
				--NukeX
					| If checked, NukeX will be used instead of just Nuke.
					|
				--BatchMode
					| This uses the Nuke plugin's Batch Mode. It keeps the Nuke script loaded in memory between frames, which reduces the overhead of rendering the job.
					|
				--BatchModeIsMovie
					| If checked, Deadline will render as a single chunk in Batch Mode, instead of rendering each frame separately. This is necessary for movie renders, otherwise only the last frame is written to the output file.
					|
				--ContinueOnError
					| If checked Nuke will attempt to render subsequent frames in the range after an error. Otherwise, Nuke will stop on the first error.
					|
				--EnforceRenderOrder
					| Forces Nuke to obey the render order of Write nodes.
					|
				--RenderMode
					| Whether or not the scene should be rendered in full resolution or using proxies.
					| values = Scene Settings,Render Full Resolution,Render using Proxies
					|
				--UseGpu
					| If Nuke should also use the GPU for rendering.
					|
				--GpuOverride
					| The GPU that Nuke should use if you are using the GPU for rendering. ( Used for Nuke 8 and higher. )
					| min=0 max=15
					|
				--Threads
					| The number of threads to use for rendering. Set to 0 to have Nuke automatically determine the optimal thread count.
					| min=0 max=128
					|
				--RamUse
					| The maximum RAM usage to allow. Set to 0 to not enforce a maximum amount of RAM.
					| min=0 max=64000
					|
				--StackSize
					| The minimum stack size to use. Set to 0 to not enforce a minimum stack size.
					| min=0 max=64000
					|
				--Views
					| A comma separated list of the views to render.
					|
				--PerformanceProfiler
					| If enabled Nuke will profile the performance of the Nuke DAG whilst rendering and create a *.xml file for later analysis.
					|
				--PerformanceProfilerDir
					| If Performance Profiler is enabled, define the directory on the network where the *.xml files will be saved.
					|
				--ScriptJob
					| If enabled, a script will be run instead of rendering the Nuke scene.
					|
				--ScriptFilename
					| The script filename as it exists on the network.
					|
				--WriteNode
					| If Set Will Only Render The comma separated list of write node names
					|
					"""
		self.SceneFile              = SceneFile
		self.Version                = Version
		self.NukeX                  = NukeX
		self.BatchMode              = BatchMode
		self.BatchModeIsMovie       = BatchModeIsMovie
		self.ContinueOnError        = ContinueOnError
		self.EnforceRenderOrder     = EnforceRenderOrder
		self.RenderMode             = RenderMode
		self.UseGpu                 = UseGpu
		self.GpuOverride            = GpuOverride
		self.Threads                = Threads
		self.RamUse                 = RamUse
		self.StackSize              = StackSize
		self.Views                  = Views
		self.PerformanceProfiler    = PerformanceProfiler
		self.PerformanceProfilerDir = PerformanceProfilerDir
		self.ScriptJob              = ScriptJob
		self.ScriptFilename         = ScriptFilename
		self.WriteNodes             = WriteNodes
	
	def create_Submit_String(self):
		lines = []
		lines.append(build_Options_Line("SceneFile", self.SceneFile))
		lines.append(build_Options_Line("Version", self.Version))
		lines.append(build_Options_Line("Threads", self.Threads))
		lines.append(build_Options_Line("RamUse", self.RamUse))
		lines.append(build_Options_Line("StackSize", self.StackSize))
		lines.append(build_Options_Line("Views", self.Views))
		lines.append(build_Options_Line("ContinueOnError", self.ContinueOnError))
		lines.append(build_Options_Line("RenderMode", self.RenderMode))
		
		if self.NukeX:
			lines.append("NukeX=True")
		else:
			lines.append("NukeX=False")
			
		if self.BatchMode:
			lines.append("BatchMode=True")
			
			if self.BatchModeIsMovie:
				lines.append("BatchModeIsMovie=True")
		else:
			lines.append("BatchMode=False")
			
		if self.UseGpu:
			lines.append("UseGpu=True")
			lines.append(build_Options_Line("GpuOverride", self.GpuOverride))
		else:
			lines.append("UseGpu=False")
			
		if self.PerformanceProfiler:
			lines.append("PerformanceProfiler=True")
			lines.append(build_Options_Line("PerformanceProfilerDir", self.PerformanceProfilerDir))
		else:
			lines.append("PerformanceProfiler=False")
		
		if self.ScriptJob:
			lines.append(build_Options_Line("ScriptJob", self.ScriptJob))
			lines.append(build_Options_Line("ScriptFilename", self.ScriptFilename))
			
		if len(self.WriteNodes):
			lines.append(build_Options_Line("WriteNode", ",".join(self.WriteNodes)))
		return "\n".join(lines)
	
########################################################################
class GimpPSD_Plugin_Info(Base_Plugin_Info):
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
			lines.append(build_Options_Line("JsonData", self.jsondata))
		else:
			lines.append(build_Options_Line("JsonFile", self.jsonfile))
		return "\n".join(lines)

########################################################################
class Job_Submitter(object):
	""""""

	#----------------------------------------------------------------------
	def __init__(self, job_info, plugin_info):
		"""Constructor"""
		self.plugin = plugin_info
		self.job    = job_info
		
	def Submit_the_job_to_Deadline(self):
		jobFilename = self.job.Write_File()
		plugin_file_name = self.plugin.Write_File()
		Result = Deadline_Commands.Submit_Deadline_Job(jobFilename, plugin_file_name)
		self.Result        = Result.result.Result
		self.jobId         = Result.result.JobID
		
    
	