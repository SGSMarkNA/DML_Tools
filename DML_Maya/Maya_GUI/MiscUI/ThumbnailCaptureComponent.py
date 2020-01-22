

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class ThumbnailCaptureComponent(UI_Object.UI):
	"""
	This command is used to generate a thumbnail/playblast sequence from the scene.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.thumbnailCaptureComponent(**kwargs)
			super(ThumbnailCaptureComponent, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.thumbnailCaptureComponent(name, exists=True):
				super(ThumbnailCaptureComponent, self).__init__(name)
			else:
				name = cmds.thumbnailCaptureComponent(name, **kwargs)
				super(ThumbnailCaptureComponent, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def capturedFrameCount(self):
		"""
		
				Query only. Return the number of frames that have been captured.
				
		"""
		return self.query(capturedFrameCount=True)
	#----------------------------------------------------------------------
	@property
	def endFrame(self):
		"""
		
				Set the end captured frame. Only valid when the -c/capture flag is set.
				If -sf/startFrame is set and not -ef/endFrame, or if endFrame is smaller than startFrame, endFrame will be automatically set to startFrame.
				
		"""
		return self.query(endFrame=True)
	#----------------------------------------------------------------------
	@property
	def isSessionOpened(self):
		"""
		
				Returns true if a thumbnail/playblast capture session is currently running (already opened and still not cancelled/saved).
				
		"""
		return self.query(isSessionOpened=True)
	#----------------------------------------------------------------------
	@property
	def launchedFromOptionsBox(self):
		"""
		
				Returns true if the thumbnail capture component was launched through the options dialog box, else false.
				
		"""
		return self.query(launchedFromOptionsBox=True)
	#----------------------------------------------------------------------
	@property
	def previewPath(self):
		"""
		
				Returns the generated preview path (the first frame of generated sequence resized to 100x100 px).
				
		"""
		return self.query(previewPath=True)
	#----------------------------------------------------------------------
	@property
	def startFrame(self):
		"""
		
				Set the start captured frame. Only valid when -c/capture flag is set.
				
		"""
		return self.query(startFrame=True)