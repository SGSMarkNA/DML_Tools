import maya.cmds as cmds


########################################################################
class Named_Object(object):
	"""This Class Is A Base Class That Holds The A Memeory Pointer to a node it can be sent to maya.cmds as itself and acts like a string useing the pointers name to repesent itself"""
	#----------------------------------------------------------------------
	def __init__(self,name):
		self._name = name
	#----------------------------------------------------------------------
	def __str__(self):
		return unicode(self.name)
	#----------------------------------------------------------------------
	def __repr__(self):
		return unicode(self.name)
	#----------------------------------------------------------------------
	def __hash__(self):
		return hash(self.name)
	#----------------------------------------------------------------------
	def __eq__(self, other):
		return unicode(self.name) == unicode(other)
	#----------------------------------------------------------------------
	def __ne__(self, other):
		return unicode(self.name) != unicode(other)
	#----------------------------------------------------------------------
	def get_name(self):
		return unicode(self._name)
	#----------------------------------------------------------------------
	name          = property(get_name)


########################################################################
class SelectionConnection(Named_Object):
	"""
	This command creates a named selectionConnection object. This object
	is simply a shared selection list. It may be used by editors to
	share their highlight data. For example, an outliner may attach its
	selected list to one of these objects, and a graph editor may use the
	same object as a list source. Then, the graph editor would only
	display objects that are selected in the outliner.
	
	Selection connections are UI objects which contain a list of model
	objects. Selection connections are useful for specifying which objects
	are to be displayed within a particular editor. Editor's have three
	 where a selection connection may be attached.
	They are:
	
	There are several different types of selection connections that may be
	created. They include:
	
	Below is an example selectionConnection network between two
	editors. Editor 1 is setup to display objects on the activeList.
	Editor 2 is setup to display objects which are selected within Editor
	1, and objects that are selected in Editor 2 are highlighted within
	Editor 1:
	
	The following commands will establish this network:
	
	Note: to delete a  use the deleteUI command
	Note: commands which expect objects may be given a selection connection
	instead, and the command will operate upon the objects wrapped by the
	selection connection
	Note: the graph editor and the dope sheet are the only editors which can use the
	editor connection to the highlightConnection of another editor
	WARNING: some flag combinations may not behave as you expect.  The command
	is really intended for internal use for managing the outliner used by
	the various editors.
	"""
	#----------------------------------------------------------------------
	@property
	def cmd_name(self):
		command_name = self.__class__.__name__
		command_name = command_name[0].lower() + command_name[1:]
		return command_name
	#----------------------------------------------------------------------
	@property
	def cmd(self):
		command_name = self.cmd_name
		return getattr(cmds, command_name)
	
	#----------------------------------------------------------------------
	def query(self, **kwargs):
		kwargs["query"] = True
		return self.cmd(self, **kwargs)
	
	#----------------------------------------------------------------------
	def edit(self, **kwargs):
		kwargs["edit"] = True
		return self.cmd(self, **kwargs)
	
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		if name == None:
			name = cmds.selectionConnection(**kwargs)
			super(SelectionConnection, self).__init__(name)
			
		else:
			if cmds.selectionConnection(name, exists=True):
				super(SelectionConnection, self).__init__(name)
			else:
				name = cmds.selectionConnection(name, **kwargs)
				super(SelectionConnection, self).__init__(name)
	#----------------------------------------------------------------------
	def get_addScript(self):
		"""
		Specify a script to be called when something is added to the
		selection.
		"""
		return self.query(addScript=True)
	#----------------------------------------------------------------------
	def set_addScript(self, value):
		"""
		Specify a script to be called when something is added to the
		selection.
		"""
		self.edit(addScript=value)
	#----------------------------------------------------------------------
	addScript = property(get_addScript, set_addScript)

	#----------------------------------------------------------------------
	def addTo(self,value):
		"""
		The name of a selection connection that should be added to this
		list of connections.
		"""
		self.edit(addTo=value)
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Remove everything from the selection connection.
		"""
		self.edit(clear=True)

	#----------------------------------------------------------------------
	@property
	def connectionList(self):
		"""
		Specifies that this connection should contain a list of selection
		connections.
		"""
		return self.query(connectionList=True)
	#----------------------------------------------------------------------
	def deselect(self,value):
		"""
		Remove something from the selection.
		"""
		self.edit(deselect=value)
	#----------------------------------------------------------------------
	def get_editor(self):
		"""
		Specifies that this connection should reflect the -mainListConnection
		of the specified editor.
		"""
		return self.query(editor=True)
	#----------------------------------------------------------------------
	def set_editor(self, value):
		"""
		Specifies that this connection should reflect the -mainListConnection
		of the specified editor.
		"""
		self.edit(editor=value)
	#----------------------------------------------------------------------
	editor = property(get_editor, set_editor)
	#----------------------------------------------------------------------
	def get_filter(self):
		"""
		Optionally specifies an itemFilter for this connection.
		An empty string ("") clears the current filter.
		If a filter is specified, all the information going into
		the selectionConnection must first pass through the filter
		before being accepted.
		
		NOTE: filters can only be attached to regular selectionConnections.
		They cannot be attached to any connection created using
		the -act, -mdl, -key, -wl, -sl, -cl, -lst, -obj, or -ren flags.
		We strongly recommend that you do not attach filters to a
		selectionConnection --- it is better to attach your filter
		to the editor that is using the selectionConnection instead.
		"""
		return self.query(filter=True)
	#----------------------------------------------------------------------
	def set_filter(self, value):
		"""
		Optionally specifies an itemFilter for this connection.
		An empty string ("") clears the current filter.
		If a filter is specified, all the information going into
		the selectionConnection must first pass through the filter
		before being accepted.
		
		NOTE: filters can only be attached to regular selectionConnections.
		They cannot be attached to any connection created using
		the -act, -mdl, -key, -wl, -sl, -cl, -lst, -obj, or -ren flags.
		We strongly recommend that you do not attach filters to a
		selectionConnection --- it is better to attach your filter
		to the editor that is using the selectionConnection instead.
		"""
		self.edit(filter=value)
	#----------------------------------------------------------------------
	filter = property(get_filter, set_filter)

	#----------------------------------------------------------------------
	def findObject(self,name):
		"""
		Find a selection connection in this list that wraps the specified
		object.
		"""
		return self.query(findObject=name)

	#----------------------------------------------------------------------
	def get_g(self):
		"""
		A global selection connection cannot be deleted by any script
		commands.
		"""
		return self.query(g=True)
	#----------------------------------------------------------------------
	def set_g(self, value):
		"""
		A global selection connection cannot be deleted by any script
		commands.
		"""
		self.edit(g=value)
	#----------------------------------------------------------------------
	g = property(get_g, set_g)


	#----------------------------------------------------------------------
	@property
	def identify(self):
		"""
		Find out what type of selection connection this is.  May be:
		activeList | modelList | keyframeList | worldList | objectList
		listList | editorList | connection | unknown
		"""
		return self.query(identify=True)
	#----------------------------------------------------------------------
	def get_lock(self):
		"""
		For activeList connections, locking the connection means that
		it will not listen to activeList changes.
		"""
		return self.query(lock=True)
	#----------------------------------------------------------------------
	def set_lock(self, value):
		"""
		For activeList connections, locking the connection means that
		it will not listen to activeList changes.
		"""
		self.edit(lock=value)
	#----------------------------------------------------------------------
	lock = property(get_lock, set_lock)

	#----------------------------------------------------------------------
	def get_object(self):
		"""
		Specifies that this connection should wrap around the specified
		object (which may be a set).  Query will return all the members of the
		selection connection (if the connection wraps a set, the set members will
		be returned)
		"""
		return self.query(object=True)
	#----------------------------------------------------------------------
	def set_object(self, value):
		"""
		Specifies that this connection should wrap around the specified
		object (which may be a set).  Query will return all the members of the
		selection connection (if the connection wraps a set, the set members will
		be returned)
		"""
		self.edit(object=value)
	#----------------------------------------------------------------------
	object = property(get_object, set_object)

	#----------------------------------------------------------------------
	def get_parent(self):
		"""
		The name of a UI object this should be attached to.  When the
		parent is destroyed, the selectionConnection will auto-delete.
		If no parent is specified, the connection is created in the
		current controlLayout.
		"""
		return self.query(parent=True)
	#----------------------------------------------------------------------
	def set_parent(self, value):
		"""
		The name of a UI object this should be attached to.  When the
		parent is destroyed, the selectionConnection will auto-delete.
		If no parent is specified, the connection is created in the
		current controlLayout.
		"""
		self.edit(parent=value)
	#----------------------------------------------------------------------
	parent = property(get_parent, set_parent)

	#----------------------------------------------------------------------
	def remove(self,value):
		"""
		The name of a selection connection that should be removed from
		this list of connections.
		"""
		self.edit(remove=value)

	#----------------------------------------------------------------------
	def get_removeScript(self):
		"""
		Specify a script to be called when something is removed from
		the selection.
		"""
		return self.query(removeScript=True)
	#----------------------------------------------------------------------
	def set_removeScript(self, value):
		"""
		Specify a script to be called when something is removed from
		the selection.
		"""
		self.edit(removeScript=value)
	#----------------------------------------------------------------------
	removeScript = property(get_removeScript, set_removeScript)

	#----------------------------------------------------------------------
	def select(self,value):
		"""
		Add something to the selection. This does not replace the
		existing selection.
		"""
		self.edit(select=value)

	#----------------------------------------------------------------------
	@property
	def switch(self):
		"""
		Acts as a modifier to -connectionList which sets the list of objects
		to be the first non-empty selection connection.  selection connections
		are tested in the order in which they are added.
		"""
		return self.query(switch=True)