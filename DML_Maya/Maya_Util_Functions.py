import os,sys,logging,inspect
import maya.cmds as cmds
import maya.mel as mel
from . import General_Utils
from PySide2.QtWidgets import qApp
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

if False:
	from PySide2.QtWidgets import QApplication
	isinstance(qApp,QApplication)

#---------------------------------------------------------------------------------
def getCurrentFPS():
	'''
	returns the current frames per second as a number, rather than a useless string
	'''
	fpsDict = {"game":15.0, "film":24.0, "pal":25.0, "ntsc":30.0, "show":48.0, "palf":50.0, "ntscf":60.0}
	return fpsDict[cmds.currentUnit(q=True, fullName=True, time=True)]

#---------------------------------------------------------------------------------
def inspectFunctionSource(value):
	'''
	This is a neat little wrapper over the mel "whatIs" and Pythons inspect
	module that finds the given functions source filePath, either Mel or Python
	and opens the original file in the default program.
	Great for developers
	Supports all Mel functions, and Python Class / functions
	'''
	path=None
	#sourceType=None
	#Inspect for MEL
	log.debug('inspecting given command: %s' % value)
	try:
		path=mel.eval('whatIs("%s")' % value)
		if path and not path=="Command":
			path=path.split("in: ")[-1]
		elif path=="Command":
			cmds.warning('%s : is a Command not a script' % value)
			return False
	except Exception as error:
		log.info(error)
	#Inspect for Python
	if not path or not os.path.exists(path):
		log.info('This is not a known Mel command, inspecting Python libs for : %s' % value)
		try:
			log.debug('value :  %s' % value)
			log.debug('value isString : ', isinstance(value, str))
			log.debug('value callable: ', callable(value))
			log.debug('value is module : ', inspect.ismodule(value))
			log.debug('value is method : ', inspect.ismethod(value))
			if isinstance(value, str):
			#if not callable(value):
				value=eval(value)
			path=inspect.getsourcefile(value)
			if path:
				#sourceType='python'
				log.info('path : %s' % path)
		except Exception as error:
			log.exception(error)

	#Open the file with the default editor
	#FIXME: If Python and you're a dev then the .py file may be set to open in the default
	#Python runtime/editor and won't open as expected. Need to look at this.
	if path and os.path.exists(path):
		log.debug('NormPath : %s' % os.path.normpath(path))
		os.startfile(os.path.normpath(path))
		return True
	else:
		log.warning('No valid path or functions found matches selection')
		return False

#---------------------------------------------------------------------------------
def getScriptEditorSelection():
	'''
	this is a hack to bypass an issue with getting the data back from the
	ScriptEditorHistory scroll. We need to copy the selected text to the
	clipboard then pull it back afterwards.
	'''
	control=mel.eval("$v=$gLastFocusedCommandControl")
	executer=mel.eval("$v=$gLastFocusedCommandExecuter")
	reporter=mel.eval("$v=$gLastFocusedCommandReporter")
	func=""
	if control==executer:
		func=cmds.cmdScrollFieldExecuter(control, q=True, selectedText=True)
	elif control == reporter:
		cmds.cmdScrollFieldReporter(reporter, e=True, copySelection=True)
		func=qApp.clipboard().text()
	log.info('command caught: %s ' % func)
	return func

#---------------------------------------------------------------------------------
def get_Mel_Variable(name):
	if not name.startswith("$"):
		name = "$"+name

	typ = mel.eval('whatIs "%s"' % name)
	if not typ == 'Unknown':

		typ = typ.split()[0]

		if typ.startswith("string"):
			if typ.endswith("[]"):
				res = mel.eval('$AW_G_SA_Var = %s;' % name)
			else:
				res = mel.eval('$AW_G_S_Var = %s;' % name)
		elif typ.startswith("int"):
			if typ.endswith("[]"):
				res = mel.eval('$AW_G_IA_Var = %s;' % name)
			else:
				res = mel.eval('$AW_G_I_Var = %s;' % name)
		elif typ.startswith("float"):
			if typ.endswith("[]"):
				res = mel.eval('$AW_G_FA_Var = %s;' % name)
			else:
				res = mel.eval('$AW_G_F_Var = %s;' % name)
		elif typ.startswith("vector"):
			if typ.endswith("[]"):
				res = mel.eval('$AW_G_VA_Var = %s;' % name)
			else:
				res = mel.eval('$AW_G_V_Var = %s;' % name)
		elif typ.startswith("matrix"):
			res = mel.eval('$AW_G_MX_Var = %s;' % name)
		return res
	else:
		return None