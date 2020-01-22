

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class HeadsUpDisplay(UI_Object.UI):
	"""
	This command creates a Heads-up Display (HUD) object which is placed in a 2D
	inactive overlay plane on the 3D viewport. It is to be used to provide hands-on
	information designated by a user script. The text string displayed on the viewport
	is formatted using the various flags of this command.
	
	The only mandatory flags, on creation are the section and block flags. Note if the preset
	OR command/trigger flags are not present, only a label will be drawn on the viewport.
	
	Upon creation of a HUD object, an ID number will be assigned to it. This can be used to
	remove the HUD object (-rid/removeID [int IDNumber]), if desired. Alternatively, HUD
	objects may be removed via their position (section and block), or their unique name.
		  
	      hud, headsupdisplay
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.headsUpDisplay(**kwargs)
			super(HeadsUpDisplay, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.headsUpDisplay(name, exists=True):
				super(HeadsUpDisplay, self).__init__(name)
			else:
				name = cmds.headsUpDisplay(name, **kwargs)
				super(HeadsUpDisplay, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def allDescendants(self,value):
		"""
		
				This flag can only be used in conjunction with the -ac/attributeChange
				flag. If it is specified, and the HUD is attached to a compound or multi
				attribute, then the HUD command will run due to changes to the specified
				attribute as well as changes to its descendants.
				
		"""
		self.edit(allDescendants=value)
	#----------------------------------------------------------------------
	def get_allowOverlap(self):
		"""
		
				Sets the Heads-Up Display to be visible regardless of overlapping section
				widths/limitations (see -s/section flag description for more details).
				
		"""
		return self.query(allowOverlap=True)
	#----------------------------------------------------------------------
	def set_allowOverlap(self, value):
		"""
		
				Sets the Heads-Up Display to be visible regardless of overlapping section
				widths/limitations (see -s/section flag description for more details).
				
		"""
		self.edit(allowOverlap=value)
	#----------------------------------------------------------------------
	allowOverlap = property(get_allowOverlap, set_allowOverlap)
	#----------------------------------------------------------------------
	def get_attachToRefresh(self):
		"""
		
				Attaches the command to the refresh process. The script is then run each time
				an idle refresh is run and updates directly following it.
				
		"""
		return self.query(attachToRefresh=True)
	#----------------------------------------------------------------------
	def set_attachToRefresh(self, value):
		"""
		
				Attaches the command to the refresh process. The script is then run each time
				an idle refresh is run and updates directly following it.
				
		"""
		self.edit(attachToRefresh=value)
	#----------------------------------------------------------------------
	attachToRefresh = property(get_attachToRefresh, set_attachToRefresh)
	#----------------------------------------------------------------------
	def attributeChange(self,value):
		"""
		
				Runs the command when the named attribute changes value. The string must
				identify both the dependency node and the particular attribute. If the
				dependency node is deleted, this HUD is removed (even if the deletion is
				undoable).
				
		"""
		self.edit(attributeChange=value)
	#----------------------------------------------------------------------
	def get_block(self):
		"""
		
				Denotes the individual block that the HUD will reside in, within a
				section. Each section is composed of a single column of blocks.
				The total number of blocks contained within each section is variable.
				
				The number of blocks that will be visible within each section is
				dependent on the size of blocks contained in each section and the
				current size of the window. Blocks begin enumerating from 0 and
				flexibly increase based on need.
				
				The resultant output string of each HUD is formatted within each block,
				using parameters defined by the formatting flags listed below (eg. justify,
				padding, labelWidth and dataWidth). The layout is shown in the following
				diagram:
				
				 __________________________________________
				|     |     |        |         |     |     |
				|  P  |  J  |   LW   |   DWX   |  J  |  P  |
				|_____|_____|________|_________|_____|_____|
				P = Sub-block of width, padding
				J = Justification of the entire block
				LW = Sub-block of width, labelWidth
				DWX = X number of sub-blocks of width, dataWidth, for X data elements.
				
				
				Block Layout
				
				The above diagram shows the layout of each block. The widths: padding,
				labelWidth and dataWidth are defined by their respective flags. To
				elaborate on the layout of the blocks, First the padding of the block is
				calculated. Then the two main sub-blocks (LW and DWX) in the above diagram,
				are justified and positioned together between the left and right margins
				of the block. The widths of the main sub-blocks are not variable based on
				it's contents. The only sub-block in the above diagram which is unique is the
				DWX sub-block which actually represents X number of sub-blocks, where X
				is the number of data elements returned by the command.
				
				Block Positioning
				
				Blocks on the top section begin from the top edge of the main
				viewport, while the bottom section begins from the bottom edge.
				Blocks are dynamically removed from visibility from the midpoint
				of the viewport. So, a relatively large block number will not
				draw to the viewport.
				
				Lastly, there can be at most one HUD occupying a block at any time.
				Trying to position a HUD in an occupied block will result in an error.
				Keep this in mind when positioning the HUD.
				
		"""
		return self.query(block=True)
	#----------------------------------------------------------------------
	def set_block(self, value):
		"""
		
				Denotes the individual block that the HUD will reside in, within a
				section. Each section is composed of a single column of blocks.
				The total number of blocks contained within each section is variable.
				
				The number of blocks that will be visible within each section is
				dependent on the size of blocks contained in each section and the
				current size of the window. Blocks begin enumerating from 0 and
				flexibly increase based on need.
				
				The resultant output string of each HUD is formatted within each block,
				using parameters defined by the formatting flags listed below (eg. justify,
				padding, labelWidth and dataWidth). The layout is shown in the following
				diagram:
				
				 __________________________________________
				|     |     |        |         |     |     |
				|  P  |  J  |   LW   |   DWX   |  J  |  P  |
				|_____|_____|________|_________|_____|_____|
				P = Sub-block of width, padding
				J = Justification of the entire block
				LW = Sub-block of width, labelWidth
				DWX = X number of sub-blocks of width, dataWidth, for X data elements.
				
				
				Block Layout
				
				The above diagram shows the layout of each block. The widths: padding,
				labelWidth and dataWidth are defined by their respective flags. To
				elaborate on the layout of the blocks, First the padding of the block is
				calculated. Then the two main sub-blocks (LW and DWX) in the above diagram,
				are justified and positioned together between the left and right margins
				of the block. The widths of the main sub-blocks are not variable based on
				it's contents. The only sub-block in the above diagram which is unique is the
				DWX sub-block which actually represents X number of sub-blocks, where X
				is the number of data elements returned by the command.
				
				Block Positioning
				
				Blocks on the top section begin from the top edge of the main
				viewport, while the bottom section begins from the bottom edge.
				Blocks are dynamically removed from visibility from the midpoint
				of the viewport. So, a relatively large block number will not
				draw to the viewport.
				
				Lastly, there can be at most one HUD occupying a block at any time.
				Trying to position a HUD in an occupied block will result in an error.
				Keep this in mind when positioning the HUD.
				
		"""
		self.edit(block=value)
	#----------------------------------------------------------------------
	block = property(get_block, set_block)
	#----------------------------------------------------------------------
	def get_blockAlignment(self):
		"""
		
				Specifies the alignment of the block within its respective column. Available
				alignments are: "center", "left" and "right". The default alignment is "left".
				
		"""
		return self.query(blockAlignment=True)
	#----------------------------------------------------------------------
	def set_blockAlignment(self, value):
		"""
		
				Specifies the alignment of the block within its respective column. Available
				alignments are: "center", "left" and "right". The default alignment is "left".
				
		"""
		self.edit(blockAlignment=value)
	#----------------------------------------------------------------------
	blockAlignment = property(get_blockAlignment, set_blockAlignment)
	#----------------------------------------------------------------------
	def get_blockSize(self):
		"""
		
				Sets the height of each block. Available heights are: small, medium and large.
				In pixel measurements, each corresponds to a 20, 35 or 50 pixel height, respectively.
				
		"""
		return self.query(blockSize=True)
	#----------------------------------------------------------------------
	def set_blockSize(self, value):
		"""
		
				Sets the height of each block. Available heights are: small, medium and large.
				In pixel measurements, each corresponds to a 20, 35 or 50 pixel height, respectively.
				
		"""
		self.edit(blockSize=value)
	#----------------------------------------------------------------------
	blockSize = property(get_blockSize, set_blockSize)
	#----------------------------------------------------------------------
	def get_command(self):
		"""
		
				Specifies the procedure or script to run, in order to obtain the
				desired information. This must return a value or an array of values.
				A warning will be displayed if the command does not return a value.
				This flag MUST always be accompanied by a trigger flag (eg. a condition flag,
				an event flag, an attachToRefresh flag, etc.).
				
		"""
		return self.query(command=True)
	#----------------------------------------------------------------------
	def set_command(self, value):
		"""
		
				Specifies the procedure or script to run, in order to obtain the
				desired information. This must return a value or an array of values.
				A warning will be displayed if the command does not return a value.
				This flag MUST always be accompanied by a trigger flag (eg. a condition flag,
				an event flag, an attachToRefresh flag, etc.).
				
		"""
		self.edit(command=value)
	#----------------------------------------------------------------------
	command = property(get_command, set_command)
	#----------------------------------------------------------------------
	def conditionChange(self,value):
		"""
		
				A trigger which runs the command (to sample the data), when the
				named condition changes. The named condition must be pre-defined or a
				user defined boolean. To get a list of what conditions exist, use
				the -lc/listConditions flag.
				
		"""
		self.edit(conditionChange=value)
	#----------------------------------------------------------------------
	def conditionFalse(self,value):
		"""
		
				A trigger which runs the command (to sample the data), when the
				named condition becomes false. The named condition must be pre-defined or
				a user defined boolean. To get a list of what conditions exist, use
				the -lc/listConditions flag.
				
		"""
		self.edit(conditionFalse=value)
	#----------------------------------------------------------------------
	def conditionTrue(self,value):
		"""
		
				A trigger which runs the command (to sample the data), when the
				named condition becomes true. The named condition must be pre-defined or a
				user defined boolean. To get a list of what conditions exist, use
				the -lc/listConditions flag.
				
		"""
		self.edit(conditionTrue=value)
	#----------------------------------------------------------------------
	def connectionChange(self,value):
		"""
		
				Runs the command when the named attribute changes its connectivity. The
				string must identify both the dependency node and the particular attribute.
				If the dependency node is deleted, this HUD is removed (even if the deletion
				is undoable).
				
		"""
		self.edit(connectionChange=value)
	#----------------------------------------------------------------------
	def get_dataAlignment(self):
		"""
		
				Specifies the alignment of the data blocks and the data text, within a HUD block.
				Available alignments are: "left" and "right". The default alignment is "left".
				
		"""
		return self.query(dataAlignment=True)
	#----------------------------------------------------------------------
	def set_dataAlignment(self, value):
		"""
		
				Specifies the alignment of the data blocks and the data text, within a HUD block.
				Available alignments are: "left" and "right". The default alignment is "left".
				
		"""
		self.edit(dataAlignment=value)
	#----------------------------------------------------------------------
	dataAlignment = property(get_dataAlignment, set_dataAlignment)
	#----------------------------------------------------------------------
	def get_dataFontSize(self):
		"""
		
				Sets the font size of the returned data. Available sizes are: small and large.
				
		"""
		return self.query(dataFontSize=True)
	#----------------------------------------------------------------------
	def set_dataFontSize(self, value):
		"""
		
				Sets the font size of the returned data. Available sizes are: small and large.
				
		"""
		self.edit(dataFontSize=value)
	#----------------------------------------------------------------------
	dataFontSize = property(get_dataFontSize, set_dataFontSize)
	#----------------------------------------------------------------------
	def get_dataWidth(self):
		"""
		
				Specifies the pixel width of the virtual "textbox" which will hold a data value.
				For commands which return more than one value (ie. arrays), one of these "textboxes"
				will be created for each data element, each with this specified width. If the width
				of the data value exceeds the width of the "textbox", the data value will be
				truncated to fit within the dimensions of the "textbox." (To see a layout of a
				block, see the description of the -block flag.)
				
		"""
		return self.query(dataWidth=True)
	#----------------------------------------------------------------------
	def set_dataWidth(self, value):
		"""
		
				Specifies the pixel width of the virtual "textbox" which will hold a data value.
				For commands which return more than one value (ie. arrays), one of these "textboxes"
				will be created for each data element, each with this specified width. If the width
				of the data value exceeds the width of the "textbox", the data value will be
				truncated to fit within the dimensions of the "textbox." (To see a layout of a
				block, see the description of the -block flag.)
				
		"""
		self.edit(dataWidth=value)
	#----------------------------------------------------------------------
	dataWidth = property(get_dataWidth, set_dataWidth)
	#----------------------------------------------------------------------
	def get_decimalPrecision(self):
		"""
		
				Sets the decimal precision of any floating point value returned by the command. The valid
				range of precision values are 1 to 8.
				
		"""
		return self.query(decimalPrecision=True)
	#----------------------------------------------------------------------
	def set_decimalPrecision(self, value):
		"""
		
				Sets the decimal precision of any floating point value returned by the command. The valid
				range of precision values are 1 to 8.
				
		"""
		self.edit(decimalPrecision=value)
	#----------------------------------------------------------------------
	decimalPrecision = property(get_decimalPrecision, set_decimalPrecision)
	#----------------------------------------------------------------------
	def disregardIndex(self,value):
		"""
		
				This flag can only be used in conjunction with the -ac/attributeChange
				flag. If it is specified, and the HUD is attached to a multi (indexed)
				attribute, then the HUD command will run no matter which attribute in
				the multi changes.
				
		"""
		self.edit(disregardIndex=value)
	#----------------------------------------------------------------------
	def event(self,value):
		"""
		
				Runs the command when the named event occurs. The named event, must be a
				pre-defined Maya event. To get a list of what events exist, use the
				-le/listEvents flag.
				
		"""
		self.edit(event=value)
	#----------------------------------------------------------------------
	@property
	def exists(self):
		"""
		
				This flag returns whether the given object exists in the Heads-Up Display layout.
				An object name must be supplied with this command. This flag cannot be combined
				with any other flag.
				
		"""
		return self.query(exists=True)
	#----------------------------------------------------------------------
	@property
	def getOption(self):
		"""
		
				This flag will return the value of the option specified by the string.
				See setOption for a list of options
							In query mode, this flag needs a value.
				
		"""
		return self.query(getOption=True)
	#----------------------------------------------------------------------
	def get_gridColor(self):
		"""
		
				This flag specifies a color for the grid lines using the inactive color palette. Specifying
				an index number between 1 to 23 will select the corresponding color in the palette.
				
		"""
		return self.query(gridColor=True)
	#----------------------------------------------------------------------
	def set_gridColor(self, value):
		"""
		
				This flag specifies a color for the grid lines using the inactive color palette. Specifying
				an index number between 1 to 23 will select the corresponding color in the palette.
				
		"""
		self.edit(gridColor=value)
	#----------------------------------------------------------------------
	gridColor = property(get_gridColor, set_gridColor)
	#----------------------------------------------------------------------
	def get_label(self):
		"""
		
				Text string that appears to the left of the desired information.
				
		"""
		return self.query(label=True)
	#----------------------------------------------------------------------
	def set_label(self, value):
		"""
		
				Text string that appears to the left of the desired information.
				
		"""
		self.edit(label=value)
	#----------------------------------------------------------------------
	label = property(get_label, set_label)
	#----------------------------------------------------------------------
	def get_labelFontSize(self):
		"""
		
				Sets the font size of the label. Available sizes are: small and large.
				
		"""
		return self.query(labelFontSize=True)
	#----------------------------------------------------------------------
	def set_labelFontSize(self, value):
		"""
		
				Sets the font size of the label. Available sizes are: small and large.
				
		"""
		self.edit(labelFontSize=value)
	#----------------------------------------------------------------------
	labelFontSize = property(get_labelFontSize, set_labelFontSize)
	#----------------------------------------------------------------------
	def get_labelWidth(self):
		"""
		
				Specifies the pixel width of the virtual "textbox" which will hold the label. The
				contents of this "textbox" will be left justified. If the width of the actual label
				exceeds the width of the "textbox," the label will be truncated to fit within the
				dimensions of the "textbox." (To see a layout of a block, see the description
				of the -block flag.)
				
		"""
		return self.query(labelWidth=True)
	#----------------------------------------------------------------------
	def set_labelWidth(self, value):
		"""
		
				Specifies the pixel width of the virtual "textbox" which will hold the label. The
				contents of this "textbox" will be left justified. If the width of the actual label
				exceeds the width of the "textbox," the label will be truncated to fit within the
				dimensions of the "textbox." (To see a layout of a block, see the description
				of the -block flag.)
				
		"""
		self.edit(labelWidth=value)
	#----------------------------------------------------------------------
	labelWidth = property(get_labelWidth, set_labelWidth)
	#----------------------------------------------------------------------
	def get_layoutVisibility(self):
		"""
		
				Sets the visibility of Heads-Up Display layout on and off. This does not
				modify individual visibilities of heads-up displays, but turns off the layout
				so that no heads-up displays will draw to screen. Personalized settings for
				the visibilities of HUDs are kept safe. This flag can only be used by itself,
				excepting edit and query.
				
		"""
		return self.query(layoutVisibility=True)
	#----------------------------------------------------------------------
	def set_layoutVisibility(self, value):
		"""
		
				Sets the visibility of Heads-Up Display layout on and off. This does not
				modify individual visibilities of heads-up displays, but turns off the layout
				so that no heads-up displays will draw to screen. Personalized settings for
				the visibilities of HUDs are kept safe. This flag can only be used by itself,
				excepting edit and query.
				
		"""
		self.edit(layoutVisibility=value)
	#----------------------------------------------------------------------
	layoutVisibility = property(get_layoutVisibility, set_layoutVisibility)
	#----------------------------------------------------------------------
	@property
	def listConditions(self):
		"""
		
				This flag will return a string array containing all names of the available
				conditions.
				
		"""
		return self.query(listConditions=True)
	#----------------------------------------------------------------------
	@property
	def listEvents(self):
		"""
		
				This flag will return a string array containing all names of the available
				events.
				
		"""
		return self.query(listEvents=True)
	#----------------------------------------------------------------------
	@property
	def listHeadsUpDisplays(self):
		"""
		
				This flag will return a string array containing all names of existing HUDs.
				
		"""
		return self.query(listHeadsUpDisplays=True)
	#----------------------------------------------------------------------
	@property
	def listNodeChanges(self):
		"""
		
				This flag will return a string array containing all names of the available
				node changes.
				
		"""
		return self.query(listNodeChanges=True)
	#----------------------------------------------------------------------
	@property
	def listPresets(self):
		"""
		
				This flag will return a string array containing all names of the available
				preset HUDs.
				
		"""
		return self.query(listPresets=True)
	#----------------------------------------------------------------------
	def name(self,value):
		"""
		
				This flag only permits the EDITING of the name of the Heads-Up Display.
				
		"""
		self.edit(name=value)
	#----------------------------------------------------------------------
	def get_nodeChanges(self):
		"""
		
				Works only with selection based triggers (ie. "SelectionChanged" or "SomethingSelected"),
				otherwise this flag is ignored. This flag attaches the HUD script to execute on specific
				node changes of any selected node. This flag is used to set a nodeChange. In order to
				reset a nodeChange, use the -rnc/resetNodeChanges flag. To view a list of all available
				node changes, use the -lnc/listNodeChanges flag. The following is a list of available node
				changes and their function:
				
				attributeChange:  The script will be sensitive to any attribute changes in the currently
				                  selected nodes.
				
				connectionChange: The script will be sensitive to any connection changes in the currently
				                  selected nodes.
				
				instanceChange:   The script will be sensitive to any changes to an instance in the
				                  currently selected nodes.
				
				
				On query mode, this flag will return the values of all nodeChanges in pairs of values
				(the name of the nodeChange followed by its value).
				
				WARNING: (Performance Warning)
				         Attaching a nodeChange trigger to a selection based trigger can cause a large
				         performance drop, if the node change that is being watched is caused by the
				         HUD script itself.
				
				         With this said, an attempt should be made to keep the HUD command/script
				                 simple and limited to retrieving data. Changing an attribute, creating or
				                 modifying a connection or instance will all result in a performance drop.
				
		"""
		return self.query(nodeChanges=True)
	#----------------------------------------------------------------------
	def set_nodeChanges(self, value):
		"""
		
				Works only with selection based triggers (ie. "SelectionChanged" or "SomethingSelected"),
				otherwise this flag is ignored. This flag attaches the HUD script to execute on specific
				node changes of any selected node. This flag is used to set a nodeChange. In order to
				reset a nodeChange, use the -rnc/resetNodeChanges flag. To view a list of all available
				node changes, use the -lnc/listNodeChanges flag. The following is a list of available node
				changes and their function:
				
				attributeChange:  The script will be sensitive to any attribute changes in the currently
				                  selected nodes.
				
				connectionChange: The script will be sensitive to any connection changes in the currently
				                  selected nodes.
				
				instanceChange:   The script will be sensitive to any changes to an instance in the
				                  currently selected nodes.
				
				
				On query mode, this flag will return the values of all nodeChanges in pairs of values
				(the name of the nodeChange followed by its value).
				
				WARNING: (Performance Warning)
				         Attaching a nodeChange trigger to a selection based trigger can cause a large
				         performance drop, if the node change that is being watched is caused by the
				         HUD script itself.
				
				         With this said, an attempt should be made to keep the HUD command/script
				                 simple and limited to retrieving data. Changing an attribute, creating or
				                 modifying a connection or instance will all result in a performance drop.
				
		"""
		self.edit(nodeChanges=value)
	#----------------------------------------------------------------------
	nodeChanges = property(get_nodeChanges, set_nodeChanges)
	#----------------------------------------------------------------------
	def get_padding(self):
		"""
		
				Specifies the width of both the left and right margins of a block. Default
				value is 15 pixels.
				
		"""
		return self.query(padding=True)
	#----------------------------------------------------------------------
	def set_padding(self, value):
		"""
		
				Specifies the width of both the left and right margins of a block. Default
				value is 15 pixels.
				
		"""
		self.edit(padding=value)
	#----------------------------------------------------------------------
	padding = property(get_padding, set_padding)
	#----------------------------------------------------------------------
	def get_preset(self):
		"""
		
				This setting is used to select certain pre-defined HUDs, some of which retrieve
				specific data, that is unobtainable through normal MEL commands or scripts. This flag
				is mutually exclusive from the command and trigger flag combination. However, presets
				can work with all other headsUpDisplay attribute flags (ie. block alignment, label,
				dataFontSize, etc.), unless otherwise specified below. To obtain a list
				of available presets, use the -lp/listPresets flag on this command.
				
				The following is a list of available presets and a description of each:
				
				cameraNames
				This will return the camera name that the view is looking through, in
				the data block, for each view that the HUD is drawing to.
				polyVerts
				This will return three values in the data block, regarding the number of
				vertices that are visible by the camera.
				
				1st Value: Represents the number of camera visible vertices, both
				active and inactive.
				2nd Value: Represents the number of camera visible vertices, on
				active objects only.
				3rd Value: Represents the number of camera visible vertices, that
				are active.
				
				polyEdges
				This will return three values in the data block, regarding the number of
				edges that are visible by the camera. The order of these three values are
				similar to the polyVerts preset.
				polyFaces
				This will return three values in the data block, regarding the number of
				faces that are visible by the camera. The order of these three values are
				similar to the polyVerts preset.
				polyUVs
				This will return three values in the data block, regarding the number of
				UVs that are visible by the camera. The order of these three values are
				similar to the polyVerts preset.
				polyTriangles
				This will return three values in the data block, regarding the number of
				triangles that are visible by the camera. The order of these three values are
				similar to the polyVerts preset.
				materialLoadingCount
				This will return the material loading count.
				It updates on each refresh.
				textureLoadingCount
				This will return the texture loading count.
				It updates on each refresh.
				frameRate
				This will return a single string carrying both the frame rate and the "fps"
				string in the data block. It updates on each refresh.
				viewAxis
				This will draw the orientation of the grid axes within the HUD. It updates
				on each refresh. While this preset can take in all attribute flags, the
				only one which will have an effect are block attribute related flags
				(ie. block alignment and block size). The block dimensions of this preset
				are: blockSize - "large" and blockWidth - "50", which results in a 50x50
				pixel region.
				distanceFromCamera
				This will return in the data block the distance from the view's camera
				to the centre of the bounding box containing the selected objects in the view.
				
		"""
		return self.query(preset=True)
	#----------------------------------------------------------------------
	def set_preset(self, value):
		"""
		
				This setting is used to select certain pre-defined HUDs, some of which retrieve
				specific data, that is unobtainable through normal MEL commands or scripts. This flag
				is mutually exclusive from the command and trigger flag combination. However, presets
				can work with all other headsUpDisplay attribute flags (ie. block alignment, label,
				dataFontSize, etc.), unless otherwise specified below. To obtain a list
				of available presets, use the -lp/listPresets flag on this command.
				
				The following is a list of available presets and a description of each:
				
				cameraNames
				This will return the camera name that the view is looking through, in
				the data block, for each view that the HUD is drawing to.
				polyVerts
				This will return three values in the data block, regarding the number of
				vertices that are visible by the camera.
				
				1st Value: Represents the number of camera visible vertices, both
				active and inactive.
				2nd Value: Represents the number of camera visible vertices, on
				active objects only.
				3rd Value: Represents the number of camera visible vertices, that
				are active.
				
				polyEdges
				This will return three values in the data block, regarding the number of
				edges that are visible by the camera. The order of these three values are
				similar to the polyVerts preset.
				polyFaces
				This will return three values in the data block, regarding the number of
				faces that are visible by the camera. The order of these three values are
				similar to the polyVerts preset.
				polyUVs
				This will return three values in the data block, regarding the number of
				UVs that are visible by the camera. The order of these three values are
				similar to the polyVerts preset.
				polyTriangles
				This will return three values in the data block, regarding the number of
				triangles that are visible by the camera. The order of these three values are
				similar to the polyVerts preset.
				materialLoadingCount
				This will return the material loading count.
				It updates on each refresh.
				textureLoadingCount
				This will return the texture loading count.
				It updates on each refresh.
				frameRate
				This will return a single string carrying both the frame rate and the "fps"
				string in the data block. It updates on each refresh.
				viewAxis
				This will draw the orientation of the grid axes within the HUD. It updates
				on each refresh. While this preset can take in all attribute flags, the
				only one which will have an effect are block attribute related flags
				(ie. block alignment and block size). The block dimensions of this preset
				are: blockSize - "large" and blockWidth - "50", which results in a 50x50
				pixel region.
				distanceFromCamera
				This will return in the data block the distance from the view's camera
				to the centre of the bounding box containing the selected objects in the view.
				
		"""
		self.edit(preset=value)
	#----------------------------------------------------------------------
	preset = property(get_preset, set_preset)
	#----------------------------------------------------------------------
	def remove(self,value):
		"""
		
				This command will remove a given HUD object, given a specified HUD name. This flag will
				override all other flags and is mutually exclusive from the other remove flags.
				
		"""
		self.edit(remove=value)
	#----------------------------------------------------------------------
	def removeID(self,value):
		"""
		
				This command will remove a given HUD object, given a specified HUD ID number assigned
				to it at creation time. This flag will override all other flags and is mutually exclusive
				from the other remove flags.
				
		"""
		self.edit(removeID=value)
	#----------------------------------------------------------------------
	def removePosition(self,value):
		"""
		
				This command will remove the contents of a specific block location in the HUD layout.
				This flag will override all other flags and is mutually exclusive from the other remove
				flags. Syntax for this flag is: -removePosition/rp [section] [block].
				
		"""
		self.edit(removePosition=value)
	#----------------------------------------------------------------------
	def resetNodeChanges(self,value):
		"""
		
				This flag will reset a specificied nodeChange back to false. This flag only operates under
				the edit flag. See the description for the -nc/nodeChanges flag for further details.
				
		"""
		self.edit(resetNodeChanges=value)
	#----------------------------------------------------------------------
	@property
	def scriptResult(self):
		"""
		
				This flag is only used in conjunction with the query flag. Calling a query on this flag
				returns the most recent result of the HUD.
				
		"""
		return self.query(scriptResult=True)
	#----------------------------------------------------------------------
	def get_section(self):
		"""
		
				Defines the section the HUD will appear in. There are 10 sections
				divided across the screen. Five columns and two rows make up the
				ten element matrix which divide the main viewport. Here is a visual
				layout of the sections.
				
				 ________________________
				|    |    |    |    |    |
				|    |    |    |    |    |
				| 0  | 1  | 2  | 3  | 4  |
				|    |    |    |    |    |
				|____|____|____|____|____|
				|    |    |    |    |    |
				|    |    |    |    |    |
				| 5  | 6  | 7  | 8  | 9  |
				|    |    |    |    |    |
				|____|____|____|____|____|
				Each section is denoted by a number from 0 to 9 as illustrated above.
				For example, if the second column of the top row was desired, the
				section would be defined as: -sec 1
				
				To prevent HUD objects from displaying over each other and causing a
				clutter of letters, each row has a defined visibility precedence,
				where each section would have a visibility priority level. Depending
				on each priority level, when the screen space begins to shrink to
				a point where the section widths of a given row begin to collide, the
				HUD automatically compensates for this by removing the sections of
				least priority. These sections are made invisible and a warning is
				issued to inform the user of the removal. This continues until only
				the section of highest priority remains.
				
				For each row, the priorities are defined as follows. Using the top
				row as an example: Section 0, has the highest priority, followed
				by Section 4, making the outermost sections of highest priority.
				Next in the list is Section 2, and lastly Sections 1 and 3 are of
				the equal and least priority. This priority structure can be applied
				to the bottom row as well. The two outermost sections have the highest
				priority, followed by the middle section, and finally the remaining
				two sections are of lowest priority.
				
				This means that as the viewport gradually decreases in width
				to the point where sections in the top row begin to overlap, sections
				1 and 3 will be removed from view first, followed by section 2, and
				finally section 4. A similar note is provided below for the block layout.
				
		"""
		return self.query(section=True)
	#----------------------------------------------------------------------
	def set_section(self, value):
		"""
		
				Defines the section the HUD will appear in. There are 10 sections
				divided across the screen. Five columns and two rows make up the
				ten element matrix which divide the main viewport. Here is a visual
				layout of the sections.
				
				 ________________________
				|    |    |    |    |    |
				|    |    |    |    |    |
				| 0  | 1  | 2  | 3  | 4  |
				|    |    |    |    |    |
				|____|____|____|____|____|
				|    |    |    |    |    |
				|    |    |    |    |    |
				| 5  | 6  | 7  | 8  | 9  |
				|    |    |    |    |    |
				|____|____|____|____|____|
				Each section is denoted by a number from 0 to 9 as illustrated above.
				For example, if the second column of the top row was desired, the
				section would be defined as: -sec 1
				
				To prevent HUD objects from displaying over each other and causing a
				clutter of letters, each row has a defined visibility precedence,
				where each section would have a visibility priority level. Depending
				on each priority level, when the screen space begins to shrink to
				a point where the section widths of a given row begin to collide, the
				HUD automatically compensates for this by removing the sections of
				least priority. These sections are made invisible and a warning is
				issued to inform the user of the removal. This continues until only
				the section of highest priority remains.
				
				For each row, the priorities are defined as follows. Using the top
				row as an example: Section 0, has the highest priority, followed
				by Section 4, making the outermost sections of highest priority.
				Next in the list is Section 2, and lastly Sections 1 and 3 are of
				the equal and least priority. This priority structure can be applied
				to the bottom row as well. The two outermost sections have the highest
				priority, followed by the middle section, and finally the remaining
				two sections are of lowest priority.
				
				This means that as the viewport gradually decreases in width
				to the point where sections in the top row begin to overlap, sections
				1 and 3 will be removed from view first, followed by section 2, and
				finally section 4. A similar note is provided below for the block layout.
				
		"""
		self.edit(section=value)
	#----------------------------------------------------------------------
	section = property(get_section, set_section)
	#----------------------------------------------------------------------
	def setOption(self,value):
		"""
		
				This flag will edit the option specified by the first string. Current options are:
				smpPolyCount - "cage" or "smp" - in smooth mesh preview, determines the poly count display
				
		"""
		self.edit(setOption=value)
	#----------------------------------------------------------------------
	def get_showGrid(self):
		"""
		
				This flag will toggle the display of the grid lines of the HUD layout.
				
		"""
		return self.query(showGrid=True)
	#----------------------------------------------------------------------
	def set_showGrid(self, value):
		"""
		
				This flag will toggle the display of the grid lines of the HUD layout.
				
		"""
		self.edit(showGrid=value)
	#----------------------------------------------------------------------
	showGrid = property(get_showGrid, set_showGrid)
	#----------------------------------------------------------------------
	def get_visible(self):
		"""
		
				Sets the visibility of the Heads-Up Display on and off.
				
		"""
		return self.query(visible=True)
	#----------------------------------------------------------------------
	def set_visible(self, value):
		"""
		
				Sets the visibility of the Heads-Up Display on and off.
				
		"""
		self.edit(visible=value)
	#----------------------------------------------------------------------
	visible = property(get_visible, set_visible)