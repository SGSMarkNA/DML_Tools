import os
import DML_Tools
DML_PYQT = DML_Tools.DML_PYQT
import nuke
import _nuke
import uuid

########################################################################
class Update_Actions(object):
	""""""
	__metaclass__ = DML_Tools.DML_General_Utilities.Generic_Classes.Singleton
	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		self.skip_update = False
		self.external_change = True
		
UPDATE_ACTIONS = Update_Actions()
nuke.__dict__["DML_NUKE_VIEWS_UPDATE_ACTIONS"] = UPDATE_ACTIONS

########################################################################
class _CallBack_Singles(DML_PYQT.QObject):
	"""A Signal That Is A emited whatever a knob has changed on any node that has a Python Widget Knob Attached To It"""
	Root_Views_Knob_Chaged  = DML_PYQT.Signal()
	View_Renamed            = DML_PYQT.Signal(str,object)
	View_About_To_Be_Remove = DML_PYQT.Signal(object)
	View_Remove             = DML_PYQT.Signal(object)
	Views_Removed           = DML_PYQT.Signal(list)
	View_Added              = DML_PYQT.Signal(object)
	Views_Added             = DML_PYQT.Signal(list)
	View_Changed            = DML_PYQT.Signal(object)
	Views_Changed           = DML_PYQT.Signal(list)
	
CallBack_Singles = _CallBack_Singles()
nuke.__dict__["DML_NUKE_VIEWS_CALLBACK_SINGLES"] = CallBack_Singles

#----------------------------------------------------------------------
def view_To_Image_Name(filepath):
	for key in DML_Nuke_View_System._name_to_image.keys():
		if key in filepath.split("/"):
			filepath = filepath.replace(key,DML_Nuke_View_System.get_Image_Name_From_View_Name(key))
			return filepath
	return None
#----------------------------------------------------------------------
def on_Nuke_Root_View_Knob_Changed():
	if UPDATE_ACTIONS.external_change:
		if nuke.thisKnob().name() == "views":
			try:
				view_knob = nuke.root().knob("views")
			except ValueError:
				view_knob = None
			finally:
				if view_knob is not None:
					if DML_Nuke_View_System._needs_Update_Check():
						nuke.DML_Nuke_View_System._full_Rebuild()
						CallBack_Singles.Root_Views_Knob_Chaged.emit()
	if nuke.thisKnob().name() == "DML_nuke_views_system_use_image_name":
		if nuke.thisKnob().value():
			nuke.addFilenameFilter(view_To_Image_Name, nodeClass='*')
		else:
			nuke.removeFilenameFilter(view_To_Image_Name,nodeClass='*')

#----------------------------------------------------------------------
def parse_Nuke_Views(knob=None):
	""""""
	nuke_view_names = nuke.views()
	view_data = []
	try:
		if knob == None:
			views = nuke.root().knob("views").toScript()
		else:
			views = knob.toScript()
		views = views.replace("{","").replace("}","")
		views = views.splitlines()
		for view,nuke_view in zip(views,nuke_view_names):
			items = [nuke_view]
			if len(nuke_view.split()) > 1:
				view = view.replace('"'+nuke_view+'" ',"")
			else:
				view = view.replace(nuke_view+' ',"")
			view_items = view.split()
			items.extend(view_items)
			if len(items)==2:
				items.extend([items[0],str(uuid.uuid4())])
			view_data.append(items)
			
	except:
		pass
	return view_data

#----------------------------------------------------------------------
def RGB_To_Hex(*args):
	if len(args)==3:
		r,g,b = args[0], args[1], args[2]
		hexCol = '#%02x%02x%02x' % (r,g,b)	
	elif len(args)==1:
		if isinstance(args[0],DML_PYQT.QColor):
			r,g,b = args[0].red(), args[0].green(), args[0].blue()
			hexCol = '#%02x%02x%02x' % (r,g,b)
		elif isinstance(args[0],(int,long)):
			color = DML_PYQT.QColor.fromRgb(args[0])
			r,g,b = color.red(), color.green(), color.blue()
			hexCol = '#%02x%02x%02x' % (r,g,b)	
	else:
		raise ValueError("Cound Not Convert {} to hex value".format(args))
	return hexCol

#----------------------------------------------------------------------
def Hex_to_RGB(value):
	value = value.lstrip('#')
	lv = len(value)
	return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))



#----------------------------------------------------------------------
def get_QColor(arg):
	if isinstance(arg,DML_PYQT.QColor):
		return arg
	elif isinstance(arg,(list,tuple)):
		if len(arg)==3:
			r,g,b = arg[0], arg[1], arg[2]
			color = DML_PYQT.QColor(r,g,b)
		else:
			raise ValueError("bad input value")
	elif isinstance(arg,(int,long)):
		color = DML_PYQT.QColor.fromRgba(arg)
		return color
	elif isinstance(arg,str):
		if arg == "" or arg == '""':
			return DML_PYQT.QColor(DML_PYQT.Qt.GlobalColor.black)
		else:
			color = DML_PYQT.QColor(*Hex_to_RGB(arg))
		return color
	elif arg == None:
		return DML_PYQT.QColor(DML_PYQT.Qt.GlobalColor.black)
	else:
		raise ValueError("Wrong Type Of Input")

########################################################################
class Nuke_View(object):
	#----------------------------------------------------------------------
	def __init__(self,nuke_views,view_name,color=None,image_name=None,uid=None):
		self._nuke_views = nuke_views
		self._view_name = view_name
		self._color = get_QColor(color)
		self._image_name = image_name if not image_name==None else view_name
		self._mode = 0
		self._uid = uid if not uid == None else str(uuid.uuid4())
		if False:
			self.color=DML_PYQT.QColor()
	#----------------------------------------------------------------------
	@property
	def index(self):
		try:
			return nuke.views().index(self.name)
		except IndexError:
			return -1
	#----------------------------------------------------------------------
	@property
	def uid(self):
		return self._uid
	#----------------------------------------------------------------------
	@property
	def hex_color(self):
		""""""
		return RGB_To_Hex(self.color.red(),self.color.green(),self.color.blue())
	#----------------------------------------------------------------------
	@property
	def color(self):
		""""""
		return self._color
	#----------------------------------------------------------------------
	@color.setter
	def color(self,args):
		""""""
		self._color = get_QColor(args)
		if not UPDATE_ACTIONS.skip_update:
			UPDATE_ACTIONS.external_change = False
			self._nuke_views._update_Nuke_Views_Knob()
			UPDATE_ACTIONS.external_change = True
			if nuke.GUI:
				CallBack_Singles.View_Changed.emit(self)
	#----------------------------------------------------------------------
	def pick_Color(self):
		""""""
		new_color = color = DML_PYQT.QColorDialog.getColor(self.color)
		if not new_color == None:
			self.color = new_color
	#----------------------------------------------------------------------
	@property
	def name(self):
		return self._view_name
	#----------------------------------------------------------------------
	@name.setter
	def name(self, value):
		try:
			del self._nuke_views.self._name_to_image[self._view_name]
		except:
			pass
		
		self._view_name = value
		self._nuke_views.self._name_to_image[self._view_name]=self._image_name
		if not UPDATE_ACTIONS.skip_update:
			UPDATE_ACTIONS.external_change = False
			self._nuke_views._update_Nuke_Views_Knob()
			UPDATE_ACTIONS.external_change = True
			if nuke.GUI:
				CallBack_Singles.View_Changed.emit(self)
	#----------------------------------------------------------------------
	@property
	def image_name(self):
		return self._image_name
	#----------------------------------------------------------------------
	@image_name.setter
	def image_name(self, value):
		self._image_name = value
		self._nuke_views._name_to_image[self._view_name]=self._image_name
		if not UPDATE_ACTIONS.skip_update:
			UPDATE_ACTIONS.external_change = False
			self._nuke_views._update_Nuke_Views_Knob()
			UPDATE_ACTIONS.external_change = True
			if nuke.GUI:
				CallBack_Singles.View_Changed.emit(self)
	#----------------------------------------------------------------------
	def __str__(self):
		""""""
		return "{" + "{} {} {} {}".format(self.name,self.hex_color,self.image_name,self.uid) + "}"
	#----------------------------------------------------------------------
	def __repr__(self):
		""""""
		return self.__str__()
	#----------------------------------------------------------------------
	def __eq__(self,other):
		""""""
		if isinstance(other,str):
			return self.uid == other
		elif isinstance(other,Nuke_View):
			return self.uid == other.uid
		else:
			return False
########################################################################
class Nuke_Views(object):
	""""""
	__metaclass__ = DML_Tools.DML_General_Utilities.Generic_Classes.Singleton
	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		self.views = []
		self._uid_to_view = dict()
		self._name_to_image = dict()
		self._full_Rebuild()
		if False:
			isinstance(self.root_views_knob,nuke.Knob)
		
		if "DML_nuke_views_system_use_image_name" in nuke.root().knobs():
			if nuke.root().knob("DML_nuke_views_system_use_image_name").value():
				nuke.addFilenameFilter(view_To_Image_Name, nodeClass='*')
			else:
				nuke.removeFilenameFilter(view_To_Image_Name,nodeClass='*')
	#----------------------------------------------------------------------
	@property
	def root_views_knob(self):
		""""""
		return nuke.root().knob("views")
		
	#----------------------------------------------------------------------
	def _needs_Update_Check(self):
		""""""
		return str(self) != self.root_views_knob.toScript().replace("\n"," ")
	#----------------------------------------------------------------------
	def _full_Rebuild(self):
		""""""
		if self._needs_Update_Check():
			UPDATE_ACTIONS.external_change = False
			self.views = []
			self._uid_to_view = dict()
			view_data = parse_Nuke_Views()
			for name,color,image,uid in view_data:
				nuke_view = Nuke_View(self,name, color=color, image_name=image, uid=uid)
				self._internal_Add_View(nuke_view)
			self._update_Nuke_Views_Knob()
			if nuke.GUI:
				CallBack_Singles.Root_Views_Knob_Chaged.emit()
			UPDATE_ACTIONS.external_change = True
	#----------------------------------------------------------------------
	def _Update_On_Applacation_Changed(self,knob=None):
		""""""
		view_data = parse_Nuke_Views(knob=knob)
		nuke_uids = []
		views_changed = []
		views_removed = []
		views_added   = []
		for name,color,image,uid in view_data:
			nuke_uids.append(uid)
			nuke_view = self.get_View_By_Uid(uid)
			if nuke_view != None:
				if not nuke_view.name == name or not nuke_view.hex_color == color or not nuke_view.image_name == image:
					views_changed.append([nuke_view,name,color,image])
			else:
				nuke_view = Nuke_View(self,name, color=color, image_name=image, uid=uid)
				views_added.append(nuke_view)
				
		for nuke_view in self:
			if not nuke_view.uid in nuke_uids:
				views_removed.append(nuke_view)
				
		if len(views_added) or len(views_changed) or len(views_removed):
			UPDATE_ACTIONS.external_change = False
			UPDATE_ACTIONS.skip_update = True
			
			for nuke_view in views_added:
				self._internal_Add_View(nuke_view)
			if len(views_changed):
				for nuke_view,name,color,image in views_changed:
					nuke_view.name = name
					nuke_view.color = color
					nuke_view.image_name = image
			
			for nuke_view in views_removed:
				self._internal_Remove_View(nuke_view)
				
			self._update_Nuke_Views_Knob()
			
			UPDATE_ACTIONS.external_change = True
			UPDATE_ACTIONS.skip_update = False
			
		if nuke.GUI:
			if len(views_added):
				CallBack_Singles.Views_Added.emit(views_added)
			if len(views_changed):
				views = [v[0] for v in views_changed]
				CallBack_Singles.Views_Changed.emit(views)
			if len(views_removed):
				CallBack_Singles.Views_Removed(views_removed)
			CallBack_Singles.Root_Views_Knob_Chaged.emit()
				
	#----------------------------------------------------------------------
	def _internal_Add_View(self,nuke_view):
		""""""
		self.views.append(nuke_view)
		self._uid_to_view[nuke_view.uid]    = nuke_view
		self._name_to_image[nuke_view.name] = nuke_view.image_name
	#----------------------------------------------------------------------
	def _internal_Remove_View(self,nuke_view):
		""""""
		self.views.remove(nuke_view)
		del self._uid_to_view[nuke_view.uid]
		del self._name_to_image[nuke_view.name]
	#----------------------------------------------------------------------
	def _update_Nuke_Views_Knob(self):
		""""""
		if self._needs_Update_Check():
			old_value = UPDATE_ACTIONS.external_change
			UPDATE_ACTIONS.external_change = False
			self.root_views_knob.fromScript(str(self))
			UPDATE_ACTIONS.external_change = old_value
	#----------------------------------------------------------------------
	def get_View_By_Name(self,name):
		""""""
		res = None
		for v in self:
			isinstance(v,Nuke_View)
			if v.name == name:
				res = v
				break
		isinstance(res,Nuke_View)
		return res
	#----------------------------------------------------------------------
	def get_View_By_Uid(self,uid):
		""""""
		res = None
		if uid in self._uid_to_view:
			res = self._uid_to_view[uid]
		isinstance(res,Nuke_View)
		return res
	#----------------------------------------------------------------------
	def get_View_By_Image_Name(self,name):
		""""""
		res = None
		for v in self:
			isinstance(v,Nuke_View)
			if v.image_name == name:
				res = v
				break
		isinstance(res,Nuke_View)
		return res
	#----------------------------------------------------------------------
	def get_View_By_Index(self,index):
		""""""
		res = None
		for v in self:
			isinstance(v,Nuke_View)
			if v.index == index:
				res = v
				break
		isinstance(res,Nuke_View)
		return res
	#----------------------------------------------------------------------
	def get_Image_Name_From_View_Name(self,name):
		""""""
		view = self.get_View_By_Name(name)
		if view is not None:
			return view.image_name
		else:
			raise LookupError("No View Exists with the name {}".format(name))
	#----------------------------------------------------------------------
	def get_View_Name_From_Image_Name(self,name):
		""""""
		view = self.get_View_By_Image_Name(name)
		if view is not None:
			return view.name
		else:
			raise LookupError("No View Exists with the name {}".format(name))
	#----------------------------------------------------------------------
	@property
	def view_names(self):
		""""""
		return [view.name for view in self.views]
	#----------------------------------------------------------------------
	def add_View(self,name,color=None,image_name=None, uid=None):
		""""""
		UPDATE_ACTIONS.external_change = False
		nuke.addView(name)
		nuke_view = Nuke_View(self,name, color=color,image_name=image_name, uid=uid)
		self._internal_Add_View(nuke_view)
		self._update_Nuke_Views_Knob()
		UPDATE_ACTIONS.external_change = True
		if nuke.GUI:
			CallBack_Singles.View_Added.emit(nuke_view)
	#----------------------------------------------------------------------
	def remove_View(self,name):
		""""""
		nuke_view = self.get_View_By_Name(name)
		if nuke_view != None:
			UPDATE_ACTIONS.external_change = False
			nuke.deleteView(nuke_view.name)
			self._internal_Remove_View(nuke_view)
			UPDATE_ACTIONS.external_change = True
			if nuke.GUI:
				CallBack_Singles.View_Remove.emit(nuke_view)
	#----------------------------------------------------------------------
	def __iter__(self):
		""""""
		for v in self.views:
			yield v
	
	#----------------------------------------------------------------------
	def __str__(self):
		""""""
		return " ".join([str(v) for v in self])
	


DML_Nuke_View_System = Nuke_Views()
nuke.__dict__["DML_Nuke_View_System"]=DML_Nuke_View_System

#----------------------------------------------------------------------
def scriptOpen(*args):
	""""""
	res = _nuke.scriptOpen(*args)
	nuke.DML_Nuke_View_System._full_Rebuild()
	CallBack_Singles.Root_Views_Knob_Chaged.emit()
	print "scriptOpen"
	return res
#----------------------------------------------------------------------
def scriptClear():
	""""""
	res = _nuke.scriptClear()
	nuke.DML_Nuke_View_System._full_Rebuild()
	CallBack_Singles.Root_Views_Knob_Chaged.emit()
	print "scriptClear"
	return res

#----------------------------------------------------------------------
def scriptNew(*args):
	""""""
	res = _nuke.scriptNew(*args)
	nuke.DML_Nuke_View_System._full_Rebuild()
	CallBack_Singles.Root_Views_Knob_Chaged.emit()
	print "scriptNew"
	return res

#----------------------------------------------------------------------
def scriptClose():
	""""""
	res = _nuke.scriptClose()
	nuke.DML_Nuke_View_System._full_Rebuild()
	CallBack_Singles.Root_Views_Knob_Chaged.emit()
	print "scriptClose"
	return res
	
	
nuke.scriptClear = scriptClear
nuke.scriptNew = scriptNew
nuke.scriptOpen = scriptOpen
nuke.scriptClose = scriptClose

nuke.addKnobChanged(on_Nuke_Root_View_Knob_Changed, nodeClass='Root')
