import clr

from System.Collections.Specialized import *
from System.IO import *
from System.Text import *

from Deadline.Scripting import *
from DeadlineUI.Controls.Scripting.DeadlineScriptDialog import DeadlineScriptDialog

# Job Options UI
import imp
import os
import json
imp.load_source( "JobOptionsUI", os.path.join( RepositoryUtils.GetRepositoryPath( "submission/Common/Main", True ), "JobOptionsUI.py" ) )
import JobOptionsUI

########################################################################
## Globals
########################################################################
scriptDialog = None
settings = None
count = 0
jobOptions_dialog = None

########################################################################
## Main Function Called By Deadline
########################################################################
def __main__( *args ):
    global scriptDialog
    global settings
    global CommandBox
    global jobOptions_dialog
    
    scriptDialog = DeadlineScriptDialog()
    scriptDialog.SetTitle( "Submit Command Script Job To Deadline" )
    scriptDialog.SetIcon( scriptDialog.GetIcon( 'CommandScript' ) )

    jobOptions_dialog = JobOptionsUI.JobOptionsDialog( parentAppName = "CommandScriptMonitor" )
    
    scriptDialog.AddScriptControl( "JobOptionsDialog", jobOptions_dialog, "" )
    
    scriptDialog.AddGrid()
    scriptDialog.AddControlToGrid( "Separator3", "SeparatorControl", "Command Script Options", 0, 0, colSpan=2 )
    scriptDialog.AddControlToGrid("Label1", "LabelControl", "json File.", 1,0, "A tooltip", False)
    scriptDialog.AddSelectionControlToGrid( "FileBox", "FileBrowserControl", "", "json Files (*.json);;All Files (*.*)", 1, 1 )
    #scriptDialog.AddControlToGrid( "Separator3", "SeparatorControl", "Command Script Options", 0, 0, colSpan=6 )

    #scriptDialog.AddControlToGrid("CommandsLabel","LabelControl","Commands to Execute: 0", 1, 0, "Specify a list of commands to execute, one commmand per line.", colSpan=6)
    
    #InsertFileButton = scriptDialog.AddControlToGrid("InsertFileButton","ButtonControl","Insert File Path", 2, 0, "Insert a file path at the current cursor location.", False)
    #InsertFileButton.ValueModified.connect(InsertFilePressed)
    
    #InsertFolderButton = scriptDialog.AddControlToGrid("InsertFolderButton","ButtonControl","Insert Folder Path", 2, 1, "Insert a folder path at the current cursor location.", False)
    #InsertFolderButton.ValueModified.connect(InsertFolderPressed)
    
    #scriptDialog.AddHorizontalSpacerToGrid("HSpacer1", 2, 2 )
    
    #LoadButton = scriptDialog.AddControlToGrid("LoadButton","ButtonControl","Load", row=2, column=3, tooltip="Load a list of commands from a file.", expand=False )
    #LoadButton.ValueModified.connect(LoadPressed)
    
    #SaveButton = scriptDialog.AddControlToGrid("SaveButton","ButtonControl","Save", row=2, column=4, tooltip="Save the current list of commands to a file.", expand=False )
    #SaveButton.ValueModified.connect(SavePressed)
    
    #ClearButton=scriptDialog.AddControlToGrid("ClearButton","ButtonControl","Clear", row=2, column=5, tooltip="Clear the current list of commands.", expand=False)
    #ClearButton.ValueModified.connect(ClearPressed)
    scriptDialog.EndGrid()
    #scriptDialog.AddGrid()
    #CommandBox=scriptDialog.AddControlToGrid("CommandsBox","MultiLineTextControl","", 0, 0, colSpan=4)
    #CommandBox.ValueModified.connect(CommandsChanged)

    #scriptDialog.AddControlToGrid("StartupLabel","LabelControl","Startup Directory",1, 0, "The directory where each command will startup (optional).", False)
    #scriptDialog.AddSelectionControlToGrid("StartupBox","FolderBrowserControl","","",1, 1, colSpan=3)

    #scriptDialog.AddControlToGrid( "ChunkSizeLabel", "LabelControl", "Commands Per Task", 2, 0, "This is the number of commands that will be rendered at a time for each job task.", False )
    #scriptDialog.AddRangeControlToGrid( "ChunkSizeBox", "RangeControl", 1, 1, 1000000, 0, 1, 2, 1, expand=False)
    #shellExecute = scriptDialog.AddSelectionControlToGrid( "ShellExecuteBox", "CheckBoxControl", False, "Execute In Shell", 2, 2, "If enabled, the specified command(s) will be executed through the current shell." )
    #shellExecute.ValueModified.connect(ShellExecuteButtonPressed)
    #scriptDialog.AddComboControlToGrid( "ShellToUseBox", "ComboControl", "default", ["default","bash","csh","ksh","sh","tcsh","zsh","cmd"], 2, 3 )
    #scriptDialog.EndGrid()

    scriptDialog.AddGrid()
    scriptDialog.AddHorizontalSpacerToGrid( "HSpacer2", 0, 0 )

    submitButton = scriptDialog.AddControlToGrid( "SubmitButton", "ButtonControl", "Submit", 0, 1, expand=False )
    submitButton.ValueModified.connect(SubmitButtonPressed)

    closeButton = scriptDialog.AddControlToGrid( "CloseButton", "ButtonControl", "Close", 0, 2, expand=False )
    closeButton.ValueModified.connect(scriptDialog.closeEvent)
    closeButton.ValueModified.connect(jobOptions_dialog.closeEvent)

    scriptDialog.EndGrid()
    
    #settings = ( "ChunkSizeBox","StartupBox","ShellExecuteBox","ShellToUseBox" )
    #scriptDialog.LoadSettings( GetSettingsFilename(), settings )
    #scriptDialog.EnabledStickySaving( settings, GetSettingsFilename() )
    
    #CommandsChanged( None )
    #ShellExecuteButtonPressed( None )

    scriptDialog.ShowDialog( True )
    
def GetSettingsFilename():
    return Path.Combine( ClientUtils.GetUsersSettingsDirectory(), "CommandScriptSettings.ini" )
    
def SubmitButtonPressed( *args ):
    global scriptDialog
    global count
    global jobOptions_dialog
    
    errors = []
        
    json_file_path = scriptDialog.GetValue( "FileBox" ).strip()
    
    if not (os.path.exists(json_file_path)):
        errors.append( "The Json File Does Not Exist!" )    
    else:
        with file(json_file_path,"r") as fp:
            build_data = json.load(fp)
        frame_count = len(build_data["builds"])

    if len( errors ) > 0:
        scriptDialog.ShowMessageBox( "The following errors were encountered:\n\n%s\n\nPlease resolve these issues and submit again.\n" % ( "\n\n".join( errors ) ), "Errors" )
        return
    
    jobOptions = jobOptions_dialog.GetJobOptionsValues()

    # Create job info file.
    jobInfoFilename = Path.Combine( ClientUtils.GetDeadlineTempPath(), "cmd_Gimp_PSD_job_info.job" )
    writer = StreamWriter( jobInfoFilename, False, Encoding.Unicode )
    writer.WriteLine( "Plugin=GimpPSD" )

    for option, value in jobOptions.iteritems():
        writer.WriteLine( "%s=%s" % ( option, value ) )
    
    writer.WriteLine( "Frames=0-" + str(frame_count-1))
    writer.WriteLine( "ChunkSize=1" )
    writer.WriteLine( "EnvironmentKeyValue0=JsonFilePath=%s" % json_file_path )
    
    writer.Close()
    
    # Create plugin info file.
    pluginInfoFilename = Path.Combine( ClientUtils.GetDeadlineTempPath(), "cmd_Gimp_PSD_plugin_info.job" )
    writer = StreamWriter( pluginInfoFilename, False, Encoding.Unicode )
    writer.Close()
        
    # Setup the command line arguments.
    arguments = StringCollection()
    
    arguments.Add( jobInfoFilename )
    arguments.Add( pluginInfoFilename )
    #arguments.Add( commandsFilename )
    
    # Now submit the job.
    results = ClientUtils.ExecuteCommandAndGetOutput( arguments )
    scriptDialog.ShowMessageBox( results, "Submission Results" )
