import maya.cmds as cmds
import DML_Tools.Maya.DML_Maya as DML_Maya

from DML_Asset_Views_View_State_Object_Set import Asset_Views_View_State_Object_Set

if False:
	from DML_Asset_Views_View_State_Collection import Asset_Views_View_State_Collection
########################################################################
class Objects_Plug(DML_Maya.Maya_Nodes.Base_Nodes.API_Plug.API_Plug):
	""""""
	MAYA_PLUG_TYPE_RELATION   = None
	RETURN_OVERIDE_CHECK_TYPE = "message"
	#----------------------------------------------------------------------
	@classmethod
	def _overide_Return_Check(cls,plg):
		""""""
		node = str(plg).split(".",1)[0]
		plg_name = str(plg).split(".")[-1]
		try:
			if cmds.getAttr( plg,typ=True)=="message" and cmds.attributeQuery(plg_name,node=node,multi=True) and cmds.attributeQuery("dmlAssetViewsViewState", node=node,exists=True):
				return True
			return False
		except:
			return False
	#----------------------------------------------------------------------
	def add_Objects(self,*args):
		""""""
		res = []
		if not len(args):
			args = DML_Maya.dml.to_DML_Nodes(cmds.listRelatives(cmds.ls(sl=True, dagObjects=True, shapes=True,),type="transform",parent=True, fullPath=True))
		else:
			args = DML_Maya.dml.to_DML_Nodes(cmds.listRelatives(cmds.ls(args, dagObjects=True, shapes=True,),type="transform",parent=True, fullPath=True))
			
		if len(args):
			current_items  = self.get_Element_Source_Nodes()
			current_items_set = set(current_items)
			args_set = set(args)
			args           = list(args_set.difference(current_items_set))
			for obj in args:
				#items = [con for con in cmds.listConnections(obj+".message",d=True,plugs=True) if not self.node.name in con ]
				#items
				#[u'DML_Asset_Views_Manager_Collections_default_collection_default_View.objects[29]']
				#if not self.is_Node_A_Source_In_Elements(obj):
				cmds.connectAttr(obj.message,self,force=True, nextAvailable=True)
				res.append(obj)
		return res		
	#----------------------------------------------------------------------
	def remove_Objects(self,*args):
		""""""
		res = []
		if not len(args):
			args = DML_Maya.dml.to_DML_Nodes(cmds.listRelatives(cmds.ls(sl=True, dagObjects=True, shapes=True,),type="transform",parent=True, fullPath=True))
		else:
			args = DML_Maya.dml.to_DML_Nodes(cmds.listRelatives(cmds.ls(args, dagObjects=True, shapes=True,),type="transform",parent=True, fullPath=True))
		if len(args):
			current_items  = self.get_Element_Source_Nodes()
			current_items_set = set(current_items)
			args_set = set(args)
			#current_elements = self.existingArrayAttributeElements
			newargs = list(set(current_items).difference(set(args)))
			newargs = list(set(args).difference(set(current_items)))
			#for obj in newargs:
				#cmds.disconnectAttr(obj.message,self, nextAvail5able=True)
			
			#for elem in self.multiElements:
				#if not elem.isConnected:
					#cmds.removeMultiInstance( elem,b=True)
			
			#rebuild_data = []
			#for current_connection in self.arrayElementsWithConnections:
				#rebuild_data.append(current_connection.source_plug())
			
			for elem in self.multiElements:
				cmds.removeMultiInstance( elem,b=True)
				
			for obj in newargs:	
				#for index,source_plg in enumerate(rebuild_data):
				cmds.connectAttr(obj.message,self,force=True, nextAvailable=True)
				#obj.message >> self.elementByLogicalIndex(index)
						
		return res
########################################################################
class Asset_Views_View_State(DML_Maya.Maya_Nodes.Network):
	RETURN_OVERIDE_CHECK_TYPE = "network"
	#----------------------------------------------------------------------
	@classmethod
	def _overide_Return_Check(cls,node):
		""""""
		return cmds.attributeQuery( 'dmlAssetViewsViewState', node=node, exists=True )
	#----------------------------------------------------------------------
	@classmethod
	def createNode(cls,*args,**kwargs):
		""""""
		if not "name" in kwargs or kwargs.get("name") == None:
			kwargs["name"] = "Asset_View_State"
		res = DML_Maya.Maya_Nodes.Network.createNode(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		self.addAttr('dmlAssetViewsViewState', dt="string",hidden=True)
		self.plg_state_Collection = self.addAttr('stateCollection', at="message",writable=True,readable=False)
		self.plg_name             = self.addAttr('name', dt="string")
		self.plg_state_object_set = self.addAttr('viewStateObjectSet', at="message", writable=True, readable=False)
		self.plg_state_view       = self.addAttr('dmlStateView', at="message",writable=True,readable=False)
		self.plug_display_layer   = self.addAttr('layer', at="message",writable=True,readable=False)
		self.plug_thumbnail_icon  = self.addAttr('thumbnailIcon', dt="string",hidden=True)
		
		self.lockNode()
		if not self.plg_state_view.isConnected:
			view = DML_Maya.Maya_Nodes.Camera_View()
			self.plg_state_view.value = view.message
		if not self.plg_state_object_set.isConnected:
			object_set = Asset_Views_View_State_Object_Set(empty=True)
			object_set.plg_view_state.value = self.plg_state_object_set
			
		if False:
			self.camera_view == DML_Maya.Maya_Nodes.Camera_View()
			isinstance(self.camera_view,DML_Maya.Maya_Nodes.Camera_View)
			self.object_set == Asset_Views_View_State_Object_Set()
			isinstance(self.object_set,Asset_Views_View_State_Object_Set)
	#----------------------------------------------------------------------
	def get_State_Collection(self):
		""""""
		res = self.plg_state_Collection.source_node()
		if False:
			isinstance(res,Asset_Views_View_State_Collection)
		return res
	#----------------------------------------------------------------------
	def get_State_Object_Set(self):
		""""""
		res = self.plg_state_object_set.destination_nodes()
		if len(res):
			res = res[0]
		isinstance(res,Asset_Views_View_State_Object_Set)
		return res
	#----------------------------------------------------------------------
	def set_State_Object_Set(self,node):
		""""""
		if isinstance(node,Asset_Views_View_State_Object_Set):
			node.plg_view_state.value = self.plg_state_object_set
	#----------------------------------------------------------------------
	object_set = property(get_State_Object_Set,set_State_Object_Set)
	#----------------------------------------------------------------------
	def add_Objects(self,*args):
		""""""
		
		newargs = []
		if not len(args):
			args = DML_Maya.dml.ls(sl=True, type="transform")
		else:
			args = DML_Maya.dml.ls(*args, type="transform")
			
		if len(args):
			current_items  = self.object_set.members()
			current_items_set = set(current_items)
			args_set = set(args)
			newargs  = list(args_set.difference(current_items_set))
			if len(newargs):
				self.object_set.forceElement(newargs)
		return newargs
	#----------------------------------------------------------------------
	def remove_Objects(self,*args):
		""""""
		res = []
		if not len(args):
			args = args = DML_Maya.dml.ls(sl=True, type="transform")
		else:
			args = DML_Maya.dml.ls(args, type="transform")
		if len(args):
			current_items     = self.object_set.members()
			current_items_set = set(current_items)
			args_set = set(args)
			newargs = list(current_items_set.intersection(args_set))
			if len(newargs):
				self.object_set.remove(newargs)
				res = newargs
		return res
	#----------------------------------------------------------------------
	def get_Nodes(self):
		""""""
		return self.object_set.members()
	#----------------------------------------------------------------------
	def get_View_Name(self):
		""""""
		if self.plg_name.value == None:
			self.plg_name.value = self.nice_name
		return self.plg_name.value
	#----------------------------------------------------------------------
	def set_View_Name(self,val):
		""""""
		self.plg_name.value = val
		self.rename(val)
		self.camera_view.rename(val+"_Camera_View")
		self.object_set.rename(val+"_Object_Set")
	#----------------------------------------------------------------------
	view_state_name = property(get_View_Name,set_View_Name)
	#----------------------------------------------------------------------
	@property
	def camera_view(self):
		""""""
		return self.plg_state_view.source_node()
	#----------------------------------------------------------------------
	def apply_Camera_View(self,camera=None):
		""""""
		self.camera_view.setCamera(camera=camera)
	#----------------------------------------------------------------------
	def update_Camera_View(self,camera=None):
		""""""
		self.camera_view.setView(camera=camera)
	#----------------------------------------------------------------------
	def get_Camera(self):
		""""""
		return self.get_State_Collection().get_State_Collections().plg_manager