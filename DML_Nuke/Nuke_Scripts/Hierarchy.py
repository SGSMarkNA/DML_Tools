import nuke

#===============================================================================
def find_upstream_node(startnode,matchclass):
	"""
	In the simplest way possible, this function will go upstream and find
	the first node matching the specified class.
	"""
	isinstance(startnode,nuke.Node)
	if  startnode.Class() == matchclass:
		return startnode
	else:
		if startnode.Class() == 'Input':
			try:
				grp = nuke.toNode(startnode.fullName().split(".",1)[0])
				startnode = grp
			except:
				pass
		for node in startnode.dependencies(nuke.INPUTS):
			scan = find_upstream_node(node,matchclass)
			if scan != None:
				return scan
	return None


