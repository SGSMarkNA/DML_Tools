import nuke
from ..Abstract_Nodes import Knob
from ...Decorators.Node_Wraper_Manager import node_Return_Wrapper,nuke_Object_Return_Wrapper,knob_Return_Wrapper

################################################################################
class Array_Knob(Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "Array_Knob"
	#----------------------------------------------------------------------
	def animation(self,chan,view=None):
		"""
			self.animation(chan, view) -> AnimationCurve or None.

			Return the AnimationCurve for the  channel 'chan' and view 'view'. The view argument is optional.

			@param channel: The channel index.

			@param view: Optional view.

			@return: AnimationCurve or None.

		"""
		res = self.nuke_object.animation(chan,view=view)
		isinstance(res,nuke.AnimationCurve)
		return res
	#----------------------------------------------------------------------
	@nuke_Object_Return_Wrapper
	def animations(self,view=None):
		"""
			self.animations(view) -> AnimationCurve list.

			@param view: Optional view.

			@return: AnimationCurve list.

			Example:

			b = nuke.nodes.Blur()

			k = b['size']

			k.setAnimated(0)

			a = k.animations()

			a[0].setKey(0, 11)

			a[0].setKey(10, 20)

		"""
		return self.nuke_object.animations(view)
	#----------------------------------------------------------------------
	def array(self):
		"""
			self.array() -> List of knob values.

			@return: List of knob values.

		"""
		return self.nuke_object.array()
	#----------------------------------------------------------------------
	def arraySize(self):
		"""
			self.arraySize() -> Number of elements in array.

			@return: Number of elements in array.

		"""
		return self.nuke_object.arraySize()
	#----------------------------------------------------------------------
	def copyAnimation(self,channel, curve,**kwargs):
		"""
			self.copyAnimation(channel, curve, view) -> None.

			Copies the i'th channel of the AnimationCurve curve to this object. The view is optional and defaults to the current view.

			@param channel: The channel index.

			@param curve: AnimationCurve.

			@param view: Optional view. Defaults to current.

			@return: None.

		"""
		return self.nuke_object.copyAnimation(channel, curve,**kwargs)
	#----------------------------------------------------------------------
	def copyAnimations(self,curves,**kwargs):
		"""
			self.copyAnimations(curves, view) -> None.

			Copies the AnimationCurves from curves to this object. The view is optional and defaults to the current view.

			@param curves: AnimationCurve list.

			@param view: Optional view. Defaults to current.

			@return: None.

		"""
		return self.nuke_object.copyAnimations(curves,**kwargs)
	#----------------------------------------------------------------------
	def defaultValue(self):
		"""
			self.defaultValue() -> Default value.

			@return: Default value.

		"""
		return self.nuke_object.defaultValue()
	#----------------------------------------------------------------------
	def deleteAnimation(self,curve):
		"""
			self.deleteAnimation(curve) -> None. Raises ValueError if not found.

			Deletes the AnimationCurve.

			@param curve: An AnimationCurve instance which belongs to this Knob.

			@return: None. Raises ValueError if not found.

		"""
		return self.nuke_object.deleteAnimation(curve)
	#----------------------------------------------------------------------
	def dimensions(self):
		"""
			self.dimensions() -> Dimensions in array.

			@return: Dimensions in array.

		"""
		return self.nuke_object.dimensions()
	#----------------------------------------------------------------------
	def frame(self):
		"""
			self.frame() -> Frame number.

			@return: Frame number.

		"""
		return self.nuke_object.frame()
	#----------------------------------------------------------------------
	def height(self):
		"""
			self.height() -> Height of array of values.

			@return: Height of array of values.

		"""
		return self.nuke_object.height()
	#----------------------------------------------------------------------
	def max(self):
		"""
			self.max() -> Maximum value.

			@return: Maximum value.

		"""
		return self.nuke_object.max()
	#----------------------------------------------------------------------
	def maximum(self):
		"""
			self.max() -> Maximum value.

			@return: Maximum value.

		"""
		return self.nuke_object.maximum()
	#----------------------------------------------------------------------
	def min(self):
		"""
			self.min() -> Minimum value.

			@return: Minimum value.

		"""
		return self.nuke_object.min()
	#----------------------------------------------------------------------
	def minimum(self):
		"""
			self.min() -> Minimum value.

			@return: Minimum value.

		"""
		return self.nuke_object.minimum()
	#----------------------------------------------------------------------
	def notDefault(self):
		"""
			self.notDefault() -> True if any of the values is not set to the default, False otherwise.

			@return: True if any of the values is not set to the default, False otherwise.

		"""
		return self.nuke_object.notDefault()
	#----------------------------------------------------------------------
	def resize(self,*args):
		"""
			self.resize(w, h) -> True if successful, False otherwise.

			Resize the array.

			@param w: New width

			@param h: Optional new height

			@return: True if successful, False otherwise.

		"""
		return self.nuke_object.resize(*args)
	#----------------------------------------------------------------------
	def setDefaultValue(self,seq):
		"""
			self.setDefaultValue(s) -> None.

			@param s: Sequence of floating-point values.

			@return: None.

		"""
		return self.nuke_object.setDefaultValue(seq)
	#----------------------------------------------------------------------
	def setKeyAt(self,*args):
		"""
			self.setKeyAt(time, index, view) -> None.

			Set a key on element 'index', at time and view.

			@param time: Time.

			@param index: Optional index.

			@param view: Optional view.

			@return: None.

		"""
		return self.nuke_object.setKeyAt(*args)
	#----------------------------------------------------------------------
	def setRange(self,f1, f2):
		"""
			self.setRange(f1, f2) -> None.

			Set range of values.

			@param f1 Min value.

			@param f2 Max value.

			@return: None.

		"""
		return self.nuke_object.setRange(f1, f2)
	#----------------------------------------------------------------------
	def setSingleValue(self,*args):
		"""
			self.setSingleValue(b, view) -> None.

			Set to just hold a single value or not.

			@param b: Boolean object.

			@param view: Optional view. Default is current view.

			@return: None.

		"""
		return self.nuke_object.setSingleValue(*args)
	#----------------------------------------------------------------------
	def singleValue(self,*args):
		"""
			self.singleValue(view) -> True if holds a single value.

			@param view: Optional view. Default is current view.

			@return: True if holds a single value.

		"""
		return self.nuke_object.singleValue(*args)
	#----------------------------------------------------------------------
	def splitView(self,*args):
		"""
			self.splitView(view) -> None.

			Split the view away from the current knob value.

			@param view: Optional view. Default is current view.

			@return: None.

		"""
		return self.nuke_object.splitView(*args)
	#----------------------------------------------------------------------
	def unsplitView(self,*args):
		"""
			self.unsplitView(view) -> None.

			Unsplit the view so that it shares a value with other views.

			@param view: Optional view. Default is current view.

			@return: None.

		"""
		return self.nuke_object.unsplitView(*args)
	#----------------------------------------------------------------------
	def valueAt(self,*args):
		"""
			self.valueAt(time, index, view) -> Floating point or List of floating point values (in case some are different).

			Return value for this knob at specified time, optional index and view.

			@param time: Time.

			@param index: Optional index. Default is 0.

			@param view: Optional view.

			@return: Floating point or List of floating point values (in case some are different).

		"""
		return self.nuke_object.valueAt(*args)
	#----------------------------------------------------------------------
	def vect(self):
		"""
			self.vect() -> List of knob values.

			@return: List of knob values.

		"""
		return self.nuke_object.vect()
	#----------------------------------------------------------------------
	def width(self):
		"""
			self.width() -> Width of array of values.

			@return: Width of array of values.

		"""
		return self.nuke_object.width()

