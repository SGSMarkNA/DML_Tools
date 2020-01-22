
import nuke
from ..Base_Nodes import DML_Nuke_Object
from ...Decorators.Node_Wraper_Manager import node_Return_Wrapper,nuke_Object_Return_Wrapper,knob_Return_Wrapper

########################################################################
class Interpolations:
	""""""
	HORIZONTAL    = nuke.HORIZONTAL
	BREAK         = nuke.BREAK
	BEFORE_CONST  = nuke.BEFORE_CONST
	BEFORE_LINEAR = nuke.BEFORE_LINEAR
	AFTER_CONST   = nuke.AFTER_CONST
	AFTER_LINEAR  = nuke.AFTER_LINEAR
		
		
    
	
################################################################################
class AnimationCurve(DML_Nuke_Object):
	INTERPOLATIONS = Interpolations
	#----------------------------------------------------------------------
	def addKey(self,keys):
		"""
		self.addKey(keys) -> None.
		Insert a sequence of keys.
		@param keys: Sequence of AnimationKey.
		@return: None.
		"""
		return self.nuke_object.addKey(keys)
	#----------------------------------------------------------------------
	def changeInterpolation(self,keys, typ):
		"""
		self.changeInterpolation(keys, type) -> None.
		Change interpolation (and extrapolation) type for the keys.
		@param keys: Sequence of keys.
		@param type: Interpolation type. One of:
		       nuke.HORIZONTAL
		       nuke.BREAK
		       nuke.BEFORE_CONST
		       nuke.BEFORE_LINEAR
		       nuke.AFTER_CONST
		       nuke.AFTER_LINEAR.
		@return: None.
		"""
		return self.nuke_object.changeInterpolation(keys, typ)
	#----------------------------------------------------------------------
	def clear(self):
		"""self.clear() -> None. Delete all keys. @return: None."""
		return self.nuke_object.clear()
	#----------------------------------------------------------------------
	def fixSlopes(self):
		"""self.fixSlopes() -> None. @return: None."""
		return self.nuke_object.fixSlopes()
	#----------------------------------------------------------------------
	def constant(self):
		"""
			self.constant() -> bool @return:
			True if the animation appears to be a horizontal line, is a simple number,
			or it is the default and all the points are at the same y value and have 0 slopes.
			False otherwise."""
		return self.nuke_object.constant()
	#----------------------------------------------------------------------
	def size(self):
		"""self.size() -> Number of keys. @return: Number of keys."""
		return self.nuke_object.size()
	#----------------------------------------------------------------------
	def knobIndex(self):
		"""
			self.knobIndex() -> Int. Return 
			the knob index this animation belongs to.
			@return: Int.
		"""
		return self.nuke_object.knobIndex()
	#----------------------------------------------------------------------
	def inverse(self,y):
		"""
			self.inverse(y) -> Float. 
			The inverse function at value y.
			This is the value of x such that evaluate(x) returns y.
			This is designed to invert color lookup tables.
			It only works if the derivative is zero or positive everywhere.
			
			@param y: The value of the function to get the inverse for.
			@return: Float.
		"""
		return self.nuke_object.inverse(y)
	#----------------------------------------------------------------------
	def selected(self):
		"""self.selected() -> bool @return: True if selected, False otherwise."""
		return self.nuke_object.selected()
	#----------------------------------------------------------------------
	def setKey(self,t, y):
		"""
			self.setKey(t, y) -> Key. Set a key at time t and value y.
			If there is no key there one is created.
			If there is a key there it is moved vertically to be at y.
			If a new key is inserted the interpolation and extrapolation are copied from a neighboring key,
			if there were no keys then it is set to nuke.SMOOTH interpolation and nuke.CONSTANT extrapolation.
			
			@param t: The time to set the key at.
			@param y: The value for the key.
			@return: The new key.
		"""
		return self.nuke_object.setKey(t, y)
	#----------------------------------------------------------------------
	def toScript(self,selected):
		"""self.toScript(selected) -> str 
		@param selected: Optional parameter. 
		If this is given and is True, 
		then only process the selected curves;
		otherwise convert all. 
		@return: A string containing the curves."""
		return self.nuke_object.toScript(selected)
	#----------------------------------------------------------------------
	@knob_Return_Wrapper
	def knob(self):
		"""self.knob() -> Knob. Return knob this animation belongs to.@return: Knob."""
		return self.nuke_object.knob()
	#----------------------------------------------------------------------
	@nuke_Object_Return_Wrapper
	def keys(self):
		"""self.keys() -> List of keys. @return: List of keys."""
		return self.nuke_object.keys()
	#----------------------------------------------------------------------
	def evaluate(self,t):
		"""self.evaluate(t) -> float Value at time 't'. @param t: Time. @return: The value of the animation at time 't'."""
		return self.nuke_object.evaluate(t)
	#----------------------------------------------------------------------
	def integrate(self):
		"""self.integrate(t1, t2) -> Float. Calculate the area underneath the curve from t1 to t2. @param t1 The start of the integration range. @param t2 The end of the integration range. @return: The result of the integration."""
		return self.nuke_object.integrate()
	#----------------------------------------------------------------------
	def derivative(self):
		"""self.derivative(t, n) -> Float. The n'th derivative at time 't'. If n is less than 1 it returns evaluate(t). @param t: Time. @param n: Optional. Default is 1. @return: The value of the derivative."""
		return self.nuke_object.derivative()
	#----------------------------------------------------------------------
	def setExpression(self,s):
		"""self.setExpression(s) -> None. Set expression. @param s: A string containing the expression. @return: None."""
		return self.nuke_object.setExpression(s)
	#----------------------------------------------------------------------
	def identity(self):
		"""self.identity() -> bool @return: True if the animation appears to be such that y == x everywhere. This is True only for an expression of 'x' or the default expression and all points having y == x and slope == 1. Extrapolation is ignored."""
		return self.nuke_object.identity()
	#----------------------------------------------------------------------
	def fromScript(self,s):
		"""self.fromScript(s) -> None. @param s: String. @return: None."""
		return self.nuke_object.fromScript(s)
	#----------------------------------------------------------------------
	def knobAndFieldName(self):
		"""self.knobAndFieldName() -> string. Knob and field name combined (e.g. 'translate.x'). @return: string."""
		return self.nuke_object.knobAndFieldName()
	#----------------------------------------------------------------------
	def noExpression(self):
		"""self.noExpression() -> bool @return: True if the expression is the default expression (i.e. the keys control the curve), False otherwise."""
		return self.nuke_object.noExpression()
	#----------------------------------------------------------------------
	def expression(self):
		"""self.expression() -> String. Get the expression.@return: String."""
		return self.nuke_object.expression()
	#----------------------------------------------------------------------
	def view(self):
		"""self.view() -> String. The view this AnimationCurve object is associated with. @return: String."""
		return self.nuke_object.view()
