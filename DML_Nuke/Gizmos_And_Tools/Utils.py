import DML_Tools
import nuke
import os
DML_PYQT = DML_Tools.DML_PYQT

#----------------------------------------------------------------------
def Find_First_Existing_Folder_Path(folder):
	""""""
	folder = folder.replace("/", "\\")
	
	if not os.path.exists(folder):
		while not os.path.exists(folder):
			if os.path.dirname(folder) == folder:
				folder = nuke.script_directory()
				break
			else:
				folder = os.path.dirname(folder)
	return folder
#----------------------------------------------------------------------
def Get_Folder_Dialog(label="Output Folder", UseNativeDialog=False, folder="", parent=None):
	""""""
	options = DML_PYQT.QFileDialog.DontResolveSymlinks | DML_PYQT.QFileDialog.ShowDirsOnly
	if UseNativeDialog:
		options |= DML_PYQT.QFileDialog.DontUseNativeDialog
	if folder == "":
		folder = nuke.script_directory()
		
	folder = Find_First_Existing_Folder_Path(folder)
	
	folder_Picked = DML_PYQT.QFileDialog.getExistingDirectory(parent,label,folder, options)
	if folder_Picked:
		return folder_Picked.replace("\\","/")
	else:
		return False