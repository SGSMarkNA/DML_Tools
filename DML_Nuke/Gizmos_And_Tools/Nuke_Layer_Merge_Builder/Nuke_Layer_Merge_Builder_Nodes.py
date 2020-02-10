import nuke
import DML_Tools
import DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Generic_Widgets_Nodes
DML_Nuke = DML_Tools.DML_Nuke

################################################################################
class DML_Layer_Order_Builder(DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Generic_Widgets_Nodes.Layer_Order_Output_Builder_Node):
	NODE_TYPE_RELATION  = "DML_Layer_Order_Builder"
	
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		""""""
		DML_Tools.DML_Nuke.Nuke_GUI.Generic_Widgets.Generic_Widgets_Nodes.Layer_Order_Output_Builder_Node.__init__(self,*args,**kwargs)
		self._write_node = None
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
			padding   = "%0[value {}.dml_frame_padding]".format(self.name)
			file_type = self.write_node.knob("file_type").value()
			value     = '{}/{}{}d.{}'.format(folder,name,padding,file_type)
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
				
				# Check If The backdrop node exists if so then delete it along with all the nodes in it
				if nuke.exists(backdrop_name):
					bd=DML_Nuke.Nuke_Nodes.Standered_Nodes.BackdropNode(backdrop_name)
					if bd.nuke_object.Class()=="BackdropNode":
						bd.delete(includeContents=True)
				
				shuffle_nodes = DML_Nuke.Nuke_Nodes.Node_List()
				# this will collect all the node that the backdrow will be created around 
				nodes_for_backdrop_createion = DML_Nuke.Nuke_Nodes.Node_List()
				
				last_created_shuffle = None
				last_created_merge   = None
				
				# scan over each layer and create the nodes
				for index,layer in enumerate(createion_layers):
					# create the shuffle node
					shuffle_node = DML_Nuke.Nuke_Nodes.Standered_Nodes.Shuffle(**{"in":layer, "out":"rgba", "xpos":master_xpos + (150 * index), "ypos":master_ypos,"label":"[value in ]"})
					nodes_for_backdrop_createion.append(shuffle_node)
					
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
			
		
				w=DML_Nuke.Nuke_Nodes.Standered_Nodes.Write(xpos=master_xpos,
															ypos=master_ypos + ( 100 * len(shuffle_nodes)),
															name=start_node.name+"_Client_Approval_Write",
															colorspace="sRGB",
															file_type="png",
															create_directories=True,
															channels="rgb")
				w.setInput(0,last_created_merge)
				nodes_for_backdrop_createion.append(w)
				w.selectOnly()
				if "ICC_knob" in w.knobs():
					w.knob("ICC_knob").setValue('sRGB.icc')
				
				text_node = DML_Nuke.dml.to_DML_Node(nuke.createNode("Text",'message "[value [value input.name].file]" xjustify left yjustify baseline size 20 box "0 0 0 0" translate "10 50" Transform 1',False))
				text_node.y = text_node.y + 50
				nodes_for_backdrop_createion.append(text_node)
				DML_Nuke.Nuke_Nodes.Standered_Nodes.BackdropNode(name=backdrop_name,
																 label="PNG Sequence out to Client Approval",
																 note_font_size=25,
																 note_font_color=255,
																 note_font='Verdana Bold',
																 post_kwargs=dict(nodes=nodes_for_backdrop_createion))
				res = w
				self._write_node = w
				self._update_Write_Node_File_Path()
			except:
				nuke.message("Something went wrong")
		return res