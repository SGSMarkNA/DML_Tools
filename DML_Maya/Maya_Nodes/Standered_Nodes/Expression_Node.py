import maya.cmds as cmds
from .. import Dependency_Node 
from ...General_Utils import flatten

class Expression(Dependency_Node):
	MAYA_NODE_TYPE_RELATION = "expression"
	#----------------------------------------------------------------------
	@classmethod
	def createNode(cls,*args,**kwargs):
		"""
		alwaysEvaluate e,q,c
			If this is TRUE (the default), 
			then the expression will be evaluated whenever time changes
			regardless of whether the other inputs have changed, and an output is requested.
			If it is FALSE, 
			then the expression will only be evaluated if one or more of the inputs changes and an output is requested.
			Note, if 'time' or 'frame' are inputs, then the expression will act as if this was set to TRUE.
			
		animated e,q,c
			Sets the animation mode on the expression node: 0 = Not Animated, 1 = Animated, 2 = Animated with No Callback
			
		name e,q,c
			Sets the name of the dependency graph node to use for the expression 
			
		object e,q,c
			 Sets the "default" object for the expression. This allows the expression writer to not type the object name for frequently-used objects.
			 
		safe q
			Returns true if no potential side effect can occurs running that expression. Safe expression will be optimized to evaluate only when needed even if flagged alwaysEvaluate. 
			
		shortNames e,q,c
			When used with the -q/query flag,
			tells the command to return the expression with attribute names as short as possible.
			The default is to return the FULL attribute name,
			regardless of how the user entered it into the expression,
			including the object names.
			With this flag set, 
			attribute names are returned as their short versions,
			and any attribute that belongs to the default object,
			if there is one specified,
			will not display the object's name.
			
		string e,q,c
			Set the expression string 
			
		
		"""
		# cmds.expression( attribute="", alwaysEvaluate=0, animated=0, name="", object="", string="", safe=True, shortNames=True, timeDependent=True, unitConversion="",)
		name = cmds.expression(*args,**kwargs)
		return name
	#----------------------------------------------------------------------
	def get_alwaysEvaluate(self):
		""""""
		return cmds.expression(self,q=True,alwaysEvaluate=True)
	#----------------------------------------------------------------------
	def set_alwaysEvaluate(self,val):
		""""""
		return cmds.expression(self,e=True,alwaysEvaluate=val)
	#----------------------------------------------------------------------
	alwaysEvaluate = property(get_alwaysEvaluate,set_alwaysEvaluate)
	#----------------------------------------------------------------------
	def get_String(self):
		""""""
		return cmds.expression(self,q=True,s=True)
	#----------------------------------------------------------------------
	def set_String(self,val):
		""""""
		return cmds.expression(self,e=True,s=val)
	#----------------------------------------------------------------------
	expression_string = property(get_String,set_String)
	#----------------------------------------------------------------------
	def get_Object(self):
		""""""
		return cmds.expression(self,q=True,object=True)
	#----------------------------------------------------------------------
	def set_Object(self,val):
		""""""
		return cmds.expression(self,e=True,object=val)
	#----------------------------------------------------------------------
	expression_object = property(get_Object,set_Object)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	