try:
	import subprocess_original as subprocess
except:
	import subprocess

import os
import datetime
import json
import tempfile

import string
invalid_chars = list(string.punctuation.replace("_", "") + string.whitespace)
string_digits = list(string.digits)
del string

_Json_Output       = False
_NoJson_Output     = False
_PrettyJson_Output = False
_Force_Raw_Output  = False
_cashed_deadline_command    = None
_cashed_deadline_executable = None

#################################################################################
class Dict_Attribute_Keys(object):
	def __init__(self, data):
		self._orig_data = data
		for key, value in data.iteritems():
			key = "_".join(key.split())
			key = "".join([k for k in list(key) if not k in invalid_chars])
			key = str("n_" + key) if key[0] in string_digits else key
			if isinstance(value, dict):
				self.__dict__[key] = Dict_Attribute_Keys(value)
			elif isinstance(value, list):
				new_val = []
				for val in value:
					if isinstance(val, dict):
						val = Dict_Attribute_Keys(val)
					new_val.append(val)
				self.__dict__[key] = new_val
			else:
				self.__dict__[key] = value
	def __repr__(self):
		return self.__class__.__name__ + "(%r)" % self._orig_data

def get_DeadLine_Command():
	global _cashed_deadline_command

	if _cashed_deadline_command == None:
		deadline_bin = ""
		deadline_exe = "deadlinecommand.exe"
		try:
			deadline_bin = os.environ['DEADLINE_PATH']
		except KeyError:
			if os.path.exists( "/Program Files/Thinkbox/Deadline10/bin" ):
				deadline_bin = os.path.realpath( "/Program Files/Thinkbox/Deadline10/bin" )
			else:
				raise LookupError("The DEADLINE_PATH env key is not set and /Program Files/Thinkbox/Deadline10/bin Does Not Exist")

		deadline_command = os.path.join(deadline_bin,deadline_exe)
		if not os.path.exists(deadline_command):
			raise OSError("The Deadline Executable '{}' Does not exist".format(deadline_command))
		_cashed_deadline_command = deadline_command

	return _cashed_deadline_command

def get_DeadLine_Exacutble():
	global _cashed_deadline_executable
	if _cashed_deadline_executable == None:
		_cashed_deadline_executable = '"%s"' % get_DeadLine_Command()
	return _cashed_deadline_executable

def get_Temp_Result_File():
	temp_folder = os.environ['TEMP']
	temp_file   = "dead_line_output.txt"
	temp_path   = os.path.join(temp_folder,temp_file)
	return temp_path


def CallDeadlineCommand(command,hideWindow=True,no_Json=False,as_PrittyJson=False,raw_return=False):
	global _Json_Output, _NoJson_Output, _PrettyJson_Output, _Force_Raw_Output

	startupinfo = None
	
	if hideWindow and os.name == 'nt':
		# Python 2.6 has subprocess.STARTF_USESHOWWINDOW, and Python 2.7 has subprocess._subprocess.STARTF_USESHOWWINDOW, so check for both.
		if hasattr( subprocess, '_subprocess' ) and hasattr( subprocess._subprocess, 'STARTF_USESHOWWINDOW' ):
			startupinfo = subprocess.STARTUPINFO()
			startupinfo.dwFlags |= subprocess._subprocess.STARTF_USESHOWWINDOW
		elif hasattr( subprocess, 'STARTF_USESHOWWINDOW' ):
			startupinfo = subprocess.STARTUPINFO()
			startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW


	deadline_command   = get_DeadLine_Command()
	deadline_exacutble = get_DeadLine_Exacutble()
	
	if not command.startswith("SubmitJobToDeadline"):
		if not raw_return or _Force_Raw_Output:
			if no_Json or _NoJson_Output:
				command = "NoJson " + command
			elif as_PrittyJson or _PrettyJson_Output:
				command = "PrettyJson " + command
			else:
				command = "Json " + command
	

		if not command.startswith("-"):
			command = "-" + command
	else:
		command = command.replace("SubmitJobToDeadline","")

	command   = deadline_exacutble + " " + command

	environment = {}
	for key in os.environ.keys():
		environment[key] = str(os.environ[key])

	# Need to set the PATH, cuz windows seems to load DLLs from the PATH earlier that cwd....
	if os.name == 'nt':
		deadlineCommandDir = os.path.dirname( deadline_command )
		if not deadlineCommandDir == "" :
			environment['PATH'] = deadlineCommandDir + os.pathsep + os.environ['PATH']

	try:
		proc = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=startupinfo, env=environment)
		#submit = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	except:
		temp_file = get_Temp_Result_File()
		with file(temp_file, "w") as f:
			proc = subprocess.Popen(command, stdin=f, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=startupinfo, env=environment)
			#submit = subprocess.Popen(command, stdin=f, stdout=subprocess.PIPE, shell=True)

	output, errors = proc.communicate()
	json_load_check = False
	if raw_return or _Force_Raw_Output:
		return output
	else:
		if no_Json or _NoJson_Output:
			return output
		else:
			try:
				data = json.loads(output)
				json_load_check = True
			except ValueError:
				json_load_check = False

		if not json_load_check:
			data = dict(ok=True,result=dict(lines=[]))
			res = output.splitlines()
			if _Force_Raw_Output:
				return res
			if len(res):
				if res[0].startswith("Error:"):
					data['ok'] = False
				else:
					for line in res:
						if len(line):
							data["result"]["lines"].append(line)
							if "=" in line:
								key, value =  line.split("=", 1)
								data["result"][key]=value.strip()
							elif ":" in line:
								key, value =  line.split(":", 1)
								data["result"][key]=value.strip()
			else:
				data['ok'] = False
		data["orig_output"] = output
		data  = Dict_Attribute_Keys(data)
		if isinstance(data.result,list):
			if len(data.result)==1:
				data.result = data.result[0]
		return data


def Select_MachineList(items=None):
	"""Allows you to select a list of machines, then prints them to stdout"""
	cmd = "SelectMachineList"
	if items is not None and not items == "":
		cmd = cmd + ' %s' % items
	res = CallDeadlineCommand(cmd)
	if len(res):
		res = res[0]
		if res == "Action was cancelled by user":
			res = False
	else:
		res = False
	return res
def Select_LimitGroups(items=None):
	"""Allows you to select a list of limit, then prints them to stdout"""
	cmd = "SelectLimitGroups"
	if items is not None and not items == "":
		cmd = cmd + ' %s' % items
	res = CallDeadlineCommand(cmd)
	if len(res):
		res = res[0]
		if res == "Action was cancelled by user":
			res = False
	else:
		res = False
	return res

def Select_Directory(path=None):
	"""Opens a folder browser and prints out the result"""
	cmd = "SelectDirectory"
	if path is not None:
		cmd = cmd + ' %s' % path
	res = CallDeadlineCommand(cmd)
	if len(res):
		res = res[0]
	else:
		res = ''
	res = res.replace("\\", "/")
	return res
def Select_Dependencies(items=None):
	"""Allows you to select a list of dependencies,then prints them to stdout"""
	cmd = "SelectDependencies"
	if items is not None and not items == "":
		cmd = cmd + ' %s' % items
	res = CallDeadlineCommand(cmd)
	if len(res):
		res = res[0]
		if  res == "Action was cancelled by user":
			res = False
	else:
		res = False
	return res
def Select_FilenameLoad(path=None, filters=None):
	"""Opens a file load dialog and prints out the result"""
	cmd = "SelectFilenameLoad"
	if path is not None:
		cmd = cmd + ' %s' % path
	else:
		cmd = cmd + ' ""' % path
	if filters is not None:
		cmd = cmd + ' %s' % filters
	res = CallDeadlineCommand(cmd)
	if len(res):
		res = res[0]
	else:
		res = ''
	res = res.replace("\\", "/")
	return res

def Select_FilenameSave(path=None, filters=None):
	"""Opens a file save dialog and prints out the result"""
	cmd = "SelectFilenameSave"
	if path is not None:
		cmd = cmd + ' %s' % path
	else:
		cmd = cmd + ' ""' % path
	if filters is not None:
		cmd = cmd + ' %s' % filters
	res = CallDeadlineCommand(cmd)
	if len(res):
		res = res[0]
	else:
		res = ''
	res = res.replace("\\", "/")
	return res

