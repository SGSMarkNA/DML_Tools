import os
from Data_Encoding import Read_CSV,Write_CSV
########################################################################
class _Base_Object(object):
	"""The Base Class That All Other Classes"""
		
########################################################################
class Name_Association(_Base_Object):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,name,associations=[]):
		"""Constructor"""
		self.name = name
		self._associations = associations
	#----------------------------------------------------------------------
	def Add_Association(self,name):
		"""Adds a new association if it does not allready exist"""
		if not name in self:
			self._associations.append(name)
	#----------------------------------------------------------------------
	def Remove_Association(self,name):
		"""Removes the given name from the list of associations"""
		if name in self:
			self._associations.remove(name)
	#----------------------------------------------------------------------
	def __iter__(self):
		""""""
		for item in self._associations:
			yield item
	#----------------------------------------------------------------------
	def __getitem__(self,key):
		""""""
		return self._associations[key]
	#----------------------------------------------------------------------
	def __contains__(self,val):
		"""Checks weather or not the input name exist witin the associations"""
		return val in self._associations
	#----------------------------------------------------------------------
	def __repr__(self):
		""""""
		return "Name_Association('{}',associations={})".format(self.name,self._associations)
	#----------------------------------------------------------------------
	@property
	def associations(self):
		""""""
		return self._associations
		
########################################################################
class Name_Associations(_Base_Object):
	"""Holds A list That Name_Association objects"""
	#----------------------------------------------------------------------
	def __init__(self,name_associations=[]):
		"""Constructor"""
		self._name_associations = name_associations
	#----------------------------------------------------------------------
	def Add_Name_Association(self,name,associations=[]):
		"""Adds a new association if it does not allready exist"""
		if not name in self:
			if isinstance(name,basestring):
				name = Name_Association(name, associations=associations)
			self._name_associations.append(name)
			return name
	#----------------------------------------------------------------------
	def Remove_Name_Association(self,name):
		"""Removes the given name from the list of associations"""
		if name in self:
			if isinstance(name,basestring):
				for item in self:
					if item.name == name:
						self._name_associations.remove(item)
		
	#----------------------------------------------------------------------
	@property
	def names(self):
		"""Returns all key names"""
		return [item.name for item in self]
	
	#----------------------------------------------------------------------
	def __iter__(self):
		""""""
		for item in self._name_associations:
			yield item
	#----------------------------------------------------------------------
	def __contains__(self,name):
		"""Checks weather or not the input exist witin the associations"""
		if name in self._name_associations:
			return True
		return name in self.names
	#----------------------------------------------------------------------
	def __getitem__(self,val):
		""""""
		if type(val) == int or type(val) == slice:
			return self._name_associations[val]
		if isinstance(val,basestring):
			if not val in self:
				raise KeyError("{} does not exist in the name associations".format(val))
			else:
				for item in self._name_associations:
					if item.name == val:
						return item.associations
		else:
			raise TypeError("{} is an invalid type key type".format(val))

########################################################################
class Name_Associations_Data(_Base_Object):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,file_location=None,label="Name Associations"):
		"""Constructor"""
		self.file_location = file_location
		self.label = label
		self._data = None
		if file_location != None and self._File_Exists():
			self.Load()
		if False:
			self.Remove_Name_Association = self.data.Remove_Name_Association
			self.Add_Name_Association = self.data.Add_Name_Association
			self.names = self.data.names
	#----------------------------------------------------------------------
	def _File_Exists(self):
		"""check weather or not the file location is valid returns true if file exists"""
		return os.path.exists(self.file_location)
	
	#----------------------------------------------------------------------
	def _Read_File_Data(self):
		""""""
		path, extension = os.path.splitext(self.file_location)
		if extension == ".csv":
			try:
				file_data = Read_CSV(self.file_location)
				return file_data
			except:
				raise OSError("Could read csv file '{}'".format(self.file_location))
		else:
			raise OSError("The current file type '{}' could not be determined or is not a valid format".format(extension))
	#----------------------------------------------------------------------
	def Load(self,fp=None):
		"""Loads the json file"""
		if fp == None:
			fp = self.file_location
			
		if fp == None or not len(fp):
			raise OSError("This Name Associations Data has not yet been given a file location to load from")
		
		if not self._File_Exists():
			raise OSError("The file location for this This Name Associations Data does not exist")
		
		file_data = self._Read_File_Data()
		name_associations = []
		
		for item_set in file_data:
			name,associations = item_set
			buffer_data = Name_Association(name, associations)
			name_associations.append( buffer_data)
			
		self._data = Name_Associations(name_associations)
		
	#----------------------------------------------------------------------
	def Save(self,fp=None):
		"""Loads the json file"""
		if fp is not None:
			try:
				Write_CSV(self.data)
				self.file_location = fp
				return True
			except OSError:
				return False
		else:		
			if self.file_location == None or not len(self.file_location):
				raise OSError("This Name Associations Data has not yet been given a file location to load from")
			else:
				try:
					Write_CSV(self.data,fp=self.file_location)
					return True
				except:
					return False
				
	#----------------------------------------------------------------------
	@property
	def data(self):
		""""""
		return self._data
	
	#----------------------------------------------------------------------
	def __getattribute__(self,name):
		""""""
		try:
			return object.__getattribute__(self,name)
		except AttributeError:
			try:
				return object.__getattribute__(object.__getattribute__(self,"data"),name)
			except AttributeError:
				raise AttributeError()
	
########################################################################
class Name_Association_Manager(_Base_Object):
	""""""
	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		
test_data = Name_Associations_Data(file_location=r"D:\aw_config\Git_Live_Code\Global_Systems\DML_Tools\DML_Applications\Auto_Shader_Assignment\TestData.csv", label="Name Associations")

