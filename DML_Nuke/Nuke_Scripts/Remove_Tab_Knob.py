import nuke

#----------------------------------------------------------------------
def Remove_Tab(*args):
	"""
	1 arg  = Tab Knob
	2 args = nuke node,tab name
	
	addUserKnob {20 Tab_A l "Tab A"}
	addUserKnob {3 a_number l "A Number"} a_number
	addUserKnob {6 a_check_box l "A Check Box" +STARTLINE} a_check_box
	addUserKnob {20 Tab_B l "Tab B"}
	addUserKnob {3 other_number l "Other Number"} other_number
	"""
	# if the number of inputs is 1 then the input Should Be a nuke Knob
	if len(args) == 1:
		# assign the tab_knob
		tab_knob = args[0]
		
		# check if it is a DML wrapper Knob
		if hasattr(tab_knob,"_is_dml_object"):
			tab_knob = tab_knob.nuke_object
		# make sure that a knob was given
		if not isinstance(tab_knob,nuke.Knob):
			raise TypeError("tab_knob was not a correct Type")
		# get the node this knob is attached to
		# assign the node
		node = tab_knob.node()
		# make sure that the knob was attached to a node
		if node == None:
			raise Exception("The Knob is not attached to a node")
	# if the number of inputs is 2 then the input 1 Should Be a nuke Node and input 2 Should be a tab knob	
	elif len(args) == 2:
		node     = args[0] 
		tab_knob = args[1]
		# check if it is a DML wrapper Node
		if hasattr(node,"_is_dml_object"):
			node = node.nuke_object
		# check if input 1 was the name of a node
		elif isinstance(node,str):
			node = nuke.toNode(node)
			
		# make sure that input 1 was a nuke node
		if not isinstance(node,nuke.Node):
			raise TypeError("node was not a correct Type")
		
		# make sure input 2 was the name of a tab on this node
		if not isinstance(tab_knob,str):
			raise ValueError("arg 2 must be the name of the tab knob")
		
		# make sure a knob was found
		if node.knob(tab_knob) == None:
			raise LookupError("the node {} does not contain a knob {}".format(node.name(),tab_knob))
		else:
			# get the tab knob from the node
			tab_knob = node.knob(tab_knob)
	
	if not tab_knob.Class() == "Tab_Knob":
		raise TypeError("knob was not a Tab Knob but a {}".format(tab_knob.Class()))
	
	# Make A Variable That Will Tell The Code To Start Looking For The End Of This Tab
	# By Looking For The Next Tab Knob
	in_collection = False
	# Holds The Name Of Tab Knob That Comes After This Tab Knob
	end_tab_name = None
	# Holds The knobs that are associated with this tab
	knb_collection = []
	# Scan Each Line Of User Knobs On The Attaced Node
	for line in node.writeKnobs(nuke.WRITE_USER_KNOB_DEFS).splitlines():
		if len(line):
			if line.startswith("addUserKnob"):
				# Get The Knob Type Number
				user_knob_type = line.split()[1].replace("{","")
				# Get The Knob Name
				line_tab_name  = line.split()[2].replace("}","")
				# Check If We Have Not Found This Tab Knob Yet
				if not in_collection:
					# If Not Check if The Knob Type Is a tab and not a tab group
					if user_knob_type == '20' and not "n 1}" in line and not "n -1}" in line:
						# now check if the name matches this tab
						if line_tab_name == tab_knob.name():
							# We Are Now In This Tab Knob
							in_collection=True
				else:
					# If So Check if The Knob Type Is a tab and not a tab group
					if user_knob_type == '20' and not "n 1}" in line and not "n -1}" in line:
						# If So Then Mark it and stop this scan
						end_tab_name = line_tab_name
						break
			
	# Reset 
	in_collection = False
	# Scan Through All The Knobs On The Attached Node
	for knb in node.allKnobs():
		if knb.Class() == "Tab_Knob" and knb.name() == tab_knob.name():
			in_collection = True
			knb_collection.append(knb)
		elif in_collection:
			if knb.Class() == "Tab_Knob" and knb.name() == end_tab_name:
				in_collection = False
				break
			else:
				knb_collection.append(knb)

	for knb in reversed(knb_collection):
		node.removeKnob(knb)