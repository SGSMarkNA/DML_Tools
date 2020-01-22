

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class ColorEditor(UI_Object.UI):
	"""
	command displays a modal dialog that may be used
	to specify colors in RGB or HSV. The default behaviour
	when no arguments are specified is to provide an initial color of
	black (rgb 0.0 0.0 0.0).
	
	The command will return the user's color component values along with a
	boolean to indicate whether the dialog was dismissed by pressing
	the "OK" button.  As an alternative to responding to
	the  command's return string you can now query
	the , and 
	flags to get the same information.
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.colorEditor(**kwargs)
			super(ColorEditor, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.colorEditor(name, exists=True):
				super(ColorEditor, self).__init__(name)
			else:
				name = cmds.colorEditor(name, **kwargs)
				super(ColorEditor, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def alpha(self):
		"""
		
				Float values corresponding to the alpha transparency component,
				, which ranges from 0.0 to 1.0.  Use this flag to specify the
				initial alpha value of the Color Editor, or query
				this flag to determine the alpha value set in the editor.
				
		"""
		return self.query(alpha=True)
	#----------------------------------------------------------------------
	@property
	def hsvValue(self):
		"""
		
				Three float values corresponding to the hue, saturation, and
				value color components, where the hue value ranges from 0.0 to 360.0
				and the saturation and value components range from 0.0 to 1.0.  Use
				this flag to specify the initial color of the Color Editor, or query
				this flag to determine the color set in the editor.
				
		"""
		return self.query(hsvValue=True)
	#----------------------------------------------------------------------
	@property
	def result(self):
		"""
		
				This query only flag returns true if the dialog's "OK" button
				was pressed, false otherwise.  If you query this flag immediately
				after showing the Color Editor then it will return the same value
				as the boolean value returned in the colorEditor command's
				return string.
				
		"""
		return self.query(result=True)
	#----------------------------------------------------------------------
	@property
	def rgbValue(self):
		"""
		
				Three float values corresponding to the red, green, and blue
				color components, all of which range from 0.0 to 1.0.  Use this
				flag to specify the initial color of the Color Editor, or query
				this flag to determine the color set in the editor.
				
		"""
		return self.query(rgbValue=True)