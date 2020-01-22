
import nuke
import _nukemath
class Vector2(_nukemath.Vector2):

	def __init__(self,*args):
		if len(args) == 1 and hasattr(args[0],"xpos") and hasattr(args[0],"ypos"):
			args = float(args[0].xpos()),float(args[0].ypos())
		return super(Vector2,self).__init__(*args)

	def cross(self, *args):
		"""cross( (Vector2)arg1, (Vector2)arg2) -> float :"""
		return super(Vector2,self).cross(*args)

	def distanceBetween(self,*args):
		"""distanceBetween( (Vector2)arg1, (Vector2)arg2) -> float :"""
		return super(Vector2,self).distanceBetween(*args)

	def distanceSquared(self,*args):
		"""distanceSquared( (Vector2)arg1, (Vector2)arg2) -> float :"""
		return super(Vector2,self).distanceSquared(*args)

	def dot(self,*args):
		"""dot( (Vector2)arg1, (Vector2)arg2) -> float :"""
		return super(Vector2,self).dot(*args)

	def length(self):
		"""length( (Vector2)arg1) -> float :"""
		return super(Vector2,self).length()

	def lengthSquared(self):
		"""lengthSquared( (Vector3)arg1) -> float :"""
		return super(Vector2,self).lengthSquared()

	def negate(self):
		"""negate( (Vector2)arg1) -> None :"""
		return super(Vector2,self).negate()

	def normalize(self):
		"""normalize( (Vector2)arg1) -> float :"""
		return super(Vector2,self).normalize()

	def set(*args):
		"""set( (Vector2)arg1, (float)arg2) -> None :
		set( (Vector2)arg1, (float)arg2, (float)arg3) -> None :
		set( (Vector2)arg1, (Vector2)arg2) -> None :"""
		return super(Vector2,self).set(*args)

#class Vector3(Boost.Python.instance)

	#cross(self):
			#"""cross( (Vector3)arg1, (Vector3)arg2) -> Vector3 :
			
				#C++ signature :
					#class DD::Image::Vector3 cross(class DD::Image::Vector3 {lvalue},class DD::Image::Vector3)"""
	
	#distanceBetween(self):
		#"""distanceBetween( (Vector3)arg1, (Vector3)arg2) -> float :
		
			#C++ signature :
				#float distanceBetween(class DD::Image::Vector3 {lvalue},class DD::Image::Vector3)"""
	
	#distanceFromPlane(self):
		#"""distanceFromPlane( (Vector3)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5) -> float :
		
			#C++ signature :
				#float distanceFromPlane(class DD::Image::Vector3 {lvalue},float,float,float,float)"""
	
	#distanceSquared(self):
		#"""distanceSquared( (Vector3)arg1, (Vector3)arg2) -> float :
		
			#C++ signature :
				#float distanceSquared(class DD::Image::Vector3 {lvalue},class DD::Image::Vector3)"""
	
	#dot(self):
		#"""dot( (Vector3)arg1, (Vector3)arg2) -> float :
		
			#C++ signature :
				#float dot(class DD::Image::Vector3 {lvalue},class DD::Image::Vector3)"""
	
	#fast_normalize(self):
		#"""fast_normalize( (Vector3)arg1) -> float :
		
			#C++ signature :
				#float fast_normalize(class DD::Image::Vector3 {lvalue})"""
	
	#length(self):
		#"""length( (Vector3)arg1) -> float :
		
			#C++ signature :
				#float length(class DD::Image::Vector3 {lvalue})"""
	
	#lengthSquared(self):
		#"""lengthSquared( (Vector3)arg1) -> float :
		
			#C++ signature :
				#float lengthSquared(class DD::Image::Vector3 {lvalue})"""
	
	#maximum(self):
		#"""maximum( (Vector3)arg1, (Vector3)arg2) -> Vector3 :
		
			#C++ signature :
				#class DD::Image::Vector3 maximum(class DD::Image::Vector3 {lvalue},class DD::Image::Vector3)"""
	
	#minimum(self):
		#"""minimum( (Vector3)arg1, (Vector3)arg2) -> Vector3 :
		
			#C++ signature :
				#class DD::Image::Vector3 minimum(class DD::Image::Vector3 {lvalue},class DD::Image::Vector3)"""
	
	#negate(self):
		#"""negate( (Vector3)arg1) -> None :
		
			#C++ signature :
				#void negate(class DD::Image::Vector3 {lvalue})"""
	
	#normalize(self):
		#"""normalize( (Vector3)arg1) -> float :
		
			#C++ signature :
				#float normalize(class DD::Image::Vector3 {lvalue})"""
	
	#reflect(self):
		#"""reflect( (Vector3)arg1, (Vector3)arg2) -> Vector3 :
		
			#C++ signature :
				#class DD::Image::Vector3 reflect(class DD::Image::Vector3 {lvalue},class DD::Image::Vector3)"""
