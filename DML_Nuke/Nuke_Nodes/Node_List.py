from . import Vector2
import nuke
from functools import wraps
import sys

#----------------------------------------------------------------------
def wrapper_Empty_List_To_Selected(func):
	''' '''
	@wraps(func)
	def wrapper(*args, **kws):
		err = None
		try:
			if len(kws.get("listOfNodes",[])):
				kws["listOfNodes"]=nuke.selectedNodes()
			res=func(*args, **kws)
		except Exception as error:
			err=error
		finally:
			if err:
				traceback = sys.exc_info()[2]  # get the full traceback
				raise Exception(Exception(err), traceback)
			return res
	return wrapper

#----------------------------------------------------------------------
@wrapper_Empty_List_To_Selected
def reorder_By_X_Value(listOfNodes=[],reverse=False):
	return sorted(listOfNodes, key=lambda n: n.xpos(),reverse=reverse)

#----------------------------------------------------------------------
@wrapper_Empty_List_To_Selected
def reorder_By_Y_Value(listOfNodes=[],reverse=False):
	return sorted(listOfNodes, key=lambda n: n.ypos(),reverse=reverse)

#----------------------------------------------------------------------
@wrapper_Empty_List_To_Selected
def reorder_By_XY_Value(listOfNodes=[],reverse=False):
	if not len(listOfNodes):
		listOfNodes = nuke.selectedNodes()
	return sorted(listOfNodes, key=lambda n: Vector2(n.xpos(),n.ypos()),reverse=reverse)


#----------------------------------------------------------------------
def right_node(listOfNodes=[]):
	return reorder_By_X_Value(listOfNodes,True)[0]
#----------------------------------------------------------------------
def left_node(listOfNodes=[]):
	return reorder_By_X_Value(listOfNodes)[0]
#----------------------------------------------------------------------
def bottom_node(listOfNodes=[]):
	return reorder_By_Y_Value(listOfNodes,True)[0]
#----------------------------------------------------------------------
def top_node(listOfNodes=[]):
	return reorder_By_Y_Value(listOfNodes)[0]


class Node_List(list):
	########################################################################
	class Directions(object):
		top    = 1
		bottom = 2
		left   = 3
		right  = 4
	#----------------------------------------------------------------------
	def reorder_By_X_Value(self,reverse=False):
		""""""
		self.sort(key=lambda n: n.xpos(), reverse=reverse)
		return self
	#----------------------------------------------------------------------
	def reorder_By_Y_Value(self,reverse=False):
		""""""
		self.sort(key=lambda n: n.ypos(), reverse=reverse)
		return self
	#----------------------------------------------------------------------
	def reorder_By_Name(self,reverse=False):
		""""""
		self.sort(key=lambda n: n.fullName, reverse=reverse)
		return self
	#----------------------------------------------------------------------
	@property
	def top_node(self):
		""""""
		return top_node(self)
	#----------------------------------------------------------------------
	@property
	def right_node(self):
		""""""
		return right_node(self)
	#----------------------------------------------------------------------
	@property
	def left_node(self):
		""""""
		return left_node(self)
	#----------------------------------------------------------------------
	@property
	def bottom_node(self):
		""""""
		return bottom_node(self)
	#----------------------------------------------------------------------
	@property
	def center(self):
		Xpositions = [ n.x+n.screenWidth/2 for n in self]
		Ypositions = [ n.y+n.screenHeight/2 for n in self]
		try:
			x = float( sum( Xpositions ) ) / len( self )
			y = float( sum( Ypositions ) ) / len( self )
			return Vector2(x,y)
		except ZeroDivisionError:
			return Vector2(0,0)
	#----------------------------------------------------------------------	
	def aline_To_Center(self,direction="h"):
		'''Align nodes either horizontally or vertically.'''
		if len(self):
			if direction == "v":
				avrg = int(self.center.y)
				[n.setYpos(avrg) for n in self]
			if direction == "h":
				avrg = int(self.center.x)
				[n.setXpos(avrg) for n in self]
	#----------------------------------------------------------------------
	def scale_From_Center(self,value, direction="h"):
		if not value == None:
			value = float(value)
			amount = len( self )
			if len( self ):
				center = self.center
				
				if direction == "v":
					[n.setYpos( int(center.y + ( n.ypos() - center.y ) * value) ) for n in self]
				if direction == "h":
					[n.setXpos( int(center.x + ( n.xpos() - center.x ) * value) ) for n in self]
					
	#----------------------------------------------------------------------
	def apply_Offset(self,xOffsetValue=0, YOffsetValue=0):
	
		nodeCount = len(self)
		
		if nodeCount:
			if xOffsetValue:
				self.reorder_By_X_Value()
				for i in range(1,nodeCount,1):
					self[i].setXpos( int(float( self[i-1].xpos() + xOffsetValue )) )
		
			if YOffsetValue:
				self.reorder_By_Y_Value()
				for i in range(1,nodeCount,1):
					self[i].setYpos( int(float( self[i-1].ypos() + YOffsetValue )) )
				
	def vertically_stack_node_list(self,offset=100,sort_by_name=False, x=None,y=None):
		if len(self):
			nodes = Node_List(self)
			if sort_by_name:
				nodes.reorder_By_Name()
				
			n = nodes.left_node
			
			if x is None:
				x = n.xpos()
			if y is None:
				y = n.ypos()
		
			for i in range(0,len(nodes)):
				nodes[i].setXYpos( x, y + ( offset * i ) )
				
	def horizontaly_stack_node_list(self,offset=100,sort_by_name=False, x=None,y=None):
		if len(self):
			nodes = Node_List(self)
			if sort_by_name:
				nodes.reorder_By_Name()
				
			n = nodes.left_node
			
			if x is None:
				x = n.xpos()
			if y is None:
				y = n.ypos()
		
			for i in range(0,len(nodes)):
				nodes[i].setXYpos( x + ( offset * i ) , y )
				
				
	def calculate_bounds(self):
		# Calculate bounds for the nodes.
		bdX = min([node.xpos() for node in self])
		bdY = min([node.ypos() for node in self])
		bdW = max([node.xpos() + node.screenWidth for node in self]) - bdX
		bdH = max([node.ypos() + node.screenHeight for node in self]) - bdY
		
		# Expand the bounds to leave a little border. Elements are offsets for left, top, right and bottom edges respectively
		left, top, right, bottom = (-10, -80, 10, 30)
		bdX += left
		bdY += top
		bdW += (right - left)
		bdH += (bottom - top)
	
		# Expand the bounds to leave a little border. Elements are offsets for left, top, right and bottom edges respectively
		#left, top, right, bottom = (-50, -50, 50, 50)
		#bdX += left
		#bdY += top
		#bdW += (right - left)
		#bdH += (bottom - top)
		return bdX,bdY,bdW,bdH