import nuke
import DML_Tools
import DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Generic_Widgets_Nodes
DML_Nuke = DML_Tools.DML_Nuke

#----------------------------------------------------------------------
def is_Single_Frame_Comp():
	""""""
	root = nuke.root()
	first_frame,last_frame = root.knob("first_frame").value(),root.knob("last_frame").value()
	if first_frame == last_frame:
		return True
	else:
		return False

################################################################################
class DML_Layer_Order_Builder(DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Generic_Widgets_Nodes.Layer_Order_Output_Builder_Node):
	NODE_TYPE_RELATION  = "DML_Layer_Order_Builder"
	
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		""""""
		DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Generic_Widgets_Nodes.Layer_Order_Output_Builder_Node.__init__(self,*args,**kwargs)
		self._write_node = None
		if not self.hasKnob("dml_backdrop_link"):
			self._backdrop_link_knob = nuke.Link_Knob("dml_backdrop_link")
			self.addKnob(self._backdrop_link_knob)
			user_knob = self.knob("User")
			user_knob.setFlag(nuke.INVISIBLE)
		else:
			self._backdrop_link_knob = self.nuke_object.knobs()["dml_backdrop_link"]
			
	#----------------------------------------------------------------------
	@property
	def write_node(self):
		""""""
		if self._write_node is None:
			scan = self.find_Down_Stream_Nodes(matchclass="Write")
			if len(scan):
				self._write_node = scan[0]
		return self._write_node
	
	#----------------------------------------------------------------------
	def _update_Write_Node_File_Path(self):
		if not self.write_node == None:
			folder    = "[value {}.dml_folder_destination]".format(self.name)
			name      = "[value {}.dml_file_name]".format(self.name)
			if is_Single_Frame_Comp():
				padding   = ""
			else:
				padding   = "_%0[value {}.dml_frame_padding]d".format(self.name)
			file_type = self.write_node.knob("file_type").value()
			value     = '{}/{}{}.{}'.format(folder,name,padding,file_type)
			self.write_node.knob("file").setText(value)
	
	def create_Client_Approval_Setup(self, layer_order=[]):
		res = None
		start_node = self
		with nuke.Undo():
			try:
				layer_order = list(reversed(self.imbeded_data_layer_order))
				# convert the input node into a DML Nuke Node
				#start_node = DML_Nuke.Decorators.Node_Wraper_Manager.to_DML_Node(start_node)
				# set the node to be the only thing selected
				start_node.selectOnly()
				# get the layers for this node
				node_layers      = start_node.layers
				# Check if a layer order was given
				# if so collect only the layers that exist in the input nodes layers
				# using the layer order that was requested
				# if not then just set the node layers to the createion_layers
				createion_layers = [layer for layer in layer_order if layer in node_layers] if len(layer_order) else node_layers
				
				# get the name of the backdrop node that will be created
				backdrop_name = start_node.name + "_Client_Approval_BKDRP"
				
				# get the write node name that will be created
				#write_node_name = start_node.name+"_Client_Approval_Write"
				
				master_xpos = start_node.x + 200
				master_ypos = start_node.y
				old_back_drop_pos = []
				# Check If The backdrop node exists if so then delete it along with all the nodes in it
				if self._backdrop_link_knob.getLink() != None and nuke.exists(self._backdrop_link_knob.getLink()) or nuke.exists(backdrop_name):
					if self._backdrop_link_knob.getLink() != None and nuke.exists(self._backdrop_link_knob.getLink()):
						backdrop_name = self._backdrop_link_knob.getLink()
						backdrop_name = backdrop_name.replace("."+backdrop_name.split(".")[-1],"")
						bd=DML_Nuke.Nuke_Nodes.Standered_Nodes.BackdropNode(backdrop_name)
					elif nuke.exists(backdrop_name):
						bd=DML_Nuke.Nuke_Nodes.Standered_Nodes.BackdropNode(backdrop_name)
					master_xpos = bd.x + 200
					master_ypos = bd.y
					old_back_drop_pos = [bd.x,bd.y]
					if bd.nuke_object.Class()=="BackdropNode":
						bd.delete(includeContents=True)
				
				shuffle_nodes = DML_Nuke.Nuke_Nodes.Node_List()
				# this will collect all the node that the backdrow will be created around 
				nodes_for_backdrop_createion = DML_Nuke.Nuke_Nodes.Node_List()
				
				last_created_shuffle = None
				last_created_merge   = None
				views_expression = "input."
				# scan over each layer and create the nodes
				for index,layer in enumerate(createion_layers):
					# create the shuffle node
					shuffle_node = DML_Nuke.Nuke_Nodes.Standered_Nodes.Shuffle(**{"in":layer, "out":"rgba", "xpos":master_xpos + (150 * index), "ypos":master_ypos,"label":"[value in ]"})
					nodes_for_backdrop_createion.append(shuffle_node)
					views_expression += "input."
					if index == 0 :
						shuffle_node.setInput(0,start_node)
					else:
						shuffle_node.setInput(0,last_created_shuffle)
						merge_node = DML_Nuke.dml.to_DML_Node( nuke.nodes.PSDMerge(xpos=master_xpos, ypos=master_ypos + (100 * index),label="[value input1.in]") )
						
						if index == 1 :
							merge_node.setInput(1,shuffle_node)
							merge_node.setInput(0,last_created_shuffle)
						else:
							merge_node.setInput(1,shuffle_node)
							merge_node.setInput(0,last_created_merge)
						last_created_merge = merge_node
						nodes_for_backdrop_createion.append(merge_node)
					
					shuffle_nodes.append(shuffle_node)
					last_created_shuffle = shuffle_node
					
				views_expression += "DML_Nuke_View_Selection"
				w=DML_Nuke.Nuke_Nodes.Standered_Nodes.Write(xpos=master_xpos,
															ypos=master_ypos + ( 100 * len(shuffle_nodes)),
															name=start_node.name+"_Client_Approval_Write",
															colorspace="sRGB",
															file_type="png",
															create_directories=True,
															channels="rgb")
				w.setInput(0,last_created_merge)
				
				w.knob("views").setExpression(views_expression)
				nodes_for_backdrop_createion.append(w)
				w.selectOnly()
				if "ICC_knob" in w.knobs():
					w.knob("ICC_knob").setValue('sRGB.icc')
				
				text_node = DML_Nuke.dml.to_DML_Node(nuke.createNode("Text",'message "[value [value input.name].file]" xjustify left yjustify baseline size 20 box "0 0 0 0" translate "10 50" Transform 1',False))
				text_node.y = text_node.y + 50
				nodes_for_backdrop_createion.append(text_node)
				bd = DML_Nuke.Nuke_Nodes.Standered_Nodes.BackdropNode(name=backdrop_name,
																 label="Render Flattened Images\nfor Client Approval",
																 note_font_size=25,
																 note_font_color=255,
																 note_font='Verdana Bold',
																 post_kwargs=dict(nodes=nodes_for_backdrop_createion))
				self._backdrop_link_knob.setLink(bd.knob("name").fullName)
				if len(old_back_drop_pos):
					bd.Move(*old_back_drop_pos)
				res = w
				self._write_node = w
				self._update_Write_Node_File_Path()
			except:
				nuke.message("Something went wrong")
		return res