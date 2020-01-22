import maya.cmds as cmds
from ..Abstract_Nodes import Dag_Node
from ...General_Utils import flatten
	
########################################################################
class Joint_Orient_Options(object):
	xyz = "xyz"
	yzx = "yzx"
	zxy = "zxy"
	zyx = "zyx"
	yxz = "yxz"
	xzy = "xzy"
########################################################################
class Secondary_Axis_Orient_Options(object):
	xup = "xup"
	xdown = "xdown"
	yup = "yup"
	ydown = "ydown"
	zup = "zup"
	zdown = "zdown"
	
########################################################################
class Edit_Flags(object):
	#----------------------------------------------------------------------
	def __init__(self):
		""""""
		self.children = False
		self.assumePreferredAngles = False
		
########################################################################
class Joint(Dag_Node):			
	MAYA_NODE_TYPE_RELATION = "joint"
	CREATE_COMMAND          = cmds.joint
	secondary_axis_orient_Options = Secondary_Axis_Orient_Options
	joint_orient_options = Joint_Orient_Options
	
	#----------------------------------------------------------------------
	def _edit(self,**kwargs):
		""""""
		kwargs["edit"]=True
		cmds.joint(self,**kwargs)
	#----------------------------------------------------------------------
	def _query(self,**kwargs):
		""""""
		kwargs["query"]=True
		cmds.joint(self,**kwargs)
	#----------------------------------------------------------------------
	def get_absolute(self):
		"""The joint center position is in absolute world coordinates.
		(This is the default.)
		"""
		return self._query(absolute=True)
	#----------------------------------------------------------------------
	def set_absolute(self,value):
		"""The joint center position is in absolute world coordinates.
		(This is the default.)
		"""
		self._edit(absolute=value)
	#----------------------------------------------------------------------
	absolute = property(fget=get_absolute,fset=set_absolute)

	#----------------------------------------------------------------------
	def get_angleX(self):
		"""Set the x-axis angle. When queried, this flag
		returns a float.
		"""
		return self._query(angleX=True)
	#----------------------------------------------------------------------
	def set_angleX(self,value):
		"""Set the x-axis angle. When queried, this flag
		returns a float.
		"""
		self._edit(angleX=value)
	#----------------------------------------------------------------------
	angleX = property(fget=get_angleX,fset=set_angleX)

	#----------------------------------------------------------------------
	def get_angleY(self):
		"""Set the y-axis angle. When queried, this flag
		returns a float.
		"""
		return self._query(angleY=True)
	#----------------------------------------------------------------------
	def set_angleY(self,value):
		"""Set the y-axis angle. When queried, this flag
		returns a float.
		"""
		self._edit(angleY=value)
	#----------------------------------------------------------------------
	angleY = property(fget=get_angleY,fset=set_angleY)

	#----------------------------------------------------------------------
	def get_angleZ(self):
		"""Set the z-axis angle. When queried, this flag
		returns a float.
		"""
		return self._query(angleZ=True)
	#----------------------------------------------------------------------
	def set_angleZ(self,value):
		"""Set the z-axis angle. When queried, this flag
		returns a float.
		"""
		self._edit(angleZ=value)
	#----------------------------------------------------------------------
	angleZ = property(fget=get_angleZ,fset=set_angleZ)

	#----------------------------------------------------------------------
	def get_degreeOfFreedom(self):
		"""Specifies the degrees of freedom for the IK.
		Valid strings consist of non-duplicate letters from x,
		y, and z. The letters in the string indicate what
		rotations are to be used by IK. The order a letter
		appear in the string does not matter. Examples are x,
		yz, xyz. When queried, this flag returns a string.
		Modifying dof will change the locking state of the
		corresponding rotation attributes. The rule is: if an
		rotation is turned into a dof, it will be unlocked if
		it is currently locked. When it is turned into a
		non-dof, it will be locked if it is not currently
		locked.
		"""
		return self._query(degreeOfFreedom=True)
	#----------------------------------------------------------------------
	def set_degreeOfFreedom(self,value):
		"""Specifies the degrees of freedom for the IK.
		Valid strings consist of non-duplicate letters from x,
		y, and z. The letters in the string indicate what
		rotations are to be used by IK. The order a letter
		appear in the string does not matter. Examples are x,
		yz, xyz. When queried, this flag returns a string.
		Modifying dof will change the locking state of the
		corresponding rotation attributes. The rule is: if an
		rotation is turned into a dof, it will be unlocked if
		it is currently locked. When it is turned into a
		non-dof, it will be locked if it is not currently
		locked.
		"""
		self._edit(degreeOfFreedom=value)
	#----------------------------------------------------------------------
	degreeOfFreedom = property(fget=get_degreeOfFreedom,fset=set_degreeOfFreedom)
	
	#----------------------------------------------------------------------
	def get_limitSwitchX(self):
		"""Use the limit the x-axis rotation? When
		queried, this flag returns a boolean.
		"""
		return self._query(limitSwitchX=True)
	#----------------------------------------------------------------------
	def set_limitSwitchX(self,value):
		"""Use the limit the x-axis rotation? When
		queried, this flag returns a boolean.
		"""
		self._edit(limitSwitchX=value)
	#----------------------------------------------------------------------
	limitSwitchX = property(fget=get_limitSwitchX,fset=set_limitSwitchX)

	#----------------------------------------------------------------------
	def get_limitSwitchY(self):
		"""Use the limit the y-axis rotation? When
		queried, this flag returns a boolean.
		"""
		return self._query(limitSwitchY=True)
	#----------------------------------------------------------------------
	def set_limitSwitchY(self,value):
		"""Use the limit the y-axis rotation? When
		queried, this flag returns a boolean.
		"""
		self._edit(limitSwitchY=value)
	#----------------------------------------------------------------------
	limitSwitchY = property(fget=get_limitSwitchY,fset=set_limitSwitchY)

	#----------------------------------------------------------------------
	def get_limitSwitchZ(self):
		"""Use the Limit the z-axis rotation? When
		queried, this flag returns a boolean.
		"""
		return self._query(limitSwitchZ=True)
	#----------------------------------------------------------------------
	def set_limitSwitchZ(self,value):
		"""Use the Limit the z-axis rotation? When
		queried, this flag returns a boolean.
		"""
		self._edit(limitSwitchZ=value)
	#----------------------------------------------------------------------
	limitSwitchZ = property(fget=get_limitSwitchZ,fset=set_limitSwitchZ)

	#----------------------------------------------------------------------
	def get_limitX(self):
		"""Set lower and upper limits on the x-axis of
		rotation.  Also turns on
		the joint limit. When queried, this flag returns 2 floats.
		"""
		return self._query(limitX=True)
	#----------------------------------------------------------------------
	def set_limitX(self,value):
		"""Set lower and upper limits on the x-axis of
		rotation.  Also turns on
		the joint limit. When queried, this flag returns 2 floats.
		"""
		self._edit(limitX=value)
	#----------------------------------------------------------------------
	limitX = property(fget=get_limitX,fset=set_limitX)

	#----------------------------------------------------------------------
	def get_limitY(self):
		"""Set lower and upper limits on the y-axis of
		rotation.  Also turns on
		the joint limit. When queried, this flag returns 2 floats.
		"""
		return self._query(limitY=True)
	#----------------------------------------------------------------------
	def set_limitY(self,value):
		"""Set lower and upper limits on the y-axis of
		rotation.  Also turns on
		the joint limit. When queried, this flag returns 2 floats.
		"""
		self._edit(limitY=value)
	#----------------------------------------------------------------------
	limitY = property(fget=get_limitY,fset=set_limitY)

	#----------------------------------------------------------------------
	def get_limitZ(self):
		"""Set lower and upper limits on the z-axis of
		rotation.  Also turns on
		the joint limit. When queried, this flag returns 2 floats.
		"""
		return self._query(limitZ=True)
	#----------------------------------------------------------------------
	def set_limitZ(self,value):
		"""Set lower and upper limits on the z-axis of
		rotation.  Also turns on
		the joint limit. When queried, this flag returns 2 floats.
		"""
		self._edit(limitZ=value)
	#----------------------------------------------------------------------
	limitZ = property(fget=get_limitZ,fset=set_limitZ)

	#----------------------------------------------------------------------
	def get_orientation(self):
		"""The joint orientation. When queried, this flag
		returns 3 floats.
		"""
		return self._query(orientation=True)
	#----------------------------------------------------------------------
	def set_orientation(self,value):
		"""The joint orientation. When queried, this flag
		returns 3 floats.
		"""
		self._edit(orientation=value)
	#----------------------------------------------------------------------
	orientation = property(fget=get_orientation,fset=set_orientation)

	#----------------------------------------------------------------------
	def get_position(self):
		"""Specifies the position of the center of the joint.
		This position may be relative to the joint's parent
		or in absolute world coordinates (see -r and -a
		below). When queried, this flag returns 3 floats.
		"""
		return self._query(position=True)
	#----------------------------------------------------------------------
	def set_position(self,value):
		"""Specifies the position of the center of the joint.
		This position may be relative to the joint's parent
		or in absolute world coordinates (see -r and -a
		below). When queried, this flag returns 3 floats.
		"""
		self._edit(position=value)
	#----------------------------------------------------------------------
	position = property(fget=get_position,fset=set_position)

	#----------------------------------------------------------------------
	def get_radius(self):
		"""Specifies the joint radius.
		"""
		return self._query(radius=True)
	#----------------------------------------------------------------------
	def set_radius(self,value):
		"""Specifies the joint radius.
		"""
		self._edit(radius=value)
	#----------------------------------------------------------------------
	radius = property(fget=get_radius,fset=set_radius)

	#----------------------------------------------------------------------
	def get_relative(self):
		"""The joint center position is relative to the joint's parent.
		"""
		return self._query(relative=True)
	#----------------------------------------------------------------------
	def set_relative(self,value):
		"""The joint center position is relative to the joint's parent.
		"""
		self._edit(relative=value)
	#----------------------------------------------------------------------
	relative = property(fget=get_relative,fset=set_relative)

	#----------------------------------------------------------------------
	def get_rotationOrder(self):
		"""The rotation order of the joint. The
		argument can be one of the following strings: xyz,
		yzx, zxy, zyx, yxz, xzy.
		"""
		return self._query(rotationOrder=True)
	#----------------------------------------------------------------------
	def set_rotationOrder(self,value):
		"""The rotation order of the joint. The
		argument can be one of the following strings: xyz,
		yzx, zxy, zyx, yxz, xzy.
		"""
		self._edit(rotationOrder=value)
	#----------------------------------------------------------------------
	rotationOrder = property(fget=get_rotationOrder,fset=set_rotationOrder)

	#----------------------------------------------------------------------
	def get_scale(self):
		"""Scale of the joint. When queried, this flag
		returns 3 floats.
		"""
		return self._query(scale=True)
	#----------------------------------------------------------------------
	def set_scale(self,value):
		"""Scale of the joint. When queried, this flag
		returns 3 floats.
		"""
		self._edit(scale=value)
	#----------------------------------------------------------------------
	scale = property(fget=get_scale,fset=set_scale)

	#----------------------------------------------------------------------
	def get_scaleCompensate(self):
		"""It sets the scaleCompenstate attribute of
		the joint to the given argument. When this is true,
		the scale of the parent joint will be compensated
		before any rotation of this joint is applied, so that
		the bone to the joint is scaled but not the bones to
		its child joints. When queried, this flag returns an
		boolean.
		"""
		return self._query(scaleCompensate=True)
	#----------------------------------------------------------------------
	def set_scaleCompensate(self,value):
		"""It sets the scaleCompenstate attribute of
		the joint to the given argument. When this is true,
		the scale of the parent joint will be compensated
		before any rotation of this joint is applied, so that
		the bone to the joint is scaled but not the bones to
		its child joints. When queried, this flag returns an
		boolean.
		"""
		self._edit(scaleCompensate=value)
	#----------------------------------------------------------------------
	scaleCompensate = property(fget=get_scaleCompensate,fset=set_scaleCompensate)

	#----------------------------------------------------------------------
	def get_scaleOrientation(self):
		"""Set the orientation of the coordinate axes for
		scaling. When queried, this flag returns 3 floats.
		"""
		return self._query(scaleOrientation=True)
	#----------------------------------------------------------------------
	def set_scaleOrientation(self,value):
		"""Set the orientation of the coordinate axes for
		scaling. When queried, this flag returns 3 floats.
		"""
		self._edit(scaleOrientation=value)
	#----------------------------------------------------------------------
	scaleOrientation = property(fget=get_scaleOrientation,fset=set_scaleOrientation)

	#----------------------------------------------------------------------
	def get_stiffnessX(self):
		"""Set the stiffness (from 0 to 100.0) for x-axis.
		When queried, this flag returns a float.
		"""
		return self._query(stiffnessX=True)
	#----------------------------------------------------------------------
	def set_stiffnessX(self,value):
		"""Set the stiffness (from 0 to 100.0) for x-axis.
		When queried, this flag returns a float.
		"""
		self._edit(stiffnessX=value)
	#----------------------------------------------------------------------
	stiffnessX = property(fget=get_stiffnessX,fset=set_stiffnessX)

	#----------------------------------------------------------------------
	def get_stiffnessY(self):
		"""Set the stiffness (from 0 to 100.0) for y-axis.
		When queried, this flag returns a float.
		"""
		return self._query(stiffnessY=True)
	#----------------------------------------------------------------------
	def set_stiffnessY(self,value):
		"""Set the stiffness (from 0 to 100.0) for y-axis.
		When queried, this flag returns a float.
		"""
		self._edit(stiffnessY=value)
	#----------------------------------------------------------------------
	stiffnessY = property(fget=get_stiffnessY,fset=set_stiffnessY)

	#----------------------------------------------------------------------
	def get_stiffnessZ(self):
		"""Set the stiffness (from 0 to 100.0) for z-axis.
		When queried, this flag returns a float.
		"""
		return self._query(stiffnessZ=True)
	#----------------------------------------------------------------------
	def set_stiffnessZ(self,value):
		"""Set the stiffness (from 0 to 100.0) for z-axis.
		When queried, this flag returns a float.
		"""
		self._edit(stiffnessZ=value)
	#----------------------------------------------------------------------
	stiffnessZ = property(fget=get_stiffnessZ,fset=set_stiffnessZ)