

import nuke
from ..Base_Nodes import DML_Nuke_Object


#----------------------------------------------------------------------
def get_extrapolation(self):
	"""Controls how to set the left slope of the first point and the right slope of the last point"""
	return self.nuke_node.extrapolation
#----------------------------------------------------------------------
def set_extrapolation(self,val):
	"""Controls how to set the left slope of the first point and the right slope of the last point"""
	self.nuke_node.extrapolation = val
	
#----------------------------------------------------------------------
def get_interpolation(self):
	"""Used to calculate all the slopes except for the left slope of the first key and the right slope of the last key"""
	return self.nuke_node.interpolation
#----------------------------------------------------------------------
def set_interpolation(self,val):
	"""Used to calculate all the slopes except for the left slope of the first key and the right slope of the last key"""
	self.nuke_node.interpolation = val
	
#----------------------------------------------------------------------
def get_la(self):
	"""The left 'bicubic' value"""
	return self.nuke_node.la
#----------------------------------------------------------------------
def set_la(self,val):
	"""The left 'bicubic' value"""
	self.nuke_node.la = val

#----------------------------------------------------------------------
def get_lslope(self):
	"""The derivative to the left of the point"""
	return self.nuke_node.lslope
#----------------------------------------------------------------------
def set_lslope(self,val):
	"""The derivative to the left of the point"""
	self.nuke_node.lslope = val

#----------------------------------------------------------------------
def get_ra(self):
	"""The right 'bicubic' value"""
	return self.nuke_node.ra
#----------------------------------------------------------------------
def set_ra(self,val):
	"""The right 'bicubic' value"""
	self.nuke_node.ra = val

#----------------------------------------------------------------------
def get_rslope(self):
	"""The derivative to the right of the point"""
	return self.nuke_node.rslope
#----------------------------------------------------------------------
def set_rslope(self,val):
	"""The derivative to the right of the point"""
	self.nuke_node.rslope = val

#----------------------------------------------------------------------
def get_selected(self):
	"""True if the point is selected in the curve editor"""
	return self.nuke_node.selected
#----------------------------------------------------------------------
def set_selected(self,val):
	"""True if the point is selected in the curve editor"""
	self.nuke_node.selected = val

#----------------------------------------------------------------------
def get_x(self):
	"""The horizontal position of the point"""
	return self.nuke_node.x
#----------------------------------------------------------------------
def set_x(self,val):
	"""The horizontal position of the point"""
	self.nuke_node.x = val

#----------------------------------------------------------------------
def get_y(self):
	"""The vertical position of the point"""
	return self.nuke_node.y
#----------------------------------------------------------------------
def set_y(self,val):
	"""The vertical position of the point"""
	self.nuke_node.y = val
	
################################################################################
class AnimationKey(DML_Nuke_Object):
	#----------------------------------------------------------------------
	extrapolation = property(fget=get_extrapolation, fset=set_extrapolation,doc="controls how to set the left slope of the first point and the right slope of\nthe last point. Notice that this can be set differently on the first and last\npoints, and is also remembered on all internal points so if end points are\ndeleted old behavior is restored).\n- constant: the left slope of the first point, and the right slope of the last\n			point, are set to zero.\n\n- linear: (and all other values): The left slope of the first point is set\n		  equal to it's right slope (calculated by the interpolation).\n\nthe right slope of the last point is set equal to it's left slope.\nif there is only one point both slopes are set to zero.")
	#----------------------------------------------------------------------
	interpolation = property(fget=get_interpolation, fset=set_interpolation, doc="Used to calculate all the slopes except for the left slope of the first key and the right slope of the last key.\nLegal values are:\n- USER_SET_SLOPE: If this bit is on, the slopes are fixed by\n				  the user and interpolation and extrapolation are ignored.\n\n- CONSTANT: The value of the curve is equal to the y of the point to the left.\n\n- LINEAR: slopes point directly at the next key.\n\n- SMOOTH: same as CATMULL_ROM but the slopes are clamped so that the\n		  convex-hull property is preserved\n		  (meaning no part of the curve extends vertically outside the range of the keys on each side of it).\n		  This is the default.\n\n- CATMULL_ROM: the slope at key n is set to the slope between the control\n			   points n-1 and n+1. This is used by lots of software.\n\n- cubic: the slope is calculated to the only cubic interpolation which makes\n		 the first and second derivatives continuous. This type of\n		 interpolation was very popular in older animation software.  A\n		 different cubic interpolation is figured out for each set of adjacent\n		 points with the CUBIC type.\n\n- for the smooth, CATMULL_ROM, and CUBIC interpolations, the first and last\n  key have slopes calculated so that the second derivative is zero at them.")
	#----------------------------------------------------------------------
	la = property(fget=get_la, fset=set_la, doc="The left 'bicubic' value.\nThis represents the horizontal\nposition of the left bezier handle end, where 1.0 means 1/3 of the\ndistance to the previous point. If both handles for a span are 1.0\nthen the horizontal interpolation is linear and thus the vertical\ninterpolation a cubic function.  The legal values are 0 to\n3. Setting outside of this range will produce undefined results.")
	#----------------------------------------------------------------------
	lslope = property(fget=get_lslope, fset=set_lslope, doc="The derivative to the left of the point")
	#----------------------------------------------------------------------
	ra = property(fget=get_ra, fset=set_ra, doc="The right 'bicubic' value")
	#----------------------------------------------------------------------
	rslope = property(fget=get_rslope, fset=set_rslope, doc="The derivative to the right of the point")	
	#----------------------------------------------------------------------
	selected = property(fget=get_selected, fset=set_selected, doc="True if the point is selected in the curve editor")
	#----------------------------------------------------------------------
	x = property(fget=get_x, fset=set_x, doc="The horizontal position of the point")
	#----------------------------------------------------------------------
	y = property(fget=get_y, fset=set_y, doc="The vertical position of the point")