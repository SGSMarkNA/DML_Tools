

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class HudButton(UI_Object.UI):
	"""
	This command creates a Heads-up Display (HUD) button control which is placed in
	a 2D inactive overlay plane on the 3D viewport. It is to be used to provide hands-on
	interaction designated by a user script. The HUD button is derived from
	a generic HUD object and thus inherits a similar workflow.
	
	Although this command provides much of the same functionality as the headsUpDisplay
	command, it does not provide headsUpDisplay layout controls such as layoutVisibility,
	nextFreeBlock, lastOccupiedBlock, exists, remove, etc. To access that functionality,
	please use the headsUpDisplay command. This command is focused solely around the creation
	and management of HUD button controls. Similarly, all operations performed by
	this command are limited to HUDs that are button controls.
	
	The only mandatory flags, on creation are the section and block flags.
	
	Like the headsUpDisplay command, upon creation of a HUD button, an ID number
	will be assigned to it. This can be used to remove the HUD via the headsUpDisplay
	command (-rid/removeID [int IDNumber]), if desired. Alternatively, the headsUpDisplay
	command can remove HUD objects via their position (section and block),
	or their unique name.
		  
	      hud, headsupdisplay, button, hudbutton
	"""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.hudButton(**kwargs)
			super(HudButton, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.hudButton(name, exists=True):
				super(HudButton, self).__init__(name)
			else:
				name = cmds.hudButton(name, **kwargs)
				super(HudButton, self).__init__(name, **dict(qtParent=parent))
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
	def get_block(self):
		"""
		
				Denotes the individual block that the HUD will reside in, within a
				section. Each section is composed of a single column of blocks.
				The total number of blocks contained within each section is variable.
				
				The number of blocks that will be visible within each section is
				dependent on the size of blocks contained in each section and the
				current size of the window. Blocks begin enumerating from 0 and
				flexibly increase based on need.
				
				For HUD buttons, the format differs from that of the standard HUD.
				The layout using parameters defined by the formatting flags listed
				below (eg. justify, padding, buttonWidth) is shown below:
				
				 __________________________________
				|     |     |          |     |     |
				|  P  |  J  |  Button  |  J  |  P  |
				|_____|_____|__________|_____|_____|
				P = Sub-block of width, padding
				J = Justification of the entire block
				Button = Sub-block of width, buttonWidth
				
				
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
				
				For HUD buttons, the format differs from that of the standard HUD.
				The layout using parameters defined by the formatting flags listed
				below (eg. justify, padding, buttonWidth) is shown below:
				
				 __________________________________
				|     |     |          |     |     |
				|  P  |  J  |  Button  |  J  |  P  |
				|_____|_____|__________|_____|_____|
				P = Sub-block of width, padding
				J = Justification of the entire block
				Button = Sub-block of width, buttonWidth
				
				
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
	def get_buttonShape(self):
		"""
		
				Specifies the shape of the button. Available button shapes are:
				"rectangle" and "roundRectangle". The first will draw a rectangular
				button, while the latter is a rectangle with rounded edges.
				
		"""
		return self.query(buttonShape=True)
	#----------------------------------------------------------------------
	def set_buttonShape(self, value):
		"""
		
				Specifies the shape of the button. Available button shapes are:
				"rectangle" and "roundRectangle". The first will draw a rectangular
				button, while the latter is a rectangle with rounded edges.
				
		"""
		self.edit(buttonShape=value)
	#----------------------------------------------------------------------
	buttonShape = property(get_buttonShape, set_buttonShape)
	#----------------------------------------------------------------------
	def get_buttonWidth(self):
		"""
		
				Specifies the width of the button.
				
		"""
		return self.query(buttonWidth=True)
	#----------------------------------------------------------------------
	def set_buttonWidth(self, value):
		"""
		
				Specifies the width of the button.
				
		"""
		self.edit(buttonWidth=value)
	#----------------------------------------------------------------------
	buttonWidth = property(get_buttonWidth, set_buttonWidth)
	#----------------------------------------------------------------------
	def get_label(self):
		"""
		
				Text label of the HUD button.
				
		"""
		return self.query(label=True)
	#----------------------------------------------------------------------
	def set_label(self, value):
		"""
		
				Text label of the HUD button.
				
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
	def get_pressCommand(self):
		"""
		
				Specifies the procedure or script to run during a mouse click event.
				
		"""
		return self.query(pressCommand=True)
	#----------------------------------------------------------------------
	def set_pressCommand(self, value):
		"""
		
				Specifies the procedure or script to run during a mouse click event.
				
		"""
		self.edit(pressCommand=value)
	#----------------------------------------------------------------------
	pressCommand = property(get_pressCommand, set_pressCommand)
	#----------------------------------------------------------------------
	def get_releaseCommand(self):
		"""
		
				Specifies the procedure or script to run during a mouse release event.
				
		"""
		return self.query(releaseCommand=True)
	#----------------------------------------------------------------------
	def set_releaseCommand(self, value):
		"""
		
				Specifies the procedure or script to run during a mouse release event.
				
		"""
		self.edit(releaseCommand=value)
	#----------------------------------------------------------------------
	releaseCommand = property(get_releaseCommand, set_releaseCommand)
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