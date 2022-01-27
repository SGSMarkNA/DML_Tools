import os
from .Data_Encoding import Read_CSV,Write_CSV
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
			return True
		else:
			return False
	#----------------------------------------------------------------------
	def Remove_Association(self,name):
		"""Removes the given name from the list of associations"""
		if name in self:
			self._associations.remove(name)
			return True
		else:
			return False
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
		self._metaData = {}
	#----------------------------------------------------------------------
	def Add_Name_Association(self,name,associations=[]):
		"""Adds a new association if it does not allready exist"""
		if not name in self:
			if isinstance(name,str):
				name = Name_Association(name, associations=associations)
			self._name_associations.append(name)
			return name
		else:
			return False
	#----------------------------------------------------------------------
	def Remove_Name_Association(self,name):
		"""Removes the given name from the list of associations"""
		if name in self:
			if isinstance(name,str):
				for item in self:
					if item.name == name:
						self._name_associations.remove(item)
						return True
		return False
		
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
		if isinstance(val,str):
			if not val in self:
				raise KeyError("{} does not exist in the name associations".format(val))
			else:
				for item in self._name_associations:
					if item.name == val:
						return item.associations
		else:
			raise TypeError("{} is an invalid type key type".format(val))

########################################################################
class Name_List_Item(str):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,name):
		"""Constructor"""
		super(Name_List_Item,self).__init__(name)

########################################################################
class Name_List_Data(_Base_Object):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,file_location=None):
		"""Constructor"""
		self.file_location = file_location
		self._data = []
		if file_location != None and self._File_Exists():
			self.Load()
	#----------------------------------------------------------------------
	def Clear(self):
		""""""
		self._data = []
	#----------------------------------------------------------------------
	def _File_Exists(self):
		"""check weather or not the file location is valid returns true if file exists"""
		return os.path.exists(self.file_location)
	#----------------------------------------------------------------------
	def _Read_File_Data(self,fp=None):
		""""""
		try:
			with open(fp,"r") as f:
				data = f.read()
				res = sorted(data.splitlines())
		except:
			raise OSError("Could read file '{}'".format(fp))
		return res
	#----------------------------------------------------------------------
	def Add_Name(self,name):
		""""""
		if not name in self._data:
			self.data.append(Name_List_Item(name))
			return True
		else:
			return False
	#----------------------------------------------------------------------
	def Remove_Name(self,name):
		""""""
		if name in self._data:
			self.data.remove(name)
			return True
		else:
			return False
	#----------------------------------------------------------------------
	def Load(self,fp=None):
		"""Loads the names from file"""
		if fp == None:
			fp = self.file_location
		
		if fp == None or not len(fp):
			raise OSError("This Data has not yet been given a file location to load from")
		
		if not os.path.exists(fp):
			raise OSError("The file at location {} does not exist".format(fp))
		self._data = []
		for name in self._Read_File_Data(fp):
			self.Add_Name(name)
		self.file_location = fp
	#----------------------------------------------------------------------
	def Save(self,fp=None):
		"""Save the names to file"""
		if fp is None:
			fp = self.file_location
			
		if fp == None or not len(fp):
			raise OSError("This Data has not yet been given a file location to Save To")
		try:
			with open(fp,"w") as f:
				f.write("\n".join(sorted(self._data)))
		except:
			raise OSError("Could not write data to file {}".format(fp))
		
		self.file_location = fp
	#----------------------------------------------------------------------
	@property
	def data(self):
		""""""
		return self._data

########################################################################
class Name_Associations_Data(_Base_Object):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,file_location=None):
		"""Constructor"""
		self.file_location = file_location
		self._data = Name_Associations([Name_Association("None", associations=[])])
		if file_location != None and self._File_Exists():
			self.Load()
	#----------------------------------------------------------------------
	def _File_Exists(self):
		"""check weather or not the file location is valid returns true if file exists"""
		return os.path.exists(self.file_location)
	#----------------------------------------------------------------------
	def _Read_File_Data(self,fp):
		""""""
		path, extension = os.path.splitext(fp)
		if extension == ".csv":
			try:
				file_data = Read_CSV(fp)
				return file_data
			except:
				raise OSError("Could read csv file '{}'".format(fp))
		else:
			raise OSError("The current file type '{}' could not be determined or is not a valid format".format(extension))
	#----------------------------------------------------------------------
	def Load(self,fp=None):
		"""Loads the json file"""
		if fp == None:
			fp = self.file_location
			
		if fp == None or not len(fp):
			raise OSError("This Name Associations Data has not yet been given a file location to load from")
		
		if not os.path.exists(fp):
			raise OSError("The file location for this This Name Associations Data does not exist")
		
		file_data = self._Read_File_Data(fp)
		self.file_location = fp
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
				Write_CSV(self.data,fp)
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
class Name_Associations_Data_Location_Manager(_Base_Object):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,file_location=None):
		"""Constructor"""
		if not file_location is None and len(file_location):
			self._file_location = file_location
		else:
			self._file_location = None
		self.name_associations = Name_Associations_Data()
		self.name_list         = Name_List_Data()
	#----------------------------------------------------------------------
	def set_File_Location(self,fp):
		""""""
		if not fp is None and len(fp):
			path,ext = os.path.splitext(fp)
			path += ".nadlm"
			self._file_location = path
	#----------------------------------------------------------------------
	def get_File_Location(self):
		""""""
		return self._file_location
	#----------------------------------------------------------------------
	def _Read_File_Data(self,fp=None):
		""""""
		try:
			with open(fp,"r") as f:
				data = f.read()
				res = data.splitlines()
		except:
			raise OSError("Could read file '{}'".format(fp))
		if not len(res) == 2:
			raise ValueError("The file '{}' has an invalied number of file path values".format(fp))
		return res
	#----------------------------------------------------------------------
	def Load(self,fp=None):
		"""Loads the names from file"""
		if fp == None:
			fp = self._file_location
		
		if fp == None or not len(fp):
			raise OSError("This Data has not yet been given a file location to load from")
		
		if not os.path.exists(fp):
			raise OSError("The file at location {} does not exist".format(fp))
		
		associations_file_path,names_file_path = self._Read_File_Data(fp)
		self.name_associations.Load(associations_file_path)
		self.name_list.Load(names_file_path)
		self._file_location = fp
	#----------------------------------------------------------------------
	def Save(self,fp=None):
		"""Save the names to file"""
		if fp is None:
			fp = self._file_location
		else:
			self.set_File_Location(fp)
		
		if self._file_location == None or not len(self._file_location):
			raise OSError("This Data has not yet been given a file location to Save To")

		if self.name_associations.file_location == None:
			self.name_associations.file_location = os.path.splitext(self._file_location)[0]+".csv"
		if self.name_list.file_location == None:
			self.name_list.file_location = os.path.splitext(self._file_location)[0]+".txt"
		
		self.name_associations.Save()
		self.name_list.Save()
		try:
			with open(fp,"w") as f:
				f.write("\n".join([self.name_associations.file_location,self.name_list.file_location]))
		except:
			raise OSError("Could not write data to file {}".format(fp))
		

