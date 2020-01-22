import os
import maya.api.OpenMaya
new_om = maya.api.OpenMaya

import maya.OpenMaya

old_om = maya.OpenMaya


########################################################################
class Maya_API_Callback_ID(object):
	'''Wrapper class to handle cleaning up of MCallbackIds from registered MMessage'''
	#---------------------------------------------------------------------------------
	def __init__(self, callbackId):
		self.callbackId = callbackId
	#---------------------------------------------------------------------------------
	def __del__(self):
		#print("Call back Being Deleted")
		try:
			new_om.MMessage.removeCallback(self.callbackId)
		except:
			try:
				old_om.MMessage.removeCallback(self.callbackId)
			except:
				pass
	#---------------------------------------------------------------------------------
	def __repr__(self):
		return 'Maya_API_Callback_ID(%r)'% self.callbackId.__hash__()
	
	#---------------------------------------------------------------------------------
	def hash_id(self):
		return self.callbackId.__hash__()