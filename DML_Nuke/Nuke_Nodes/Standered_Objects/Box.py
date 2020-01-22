
import nuke
from ..Base_Nodes import DML_Nuke_Object
from ...Decorators.Node_Wraper_Manager import nuke_Node_Return_Wrapper,node_Return_Wrapper,nuke_Object_Return_Wrapper,knob_Return_Wrapper
################################################################################
class Box(DML_Nuke_Object):

	#def __init__(self,x=0,y=0,r=0,t=0):
		#nuke_node = nuke.Box(int(x), int(y), int(r), int(t))
		#super(Box,self).__init__(nuke_node)
		#if False:
			#isinstance(self._nukeNode,nuke.Box)
	def set(self, x, y, r, t):
		"""set all values at once."""
		self.nuke_object.set(x, y, r, t)

	def move(self, dx, dy):
		"""Move all the sides and thus the entire box by the given deltas."""
		self.nuke_object.move(dx, dy)

	@property
	def isConstant(self):
		"""if box is 1x1 in both directions, False otherwise."""
		return self.nuke_object.isConstant()

	def clampY(self,y):
		"""Return y restricted to pointing at a pixel in the box."""
		return self.nuke_object.clampY(y)

	def clampX(self,x):
		"""Return x restricted to pointing at a pixel in the box."""
		return self.nuke_object.clampX(x)

	def pad(self, dx, dy, dr, dt):
		"""pad(dx, dy, dr, dt) -> None. Move all the sides and thus the entire box by the given deltas."""
		self.nuke_object.pad(dx, dy, dr, dt)

	def intersect(self,*args):
		"""Intersect with the given edges."""
		set_check=False

		if len(*args)==4:
			x,y,r,t = args[0], args[1], args[2], args[3]
			set_check=True

		elif len(*args)==1 and isinstance(args[0], Box):
			x,y,r,t = args[0].x, args[0].y, args[0].r, args[0].t
			set_check=True

		elif len(*args)==1 and isinstance(args[0], BackdropNode):
			x,y,r,t = args[0]._box.x, args[0]._box.y, args[0]._box.r, args[0]._box.t
			set_check=True

		elif len(*args)==1 and isinstance(args[0], nuke.Box):
			x,y,r,t = args[0].x(), args[0].y(), args[0].r(), args[0].t()
			set_check=True

		if set_check:
			self.nuke_object.intersect(x, y, r, t)

	def clear(self):
		"""clear() -> None.Set to is_constant()."""
		self.nuke_object.clear()

	def merge(self,*args):
		"""merge(x, y, r, t) -> None.Merge with the given edges."""
		set_check=False

		if len(*args)==4:
			x,y,r,t = args[0], args[1], args[2], args[3]
			set_check=True

		elif len(*args)==1 and isinstance(args[0], Box):
			x,y,r,t = args[0].x, args[0].y, args[0].r, args[0].t
			set_check=True

		elif len(*args)==1 and hasattr(args[0], "_is_dml_object") and args[0].Class == "BackdropNode":
			x,y,r,t = args[0]._box.x, args[0]._box.y, args[0]._box.r, args[0]._box.t
			set_check=True

		elif len(*args)==1 and isinstance(args[0], nuke.Box):
			x,y,r,t = args[0].x(), args[0].y(), args[0].r(), args[0].t()
			set_check=True

		if set_check:
			self.nuke_object.merge(x,y,r,t)

	def getR(self):
		"""r() -> intReturn right edge."""
		return self.nuke_object.r()

	def setR(self,value):
		return self.nuke_object.setR(value)
	r = property(getR,setR)

	def getT(self):
		"""t() -> intReturn top edge."""
		return self.nuke_object.t()

	def setT(self,value):
		return self.nuke_object.setT(value)
	t = property(getT,setT)

	def getW(self):
		"""w() -> intReturn width."""
		return self.nuke_object.w()

	def setW(self,value):
		return self.nuke_object.setW(value)
	w = property(getW,setW)

	def getY(self):
		"""y() -> intReturn bottom edge."""
		return self.nuke_object.y()

	def setY(self,value):
		return self.nuke_object.setY(value)
	y = property(getY,setY)

	def getX(self):
		"""x() -> intReturn left edge."""
		return self.nuke_object.x()

	def setX(self,value):
		return self.nuke_object.setX(value)
	x = property(getX,setX)

	def getH(self):
		"""h() -> intReturn height."""
		return self.nuke_object.h()

	def setH(self,value):
		return self.nuke_object.setH(value)
	h = property(getH,setH)

	@property
	def centerY(self):
		return self.nuke_object.centerY()
	@property
	def centerX(self):
		return self.nuke_object.centerX()

	#----------------------------------------------------------------------
	@nuke_Node_Return_Wrapper
	def Is_Node_Inside(self,node):
		""""""
		if node.xpos() > self.x and node.xpos() + node.screenWidth() < self.r and node.ypos() > self.t and node.ypos() + node.screenHeight() < self.y:
			return True
		return False
