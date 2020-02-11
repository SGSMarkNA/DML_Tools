
import nuke
from ..Abstract_Nodes import Node
from .. import Vector2
from ...Decorators.Node_Wraper_Manager import to_DML_Nodes,node_Return_Wrapper,nuke_Object_Return_Wrapper,knob_Return_Wrapper,to_Real_Nuke_Nodes
from ..Standered_Objects import Box
from .. import Node_List
from functools import wraps
import sys

#----------------------------------------------------------------------
def wrapper_Auto_Apply_Offset(func):
	''' '''
	@wraps(func)
	def wrapper(*args, **kws):
		offset_data = args[0].nodes_offset_dict
		err = None
		try:
			res=func(*args, **kws)
			args[0].apply_node_Offset(offset_data)
		except Exception, error:
			err=error
		finally:
			if err:
				traceback = sys.exc_info()[2]  # get the full traceback
				raise StandardError(Exception(err), traceback)
			return res
	return wrapper
#----------------------------------------------------------------------
def wrapper_Auto_Update_Box(func):
	''' '''
	@wraps(func)
	def wrapper(*args, **kws):
		err = None
		try:
			res=func(*args, **kws)
			args[0].update_box()
		except Exception, error:
			err=error
		finally:
			if err:
				traceback = sys.exc_info()[2]  # get the full traceback
				raise StandardError(Exception(err), traceback)
			return res
	return wrapper

################################################################################
class BackdropNode(Node):
	NODE_TYPE_RELATION        = "BackdropNode"
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		""""""
		post_keys = kwargs.get("post_kwargs",dict())
		self._make_backdrop_BBox()
		self.update_backdrop()
		if "nodes" in post_keys.keys():
			self.set_To_Nodes(post_keys.get("nodes"))
		if False:
			isinstance(self.bd_WH,Vector2)
	#----------------------------------------------------------------------
	def delete(self,includeContents=True):
		""""""
		if includeContents:
			[nuke.delete(n) for n in to_Real_Nuke_Nodes(self.nodes)]
		super(BackdropNode,self).delete()
	#----------------------------------------------------------------------
	@wrapper_Auto_Update_Box
	def set_To_Nodes(self,nodes):
		""""""
		nodes = Node_List(nodes)
		bounds = nodes.calculate_bounds()
		self.x = bounds[0]
		self.y = bounds[1]
		self.bdwidth = bounds[2]
		self.bdheight = bounds[3]
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def getNodes(self):
		"""
			self.getNodes() -> a list of nodes contained inside the backdrop

			Get the nodes contained inside a backdrop node

			Example:

			backdrop = nuke.toNode("BackdropNode1")

			nodesInBackdrop = backdrop.getNodes()

			@return: a list of nodes contained inside the backdrop.

		"""
		return self.nuke_object.getNodes()
	#----------------------------------------------------------------------
	@node_Return_Wrapper
	def selectNodes(self):
		"""
			self.selectNodes(selectNodes) -> None

			Select or deselect all nodes in backdrop node

			Example:

			backdrop = nuke.toNode("BackdropNode1")

			backdrop.selectNodes(True)

			@return: None.

		"""
		return self.nuke_object.selectNodes()
	#----------------------------------------------------------------------
	@property
	def bdwidth(self):
		""""""
		return self.knob("bdwidth").value()
	#----------------------------------------------------------------------
	@bdwidth.setter
	def bdwidth(self,val):
		""""""
		self.knob("bdwidth").setValue(val)
	#----------------------------------------------------------------------
	@property
	def bdheight(self):
		""""""
		return self.knob("bdheight").value()
	#----------------------------------------------------------------------
	@bdheight.setter
	def bdheight(self,val):
		""""""
		self.knob("bdheight").setValue(val)
	#----------------------------------------------------------------------
	@property
	def bd_WH(self):
		""""""
		return Vector2(self.bdwidth,self.bdheight)
	#----------------------------------------------------------------------
	@bd_WH.setter
	def bd_WH(self,*args):
		""""""
		if len(args)==1 and isinstance(args[0],list):
			self.bdwidth = args[0][0]
			self.bdheight = args[0][1]
		elif len(args)==1 and isinstance(args[0],Vector2):
			self.bdwidth = args[0].x
			self.bdheight = args[0].y
		elif len(args)==2:
			self.bdwidth = args[0]
			self.bdheight = args[1]
		else:
			raise ValueError("Value must be A list, Vector2, or 2 values")
	#----------------------------------------------------------------------		
	def update_box(self):
		self._box.set(int(self.L), int(self.B), int(self.R), int(self.T))
	#----------------------------------------------------------------------
	def update_backdrop(self):
		self.update_box()
	#----------------------------------------------------------------------
	@property
	@node_Return_Wrapper
	def nodes(self):
		'''
		Returns all the nodes contained in backdropNode input or all selected Backdrop nodes.
		'''
		inNodes = []
		#left   = self.xpos()
		#top    = self.ypos()
		#right  = left + self.bdwidth
		#bottom = top + self.bdheight
		#box = Box(x=left, y=bottom, r=right, t=top)
		for node in nuke.allNodes():
			if node.Class() == "Viewer":
				continue
			elif self._box.Is_Node_Inside(node):
				inNodes.append(node)
		return inNodes
	#----------------------------------------------------------------------
	def make_nodelist(self):
		return  Node_List(self.nodes)
	#----------------------------------------------------------------------
	def _make_backdrop_BBox(self):
		bd_wh = Vector2(self.bdwidth,self.bdheight)
		bd_xy = Vector2(self.xpos(),self.ypos())
		bd_wh = bd_xy + bd_wh
		self._box = Box(nuke.Box(x=int(bd_xy.x), y=int(bd_wh.y), r=int(bd_wh.x), t=int(bd_xy.y)))
		return self._box
	#----------------------------------------------------------------------
	def get_node_offset(self,n):
		bdXvec = Vector2(self.xpos(),0)
		nXvec  = Vector2(n.xpos(),0)
	
		bdYvec = Vector2(self.ypos(),0)
		nYvec = Vector2(n.ypos(),0)
	
		x = bdXvec.distanceBetween(nXvec)
		y = bdYvec.distanceBetween(nYvec)
	
		offset = Vector2(x,y)
		return offset
	#----------------------------------------------------------------------
	@property
	def nodes_offset_dict(self):
		res = {}
		for n in self.nodes:
			res[n]=self.get_node_offset(n)
		return res
	#----------------------------------------------------------------------
	def apply_node_Offset(self,offset_data):
		v1 = Vector2(self.xpos(),self.ypos())
		for n,v in offset_data.items():
			v = v1 + v
			n.setXYpos(int(v.x),int(v.y))
	#----------------------------------------------------------------------
	@property
	def center(self):
		return Vector2(self._box.centerX,self._box.centerY)
	#----------------------------------------------------------------------
	def get_Top_Left(self):
		bd_xy = Vector2(self.xpos(),self.ypos())
		return bd_xy
	#----------------------------------------------------------------------
	def get_Bottom_Left(self):
		bd_wh = Vector2(self.bdwidth,self.bdheight)
		bd_xy = Vector2(self.xpos(),self.ypos())
		res   = Vector2(bd_xy.x,bd_xy.y+bd_wh.y)
		return res
	#----------------------------------------------------------------------
	def get_Top_Right(self):
		bd_wh = Vector2(self.bdwidth,self.bdheight)
		bd_xy = Vector2(self.xpos(),self.ypos())
		res   = Vector2(bd_xy.x+bd_wh.x,bd_xy.y)
		return res
	#----------------------------------------------------------------------
	def get_Bottom_Right(self):
		bd_wh = Vector2(self.bdwidth,self.bdheight)
		bd_xy = Vector2(self.xpos(),self.ypos())
		res   = Vector2(bd_xy.x+bd_wh.x,bd_xy.y+bd_wh.y)
		return res
	#----------------------------------------------------------------------
	@wrapper_Auto_Update_Box
	def set_Top_Left(self,x,y):
		self.extend_Left(x)
		self.extend_Up(y)
	#----------------------------------------------------------------------
	@wrapper_Auto_Update_Box
	def set_Top_Right(self,x,y):
		# Get The Current pos
		current = self.get_Top_Right()
		vec1 = Vector2(y,0)
		vec2 = Vector2(y,0)
		yd = vec1.distanceBetween(vec2)

		old_x = self.xpos()
		vec1 = Vector2(old_x,0)
		self.setXpos(x)
		vec2 = Vector2(self.xpos(),0)
		xd = vec1.distanceBetween(vec2)

		offset = Vector2(xd,yd)

		if y > current:
			self.bdwidth = self.bdwidth + offset.y
		else:
			self.bdwidth = self.bdwidth + (offset.y * -1)

		if x > self.R:
			self.bdheight = self.bdheight + offset.x
		else:
			self.bdheight = self.bdheight + (offset.x * -1)
	#----------------------------------------------------------------------
	@wrapper_Auto_Update_Box
	def set_Bottom_Left(self,x,y):
		old_L = self.L
		vec1 = Vector2(self.L,0)
		self._nukeNode.setXpos(x)
		vec2 = Vector2(self.L,0)
		xd = vec1.distanceBetween(vec2)
		vec1 = Vector2(self.B,0)
		vec2 = Vector2(y,0)
		yd = vec1.distanceBetween(vec2)
		offset = Vector2(xd,yd)

		if x < old_L:
			self.bdwidth = self.bdwidth + offset.x
		else:
			self.bdwidth = self.bdwidth + (offset.x * -1)

		if y > self.B:
			self.bdheight = self.bdheight + offset.y
		else:
			self.bdheight = self.bdheight + (offset.y * -1)
	#----------------------------------------------------------------------
	@wrapper_Auto_Update_Box
	def set_Bottom_Right(self,x,y):
		vec1 = Vector2(self.R,0)
		vec2 = Vector2(x,0)
		xd = vec1.distanceBetween(vec2)
		vec1 = Vector2(self.B,0)
		vec2 = Vector2(y,0)
		yd = vec1.distanceBetween(vec2)
		offset = Vector2(xd,yd)

		if x > self.R:
			self.bdwidth = self.bdwidth + offset.x
		else:
			self.bdwidth = self.bdwidth + (offset.x * -1)

		if y > self.B:
			self.bdheight = self.bdheight + offset.y
		else:
			self.bdheight = self.bdheight + (offset.y * -1)
	#----------------------------------------------------------------------
	@wrapper_Auto_Apply_Offset
	def extend_Left(self,val):
		old = self.get_Top_Left()
		self.x = self.x - val
		new = self.get_Top_Left()
		dif = new.distanceBetween(old)
		self.extend_Right(dif)
	#----------------------------------------------------------------------
	@wrapper_Auto_Update_Box
	def extend_Right(self,val):
		self.bdwidth = self.bdwidth + val
	#----------------------------------------------------------------------
	@wrapper_Auto_Apply_Offset
	def extend_Up(self,val):
		old = self.get_Bottom_Right()
		self.y = self.y - val
		new = self.get_Bottom_Right()
		dif = new.distanceBetween(old)
		self.extend_Down(dif)
	#----------------------------------------------------------------------
	@wrapper_Auto_Update_Box
	def extend_Down(self,val):
		self.bdheight = self.bdheight + val
	#----------------------------------------------------------------------
	@wrapper_Auto_Apply_Offset
	def Offset(self,x=0,y=0):
		x = self.xpos()+x
		y = self.ypos()+y
		self.setXYpos(x,y)
	#----------------------------------------------------------------------
	@wrapper_Auto_Apply_Offset
	def Move(self,x=0,y=0):
		self.setXYpos(x,y)
	#----------------------------------------------------------------------
	@property
	def L(self):
		return self.xpos()
	#----------------------------------------------------------------------
	@property
	def T(self):
		return self.ypos()
	#----------------------------------------------------------------------
	@property
	def R(self):
		return self.get_Bottom_Right().x
	#----------------------------------------------------------------------
	@property
	def B(self):
		return self.get_Bottom_Right().y