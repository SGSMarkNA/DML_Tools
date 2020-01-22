import maya.cmds as cmds
from .. import Dependency_Node 
from ...General_Utils import flatten
	
	
########################################################################
class Bookmark_Type(object):
	""" Camera View bookmark types, which can be: 0. 3D bookmark; 1. 2D Pan/Zoom bookmark.  """
	D3 = 0
	D2 = 1
		
		
    
	
########################################################################
class Camera_View(Dependency_Node):
	"""Dependency node to represent a camera's view.
	cmds.cameraView( edit=True, addBookmark=True, animate=False, camera Name=True, name="", removeBookmark=True, setCamera=True, setView=True, bookmarkType=0,)
	"""
	MAYA_NODE_TYPE_RELATION = "cameraView"
	CREATE_COMMAND          = cmds.cameraView
	BOOKMARK_TYPE           = Bookmark_Type
	#----------------------------------------------------------------------
	def addBookmark(self,camera=None,bookmarkType=0):
		"""Associate this view with the camera specified or the camera in the active model panel"""
		self.CREATE_COMMAND( self, edit=True, camera=camera,addBookmark=True,bookmarkType=bookmarkType)
		
	#----------------------------------------------------------------------
	def removeBookmark(self,camera):
		"""Remove the association of this view with the camera specified or the camera in the active model panel."""
		cmds.cameraView( self, edit=True, camera=camera, removeBookmark=True)

	#----------------------------------------------------------------------
	def setCamera(self,camera=None,animate=True):
		""" Set this view into a camera specified by the camera flag or the camera in the active model panel """
		cmds.cameraView( self, edit=True, camera=camera, setCamera=True,animate=animate)
		
	#----------------------------------------------------------------------
	def setView(self,camera=None,animate=True):
		"""Set the camera view to match a camera specified or the active model panel."""
		cmds.cameraView( self, edit=True, camera=camera, setView=True, animate=animate)
		