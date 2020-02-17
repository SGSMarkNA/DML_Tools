import nuke
from ..Base_Nodes.API_Knob import DML_Knob
from ...Decorators.Node_Wraper_Manager import node_Return_Wrapper,nuke_Object_Return_Wrapper,knob_Return_Wrapper


################################################################################
class Knob(DML_Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "default"
	
	#----------------------------------------------------------------------
	@property
	def Class(self):
		"""
			self.Class() -> Class name.

			@return: Class name.

		"""
		return self.nuke_object.Class()
	#----------------------------------------------------------------------
	def clearAnimated(self,channel=-1):
		"""
			Clear animation for channel 'c'. Return True if successful.

		"""
		return self.nuke_object.clearAnimated(channel)
	#----------------------------------------------------------------------
	def clearFlag(self,f):
		"""
			self.clearFlag(f) -> None.

			Clear flag.

			@param f: Flag.

			@return: None.

		"""
		return self.nuke_object.clearFlag(f)
	#----------------------------------------------------------------------
	def critical(self,message):
		"""
			self.critical(message) -> None.

			@param message: message to put the knob in error, and do a popup.

			@return: None.

		"""
		return self.nuke_object.critical(message)
	#----------------------------------------------------------------------
	def debug(self,message):
		"""
			self.debug(message) -> None.

			@param message: message to put out to the error console, attached to the knob, if the verbosity level is set high enough.

			@return: None.

		"""
		return self.nuke_object.debug(message)
	#----------------------------------------------------------------------
	def error(self,message):
		"""
			self.error(message) -> None.

			@param message: message to put the knob in error.

			@return: None.

		"""
		return self.nuke_object.error(message)
	#----------------------------------------------------------------------
	def warning(self,message):
		"""
			self.warning(message) -> None.

			@param message: message to put a warning on the knob.

			@return: None.

		"""
		return self.nuke_object.warning(message)	
	#----------------------------------------------------------------------
	def fromScript(self,arg):
		"""
			Initialise from script.

		"""
		return self.nuke_object.fromScript(arg)
	#----------------------------------------------------------------------
	def fullyQualifiedName(self,channel=-1):
		"""
			self.fullyQualifiedName(channel=-1) -> string

			Returns the fully-qualified name of the knob within the node. This can be useful for expression linking.

			@param channel: Optional parameter, specifies the channel number of the sub-knob (for example, channels of  0 and 1 would refer to the x and y of a XY_Knob respectively), leave blank or set to -1 to get the  qualified name of the knob only.

			@return: The string of the qualified knob or sub-knob, which can be used directly in expression links.

		"""
		return self.nuke_object.fullyQualifiedName(channel)
	#----------------------------------------------------------------------
	def getDerivative(self,floatVal):
		"""
			Return derivative at time 't' for channel 'c'.

		"""
		return self.nuke_object.getDerivative(floatVal)
	#----------------------------------------------------------------------
	def getFlag(self,f):
		"""
			self.getFlag(f) -> Bool.

			Returns whether the input flag is set.

			@param f: Flag.

			@return: True if set, False otherwise.

		"""
		return self.nuke_object.getFlag(f)
	#----------------------------------------------------------------------
	def getIntegral(self,t1,t2,channel=-1):
		"""
			Return integral at the interval [t1, t2] for channel 'c'.

		"""
		return self.nuke_object.getIntegral(t1,t2,channel)
	#----------------------------------------------------------------------
	def getKeyIndex(self,t,channel=-1):
		"""
			Return keyframe index at time 't' for channel 'c'.

		"""
		return self.nuke_object.getKeyIndex(t,channel)
	#----------------------------------------------------------------------
	def getKeyList(self):
		"""
			Get all unique keys on the knob.  Returns list.

		"""
		res = self.nuke_object.getKeyList()
		isinstance(res,list)
		return res
	#----------------------------------------------------------------------
	def getKeyTime(self,t,channel=-1):
		"""
			Return index of the keyframe at time 't' for channel 'c'.

		"""
		return self.nuke_object.getKeyTime(t,channel)
	#----------------------------------------------------------------------
	def getNthDerivative(self,t,channel=-1):
		"""
			Return nth derivative at time 't' for channel 'c'.

		"""
		return self.nuke_object.getNthDerivative(t,channel)
	#----------------------------------------------------------------------
	def getNumKeys(self,channel=-1):
		"""
			Return number of keyframes for channel 'c'.

		"""
		return self.nuke_object.getNumKeys(channel)
	#----------------------------------------------------------------------
	def getValue(self,channel=-1):
		"""
			Return value at the current frame for channel 'c'.

		"""
		try:
			return self.nuke_object.getValue(channel)
		except:
			return self.nuke_object.getValue()
	#----------------------------------------------------------------------
	def getValueAt(self,t,channel=-1):
		"""
			Return value at time 't' for channel 'c'.

		"""
		return self.nuke_object.getValueAt(t,channel)
	#----------------------------------------------------------------------
	def hasExpression(self,index=-1):
		"""
			self.hasExpression(index=-1) -> bool

			Return True if animation at index 'index' has an expression.

			@param index: Optional index parameter. Defaults to -1 if not specified. This can be specified as a keyword parameter if desired.

			@return: True if has expression, False otherwise.

		"""
		return self.nuke_object.hasExpression(index)
	#----------------------------------------------------------------------
	def isAnimated(self,channel=-1):
		"""
			Return True if channel 'c' is animated.

		"""
		return self.nuke_object.isAnimated(channel)
	#----------------------------------------------------------------------
	def isKey(self,channel=-1):
		"""
			Return True if there is a keyframe at the current frame for channel 'c'.

		"""
		return self.nuke_object.isKey(channel)
	#----------------------------------------------------------------------
	def isKeyAt(self,t,channel=-1):
		"""
			Return True if there is a keyframe at time 't' for channel 'c'.

		"""
		return self.nuke_object.isKeyAt(t,channel)
	#----------------------------------------------------------------------
	def node(self):
		"""
			self.node() -> nuke.Node

			Return the node that this knob belongs to. If the node has been cloned, we'll always return a reference to the original.

			@return: The node which owns this knob, or None if the knob has no owner yet.

		"""
		return self.nuke_object.node()
	#----------------------------------------------------------------------
	def removeKey(self,channel=-1):
		"""
			Remove key for channel 'c'. Return True if successful.

		"""
		return self.nuke_object.removeKey(channel)
	#----------------------------------------------------------------------
	def removeKeyAt(self,t,*c):
		"""
			Remove key at time 't' for channel 'c'. Return True if successful.

		"""
		return self.nuke_object.removeKeyAt(t,*c)
	#----------------------------------------------------------------------
	def setAnimated(self,*c):
		"""
			Set channel 'c' to be animated.

		"""
		return self.nuke_object.setAnimated(*c)
	#----------------------------------------------------------------------
	def setExpression(self,expression, **kwargs):
		"""
			self.setExpression(expression, channel=-1, view=None) -> bool

			Set the expression for a knob. You can optionally specify a channel to set the expression for.

			@param expression: The new expression for the knob. This should be a string.

			@param channel: Optional parameter, specifying the channel to set the expression for. This should be an integer.

			@param view: Optional view parameter. Without, this command will set the expression for the current view theinterface is displaying. Can be the name of the view or the index.

			@return: True if successful, False if not.

		"""
		return self.nuke_object.setExpression(expression, **kwargs)
	#----------------------------------------------------------------------
	def setFlag(self,f):
		"""
			self.setFlag(f) -> None.

			Logical OR of the argument and existing knob flags.

			@param f: Flag.

			@return: None.

		"""
		return self.nuke_object.setFlag(f)
	#----------------------------------------------------------------------
	def setLabel(self,s):
		"""
			self.setLabel(s) -> None.

			@param s: New label.

			@return: None.

		"""
		return self.nuke_object.setLabel(s)
	#----------------------------------------------------------------------
	def setName(self,s):
		"""
			self.setName(s) -> None.

			@param s: New name.

			@return: None.

		"""
		return self.nuke_object.setName(s)
	#----------------------------------------------------------------------
	def setTooltip(self,s):
		"""
			self.setTooltip(s) -> None.

			@param s: New tooltip.

			@return: None.

		"""
		return self.nuke_object.setTooltip(s)
	#----------------------------------------------------------------------
	def setValue(self,val,channel=-1):
		"""
			self.setValue(val, chan) -> bool

			Sets the value 'val' at channel 'chan'.

			@return: True if successful, False if not.

		"""
		if not channel == -1:
			return self.nuke_object.setValue(val,channel)
		else:
			return self.nuke_object.setValue(val)
	#----------------------------------------------------------------------
	def setValueAt(self,val, time, chan=-1):
		"""
			self.setValueAt(val, time, chan) -> bool

			Sets the value 'val' at channel 'chan' for time 'time'.

			@return: True if successful, False if not.

		"""
		return self.nuke_object.setValueAt(val, time, chan)
	#----------------------------------------------------------------------
	def setVisible(self,visible):
		"""
			self.setVisible(visible) -> None.

			Show or hide the knob.

			@param visible: True to show the knob, False to hide it.

		"""
		return self.nuke_object.setVisible(visible)
	#----------------------------------------------------------------------
	def toScript(self,quote=False,context=None):
		"""
			toScript(quote, context=current) -> string.

			Return the value of the knob in script syntax.

			Pass True for quote to return results quoted in {}.

			Pass None for context to get results for all views and key times (as stored in a .nk file).

		"""
		return self.nuke_object.toScript(quote,context)
	#----------------------------------------------------------------------
	def value(self,channel=-1):
		"""
			Return value at the current frame for channel 'c'.

		"""
		try:
			return self.nuke_object.value(channel)
		except:
			return self.nuke_object.value()
