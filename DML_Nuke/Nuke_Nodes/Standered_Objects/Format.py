import nuke
from ..Base_Nodes import DML_Nuke_Object

################################################################################
class Format(DML_Nuke_Object):
	#----------------------------------------------------------------------
	def setPixelAspect(self,aspectRatio):
		"""self.setPixelAspect(aspectRatio) -> None  Set a new pixel aspect ratio for this format. The aspectRatio parameter is the new ratio, found by dividing the desired pixel width by the desired pixel height."""
		return self.nuke_object.setPixelAspect(aspectRatio)
	#----------------------------------------------------------------------
	def height(self):
		"""self.height() -> int  Return the height of image file in pixels."""
		return self.nuke_object.height()
	#----------------------------------------------------------------------
	def scaled(self):
		"""scaled(sx, sy, tx, ty) -> Format  Scale and translate this format by sx, sy, tx and ty.  @param sx: Scale factor in X.@param sy: Scale factor in Y.@param tx: Offset factor in X.@param ty: Offset factor in Y.@return: Format."""
		return self.nuke_object.scaled()
	#----------------------------------------------------------------------
	def setWidth(self,newWidth):
		"""self.setWidth(newWidth) -> None  Set the width of image file in pixels.newWidth is the new width for the image; it should be a positive integer."""
		return self.nuke_object.setWidth(newWidth)
	#----------------------------------------------------------------------
	def width(self):
		"""self.width() -> int  Return the width of image file in pixels."""
		return self.nuke_object.width()
	#----------------------------------------------------------------------
	def add(self,name):
		"""self.add(name) -> None  Add this instance to a list of "named" formats. The name parameter is the name of the list to add the format to."""
		return self.nuke_object.add(name)
	#----------------------------------------------------------------------
	def setName(self,name):
		"""self.setName(name) -> None  Set name of this format. The name parameter is the new name for the format."""
		return self.nuke_object.setName(name)
	#----------------------------------------------------------------------
	def setT(self,newT):
		"""self.setT(newT) -> None  Set the top edge of image file in pixels. newY is the new top edge for the image; it should be a positive integer."""
		return self.nuke_object.setT(newT)
	#----------------------------------------------------------------------
	def setR(self,newR):
		"""self.setR(newR) -> None  Set the right edge of image file in pixels. newR is the new right edge for the image; it should be a positive integer."""
		return self.nuke_object.setR(newR)
	#----------------------------------------------------------------------
	def fromUV(self):
		"""self.fromUV(u, v) -> [x, y]  Transform a UV coordinate in the range 0-1 into the format's XY range. Returns a list containing the x and y coordinates.  @param u: The U coordinate. @param v: The V coordinate. @return: [x, y]"""
		return self.nuke_object.fromUV()
	#----------------------------------------------------------------------
	def setX(self,newX):
		"""self.setX(newX) -> None  Set the left edge of image file in pixels. newX is the new left edge for the  image; it should be a positive integer."""
		return self.nuke_object.setX(newX)
	#----------------------------------------------------------------------
	def setY(self,newY):
		"""self.setY(newY) -> None  Set the bottom edge of image file in pixels. newY is the new bottom edge for the image; it should be a positive integer."""
		return self.nuke_object.setY(newY)
	#----------------------------------------------------------------------
	def setHeight(self,newHeight):
		"""self.setHeight(newHeight) -> None  Set the height of image file in pixels. newHeight is the new height for the image; it should be a positive integer."""
		return self.nuke_object.setHeight(newHeight)
	#----------------------------------------------------------------------
	def pixelAspect(self):
		"""self.pixelAspect() -> float  Returns the pixel aspect ratio (pixel width divided by pixel height) for this format."""
		return self.nuke_object.pixelAspect()
	#----------------------------------------------------------------------
	def name(self):
		"""self.name() -> string  Returns the user-visible name of the format."""
		return self.nuke_object.name()
	#----------------------------------------------------------------------
	def r(self):
		"""self.r() -> int  Return the right edge of image file in pixels."""
		return self.nuke_object.r()
	#----------------------------------------------------------------------
	def t(self):
		"""self.t() -> int  Return the top edge of image file in pixels."""
		return self.nuke_object.t()
	#----------------------------------------------------------------------
	def toUV(self):
		"""self.toUV(x, y) -> (u, v)  Back-transform an XY coordinate in the format's space into UV space.  @param x: The X coordinate. @param y: The Y coordinate. @return: [u, v]."""
		return self.nuke_object.toUV()
	#----------------------------------------------------------------------
	def y(self):
		"""self.y() -> int  Return the bottom edge of image file in pixels."""
		return self.nuke_object.y()
	#----------------------------------------------------------------------
	def x(self):
		"""self.x() -> int  Return the left edge of image file in pixels."""
		return self.nuke_object.x()
