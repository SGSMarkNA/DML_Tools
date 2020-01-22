

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class ViewManip(UI_Object.UI):
	"""
	Mel access to the view cube manipulator.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.viewManip(**kwargs)
			super(ViewManip, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.viewManip(name, exists=True):
				super(ViewManip, self).__init__(name)
			else:
				name = cmds.viewManip(name, **kwargs)
				super(ViewManip, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def bottomLeft(self):
		"""
		
				Positions the cube in the bottom left of the screen.
				
		"""
		return self.query(bottomLeft=True)
	#----------------------------------------------------------------------
	@property
	def bottomRight(self):
		"""
		
				Positions the cube in the bottom right of the screen.
				
		"""
		return self.query(bottomRight=True)
	#----------------------------------------------------------------------
	@property
	def compassAngle(self):
		"""
		
				Angle (in degrees) to rotate the compass.
				
		"""
		return self.query(compassAngle=True)
	#----------------------------------------------------------------------
	@property
	def dragSnap(self):
		"""
		
				Enable snapping of orbit direction to view cube part directions during drag operation.
				
		"""
		return self.query(dragSnap=True)
	#----------------------------------------------------------------------
	@property
	def drawCompass(self):
		"""
		
				Show compass below the view cube.
				
		"""
		return self.query(drawCompass=True)
	#----------------------------------------------------------------------
	@property
	def frontParameters(self):
		"""
		
				Parameter string for the front position
				
		"""
		return self.query(frontParameters=True)
	#----------------------------------------------------------------------
	@property
	def goDefault(self):
		"""
		
				Go to the default position
				
		"""
		return self.query(goDefault=True)
	#----------------------------------------------------------------------
	@property
	def goHome(self):
		"""
		
				Go to the home position
				
		"""
		return self.query(goHome=True)
	#----------------------------------------------------------------------
	@property
	def homeParameters(self):
		"""
		
				Parameter string for the home position
				
		"""
		return self.query(homeParameters=True)
	#----------------------------------------------------------------------
	@property
	def minOpacity(self):
		"""
		
				Opacity level (in range [0,1]) on view cube when the cursor is away from it (it is fully opaque when the cursor is in the view cube area).
				
		"""
		return self.query(minOpacity=True)
	#----------------------------------------------------------------------
	@property
	def namespace(self):
		"""
		
				Namespace to use for the object
				
		"""
		return self.query(namespace=True)
	#----------------------------------------------------------------------
	@property
	def postCommand(self):
		"""
		
				Command to run after moving
				
		"""
		return self.query(postCommand=True)
	#----------------------------------------------------------------------
	@property
	def preCommand(self):
		"""
		
				Command to run before moving
				
		"""
		return self.query(preCommand=True)
	#----------------------------------------------------------------------
	@property
	def preserveSceneUp(self):
		"""
		
				Specify whether the scene "up" direction should be preserved
				
		"""
		return self.query(preserveSceneUp=True)
	#----------------------------------------------------------------------
	@property
	def resetFront(self):
		"""
		
				Reset the front position
				
		"""
		return self.query(resetFront=True)
	#----------------------------------------------------------------------
	@property
	def resetHome(self):
		"""
		
				Reset the home position
				
		"""
		return self.query(resetHome=True)
	#----------------------------------------------------------------------
	@property
	def selectionLockParameters(self):
		"""
		
				String containing the selection lock parameters
				
		"""
		return self.query(selectionLockParameters=True)
	#----------------------------------------------------------------------
	@property
	def size(self):
		"""
		
				Set or query the size of the View Cube, which can be one of "tiny",
				"small", "normal", "large" or "auto". When set to "auto" the View Cube
				will be automatically set to the size most appropriate for the view.
				
		"""
		return self.query(size=True)
	#----------------------------------------------------------------------
	@property
	def topLeft(self):
		"""
		
				Positions the cube in the top left of the screen.
				
		"""
		return self.query(topLeft=True)
	#----------------------------------------------------------------------
	@property
	def topRight(self):
		"""
		
				Positions the cube in the top right of the screen.
				
		"""
		return self.query(topRight=True)
	#----------------------------------------------------------------------
	@property
	def visible(self):
		"""
		
				Shows/hides the view manip.
				
		"""
		return self.query(visible=True)
	#----------------------------------------------------------------------
	@property
	def zoomToFitScene(self):
		"""
		
				Zoom the camera during animated transitions to fit the scene object in the viewport.
				
		"""
		return self.query(zoomToFitScene=True)