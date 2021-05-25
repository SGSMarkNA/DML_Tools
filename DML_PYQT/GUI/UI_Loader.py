from .. import QT

class UiLoader(QT.QUiLoader):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(UiLoader,self).__init__(*args,**kwargs)
		self._custom_wigets = dict()
		self._wigs = []
		self._lays = []
	#----------------------------------------------------------------------
	def availableLayouts(self):
		"""
		Returns a list naming all available layouts that can be built using the PySide.QtUiTools.QUiLoader.createLayout() function
		"""
		res = super(UiLoader,self).availableLayouts()
		return res
	#----------------------------------------------------------------------
	def availableWidgets(self):
		"""
		Returns a list naming all available widgets that can be built using the PySide.QtUiTools.QUiLoader.createWidget() function, i.e all the widgets specified within the given plugin paths.
		"""
		res = super(UiLoader,self).availableWidgets()
		return res
	#----------------------------------------------------------------------
	def clearPluginPaths(self):
		"""
		Clears the list of paths in which the loader will search when locating plugins.
		"""
		res = super(UiLoader,self).clearPluginPaths()
		return res
	#----------------------------------------------------------------------
	def pluginPaths(self):
		"""
		Returns a list naming the paths in which the loader will search when locating custom widget plugins.
		"""
		res = super(UiLoader,self).pluginPaths()
		return res
	#----------------------------------------------------------------------
	def workingDirectory(self):
		"""
		Returns the working directory of the loader.
		"""
		res = super(UiLoader,self).workingDirectory()
		isinstance(QT.QDir)
		return res
	#----------------------------------------------------------------------
	def createAction(self,parent=None,name=None):
		"""
		createAction(parent=None,name=None)
			parent=QtCore.QObject
			name=unicode

		Creates a new action with the given parent and name .
		The function is also used internally by the PySide.QtUiTools.QUiLoader class whenever it creates a widget
		Hence, you can subclass PySide.QtUiTools.QUiLoader and reimplement this function to intervene process of constructing a user interface or widget
		However, in your implementation, ensure that you call PySide.QtUiTools.QUiLoader s version first.
		"""
		res = super(UiLoader,self).createAction(parent,name)
		isinstance(res,QT.QAction)
		return res
	#----------------------------------------------------------------------
	def createActionGroup(self,parent=None,name=None):
		"""
		createActionGroup(parent=None,name=None)
			parent=QtCore.QObject
			name=unicode

		Creates a new action group with the given parent and name .
		The function is also used internally by the PySide.QtUiTools.QUiLoader class whenever it creates a widget
		Hence, you can subclass PySide.QtUiTools.QUiLoader and reimplement this function to intervene process of constructing a user interface or widget
		However, in your implementation, ensure that you call PySide.QtUiTools.QUiLoader s version first.
		"""
		res = super(UiLoader,self).createActionGroup(parent,name)
		isinstance(res,QT.QActionGroup)
		return res
	#----------------------------------------------------------------------
	def createLayout(self,className,parent=None,name=None):
		"""
		createLayout(className,parent=None,name=None)
			className=unicode
			parent=QtCore.QObject
			name=unicode

		Creates a new layout with the given parent and name using the class specified by className .
		The function is also used internally by the PySide.QtUiTools.QUiLoader class whenever it creates a widget
		Hence, you can subclass PySide.QtUiTools.QUiLoader and reimplement this function to intervene process of constructing a user interface or widget
		However, in your implementation, ensure that you call PySide.QtUiTools.QUiLoader s version first.
		"""
		res = super(UiLoader,self).createLayout(className,parent,name)
		isinstance(res,QT.QLayout)
		self._lays.append(res)
		return res
	#----------------------------------------------------------------------
	def createWidget(self,className,parent=None,name=None):
		"""
		createWidget(className,parent=None,name=None)
			className=unicode
			parent=QtGui.QWidget
			name=unicode

		Creates a new widget with the given parent and name using the class specified by className
		You can use this function to create any of the widgets returned by the PySide.QtUiTools.QUiLoader.availableWidgets() function.
		The function is also used internally by the PySide.QtUiTools.QUiLoader class whenever it creates a widget
		Hence, you can subclass PySide.QtUiTools.QUiLoader and reimplement this function to intervene process of constructing a user interface or widget
		However, in your implementation, ensure that you call PySide.QtUiTools.QUiLoader s version first.
		"""
		if className in self._custom_wigets:
			if not parent == None:
				res = self._custom_wigets[className](parent=parent)
			else:
				res = self._custom_wigets[className]()
			res.setObjectName(name)
		else:
			res = super(UiLoader,self).createWidget(className,parent,name)
		isinstance(res,QT.QWidget)
		self._wigs.append(res)
		return res
	#----------------------------------------------------------------------
	def load(self,*args,**kwargs):
		"""
		load(device,parentWidget=None)
			device=QtCore.QIODevice
			parentWidget=QtGui.QWidget

		load(arg__1,parentWidget=None)
			arg__1=unicode
			parentWidget=QtGui.QWidget

		Loads a form from the given device and creates a new widget with the given parentWidget to hold its contents.
		"""
		res = super(UiLoader,self).load(*args,**kwargs)
		isinstance(res,QT.QWidget)
		return res
	#----------------------------------------------------------------------
	def load_file(self, file_path, parent_widget=None):
		""""""
		Qfile = QT.QFile(file_path)
		Qfile.open(QT.QFile.ReadOnly)
		ui_wig = self.load(Qfile,parent_widget)
		Qfile.close()
		return ui_wig
	#----------------------------------------------------------------------
	def registerCustomWidget(self,customWidgetType):
		"""
		registerCustomWidget(customWidgetType)
			customWidgetType=Object

		Registers a Python created custom widget to QUiLoader, so it can be recognized when
		loading a .ui file
		The custom widget type is passed via the customWidgetType argument.
		This is needed when you want to override a virtual method of some widget in the interface,
		since duck punching will not work with widgets created by QUiLoader based on the contents
		of the .ui file.
		(Remember that duck punching virtual methods is an invitation for your own demise!)
		Lets see an obvious example
		If you want to create a new widget its probable youll end up
		overriding QWidgets paintEvent() method.
		"""
		self._custom_wigets[customWidgetType.__name__] = customWidgetType
		res = super(UiLoader,self).registerCustomWidget(customWidgetType)
		return res
	#----------------------------------------------------------------------
	def setWorkingDirectory(self,dir):
		"""
		setWorkingDirectory(dir)
			dir=QtCore.QDir

		Sets the working directory of the loader to dir
		The loader will look for other resources, such as icons and resource files, in paths relative to this directory.
		"""
		res = super(UiLoader,self).setWorkingDirectory(dir)
		return res
	
GUI_Loader = UiLoader()