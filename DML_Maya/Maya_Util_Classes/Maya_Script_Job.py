
import maya.cmds as cmds
########################################################################
class Maya_Script_Job(object):
	'''Wrapper class to handle cleaning up of scriptjob'''
	#---------------------------------------------------------------------------------
	def __init__(self, *args,**kwargs):
		if len(args) == 1 and isinstance(args[0],int):
			self.callbackId = args[0]
		else:
			self.callbackId = cmds.scriptJob(**kwargs)
		self._get_job_value()
	#---------------------------------------------------------------------------------
	def _get_job_value(self):
		jobs = cmds.scriptJob( listJobs=True)
		if not jobs == None:
			for job in cmds.scriptJob( listJobs=True):
				if int(job.split(":")[0]) == self.callbackId:
					self.job_value = job.split(":")[-1].strip()
					break
	#---------------------------------------------------------------------------------
	def __del__(self):
		import maya.cmds as cmds
		if not self.callbackId == None:
			if cmds.scriptJob(exists=self.callbackId):
				try:
					cmds.scriptJob( kill=self.callbackId, force=True)
				except:
					pass
	#---------------------------------------------------------------------------------
	def __repr__(self):
		return self.job_value