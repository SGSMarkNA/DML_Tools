from .Command_Access import CallDeadlineCommand

def About():
	"""Displays the about text"""
	return CallDeadlineCommand("About")

#----------------------------------------------------------------------
def AddAssetServerRoots(Path):
	"""Appends new asset server root directories to the list.

	Params: Name: Discription
	------------------------------
		| **Path** : *The directories to append.*
	"""
	return CallDeadlineCommand("AddAssetServerRoots  %s" % (Path))

#----------------------------------------------------------------------
def AddGroup(Group_Name):
	"""Adds the group.

	Params: Name: Discription
	------------------------------
		| **Group_Name** : *The group name*
	"""
	return CallDeadlineCommand("AddGroup  %s" % (Group_Name))

#----------------------------------------------------------------------
def AddGroupMapping(Region,Group,Image,Machine_Type,Cost,Pool):
	"""Add or Edit a Group Mapping.

	Params: Name: Discription
	------------------------------
		| **Region** : *The name of the Cloud Region*
		| **Group** : *Name of the Group*
		| **Image** : *Image Name*
		| **Machine_Type** : *Machine Type*
		| **Cost** : *Cost defaults=1*
		| **Pool** : *Name of the Pool default=none*
	"""
	return CallDeadlineCommand("AddGroupMapping  %s %s %s %s %s %s" % (Region,Group,Image,Machine_Type,Cost,Pool))

#----------------------------------------------------------------------
def AddGroupToSlave(Worker_Names,Group_Names):
	"""Adds a group to the Worker.

	Params: Name: Discription
	------------------------------
		| **Worker_Names** : *The Worker name, or a list of Worker names separated by commas*
		| **Group_Names** : *The group name, or a list of group names separated by commas*
	"""
	Worker_Names = Worker_Names if not isinstance(Worker_Names,(list,tuple)) else ','.join([str(item) for item in Worker_Names])
	Group_Names = Group_Names if not isinstance(Group_Names,(list,tuple)) else ','.join([str(item) for item in Group_Names])
	return CallDeadlineCommand("AddGroupToSlave  %s %s" % (Worker_Names,Group_Names))

#----------------------------------------------------------------------
def AddJobHistoryEntry(Job_ID,History_Entry):
	"""Adds a Job History Entry for the Job.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job's ID*
		| **History_Entry** : *The history entry to add.*
	"""
	return CallDeadlineCommand("AddJobHistoryEntry  %s %s" % (Job_ID,History_Entry))

#----------------------------------------------------------------------
def AddPool(Pool_Names):
	"""Adds the pool.

	Params: Name: Discription
	------------------------------
		| **Pool_Names** : *The pool name, or a list of names separated by commas*
	"""
	Pool_Names = Pool_Names if not isinstance(Pool_Names,(list,tuple)) else ','.join([str(item) for item in Pool_Names])
	return CallDeadlineCommand("AddPool  %s" % (Pool_Names))

#----------------------------------------------------------------------
def AddPoolToSlave(Worker_Names,Pool_Names):
	"""Adds a pool to the Worker.

	Params: Name: Discription
	------------------------------
		| **Worker_Names** : *The Worker name, or a list of Worker names separated by commas*
		| **Pool_Names** : *The pool name, or a list of pool names separated by commas*
	"""
	Worker_Names = Worker_Names if not isinstance(Worker_Names,(list,tuple)) else ','.join([str(item) for item in Worker_Names])
	Pool_Names = Pool_Names if not isinstance(Pool_Names,(list,tuple)) else ','.join([str(item) for item in Pool_Names])
	return CallDeadlineCommand("AddPoolToSlave  %s %s" % (Worker_Names,Pool_Names))

#----------------------------------------------------------------------
def AddRepositoryHistoryEntry(History_Entry):
	"""Adds a Repository History Entry.

	Params: Name: Discription
	------------------------------
		| **History_Entry** : *The history entry to add.*
	"""
	return CallDeadlineCommand("AddRepositoryHistoryEntry  %s" % (History_Entry))

#----------------------------------------------------------------------
def AddSlaveHistoryEntry(Worker_Name,History_Entry):
	"""Adds a Worker History Entry for the Worker.

	Params: Name: Discription
	------------------------------
		| **Worker_Name** : *The Worker name*
		| **History_Entry** : *The history entry to add.*
	"""
	return CallDeadlineCommand("AddSlaveHistoryEntry  %s %s" % (Worker_Name,History_Entry))

#----------------------------------------------------------------------
def AddSlavesToJobMachineLimitList(Job_IDs,Workers):
	"""Adds Workers to the job's listed Workers.

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The job ID, or a list of job IDs separated by commas*
		| **Workers** : *The Workers to add, separated by commas*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	Workers = Workers if not isinstance(Workers,(list,tuple)) else ','.join([str(item) for item in Workers])
	return CallDeadlineCommand("AddSlavesToJobMachineLimitList  %s %s" % (Job_IDs,Workers))

#----------------------------------------------------------------------
def AddSlavesToLimitGroupList(Limit_Names,Workers):
	"""Adds Workers to the limit's listed Workers.

	Params: Name: Discription
	------------------------------
		| **Limit_Names** : *The limit name, or a list of limit names separated by commas*
		| **Workers** : *The Workers to add, separated by commas*
	"""
	Limit_Names = Limit_Names if not isinstance(Limit_Names,(list,tuple)) else ','.join([str(item) for item in Limit_Names])
	Workers = Workers if not isinstance(Workers,(list,tuple)) else ','.join([str(item) for item in Workers])
	return CallDeadlineCommand("AddSlavesToLimitGroupList  %s %s" % (Limit_Names,Workers))

#----------------------------------------------------------------------
def AddUserToUserGroup(User_Names,User_Group_Names):
	"""Adds a user to the user group.

	Params: Name: Discription
	------------------------------
		| **User_Names** : *The user name, or a list of user names separated by commas*
		| **User_Group_Names** : *The user group name, or a list of user group names separated by commas*
	"""
	User_Names = User_Names if not isinstance(User_Names,(list,tuple)) else ','.join([str(item) for item in User_Names])
	User_Group_Names = User_Group_Names if not isinstance(User_Group_Names,(list,tuple)) else ','.join([str(item) for item in User_Group_Names])
	return CallDeadlineCommand("AddUserToUserGroup  %s %s" % (User_Names,User_Group_Names))

#----------------------------------------------------------------------
def AppendJobFrameRange(Job_IDs,Frame_List):
	"""Appends to the job's existing frame range.

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The job ID, or a list of job IDs separated by commas*
		| **Frame_List** : *The additional frames to append*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	return CallDeadlineCommand("AppendJobFrameRange  %s %s" % (Job_IDs,Frame_List))

#----------------------------------------------------------------------
def ArchiveJob(Job_IDs):
	"""Archives the job.

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The job ID, or a list of job IDs separated by commas*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	return CallDeadlineCommand("ArchiveJob  %s" % (Job_IDs))

#----------------------------------------------------------------------
def AWSPortalPrecacheJob(Job_IDs):
	"""Precaches the AWS Portal Assets of the jobs.

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The job ID, or a list of job IDs separated by commas*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	return CallDeadlineCommand("AWSPortalPrecacheJob  %s" % (Job_IDs))

#----------------------------------------------------------------------
def Background(notify,Job_Files):
	"""Submits a job as a background process.

	Params: Name: Discription
	------------------------------
		| **notify** : *This flag displays a notification window after the jobs have been submitted*
		| **Job_Files** : *The list of job files*
	"""
	Job_Files = Job_Files if not isinstance(Job_Files,(list,tuple)) else ','.join([str(item) for item in Job_Files])
	return CallDeadlineCommand("Background  %s %s" % (notify,Job_Files))

#----------------------------------------------------------------------
def ChangeAutoConfigurationPort(Port):
	"""Changes the port that the Auto Configuration feature uses.

	Params: Name: Discription
	------------------------------
		| **Port** : *The new port number, between 1 and 65535 inclusive*
	"""
	return CallDeadlineCommand("ChangeAutoConfigurationPort  %s" % (Port))

#----------------------------------------------------------------------
def ChangeLicenseMode(License_Mode):
	"""Sets the Deadline License Mode

	Params: Name: Discription
	------------------------------
		| **License_Mode** : *Standard or UsageBased*
	"""
	return CallDeadlineCommand("ChangeLicenseMode  %s" % (License_Mode))

#----------------------------------------------------------------------
def ChangeLicenseServer(License_Server):
	"""Allows you to change the license server the Balancer and Workers connect to.

	Params: Name: Discription
	------------------------------
		| **License_Server** : *(optional) If not specified, a License Server dialog will be displayed*
	"""
	return CallDeadlineCommand("ChangeLicenseServer  %s" % (License_Server))

#----------------------------------------------------------------------
def ChangeListeningPort(Port):
	"""Changes the port that the Deadline Launcher listens on.

	Params: Name: Discription
	------------------------------
		| **Port** : *The new port number, between 1 and 65535 inclusive*
	"""
	return CallDeadlineCommand("ChangeListeningPort  %s" % (Port))

#----------------------------------------------------------------------
def ChangeRepository(Connection_Type,Connection_String,Client_Certificate,Certificate_Password):
	"""Allows you to change the Repository Connection Settings that Deadline uses by default. If no arguments are provided, the Change Repository dialog will be displayed.

	Params: Name: Discription
	------------------------------
		| **Connection_Type** : *Optional. Specifies the type of connection to use when connecting (either Direct or Proxy). If not specified, the type will be inferred from the connection string.*
		| **Connection_String** : *When using Direct connection, this is the path to the root of the Repository. When using a Proxy connection, this is a string of format <HOST>:<PORT>.*
		| **Client_Certificate** : *Optional. The path to a client certificate to use when connecting to a Proxy or Database over SSL/TLS.*
		| **Certificate_Password** : *Optional. The password to the provided Client Certificate, if required.*
	"""
	return CallDeadlineCommand("ChangeRepository  %s %s %s %s" % (Connection_Type,Connection_String,Client_Certificate,Certificate_Password))

#----------------------------------------------------------------------
def ChangeRepositorySkipValidation(Connection_Type,Connection_String,Client_Certificate,Certificate_Password):
	"""Allows you to change the Repository Connection Settings that Deadline uses by default and saves those setting without validating them. If no arguments are provided, the Change Repository dialog will be displayed.

	Params: Name: Discription
	------------------------------
		| **Connection_Type** : *Optional. Specifies the type of connection to use when connecting (either Direct or Proxy). If not specified, the type will be inferred from the connection string.*
		| **Connection_String** : *When using Direct connection, this is the path to the root of the Repository. When using a Proxy connection, this is a string of format <HOST>:<PORT>.*
		| **Client_Certificate** : *Optional. The path to a client certificate to use when connecting to a Proxy or Database over SSL/TLS.*
		| **Certificate_Password** : *Optional. The password to the provided Client Certificate, if required. Only used for Direct connections.*
	"""
	return CallDeadlineCommand("ChangeRepositorySkipValidation  %s %s %s %s" % (Connection_Type,Connection_String,Client_Certificate,Certificate_Password))

#----------------------------------------------------------------------
def ChangeUser(User_Name):
	"""Changes the current Deadline user on this machine.

	Params: Name: Discription
	------------------------------
		| **User_Name** : *(optional) If not specified, a User Login dialog will be displayed*
	"""
	return CallDeadlineCommand("ChangeUser  %s" % (User_Name))

#----------------------------------------------------------------------
def CheckAdminPrivileges(Verbose):
	"""Checks if the current user has admin privileges.

	Params: Name: Discription
	------------------------------
		| **Verbose** : *true/false*
	"""
	return CallDeadlineCommand("CheckAdminPrivileges  %s" % (Verbose))

#----------------------------------------------------------------------
def CheckFilePermissions(ReadOnly_or_WriteOnly,Quiet,Filename):
	"""Checks the read/write permissions on the file.

	Params: Name: Discription
	------------------------------
		| **ReadOnly_or_WriteOnly** : *Checks both if omitted (optional)*
		| **Quiet** : *Print only SUCCESS or errors (optional)*
		| **Filename** : *The file to check*
	"""
	return CallDeadlineCommand("CheckFilePermissions  %s %s %s" % (ReadOnly_or_WriteOnly,Quiet,Filename))

#----------------------------------------------------------------------
def CheckPathMapping(Path,Force_Separator):
	"""Performs path mapping on the given path. Uses the path mappings in the Repository Options.

	Params: Name: Discription
	------------------------------
		| **Path** : *The path to map*
		| **Force_Separator** : *All path separators in the replacement path will be replaced with this before the original path is mapped (optional)*
	"""
	return CallDeadlineCommand("CheckPathMapping  %s %s" % (Path,Force_Separator))

#----------------------------------------------------------------------
def CheckPathMappingForMultiplePaths(Paths,Force_Separator):
	"""Performs path mapping on the given paths. Uses the path mappings in the Repository Options.

	Params: Name: Discription
	------------------------------
		| **Paths** : *The path to map, or a list of paths to map each separated by a space*
		| **Force_Separator** : *All path separators in the replacement path will be replaced with this before the original path is mapped (optional). To set this please precede the separator with "forceSeparator:".*
	"""
	Paths = Paths if not isinstance(Paths,(list,tuple)) else ','.join([str(item) for item in Paths])
	return CallDeadlineCommand("CheckPathMappingForMultiplePaths  %s %s" % (Paths,Force_Separator))

#----------------------------------------------------------------------
def CheckPathMappingInFile(Input_File,Output_File,Force_Separator):
	"""Performs path mapping on the contents of the given file. Uses the path mappings in the Repository Options.

	Params: Name: Discription
	------------------------------
		| **Input_File** : *The original file name*
		| **Output_File** : *The new file name where the mapped contents will be stored*
		| **Force_Separator** : *All path separators in the replacement path will be replaced with this before the original path is mapped (optional)*
	"""
	return CallDeadlineCommand("CheckPathMappingInFile  %s %s %s" % (Input_File,Output_File,Force_Separator))

#----------------------------------------------------------------------
def CheckPathMappingInFileAndReplaceSeparator(Input_File,Output_File,Old_Separator,New_Separator,Force_Separator):
	"""Performs path mapping on the contents of the given file, and updates all path separators in any paths that are mapped. Uses the path mappings in the Repository Options.

	Params: Name: Discription
	------------------------------
		| **Input_File** : *The original file name*
		| **Output_File** : *The new file name where the mapped contents will be stored*
		| **Old_Separator** : *The path separator to replace*
		| **New_Separator** : *The new path separator*
		| **Force_Separator** : *All path separators in the replacement path will be replaced with this before the original path is mapped (optional)*
	"""
	return CallDeadlineCommand("CheckPathMappingInFileAndReplaceSeparator  %s %s %s %s %s" % (Input_File,Output_File,Old_Separator,New_Separator,Force_Separator))

#----------------------------------------------------------------------
def CompleteJob(Job_IDs):
	"""Completes a job.

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The job ID, or a list of job IDs separated by commas*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	return CallDeadlineCommand("CompleteJob  %s" % (Job_IDs))

#----------------------------------------------------------------------
def CompleteJobTask(Job_ID,Task_ID):
	"""Marks the specified task for the job as complete.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
		| **Task_ID** : *The task ID*
	"""
	return CallDeadlineCommand("CompleteJobTask  %s %s" % (Job_ID,Task_ID))

#----------------------------------------------------------------------
def CompleteJobTasks(Job_ID,Task_IDs):
	"""Completes the specified tasks for the job.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
		| **Task_IDs** : *The comma separated list of task IDs*
	"""
	Task_IDs = Task_IDs if not isinstance(Task_IDs,(list,tuple)) else ','.join([str(item) for item in Task_IDs])
	return CallDeadlineCommand("CompleteJobTasks  %s %s" % (Job_ID,Task_IDs))

#----------------------------------------------------------------------
def ConfigureDatabase(Host,Port,DB_Name,SSL,Client_Certificate,Certificate_Password,Authenticate,Username,Password,Replica_Set,Split_DB):
	"""Configures (or re-configures) a Deadline database. This will connect to Mongo DB using the provided information, and prints out server connection info that was used in a successful connection (might be slightly different from the input).

	Params: Name: Discription
	------------------------------
		| **Host** : *The host name or IP address of the database machine.*
		| **Port** : *The database port*
		| **DB_Name** : *The name of the Deadline database.*
		| **SSL** : *True if SSL/TLS should be used when connecting to the Database server, False otherwise.*
		| **Client_Certificate** : *The path to a client x.509 certificate to present when connecting using SSL/TLS. Ignored if SSL is False.*
		| **Certificate_Password** : *The password to the client certificate provided. Ignored if SSL is False, or if no certificate was provided. If left empty and a password is required, you will be prompted to enter it.*
		| **Authenticate** : *True if Deadline needs to authenticate in order to interact with the Database, False otherwise.*
		| **Username** : *The username with which to authenticate. If empty, and both Authenticate and SSL are true, the client certificate will be used instead. Ignored if Authenticate is False.*
		| **Password** : *The password for the specified user. Ignored if Authenticate is False, or if no user name was provided. If empty and both 'Authenticate' and 'Username' are specified, you will be prompted for the password.*
		| **Replica_Set** : *The name of the Replica set which the Database belongs to, if applicable.*
		| **Split_DB** : *Whether or not to split Deadline data across multiple databases. These databases will be prefixed by <DB Name> (Default: False).*
	"""
	return CallDeadlineCommand("ConfigureDatabase  %s %s %s %s %s %s %s %s %s %s %s" % (Host,Port,DB_Name,SSL,Client_Certificate,Certificate_Password,Authenticate,Username,Password,Replica_Set,Split_DB))

#----------------------------------------------------------------------
def ConnectToBalancerLog(BalancerName,ShowWindow):
	"""Connect to Balancer to watch its log in real time. Press Enter at any time to disconnect from the Balancer.

	Params: Name: Discription
	------------------------------
		| **BalancerName** : *The balancer to connect to*
		| **ShowWindow** : *If a log window should be displayed (optional, defaults to false)*
	"""
	return CallDeadlineCommand("ConnectToBalancerLog  %s %s" % (BalancerName,ShowWindow))

#----------------------------------------------------------------------
def ConnectToLicenseForwarderLog(LicenseForwarderName,ShowWindow):
	"""Connect to License Forwarder to watch its log in real time. Press Enter at any time to disconnect from the License Forwarder.

	Params: Name: Discription
	------------------------------
		| **LicenseForwarderName** : *The license forwarder to connect to*
		| **ShowWindow** : *If a log window should be displayed (optional, defaults to false)*
	"""
	return CallDeadlineCommand("ConnectToLicenseForwarderLog  %s %s" % (LicenseForwarderName,ShowWindow))

#----------------------------------------------------------------------
def ConnectToPulseLog(PulseName,ShowWindow):
	"""Connect to Pulse to watch its log in real time. Press Enter at any time to disconnect from the Worker.

	Params: Name: Discription
	------------------------------
		| **PulseName** : *The pulse to connect to*
		| **ShowWindow** : *If a log window should be displayed (optional, defaults to false)*
	"""
	return CallDeadlineCommand("ConnectToPulseLog  %s %s" % (PulseName,ShowWindow))

#----------------------------------------------------------------------
def ConnectToSlaveLog(WorkerName,ShowWindow):
	"""Connect to a remote Worker to watch its log in real time. Press Enter at any time to disconnect from the Worker.

	Params: Name: Discription
	------------------------------
		| **WorkerName** : *The Worker to connect to*
		| **ShowWindow** : *If a log window should be displayed (optional, defaults to false)*
	"""
	return CallDeadlineCommand("ConnectToSlaveLog  %s %s" % (WorkerName,ShowWindow))

#----------------------------------------------------------------------
def CreateCloudRegion(Name,Plugin_Name,Config_File):
	"""Creates a new Cloud Region.

	Params: Name: Discription
	------------------------------
		| **Name** : *The name of the Cloud Region*
		| **Plugin_Name** : *The Cloud Plugin name*
		| **Config_File** : *Path to Cloud Region config file*
	"""
	return CallDeadlineCommand("CreateCloudRegion  %s %s %s" % (Name,Plugin_Name,Config_File))

#----------------------------------------------------------------------
def CreateMongoDBUser(Connection_String,Authentication_Type,Username_or_Certificate,Password):
	"""Attempts to create a Deadline User in the given database. The user will be created with 'readWriteAnyDatabase' and 'clusterMonitor' roles.

	Params: Name: Discription
	------------------------------
		| **Connection_String** : *The connection string that specifies how to connect to the database (e.g. mongodb://<host>:<port>).*
		| **Authentication_Type** : *The Type of authentication mechanism to use. Only X509 is currently supported.*
		| **Username_or_Certificate** : *The client certificate (X509) in PKCS12 format.*
		| **Password** : *The password required to decrypt the client certificate (X509), if applicable. If left empty and a password is required, you will be prompted for it.*
	"""
	return CallDeadlineCommand("CreateMongoDBUser  %s %s %s %s" % (Connection_String,Authentication_Type,Username_or_Certificate,Password))

#----------------------------------------------------------------------
def DeleteBalancer(Balancer_Names):
	"""Deletes the Balancer.

	Params: Name: Discription
	------------------------------
		| **Balancer_Names** : *The Balancer name, or a list of Balancer names separated by commas.*
	"""
	Balancer_Names = Balancer_Names if not isinstance(Balancer_Names,(list,tuple)) else ','.join([str(item) for item in Balancer_Names])
	return CallDeadlineCommand("DeleteBalancer  %s" % (Balancer_Names))

#----------------------------------------------------------------------
def DeleteGroup(Group_Name):
	"""Deletes the group.

	Params: Name: Discription
	------------------------------
		| **Group_Name** : *The group name*
	"""
	return CallDeadlineCommand("DeleteGroup  %s" % (Group_Name))

#----------------------------------------------------------------------
def DeleteJob(Job_IDs):
	"""Deletes the job(s).

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The job ID, or a list of job IDs separated by commas*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	return CallDeadlineCommand("DeleteJob  %s" % (Job_IDs))

#----------------------------------------------------------------------
def DeleteLimitGroup(Limit_Names):
	"""Deletes the limit.

	Params: Name: Discription
	------------------------------
		| **Limit_Names** : *The limit name, or a list of names separated by commas*
	"""
	Limit_Names = Limit_Names if not isinstance(Limit_Names,(list,tuple)) else ','.join([str(item) for item in Limit_Names])
	return CallDeadlineCommand("DeleteLimitGroup  %s" % (Limit_Names))

#----------------------------------------------------------------------
def DeletePool(Pool_Name):
	"""Deletes the pool.

	Params: Name: Discription
	------------------------------
		| **Pool_Name** : *The pool name*
	"""
	return CallDeadlineCommand("DeletePool  %s" % (Pool_Name))

#----------------------------------------------------------------------
def DeleteProxyServer(Proxy_Server_Names):
	"""Deletes specified Proxy Server(s).

	Params: Name: Discription
	------------------------------
		| **Proxy_Server_Names** : *The Proxy Server name, or list of comma-separated names.*
	"""
	Proxy_Server_Names = Proxy_Server_Names if not isinstance(Proxy_Server_Names,(list,tuple)) else ','.join([str(item) for item in Proxy_Server_Names])
	return CallDeadlineCommand("DeleteProxyServer  %s" % (Proxy_Server_Names))

#----------------------------------------------------------------------
def DeletePulse(Pulse_Names):
	"""Deletes the pulse.

	Params: Name: Discription
	------------------------------
		| **Pulse_Names** : *The pulse name, or a list of pulse names separated by commas*
	"""
	Pulse_Names = Pulse_Names if not isinstance(Pulse_Names,(list,tuple)) else ','.join([str(item) for item in Pulse_Names])
	return CallDeadlineCommand("DeletePulse  %s" % (Pulse_Names))

#----------------------------------------------------------------------
def DeleteSlave(Worker_Names):
	"""Deletes the Worker.

	Params: Name: Discription
	------------------------------
		| **Worker_Names** : *The Worker name, or a list of Worker names separated by commas*
	"""
	Worker_Names = Worker_Names if not isinstance(Worker_Names,(list,tuple)) else ','.join([str(item) for item in Worker_Names])
	return CallDeadlineCommand("DeleteSlave  %s" % (Worker_Names))

#----------------------------------------------------------------------
def DeleteUser(User_Names):
	"""Deletes the user.

	Params: Name: Discription
	------------------------------
		| **User_Names** : *The user name, or a list of names separated by commas*
	"""
	User_Names = User_Names if not isinstance(User_Names,(list,tuple)) else ','.join([str(item) for item in User_Names])
	return CallDeadlineCommand("DeleteUser  %s" % (User_Names))

#----------------------------------------------------------------------
def DeleteUserGroup(User_Group_Name):
	"""Deletes the User Groups with the given user group name.

	Params: Name: Discription
	------------------------------
		| **User_Group_Name** : *The user group name*
	"""
	return CallDeadlineCommand("DeleteUserGroup  %s" % (User_Group_Name))

#----------------------------------------------------------------------
def DoPendingJobScan(Check_Last_Time,Verbose,Log_Repo_History,Region):
	"""Scans for pending jobs to be released and pending job events to be processed.

	Params: Name: Discription
	------------------------------
		| **Check_Last_Time** : *Optional. If true, the pending job scan will only be performed if the appropriate amount of time has passed since the last check (true/false).*
		| **Verbose** : *Optional. If logging should be enabled (true/false).*
		| **Log_Repo_History** : *Optional. If a history entry should be logged (true/false).*
		| **Region** : *Optional. The region to be used for path mapping.*
	"""
	return CallDeadlineCommand("DoPendingJobScan  %s %s %s %s" % (Check_Last_Time,Verbose,Log_Repo_History,Region))

#----------------------------------------------------------------------
def DoRepositoryRepair(Check_Last_Time,Verbose,Log_Repo_History,Mode):
	"""Performs repository repair operations.

	Params: Name: Discription
	------------------------------
		| **Check_Last_Time** : *Optional. If true, a repository repair will only be performed if the appropriate amount of time has passed since the last check (true/false). This is always True if a mode is specified.*
		| **Verbose** : *Optional. If logging should be enabled (true/false).*
		| **Log_Repo_History** : *Optional. If a history entry should be logged (true/false). This is ignored if a mode other than 'All' is specified.*
		| **Mode** : *Optional. If not specified, all repair operations will be performed. Available modes are: All, FindOrphanedTasks, FindOrphanedLimitStubs, FindStalledSlaves, FindStalledPulses, FindStalledBalancers*
	"""
	return CallDeadlineCommand("DoRepositoryRepair  %s %s %s %s" % (Check_Last_Time,Verbose,Log_Repo_History,Mode))

#----------------------------------------------------------------------
def ExecuteScript(Filename):
	"""Executes the script.

	Params: Name: Discription
	------------------------------
		| **Filename** : *The path to a given script file*
	"""
	return CallDeadlineCommand("ExecuteScript  %s" % (Filename))

#----------------------------------------------------------------------
def ExecuteScriptNoGui(Filename):
	"""Executes the script without importing any GUI elements.

	Params: Name: Discription
	------------------------------
		| **Filename** : *The path to a given script file*
	"""
	return CallDeadlineCommand("ExecuteScriptNoGui  %s" % (Filename))

#----------------------------------------------------------------------
def Exit():
	"""Exit Deadline Interactive mode. Equivalent to Quit."""
	return CallDeadlineCommand("Exit")

#----------------------------------------------------------------------
def FailJob(Job_IDs):
	"""Fails a job.

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The job ID, or a list of job IDs separated by commas*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	return CallDeadlineCommand("FailJob  %s" % (Job_IDs))

#----------------------------------------------------------------------
def FailJobTask(Job_ID,Task_ID):
	"""Fails the specified task for the job.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
		| **Task_ID** : *The task ID*
	"""
	return CallDeadlineCommand("FailJobTask  %s %s" % (Job_ID,Task_ID))

#----------------------------------------------------------------------
def FailJobTasks(Job_ID,Task_IDs):
	"""Fails the specified tasks for the job.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
		| **Task_IDs** : *The comma separated list of task IDs*
	"""
	Task_IDs = Task_IDs if not isinstance(Task_IDs,(list,tuple)) else ','.join([str(item) for item in Task_IDs])
	return CallDeadlineCommand("FailJobTasks  %s %s" % (Job_ID,Task_IDs))

#----------------------------------------------------------------------
def FarmReports(Report_Name,Start_Date,End_Date,Export_Mode,Export_File_Name):
	"""Allows you to view farm reports. If a report name is specified, that report will instead be automatically be exported to the given file.

	Params: Name: Discription
	------------------------------
		| **Report_Name** : *The name of an existing report*
		| **Start_Date** : *The start date, in yyyy-MM-dd format*
		| **End_Date** : *The end date, in yyyy-MM-dd format*
		| **Export_Mode** : *CSV or TSV*
		| **Export_File_Name** : *The file to export to*
	"""
	return CallDeadlineCommand("FarmReports  %s %s %s %s %s" % (Report_Name,Start_Date,End_Date,Export_Mode,Export_File_Name))

#----------------------------------------------------------------------
def FileCheck(ReadOnly_or_WriteOnly,Quiet,Filename):
	"""Checks the read/write permissions on the file.

	Params: Name: Discription
	------------------------------
		| **ReadOnly_or_WriteOnly** : *Checks both if omitted (optional)*
		| **Quiet** : *Print only SUCCESS or errors (optional)*
		| **Filename** : *The file to check*
	"""
	return CallDeadlineCommand("FileCheck  %s %s %s" % (ReadOnly_or_WriteOnly,Quiet,Filename))

#----------------------------------------------------------------------
def GenerateRSAKeys(UserSpecific):
	"""Creates and saves RSA key-pairs for internal use by Deadline. Administrator/root privileges might be required to create machine-wide keys.

	Params: Name: Discription
	------------------------------
		| **UserSpecific** : *If True, keys specific to the current OS user will be generated. (Default: False)*
	"""
	return CallDeadlineCommand("GenerateRSAKeys  %s" % (UserSpecific))

#----------------------------------------------------------------------
def GenerateSubmissionInfoFiles(Job_ID,Job_Info_File,Plugin_Info_File):
	"""Generates a Job Info file and a Plugin Info file that can be used to submit a new Job, based on an existing one.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The ID of the Job on which to base the Submission Parameters.*
		| **Job_Info_File** : *The file to which the Job Submission Info will be output.*
		| **Plugin_Info_File** : *The file to which the Plugin Submission Info will be output.*
	"""
	return CallDeadlineCommand("GenerateSubmissionInfoFiles  %s %s %s" % (Job_ID,Job_Info_File,Plugin_Info_File))

#----------------------------------------------------------------------
def GetAssetServerInfo(Name):
	"""Gets the value of the specified Asset Server Info setting if it exists.

	Params: Name: Discription
	------------------------------
		| **Name** : *The name of the Asset Server Info setting.*
	"""
	return CallDeadlineCommand("GetAssetServerInfo  %s" % (Name))

#----------------------------------------------------------------------
def GetAssetServerSetting(Name):
	"""Gets the value of the specified Asset Server setting if it exists.

	Params: Name: Discription
	------------------------------
		| **Name** : *The name of the Asset Server setting.*
	"""
	return CallDeadlineCommand("GetAssetServerSetting  %s" % (Name))

#----------------------------------------------------------------------
def GetAWSPortalSetting(Name):
	"""Gets the value of the specified AWS Portal setting if it exists.

	Params: Name: Discription
	------------------------------
		| **Name** : *The name of the AWS Portal setting.*
	"""
	return CallDeadlineCommand("GetAWSPortalSetting  %s" % (Name))

#----------------------------------------------------------------------
def GetBalancerInfo(Balancer_Name):
	"""Retrieves BalancerInfo for a specified Balancer.

	Params: Name: Discription
	------------------------------
		| **Balancer_Name** : *The name of the Balancer to retrieve BalancerInfo for.*
	"""
	return CallDeadlineCommand("GetBalancerInfo  %s" % (Balancer_Name))

#----------------------------------------------------------------------
def GetBalancerInfos(Balancer_Names):
	"""Get BalancerInfo for all specified (by name) Balancers.

	Params: Name: Discription
	------------------------------
		| **Balancer_Names** : *Comma-separated list of Balancer names to query. Leave blank to query all Balancers.*
	"""
	Balancer_Names = Balancer_Names if not isinstance(Balancer_Names,(list,tuple)) else ','.join([str(item) for item in Balancer_Names])
	return CallDeadlineCommand("GetBalancerInfos  %s" % (Balancer_Names))

#----------------------------------------------------------------------
def GetBalancerNames():
	"""Prints a list of all Balancer names."""
	return CallDeadlineCommand("GetBalancerNames")

#----------------------------------------------------------------------
def GetBalancerSettings(Balancer_Name):
	"""Retrieves BalancerSettings for a specified Balancer.

	Params: Name: Discription
	------------------------------
		| **Balancer_Name** : *The name of the Balancer to retrieve BalancerSettings for.*
	"""
	return CallDeadlineCommand("GetBalancerSettings  %s" % (Balancer_Name))

#----------------------------------------------------------------------
def GetBalancerSettingsList(Balancer_Names):
	"""Get BalancerInfo for all specified (by name) Balancers.

	Params: Name: Discription
	------------------------------
		| **Balancer_Names** : *Comma-separated list of Balancer names to query. Leave blank to query all Balancers.*
	"""
	Balancer_Names = Balancer_Names if not isinstance(Balancer_Names,(list,tuple)) else ','.join([str(item) for item in Balancer_Names])
	return CallDeadlineCommand("GetBalancerSettingsList  %s" % (Balancer_Names))

#----------------------------------------------------------------------
def GetBinDirectory():
	"""Displays the bin directory of the Deadline Client software"""
	return CallDeadlineCommand("GetBinDirectory")

#----------------------------------------------------------------------
def GetCloudPluginParams(Plugin_Name):
	"""Show all the parameters for a given cloud plugin.

	Params: Name: Discription
	------------------------------
		| **Plugin_Name** : *The name of the cloud plugin*
	"""
	return CallDeadlineCommand("GetCloudPluginParams  %s" % (Plugin_Name))

#----------------------------------------------------------------------
def GetCommonAppPath():
	"""Prints out the path to the common application data folder."""
	return CallDeadlineCommand("GetCommonAppPath")

#----------------------------------------------------------------------
def GetCurrentUserHomeDirectory():
	"""Displays the current user home directory of the Deadline Client software"""
	return CallDeadlineCommand("GetCurrentUserHomeDirectory")

#----------------------------------------------------------------------
def GetCurrentUserName():
	"""Display the current Deadline user"""
	return CallDeadlineCommand("GetCurrentUserName")

#----------------------------------------------------------------------
def GetDatabaseSettings(Repository):
	"""Prints the given repository's connection.ini file contents to stdout.

	Params: Name: Discription
	------------------------------
		| **Repository** : *The path to the repository root*
	"""
	return CallDeadlineCommand("GetDatabaseSettings  %s" % (Repository))

#----------------------------------------------------------------------
def GetDeletedJob(Job_IDs,Use_Ini_Display):
	"""Display information for the deleted job(s).

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The job ID, or a list of job IDs separated by commas*
		| **Use_Ini_Display** : *true/false (optional, default is false)*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	return CallDeadlineCommand("GetDeletedJob  %s %s" % (Job_IDs,Use_Ini_Display))

#----------------------------------------------------------------------
def GetDeletedJobIds():
	"""Displays all the deleted job IDs"""
	return CallDeadlineCommand("GetDeletedJobIds")

#----------------------------------------------------------------------
def GetDeletedJobs(Use_Ini_Display):
	"""Displays information for all the deleted jobs.

	Params: Name: Discription
	------------------------------
		| **Use_Ini_Display** : *true/false (optional, default is false)*
	"""
	return CallDeadlineCommand("GetDeletedJobs  %s" % (Use_Ini_Display))

#----------------------------------------------------------------------
def GetDirectory(Initial_Path):
	"""Opens a folder browser and prints out the result.

	Params: Name: Discription
	------------------------------
		| **Initial_Path** : *The path to the initial directory (optional)*
	"""
	return CallDeadlineCommand("GetDirectory  %s" % (Initial_Path))

#----------------------------------------------------------------------
def GetEventPluginNames():
	"""Displays all event plugin names."""
	return CallDeadlineCommand("GetEventPluginNames")

#----------------------------------------------------------------------
def GetFarmStatistics():
	"""Displays quick summary information of jobs and Workers"""
	return CallDeadlineCommand("GetFarmStatistics")

#----------------------------------------------------------------------
def GetFarmStatisticsEx():
	"""Displays quick summary information of jobs and Workers"""
	return CallDeadlineCommand("GetFarmStatisticsEx")

#----------------------------------------------------------------------
def GetGroupNames():
	"""Displays all groups."""
	return CallDeadlineCommand("GetGroupNames")

#----------------------------------------------------------------------
def GetHomeDirectory():
	"""Displays the home directory of the Deadline Client software"""
	return CallDeadlineCommand("GetHomeDirectory")

#----------------------------------------------------------------------
def GetIniFileSetting(Key):
	"""Returns the value for the given key from the deadline.ini configuration file.

	Params: Name: Discription
	------------------------------
		| **Key** : *The key to get*
	"""
	return CallDeadlineCommand("GetIniFileSetting  %s" % (Key))

#----------------------------------------------------------------------
def GetJob(Job_IDs,Use_Ini_Display):
	"""Display information for the job(s).

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The job ID, or a list of job IDs separated by commas*
		| **Use_Ini_Display** : *true/false (optional, default is false)*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	return CallDeadlineCommand("GetJob  %s %s" % (Job_IDs,Use_Ini_Display))

#----------------------------------------------------------------------
def GetJobAuxiliaryPath(Job_ID):
	"""Displays the Jobs Auxillary path

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
	"""
	return CallDeadlineCommand("GetJobAuxiliaryPath  %s" % (Job_ID))

#----------------------------------------------------------------------
def GetJobDetails(Job_IDs):
	"""Displays the job details.

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The job ID, or a list of job IDs separated by commas*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	return CallDeadlineCommand("GetJobDetails  %s" % (Job_IDs))

#----------------------------------------------------------------------
def GetJobErrorReportFilenames(Job_ID):
	"""Gets the error report filenames for the job.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
	"""
	return CallDeadlineCommand("GetJobErrorReportFilenames  %s" % (Job_ID))

#----------------------------------------------------------------------
def GetJobExtraInfoKeyValue(Job_ID,Extra_Info_Key):
	"""Gets the value from the extra info dictionary.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
		| **Extra_Info_Key** : *The extra info key to get.*
	"""
	return CallDeadlineCommand("GetJobExtraInfoKeyValue  %s %s" % (Job_ID,Extra_Info_Key))

#----------------------------------------------------------------------
def GetJobIds():
	"""Displays all the job IDs"""
	return CallDeadlineCommand("GetJobIds")

#----------------------------------------------------------------------
def GetJobIdsFilter(Filter_1,Repeated_Arg):
	"""Display job Ids for jobs that fulfill the specified filters.

	Params: Name: Discription
	------------------------------
		| **Filter_1** : *A filter, in the form of <Setting=Value>*
		| **Repeated_Arg** : *Additional filters...*
	"""
	return CallDeadlineCommand("GetJobIdsFilter  %s %s" % (Filter_1,Repeated_Arg))

#----------------------------------------------------------------------
def GetJobIdsFilterAnd(Filter_1,Repeated_Arg):
	"""Display jobs that fulfill all the specified filters.

	Params: Name: Discription
	------------------------------
		| **Filter_1** : *A filter, in the form of <Setting=Value>*
		| **Repeated_Arg** : *Additional filters...*
	"""
	return CallDeadlineCommand("GetJobIdsFilterAnd  %s %s" % (Filter_1,Repeated_Arg))

#----------------------------------------------------------------------
def GetJobLogReportFilenames(Job_ID):
	"""Gets the log report filenames for the job.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
	"""
	return CallDeadlineCommand("GetJobLogReportFilenames  %s" % (Job_ID))

#----------------------------------------------------------------------
def GetJobPluginInfoKeyValue(Job_ID,Plugin_Info_Key):
	"""Gets the value from the plugin info dictionary.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
		| **Plugin_Info_Key** : *The plugin info key to get.*
	"""
	return CallDeadlineCommand("GetJobPluginInfoKeyValue  %s %s" % (Job_ID,Plugin_Info_Key))

#----------------------------------------------------------------------
def GetJobs(Use_Ini_Display):
	"""Displays information for all the jobs.

	Params: Name: Discription
	------------------------------
		| **Use_Ini_Display** : *true/false (optional, default is false)*
	"""
	return CallDeadlineCommand("GetJobs  %s" % (Use_Ini_Display))

#----------------------------------------------------------------------
def GetJobSetting(Job_ID,Job_Setting):
	"""Gets the value of a setting for the job.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
		| **Job_Setting** : *The job setting*
	"""
	return CallDeadlineCommand("GetJobSetting  %s %s" % (Job_ID,Job_Setting))

#----------------------------------------------------------------------
def GetJobsFilter(Filter_1,Repeated_Arg):
	"""Display jobs that fulfill the specified filters.

	Params: Name: Discription
	------------------------------
		| **Filter_1** : *A filter, in the form of <Setting=Value>*
		| **Repeated_Arg** : *Additional filters...*
	"""
	return CallDeadlineCommand("GetJobsFilter  %s %s" % (Filter_1,Repeated_Arg))

#----------------------------------------------------------------------
def GetJobsFilterAnd(Filter_1,Repeated_Arg):
	"""Display jobs that fulfill all the specified filters.

	Params: Name: Discription
	------------------------------
		| **Filter_1** : *A filter, in the form of <Setting=Value>*
		| **Repeated_Arg** : *Additional filters...*
	"""
	return CallDeadlineCommand("GetJobsFilterAnd  %s %s" % (Filter_1,Repeated_Arg))

#----------------------------------------------------------------------
def GetJobsFilterIni(Filter_1,Repeated_Arg):
	"""Display jobs that fulfill the specified filters, in an ini format.

	Params: Name: Discription
	------------------------------
		| **Filter_1** : *A filter, in the form of <Setting=Value>*
		| **Repeated_Arg** : *Additional filters...*
	"""
	return CallDeadlineCommand("GetJobsFilterIni  %s %s" % (Filter_1,Repeated_Arg))

#----------------------------------------------------------------------
def GetJobsFilterIniAnd(Filter_1,Repeated_Arg):
	"""Display jobs that fulfill all the specified filters, in an ini format.

	Params: Name: Discription
	------------------------------
		| **Filter_1** : *A filter, in the form of <Setting=Value>*
		| **Repeated_Arg** : *Additional filters...*
	"""
	return CallDeadlineCommand("GetJobsFilterIniAnd  %s %s" % (Filter_1,Repeated_Arg))

#----------------------------------------------------------------------
def GetJobStatistics():
	"""Displays quick summary information of jobs"""
	return CallDeadlineCommand("GetJobStatistics")

#----------------------------------------------------------------------
def GetJobTask(Job_ID,Task_ID):
	"""Display the specified task for the job.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
		| **Task_ID** : *The task ID*
	"""
	return CallDeadlineCommand("GetJobTask  %s %s" % (Job_ID,Task_ID))

#----------------------------------------------------------------------
def GetJobTaskAverageTime(Job_ID):
	"""Display average task render time for the job.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
	"""
	return CallDeadlineCommand("GetJobTaskAverageTime  %s" % (Job_ID))

#----------------------------------------------------------------------
def GetJobTaskAverageTimeNorm(Job_ID):
	"""Display average task normalized render time for the job.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
	"""
	return CallDeadlineCommand("GetJobTaskAverageTimeNorm  %s" % (Job_ID))

#----------------------------------------------------------------------
def GetJobTaskIds(Job_ID):
	"""Display the task IDs for the job.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
	"""
	return CallDeadlineCommand("GetJobTaskIds  %s" % (Job_ID))

#----------------------------------------------------------------------
def GetJobTaskLimit():
	"""Displays the task limit value for job."""
	return CallDeadlineCommand("GetJobTaskLimit")

#----------------------------------------------------------------------
def GetJobTasks(Job_ID,Use_Ini_Display):
	"""Display the tasks for the job.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
		| **Use_Ini_Display** : *true/false (optional, default is false)*
	"""
	return CallDeadlineCommand("GetJobTasks  %s %s" % (Job_ID,Use_Ini_Display))

#----------------------------------------------------------------------
def GetJobTaskTotalTime(Job_ID):
	"""Display total task render time for the job.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
	"""
	return CallDeadlineCommand("GetJobTaskTotalTime  %s" % (Job_ID))

#----------------------------------------------------------------------
def GetJobTaskTotalTimeNorm(Job_ID):
	"""Display total task normalized render time for the job.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
	"""
	return CallDeadlineCommand("GetJobTaskTotalTimeNorm  %s" % (Job_ID))

#----------------------------------------------------------------------
def GetLicenseMode():
	"""Gets the Deadline License Mode"""
	return CallDeadlineCommand("GetLicenseMode")

#----------------------------------------------------------------------
def GetLicenseServer():
	"""Gets the Deadline License Server"""
	return CallDeadlineCommand("GetLicenseServer")

#----------------------------------------------------------------------
def GetLimitGroup(Limit_Names,Use_Ini_Display):
	"""Displays information for the limit.

	Params: Name: Discription
	------------------------------
		| **Limit_Names** : *The limit name, or a list of names separated by commas*
		| **Use_Ini_Display** : *true/false (optional, default is false)*
	"""
	Limit_Names = Limit_Names if not isinstance(Limit_Names,(list,tuple)) else ','.join([str(item) for item in Limit_Names])
	return CallDeadlineCommand("GetLimitGroup  %s %s" % (Limit_Names,Use_Ini_Display))

#----------------------------------------------------------------------
def GetLimitGroupNames():
	"""Display all limit names."""
	return CallDeadlineCommand("GetLimitGroupNames")

#----------------------------------------------------------------------
def GetLimitGroups(Use_Ini_Display):
	"""Displays information for all limits.

	Params: Name: Discription
	------------------------------
		| **Use_Ini_Display** : *true/false (optional, default is false)*
	"""
	return CallDeadlineCommand("GetLimitGroups  %s" % (Use_Ini_Display))

#----------------------------------------------------------------------
def GetMachinesRenderingJob(Job_ID,Get_IP_Address,Get_Duplicates):
	"""Display the machine names of the Workers that are rendering the job. If the second parameter is 'true', the machine IP addresses will be shown instead. If the third parameter is 'true', then duplicate machine names and IP addresses will be shown.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
		| **Get_IP_Address** : *true/false (optional, default is false)*
		| **Get_Duplicates** : *true/false (optional, default is false)*
	"""
	Get_IP_Address = Get_IP_Address if not isinstance(Get_IP_Address,(list,tuple)) else ','.join([str(item) for item in Get_IP_Address])
	Get_Duplicates = Get_Duplicates if not isinstance(Get_Duplicates,(list,tuple)) else ','.join([str(item) for item in Get_Duplicates])
	return CallDeadlineCommand("GetMachinesRenderingJob  %s %s %s" % (Job_ID,Get_IP_Address,Get_Duplicates))

#----------------------------------------------------------------------
def GetMajorVersion():
	"""Gets the Deadline Major Version"""
	return CallDeadlineCommand("GetMajorVersion")

#----------------------------------------------------------------------
def GetMaximumPriority():
	"""Displays the maximum priority value for jobs."""
	return CallDeadlineCommand("GetMaximumPriority")

#----------------------------------------------------------------------
def GetNetworkDrives():
	"""Display all network drives"""
	return CallDeadlineCommand("GetNetworkDrives")

#----------------------------------------------------------------------
def GetPathMappings():
	"""Returns a list of all path mappings that can will be applied in the current context. Uses the path mappings in the Repository Options."""
	return CallDeadlineCommand("GetPathMappings")

#----------------------------------------------------------------------
def GetPluginLimitGroups(Plugin_Name):
	"""Displays all limit group names assigned to a Plugin.

	Params: Name: Discription
	------------------------------
		| **Plugin_Name** : *The name of the Plugin to retrieve Limits for.*
	"""
	return CallDeadlineCommand("GetPluginLimitGroups  %s" % (Plugin_Name))

#----------------------------------------------------------------------
def GetPluginNames():
	"""Displays all plugin names."""
	return CallDeadlineCommand("GetPluginNames")

#----------------------------------------------------------------------
def GetPoolNames():
	"""Displays all pool names."""
	return CallDeadlineCommand("GetPoolNames")

#----------------------------------------------------------------------
def GetProcess(Process_Name,Use_Ini_Display):
	"""Displays information for all running processes with the given name.

	Params: Name: Discription
	------------------------------
		| **Process_Name** : *Process name to search for*
		| **Use_Ini_Display** : *true/false (optional, default is false)*
	"""
	return CallDeadlineCommand("GetProcess  %s %s" % (Process_Name,Use_Ini_Display))

#----------------------------------------------------------------------
def GetProcesses(Use_Ini_Display):
	"""Displays information for all running processes.

	Params: Name: Discription
	------------------------------
		| **Use_Ini_Display** : *true/false (optional, default is false)*
	"""
	return CallDeadlineCommand("GetProcesses  %s" % (Use_Ini_Display))

#----------------------------------------------------------------------
def GetProcessNames(Process_Name):
	"""Displays all running process names.

	Params: Name: Discription
	------------------------------
		| **Process_Name** : *Process name to search for (optional)*
	"""
	return CallDeadlineCommand("GetProcessNames  %s" % (Process_Name))

#----------------------------------------------------------------------
def GetProxyServerInfo(Proxy_Server_Name):
	"""Get ProxyServerInfo for a specified (by name) Proxy Server.

	Params: Name: Discription
	------------------------------
		| **Proxy_Server_Name** : *Name of the Proxy Server to query.*
	"""
	return CallDeadlineCommand("GetProxyServerInfo  %s" % (Proxy_Server_Name))

#----------------------------------------------------------------------
def GetProxyServerInfos(Proxy_Server_Names):
	"""Get ProxyServerInfo for all specified (by name) Proxy Servers.

	Params: Name: Discription
	------------------------------
		| **Proxy_Server_Names** : *Comma-separated list of Proxy Server names to query. Leave blank to query all Proxy Servers.*
	"""
	Proxy_Server_Names = Proxy_Server_Names if not isinstance(Proxy_Server_Names,(list,tuple)) else ','.join([str(item) for item in Proxy_Server_Names])
	return CallDeadlineCommand("GetProxyServerInfos  %s" % (Proxy_Server_Names))

#----------------------------------------------------------------------
def GetProxyServerNames():
	"""Display all Proxy Server names."""
	return CallDeadlineCommand("GetProxyServerNames")

#----------------------------------------------------------------------
def GetProxyServerSettings(Proxy_Server_Name):
	"""Get ProxyServerInfo for a specified (by name) Proxy Server.

	Params: Name: Discription
	------------------------------
		| **Proxy_Server_Name** : *Name of the Proxy Server to query.*
	"""
	return CallDeadlineCommand("GetProxyServerSettings  %s" % (Proxy_Server_Name))

#----------------------------------------------------------------------
def GetProxyServerSettingsList(Proxy_Server_Names):
	"""Get ProxyServerSettings for all specified (by name) Proxy Servers.

	Params: Name: Discription
	------------------------------
		| **Proxy_Server_Names** : *Comma-separated list of Proxy Server names to query. Leave blank to query all Proxy Servers.*
	"""
	Proxy_Server_Names = Proxy_Server_Names if not isinstance(Proxy_Server_Names,(list,tuple)) else ','.join([str(item) for item in Proxy_Server_Names])
	return CallDeadlineCommand("GetProxyServerSettingsList  %s" % (Proxy_Server_Names))

#----------------------------------------------------------------------
def GetPublicEncryptionKey(UserSpecific):
	"""Prints out the Public Key used for encryption of messages sent to this Deadline client, in XML format. This creates a key if one is not already present, and therefore might require administrator/root privileges when retrieving the machine-wide key.

	Params: Name: Discription
	------------------------------
		| **UserSpecific** : *If True, key specific to the current OS user will be returned. (Default: False)*
	"""
	return CallDeadlineCommand("GetPublicEncryptionKey  %s" % (UserSpecific))

#----------------------------------------------------------------------
def GetPublicSigningKey(UserSpecific):
	"""Prints out the Public Key used for verification of signatures by this Deadline client, in XML format. This creates a key if one is not already present, and therefore might require administrator/root privileges privileges when retrieving the machine-wide key.

	Params: Name: Discription
	------------------------------
		| **UserSpecific** : *If True, key specific to the current OS user will be returned. (Default: False)*
	"""
	return CallDeadlineCommand("GetPublicSigningKey  %s" % (UserSpecific))

#----------------------------------------------------------------------
def GetPulseInfo(Pulse_Name):
	"""Gets the pulse information.

	Params: Name: Discription
	------------------------------
		| **Pulse_Name** : *The pulse name*
	"""
	return CallDeadlineCommand("GetPulseInfo  %s" % (Pulse_Name))

#----------------------------------------------------------------------
def GetPulseInfos(Pulse_Names):
	"""Gets the pulse information for the specified pulses or all pulses.

	Params: Name: Discription
	------------------------------
		| **Pulse_Names** : *The pulse name, or a list of pulse names separated by commas, or none to retrieve all pulse info*
	"""
	Pulse_Names = Pulse_Names if not isinstance(Pulse_Names,(list,tuple)) else ','.join([str(item) for item in Pulse_Names])
	return CallDeadlineCommand("GetPulseInfos  %s" % (Pulse_Names))

#----------------------------------------------------------------------
def GetPulseNames():
	"""Get pulse names."""
	return CallDeadlineCommand("GetPulseNames")

#----------------------------------------------------------------------
def GetPulseSettings(Pulse_Name):
	"""Gets the pulse settings for a specified pulse.

	Params: Name: Discription
	------------------------------
		| **Pulse_Name** : *The pulse name*
	"""
	return CallDeadlineCommand("GetPulseSettings  %s" % (Pulse_Name))

#----------------------------------------------------------------------
def GetPulseSettingsList(Pulse_Names):
	"""Gets the pulse settings for specified or all pulses.

	Params: Name: Discription
	------------------------------
		| **Pulse_Names** : *The pulse name, or a list of pulse names separated by a comma, or none to retrieve all pulse settings*
	"""
	Pulse_Names = Pulse_Names if not isinstance(Pulse_Names,(list,tuple)) else ','.join([str(item) for item in Pulse_Names])
	return CallDeadlineCommand("GetPulseSettingsList  %s" % (Pulse_Names))

#----------------------------------------------------------------------
def GetRegistryKeyValue(Key_Name,Value_Name,Default_Value):
	"""Returns the specified value for the specified registry key.

	Params: Name: Discription
	------------------------------
		| **Key_Name** : *The name of the registry key*
		| **Value_Name** : *The name of the value to get*
		| **Default_Value** : *(optional) The default value to return*
	"""
	return CallDeadlineCommand("GetRegistryKeyValue  %s %s %s" % (Key_Name,Value_Name,Default_Value))

#----------------------------------------------------------------------
def GetRepositoryFilePath(FilePath,Custom):
	"""Returns the appropriate full path to the given file in the Repository.

	Params: Name: Discription
	------------------------------
		| **FilePath** : *The repository's file path to retrieve.*
		| **Custom** : *Whether or not to check the Custom folder first.*
	"""
	return CallDeadlineCommand("GetRepositoryFilePath  %s %s" % (FilePath,Custom))

#----------------------------------------------------------------------
def GetRepositoryOption(Repository_Option):
	"""Gets the value of the provided Repository Option if it exists and is exposed.

	Params: Name: Discription
	------------------------------
		| **Repository_Option** : *The name of the Repository Option we want to get*
	"""
	return CallDeadlineCommand("GetRepositoryOption  %s" % (Repository_Option))

#----------------------------------------------------------------------
def GetRepositoryOptions():
	"""Displays the list of all exposed Repository Options."""
	return CallDeadlineCommand("GetRepositoryOptions")

#----------------------------------------------------------------------
def GetRepositoryOptionsWithValues():
	"""Displays the list of all exposed Repository Options and their values."""
	return CallDeadlineCommand("GetRepositoryOptionsWithValues")

#----------------------------------------------------------------------
def GetRepositoryPath(Subdir,Custom):
	"""Returns the appropriate full path to the given subdirectory of the Repository.

	Params: Name: Discription
	------------------------------
		| **Subdir** : *The repository's sub-directory to retrieve.*
		| **Custom** : *Whether or not to check the Custom folder first.*
	"""
	return CallDeadlineCommand("GetRepositoryPath  %s %s" % (Subdir,Custom))

#----------------------------------------------------------------------
def GetRepositoryRoot():
	"""Display the repository network root"""
	return CallDeadlineCommand("GetRepositoryRoot")

#----------------------------------------------------------------------
def GetRepositoryRoots():
	"""Display all repository roots in the Deadline config file"""
	return CallDeadlineCommand("GetRepositoryRoots")

#----------------------------------------------------------------------
def GetRepositoryVersion():
	"""Gets the Deadline Repository and Integration Version"""
	return CallDeadlineCommand("GetRepositoryVersion")

#----------------------------------------------------------------------
def GetSettingsDirectory():
	"""Displays settings directory of the Deadline Client software"""
	return CallDeadlineCommand("GetSettingsDirectory")

#----------------------------------------------------------------------
def GetSlave(Worker_Names,Use_Ini_Display):
	"""Display information for the Worker.

	Params: Name: Discription
	------------------------------
		| **Worker_Names** : *The Worker name, or a list of Worker names separated by commas*
		| **Use_Ini_Display** : *true/false (optional, default is false)*
	"""
	Worker_Names = Worker_Names if not isinstance(Worker_Names,(list,tuple)) else ','.join([str(item) for item in Worker_Names])
	return CallDeadlineCommand("GetSlave  %s %s" % (Worker_Names,Use_Ini_Display))

#----------------------------------------------------------------------
def GetSlaveErrorReportFilenames(Worker_Name):
	"""Gets the error report filenames for the Worker.

	Params: Name: Discription
	------------------------------
		| **Worker_Name** : *The Worker name*
	"""
	return CallDeadlineCommand("GetSlaveErrorReportFilenames  %s" % (Worker_Name))

#----------------------------------------------------------------------
def GetSlaveExtraInfoKeyValue(Worker_Name,Extra_Info_Key):
	"""Gets the value from the extra info dictionary.

	Params: Name: Discription
	------------------------------
		| **Worker_Name** : *The name of the Worker*
		| **Extra_Info_Key** : *The extra info key to get.*
	"""
	return CallDeadlineCommand("GetSlaveExtraInfoKeyValue  %s %s" % (Worker_Name,Extra_Info_Key))

#----------------------------------------------------------------------
def GetSlaveInfo(Worker_Name,Worker_Info_Name):
	"""Gets the info value for the Worker.

	Params: Name: Discription
	------------------------------
		| **Worker_Name** : *The Worker name*
		| **Worker_Info_Name** : *The name of the info*
	"""
	return CallDeadlineCommand("GetSlaveInfo  %s %s" % (Worker_Name,Worker_Info_Name))

#----------------------------------------------------------------------
def GetSlaveLogReportFilenames(Worker_Name):
	"""Gets the log report filenames for the Worker.

	Params: Name: Discription
	------------------------------
		| **Worker_Name** : *The Worker name*
	"""
	return CallDeadlineCommand("GetSlaveLogReportFilenames  %s" % (Worker_Name))

#----------------------------------------------------------------------
def GetSlaveNames():
	"""Displays all the Worker names."""
	return CallDeadlineCommand("GetSlaveNames")

#----------------------------------------------------------------------
def GetSlaveNamesInGroup(Group_Names):
	"""Displays the Worker names that have been assigned to the specified group.

	Params: Name: Discription
	------------------------------
		| **Group_Names** : *The group name, or a list of group names separated by commas*
	"""
	Group_Names = Group_Names if not isinstance(Group_Names,(list,tuple)) else ','.join([str(item) for item in Group_Names])
	return CallDeadlineCommand("GetSlaveNamesInGroup  %s" % (Group_Names))

#----------------------------------------------------------------------
def GetSlaveNamesInPool(Pool_Names):
	"""Displays the Worker names that have been assigned to the specified pool.

	Params: Name: Discription
	------------------------------
		| **Pool_Names** : *The pool name, or a list of pool names separated by commas*
	"""
	Pool_Names = Pool_Names if not isinstance(Pool_Names,(list,tuple)) else ','.join([str(item) for item in Pool_Names])
	return CallDeadlineCommand("GetSlaveNamesInPool  %s" % (Pool_Names))

#----------------------------------------------------------------------
def GetSlaveReportFilenames(Worker_Name):
	"""Gets the report filenames for the Worker.

	Params: Name: Discription
	------------------------------
		| **Worker_Name** : *The Worker name*
	"""
	return CallDeadlineCommand("GetSlaveReportFilenames  %s" % (Worker_Name))

#----------------------------------------------------------------------
def GetSlaves(Use_Ini_Display):
	"""Displays information for all the Worker names.

	Params: Name: Discription
	------------------------------
		| **Use_Ini_Display** : *true/false (optional, default is false)*
	"""
	return CallDeadlineCommand("GetSlaves  %s" % (Use_Ini_Display))

#----------------------------------------------------------------------
def GetSlaveSetting(Worker_Name,Worker_Setting):
	"""Gets the value of a setting for the Worker.

	Params: Name: Discription
	------------------------------
		| **Worker_Name** : *The Worker name*
		| **Worker_Setting** : *The Worker setting*
	"""
	return CallDeadlineCommand("GetSlaveSetting  %s %s" % (Worker_Name,Worker_Setting))

#----------------------------------------------------------------------
def GetSlavesRenderingJob(Job_ID):
	"""Display the Workers that are rendering the job.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
	"""
	return CallDeadlineCommand("GetSlavesRenderingJob  %s" % (Job_ID))

#----------------------------------------------------------------------
def GetSlaveStatistics():
	"""Displays quick summary information of Workers"""
	return CallDeadlineCommand("GetSlaveStatistics")

#----------------------------------------------------------------------
def GetSubmissionInfo(Types):
	"""Displays common submission information that can be used by job submission scripts.

	Params: Name: Discription
	------------------------------
		| **Types** : *A list of specific submission information. Each type should be separated by a space. The available types are: version, shortversion, pools, groups, maxpriority, tasklimit, homedir, userhomedir, repodir:[folder], repodirnocustom:[folder], filetransferserver. Note that repodir and repodirnocustom can be specified multiple times, and each one should be followed by a colon and a repository folder.*
	"""
	Types = Types if not isinstance(Types,(list,tuple)) else ' '.join([str(item) for item in Types])
	return CallDeadlineCommand("GetSubmissionInfo  %s" % (Types))

#----------------------------------------------------------------------
def GetTaskProgress(Job_ID):
	"""Display progress information about the job's tasks.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
	"""
	return CallDeadlineCommand("GetTaskProgress  %s" % (Job_ID))

#----------------------------------------------------------------------
def GetUser(User_Names,Use_Ini_Display):
	"""Displays information for the user.

	Params: Name: Discription
	------------------------------
		| **User_Names** : *The user name, or a list of names separated by commas*
		| **Use_Ini_Display** : *true/false (optional, default is false)*
	"""
	User_Names = User_Names if not isinstance(User_Names,(list,tuple)) else ','.join([str(item) for item in User_Names])
	return CallDeadlineCommand("GetUser  %s %s" % (User_Names,Use_Ini_Display))

#----------------------------------------------------------------------
def GetUserGroup(User_Group_Name):
	"""Displays all User names in User Group.

	Params: Name: Discription
	------------------------------
		| **User_Group_Name** : *The user group name*
	"""
	return CallDeadlineCommand("GetUserGroup  %s" % (User_Group_Name))

#----------------------------------------------------------------------
def GetUserGroupNames():
	"""Display all the user group names."""
	return CallDeadlineCommand("GetUserGroupNames")

#----------------------------------------------------------------------
def GetUserGroupsForUser(User_Name):
	"""Display all the user group names for the user.

	Params: Name: Discription
	------------------------------
		| **User_Name** : *The user name*
	"""
	return CallDeadlineCommand("GetUserGroupsForUser  %s" % (User_Name))

#----------------------------------------------------------------------
def GetUserNames():
	"""Display all the user names."""
	return CallDeadlineCommand("GetUserNames")

#----------------------------------------------------------------------
def GetUsers(Use_Ini_Display):
	"""Displays information for all users.

	Params: Name: Discription
	------------------------------
		| **Use_Ini_Display** : *true/false (optional, default is false)*
	"""
	return CallDeadlineCommand("GetUsers  %s" % (Use_Ini_Display))

#----------------------------------------------------------------------
def GetVersion():
	"""Gets the Deadline Version"""
	return CallDeadlineCommand("GetVersion")

#----------------------------------------------------------------------
def Groups():
	"""Displays all groups."""
	return CallDeadlineCommand("Groups")

#----------------------------------------------------------------------
def ImportJob(Delete_Archive,Archived_Job_File):
	"""Imports the archived job.

	Params: Name: Discription
	------------------------------
		| **Delete_Archive** : *If the original archive should be deleted (true/false).*
		| **Archived_Job_File** : *The archived job file. Specify multiple files as separate parameters.*
	"""
	return CallDeadlineCommand("ImportJob  %s %s" % (Delete_Archive,Archived_Job_File))

#----------------------------------------------------------------------
def InstallLauncherService(true_or_false):
	"""Installs the Deadline Launcher Service, and optionally starts it.

	Params: Name: Discription
	------------------------------
		| **true_or_false** : *Whether or not to start the Launcher Service after it has been installed (optional)*
	"""
	return CallDeadlineCommand("InstallLauncherService  %s" % (true_or_false))

#----------------------------------------------------------------------
def InstallLauncherServiceLogOn(User_Name,Password,true_or_false):
	"""Installs the Deadline Launcher Service with the given account, and optionally starts it.

	Params: Name: Discription
	------------------------------
		| **User_Name** : *The account user name*
		| **Password** : *The account password. If empty or not specified, the caller will be prompted to enter it via standard input.*
		| **true_or_false** : *Whether or not to start the Launcher Service after it has been installed (optional)*
	"""
	return CallDeadlineCommand("InstallLauncherServiceLogOn  %s %s %s" % (User_Name,Password,true_or_false))

#----------------------------------------------------------------------
def JobStatistics(Start_Date,End_Date,Pool_Filter,Group_Filter,Plugin_Filter):
	"""Shows statistics for jobs that have completed between the specified dates, inclusive.

	Params: Name: Discription
	------------------------------
		| **Start_Date** : *The start date in the form yyyy-MM (ie: 2010-01)*
		| **End_Date** : *The end date in the form yyyy-MM (ie: 2010-12)*
		| **Pool_Filter** : *A comma separate list of pools (or an empty string for no filter)*
		| **Group_Filter** : *A comma separate list of groups (or an empty string for no filter)*
		| **Plugin_Filter** : *A comma separate list of plugins (or an empty string for no filter)*
	"""
	return CallDeadlineCommand("JobStatistics  %s %s %s %s %s" % (Start_Date,End_Date,Pool_Filter,Group_Filter,Plugin_Filter))

#----------------------------------------------------------------------
def JobSubmissionInfoFromJob(Job_ID):
	"""Generates a list of Job Submission Parameters that can be used to submit a similar Job to the one provided.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The ID of the Job on which to base the Job Submission Parameters.*
	"""
	return CallDeadlineCommand("JobSubmissionInfoFromJob  %s" % (Job_ID))

#----------------------------------------------------------------------
def KillProcess(Process_Name_Or_ID):
	"""Kills all processes with specified name or PID.

	Params: Name: Discription
	------------------------------
		| **Process_Name_Or_ID** : *Name of the process or process ID*
	"""
	return CallDeadlineCommand("KillProcess  %s" % (Process_Name_Or_ID))

#----------------------------------------------------------------------
def LaunchPreviewStyleWindow(Style):
	"""Previews a style.

	Params: Name: Discription
	------------------------------
		| **Style** : *The style info to preview (JSON format)*
	"""
	return CallDeadlineCommand("LaunchPreviewStyleWindow  %s" % (Style))

#----------------------------------------------------------------------
def LimitGroups():
	"""Display all limit names."""
	return CallDeadlineCommand("LimitGroups")

#----------------------------------------------------------------------
def MapDrives():
	"""Maps mapped drives from network settings on Windows."""
	return CallDeadlineCommand("MapDrives")

#----------------------------------------------------------------------
def Multi(dependent,notify,Job_Files):
	"""Submits multiple jobs at once.

	Params: Name: Discription
	------------------------------
		| **dependent** : *This flag makes each job in the list of jobs specified dependent on the previous job. This is shorthand for specifying -dependsonprevious for each job being submitted*
		| **notify** : *This flag displays a notification window after the jobs have been submitted*
		| **Job_Files** : *This flag must precede each list of files for each individual job being submitted. You can also add the -dependsonprevious flag to make a single job dependent on the previous job*
	"""
	Job_Files = Job_Files if not isinstance(Job_Files,(list,tuple)) else ','.join([str(item) for item in Job_Files])
	return CallDeadlineCommand("Multi  %s %s %s" % (dependent,notify,Job_Files))

#----------------------------------------------------------------------
def Networks():
	"""Display all repository roots in the Deadline config file"""
	return CallDeadlineCommand("Networks")

#----------------------------------------------------------------------
def NewUserGroups(User_Group_Names):
	"""Creates new User Groups with the given user group names, if they do not already exist.

	Params: Name: Discription
	------------------------------
		| **User_Group_Names** : *The user group name, or a list of user group names separated by commas*
	"""
	User_Group_Names = User_Group_Names if not isinstance(User_Group_Names,(list,tuple)) else ','.join([str(item) for item in User_Group_Names])
	return CallDeadlineCommand("NewUserGroups  %s" % (User_Group_Names))

#----------------------------------------------------------------------
def Notify(drop,notify,deleteFiles):
	"""Submits a job and notifies upon completion.

	Params: Name: Discription
	------------------------------
		| **drop** : *Specify this flag to do a drop job*
		| **notify** : *Specify this flag to display a notification when submission completes*
		| **deleteFiles** : *Specify this flag to delete local files after submission*
	"""
	deleteFiles = deleteFiles if not isinstance(deleteFiles,(list,tuple)) else ','.join([str(item) for item in deleteFiles])
	return CallDeadlineCommand("Notify  %s %s %s" % (drop,notify,deleteFiles))

#----------------------------------------------------------------------
def ParseFrameList(frame_list,combine_frames):
	"""Parses a frame list.

	Params: Name: Discription
	------------------------------
		| **frame_list** : *The list of frames to parse*
		| **combine_frames** : *If subsequent frames should be combined (optional, defaults to true)*
	"""
	combine_frames = combine_frames if not isinstance(combine_frames,(list,tuple)) else ','.join([str(item) for item in combine_frames])
	return CallDeadlineCommand("ParseFrameList  %s %s" % (frame_list,combine_frames))

#----------------------------------------------------------------------
def PendJob(Job_IDs):
	"""Marks the job as pending (if it has job dependencies, required assets, or scheduling settings).

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The job ID, or a list of job IDs separated by commas*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	return CallDeadlineCommand("PendJob  %s" % (Job_IDs))

#----------------------------------------------------------------------
def Plugins():
	"""Displays all plugin names."""
	return CallDeadlineCommand("Plugins")

#----------------------------------------------------------------------
def PluginSubmissionInfoFromJob(Job_ID):
	"""Generates a list of Plugin Submission Parameters that can be used to submit a similar Job to the one provided.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The ID of the Job on which to base the Plugin Submission Parameters.*
	"""
	return CallDeadlineCommand("PluginSubmissionInfoFromJob  %s" % (Job_ID))

#----------------------------------------------------------------------
def Pools():
	"""Displays all pool names."""
	return CallDeadlineCommand("Pools")

#----------------------------------------------------------------------
def PopulateAssetServerDefaultSettings(Force,Global_Whitelist_Patte):
	"""Populate the default settings for Asset Server.

	Params: Name: Discription
	------------------------------
		| **Force** : *Whether to repopulate the default settings for asset server (this may override existing settings)*
		| **Global_Whitelist_Patte** : *The file containing the global whitelist patterns*
	"""
	return CallDeadlineCommand("PopulateAssetServerDefaultSettings  %s %s" % (Force,Global_Whitelist_Patte))

#----------------------------------------------------------------------
def PopulatePythonSync(PopulatePythonSync):
	"""Adds the PythonSync zip to the user folder in the appropriate place.

	Params: Name: Discription
	------------------------------
		| **PopulatePythonSync** : *The path to the PythonSync.zip.*
	"""
	return CallDeadlineCommand("PopulatePythonSync  %s" % (PopulatePythonSync))

#----------------------------------------------------------------------
def PopupMessage(Message,Delete_Message_File):
	"""Displays a popup message.

	Params: Name: Discription
	------------------------------
		| **Message** : *The message to display. This can be a string, or a path to a file that contains a message.*
		| **Delete_Message_File** : *(optional) If the message is stored in a file, specify 'true' to delete the file after.*
	"""
	return CallDeadlineCommand("PopupMessage  %s %s" % (Message,Delete_Message_File))

#----------------------------------------------------------------------
def Prompt():
	"""Turn on interactive Deadline Command mode."""
	return CallDeadlineCommand("Prompt")

#----------------------------------------------------------------------
def PurgeDeletedJob(Job_IDs):
	"""Purges the deleted job(s).

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The deleted job ID, or a list of deleted job IDs separated by commas*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	return CallDeadlineCommand("PurgeDeletedJob  %s" % (Job_IDs))

#----------------------------------------------------------------------
def PurgeObsoleteGroups(Group_Name):
	"""Purges groups that are no longer in use.

	Params: Name: Discription
	------------------------------
		| **Group_Name** : *The replacement group for jobs that are using obsolete groups (optional)*
	"""
	return CallDeadlineCommand("PurgeObsoleteGroups  %s" % (Group_Name))

#----------------------------------------------------------------------
def PurgeObsoletePools(Pool_Name):
	"""Purges pools that are no longer in use.

	Params: Name: Discription
	------------------------------
		| **Pool_Name** : *The replacement pool for jobs that are using obsolete pools (optional)*
	"""
	return CallDeadlineCommand("PurgeObsoletePools  %s" % (Pool_Name))

#----------------------------------------------------------------------
def Quit():
	"""Exit Deadline Interactive mode. Equivalent to Exit."""
	return CallDeadlineCommand("Quit")

#----------------------------------------------------------------------
def ReleasePendingJob(Job_IDs):
	"""Releases the pending job.

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The job ID, or a list of job IDs separated by commas*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	return CallDeadlineCommand("ReleasePendingJob  %s" % (Job_IDs))

#----------------------------------------------------------------------
def RemoteControl(Machine_Names,Remote_Command,Argument):
	"""Send the remote command to the Deadline Launcher running on the specified machine(s).

	Params: Name: Discription
	------------------------------
		| **Machine_Names** : *The machine name, or a list of machine names separated by commas.*
		| **Remote_Command** : *The remote command. The available commands are StopLauncher, LaunchSlave, LaunchAllSlaves, LaunchNewSlave, RemoveSlave, LaunchSlaveDelay, StopSlave, RelaunchSlave, ForceStopSlave, ForceRelaunchSlave, OnLastTaskComplete, LaunchPulse, StopPulse, RestartPulse, RemotePulseCommand, LaunchProxyServer, StopProxyServer, RestartProxyServer, LaunchBalancer, StopBalancer, RestartBalancer, RemoteBalancerCommand, LaunchMonitor, StopMonitor, StopConfig, RestartMachine, StartMachine, ShutdownMachine, Execute, ExecuteNoWait*
		| **Argument** : *The argument for LaunchSlave, LaunchNewSlave, and RemoveSlave is the name of the Worker. The argument for Execute and ExecuteNoWait is the command to execute. Valid arguments for OnLastTaskComplete are Continue, StopSlave, RestartSlave, CheckForTasks, CancelTask, ClearFailureCache, ShutdownMachine [comment] and RestartMachine [comment]. [comment] is a message that can be sent to explain why the shutdown or restart machine command was executed. It will be recorded in the machines event log. Valid arguments for RemotePulseCommand are HouseCleaning, PendingJobScan, RepositoryRepair, and PowerManagement. Valid arguments for RemoteBalancerCommand are Balancing.*
	"""
	Machine_Names = Machine_Names if not isinstance(Machine_Names,(list,tuple)) else ','.join([str(item) for item in Machine_Names])
	return CallDeadlineCommand("RemoteControl  %s %s %s" % (Machine_Names,Remote_Command,Argument))

#----------------------------------------------------------------------
def RemoveCloudRegion(CloudRegion):
	"""Remove a Cloud Region. This will terminate any running instances that have been started in this region. Also, this will purge the region from Balancer, Pulse and User settings. Additionally, this will remove any mapped paths for this region.

	Params: Name: Discription
	------------------------------
		| **CloudRegion** : *The name of the Cloud Region*
	"""
	return CallDeadlineCommand("RemoveCloudRegion  %s" % (CloudRegion))

#----------------------------------------------------------------------
def RemoveGroupFromSlave(Worker_Names,Group_Names):
	"""Removes a group from the Worker.

	Params: Name: Discription
	------------------------------
		| **Worker_Names** : *The Worker name, or a list of Worker names separated by commas*
		| **Group_Names** : *The group name, or a list of group names separated by commas*
	"""
	Worker_Names = Worker_Names if not isinstance(Worker_Names,(list,tuple)) else ','.join([str(item) for item in Worker_Names])
	Group_Names = Group_Names if not isinstance(Group_Names,(list,tuple)) else ','.join([str(item) for item in Group_Names])
	return CallDeadlineCommand("RemoveGroupFromSlave  %s %s" % (Worker_Names,Group_Names))

#----------------------------------------------------------------------
def RunAWSPortalS3Setup(Region):
	"""Creates S3 buckets and access policies/users/roles for use with AWS Portal Asset Server.

	Params: Name: Discription
	------------------------------
		| **Region** : *An AWS Region*
	"""
	return CallDeadlineCommand("RunAWSPortalS3Setup  %s" % (Region))

#----------------------------------------------------------------------
def RemovePoolFromSlave(Worker_Names,Pool_Names):
	"""Removes a pool from the Worker.

	Params: Name: Discription
	------------------------------
		| **Worker_Names** : *The Worker name, or a list of Worker names separated by commas*
		| **Pool_Names** : *The pool name, or a list of pool names separated by commas*
	"""
	Worker_Names = Worker_Names if not isinstance(Worker_Names,(list,tuple)) else ','.join([str(item) for item in Worker_Names])
	Pool_Names = Pool_Names if not isinstance(Pool_Names,(list,tuple)) else ','.join([str(item) for item in Pool_Names])
	return CallDeadlineCommand("RemovePoolFromSlave  %s %s" % (Worker_Names,Pool_Names))

#----------------------------------------------------------------------
def RemoveRegistryKeyValue(Key_Name,Value_Name,Recursive):
	"""Removes the specified value for the specified registry key. Enable Recursive to delete sub keys.

	Params: Name: Discription
	------------------------------
		| **Key_Name** : *The name of the registry key*
		| **Value_Name** : *The name of the value to remove*
		| **Recursive** : *True/False*
	"""
	return CallDeadlineCommand("RemoveRegistryKeyValue  %s %s %s" % (Key_Name,Value_Name,Recursive))

#----------------------------------------------------------------------
def RemoveSlavesFromJobMachineLimitList(Job_IDs,Workers):
	"""Removes Workers from the job's listed Workers.

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The job ID, or a list of job IDs separated by commas*
		| **Workers** : *The Workers to remove, separated by commas*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	Workers = Workers if not isinstance(Workers,(list,tuple)) else ','.join([str(item) for item in Workers])
	return CallDeadlineCommand("RemoveSlavesFromJobMachineLimitList  %s %s" % (Job_IDs,Workers))

#----------------------------------------------------------------------
def RemoveSlavesFromLimitGroupList(Limit_Names,Workers):
	"""Removes Workers from the limit's listed Workers.

	Params: Name: Discription
	------------------------------
		| **Limit_Names** : *The limit name, or a list of limit names separated by commas*
		| **Workers** : *The Workers to remove, separated by commas*
	"""
	Limit_Names = Limit_Names if not isinstance(Limit_Names,(list,tuple)) else ','.join([str(item) for item in Limit_Names])
	Workers = Workers if not isinstance(Workers,(list,tuple)) else ','.join([str(item) for item in Workers])
	return CallDeadlineCommand("RemoveSlavesFromLimitGroupList  %s %s" % (Limit_Names,Workers))

#----------------------------------------------------------------------
def RemoveUserFromUserGroup(User_Names,User_Group_Names):
	"""Removes a user from the user group.

	Params: Name: Discription
	------------------------------
		| **User_Names** : *The user name, or a list of user names separated by commas*
		| **User_Group_Names** : *The user group name, or a list of user group names separated by commas*
	"""
	User_Names = User_Names if not isinstance(User_Names,(list,tuple)) else ','.join([str(item) for item in User_Names])
	User_Group_Names = User_Group_Names if not isinstance(User_Group_Names,(list,tuple)) else ','.join([str(item) for item in User_Group_Names])
	return CallDeadlineCommand("RemoveUserFromUserGroup  %s %s" % (User_Names,User_Group_Names))

#----------------------------------------------------------------------
def RenderJob(JobInfoFile,PluginInfoFile,Auxiliary_Files):
	"""Renders a job immediately on the local machine without submitting it to the repository.

	Params: Name: Discription
	------------------------------
		| **JobInfoFile** : *The job info file*
		| **PluginInfoFile** : *The plugin info file*
		| **Auxiliary_Files** : *Additional optional files to submit with the job (specify each file as a separate argument)*
	"""
	Auxiliary_Files = Auxiliary_Files if not isinstance(Auxiliary_Files,(list,tuple)) else ','.join([str(item) for item in Auxiliary_Files])
	return CallDeadlineCommand("RenderJob  %s %s %s" % (JobInfoFile,PluginInfoFile,Auxiliary_Files))

#----------------------------------------------------------------------
def RequeueJob(Job_IDs):
	"""Requeues the job.

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The job ID, or a list of job IDs separated by commas*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	return CallDeadlineCommand("RequeueJob  %s" % (Job_IDs))

#----------------------------------------------------------------------
def RequeueJobTask(Job_ID,Task_ID):
	"""Requeues the specified task for the job.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
		| **Task_ID** : *The task ID*
	"""
	return CallDeadlineCommand("RequeueJobTask  %s %s" % (Job_ID,Task_ID))

#----------------------------------------------------------------------
def RequeueJobTasks(Job_ID,Task_IDs):
	"""Requeues the specified tasks for the job.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
		| **Task_IDs** : *The comma separated list of task IDs*
	"""
	Task_IDs = Task_IDs if not isinstance(Task_IDs,(list,tuple)) else ','.join([str(item) for item in Task_IDs])
	return CallDeadlineCommand("RequeueJobTasks  %s %s" % (Job_ID,Task_IDs))

#----------------------------------------------------------------------
def ResubmitJob(Job_ID,Frame_List,Chunk_Size,Submit_Suspended):
	"""Resubmits an existing job with a new frame list and chunksize.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The ID of the job to resubmit*
		| **Frame_List** : *The new frame list*
		| **Chunk_Size** : *The new chunk size*
		| **Submit_Suspended** : *If the job should be submitted suspended (optional)*
	"""
	return CallDeadlineCommand("ResubmitJob  %s %s %s %s" % (Job_ID,Frame_List,Chunk_Size,Submit_Suspended))

#----------------------------------------------------------------------
def ResumeFailedJob(Job_IDs):
	"""Resumes the failed job.

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The job ID, or a list of job IDs separated by commas*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	return CallDeadlineCommand("ResumeFailedJob  %s" % (Job_IDs))

#----------------------------------------------------------------------
def ResumeFailedJobTask(Job_ID,Task_ID):
	"""Resumes the specified failed task for the job.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
		| **Task_ID** : *The task ID*
	"""
	return CallDeadlineCommand("ResumeFailedJobTask  %s %s" % (Job_ID,Task_ID))

#----------------------------------------------------------------------
def ResumeFailedJobTasks(Job_ID,Task_IDs):
	"""Resumes the specified failed tasks for the job.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
		| **Task_IDs** : *The comma separated list of task IDs*
	"""
	Task_IDs = Task_IDs if not isinstance(Task_IDs,(list,tuple)) else ','.join([str(item) for item in Task_IDs])
	return CallDeadlineCommand("ResumeFailedJobTasks  %s %s" % (Job_ID,Task_IDs))

#----------------------------------------------------------------------
def ResumeJob(Job_IDs):
	"""Resumes the job.

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The job ID, or a list of job IDs separated by commas*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	return CallDeadlineCommand("ResumeJob  %s" % (Job_IDs))

#----------------------------------------------------------------------
def ResumeJobTask(Job_ID,Task_ID):
	"""Resumes the specified suspended task for the job.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
		| **Task_ID** : *The task ID*
	"""
	return CallDeadlineCommand("ResumeJobTask  %s %s" % (Job_ID,Task_ID))

#----------------------------------------------------------------------
def ResumeJobTasks(Job_ID,Task_IDs):
	"""Resumes the specified suspended tasks for the job.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
		| **Task_IDs** : *The comma separated list of task IDs*
	"""
	Task_IDs = Task_IDs if not isinstance(Task_IDs,(list,tuple)) else ','.join([str(item) for item in Task_IDs])
	return CallDeadlineCommand("ResumeJobTasks  %s %s" % (Job_ID,Task_IDs))

#----------------------------------------------------------------------
def Root():
	"""Display the repository network root"""
	return CallDeadlineCommand("Root")

#----------------------------------------------------------------------
def RunAWSPortalS3Setup(Region):
	"""Creates S3 buckets and access policies/users/roles for use with AWS Portal Asset Server.

	Params: Name: Discription
	------------------------------
		| **Region** : *An AWS Region*
	"""
	return CallDeadlineCommand("RunAWSPortalS3Setup  %s" % (Region))

#----------------------------------------------------------------------
def RunCommandForRepository(Connection_Type,Connection_String,Command):
	"""Runs the given command on a given repository.

	Params: Name: Discription
	------------------------------
		| **Connection_Type** : *The Connection type can be 'Direct' or 'Proxy'*
		| **Connection_String** : *Path to the repository root or the URL of a proxy repository.*
		| **Command** : *The command to execute followed by any additional arguments.*
	"""
	return CallDeadlineCommand("RunCommandForRepository  %s %s %s" % (Connection_Type,Connection_String,Command))

#----------------------------------------------------------------------
def SaveBalancerInfo(BalancerInfo_Object):
	"""Save a specified BalancerInfo object to the Database.

	Params: Name: Discription
	------------------------------
		| **BalancerInfo_Object** : *JSON Object representing a BalancerInfo to save.*
	"""
	return CallDeadlineCommand("SaveBalancerInfo  %s" % (BalancerInfo_Object))

#----------------------------------------------------------------------
def SaveBalancerSettings(BalancerSettings_Objec):
	"""Save a specified BalancerSettings object to the Database.

	Params: Name: Discription
	------------------------------
		| **BalancerSettings_Objec** : *JSON Object representing a BalancerSettings to save.*
	"""
	return CallDeadlineCommand("SaveBalancerSettings  %s" % (BalancerSettings_Objec))

#----------------------------------------------------------------------
def SaveCertificatePassword(Connection_String,Client_Certificate,Certificate_Password,All_Users):
	"""Allows you to change the password that is used to decrypt the given client certificate on this Machine, when connecting to the specified repository. Note that this is not currently implemented when using a Proxy connection.

	Params: Name: Discription
	------------------------------
		| **Connection_String** : *Required. When using Direct connection, this is the path to the root of the Repository. When using a Proxy connection, this is a string of format <HOST>:<PORT>.*
		| **Client_Certificate** : *Required. The path to the x509 client certificate that is used to connect to the Repository with TLS/SSL.*
		| **Certificate_Password** : *Optional. The password to encrypt and save on this machine. If blank, will clear any existing saved password for the specified certificate. Default is empty (ie, will clear existing password).*
		| **All_Users** : *Optional. If true, the specified password will be saved for all users on this machine. Otherwise, it will only be saved for the current user. Defaults to False.*
	"""
	All_Users = All_Users if not isinstance(All_Users,(list,tuple)) else ','.join([str(item) for item in All_Users])
	return CallDeadlineCommand("SaveCertificatePassword  %s %s %s %s" % (Connection_String,Client_Certificate,Certificate_Password,All_Users))

#----------------------------------------------------------------------
def SaveProxyServerInfo(ProxyServerInfo_Object):
	"""Save a specified ProxyServerInfo object to the Database.

	Params: Name: Discription
	------------------------------
		| **ProxyServerInfo_Object** : *JSON Object representing a ProxyServerInfo to save.*
	"""
	return CallDeadlineCommand("SaveProxyServerInfo  %s" % (ProxyServerInfo_Object))

#----------------------------------------------------------------------
def SaveProxyServerSettings(ProxyServerSettings_Ob):
	"""Save a specified ProxyServerSettings object to the Database.

	Params: Name: Discription
	------------------------------
		| **ProxyServerSettings_Ob** : *JSON Object representing a ProxyServerSettings to save.*
	"""
	return CallDeadlineCommand("SaveProxyServerSettings  %s" % (ProxyServerSettings_Ob))

#----------------------------------------------------------------------
def SavePulseInfo(PulseInfo_object):
	"""Saves a specified PulseInfo object.

	Params: Name: Discription
	------------------------------
		| **PulseInfo_object** : *The PulseInfo object*
	"""
	return CallDeadlineCommand("SavePulseInfo  %s" % (PulseInfo_object))

#----------------------------------------------------------------------
def SavePulseSettings(Pulse_Settings_object):
	"""Saves the pulse settings.

	Params: Name: Discription
	------------------------------
		| **Pulse_Settings_object** : *The pulse settings object*
	"""
	return CallDeadlineCommand("SavePulseSettings  %s" % (Pulse_Settings_object))

#----------------------------------------------------------------------
def IsInPath():
	""""""
	return CallDeadlineCommand("IsInPath")

#----------------------------------------------------------------------
def SelectDependencies(Initial_Dependencies=""):
	"""Allows you to select a list of dependencies, then prints them to stdout.

	Params: Name: Discription
	------------------------------
		| **Initial_Dependencies** : *A comma separated list of the initially selected dependencies (optional)*
	"""
	Initial_Dependencies = Initial_Dependencies if not isinstance(Initial_Dependencies,(list,tuple)) else ','.join([str(item) for item in Initial_Dependencies])
	res = CallDeadlineCommand("SelectDependencies  %s" % (Initial_Dependencies),hideWindow=False,raw_return=True).strip()
	return res

#----------------------------------------------------------------------
def SelectDirectory(Initial_Path=""):
	"""Opens a folder browser and prints out the result.

	Params: Name: Discription
	------------------------------
		| **Initial_Path** : *The path to the initial directory (optional)*
	"""
	res = CallDeadlineCommand("SelectDirectory  %s" % (Initial_Path),hideWindow=False).strip()
	if res == "Action was cancelled by user" or res == "":
		return None
	return res
#----------------------------------------------------------------------
def SelectFilenameLoad(Initial_Path="",Filter="Text Files (*.txt);;All Files (*.*)"):
	"""Opens a file load dialog and prints out the result.

	Params: Name: Discription
	------------------------------
		| **Initial_Path** : *The path to the initial filename (optional)*
		| **Filter** : *The filter string (optional) - an example filter would look like "Text Files (*.txt);;All Files (*.*)"*
	"""
	res = CallDeadlineCommand("SelectFilenameLoad  %s %s" % (Initial_Path,Filter),hideWindow=False).strip()
	if res == "Action was cancelled by user" or res == "":
		return None
	return res	

#----------------------------------------------------------------------
def SelectFilenameSave(Initial_Path="",Filter="Text Files (*.txt);;All Files (*.*)"):
	"""Opens a file save dialog and prints out the result.

	Params: Name: Discription
	------------------------------
		| **Initial_Path** : *The path to the initial filename (optional)*
		| **Filter** : *The filter string (optional) - an example filter would look like "Text Files (*.txt);;All Files (*.*)"*
	"""
	res = CallDeadlineCommand("SelectFilenameSave  %s %s" % (Initial_Path,Filter),hideWindow=False).strip()
	if res == "Action was cancelled by user" or res == "":
		return None
	return res	

#----------------------------------------------------------------------
def SelectLimitGroups(Initial_Limits=""):
	"""Allows you to select a list of limits, then prints them to stdout.

	Params: Name: Discription
	------------------------------
		| **Initial_Limits** : *A comma separated list of the initially selected limits (optional)*
	"""
	Initial_Limits = Initial_Limits if not isinstance(Initial_Limits,(list,tuple)) else ','.join([str(item) for item in Initial_Limits])
	res = CallDeadlineCommand("SelectLimitGroups  %s" % (Initial_Limits),hideWindow=False,raw_return=True).strip()
	return res

#----------------------------------------------------------------------
def SelectMachineList(Initial_Machines=""):
	"""Allows you to select a list of machines, then prints them to stdout.

	Params: Name: Discription
	------------------------------
		| **Initial_Machines** : *A comma separated list of the initially selected machines (optional)*
	"""
	Initial_Machines = Initial_Machines if not isinstance(Initial_Machines,(list,tuple)) else ','.join([str(item) for item in Initial_Machines])
	return CallDeadlineCommand("SelectMachineList  %s" % (Initial_Machines),hideWindow=False,raw_return=True).strip()

#----------------------------------------------------------------------
def SelectNetwork():
	"""Select the repository root from a dialog"""
	return CallDeadlineCommand("SelectNetwork",hideWindow=False,raw_return=True).strip()

#----------------------------------------------------------------------
def SelectRepository():
	"""Select the repository root from a dialog"""
	return CallDeadlineCommand("SelectRepository",hideWindow=False,raw_return=True).strip()

#----------------------------------------------------------------------
def SendEmail(to_Email,subject_Subject,message_Message,cc_Email,attach_Attachment):
	"""Sends an email.

	Params: Name: Discription
	------------------------------
		| **to_Email** : *TO email address*
		| **subject_Subject** : *The subject*
		| **message_Message** : *The message, or the path to the file that contains the message*
		| **cc_Email** : *CC email address (optional)*
		| **attach_Attachment** : *Attachment file (optional)*
	"""
	return CallDeadlineCommand("SendEmail  %s %s %s %s %s" % (to_Email,subject_Subject,message_Message,cc_Email,attach_Attachment))

#----------------------------------------------------------------------
def SendPopupMessage(Machine_Names,Message,Delete_Message_File):
	"""Sends a popup message to the Deadline running on the specified machine(s).

	Params: Name: Discription
	------------------------------
		| **Machine_Names** : *The machine name, or a list of machine names separated by commas.*
		| **Message** : *The message to send. This can be a string, or a path to a file that contains a message.*
		| **Delete_Message_File** : *(optional) If the message is stored in a file, specify 'true' to delete the file after.*
	"""
	Machine_Names = Machine_Names if not isinstance(Machine_Names,(list,tuple)) else ','.join([str(item) for item in Machine_Names])
	return CallDeadlineCommand("SendPopupMessage  %s %s %s" % (Machine_Names,Message,Delete_Message_File))

#----------------------------------------------------------------------
def SetAssetCrawlerEnabled(Name,Enabled):
	"""Dis/enable an Asset Crawler for a given Cloud Region.

	Params: Name: Discription
	------------------------------
		| **Name** : *Name of the Cloud Region*
		| **Enabled** : *True/False*
	"""
	return CallDeadlineCommand("SetAssetCrawlerEnabled  %s %s" % (Name,Enabled))

#----------------------------------------------------------------------
def SetAssetCrawlerSettings(Name,Hostname,Port,OS):
	"""Change the Asset Crawler settings for a Cloud Region.

	Params: Name: Discription
	------------------------------
		| **Name** : *Name of the Cloud Region*
		| **Hostname** : *Host name*
		| **Port** : *Port number*
		| **OS** : *Operating System (Windows, Linux, Mac OSX)*
	"""
	return CallDeadlineCommand("SetAssetCrawlerSettings  %s %s %s %s" % (Name,Hostname,Port,OS))

#----------------------------------------------------------------------
def SetAssetServerSetting(Name,Value):
	"""Sets the value of the specified Asset Server setting if it exists.

	Params: Name: Discription
	------------------------------
		| **Name** : *The name of the Asset Server setting.*
		| **Value** : *The value to apply to the AWS Portal setting.*
	"""
	return CallDeadlineCommand("SetAssetServerSetting  %s %s" % (Name,Value))

#----------------------------------------------------------------------
def SetAssetServerSetting(Name,Value):
	"""Sets the value of the specified Asset Server setting if it exists.

	Params: Name: Discription
	------------------------------
		| **Name** : *The name of the Asset Server setting.*
		| **Value** : *The value to apply to the AWS Portal setting.*
	"""
	return CallDeadlineCommand("SetAssetServerSetting  %s %s" % (Name,Value))

#----------------------------------------------------------------------
def SetAWSPortalSetting(Name,Value):
	"""Sets the value of the specified AWS Portal setting if it exists.

	Params: Name: Discription
	------------------------------
		| **Name** : *The name of the AWS Portal setting.*
		| **Value** : *The value to apply to the AWS Portal setting.*
	"""
	return CallDeadlineCommand("SetAWSPortalSetting  %s %s" % (Name,Value))

#----------------------------------------------------------------------
def SetRegionEnabled(Name,Enabled):
	"""Enables or Disables Balancer features for the given Cloud Region.

	Params: Name: Discription
	------------------------------
		| **Name** : *Name of the Cloud Region*
		| **Enabled** : *True/False*
	"""
	return CallDeadlineCommand("SetRegionEnabled  %s %s" % (Name,Enabled))

#----------------------------------------------------------------------
def SetRegionBudget(Name,Budget):
	"""Sets the budget of a Cloud Region.

	Params: Name: Discription
	------------------------------
		| **Name** : *Name of the Cloud Region*
		| **Budget** : *Total Budget Amount*
	"""
	return CallDeadlineCommand("SetRegionBudget  %s %s" % (Name,Budget))

#----------------------------------------------------------------------
def SetCloudRegionEnabled(Name,Enabled):
	"""Enables or Disables the given Cloud Region.

	Params: Name: Discription
	------------------------------
		| **Name** : *Name of the Cloud Region*
		| **Enabled** : *True/False*
	"""
	return CallDeadlineCommand("SetCloudRegionEnabled  %s %s" % (Name,Enabled))

#----------------------------------------------------------------------
def SetGroupsForSlave(Worker_Names,Group_Names):
	"""Sets the groups for a Worker.

	Params: Name: Discription
	------------------------------
		| **Worker_Names** : *The Worker name, or a list of Worker names separated by commas*
		| **Group_Names** : *The group name, or a list of group names separated by commas*
	"""
	Worker_Names = Worker_Names if not isinstance(Worker_Names,(list,tuple)) else ','.join([str(item) for item in Worker_Names])
	Group_Names = Group_Names if not isinstance(Group_Names,(list,tuple)) else ','.join([str(item) for item in Group_Names])
	return CallDeadlineCommand("SetGroupsForSlave  %s %s" % (Worker_Names,Group_Names))

#----------------------------------------------------------------------
def SetIniFileSetting(Key,Value,Set_For_All_Users):
	"""Sets the value for the given key in the deadline.ini configuration file.

	Params: Name: Discription
	------------------------------
		| **Key** : *The key to be set*
		| **Value** : *The value to set it to*
		| **Set_For_All_Users** : *(optional) True/False*
	"""
	Set_For_All_Users = Set_For_All_Users if not isinstance(Set_For_All_Users,(list,tuple)) else ','.join([str(item) for item in Set_For_All_Users])
	return CallDeadlineCommand("SetIniFileSetting  %s %s %s" % (Key,Value,Set_For_All_Users))

#----------------------------------------------------------------------
def SetInstallerVersion(Version):
	"""Sets the client installer version

	Params: Name: Discription
	------------------------------
		| **Version** : *The version string*
	"""
	return CallDeadlineCommand("SetInstallerVersion  %s" % (Version))

#----------------------------------------------------------------------
def SetJobExtraInfoKeyValue(Job_ID,Extra_Info_Key,Value):
	"""Sets the value of the specified key within the extra info dictionary.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
		| **Extra_Info_Key** : *The extra info key to get.*
		| **Value** : *The new value*
	"""
	return CallDeadlineCommand("SetJobExtraInfoKeyValue  %s %s %s" % (Job_ID,Extra_Info_Key,Value))

#----------------------------------------------------------------------
def SetJobFrameRange(Job_IDs,Frame_List,Chunk_Size):
	"""Modifies the job's frame range.

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The job ID, or a list of job IDs separated by commas*
		| **Frame_List** : *The new frame list*
		| **Chunk_Size** : *The new chunk size*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	return CallDeadlineCommand("SetJobFrameRange  %s %s %s" % (Job_IDs,Frame_List,Chunk_Size))

#----------------------------------------------------------------------
def SetJobMachineLimit(Job_IDs,Limit,Listed,Whitelist_Flag,Limit_Progress):
	"""Sets the machine limit for the job.

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The job ID, or a list of job IDs separated by commas*
		| **Limit** : *The new limit*
		| **Listed** : *The listed Workers*
		| **Whitelist_Flag** : *true/false*
		| **Limit_Progress** : *The limit progress (optional)*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	Limit_Progress = Limit_Progress if not isinstance(Limit_Progress,(list,tuple)) else ','.join([str(item) for item in Limit_Progress])
	return CallDeadlineCommand("SetJobMachineLimit  %s %s %s %s %s" % (Job_IDs,Limit,Listed,Whitelist_Flag,Limit_Progress))

#----------------------------------------------------------------------
def SetJobMachineLimitListedSlaves(Job_IDs,Workers):
	"""Sets the job's listed Workers.

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The job ID, or a list of job IDs separated by commas*
		| **Workers** : *The Workers, separated by commas*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	Workers = Workers if not isinstance(Workers,(list,tuple)) else ','.join([str(item) for item in Workers])
	return CallDeadlineCommand("SetJobMachineLimitListedSlaves  %s %s" % (Job_IDs,Workers))

#----------------------------------------------------------------------
def SetJobMachineLimitMaximum(Job_IDs,Limit):
	"""Sets the job's machine limit.

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The job ID, or a list of job IDs separated by commas*
		| **Limit** : *The machine limit*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	return CallDeadlineCommand("SetJobMachineLimitMaximum  %s %s" % (Job_IDs,Limit))

#----------------------------------------------------------------------
def SetJobMachineLimitReleaseProgress(Job_IDs,Limit_Progress):
	"""Sets the job's machine limit progress.

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The job ID, or a list of job IDs separated by commas*
		| **Limit_Progress** : *The limit progress*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	Limit_Progress = Limit_Progress if not isinstance(Limit_Progress,(list,tuple)) else ','.join([str(item) for item in Limit_Progress])
	return CallDeadlineCommand("SetJobMachineLimitReleaseProgress  %s %s" % (Job_IDs,Limit_Progress))

#----------------------------------------------------------------------
def SetJobMachineLimitWhiteListFlag(Job_IDs,Whitelist):
	"""Sets the job's whitelist flag.

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The job ID, or a list of job IDs separated by commas*
		| **Whitelist** : *True/False*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	return CallDeadlineCommand("SetJobMachineLimitWhiteListFlag  %s %s" % (Job_IDs,Whitelist))

#----------------------------------------------------------------------
def SetJobPluginInfoKeyValue(Job_ID,Plugin_Info_Key,Value):
	"""Sets the value of the specified key within the plugin info dictionary.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
		| **Plugin_Info_Key** : *The plugin info key to get.*
		| **Value** : *The new value*
	"""
	return CallDeadlineCommand("SetJobPluginInfoKeyValue  %s %s %s" % (Job_ID,Plugin_Info_Key,Value))

#----------------------------------------------------------------------
def SetJobSetting(Job_IDs,Job_Setting,Value):
	"""Sets the value of a setting for the job.

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The job ID, or a list of job IDs separated by commas*
		| **Job_Setting** : *The job setting*
		| **Value** : *The new value*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	return CallDeadlineCommand("SetJobSetting  %s %s %s" % (Job_IDs,Job_Setting,Value))

#----------------------------------------------------------------------
def SetLimitGroup(Limit_Name,Limit,Listed_Workers,Whitelist_Flag,Limit_Progress,Excluded_Workers):
	"""Modifies or creates the limit.

	Params: Name: Discription
	------------------------------
		| **Limit_Name** : *The limit name*
		| **Limit** : *The new limit*
		| **Listed_Workers** : *The listed Workers*
		| **Whitelist_Flag** : *true/false*
		| **Limit_Progress** : *The limit progress (optional)*
		| **Excluded_Workers** : *The excluded Workers (optional)*
	"""
	Listed_Workers = Listed_Workers if not isinstance(Listed_Workers,(list,tuple)) else ','.join([str(item) for item in Listed_Workers])
	Limit_Progress = Limit_Progress if not isinstance(Limit_Progress,(list,tuple)) else ','.join([str(item) for item in Limit_Progress])
	Excluded_Workers = Excluded_Workers if not isinstance(Excluded_Workers,(list,tuple)) else ','.join([str(item) for item in Excluded_Workers])
	return CallDeadlineCommand("SetLimitGroup  %s %s %s %s %s %s" % (Limit_Name,Limit,Listed_Workers,Whitelist_Flag,Limit_Progress,Excluded_Workers))

#----------------------------------------------------------------------
def SetLimitGroupListedSlaves(Limit_Names,Workers):
	"""Sets the limit's listed Workers.

	Params: Name: Discription
	------------------------------
		| **Limit_Names** : *The limit name, or a list of limit names separated by commas*
		| **Workers** : *The Workers, separated by commas*
	"""
	Limit_Names = Limit_Names if not isinstance(Limit_Names,(list,tuple)) else ','.join([str(item) for item in Limit_Names])
	Workers = Workers if not isinstance(Workers,(list,tuple)) else ','.join([str(item) for item in Workers])
	return CallDeadlineCommand("SetLimitGroupListedSlaves  %s %s" % (Limit_Names,Workers))

#----------------------------------------------------------------------
def SetLimitGroupMaximum(Limit_Names,Limit):
	"""Sets the limit's limit.

	Params: Name: Discription
	------------------------------
		| **Limit_Names** : *The limit name, or a list of limit names separated by commas*
		| **Limit** : *The machine limit*
	"""
	Limit_Names = Limit_Names if not isinstance(Limit_Names,(list,tuple)) else ','.join([str(item) for item in Limit_Names])
	return CallDeadlineCommand("SetLimitGroupMaximum  %s %s" % (Limit_Names,Limit))

#----------------------------------------------------------------------
def SetLimitGroupReleaseProgress(Limit_Names,Limit_Progress):
	"""Sets the limit's progress.

	Params: Name: Discription
	------------------------------
		| **Limit_Names** : *The limit name, or a list of limit names separated by commas*
		| **Limit_Progress** : *The limit progress*
	"""
	Limit_Names = Limit_Names if not isinstance(Limit_Names,(list,tuple)) else ','.join([str(item) for item in Limit_Names])
	Limit_Progress = Limit_Progress if not isinstance(Limit_Progress,(list,tuple)) else ','.join([str(item) for item in Limit_Progress])
	return CallDeadlineCommand("SetLimitGroupReleaseProgress  %s %s" % (Limit_Names,Limit_Progress))

#----------------------------------------------------------------------
def SetLimitGroupWhiteListFlag(Limit_Names,Whitelist):
	"""Sets the limit's whitelist flag.

	Params: Name: Discription
	------------------------------
		| **Limit_Names** : *The limit name, or a list of limit names separated by commas*
		| **Whitelist** : *True/False*
	"""
	Limit_Names = Limit_Names if not isinstance(Limit_Names,(list,tuple)) else ','.join([str(item) for item in Limit_Names])
	return CallDeadlineCommand("SetLimitGroupWhiteListFlag  %s %s" % (Limit_Names,Whitelist))

#----------------------------------------------------------------------
def SetMinimumDeadlineVersion(Installer_Minimum,Client_Minimum):
	"""Sets the minimum deadline version for the database.

	Params: Name: Discription
	------------------------------
		| **Installer_Minimum** : *The minimum version for the installer*
		| **Client_Minimum** : *The minimum version for the client*
	"""
	return CallDeadlineCommand("SetMinimumDeadlineVersion  %s %s" % (Installer_Minimum,Client_Minimum))

#----------------------------------------------------------------------
def SetPluginLimitGroups(Plugin_Name,Limit_Names):
	"""Set limit groups assigned to a Plugin.

	Params: Name: Discription
	------------------------------
		| **Plugin_Name** : *The name of the Plugin we want to modify.*
		| **Limit_Names** : *A comma-separated list of Limit names to apply to the Plugin. If any Limits contain spaces the list needs to be surrounded in double-quotes (").*
	"""
	Limit_Names = Limit_Names if not isinstance(Limit_Names,(list,tuple)) else ','.join([str(item) for item in Limit_Names])
	return CallDeadlineCommand("SetPluginLimitGroups  %s %s" % (Plugin_Name,Limit_Names))

#----------------------------------------------------------------------
def SetPoolsForSlave(Worker_Names,Pool_Names):
	"""Sets the pools for a Worker.

	Params: Name: Discription
	------------------------------
		| **Worker_Names** : *The Worker name, or a list of Worker names separated by commas*
		| **Pool_Names** : *The pool name, or a list of pool names separated by commas*
	"""
	Worker_Names = Worker_Names if not isinstance(Worker_Names,(list,tuple)) else ','.join([str(item) for item in Worker_Names])
	Pool_Names = Pool_Names if not isinstance(Pool_Names,(list,tuple)) else ','.join([str(item) for item in Pool_Names])
	return CallDeadlineCommand("SetPoolsForSlave  %s %s" % (Worker_Names,Pool_Names))

#----------------------------------------------------------------------
def SetPromptTimeOut():
	"""If set to a value other than -1, this is the number of milliseconds before Deadline Command will automatically exit while in interactive mode."""
	return CallDeadlineCommand("SetPromptTimeOut")

#----------------------------------------------------------------------
def SetRegionBudget(Name,Budget):
	"""Sets the budget of a Cloud Region.

	Params: Name: Discription
	------------------------------
		| **Name** : *Name of the Cloud Region*
		| **Budget** : *Total Budget Amount*
	"""
	return CallDeadlineCommand("SetRegionBudget  %s %s" % (Name,Budget))

#----------------------------------------------------------------------
def SetRegionEnabled(Name,Enabled):
	"""Enables or Disables Balancer features for the given Cloud Region.

	Params: Name: Discription
	------------------------------
		| **Name** : *Name of the Cloud Region*
		| **Enabled** : *True/False*
	"""
	return CallDeadlineCommand("SetRegionEnabled  %s %s" % (Name,Enabled))

#----------------------------------------------------------------------
def SetRegistryKeyValue(Key_Name,Value_Name,Value_Data):
	"""Adds and/or sets the specified value for the specified registry key.

	Params: Name: Discription
	------------------------------
		| **Key_Name** : *The name of the registry key*
		| **Value_Name** : *The name of the value to set/add*
		| **Value_Data** : *The string data to set the value to*
	"""
	return CallDeadlineCommand("SetRegistryKeyValue  %s %s %s" % (Key_Name,Value_Name,Value_Data))

#----------------------------------------------------------------------
def SetRepositoryOption(Repository_Option,Value):
	"""Sets the value of the provided Repository Option if it exists and is exposed.

	Params: Name: Discription
	------------------------------
		| **Repository_Option** : *The name of the Repository Option we want to set*
		| **Value** : *The value to set for the Repository Option*
	"""
	return CallDeadlineCommand("SetRepositoryOption  %s %s" % (Repository_Option,Value))

#----------------------------------------------------------------------
def SetSlaveExtraInfoKeyValue(Worker_Name,Extra_Info_Key,Value):
	"""Sets the value of the specified key within the extra info dictionary.

	Params: Name: Discription
	------------------------------
		| **Worker_Name** : *The name of the Worker.*
		| **Extra_Info_Key** : *The extra info key to get.*
		| **Value** : *The new value*
	"""
	return CallDeadlineCommand("SetSlaveExtraInfoKeyValue  %s %s %s" % (Worker_Name,Extra_Info_Key,Value))

#----------------------------------------------------------------------
def SetSlaveSetting(Worker_Names,Worker_Setting,Value):
	"""Sets the value of a setting for the Worker.

	Params: Name: Discription
	------------------------------
		| **Worker_Names** : *The Worker name, or a list of Worker names separated by commas*
		| **Worker_Setting** : *The Worker setting*
		| **Value** : *The new value*
	"""
	Worker_Names = Worker_Names if not isinstance(Worker_Names,(list,tuple)) else ','.join([str(item) for item in Worker_Names])
	return CallDeadlineCommand("SetSlaveSetting  %s %s %s" % (Worker_Names,Worker_Setting,Value))

#----------------------------------------------------------------------
def SetUser(User_Name,Email,Machine_Name,Notify_By_Email,Notify_By_Popup,User_Group):
	"""Modifies or creates the user.

	Params: Name: Discription
	------------------------------
		| **User_Name** : *The user name*
		| **Email** : *Their email address*
		| **Machine_Name** : *Their machine name*
		| **Notify_By_Email** : *If they want email notifications (true/false)*
		| **Notify_By_Popup** : *If they want popup notifications (true/false)*
		| **User_Group** : *Optional. The user group (or list of groups separated by commas) to add the user to. By default, the user is already part of the Everyone group.*
	"""
	return CallDeadlineCommand("SetUser  %s %s %s %s %s %s" % (User_Name,Email,Machine_Name,Notify_By_Email,Notify_By_Popup,User_Group))

#----------------------------------------------------------------------
def SetUserForUserGroup(User_Names,User_Group_Names):
	"""Removes a user from the user group.

	Params: Name: Discription
	------------------------------
		| **User_Names** : *The user name, or a list of user names separated by commas*
		| **User_Group_Names** : *The user group name, or a list of user group names separated by commas*
	"""
	User_Names = User_Names if not isinstance(User_Names,(list,tuple)) else ','.join([str(item) for item in User_Names])
	User_Group_Names = User_Group_Names if not isinstance(User_Group_Names,(list,tuple)) else ','.join([str(item) for item in User_Group_Names])
	return CallDeadlineCommand("SetUserForUserGroup  %s %s" % (User_Names,User_Group_Names))


def ShowMessageBox(title="Message", message="This is The Message", buttons=[]):
	"""Displays a simple dialog box and prints out the button selected.

	Params: Name: Discription
	------------------------------
		| **title_Title** : *The title*
		| **message_Message** : *The message, or the path to the file that contains the message*
		| **buttons_Buttons** : *A comma separated list of buttons (optional)*
	"""
	command = 'ShowMessageBox -title "%s" -message "%s"' % (title, message)
	if len(buttons):
		buttons = ",".join([str(bnt) for bnt in buttons])
		command += ' -buttons %s' % buttons
	return CallDeadlineCommand(command,hideWindow=False)

#----------------------------------------------------------------------
def ShowUserDialog(title="Message", message="This is The Message", buttons=[]):
	"""Displays a simple dialog box and prints out the button selected.

	Params: Name: Discription
	------------------------------
		| **title_Title** : *The title*
		| **message_Message** : *The message*
		| **buttons_Buttons** : *A comma separated list of buttons*
	"""
	command = 'ShowUserDialog -title "%s" -message "%s"' % (title, message)
	if len(buttons):
		buttons = ",".join([str(bnt) for bnt in buttons])
		command += ' -buttons %s' % buttons
		
	return CallDeadlineCommand(command,hideWindow=False,raw_return=True)

#----------------------------------------------------------------------
def SlaveExists(Worker_Name):
	"""Displays 'true' if the Worker exists, 'false' if it does not.

	Params: Name: Discription
	------------------------------
		| **Worker_Name** : *The Worker name*
	"""
	return CallDeadlineCommand("SlaveExists  %s" % (Worker_Name))

#----------------------------------------------------------------------
def Slaves():
	"""Displays all the Worker names."""
	return CallDeadlineCommand("Slaves")

#----------------------------------------------------------------------
def StartLauncherService():
	"""Starts the Deadline Launcher Service if it is running."""
	return CallDeadlineCommand("StartLauncherService")

#----------------------------------------------------------------------
def StartProcess(Filename):
	"""Starts the program or program associated with the file.

	Params: Name: Discription
	------------------------------
		| **Filename** : *The path to a given application or file*
	"""
	return CallDeadlineCommand("StartProcess  %s" % (Filename))

#----------------------------------------------------------------------
def StopLauncherService():
	"""Stops the Deadline Launcher Service if it is running."""
	return CallDeadlineCommand("StopLauncherService")

#----------------------------------------------------------------------
def SubmitBackgroundJob(notify,Job_Files):
	"""Submits a job as a background process.

	Params: Name: Discription
	------------------------------
		| **notify** : *This flag displays a notification window after the jobs have been submitted*
		| **Job_Files** : *The list of job files*
	"""
	Job_Files = Job_Files if not isinstance(Job_Files,(list,tuple)) else ','.join([str(item) for item in Job_Files])
	return CallDeadlineCommand("SubmitBackgroundJob  %s %s" % (notify,Job_Files))

##----------------------------------------------------------------------
#def SubmitCommandLineJob(executable_Value,arguments_Value,frames_Value,chunksize_Value,pool_Value,group_Value,priority_Value,name_Value,department_Value,initialstatus_Value,prop_Key=Value):
	#"""Submits a generic command line job to Deadline. The <STARTFRAME> and <ENDFRAME> strings in the command line arguments will be replaced with the actual start and end frame for each task. The <QUOTE> string in the command line arguments will be replaced with a '"' character.

	#Params: Name: Discription
	#------------------------------
		#| **executable_Value** : *Required: The command line executable.*
		#| **arguments_Value** : *Optional: The command line arguments.*
		#| **frames_Value** : *Required: The frame range to render.*
		#| **chunksize_Value** : *Optional: The task chunk size.*
		#| **pool_Value** : *Optional: The pool the job belongs to.*
		#| **group_Value** : *Optional: The group the job belongs to.*
		#| **priority_Value** : *Optional: The job priority (0 is the lowest).*
		#| **name_Value** : *Optional: The job name.*
		#| **department_Value** : *Optional: The job department.*
		#| **initialstatus_Value** : *Optional: The job's initial state (Active/Suspended).*
		#| **prop_Key=Value** : *Optional: Extra submission properties in the form Key=Value.*
	#"""
	#return CallDeadlineCommand("SubmitCommandLineJob  %s %s %s %s %s %s %s %s %s %s %s" % (executable_Value,arguments_Value,frames_Value,chunksize_Value,pool_Value,group_Value,priority_Value,name_Value,department_Value,initialstatus_Value,prop_Key=Value))
#----------------------------------------------------------------------
def Submit_Deadline_Job(job_info_file, job_settings_file):
	exacutble = get_DeadLine_Exacutble()
	command   = " ".join([exacutble, job_info_file, job_settings_file])
	try:
		submit = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	except:
		temp_file = get_Temp_Result_File()
		with file(temp_file, "w") as f:
			submit = subprocess.Popen(command, stdin=f, stdout=subprocess.PIPE, shell=True)
	out  = submit.communicate()[0]
	lines = out.splitlines()
	Result = False
	jobid  = None
	for line in lines:
		data = line.split("=")
		if len(data) == 2:
			if data[0] == "Result":
				if data[1] == "Success":
					Result = True
				else:
					Result = False
			elif data[0] == "JobID":
				jobid = data[1]
	return Result, jobid, out
#----------------------------------------------------------------------
def SubmitJobAndNotify(deleteFiles,Job_Files):
	"""Submits a job and notifies upon completion.

	Params: Name: Discription
	------------------------------
		| **deleteFiles** : *Specify this flag to delete local files after submission*
		| **Job_Files** : *The job files*
	"""
	deleteFiles = deleteFiles if not isinstance(deleteFiles,(list,tuple)) else ','.join([str(item) for item in deleteFiles])
	Job_Files = Job_Files if not isinstance(Job_Files,(list,tuple)) else ','.join([str(item) for item in Job_Files])
	return CallDeadlineCommand("SubmitJobAndNotify  %s %s" % (deleteFiles,Job_Files))

#----------------------------------------------------------------------
def SubmitMultipleJobs(dependent,notify,Job_Files):
	"""Submits multiple jobs at once.

	Params: Name: Discription
	------------------------------
		| **dependent** : *This flag makes each job in the list of jobs specified dependent on the previous job. This is shorthand for specifying -dependsonprevious for each job being submitted*
		| **notify** : *This flag displays a notification window after the jobs have been submitted*
		| **Job_Files** : *This flag must precede each list of files for each individual job being submitted. You can also add the -dependsonprevious flag to make a single job dependent on the previous job*
	"""
	Job_Files = Job_Files if not isinstance(Job_Files,(list,tuple)) else ','.join([str(item) for item in Job_Files])
	return CallDeadlineCommand("SubmitMultipleJobs  %s %s %s" % (dependent,notify,Job_Files))

#----------------------------------------------------------------------
def SuspendJob(Job_IDs):
	"""Suspends the job.

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The job ID, or a list of job IDs separated by commas*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	return CallDeadlineCommand("SuspendJob  %s" % (Job_IDs))

#----------------------------------------------------------------------
def SuspendJobNonRenderingTasks(Job_IDs):
	"""Suspends the tasks that are not rendering for the job.

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The job ID, or a list of job IDs separated by commas*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	return CallDeadlineCommand("SuspendJobNonRenderingTasks  %s" % (Job_IDs))

#----------------------------------------------------------------------
def SuspendJobTask(Job_ID,Task_ID):
	"""Suspends the specified task for the job.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
		| **Task_ID** : *The task ID*
	"""
	return CallDeadlineCommand("SuspendJobTask  %s %s" % (Job_ID,Task_ID))

#----------------------------------------------------------------------
def SuspendJobTasks(Job_ID,Task_IDs):
	"""Suspends the specified tasks for the job.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
		| **Task_IDs** : *The comma separated list of task IDs*
	"""
	Task_IDs = Task_IDs if not isinstance(Task_IDs,(list,tuple)) else ','.join([str(item) for item in Task_IDs])
	return CallDeadlineCommand("SuspendJobTasks  %s %s" % (Job_ID,Task_IDs))

#----------------------------------------------------------------------
def TestProtectedConfig():
	"""Runs a test to make sure that a Repository's protected configuration file will work properly on this machine."""
	return CallDeadlineCommand("TestProtectedConfig")

#----------------------------------------------------------------------
def UndeleteJob(Job_IDs):
	"""Undeletes the job(s).

	Params: Name: Discription
	------------------------------
		| **Job_IDs** : *The deleted job ID, or a list of deleted job IDs separated by commas*
	"""
	Job_IDs = Job_IDs if not isinstance(Job_IDs,(list,tuple)) else ','.join([str(item) for item in Job_IDs])
	return CallDeadlineCommand("UndeleteJob  %s" % (Job_IDs))

#----------------------------------------------------------------------
def UninstallLauncherService():
	"""Stops and uninstalls the Deadline Launcher Service."""
	return CallDeadlineCommand("UninstallLauncherService")

#----------------------------------------------------------------------
def UpdateDatabaseSettings(Repository,DbType,Host,Name,Port,AltPort,SSL,Authenticate,Username,Password,Replica_Set,Split_DB):
	"""Updates the given repository's connection.ini file with the given database settings. This function does not perform any validation on the provided settings. Note that any incorrect settings could prevent some or all Deadline Clients pointing to this Repository from connecting to the Database

	Params: Name: Discription
	------------------------------
		| **Repository** : *The path to the repository root*
		| **DbType** : *The database type (currently only MongoDB)*
		| **Host** : *The host name or IP address of the database machine*
		| **Name** : *The database name*
		| **Port** : *The database port*
		| **AltPort** : *The alternate database port (not currently used)*
		| **SSL** : *If SSL should be used to connect (not currently used)*
		| **Authenticate** : *If authentication is required*
		| **Username** : *The username*
		| **Password** : *The password*
		| **Replica_Set** : *The Replica set name*
		| **Split_DB** : *If Database should be split (by default, it is disabled)*
	"""
	return CallDeadlineCommand("UpdateDatabaseSettings  %s %s %s %s %s %s %s %s %s %s %s %s" % (Repository,DbType,Host,Name,Port,AltPort,SSL,Authenticate,Username,Password,Replica_Set,Split_DB))

#----------------------------------------------------------------------
def UpdateEnvironmentSettings(Environment):
	"""Updates the Environment in the database.

	Params: Name: Discription
	------------------------------
		| **Environment** : *The path to the environment file*
	"""
	return CallDeadlineCommand("UpdateEnvironmentSettings  %s" % (Environment))

#----------------------------------------------------------------------
def UpdateJobSubmissionDate(Job_ID):
	"""Updates the job submission date for the specified job to be the current date.

	Params: Name: Discription
	------------------------------
		| **Job_ID** : *The job ID*
	"""
	return CallDeadlineCommand("UpdateJobSubmissionDate  %s" % (Job_ID))

#----------------------------------------------------------------------
def UpdatePathVariable():
	"""Appends the Deadline bin folder to the PATH environment variable"""
	return CallDeadlineCommand("UpdatePathVariable")

#----------------------------------------------------------------------
def UpdateScriptMenus(Script_Menu_File):
	"""Updates the script menu configuration based on the given file.

	Params: Name: Discription
	------------------------------
		| **Script_Menu_File** : *The file containing the script menu configuration*
	"""
	return CallDeadlineCommand("UpdateScriptMenus  %s" % (Script_Menu_File))

#----------------------------------------------------------------------
def UpgradePluginSettings():
	"""Used by installer to upgrade the plugins without overriding user configured settings."""
	return CallDeadlineCommand("UpgradePluginSettings")

#----------------------------------------------------------------------
def Users():
	"""Display all the user names."""
	return CallDeadlineCommand("Users")

#----------------------------------------------------------------------
def Version():
	"""Gets the Deadline Version"""
	return CallDeadlineCommand("Version")


#----------------------------------------------------------------------
def Submit_Deadline_Job(job_info_file, job_settings_file):
	command = " ".join(["SubmitJobToDeadline", job_info_file, job_settings_file])
	return CallDeadlineCommand(command, hideWindow=True)