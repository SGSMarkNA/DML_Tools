#speak = QtCore.Signal((int,), (str,))
import DML_Tools
DML_PYQT = DML_Tools.DML_PYQT
import os
import QT
import Qt_Roles_And_Enums
import QStandardItemModel
import QSortFilterProxyModel
import QStandardItem
import MimeData

QStandardItem         = QStandardItem.Standard_QStandardItem
QSortFilterProxyModel = QSortFilterProxyModel.Standered_QSortFilterProxyModel
QStandardItemModel    = QStandardItemModel.Standard_QStandardItemModel

try:
	_maya_check = True
	import Scripts.NodeCls.M_Nodes
	import maya.cmds as cmds
	M_Nodes              = Scripts.NodeCls.M_Nodes
	MNODE                = M_Nodes.MNODE
	Container            = M_Nodes.Container
	Script_Node          = M_Nodes.Script_Node
	SelectionSet         = M_Nodes.SelectionSet
	VRayObjectProperties = M_Nodes.VRayObjectProperties
	DisplayLayer         = M_Nodes.DisplayLayer
	RenderLayer          = M_Nodes.RenderLayer
	ShadingNode          = M_Nodes.ShadingNode
	Shading_Engine       = M_Nodes.Shading_Engine
	MPLUG                = M_Nodes.MPLUG
	To_MNode             = M_Nodes.To_MNode
	strings_to_MNODES    = M_Nodes.strings_to_MNODES
	

except:
	_maya_check = False

########################################################################
class Data_Roles(Qt_Roles_And_Enums.Standered_Item_Data_Roles):
	ITEM           = QT.userRole_counter()
	DATA_OBJECT    = QT.userRole_counter()

#---------------------------------------------------------------------------------------------------
#_______________________________________________________________________ Utility Functions
#----------------------------------------------------------------------
def is_Base_Item_Instance(item):
	""""""
	return isinstance(item,_Base_Item)
#----------------------------------------------------------------------
def name_or_none(item):
	""""""
	if is_Base_Item_Instance(item):
		return item.data()
	else:
		return "None"
	
#---------------------------------------------------------------------------------------------------
#_______________________________________________________________________ Persistent Data Types
########################################################################
class Named_Data_Object(object):
	""""""
	def __init__(self,name,**kwargs):
		self.name = name
	def __str__(self):
		return str(self.name)

	def __repr__(self):
		return str(self.name)

##======================================================================
# Standered Data Model Items
##======================================================================
#---------------------------------------------------------------------------------------------------
#_______________________________________________________________________ Base Item Types
########################################################################
class _Base_Item(QStandardItem):
	ITEM_TYPE       = QT.user_type_counter()
	Item_Data_Roles =  Data_Roles
	def __init__(self,*args,**kwargs):
		super(_Base_Item,self).__init__(*args,**kwargs)
	
	def resort_parent(self):
		self.parent().sortChildren()
		
	def data(self, role=Data_Roles.DISPLAY):
		if role == Data_Roles.ITEM:
			return self
		return super(_Base_Item, self).data(role)
	
########################################################################
class _Data_Item(_Base_Item):
	"""Base Class For Holding Non Qt Based Data"""
	ITEM_TYPE  = QT.user_type_counter()
	def __init__(self, data=None, **kwargs):
		super(_Data_Item,self).__init__(**kwargs)
		self._data = data
		self.references = []

	def data(self, role=Data_Roles.DISPLAY):
		if role in self.Item_Data_Roles.DP_ED:
			return str(self._data)

		if role == self.Item_Data_Roles.DATA_OBJECT:
			return self._data
		
		if role == self.Item_Data_Roles.ITEM:
			return self

		return super(_Data_Item, self).data(role)

	def setData(self, value, role=Data_Roles.EDIT):
		if role in self.Item_Data_Roles.DP_ED:
			self._data =  value
		else:
			return super(_Data_Item, self).data(role)
########################################################################
class _Named_Data_Item(_Data_Item):
	ITEM_TYPE       = QT.user_type_counter()
	def __init__(self,name,**kwargs):
		data = Named_Data_Object(name)
		super(_Named_Data_Item,self).__init__(data,**kwargs)
		isinstance(self._data, Named_Data_Object)
		
	def data(self, role=Data_Roles.DISPLAY):
		
		if role in self.Item_Data_Roles.DP_ED:
			return self._data.name

		if role == self.Item_Data_Roles.DATA_OBJECT:
			return self._data
		
		return super(_Named_Data_Item, self).data(role)

	def setData(self, value, role=Data_Roles.EDIT):
		if role in self.Item_Data_Roles.DP_ED:
			if isinstance(value, (unicode, str)):
				self._data.name = value
			else:
				self._data = value
		else:
			return super(_Named_Data_Item, self).data(role)
		
########################################################################
class _Reference_Item(_Base_Item):
	ITEM_TYPE  = QT.user_type_counter()
	#----------------------------------------------------------------------
	def __init__(self,item,**kwargs):
		super(_Reference_Item,self).__init__(**kwargs)
		self._data = item
		if hasattr(item,"references"):
			item.references.append(self)
	#----------------------------------------------------------------------
	def data(self, role=Data_Roles.DISPLAY):
		return self._data.data(role)
	#----------------------------------------------------------------------
	def setData(self, value, role=Data_Roles.EDIT):
		self._data.setData(value, role)

#---------------------------------------------------------------------------------------------------
#_______________________________________________________________________ External Data Item Types
########################################################################
class MNode_Item(_Data_Item):
	ITEM_TYPE  = QT.user_type_counter()
	#----------------------------------------------------------------------
	def __init__(self, node, **kwargs):
		""""""
		super(MNode_Item,self).__init__(node, **kwargs)
		if _maya_check:
			self.node = node
	#----------------------------------------------------------------------
	def data(self, role=Data_Roles.DISPLAY):
		""""""
		if role in self.Item_Data_Roles.DP_ED:
			if _maya_check:
				return self.node_name

		if role == self.Item_Data_Roles.DATA_OBJECT:
			return self.node

		return super(MNode_Item, self).data(role)
	#----------------------------------------------------------------------
	def setData(self, value, role=Data_Roles.DISPLAY):
		""""""
		if role in self.Item_Data_Roles.DP_ED and _maya_check:
			self.node_name = value
		else:
			return super(MNode_Item, self).setData(value, role)	
	#----------------------------------------------------------------------
	def get_Node(self):
		""""""
		return self._data
	#----------------------------------------------------------------------
	def set_Node(self, node):
		""""""
		if isinstance(node, M_Nodes.MNODE):
			self._data = node
		elif isinstance(node, str) and cmds.objExists(node):
			self._data = M_Nodes.MNODE(node)
		else:
			raise ValueError("node input must be and instance of MNODE or a name of and existing Node")
	#----------------------------------------------------------------------
	node = property(get_Node, set_Node)
	#----------------------------------------------------------------------
	def get_Node_Name(self):
		""""""
		return self._data.nice_name_wo_ns
	#----------------------------------------------------------------------
	def set_Node_Name(self, name):
		""""""
		self._data.name =  name
	#----------------------------------------------------------------------
	node_name = property(get_Node_Name, set_Node_Name)
	#----------------------------------------------------------------------
	@property
	def node_type(self):
		""""""
		return self._data.objectType
	#----------------------------------------------------------------------
	@property
	def node_transform_type(self):
		""""""
		return self._data.transfromType
	#----------------------------------------------------------------------
	@property
	def node_assined_display_layer(self):
		""""""
		return self._data.assinedDisplayLayer
	#----------------------------------------------------------------------
	@property
	def node_transform_descendents(self):
		""""""
		return self._data.all_transform_Descendents
	#----------------------------------------------------------------------
	@property
	def node_child_count(self):
		""""""
		return self._data.numberOfChildern
	#----------------------------------------------------------------------
	@property
	def node_Descendents(self):
		""""""
		return self._data.allDescendents
	#----------------------------------------------------------------------
	@property
	def node_child_transforms(self):
		""""""
		return self._data.child_transforms
	#----------------------------------------------------------------------
	@property
	def node_has_child_transforms(self):
		""""""
		return self._data.has_child_transforms
	#----------------------------------------------------------------------
	@property
	def node_children(self):
		""""""
		return self._data.children
	#----------------------------------------------------------------------
	@property
	def node_parents(self):
		""""""
		return self._data.allParents
	#----------------------------------------------------------------------
	@property
	def node_exists(self):
		""""""
		return self._data.objectExists

	#----------------------------------------------------------------------
	def node_delete(self):
		""""""
		return self._data.delete()


########################################################################
class Maya_Asset_Item(MNode_Item):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name, **kwargs):
		"""Constructor"""
		if _maya_check:
			if not isinstance(name, M_Nodes.MNODE):
				name = M_Nodes.Container(name,
				                         dagContainer=True,
				                         force=False, addNode=False,
				                         current=False,
				                         includeShaders=False,
				                         publishConnections=False,
				                         nodeNamePrefix=False,
				                         includeHierarchyAbove=False,
				                         includeHierarchyBelow=False)
				
		super(Maya_Asset_Item, self).__init__(name, **kwargs)
		if _maya_check:
			if isinstance(self._data, M_Nodes.Container):
				self.node_plug_rmbCommand      = self._data.rmbCommand
				self.node_plug_templateName    = self._data.templateName
				self.node_plug_templateVersion = self._data.templateVersion
				self.node_plug_templatePath    = self._data.templatePath
				self.node_plug_iconName        = self._data.iconName
				self.node_plug_viewMode        = self._data.viewMode
				self.node_plug_creator         = self._data.creator
				self.node_plug_creationDate    = self._data.creationDate
				self.node_plug_rootTransform   = self._data.rootTransform

	#----------------------------------------------------------------------
	def node_bindAttr(self,nodeAttr,unboundName):
		"""
		Bind a contained attribute to an unbound published name on the interface of the container
		returns a list of bound published names.
		The first string specifies the node and attribute name to be bound in "node.attr" format.
		The second string specifies the name of the unbound published name.
		In query mode, returns a string array of the published names and their corresponding attributes.
		The flag can also be used in query mode in conjunction with the
		-publishName, -publishAsParent, and -publishAsChild flags.
		"""
		return self._data.bindAttr(nodeAttr, unboundName)
	#----------------------------------------------------------------------
	def node_unbindAttr(self,nodeAttr,unboundName):
		"""Unbind a published attribute from its published name on the interface of the container,
		leaving an unbound published name on the interface of the container
		returns a list of unbound published names.
		The first string specifies the node and attribute name to be unbound in "node.attr" format,
		and the second string specifies the name of the bound published name.
		In query mode, can only be used with the -publishName, -publishAsParent and -publishAsChild flags.
		"""
		return self._data.unbindAttr(nodeAttr, unboundName)
	#----------------------------------------------------------------------
	def node_unpublishName(self,name):
		"""Unpublish an unbound name from the interface of the container."""
		return self._data.unpublishName(name)
	#----------------------------------------------------------------------
	def node_unbindAndUnpublish(self,name):
		""""""
		return self._data.unbindAndUnpublish(name)
	#----------------------------------------------------------------------
	def node_publishName(self,name,bindTo=""):
		"""
		Publish a name to the interface of the container
		
		if bindTo is set with the format "node.attr"
		  Publish the given name and bind the attribute to the given name
		  
		returns the actual name published to the interface.
		"""
		return self._data.publishName(name, bindTo=bindTo)
	#----------------------------------------------------------------------
	def node_publishAsParent(self,node,name):
		"""Publish contained node to the interface of the container to indicate it can be a parent to external nodes.
		The second string is the name of the published node.
		In query mode, 
		  returns a string of array of the published names and the corresponding nodes.
		  
		If -publishName flag is used in query mode,
		  only returns the published names;
		  
		if -bindAttr flag is used in query mode,
		  only returns the name of the published nodes."""
		return self._data.publishAsParent(node, name)
	#----------------------------------------------------------------------
	def node_unpublishParent(self,name):
		""""""
		return self._data.unpublishParent(name)
	#----------------------------------------------------------------------
	def node_unpublishChild(self,name):
		""""""
		return self._data.unpublishChild(name)
	#----------------------------------------------------------------------
	def node_publishAsChild(self,node,name):
		"""Publish contained node to the interface of the container to indicate it can be a child of external nodes.
		The second string is the name of the published node.
		In query mode,
		  returns a string of the published names and the corresponding nodes.
		
		If -publishName flag is used in query mode,
		  only returns the published names;
		
		if -bindAttr flag is used in query mode,
		  only returns the name of the published nodes."""
		
		return self._data.publishAsChild(node, name)
	
	#----------------------------------------------------------------------
	def node_publishedNames(self,bound=False,unBound=False,parents=False,children=False,NodeAttr=""):
		"""returns the published names for the container.
		If the bound flag is True,
		  returns only the names that are bound;
		  
		if the unBound flag is True,
		  returns only the names that are not bound;
		  
		if the parents flags is True,
		  returns only names of published parents.
		  
		if the children flags is True,
		  returns only names of published children.
		  
		if the NodeAttr is specified with an attribute argument in the "node.attr" format,
		  returns the published name for that attribute, if any.
		"""
		return self._data.publishedNames(bound=bound, unBound=unBound, parents=parents, children=children, NodeAttr=NodeAttr)
	
	#----------------------------------------------------------------------
	def node_addNode(self, nodes, includeNetwork=False, includeHierarchyBelow=False):
		""""""
		return self._data.addNode(nodes, includeNetwork=includeNetwork, includeHierarchyBelow=includeHierarchyBelow)
	#----------------------------------------------------------------------
	def node_addSelectedNodes(self, includeNetwork=False, includeHierarchyBelow=False):
		""""""
		return self._data.addSelectedNodes(includeNetwork=includeNetwork, includeHierarchyBelow=includeHierarchyBelow)
	#----------------------------------------------------------------------
	def node_removeNode(self,*nodes):
		"""Specifies the list of nodes to remove from container."""
		return self._data.removeNode(*nodes)
	#----------------------------------------------------------------------
	@property
	def node_nodeList(self):
		"""Specifies the list of nodes to remove from container."""
		return self._data.nodeList
	#----------------------------------------------------------------------
	def node_makeCurent(self):
		""""""
		return self._data.makeCurent()
		
	#----------------------------------------------------------------------
	@property
	def node_parentContainer(self):
		""""""
		return self._data.parentContainer
		
	#----------------------------------------------------------------------
	def node_asset(self,*nodes):
		""""""
		return self._data.asset(*nodes)
	
	#----------------------------------------------------------------------
	def node_removeContainer(self):
		""""""
		return self._data.removeContainer()
	
########################################################################
class Maya_Selection_Set_Item(MNode_Item):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name, **kwargs):
		"""Constructor"""
		if _maya_check:
			if not isinstance(name, M_Nodes.MNODE):
				name = M_Nodes.SelectionSet(name, empty=True, copy=None, text="", renderable=False)
		super(Maya_Selection_Set_Item, self).__init__(name, **kwargs)
		if _maya_check:
			isinstance(self._data, M_Nodes.SelectionSet)
	#----------------------------------------------------------------------
	def node_select_set(self):
		self._data.select_set()
	#----------------------------------------------------------------------
	def node_select_members(self):
		self._data.select_members()
	#----------------------------------------------------------------------
	def node_remove_items(self,*items):
		self._data.remove(*items)
	#----------------------------------------------------------------------
	def node_remove_selected(self):
		self._data.remove_selected()
	#----------------------------------------------------------------------
	def node_include_items(self,*items):
		self._data.include(*items)
	#----------------------------------------------------------------------
	def node_include_special(self,*items):
		self._data.include_special(*items)
	#----------------------------------------------------------------------
	def node_addElement(self,*items):
		self._data.addElement(*items)
	#----------------------------------------------------------------------
	def node_intersecting_members(self,selectionSet):
		return self._data.intersecting_members(selectionSet)
	#----------------------------------------------------------------------
	def node_isSubSet(self,item):
		return self._data.isSubSet(item)
	#----------------------------------------------------------------------
	def node_hasSubSet(self,item):
		return self._data.hasSubSet(item)
	#----------------------------------------------------------------------
	@property
	def node_size(self):
		return self._data.size
	#----------------------------------------------------------------------
	@property
	def node_memberNames(self):
		return self._data.memberNames
	#----------------------------------------------------------------------
	@property
	def node_members(self):
		return self._data.members
	#----------------------------------------------------------------------
	@property
	def node_parents(self):
		return self._data.parents
	#----------------------------------------------------------------------
	@property
	def node_children(self):
		return self._data.children

########################################################################
class Vray_Object_Properties_Item(Maya_Selection_Set_Item):
	""""""

	#----------------------------------------------------------------------
	def __init__(self, name, **kwargs):
		"""Constructor"""
		if _maya_check:
			if not isinstance(name, M_Nodes.MNODE):
				name = M_Nodes.VRayObjectProperties(name)
		super(Vray_Object_Properties_Item, self).__init__(name, **kwargs)
		if _maya_check:
			if isinstance(self._data, M_Nodes.VRayObjectProperties):
				self.node_plug_giVisibility           = self._data._giVisibility_plug
				self.node_plug_primaryVisibility      = self._data._primaryVisibility_plug
				self.node_plug_reflectionVisibility   = self._data._reflectionVisibility_plug
				self.node_plug_refractionVisibility   = self._data._refractionVisibility_plug
				self.node_plug_shadowVisibility       = self._data._shadowVisibility_plug
				self.node_plug_matteSurface           = self._data._matteSurface_plug
				self.node_plug_generateRenderElements = self._data._generateRenderElements_plug
				self.node_plug_shadows                = self._data._shadows_plug
				self.node_plug_affectAlpha            = self._data._affectAlpha_plug
				self.node_plug_generateGI             = self._data._generateGI_plug
				self.node_plug_receiveGI              = self._data._receiveGI_plug
				self.node_plug_generateCaustics       = self._data._generateCaustics_plug
				self.node_plug_receiveCaustics        = self._data._receiveCaustics_plug
				self.node_plug_ignore                 = self._data._ignore_plug
				self.node_plug_overrideMBSamples      = self._data._overrideMBSamples_plug
				self.node_plug_objectIDEnabled        = self._data._objectIDEnabled_plug
				self.node_plug_alphaContribution      = self._data._alphaContribution_plug
	

#---------------------------------------------------------------------------------------------------
########################################################################
class Standard_Item_Model(QStandardItemModel):
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		super(Standard_Item_Model,self).__init__(*args,**kwargs)
		
