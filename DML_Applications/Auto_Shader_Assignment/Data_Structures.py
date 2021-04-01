import os

########################################################################
class _Base_Object(object):
	"""The Base Class That All Other Classes"""

########################################################################
class Name_Associations_Data(_Base_Object):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,file_location="",label="Name Associations"):
		"""Constructor"""
		self.file_location = file_location
		self.label = label
		
	def _File_Exists(self):
		"""check weather or not the file location is valid returns true if file exists"""
		return os.path.exists(self.file_location)
		
	def Load(self):
		"""Loads the json file"""
		if not len(self.file_location):
			raise OSError("This data has not yet been given a file location to save to")
		if not self._File_Exists():
			raise FileNotFoundError("The location for this data does not exist")
		
class Name_Association(_Base_Object):
	""""""

	def __init__(self,name="",associations=[]):
		"""Constructor"""
		self.name = name
		self._associations = associations
		
	def Association_Exists(self,name):
		"""Checks weather or not the input name exist witin the associations"""
		return name in self._associations
	
	def Add_Association(self,name):
		"""Adds a new association if it does not allready exist"""
		if not self.Association_Exists(name):
			self._associations.append(name)
			
	def Remove_Association(self,name):
		"""Removes the given name from the list of associations"""
		if self.Association_Exists(name):
			self._associations.remove(name)
			
class Name_Associations(_Base_Object):
	"""Holds A list That Name_Association objects"""

	def __init__(self,name_associations=[]):
		"""Constructor"""
		self._name_associations = name_associations
		
	def Name_Association_Exists(self,name):
		"""Checks weather or not the input exist witin the associations"""
		if name in self._name_associations:
			return True
		return name in [item.name for item in self._name_associations]
	
	def Add_Name_Association(self,name):
		"""Adds a new association if it does not allready exist"""
		if not self.Association_Exists(name):
			self._associations.append(name)
			
	def Remove_Name_Association(self,name):
		"""Removes the given name from the list of associations"""
		if self.Association_Exists(name):
			self._associations.remove(name)
			
########################################################################
class Name_Associations_Manager(_Base_Object):
	""""""
	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		
		
    
	