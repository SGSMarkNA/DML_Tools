
from ... import QT
class Standard_QWidget(QT.QWidget):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(Standard_QWidget,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def acceptDrops(self):
		"""
		This property holds whether drop events are enabled for this widget.
		Setting this property to true announces to the system that this widget may be able to accept drop events.
		If the widget is the desktop ( PySide.QT.QWidget.windowType() == Qt.Desktop ), this may fail if another application is using the desktop; you can call PySide.QT.QWidget.acceptDrops() to test if this occurs.
		By default, this property is false.
		"""
		res = super(Standard_QWidget,self).acceptDrops()

		return res
	#----------------------------------------------------------------------
	def accessibleDescription(self):
		"""
		This property holds the widgets description as seen by assistive technologies.
		By default, this property contains an empty string.
		"""
		res = super(Standard_QWidget,self).accessibleDescription()
		return res
	#----------------------------------------------------------------------
	def accessibleName(self):
		"""
		This property holds the widgets name as seen by assistive technologies.
		This property is used by accessible clients to identify, find, or announce the widget for accessible clients.
		By default, this property contains an empty string.
		"""
		res = super(Standard_QWidget,self).accessibleName()
		return res
	#----------------------------------------------------------------------
	def actions(self):
		"""
		Returns the (possibly empty) list of this widgets actions.
		"""
		res = super(Standard_QWidget,self).actions()
		return res
	#----------------------------------------------------------------------
	def activateWindow(self):
		"""
		Sets the top-level widget containing this widget to be the active window.
		An active window is a visible top-level window that has the keyboard input focus.
		This function performs the same operation as clicking the mouse on the title bar of a top-level window
		On X11, the result depends on the Window Manager
		If you want to ensure that the window is stacked on top as well you should also call raise()
		Note that the window must be visible, otherwise PySide.QT.QWidget.activateWindow() has no effect.
		On Windows, if you are calling this when the application is not currently the active one then it will not make it the active window
		It will change the color of the taskbar entry to indicate that the window has changed in some way
		This is because Microsoft does not allow an application to interrupt what the user is currently doing in another application.
		"""
		res = super(Standard_QWidget,self).activateWindow()
		return res
	#----------------------------------------------------------------------
	def adjustSize(self):
		"""
		Adjusts the size of the widget to fit its contents.
		This function uses PySide.QT.QWidget.sizeHint() if it is valid, i.e., the size hints width and height are >= 0
		Otherwise, it sets the size to the children rectangle that covers all child widgets (the union of all child widget rectangles).
		For windows, the screen size is also taken into account
		If the PySide.QT.QWidget.sizeHint() is less than (200, 100) and the size policy is expanding , the window will be at least (200, 100)
		The maximum size of a window is 2/3 of the screens width and height.
		"""
		res = super(Standard_QWidget,self).adjustSize()
		return res
	#----------------------------------------------------------------------
	def autoFillBackground(self):
		"""
		This property holds whether the widget background is filled automatically.
		If enabled, this property will cause Qt to fill the background of the widget before invoking the paint event
		The color used is defined by the QPalette.Window color role from the widgets palette .
		In addition, Windows are always filled with QPalette.Window , unless the WA_OpaquePaintEvent or WA_NoSystemBackground attributes are set.
		This property cannot be turned off (i.e., set to false) if a widgets parent has a static gradient for its background.
		By default, this property is false.
		"""
		res = super(Standard_QWidget,self).autoFillBackground()

		return res
	#----------------------------------------------------------------------
	def backgroundRole(self):
		"""
		Returns the background role of the widget.
		The background role defines the brush from the widgets PySide.QT.QWidget.palette() that is used to render the background.
		If no explicit background role is set, the widget inherts its parent widgets background role.
		"""
		res = super(Standard_QWidget,self).backgroundRole()
		isinstance(res,QT.QPalette.ColorRole)
		return res
	#----------------------------------------------------------------------
	def baseSize(self):
		"""
		This property holds the base size of the widget.
		The base size is used to calculate a proper widget size if the widget defines PySide.QT.QWidget.sizeIncrement() .
		By default, for a newly-created widget, this property contains a size with zero width and height.
		"""
		res = super(Standard_QWidget,self).baseSize()
		isinstance(res,QT.QSize)
		return res
	#----------------------------------------------------------------------
	def childrenRect(self):
		"""
		This property holds the bounding rectangle of the widgets children.
		Hidden children are excluded.
		By default, for a widget with no children, this property contains a rectangle with zero width and height located at the origin.
		"""
		res = super(Standard_QWidget,self).childrenRect()
		isinstance(res,QT.QRect)
		return res
	#----------------------------------------------------------------------
	def childrenRegion(self):
		"""
		This property holds the combined region occupied by the widgets children.
		Hidden children are excluded.
		By default, for a widget with no children, this property contains an empty region.
		"""
		res = super(Standard_QWidget,self).childrenRegion()
		isinstance(res,QT.QRegion)
		return res
	#----------------------------------------------------------------------
	def clearFocus(self):
		"""
		Takes keyboard input focus from the widget.
		If the widget has active focus, a focus out event is sent to this widget to tell it that it is about to lose the focus.
		This widget must enable focus setting in order to get the keyboard input focus, i.e
		it must call PySide.QT.QWidget.setFocusPolicy() .
		"""
		res = super(Standard_QWidget,self).clearFocus()
		return res
	#----------------------------------------------------------------------
	def clearMask(self):
		"""
		Removes any mask set by PySide.QT.QWidget.setMask() .
		"""
		res = super(Standard_QWidget,self).clearMask()
		return res
	#----------------------------------------------------------------------
	def contentsMargins(self):
		"""
		The contentsMargins function returns the widgets contents margins.
		"""
		res = super(Standard_QWidget,self).contentsMargins()
		isinstance(res,QT.QMargins)
		return res
	#----------------------------------------------------------------------
	def contentsRect(self):
		"""
		Returns the area inside the widgets margins.
		"""
		res = super(Standard_QWidget,self).contentsRect()
		isinstance(res,QT.QRect)
		return res
	#----------------------------------------------------------------------
	def contextMenuPolicy(self):
		"""
		This property holds how the widget shows a context menu.
		The default value of this property is Qt.DefaultContextMenu , which means the PySide.QT.QWidget.contextMenuEvent() handler is called
		Other values are Qt.NoContextMenu , Qt.PreventContextMenu , Qt.ActionsContextMenu , and Qt.CustomContextMenu
		With Qt.CustomContextMenu , the signal PySide.QT.QWidget.customContextMenuRequested() is emitted.
		"""
		res = super(Standard_QWidget,self).contextMenuPolicy()
		isinstance(res,QT.Qt.ContextMenuPolicy)
		return res
	#----------------------------------------------------------------------
	def createWinId(self):
		"""
		Ensures that the widget has a window system identifier, i.e
		that it is known to the windowing system.
		"""
		res = super(Standard_QWidget,self).createWinId()
		return res
	#----------------------------------------------------------------------
	def cursor(self):
		"""
		This property holds the cursor shape for this widget.
		The mouse cursor will assume this shape when its over this widget
		See the list of predefined cursor objects for a range of useful shapes.
		An editor widget might use an I-beam cursor:
		If no cursor has been set, or after a call to PySide.QT.QWidget.unsetCursor() , the parents cursor is used.
		By default, this property contains a cursor with the Qt.ArrowCursor shape.
		Some underlying window implementations will reset the cursor if it leaves a widget even if the mouse is grabbed
		If you want to have a cursor set for all widgets, even when outside the window, consider QApplication.setOverrideCursor() .
		"""
		res = super(Standard_QWidget,self).cursor()
		isinstance(res,QT.QCursor)
		return res
	#----------------------------------------------------------------------
	def effectiveWinId(self):
		"""
		Returns the effective window system identifier of the widget, i.e
		the native parents window system identifier.
		If the widget is native, this function returns the native widget ID
		Otherwise, the window ID of the first native parent widget, i.e., the top-level widget that contains this widget, is returned.
		"""
		res = super(Standard_QWidget,self).effectiveWinId()
		return res
	#----------------------------------------------------------------------
	def ensurePolished(self):
		"""
		Ensures that the widget has been polished by PySide.QT.QStyle (i.e., has a proper font and palette).
		PySide.QT.QWidget calls this function after it has been fully constructed but before it is shown the very first time
		You can call this function if you want to ensure that the widget is polished before doing an operation, e.g., the correct font size might be needed in the widgets PySide.QT.QWidget.sizeHint() reimplementation
		Note that this function is called from the default implementation of PySide.QT.QWidget.sizeHint() .
		Polishing is useful for final initialization that must happen after all constructors (from base classes as well as from subclasses) have been called.
		If you need to change some settings when a widget is polished, reimplement PySide.QT.QWidget.event() and handle the QEvent.Polish event type.
		"""
		res = super(Standard_QWidget,self).ensurePolished()
		return res
	#----------------------------------------------------------------------
	def focusNextChild(self):
		"""
		Finds a new widget to give the keyboard focus to, as appropriate for Tab , and returns true if it can find a new widget, or false if it cant.
		"""
		res = super(Standard_QWidget,self).focusNextChild()

		return res
	#----------------------------------------------------------------------
	def focusPolicy(self):
		"""
		This property holds the way the widget accepts keyboard focus.
		The policy is Qt.TabFocus if the widget accepts keyboard focus by tabbing, Qt.ClickFocus if the widget accepts focus by clicking, Qt.StrongFocus if it accepts both, and Qt.NoFocus (the default) if it does not accept focus at all.
		You must enable keyboard focus for a widget if it processes keyboard events
		This is normally done from the widgets constructor
		For instance, the PySide.QT.QLineEdit constructor calls setFocusPolicy( Qt.StrongFocus ).
		If the widget has a focus proxy, then the focus policy will be propagated to it.
		"""
		res = super(Standard_QWidget,self).focusPolicy()
		isinstance(res,QT.Qt.FocusPolicy)
		return res
	#----------------------------------------------------------------------
	def focusPreviousChild(self):
		"""
		Finds a new widget to give the keyboard focus to, as appropriate for Shift+Tab , and returns true if it can find a new widget, or false if it cant.
		"""
		res = super(Standard_QWidget,self).focusPreviousChild()

		return res
	#----------------------------------------------------------------------
	def focusProxy(self):
		"""
		Returns the focus proxy, or 0 if there is no focus proxy.
		"""
		res = super(Standard_QWidget,self).focusProxy()
		isinstance(res,QT.QWidget)
		return res
	#----------------------------------------------------------------------
	def focusWidget(self):
		"""
		Returns the last child of this widget that setFocus had been called on
		For top level widgets this is the widget that will get focus in case this window gets activated
		This is not the same as QApplication.focusWidget() , which returns the focus widget in the currently active window.
		"""
		res = super(Standard_QWidget,self).focusWidget()
		isinstance(res,QT.QWidget)
		return res
	#----------------------------------------------------------------------
	def font(self):
		"""
		This property holds the font currently set for the widget.
		This property describes the widgets requested font
		The font is used by the widgets style when rendering standard components, and is available as a means to ensure that custom widgets can maintain consistency with the native platforms look and feel
		Its common that different platforms, or different styles, define different fonts for an application.
		When you assign a new font to a widget, the properties from this font are combined with the widgets default font to form the widgets final font
		You can call PySide.QT.QWidget.fontInfo() to get a copy of the widgets final font
		The final font is also used to initialize PySide.QT.QPainter s font.
		The default depends on the system environment
		PySide.QT.QApplication maintains a system/theme font which serves as a default for all widgets
		There may also be special font defaults for certain types of widgets
		You can also define default fonts for widgets yourself by passing a custom font and the name of a widget to QApplication.setFont()
		Finally, the font is matched against Qts font database to find the best match.
		PySide.QT.QWidget propagates explicit font properties from parent to child
		If you change a specific property on a font and assign that font to a widget, that property will propagate to all the widgets children, overriding any system defaults for that property
		Note that fonts by default dont propagate to windows (see PySide.QT.QWidget.isWindow() ) unless the Qt.WA_WindowPropagation attribute is enabled.
		PySide.QT.QWidget s font propagation is similar to its palette propagation.
		The current style, which is used to render the content of all standard Qt widgets, is free to choose to use the widget font, or in some cases, to ignore it (partially, or completely)
		In particular, certain styles like GTK style, Mac style, Windows XP, and Vista style, apply special modifications to the widget font to match the platforms native look and feel
		Because of this, assigning properties to a widgets font is not guaranteed to change the appearance of the widget
		Instead, you may choose to apply a PySide.QT.QWidget.styleSheet() .
		"""
		res = super(Standard_QWidget,self).font()
		isinstance(res,QT.QFont)
		return res
	#----------------------------------------------------------------------
	def fontInfo(self):
		"""
		Returns the font info for the widgets current font
		Equivalent to QFontInto(widget-> PySide.QT.QWidget.font() ).
		"""
		res = super(Standard_QWidget,self).fontInfo()
		isinstance(res,QT.QFontInfo)
		return res
	#----------------------------------------------------------------------
	def fontMetrics(self):
		"""
		Returns the font metrics for the widgets current font
		Equivalent to PySide.QT.QFontMetrics (widget-> PySide.QT.QWidget.font() ).
		"""
		res = super(Standard_QWidget,self).fontMetrics()
		isinstance(res,QT.QFontMetrics)
		return res
	#----------------------------------------------------------------------
	def foregroundRole(self):
		"""
		Returns the foreground role.
		The foreground role defines the color from the widgets PySide.QT.QWidget.palette() that is used to draw the foreground.
		If no explicit foreground role is set, the function returns a role that contrasts with the background role.
		"""
		res = super(Standard_QWidget,self).foregroundRole()
		isinstance(res,QT.QPalette.ColorRole)
		return res
	#----------------------------------------------------------------------
	def frameGeometry(self):
		"""
		This property holds geometry of the widget relative to its parent including any window frame.
		See the Window Geometry documentation for an overview of geometry issues with windows.
		By default, this property contains a value that depends on the users platform and screen geometry.
		"""
		res = super(Standard_QWidget,self).frameGeometry()
		isinstance(res,QT.QRect)
		return res
	#----------------------------------------------------------------------
	def frameSize(self):
		"""
		This property holds the size of the widget including any window frame.
		By default, this property contains a value that depends on the users platform and screen geometry.
		"""
		res = super(Standard_QWidget,self).frameSize()
		isinstance(res,QT.QSize)
		return res
	#----------------------------------------------------------------------
	def geometry(self):
		"""
		This property holds the geometry of the widget relative to its parent and excluding the window frame.
		When changing the geometry, the widget, if visible, receives a move event ( PySide.QT.QWidget.moveEvent() ) and/or a resize event ( PySide.QT.QWidget.resizeEvent() ) immediately
		If the widget is not currently visible, it is guaranteed to receive appropriate events before it is shown.
		The size component is adjusted if it lies outside the range defined by PySide.QT.QWidget.minimumSize() and PySide.QT.QWidget.maximumSize() .
		See the Window Geometry documentation for an overview of geometry issues with windows.
		By default, this property contains a value that depends on the users platform and screen geometry.
		"""
		res = super(Standard_QWidget,self).geometry()
		isinstance(res,QT.QRect)
		return res
	#----------------------------------------------------------------------
	def getContentsMargins(self):
		"""
		Returns the widgets contents margins for left , top , right , and bottom .
		"""
		res = super(Standard_QWidget,self).getContentsMargins()
		return res
	#----------------------------------------------------------------------
	def grabKeyboard(self):
		"""
		Grabs the keyboard input.
		This widget receives all keyboard events until PySide.QT.QWidget.releaseKeyboard() is called; other widgets get no keyboard events at all
		Mouse events are not affected
		Use PySide.QT.QWidget.grabMouse() if you want to grab that.
		The focus widget is not affected, except that it doesnt receive any keyboard events
		PySide.QT.QWidget.setFocus() moves the focus as usual, but the new focus widget receives keyboard events only after PySide.QT.QWidget.releaseKeyboard() is called.
		If a different widget is currently grabbing keyboard input, that widgets grab is released first.
		"""
		res = super(Standard_QWidget,self).grabKeyboard()
		return res
	#----------------------------------------------------------------------
	def grabMouse(self):
		"""
		Grabs the mouse input.
		This widget receives all mouse events until PySide.QT.QWidget.releaseMouse() is called; other widgets get no mouse events at all
		Keyboard events are not affected
		Use PySide.QT.QWidget.grabKeyboard() if you want to grab that.
		It is almost never necessary to grab the mouse when using Qt, as Qt grabs and releases it sensibly
		In particular, Qt grabs the mouse when a mouse button is pressed and keeps it until the last button is released.
		"""
		res = super(Standard_QWidget,self).grabMouse()
		return res
	#----------------------------------------------------------------------
	def graphicsEffect(self):
		"""
		The graphicsEffect function returns a pointer to the widgets graphics effect.
		If the widget has no graphics effect, 0 is returned.
		"""
		res = super(Standard_QWidget,self).graphicsEffect()
		isinstance(res,QT.QGraphicsEffect)
		return res
	#----------------------------------------------------------------------
	def graphicsProxyWidget(self):
		"""
		Returns the proxy widget for the corresponding embedded widget in a graphics view; otherwise returns 0.
		"""
		res = super(Standard_QWidget,self).graphicsProxyWidget()
		isinstance(res,QT.QGraphicsProxyWidget)
		return res
	#----------------------------------------------------------------------
	def hasFocus(self):
		"""
		This property holds whether this widget (or its focus proxy) has the keyboard input focus.
		By default, this property is false.
		"""
		res = super(Standard_QWidget,self).hasFocus()

		return res
	#----------------------------------------------------------------------
	def hasMouseTracking(self):
		"""
		This property holds whether mouse tracking is enabled for the widget.
		If mouse tracking is disabled (the default), the widget only receives mouse move events when at least one mouse button is pressed while the mouse is being moved.
		If mouse tracking is enabled, the widget receives mouse move events even if no buttons are pressed.
		"""
		res = super(Standard_QWidget,self).hasMouseTracking()

		return res
	#----------------------------------------------------------------------
	def inputContext(self):
		"""
		This function returns the PySide.QT.QInputContext for this widget
		By default the input context is inherited from the widgets parent
		For toplevels it is inherited from PySide.QT.QApplication .
		You can override this and set a special input context for this widget by using the PySide.QT.QWidget.setInputContext() method.
		"""
		res = super(Standard_QWidget,self).inputContext()
		isinstance(res,QT.QInputContext)
		return res
	#----------------------------------------------------------------------
	def inputMethodHints(self):
		"""
		This property holds What input method specific hints the widget has..
		This is only relevant for input widgets
		It is used by the input method to retrieve hints as to how the input method should operate
		For example, if the Qt.ImhFormattedNumbersOnly flag is set, the input method may change its visual components to reflect that only numbers can be entered.
		The default value is Qt.ImhNone .
		"""
		res = super(Standard_QWidget,self).inputMethodHints()
		isinstance(res,QT.Qt.InputMethodHints)
		return res
	#----------------------------------------------------------------------
	def isActiveWindow(self):
		"""
		This property holds whether this widgets window is the active window.
		The active window is the window that contains the widget that has keyboard focus (The window may still have focus if it has no widgets or none of its widgets accepts keyboard focus).
		When popup windows are visible, this property is true for both the active window and for the popup.
		By default, this property is false.
		"""
		res = super(Standard_QWidget,self).isActiveWindow()

		return res
	#----------------------------------------------------------------------
	def isEnabled(self):
		"""
		This property holds whether the widget is enabled.
		An enabled widget handles keyboard and mouse events; a disabled widget does not.
		Some widgets display themselves differently when they are disabled
		For example a button might draw its label grayed out
		If your widget needs to know when it becomes enabled or disabled, you can use the PySide.QT.QWidget.changeEvent() with type QEvent.EnabledChange .
		Disabling a widget implicitly disables all its children
		Enabling respectively enables all child widgets unless they have been explicitly disabled.
		By default, this property is true.
		"""
		res = super(Standard_QWidget,self).isEnabled()

		return res
	#----------------------------------------------------------------------
	def isFullScreen(self):
		"""
		This property holds whether the widget is shown in full screen mode.
		A widget in full screen mode occupies the whole screen area and does not display window decorations, such as a title bar.
		By default, this property is false.
		"""
		res = super(Standard_QWidget,self).isFullScreen()

		return res
	#----------------------------------------------------------------------
	def isHidden(self):
		"""
		Returns true if the widget is hidden, otherwise returns false.
		A hidden widget will only become visible when PySide.QT.QWidget.show() is called on it
		It will not be automatically shown when the parent is shown.
		To check visibility, use ! PySide.QT.QWidget.isVisible() instead (notice the exclamation mark).
		PySide.QT.QWidget.isHidden() implies ! PySide.QT.QWidget.isVisible() , but a widget can be not visible and not hidden at the same time
		This is the case for widgets that are children of widgets that are not visible.
		Widgets are hidden if:
		"""
		res = super(Standard_QWidget,self).isHidden()

		return res
	#----------------------------------------------------------------------
	def isLeftToRight(self):
		"""

		"""
		res = super(Standard_QWidget,self).isLeftToRight()

		return res
	#----------------------------------------------------------------------
	def isMaximized(self):
		"""
		This property holds whether this widget is maximized.
		This property is only relevant for windows.
		By default, this property is false.
		"""
		res = super(Standard_QWidget,self).isMaximized()

		return res
	#----------------------------------------------------------------------
	def isMinimized(self):
		"""
		This property holds whether this widget is minimized (iconified).
		This property is only relevant for windows.
		By default, this property is false.
		"""
		res = super(Standard_QWidget,self).isMinimized()

		return res
	#----------------------------------------------------------------------
	def isModal(self):
		"""
		This property holds whether the widget is a modal widget.
		This property only makes sense for windows
		A modal widget prevents widgets in all other windows from getting any input.
		By default, this property is false.
		"""
		res = super(Standard_QWidget,self).isModal()

		return res
	#----------------------------------------------------------------------
	def isRightToLeft(self):
		"""

		"""
		res = super(Standard_QWidget,self).isRightToLeft()

		return res
	#----------------------------------------------------------------------
	def isVisible(self):
		"""
		This property holds whether the widget is visible.
		Calling setVisible(true) or PySide.QT.QWidget.show() sets the widget to visible status if all its parent widgets up to the window are visible
		If an ancestor is not visible, the widget wont become visible until all its ancestors are shown
		If its size or position has changed, Qt guarantees that a widget gets move and resize events just before it is shown
		If the widget has not been resized yet, Qt will adjust the widgets size to a useful default using PySide.QT.QWidget.adjustSize() .
		Calling setVisible(false) or PySide.QT.QWidget.hide() hides a widget explicitly
		An explicitly hidden widget will never become visible, even if all its ancestors become visible, unless you show it.
		A widget receives show and hide events when its visibility status changes
		Between a hide and a show event, there is no need to waste CPU cycles preparing or displaying information to the user
		A video application, for example, might simply stop generating new frames.
		A widget that happens to be obscured by other windows on the screen is considered to be visible
		The same applies to iconified windows and windows that exist on another virtual desktop (on platforms that support this concept)
		A widget receives spontaneous show and hide events when its mapping status is changed by the window system, e.g
		a spontaneous hide event when the user minimizes the window, and a spontaneous show event when the window is restored again.
		You almost never have to reimplement the PySide.QT.QWidget.setVisible() function
		If you need to change some settings before a widget is shown, use PySide.QT.QWidget.showEvent() instead
		If you need to do some delayed initialization use the Polish event delivered to the PySide.QT.QWidget.event() function.
		"""
		res = super(Standard_QWidget,self).isVisible()

		return res
	#----------------------------------------------------------------------
	def isWindow(self):
		"""
		Returns true if the widget is an independent window, otherwise returns false.
		A window is a widget that isnt visually the child of any other widget and that usually has a frame and a window title .
		A window can have a parent widget
		It will then be grouped with its parent and deleted when the parent is deleted, minimized when the parent is minimized etc
		If supported by the window manager, it will also have a common taskbar entry with its parent.
		PySide.QT.QDialog and PySide.QT.QMainWindow widgets are by default windows, even if a parent widget is specified in the constructor
		This behavior is specified by the Qt.Window flag.
		"""
		res = super(Standard_QWidget,self).isWindow()

		return res
	#----------------------------------------------------------------------
	def isWindowModified(self):
		"""
		This property holds whether the document shown in the window has unsaved changes.
		A modified window is a window whose content has changed but has not been saved to disk
		This flag will have different effects varied by the platform
		On Mac OS X the close button will have a modified look; on other platforms, the window title will have an * (asterisk).
		The window title must contain a [*] placeholder, which indicates where the * should appear
		Normally, it should appear right after the file name (e.g., document1.txt[*] - Text Editor)
		If the window isnt modified, the placeholder is simply removed.
		Note that if a widget is set as modified, all its ancestors will also be set as modified
		However, if you call setWindowModified(false) on a widget, this will not propagate to its parent because other children of the parent might have been modified.
		"""
		res = super(Standard_QWidget,self).isWindowModified()

		return res
	#----------------------------------------------------------------------
	def languageChange(self):
		"""

		"""
		res = super(Standard_QWidget,self).languageChange()
		return res
	#----------------------------------------------------------------------
	def layout(self):
		"""
		Returns the layout manager that is installed on this widget, or 0 if no layout manager is installed.
		The layout manager sets the geometry of the widgets children that have been added to the layout.
		"""
		res = super(Standard_QWidget,self).layout()
		isinstance(res,QT.QLayout)
		return res
	#----------------------------------------------------------------------
	def layoutDirection(self):
		"""
		This property holds the layout direction for this widget.
		By default, this property is set to Qt.LeftToRight .
		When the layout direction is set on a widget, it will propagate to the widgets children, but not to a child that is a window and not to a child for which PySide.QT.QWidget.setLayoutDirection() has been explicitly called
		Also, child widgets added afterPySide.QT.QWidget.setLayoutDirection() has been called for the parent do not inherit the parents layout direction.
		This method no longer affects text layout direction since Qt 4.7.
		"""
		res = super(Standard_QWidget,self).layoutDirection()
		isinstance(res,QT.Qt.LayoutDirection)
		return res
	#----------------------------------------------------------------------
	def locale(self):
		"""
		This property holds the widgets locale.
		As long as no special locale has been set, this is either the parents locale or (if this widget is a top level widget), the default locale.
		If the widget displays dates or numbers, these should be formatted using the widgets locale.
		"""
		res = super(Standard_QWidget,self).locale()
		isinstance(res,QT.QLocale)
		return res
	#----------------------------------------------------------------------
	def mask(self):
		"""
		Returns the mask currently set on a widget
		If no mask is set the return value will be an empty region.
		"""
		res = super(Standard_QWidget,self).mask()
		isinstance(res,QT.QRegion)
		return res
	#----------------------------------------------------------------------
	def maximumHeight(self):
		"""
		This property holds the widgets maximum height in pixels.
		This property corresponds to the height held by the PySide.QT.QWidget.maximumSize() property.
		By default, this property contains a value of 16777215.
		"""
		res = super(Standard_QWidget,self).maximumHeight()

		return res
	#----------------------------------------------------------------------
	def maximumSize(self):
		"""
		This property holds the widgets maximum size in pixels.
		The widget cannot be resized to a larger size than the maximum widget size.
		By default, this property contains a size in which both width and height have values of 16777215.
		"""
		res = super(Standard_QWidget,self).maximumSize()
		isinstance(res,QT.QSize)
		return res
	#----------------------------------------------------------------------
	def maximumWidth(self):
		"""
		This property holds the widgets maximum width in pixels.
		This property corresponds to the width held by the PySide.QT.QWidget.maximumSize() property.
		By default, this property contains a value of 16777215.
		"""
		res = super(Standard_QWidget,self).maximumWidth()

		return res
	#----------------------------------------------------------------------
	def minimumHeight(self):
		"""
		This property holds the widgets minimum height in pixels.
		This property corresponds to the height held by the PySide.QT.QWidget.minimumSize() property.
		By default, this property has a value of 0.
		"""
		res = super(Standard_QWidget,self).minimumHeight()

		return res
	#----------------------------------------------------------------------
	def minimumSize(self):
		"""
		This property holds the widgets minimum size.
		The widget cannot be resized to a smaller size than the minimum widget size
		The widgets size is forced to the minimum size if the current size is smaller.
		The minimum size set by this function will override the minimum size defined by PySide.QT.QLayout
		In order to unset the minimum size, use a value of QSize(0, 0) .
		By default, this property contains a size with zero width and height.
		"""
		res = super(Standard_QWidget,self).minimumSize()
		isinstance(res,QT.QSize)
		return res
	#----------------------------------------------------------------------
	def minimumSizeHint(self):
		"""
		This property holds the recommended minimum size for the widget.
		If the value of this property is an invalid size, no minimum size is recommended.
		The default implementation of PySide.QT.QWidget.minimumSizeHint() returns an invalid size if there is no layout for this widget, and returns the layouts minimum size otherwise
		Most built-in widgets reimplement PySide.QT.QWidget.minimumSizeHint() .
		PySide.QT.QLayout will never resize a widget to a size smaller than the minimum size hint unless PySide.QT.QWidget.minimumSize() is set or the size policy is set to QSizePolicy::Ignore
		If PySide.QT.QWidget.minimumSize() is set, the minimum size hint will be ignored.
		"""
		res = super(Standard_QWidget,self).minimumSizeHint()
		isinstance(res,QT.QSize)
		return res
	#----------------------------------------------------------------------
	def minimumWidth(self):
		"""
		This property holds the widgets minimum width in pixels.
		This property corresponds to the width held by the PySide.QT.QWidget.minimumSize() property.
		By default, this property has a value of 0.
		"""
		res = super(Standard_QWidget,self).minimumWidth()

		return res
	#----------------------------------------------------------------------
	def nativeParentWidget(self):
		"""
		Returns the native parent for this widget, i.e
		the next ancestor widget that has a system identifier, or 0 if it does not have any native parent.
		"""
		res = super(Standard_QWidget,self).nativeParentWidget()
		isinstance(res,QT.QWidget)
		return res
	#----------------------------------------------------------------------
	def nextInFocusChain(self):
		"""
		Returns the next widget in this widgets focus chain.
		"""
		res = super(Standard_QWidget,self).nextInFocusChain()
		isinstance(res,QT.QWidget)
		return res
	#----------------------------------------------------------------------
	def normalGeometry(self):
		"""
		This property holds the geometry of the widget as it will appear when shown as a normal (not maximized or full screen) top-level widget.
		For child widgets this property always holds an empty rectangle.
		By default, this property contains an empty rectangle.
		"""
		res = super(Standard_QWidget,self).normalGeometry()
		isinstance(res,QT.QRect)
		return res
	#----------------------------------------------------------------------
	def palette(self):
		"""
		This property holds the widgets palette.
		This property describes the widgets palette
		The palette is used by the widgets style when rendering standard components, and is available as a means to ensure that custom widgets can maintain consistency with the native platforms look and feel
		Its common that different platforms, or different styles, have different palettes.
		When you assign a new palette to a widget, the color roles from this palette are combined with the widgets default palette to form the widgets final palette
		The palette entry for the widgets background role is used to fill the widgets background (see QWidget.autoFillBackground ), and the foreground role initializes PySide.QT.QPainter s pen.
		The default depends on the system environment
		PySide.QT.QApplication maintains a system/theme palette which serves as a default for all widgets
		There may also be special palette defaults for certain types of widgets (e.g., on Windows XP and Vista, all classes that derive from PySide.QT.QMenuBar have a special default palette)
		You can also define default palettes for widgets yourself by passing a custom palette and the name of a widget to QApplication.setPalette()
		Finally, the style always has the option of polishing the palette as its assigned (see QStyle.polish() ).
		PySide.QT.QWidget propagates explicit palette roles from parent to child
		If you assign a brush or color to a specific role on a palette and assign that palette to a widget, that role will propagate to all the widgets children, overriding any system defaults for that role
		Note that palettes by default dont propagate to windows (see PySide.QT.QWidget.isWindow() ) unless the Qt.WA_WindowPropagation attribute is enabled.
		PySide.QT.QWidget s palette propagation is similar to its font propagation.
		The current style, which is used to render the content of all standard Qt widgets, is free to choose colors and brushes from the widget palette, or in some cases, to ignore the palette (partially, or completely)
		In particular, certain styles like GTK style, Mac style, Windows XP, and Vista style, depend on third party APIs to render the content of widgets, and these styles typically do not follow the palette
		Because of this, assigning roles to a widgets palette is not guaranteed to change the appearance of the widget
		Instead, you may choose to apply a PySide.QT.QWidget.styleSheet()
		You can refer to our Knowledge Base article here for more information.
		"""
		res = super(Standard_QWidget,self).palette()
		isinstance(res,QT.QPalette)
		return res
	#----------------------------------------------------------------------
	def parentWidget(self):
		"""
		Returns the parent of this widget, or 0 if it does not have any parent widget.
		"""
		res = super(Standard_QWidget,self).parentWidget()
		isinstance(res,QT.QWidget)
		return res
	#----------------------------------------------------------------------
	def pos(self):
		"""
		This property holds the position of the widget within its parent widget.
		If the widget is a window, the position is that of the widget on the desktop, including its frame.
		When changing the position, the widget, if visible, receives a move event ( PySide.QT.QWidget.moveEvent() ) immediately
		If the widget is not currently visible, it is guaranteed to receive an event before it is shown.
		By default, this property contains a position that refers to the origin.
		See the Window Geometry documentation for an overview of geometry issues with windows.
		"""
		res = super(Standard_QWidget,self).pos()
		isinstance(res,QT.QPoint)
		return res
	#----------------------------------------------------------------------
	def previousInFocusChain(self):
		"""
		The previousInFocusChain function returns the previous widget in this widgets focus chain.
		"""
		res = super(Standard_QWidget,self).previousInFocusChain()
		isinstance(res,QT.QWidget)
		return res
	#----------------------------------------------------------------------
	def rect(self):
		"""
		This property holds the internal geometry of the widget excluding any window frame.
		The rect property equals PySide.QT.QRect (0, 0, PySide.QT.QWidget.width() , PySide.QT.QWidget.height() ).
		See the Window Geometry documentation for an overview of geometry issues with windows.
		By default, this property contains a value that depends on the users platform and screen geometry.
		"""
		res = super(Standard_QWidget,self).rect()
		isinstance(res,QT.QRect)
		return res
	#----------------------------------------------------------------------
	def releaseKeyboard(self):
		"""
		Releases the keyboard grab.
		"""
		res = super(Standard_QWidget,self).releaseKeyboard()
		return res
	#----------------------------------------------------------------------
	def releaseMouse(self):
		"""
		Releases the mouse grab.
		"""
		res = super(Standard_QWidget,self).releaseMouse()
		return res
	#----------------------------------------------------------------------
	def resetInputContext(self):
		"""
		This function can be called on the widget that currently has focus to reset the input method operating on it.
		This function is providing for convenience, instead you should use PySide.QT.QInputContext.reset() on the input context that was returned by PySide.QT.QWidget.inputContext() .
		"""
		res = super(Standard_QWidget,self).resetInputContext()
		return res
	#----------------------------------------------------------------------
	def saveGeometry(self):
		"""
		Saves the current geometry and state for top-level widgets.
		To save the geometry when the window closes, you can implement a close event like this:
		See the Window Geometry documentation for an overview of geometry issues with windows.
		Use QMainWindow.saveState() to save the geometry and the state of toolbars and dock widgets.
		"""
		res = super(Standard_QWidget,self).saveGeometry()
		isinstance(res,QT.QByteArray)
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		This property holds the size of the widget excluding any window frame.
		If the widget is visible when it is being resized, it receives a resize event ( PySide.QT.QWidget.resizeEvent() ) immediately
		If the widget is not currently visible, it is guaranteed to receive an event before it is shown.
		The size is adjusted if it lies outside the range defined by PySide.QT.QWidget.minimumSize() and PySide.QT.QWidget.maximumSize() .
		By default, this property contains a value that depends on the users platform and screen geometry.
		"""
		res = super(Standard_QWidget,self).size()
		isinstance(res,QT.QSize)
		return res
	#----------------------------------------------------------------------
	def sizeHint(self):
		"""
		This property holds the recommended size for the widget.
		If the value of this property is an invalid size, no size is recommended.
		The default implementation of PySide.QT.QWidget.sizeHint() returns an invalid size if there is no layout for this widget, and returns the layouts preferred size otherwise.
		"""
		res = super(Standard_QWidget,self).sizeHint()
		isinstance(res,QT.QSize)
		return res
	#----------------------------------------------------------------------
	def sizeIncrement(self):
		"""
		This property holds the size increment of the widget.
		When the user resizes the window, the size will move in steps of PySide.QT.QWidget.sizeIncrement()
		PySide.QT.QWidget.width() pixels horizontally and PySide.QT.QWidget.sizeIncrement()
		PySide.QT.QWidget.height() pixels vertically, with PySide.QT.QWidget.baseSize() as the basis
		Preferred widget sizes are for non-negative integers i and j :
		Note that while you can set the size increment for all widgets, it only affects windows.
		By default, this property contains a size with zero width and height.
		"""
		res = super(Standard_QWidget,self).sizeIncrement()
		isinstance(res,QT.QSize)
		return res
	#----------------------------------------------------------------------
	def sizePolicy(self):
		"""
		This property holds the default layout behavior of the widget.
		If there is a PySide.QT.QLayout that manages this widgets children, the size policy specified by that layout is used
		If there is no such PySide.QT.QLayout , the result of this function is used.
		The default policy is Preferred/Preferred, which means that the widget can be freely resized, but prefers to be the size PySide.QT.QWidget.sizeHint() returns
		Button-like widgets set the size policy to specify that they may stretch horizontally, but are fixed vertically
		The same applies to lineedit controls (such as PySide.QT.QLineEdit , PySide.QT.QSpinBox or an editable PySide.QT.QComboBox ) and other horizontally orientated widgets (such as PySide.QT.QProgressBar )
		PySide.QT.QToolButton s are normally square, so they allow growth in both directions
		Widgets that support different directions (such as PySide.QT.QSlider , PySide.QT.QScrollBar or QHeader ) specify stretching in the respective direction only
		Widgets that can provide scroll bars (usually subclasses of PySide.QT.QScrollArea ) tend to specify that they can use additional space, and that they can make do with less than PySide.QT.QWidget.sizeHint() .
		"""
		res = super(Standard_QWidget,self).sizePolicy()
		isinstance(res,QT.QSizePolicy)
		return res
	#----------------------------------------------------------------------
	def statusTip(self):
		"""
		This property holds the widgets status tip.
		By default, this property contains an empty string.
		"""
		res = super(Standard_QWidget,self).statusTip()
		return res
	#----------------------------------------------------------------------
	def style(self):
		"""

		"""
		res = super(Standard_QWidget,self).style()
		isinstance(res,QT.QStyle)
		return res
	#----------------------------------------------------------------------
	def styleSheet(self):
		"""
		This property holds the widgets style sheet.
		The style sheet contains a textual description of customizations to the widgets style, as described in the Qt Style Sheets document.
		Since Qt 4.5, Qt style sheets fully supports Mac OS X.
		"""
		res = super(Standard_QWidget,self).styleSheet()
		return res
	#----------------------------------------------------------------------
	def takeLayout(self):
		"""

		"""
		res = super(Standard_QWidget,self).takeLayout()
		isinstance(res,QT.QLayout)
		return res
	#----------------------------------------------------------------------
	def toolTip(self):
		"""
		This property holds the widgets tooltip.
		Note that by default tooltips are only shown for widgets that are children of the active window
		You can change this behavior by setting the attribute Qt.WA_AlwaysShowToolTips on the window , not on the widget with the tooltip.
		If you want to control a tooltips behavior, you can intercept the PySide.QT.QWidget.event() function and catch the QEvent.ToolTip event (e.g., if you want to customize the area for which the tooltip should be shown).
		By default, this property contains an empty string.
		"""
		res = super(Standard_QWidget,self).toolTip()
		return res
	#----------------------------------------------------------------------
	def underMouse(self):
		"""
		Returns true if the widget is under the mouse cursor; otherwise returns false.
		This value is not updated properly during drag and drop operations.
		"""
		res = super(Standard_QWidget,self).underMouse()

		return res
	#----------------------------------------------------------------------
	def unsetCursor(self):
		"""
		This property holds the cursor shape for this widget.
		The mouse cursor will assume this shape when its over this widget
		See the list of predefined cursor objects for a range of useful shapes.
		An editor widget might use an I-beam cursor:
		If no cursor has been set, or after a call to PySide.QT.QWidget.unsetCursor() , the parents cursor is used.
		By default, this property contains a cursor with the Qt.ArrowCursor shape.
		Some underlying window implementations will reset the cursor if it leaves a widget even if the mouse is grabbed
		If you want to have a cursor set for all widgets, even when outside the window, consider QApplication.setOverrideCursor() .
		"""
		res = super(Standard_QWidget,self).unsetCursor()
		return res
	#----------------------------------------------------------------------
	def unsetLayoutDirection(self):
		"""
		This property holds the layout direction for this widget.
		By default, this property is set to Qt.LeftToRight .
		When the layout direction is set on a widget, it will propagate to the widgets children, but not to a child that is a window and not to a child for which PySide.QT.QWidget.setLayoutDirection() has been explicitly called
		Also, child widgets added afterPySide.QT.QWidget.setLayoutDirection() has been called for the parent do not inherit the parents layout direction.
		This method no longer affects text layout direction since Qt 4.7.
		"""
		res = super(Standard_QWidget,self).unsetLayoutDirection()
		return res
	#----------------------------------------------------------------------
	def unsetLocale(self):
		"""
		This property holds the widgets locale.
		As long as no special locale has been set, this is either the parents locale or (if this widget is a top level widget), the default locale.
		If the widget displays dates or numbers, these should be formatted using the widgets locale.
		"""
		res = super(Standard_QWidget,self).unsetLocale()
		return res
	#----------------------------------------------------------------------
	def updateGeometry(self):
		"""
		Notifies the layout system that this widget has changed and may need to change geometry.
		Call this function if the PySide.QT.QWidget.sizeHint() or PySide.QT.QWidget.sizePolicy() have changed.
		For explicitly hidden widgets, PySide.QT.QWidget.updateGeometry() is a no-op
		The layout system will be notified as soon as the widget is shown.
		"""
		res = super(Standard_QWidget,self).updateGeometry()
		return res
	#----------------------------------------------------------------------
	def updatesEnabled(self):
		"""
		This property holds whether updates are enabled.
		An updates enabled widget receives paint events and has a system background; a disabled widget does not
		This also implies that calling PySide.QT.QWidget.update() and PySide.QT.QWidget.repaint() has no effect if updates are disabled.
		By default, this property is true.
		PySide.QT.QWidget.setUpdatesEnabled() is normally used to disable updates for a short period of time, for instance to avoid screen flicker during large changes
		In Qt, widgets normally do not generate screen flicker, but on X11 the server might erase regions on the screen when widgets get hidden before they can be replaced by other widgets
		Disabling updates solves this.
		Example:
		Disabling a widget implicitly disables all its children
		Enabling a widget enables all child widgets except top-level widgets or those that have been explicitly disabled
		Re-enabling updates implicitly calls PySide.QT.QWidget.update() on the widget.
		"""
		res = super(Standard_QWidget,self).updatesEnabled()

		return res
	#----------------------------------------------------------------------
	def visibleRegion(self):
		"""
		Returns the unobscured region where paint events can occur.
		For visible widgets, this is an approximation of the area not covered by other widgets; otherwise, this is an empty region.
		The PySide.QT.QWidget.repaint() function calls this function if necessary, so in general you do not need to call it.
		"""
		res = super(Standard_QWidget,self).visibleRegion()
		isinstance(res,QT.QRegion)
		return res
	#----------------------------------------------------------------------
	def whatsThis(self):
		"""
		This property holds the widgets Whats This help text..
		By default, this property contains an empty string.
		"""
		res = super(Standard_QWidget,self).whatsThis()
		return res
	#----------------------------------------------------------------------
	def winId(self):
		"""
		Returns the window system identifier of the widget.
		Portable in principle, but if you use it you are probably about to do something non-portable
		Be careful.
		If a widget is non-native (alien) and winId() is invoked on it, that widget will be provided a native handle.
		On X11 the type returned is long, on other platforms its a PyCObject.
		This value may change at run-time
		An event with type PySide.QT.QEvent.WinIdChange will be sent to the widget following a change in window system identifier.
		"""
		res = super(Standard_QWidget,self).winId()
		return res
	#----------------------------------------------------------------------
	def window(self):
		"""
		Returns the window for this widget, i.e
		the next ancestor widget that has (or could have) a window-system frame.
		If the widget is a window, the widget itself is returned.
		Typical usage is changing the window title:
		"""
		res = super(Standard_QWidget,self).window()
		isinstance(res,QT.QWidget)
		return res
	#----------------------------------------------------------------------
	def windowFilePath(self):
		"""
		This property holds the file path associated with a widget.
		This property only makes sense for windows
		It associates a file path with a window
		If you set the file path, but have not set the window title, Qt sets the window title to contain a string created using the following components.
		On Mac OS X:
		On Windows and X11:
		If the window title is set at any point, then the window title takes precedence and will be shown instead of the file path string.
		Additionally, on Mac OS X, this has an added benefit that it sets the proxy icon for the window, assuming that the file path exists.
		If no file path is set, this property contains an empty string.
		By default, this property contains an empty string.
		"""
		res = super(Standard_QWidget,self).windowFilePath()
		return res
	#----------------------------------------------------------------------
	def windowFlags(self):
		"""

		"""
		res = super(Standard_QWidget,self).windowFlags()
		isinstance(res,QT.Qt.WindowFlags)
		return res
	#----------------------------------------------------------------------
	def windowIcon(self):
		"""
		This property holds the widgets icon.
		This property only makes sense for windows
		If no icon has been set, PySide.QT.QWidget.windowIcon() returns the application icon ( QApplication.windowIcon() ).
		"""
		res = super(Standard_QWidget,self).windowIcon()
		isinstance(res,QT.QIcon)
		return res
	#----------------------------------------------------------------------
	def windowIconText(self):
		"""
		This property holds the widgets icon text.
		This property only makes sense for windows
		If no icon text has been set, this functions returns an empty string.
		"""
		res = super(Standard_QWidget,self).windowIconText()
		return res
	#----------------------------------------------------------------------
	def windowModality(self):
		"""
		This property holds which windows are blocked by the modal widget.
		This property only makes sense for windows
		A modal widget prevents widgets in other windows from getting input
		The value of this property controls which windows are blocked when the widget is visible
		Changing this property while the window is visible has no effect; you must PySide.QT.QWidget.hide() the widget first, then PySide.QT.QWidget.show() it again.
		By default, this property is Qt.NonModal .
		"""
		res = super(Standard_QWidget,self).windowModality()
		isinstance(res,QT.Qt.WindowModality)
		return res
	#----------------------------------------------------------------------
	def windowOpacity(self):
		"""

		"""
		res = super(Standard_QWidget,self).windowOpacity()
		isinstance(res,QT.Qt.qreal)
		return res
	#----------------------------------------------------------------------
	def windowRole(self):
		"""
		Returns the windows role, or an empty string.
		"""
		res = super(Standard_QWidget,self).windowRole()
		return res
	#----------------------------------------------------------------------
	def windowState(self):
		"""
		Returns the current window state
		The window state is a ORed combination of Qt.WindowState : Qt.WindowMinimized , Qt.WindowMaximized , Qt.WindowFullScreen , and Qt.WindowActive .
		"""
		res = super(Standard_QWidget,self).windowState()
		isinstance(res,QT.Qt.WindowStates)
		return res
	#----------------------------------------------------------------------
	def windowTitle(self):
		"""
		This property holds the window title (caption).
		This property only makes sense for top-level widgets, such as windows and dialogs
		If no caption has been set, the title is based of the PySide.QT.QWidget.windowFilePath()
		If neither of these is set, then the title is an empty string.
		If you use the windowModified() mechanism, the window title must contain a [*] placeholder, which indicates where the * should appear
		Normally, it should appear right after the file name (e.g., document1.txt[*] - Text Editor)
		If the windowModified() property is false (the default), the placeholder is simply removed.
		"""
		res = super(Standard_QWidget,self).windowTitle()
		return res
	#----------------------------------------------------------------------
	def windowType(self):
		"""
		Returns the window type of this widget
		This is identical to PySide.QT.QWidget.windowFlags() & Qt.WindowType_Mask .
		"""
		res = super(Standard_QWidget,self).windowType()
		isinstance(res,QT.Qt.WindowType)
		return res
	#----------------------------------------------------------------------
	def x(self):
		"""
		This property holds the x coordinate of the widget relative to its parent including any window frame.
		See the Window Geometry documentation for an overview of geometry issues with windows.
		By default, this property has a value of 0.
		"""
		res = super(Standard_QWidget,self).x()

		return res
	#----------------------------------------------------------------------
	def x11Info(self):
		"""
		Returns information about the configuration of the X display used to display the widget.
		"""
		res = super(Standard_QWidget,self).x11Info()
		isinstance(res,QT.Qt.QX11Info)
		return res
	#----------------------------------------------------------------------
	def x11PictureHandle(self):
		"""
		Returns the X11 Picture handle of the widget for XRender support
		Use of this function is not portable
		This function will return 0 if XRender support is not compiled into Qt, if the XRender extension is not supported on the X11 display, or if the handle could not be created.
		"""
		res = super(Standard_QWidget,self).x11PictureHandle()

		return res
	#----------------------------------------------------------------------
	def y(self):
		"""
		This property holds the y coordinate of the widget relative to its parent and including any window frame.
		See the Window Geometry documentation for an overview of geometry issues with windows.
		By default, this property has a value of 0.
		"""
		res = super(Standard_QWidget,self).y()

		return res
	#----------------------------------------------------------------------
	def actionEvent(self,event):
		"""
		actionEvent(event)
			event=QT.QActionEvent

		This event handler is called with the given event whenever the widgets actions are changed.
		"""
		res = super(Standard_QWidget,self).actionEvent(event)
		return res
	#----------------------------------------------------------------------
	def addAction(self,action):
		"""
		addAction(action)
			action=QT.QAction

		Appends the action action to this widgets list of actions.
		All QWidgets have a list of PySide.QT.QAction s, however they can be represented graphically in many different ways
		The default use of the PySide.QT.QAction list (as returned by PySide.QT.QWidget.actions() ) is to create a context PySide.QT.QMenu .
		A PySide.QT.QWidget should only have one of each action and adding an action it already has will not cause the same action to be in the widget twice.
		The ownership of action is not transferred to this PySide.QT.QWidget .
		"""
		res = super(Standard_QWidget,self).addAction(action)
		return res
	#----------------------------------------------------------------------
	def addActions(self,actions):
		"""
		addActions(actions)
			actions=unKnown


		"""
		res = super(Standard_QWidget,self).addActions(actions)
		return res
	#----------------------------------------------------------------------
	def changeEvent(self,event):
		"""
		changeEvent(event)
			event=QT.QEvent

		This event handler can be reimplemented to handle state changes.
		The state being changed in this event can be retrieved through the event supplied.
		Change events include: QEvent.ToolBarChange , QEvent.ActivationChange , QEvent.EnabledChange , QEvent.FontChange , QEvent.StyleChange , QEvent.PaletteChange , QEvent.WindowTitleChange , QEvent.IconTextChange , QEvent.ModifiedChange , QEvent.MouseTrackingChange , QEvent.ParentChange , QEvent.WindowStateChange , QEvent.LanguageChange , QEvent.LocaleChange , QEvent.LayoutDirectionChange .
		"""
		res = super(Standard_QWidget,self).changeEvent(event)
		return res
	#----------------------------------------------------------------------
	def childAt(self,*args,**kwargs):
		"""
		childAt(p)
			p=QT.QPoint

		childAt(x,y)
			x=QT.int
			y=QT.int

		This is an overloaded function.
		Returns the visible child widget at point p in the widgets own coordinate system.
		"""
		res = super(Standard_QWidget,self).childAt(*args,**kwargs)
		isinstance(res,QT.QWidget)
		return res
	#----------------------------------------------------------------------
	def closeEvent(self,event):
		"""
		closeEvent(event)
			event=QT.QCloseEvent

		This event handler is called with the given event when Qt receives a window close request for a top-level widget from the window system.
		By default, the event is accepted and the widget is closed
		You can reimplement this function to change the way the widget responds to window close requests
		For example, you can prevent the window from closing by calling PySide.QT.QEvent.ignore() on all events.
		Main window applications typically use reimplementations of this function to check whether the users work has been saved and ask for permission before closing
		For example, the Application Example uses a helper function to determine whether or not to close the window:
		"""
		res = super(Standard_QWidget,self).closeEvent(event)
		return res
	#----------------------------------------------------------------------
	def contextMenuEvent(self,event):
		"""
		contextMenuEvent(event)
			event=QT.QContextMenuEvent

		This event handler, for event event , can be reimplemented in a subclass to receive widget context menu events.
		The handler is called when the widgets PySide.QT.QWidget.contextMenuPolicy() is Qt.DefaultContextMenu .
		The default implementation ignores the context event
		See the PySide.QT.QContextMenuEvent documentation for more details.
		"""
		res = super(Standard_QWidget,self).contextMenuEvent(event)
		return res
	#----------------------------------------------------------------------
	def destroy(self,destroyWindow=None,destroySubWindows=None):
		"""
		destroy(destroyWindow=None,destroySubWindows=None)
			destroyWindow=QT.bool
			destroySubWindows=QT.bool

		Frees up window system resources
		Destroys the widget window if destroyWindow is true.
		PySide.QT.QWidget.destroy() calls itself recursively for all the child widgets, passing destroySubWindows for the destroyWindow parameter
		To have more control over destruction of subwidgets, destroy subwidgets selectively first.
		This function is usually called from the PySide.QT.QWidget destructor.
		"""
		res = super(Standard_QWidget,self).destroy(destroyWindow,destroySubWindows)
		return res
	#----------------------------------------------------------------------
	def dragEnterEvent(self,event):
		"""
		dragEnterEvent(event)
			event=QT.QDragEnterEvent

		This event handler is called when a drag is in progress and the mouse enters this widget
		The event is passed in the event parameter.
		If the event is ignored, the widget wont receive any drag move events .
		See the Drag-and-drop documentation for an overview of how to provide drag-and-drop in your application.
		"""
		res = super(Standard_QWidget,self).dragEnterEvent(event)
		return res
	#----------------------------------------------------------------------
	def dragLeaveEvent(self,event):
		"""
		dragLeaveEvent(event)
			event=QT.QDragLeaveEvent

		This event handler is called when a drag is in progress and the mouse leaves this widget
		The event is passed in the event parameter.
		See the Drag-and-drop documentation for an overview of how to provide drag-and-drop in your application.
		"""
		res = super(Standard_QWidget,self).dragLeaveEvent(event)
		return res
	#----------------------------------------------------------------------
	def dragMoveEvent(self,event):
		"""
		dragMoveEvent(event)
			event=QT.QDragMoveEvent

		This event handler is called if a drag is in progress, and when any of the following conditions occur: the cursor enters this widget, the cursor moves within this widget, or a modifier key is pressed on the keyboard while this widget has the focus
		The event is passed in the event parameter.
		See the Drag-and-drop documentation for an overview of how to provide drag-and-drop in your application.
		"""
		res = super(Standard_QWidget,self).dragMoveEvent(event)
		return res
	#----------------------------------------------------------------------
	def dropEvent(self,event):
		"""
		dropEvent(event)
			event=QT.QDropEvent

		This event handler is called when the drag is dropped on this widget
		The event is passed in the event parameter.
		See the Drag-and-drop documentation for an overview of how to provide drag-and-drop in your application.
		"""
		res = super(Standard_QWidget,self).dropEvent(event)
		return res
	#----------------------------------------------------------------------
	def enterEvent(self,event):
		"""
		enterEvent(event)
			event=QT.QEvent

		This event handler can be reimplemented in a subclass to receive widget enter events which are passed in the event parameter.
		An event is sent to the widget when the mouse cursor enters the widget.
		"""
		res = super(Standard_QWidget,self).enterEvent(event)
		return res
	#----------------------------------------------------------------------
	def focusInEvent(self,event):
		"""
		focusInEvent(event)
			event=QT.QFocusEvent

		This event handler can be reimplemented in a subclass to receive keyboard focus events (focus received) for the widget
		The event is passed in the event parameter
		A widget normally must PySide.QT.QWidget.setFocusPolicy() to something other than Qt.NoFocus in order to receive focus events
		(Note that the application programmer can call PySide.QT.QWidget.setFocus() on any widget, even those that do not normally accept focus.)
		The default implementation updates the widget (except for windows that do not specify a PySide.QT.QWidget.focusPolicy() ).
		"""
		res = super(Standard_QWidget,self).focusInEvent(event)
		return res
	#----------------------------------------------------------------------
	def focusNextPrevChild(self,next):
		"""
		focusNextPrevChild(next)
			next=QT.bool

		Finds a new widget to give the keyboard focus to, as appropriate for Tab and Shift+Tab, and returns true if it can find a new widget, or false if it cant.
		If next is true, this function searches forward, if next is false, it searches backward.
		Sometimes, you will want to reimplement this function
		For example, a web browser might reimplement it to move its current active link forward or backward, and call PySide.QT.QWidget.focusNextPrevChild() only when it reaches the last or first link on the page.
		Child widgets call PySide.QT.QWidget.focusNextPrevChild() on their parent widgets, but only the window that contains the child widgets decides where to redirect focus
		By reimplementing this function for an object, you thus gain control of focus traversal for all child widgets.
		"""
		res = super(Standard_QWidget,self).focusNextPrevChild(next)

		return res
	#----------------------------------------------------------------------
	def focusOutEvent(self,event):
		"""
		focusOutEvent(event)
			event=QT.QFocusEvent

		This event handler can be reimplemented in a subclass to receive keyboard focus events (focus lost) for the widget
		The events is passed in the event parameter.
		A widget normally must PySide.QT.QWidget.setFocusPolicy() to something other than Qt.NoFocus in order to receive focus events
		(Note that the application programmer can call PySide.QT.QWidget.setFocus() on any widget, even those that do not normally accept focus.)
		The default implementation updates the widget (except for windows that do not specify a PySide.QT.QWidget.focusPolicy() ).
		"""
		res = super(Standard_QWidget,self).focusOutEvent(event)
		return res
	#----------------------------------------------------------------------
	def grabGesture(self,type,flags=None):
		"""
		grabGesture(type,flags=None)
			type=QT.Qt.GestureType
			flags=QT.Qt.GestureFlags


		"""
		res = super(Standard_QWidget,self).grabGesture(type,flags)
		return res
	#----------------------------------------------------------------------
	def grabMouse(self,arg__1):
		"""
		grabMouse(arg__1)
			arg__1=QT.QCursor

		This function overloads PySide.QT.QWidget.grabMouse() .
		Grabs the mouse input and changes the cursor shape.
		The cursor will assume shape cursor (for as long as the mouse focus is grabbed) and this widget will be the only one to receive mouse events until PySide.QT.QWidget.releaseMouse() is called().
		"""
		res = super(Standard_QWidget,self).grabMouse(arg__1)
		return res
	#----------------------------------------------------------------------
	def grabShortcut(self,key,context=None):
		"""
		grabShortcut(key,context=None)
			key=QT.QKeySequence
			context=QT.Qt.ShortcutContext


		"""
		res = super(Standard_QWidget,self).grabShortcut(key,context)

		return res
	#----------------------------------------------------------------------
	def heightForWidth(self,arg__1):
		"""
		heightForWidth(arg__1)
			arg__1=QT.int

		Returns the preferred height for this widget, given the width w .
		If this widget has a layout, the default implementation returns the layouts preferred height
		if there is no layout, the default implementation returns -1 indicating that the preferred height does not depend on the width.
		"""
		res = super(Standard_QWidget,self).heightForWidth(arg__1)

		return res
	#----------------------------------------------------------------------
	def hideEvent(self,event):
		"""
		hideEvent(event)
			event=QT.QHideEvent

		This event handler can be reimplemented in a subclass to receive widget hide events
		The event is passed in the event parameter.
		Hide events are sent to widgets immediately after they have been hidden.
		Note: A widget receives spontaneous show and hide events when its mapping status is changed by the window system, e.g
		a spontaneous hide event when the user minimizes the window, and a spontaneous show event when the window is restored again
		After receiving a spontaneous hide event, a widget is still considered visible in the sense of PySide.QT.QWidget.isVisible() .
		"""
		res = super(Standard_QWidget,self).hideEvent(event)
		return res
	#----------------------------------------------------------------------
	def inputMethodEvent(self,event):
		"""
		inputMethodEvent(event)
			event=QT.QInputMethodEvent

		This event handler, for event event , can be reimplemented in a subclass to receive Input Method composition events
		This handler is called when the state of the input method changes.
		Note that when creating custom text editing widgets, the Qt.WA_InputMethodEnabled window attribute must be set explicitly (using the PySide.QT.QWidget.setAttribute() function) in order to receive input method events.
		The default implementation calls event->ignore(), which rejects the Input Method event
		See the PySide.QT.QInputMethodEvent documentation for more details.
		"""
		res = super(Standard_QWidget,self).inputMethodEvent(event)
		return res
	#----------------------------------------------------------------------
	def inputMethodQuery(self,arg__1):
		"""
		inputMethodQuery(arg__1)
			arg__1=QT.Qt.InputMethodQuery


		"""
		res = super(Standard_QWidget,self).inputMethodQuery(arg__1)
		return res
	#----------------------------------------------------------------------
	def insertAction(self,before,action):
		"""
		insertAction(before,action)
			before=QT.QAction
			action=QT.QAction

		Inserts the action action to this widgets list of actions, before the action before
		It appends the action if before is 0 or before is not a valid action for this widget.
		A PySide.QT.QWidget should only have one of each action.
		"""
		res = super(Standard_QWidget,self).insertAction(before,action)
		return res
	#----------------------------------------------------------------------
	def insertActions(self,before,actions):
		"""
		insertActions(before,actions)
			before=QT.QAction
			actions=unKnown


		"""
		res = super(Standard_QWidget,self).insertActions(before,actions)
		return res
	#----------------------------------------------------------------------
	def isAncestorOf(self,child):
		"""
		isAncestorOf(child)
			child=QT.QWidget

		Returns true if this widget is a parent, (or grandparent and so on to any level), of the given child , and both widgets are within the same window; otherwise returns false.
		"""
		res = super(Standard_QWidget,self).isAncestorOf(child)

		return res
	#----------------------------------------------------------------------
	def isEnabledTo(self,arg__1):
		"""
		isEnabledTo(arg__1)
			arg__1=QT.QWidget

		Returns true if this widget would become enabled if ancestor is enabled; otherwise returns false.
		This is the case if neither the widget itself nor every parent up to but excluding ancestor has been explicitly disabled.
		isEnabledTo(0) is equivalent to PySide.QT.QWidget.isEnabled() .
		"""
		res = super(Standard_QWidget,self).isEnabledTo(arg__1)

		return res
	#----------------------------------------------------------------------
	def isVisibleTo(self,arg__1):
		"""
		isVisibleTo(arg__1)
			arg__1=QT.QWidget

		Returns true if this widget would become visible if ancestor is shown; otherwise returns false.
		The true case occurs if neither the widget itself nor any parent up to but excluding ancestor has been explicitly hidden.
		This function will still return true if the widget is obscured by other windows on the screen, but could be physically visible if it or they were to be moved.
		isVisibleTo(0) is identical to PySide.QT.QWidget.isVisible() .
		"""
		res = super(Standard_QWidget,self).isVisibleTo(arg__1)

		return res
	#----------------------------------------------------------------------
	def keyPressEvent(self,event):
		"""
		keyPressEvent(event)
			event=QT.QKeyEvent

		This event handler, for event event , can be reimplemented in a subclass to receive key press events for the widget.
		A widget must call PySide.QT.QWidget.setFocusPolicy() to accept focus initially and have focus in order to receive a key press event.
		If you reimplement this handler, it is very important that you call the base class implementation if you do not act upon the key.
		The default implementation closes popup widgets if the user presses Esc
		Otherwise the event is ignored, so that the widgets parent can interpret it.
		Note that PySide.QT.QKeyEvent starts with isAccepted() == true, so you do not need to call QKeyEvent.accept() - just do not call the base class implementation if you act upon the key.
		"""
		res = super(Standard_QWidget,self).keyPressEvent(event)
		return res
	#----------------------------------------------------------------------
	def keyReleaseEvent(self,event):
		"""
		keyReleaseEvent(event)
			event=QT.QKeyEvent

		This event handler, for event event , can be reimplemented in a subclass to receive key release events for the widget.
		A widget must accept focus initially and have focus in order to receive a key release event.
		If you reimplement this handler, it is very important that you call the base class implementation if you do not act upon the key.
		The default implementation ignores the event, so that the widgets parent can interpret it.
		Note that PySide.QT.QKeyEvent starts with isAccepted() == true, so you do not need to call QKeyEvent.accept() - just do not call the base class implementation if you act upon the key.
		"""
		res = super(Standard_QWidget,self).keyReleaseEvent(event)
		return res
	#----------------------------------------------------------------------
	def leaveEvent(self,event):
		"""
		leaveEvent(event)
			event=QT.QEvent

		This event handler can be reimplemented in a subclass to receive widget leave events which are passed in the event parameter.
		A leave event is sent to the widget when the mouse cursor leaves the widget.
		"""
		res = super(Standard_QWidget,self).leaveEvent(event)
		return res
	#----------------------------------------------------------------------
	def mapFrom(self,arg__1,arg__2):
		"""
		mapFrom(arg__1,arg__2)
			arg__1=QT.QWidget
			arg__2=QT.QPoint

		Translates the widget coordinate pos from the coordinate system of parent to this widgets coordinate system
		The parent must not be 0 and must be a parent of the calling widget.
		"""
		res = super(Standard_QWidget,self).mapFrom(arg__1,arg__2)
		isinstance(res,QT.QPoint)
		return res
	#----------------------------------------------------------------------
	def mapFromGlobal(self,arg__1):
		"""
		mapFromGlobal(arg__1)
			arg__1=QT.QPoint

		Translates the global screen coordinate pos to widget coordinates.
		"""
		res = super(Standard_QWidget,self).mapFromGlobal(arg__1)
		isinstance(res,QT.QPoint)
		return res
	#----------------------------------------------------------------------
	def mapFromParent(self,arg__1):
		"""
		mapFromParent(arg__1)
			arg__1=QT.QPoint

		Translates the parent widget coordinate pos to widget coordinates.
		Same as PySide.QT.QWidget.mapFromGlobal() if the widget has no parent.
		"""
		res = super(Standard_QWidget,self).mapFromParent(arg__1)
		isinstance(res,QT.QPoint)
		return res
	#----------------------------------------------------------------------
	def mapTo(self,arg__1,arg__2):
		"""
		mapTo(arg__1,arg__2)
			arg__1=QT.QWidget
			arg__2=QT.QPoint

		Translates the widget coordinate pos to the coordinate system of parent
		The parent must not be 0 and must be a parent of the calling widget.
		"""
		res = super(Standard_QWidget,self).mapTo(arg__1,arg__2)
		isinstance(res,QT.QPoint)
		return res
	#----------------------------------------------------------------------
	def mapToGlobal(self,arg__1):
		"""
		mapToGlobal(arg__1)
			arg__1=QT.QPoint

		Translates the widget coordinate pos to global screen coordinates
		For example, mapToGlobal(QPoint(0,0)) would give the global coordinates of the top-left pixel of the widget.
		"""
		res = super(Standard_QWidget,self).mapToGlobal(arg__1)
		isinstance(res,QT.QPoint)
		return res
	#----------------------------------------------------------------------
	def mapToParent(self,arg__1):
		"""
		mapToParent(arg__1)
			arg__1=QT.QPoint

		Translates the widget coordinate pos to a coordinate in the parent widget.
		Same as PySide.QT.QWidget.mapToGlobal() if the widget has no parent.
		"""
		res = super(Standard_QWidget,self).mapToParent(arg__1)
		isinstance(res,QT.QPoint)
		return res
	#----------------------------------------------------------------------
	def mouseDoubleClickEvent(self,event):
		"""
		mouseDoubleClickEvent(event)
			event=QT.QMouseEvent

		This event handler, for event event , can be reimplemented in a subclass to receive mouse double click events for the widget.
		The default implementation generates a normal mouse press event.
		"""
		res = super(Standard_QWidget,self).mouseDoubleClickEvent(event)
		return res
	#----------------------------------------------------------------------
	def mouseMoveEvent(self,event):
		"""
		mouseMoveEvent(event)
			event=QT.QMouseEvent

		This event handler, for event event , can be reimplemented in a subclass to receive mouse move events for the widget.
		If mouse tracking is switched off, mouse move events only occur if a mouse button is pressed while the mouse is being moved
		If mouse tracking is switched on, mouse move events occur even if no mouse button is pressed.
		QMouseEvent.pos() reports the position of the mouse cursor, relative to this widget
		For press and release events, the position is usually the same as the position of the last mouse move event, but it might be different if the users hand shakes
		This is a feature of the underlying window system, not Qt.
		If you want to show a tooltip immediately, while the mouse is moving (e.g., to get the mouse coordinates with QMouseEvent.pos() and show them as a tooltip), you must first enable mouse tracking as described above
		Then, to ensure that the tooltip is updated immediately, you must call QToolTip.showText() instead of PySide.QT.QWidget.setToolTip() in your implementation of PySide.QT.QWidget.mouseMoveEvent() .
		"""
		res = super(Standard_QWidget,self).mouseMoveEvent(event)
		return res
	#----------------------------------------------------------------------
	def mousePressEvent(self,event):
		"""
		mousePressEvent(event)
			event=QT.QMouseEvent

		This event handler, for event event , can be reimplemented in a subclass to receive mouse press events for the widget.
		If you create new widgets in the PySide.QT.QWidget.mousePressEvent() the PySide.QT.QWidget.mouseReleaseEvent() may not end up where you expect, depending on the underlying window system (or X11 window manager), the widgets location and maybe more.
		The default implementation implements the closing of popup widgets when you click outside the window
		For other widget types it does nothing.
		"""
		res = super(Standard_QWidget,self).mousePressEvent(event)
		return res
	#----------------------------------------------------------------------
	def mouseReleaseEvent(self,event):
		"""
		mouseReleaseEvent(event)
			event=QT.QMouseEvent

		This event handler, for event event , can be reimplemented in a subclass to receive mouse release events for the widget.
		"""
		res = super(Standard_QWidget,self).mouseReleaseEvent(event)
		return res
	#----------------------------------------------------------------------
	def move(self,*args,**kwargs):
		"""
		move(x,y)
			x=QT.int
			y=QT.int

		move(arg__1)
			arg__1=QT.QPoint

		This is an overloaded function.
		This corresponds to move( PySide.QT.QPoint (x , y )).
		"""
		res = super(Standard_QWidget,self).move(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def moveEvent(self,event):
		"""
		moveEvent(event)
			event=QT.QMoveEvent

		This event handler can be reimplemented in a subclass to receive widget move events which are passed in the event parameter
		When the widget receives this event, it is already at the new position.
		The old position is accessible through QMoveEvent.oldPos() .
		"""
		res = super(Standard_QWidget,self).moveEvent(event)
		return res
	#----------------------------------------------------------------------
	def overrideWindowFlags(self,type):
		"""
		overrideWindowFlags(type)
			type=QT.Qt.WindowFlags


		"""
		res = super(Standard_QWidget,self).overrideWindowFlags(type)
		return res
	#----------------------------------------------------------------------
	def overrideWindowState(self,state):
		"""
		overrideWindowState(state)
			state=QT.Qt.WindowStates


		"""
		res = super(Standard_QWidget,self).overrideWindowState(state)
		return res
	#----------------------------------------------------------------------
	def paintEvent(self,event):
		"""
		paintEvent(event)
			event=QT.QPaintEvent

		This event handler can be reimplemented in a subclass to receive paint events passed in event .
		A paint event is a request to repaint all or part of a widget
		It can happen for one of the following reasons:
		Many widgets can simply repaint their entire surface when asked to, but some slow widgets need to optimize by painting only the requested region: QPaintEvent.region()
		This speed optimization does not change the result, as painting is clipped to that region during event processing
		PySide.QT.QListView and PySide.QT.QTableView do this, for example.
		Qt also tries to speed up painting by merging multiple paint events into one
		When PySide.QT.QWidget.update() is called several times or the window system sends several paint events, Qt merges these events into one event with a larger region (see QRegion.united() )
		The PySide.QT.QWidget.repaint() function does not permit this optimization, so we suggest using PySide.QT.QWidget.update() whenever possible.
		When the paint event occurs, the update region has normally been erased, so you are painting on the widgets background.
		The background can be set using PySide.QT.QWidget.setBackgroundRole() and PySide.QT.QWidget.setPalette() .
		Since Qt 4.0, PySide.QT.QWidget automatically double-buffers its painting, so there is no need to write double-buffering code in PySide.QT.QWidget.paintEvent() to avoid flicker.
		Note for the X11 platform : It is possible to toggle global double buffering by calling qt_x11_set_global_double_buffer()
		For example,
		"""
		res = super(Standard_QWidget,self).paintEvent(event)
		return res
	#----------------------------------------------------------------------
	def releaseShortcut(self,id):
		"""
		releaseShortcut(id)
			id=QT.int

		Removes the shortcut with the given id from Qts shortcut system
		The widget will no longer receive QEvent.Shortcut events for the shortcuts key sequence (unless it has other shortcuts with the same key sequence).
		"""
		res = super(Standard_QWidget,self).releaseShortcut(id)
		return res
	#----------------------------------------------------------------------
	def removeAction(self,action):
		"""
		removeAction(action)
			action=QT.QAction

		Removes the action action from this widgets list of actions.
		"""
		res = super(Standard_QWidget,self).removeAction(action)
		return res
	#----------------------------------------------------------------------
	def render(self,*args,**kwargs):
		"""
		render(target,targetOffset=None,sourceRegion=None,renderFlags=None)
			target=QT.QPaintDevice
			targetOffset=QT.QPoint
			sourceRegion=QT.QRegion
			renderFlags=QT.QWidget.RenderFlags

		render(painter,targetOffset,sourceRegion=None,renderFlags=None)
			painter=QT.QPainter
			targetOffset=QT.QPoint
			sourceRegion=QT.QRegion
			renderFlags=QT.QWidget.RenderFlags


		"""
		res = super(Standard_QWidget,self).render(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def repaint(self,*args,**kwargs):
		"""
		repaint(x,y,w,h)
			x=QT.int
			y=QT.int
			w=QT.int
			h=QT.int

		repaint(arg__1)
			arg__1=QT.QRegion

		repaint(arg__1)
			arg__1=QT.QRect

		This is an overloaded function.
		This version repaints a rectangle (x , y , w , h ) inside the widget.
		If w is negative, it is replaced with width() - x , and if h is negative, it is replaced width height() - y .
		"""
		res = super(Standard_QWidget,self).repaint(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def resize(self,*args,**kwargs):
		"""
		resize(arg__1)
			arg__1=QT.QSize

		resize(w,h)
			w=QT.int
			h=QT.int

		This property holds the size of the widget excluding any window frame.
		If the widget is visible when it is being resized, it receives a resize event ( PySide.QT.QWidget.resizeEvent() ) immediately
		If the widget is not currently visible, it is guaranteed to receive an event before it is shown.
		The size is adjusted if it lies outside the range defined by PySide.QT.QWidget.minimumSize() and PySide.QT.QWidget.maximumSize() .
		By default, this property contains a value that depends on the users platform and screen geometry.
		"""
		res = super(Standard_QWidget,self).resize(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def resizeEvent(self,event):
		"""
		resizeEvent(event)
			event=QT.QResizeEvent

		This event handler can be reimplemented in a subclass to receive widget resize events which are passed in the event parameter
		When PySide.QT.QWidget.resizeEvent() is called, the widget already has its new geometry
		The old size is accessible through QResizeEvent.oldSize() .
		The widget will be erased and receive a paint event immediately after processing the resize event
		No drawing need be (or should be) done inside this handler.
		"""
		res = super(Standard_QWidget,self).resizeEvent(event)
		return res
	#----------------------------------------------------------------------
	def restoreGeometry(self,geometry):
		"""
		restoreGeometry(geometry)
			geometry=QT.QByteArray

		Restores the geometry and state top-level widgets stored in the byte array geometry
		Returns true on success; otherwise returns false.
		If the restored geometry is off-screen, it will be modified to be inside the available screen geometry.
		To restore geometry saved using PySide.QT.QSettings , you can use code like this:
		See the Window Geometry documentation for an overview of geometry issues with windows.
		Use QMainWindow.restoreState() to restore the geometry and the state of toolbars and dock widgets.
		"""
		res = super(Standard_QWidget,self).restoreGeometry(geometry)

		return res
	#----------------------------------------------------------------------
	def scroll(self,*args,**kwargs):
		"""
		scroll(dx,dy)
			dx=QT.int
			dy=QT.int

		scroll(dx,dy,arg__3)
			dx=QT.int
			dy=QT.int
			arg__3=QT.QRect

		Scrolls the widget including its children dx pixels to the right and dy downward
		Both dx and dy may be negative.
		After scrolling, the widgets will receive paint events for the areas that need to be repainted
		For widgets that Qt knows to be opaque, this is only the newly exposed parts
		For example, if an opaque widget is scrolled 8 pixels to the left, only an 8-pixel wide stripe at the right edge needs updating.
		Since widgets propagate the contents of their parents by default, you need to set the PySide.QT.QWidget.autoFillBackground() property, or use PySide.QT.QWidget.setAttribute() to set the Qt.WA_OpaquePaintEvent attribute, to make a widget opaque.
		For widgets that use contents propagation, a scroll will cause an update of the entire scroll area.
		"""
		res = super(Standard_QWidget,self).scroll(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setAcceptDrops(self,on):
		"""
		setAcceptDrops(on)
			on=QT.bool

		This property holds whether drop events are enabled for this widget.
		Setting this property to true announces to the system that this widget may be able to accept drop events.
		If the widget is the desktop ( PySide.QT.QWidget.windowType() == Qt.Desktop ), this may fail if another application is using the desktop; you can call PySide.QT.QWidget.acceptDrops() to test if this occurs.
		By default, this property is false.
		"""
		res = super(Standard_QWidget,self).setAcceptDrops(on)
		return res
	#----------------------------------------------------------------------
	def setAccessibleDescription(self,description):
		"""
		setAccessibleDescription(description)
			description=unicode

		This property holds the widgets description as seen by assistive technologies.
		By default, this property contains an empty string.
		"""
		res = super(Standard_QWidget,self).setAccessibleDescription(description)
		return res
	#----------------------------------------------------------------------
	def setAccessibleName(self,name):
		"""
		setAccessibleName(name)
			name=unicode

		This property holds the widgets name as seen by assistive technologies.
		This property is used by accessible clients to identify, find, or announce the widget for accessible clients.
		By default, this property contains an empty string.
		"""
		res = super(Standard_QWidget,self).setAccessibleName(name)
		return res
	#----------------------------------------------------------------------
	def setAttribute(self,arg__1,on=None):
		"""
		setAttribute(arg__1,on=None)
			arg__1=QT.Qt.WidgetAttribute
			on=QT.bool


		"""
		res = super(Standard_QWidget,self).setAttribute(arg__1,on)
		return res
	#----------------------------------------------------------------------
	def setAutoFillBackground(self,enabled):
		"""
		setAutoFillBackground(enabled)
			enabled=QT.bool

		This property holds whether the widget background is filled automatically.
		If enabled, this property will cause Qt to fill the background of the widget before invoking the paint event
		The color used is defined by the QPalette.Window color role from the widgets palette .
		In addition, Windows are always filled with QPalette.Window , unless the WA_OpaquePaintEvent or WA_NoSystemBackground attributes are set.
		This property cannot be turned off (i.e., set to false) if a widgets parent has a static gradient for its background.
		By default, this property is false.
		"""
		res = super(Standard_QWidget,self).setAutoFillBackground(enabled)
		return res
	#----------------------------------------------------------------------
	def setBackgroundRole(self,arg__1):
		"""
		setBackgroundRole(arg__1)
			arg__1=QT.QPalette.ColorRole


		"""
		res = super(Standard_QWidget,self).setBackgroundRole(arg__1)
		return res
	#----------------------------------------------------------------------
	def setBaseSize(self,*args,**kwargs):
		"""
		setBaseSize(arg__1)
			arg__1=QT.QSize

		setBaseSize(basew,baseh)
			basew=QT.int
			baseh=QT.int

		This property holds the base size of the widget.
		The base size is used to calculate a proper widget size if the widget defines PySide.QT.QWidget.sizeIncrement() .
		By default, for a newly-created widget, this property contains a size with zero width and height.
		"""
		res = super(Standard_QWidget,self).setBaseSize(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setContentsMargins(self,*args,**kwargs):
		"""
		setContentsMargins(left,top,right,bottom)
			left=QT.int
			top=QT.int
			right=QT.int
			bottom=QT.int

		setContentsMargins(margins)
			margins=QT.QMargins

		Sets the margins around the contents of the widget to have the sizes left , top , right , and bottom
		The margins are used by the layout system, and may be used by subclasses to specify the area to draw in (e.g
		excluding the frame).
		Changing the margins will trigger a PySide.QT.QWidget.resizeEvent() .
		"""
		res = super(Standard_QWidget,self).setContentsMargins(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setContextMenuPolicy(self,policy):
		"""
		setContextMenuPolicy(policy)
			policy=QT.Qt.ContextMenuPolicy

		This property holds how the widget shows a context menu.
		The default value of this property is Qt.DefaultContextMenu , which means the PySide.QT.QWidget.contextMenuEvent() handler is called
		Other values are Qt.NoContextMenu , Qt.PreventContextMenu , Qt.ActionsContextMenu , and Qt.CustomContextMenu
		With Qt.CustomContextMenu , the signal PySide.QT.QWidget.customContextMenuRequested() is emitted.
		"""
		res = super(Standard_QWidget,self).setContextMenuPolicy(policy)
		return res
	#----------------------------------------------------------------------
	def setCursor(self,arg__1):
		"""
		setCursor(arg__1)
			arg__1=QT.QCursor

		This property holds the cursor shape for this widget.
		The mouse cursor will assume this shape when its over this widget
		See the list of predefined cursor objects for a range of useful shapes.
		An editor widget might use an I-beam cursor:
		If no cursor has been set, or after a call to PySide.QT.QWidget.unsetCursor() , the parents cursor is used.
		By default, this property contains a cursor with the Qt.ArrowCursor shape.
		Some underlying window implementations will reset the cursor if it leaves a widget even if the mouse is grabbed
		If you want to have a cursor set for all widgets, even when outside the window, consider QApplication.setOverrideCursor() .
		"""
		res = super(Standard_QWidget,self).setCursor(arg__1)
		return res
	#----------------------------------------------------------------------
	def setFixedHeight(self,h):
		"""
		setFixedHeight(h)
			h=QT.int

		Sets both the minimum and maximum heights of the widget to h without changing the widths
		Provided for convenience.
		"""
		res = super(Standard_QWidget,self).setFixedHeight(h)
		return res
	#----------------------------------------------------------------------
	def setFixedSize(self,*args,**kwargs):
		"""
		setFixedSize(w,h)
			w=QT.int
			h=QT.int

		setFixedSize(arg__1)
			arg__1=QT.QSize

		This is an overloaded function.
		Sets the width of the widget to w and the height to h .
		"""
		res = super(Standard_QWidget,self).setFixedSize(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setFixedWidth(self,w):
		"""
		setFixedWidth(w)
			w=QT.int

		Sets both the minimum and maximum width of the widget to w without changing the heights
		Provided for convenience.
		"""
		res = super(Standard_QWidget,self).setFixedWidth(w)
		return res
	#----------------------------------------------------------------------
	def setFocus(self,reason):
		"""
		setFocus(reason)
			reason=QT.Qt.FocusReason


		"""
		res = super(Standard_QWidget,self).setFocus(reason)
		return res
	#----------------------------------------------------------------------
	def setFocusPolicy(self,policy):
		"""
		setFocusPolicy(policy)
			policy=QT.Qt.FocusPolicy

		This property holds the way the widget accepts keyboard focus.
		The policy is Qt.TabFocus if the widget accepts keyboard focus by tabbing, Qt.ClickFocus if the widget accepts focus by clicking, Qt.StrongFocus if it accepts both, and Qt.NoFocus (the default) if it does not accept focus at all.
		You must enable keyboard focus for a widget if it processes keyboard events
		This is normally done from the widgets constructor
		For instance, the PySide.QT.QLineEdit constructor calls setFocusPolicy( Qt.StrongFocus ).
		If the widget has a focus proxy, then the focus policy will be propagated to it.
		"""
		res = super(Standard_QWidget,self).setFocusPolicy(policy)
		return res
	#----------------------------------------------------------------------
	def setFocusProxy(self,arg__1):
		"""
		setFocusProxy(arg__1)
			arg__1=QT.QWidget

		Sets the widgets focus proxy to widget w
		If w is 0, the function resets this widget to have no focus proxy.
		Some widgets can have focus, but create a child widget, such as PySide.QT.QLineEdit , to actually handle the focus
		In this case, the widget can set the line edit to be its focus proxy.
		PySide.QT.QWidget.setFocusProxy() sets the widget which will actually get focus when this widget gets it
		If there is a focus proxy, PySide.QT.QWidget.setFocus() and PySide.QT.QWidget.hasFocus() operate on the focus proxy.
		"""
		res = super(Standard_QWidget,self).setFocusProxy(arg__1)
		return res
	#----------------------------------------------------------------------
	def setFont(self,arg__1):
		"""
		setFont(arg__1)
			arg__1=QT.QFont

		This property holds the font currently set for the widget.
		This property describes the widgets requested font
		The font is used by the widgets style when rendering standard components, and is available as a means to ensure that custom widgets can maintain consistency with the native platforms look and feel
		Its common that different platforms, or different styles, define different fonts for an application.
		When you assign a new font to a widget, the properties from this font are combined with the widgets default font to form the widgets final font
		You can call PySide.QT.QWidget.fontInfo() to get a copy of the widgets final font
		The final font is also used to initialize PySide.QT.QPainter s font.
		The default depends on the system environment
		PySide.QT.QApplication maintains a system/theme font which serves as a default for all widgets
		There may also be special font defaults for certain types of widgets
		You can also define default fonts for widgets yourself by passing a custom font and the name of a widget to QApplication.setFont()
		Finally, the font is matched against Qts font database to find the best match.
		PySide.QT.QWidget propagates explicit font properties from parent to child
		If you change a specific property on a font and assign that font to a widget, that property will propagate to all the widgets children, overriding any system defaults for that property
		Note that fonts by default dont propagate to windows (see PySide.QT.QWidget.isWindow() ) unless the Qt.WA_WindowPropagation attribute is enabled.
		PySide.QT.QWidget s font propagation is similar to its palette propagation.
		The current style, which is used to render the content of all standard Qt widgets, is free to choose to use the widget font, or in some cases, to ignore it (partially, or completely)
		In particular, certain styles like GTK style, Mac style, Windows XP, and Vista style, apply special modifications to the widget font to match the platforms native look and feel
		Because of this, assigning properties to a widgets font is not guaranteed to change the appearance of the widget
		Instead, you may choose to apply a PySide.QT.QWidget.styleSheet() .
		"""
		res = super(Standard_QWidget,self).setFont(arg__1)
		return res
	#----------------------------------------------------------------------
	def setForegroundRole(self,arg__1):
		"""
		setForegroundRole(arg__1)
			arg__1=QT.QPalette.ColorRole


		"""
		res = super(Standard_QWidget,self).setForegroundRole(arg__1)
		return res
	#----------------------------------------------------------------------
	def setGeometry(self,*args,**kwargs):
		"""
		setGeometry(x,y,w,h)
			x=QT.int
			y=QT.int
			w=QT.int
			h=QT.int

		setGeometry(arg__1)
			arg__1=QT.QRect

		This is an overloaded function.
		This corresponds to setGeometry( PySide.QT.QRect (x , y , w , h )).
		"""
		res = super(Standard_QWidget,self).setGeometry(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setGraphicsEffect(self,effect):
		"""
		setGraphicsEffect(effect)
			effect=QT.QGraphicsEffect

		The setGraphicsEffect function is for setting the widgets graphics effect.
		Sets effect as the widgets effect
		If there already is an effect installed on this widget, PySide.QT.QWidget will delete the existing effect before installing the new effect .
		If effect is the installed on a different widget, PySide.QT.QWidget.setGraphicsEffect() will remove the effect from the widget and install it on this widget.
		PySide.QT.QWidget takes ownership of effect .
		"""
		res = super(Standard_QWidget,self).setGraphicsEffect(effect)
		return res
	#----------------------------------------------------------------------
	def setInputContext(self,arg__1):
		"""
		setInputContext(arg__1)
			arg__1=QT.QInputContext

		This function sets the input context context on this widget.
		Qt takes ownership of the given input context .
		"""
		res = super(Standard_QWidget,self).setInputContext(arg__1)
		return res
	#----------------------------------------------------------------------
	def setInputMethodHints(self,hints):
		"""
		setInputMethodHints(hints)
			hints=QT.Qt.InputMethodHints

		This property holds What input method specific hints the widget has..
		This is only relevant for input widgets
		It is used by the input method to retrieve hints as to how the input method should operate
		For example, if the Qt.ImhFormattedNumbersOnly flag is set, the input method may change its visual components to reflect that only numbers can be entered.
		The default value is Qt.ImhNone .
		"""
		res = super(Standard_QWidget,self).setInputMethodHints(hints)
		return res
	#----------------------------------------------------------------------
	def setLayout(self,arg__1):
		"""
		setLayout(arg__1)
			arg__1=QT.QLayout

		Sets the layout manager for this widget to layout .
		If there already is a layout manager installed on this widget, PySide.QT.QWidget wont let you install another
		You must first delete the existing layout manager (returned by PySide.QT.QWidget.layout() ) before you can call PySide.QT.QWidget.setLayout() with the new layout.
		If layout is the layout manger on a different widget, PySide.QT.QWidget.setLayout() will reparent the layout and make it the layout manager for this widget.
		Example:
		An alternative to calling this function is to pass this widget to the layouts constructor.
		The PySide.QT.QWidget will take ownership of layout .
		"""
		res = super(Standard_QWidget,self).setLayout(arg__1)
		return res
	#----------------------------------------------------------------------
	def setLayoutDirection(self,direction):
		"""
		setLayoutDirection(direction)
			direction=QT.Qt.LayoutDirection

		This property holds the layout direction for this widget.
		By default, this property is set to Qt.LeftToRight .
		When the layout direction is set on a widget, it will propagate to the widgets children, but not to a child that is a window and not to a child for which PySide.QT.QWidget.setLayoutDirection() has been explicitly called
		Also, child widgets added afterPySide.QT.QWidget.setLayoutDirection() has been called for the parent do not inherit the parents layout direction.
		This method no longer affects text layout direction since Qt 4.7.
		"""
		res = super(Standard_QWidget,self).setLayoutDirection(direction)
		return res
	#----------------------------------------------------------------------
	def setLocale(self,locale):
		"""
		setLocale(locale)
			locale=QT.QLocale

		This property holds the widgets locale.
		As long as no special locale has been set, this is either the parents locale or (if this widget is a top level widget), the default locale.
		If the widget displays dates or numbers, these should be formatted using the widgets locale.
		"""
		res = super(Standard_QWidget,self).setLocale(locale)
		return res
	#----------------------------------------------------------------------
	def setMask(self,*args,**kwargs):
		"""
		setMask(arg__1)
			arg__1=QT.QBitmap

		setMask(arg__1)
			arg__1=QT.QRegion

		Causes only the pixels of the widget for which bitmap has a corresponding 1 bit to be visible
		If the region includes pixels outside the PySide.QT.QWidget.rect() of the widget, window system controls in that area may or may not be visible, depending on the platform.
		Note that this effect can be slow if the region is particularly complex.
		The following code shows how an image with an alpha channel can be used to generate a mask for a widget:
		The label shown by this code is masked using the image it contains, giving the appearance that an irregularly-shaped image is being drawn directly onto the screen.
		Masked widgets receive mouse events only on their visible portions.
		"""
		res = super(Standard_QWidget,self).setMask(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setMaximumHeight(self,maxh):
		"""
		setMaximumHeight(maxh)
			maxh=QT.int

		This property holds the widgets maximum height in pixels.
		This property corresponds to the height held by the PySide.QT.QWidget.maximumSize() property.
		By default, this property contains a value of 16777215.
		"""
		res = super(Standard_QWidget,self).setMaximumHeight(maxh)
		return res
	#----------------------------------------------------------------------
	def setMaximumSize(self,*args,**kwargs):
		"""
		setMaximumSize(arg__1)
			arg__1=QT.QSize

		setMaximumSize(maxw,maxh)
			maxw=QT.int
			maxh=QT.int

		This property holds the widgets maximum size in pixels.
		The widget cannot be resized to a larger size than the maximum widget size.
		By default, this property contains a size in which both width and height have values of 16777215.
		"""
		res = super(Standard_QWidget,self).setMaximumSize(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setMaximumWidth(self,maxw):
		"""
		setMaximumWidth(maxw)
			maxw=QT.int

		This property holds the widgets maximum width in pixels.
		This property corresponds to the width held by the PySide.QT.QWidget.maximumSize() property.
		By default, this property contains a value of 16777215.
		"""
		res = super(Standard_QWidget,self).setMaximumWidth(maxw)
		return res
	#----------------------------------------------------------------------
	def setMinimumHeight(self,minh):
		"""
		setMinimumHeight(minh)
			minh=QT.int

		This property holds the widgets minimum height in pixels.
		This property corresponds to the height held by the PySide.QT.QWidget.minimumSize() property.
		By default, this property has a value of 0.
		"""
		res = super(Standard_QWidget,self).setMinimumHeight(minh)
		return res
	#----------------------------------------------------------------------
	def setMinimumSize(self,*args,**kwargs):
		"""
		setMinimumSize(minw,minh)
			minw=QT.int
			minh=QT.int

		setMinimumSize(arg__1)
			arg__1=QT.QSize

		This is an overloaded function.
		This function corresponds to setMinimumSize( PySide.QT.QSize (minw, minh))
		Sets the minimum width to minw and the minimum height to minh .
		"""
		res = super(Standard_QWidget,self).setMinimumSize(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setMinimumWidth(self,minw):
		"""
		setMinimumWidth(minw)
			minw=QT.int

		This property holds the widgets minimum width in pixels.
		This property corresponds to the width held by the PySide.QT.QWidget.minimumSize() property.
		By default, this property has a value of 0.
		"""
		res = super(Standard_QWidget,self).setMinimumWidth(minw)
		return res
	#----------------------------------------------------------------------
	def setMouseTracking(self,enable):
		"""
		setMouseTracking(enable)
			enable=QT.bool

		This property holds whether mouse tracking is enabled for the widget.
		If mouse tracking is disabled (the default), the widget only receives mouse move events when at least one mouse button is pressed while the mouse is being moved.
		If mouse tracking is enabled, the widget receives mouse move events even if no buttons are pressed.
		"""
		res = super(Standard_QWidget,self).setMouseTracking(enable)
		return res
	#----------------------------------------------------------------------
	def setPalette(self,arg__1):
		"""
		setPalette(arg__1)
			arg__1=QT.QPalette

		This property holds the widgets palette.
		This property describes the widgets palette
		The palette is used by the widgets style when rendering standard components, and is available as a means to ensure that custom widgets can maintain consistency with the native platforms look and feel
		Its common that different platforms, or different styles, have different palettes.
		When you assign a new palette to a widget, the color roles from this palette are combined with the widgets default palette to form the widgets final palette
		The palette entry for the widgets background role is used to fill the widgets background (see QWidget.autoFillBackground ), and the foreground role initializes PySide.QT.QPainter s pen.
		The default depends on the system environment
		PySide.QT.QApplication maintains a system/theme palette which serves as a default for all widgets
		There may also be special palette defaults for certain types of widgets (e.g., on Windows XP and Vista, all classes that derive from PySide.QT.QMenuBar have a special default palette)
		You can also define default palettes for widgets yourself by passing a custom palette and the name of a widget to QApplication.setPalette()
		Finally, the style always has the option of polishing the palette as its assigned (see QStyle.polish() ).
		PySide.QT.QWidget propagates explicit palette roles from parent to child
		If you assign a brush or color to a specific role on a palette and assign that palette to a widget, that role will propagate to all the widgets children, overriding any system defaults for that role
		Note that palettes by default dont propagate to windows (see PySide.QT.QWidget.isWindow() ) unless the Qt.WA_WindowPropagation attribute is enabled.
		PySide.QT.QWidget s palette propagation is similar to its font propagation.
		The current style, which is used to render the content of all standard Qt widgets, is free to choose colors and brushes from the widget palette, or in some cases, to ignore the palette (partially, or completely)
		In particular, certain styles like GTK style, Mac style, Windows XP, and Vista style, depend on third party APIs to render the content of widgets, and these styles typically do not follow the palette
		Because of this, assigning roles to a widgets palette is not guaranteed to change the appearance of the widget
		Instead, you may choose to apply a PySide.QT.QWidget.styleSheet()
		You can refer to our Knowledge Base article here for more information.
		"""
		res = super(Standard_QWidget,self).setPalette(arg__1)
		return res
	#----------------------------------------------------------------------
	def setParent(self,*args,**kwargs):
		"""
		setParent(parent,f)
			parent=QT.QWidget
			f=QT.Qt.WindowFlags

		setParent(parent)
			parent=QT.QWidget


		"""
		res = super(Standard_QWidget,self).setParent(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setShortcutAutoRepeat(self,id,enable=None):
		"""
		setShortcutAutoRepeat(id,enable=None)
			id=QT.int
			enable=QT.bool

		If enable is true, auto repeat of the shortcut with the given id is enabled; otherwise it is disabled.
		"""
		res = super(Standard_QWidget,self).setShortcutAutoRepeat(id,enable)
		return res
	#----------------------------------------------------------------------
	def setShortcutEnabled(self,id,enable=None):
		"""
		setShortcutEnabled(id,enable=None)
			id=QT.int
			enable=QT.bool

		If enable is true, the shortcut with the given id is enabled; otherwise the shortcut is disabled.
		"""
		res = super(Standard_QWidget,self).setShortcutEnabled(id,enable)
		return res
	#----------------------------------------------------------------------
	def setSizeIncrement(self,*args,**kwargs):
		"""
		setSizeIncrement(w,h)
			w=QT.int
			h=QT.int

		setSizeIncrement(arg__1)
			arg__1=QT.QSize

		This is an overloaded function.
		Sets the x (width) size increment to w and the y (height) size increment to h .
		"""
		res = super(Standard_QWidget,self).setSizeIncrement(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setSizePolicy(self,*args,**kwargs):
		"""
		setSizePolicy(arg__1)
			arg__1=QT.QSizePolicy

		setSizePolicy(horizontal,vertical)
			horizontal=QT.QSizePolicy.Policy
			vertical=QT.QSizePolicy.Policy

		This property holds the default layout behavior of the widget.
		If there is a PySide.QT.QLayout that manages this widgets children, the size policy specified by that layout is used
		If there is no such PySide.QT.QLayout , the result of this function is used.
		The default policy is Preferred/Preferred, which means that the widget can be freely resized, but prefers to be the size PySide.QT.QWidget.sizeHint() returns
		Button-like widgets set the size policy to specify that they may stretch horizontally, but are fixed vertically
		The same applies to lineedit controls (such as PySide.QT.QLineEdit , PySide.QT.QSpinBox or an editable PySide.QT.QComboBox ) and other horizontally orientated widgets (such as PySide.QT.QProgressBar )
		PySide.QT.QToolButton s are normally square, so they allow growth in both directions
		Widgets that support different directions (such as PySide.QT.QSlider , PySide.QT.QScrollBar or QHeader ) specify stretching in the respective direction only
		Widgets that can provide scroll bars (usually subclasses of PySide.QT.QScrollArea ) tend to specify that they can use additional space, and that they can make do with less than PySide.QT.QWidget.sizeHint() .
		"""
		res = super(Standard_QWidget,self).setSizePolicy(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setStatusTip(self,arg__1):
		"""
		setStatusTip(arg__1)
			arg__1=unicode

		This property holds the widgets status tip.
		By default, this property contains an empty string.
		"""
		res = super(Standard_QWidget,self).setStatusTip(arg__1)
		return res
	#----------------------------------------------------------------------
	def setStyle(self,arg__1):
		"""
		setStyle(arg__1)
			arg__1=QT.QStyle

		Sets the widgets GUI style to style
		The ownership of the style object is not transferred.
		If no style is set, the widget uses the applications style, QApplication.style() instead.
		Setting a widgets style has no effect on existing or future child widgets.
		"""
		res = super(Standard_QWidget,self).setStyle(arg__1)
		return res
	#----------------------------------------------------------------------
	def setToolTip(self,arg__1):
		"""
		setToolTip(arg__1)
			arg__1=unicode

		This property holds the widgets tooltip.
		Note that by default tooltips are only shown for widgets that are children of the active window
		You can change this behavior by setting the attribute Qt.WA_AlwaysShowToolTips on the window , not on the widget with the tooltip.
		If you want to control a tooltips behavior, you can intercept the PySide.QT.QWidget.event() function and catch the QEvent.ToolTip event (e.g., if you want to customize the area for which the tooltip should be shown).
		By default, this property contains an empty string.
		"""
		res = super(Standard_QWidget,self).setToolTip(arg__1)
		return res
	#----------------------------------------------------------------------
	def setUpdatesEnabled(self,enable):
		"""
		setUpdatesEnabled(enable)
			enable=QT.bool

		This property holds whether updates are enabled.
		An updates enabled widget receives paint events and has a system background; a disabled widget does not
		This also implies that calling PySide.QT.QWidget.update() and PySide.QT.QWidget.repaint() has no effect if updates are disabled.
		By default, this property is true.
		PySide.QT.QWidget.setUpdatesEnabled() is normally used to disable updates for a short period of time, for instance to avoid screen flicker during large changes
		In Qt, widgets normally do not generate screen flicker, but on X11 the server might erase regions on the screen when widgets get hidden before they can be replaced by other widgets
		Disabling updates solves this.
		Example:
		Disabling a widget implicitly disables all its children
		Enabling a widget enables all child widgets except top-level widgets or those that have been explicitly disabled
		Re-enabling updates implicitly calls PySide.QT.QWidget.update() on the widget.
		"""
		res = super(Standard_QWidget,self).setUpdatesEnabled(enable)
		return res
	#----------------------------------------------------------------------
	def setVisible(self,visible):
		"""
		setVisible(visible)
			visible=QT.bool

		This property holds whether the widget is visible.
		Calling setVisible(true) or PySide.QT.QWidget.show() sets the widget to visible status if all its parent widgets up to the window are visible
		If an ancestor is not visible, the widget wont become visible until all its ancestors are shown
		If its size or position has changed, Qt guarantees that a widget gets move and resize events just before it is shown
		If the widget has not been resized yet, Qt will adjust the widgets size to a useful default using PySide.QT.QWidget.adjustSize() .
		Calling setVisible(false) or PySide.QT.QWidget.hide() hides a widget explicitly
		An explicitly hidden widget will never become visible, even if all its ancestors become visible, unless you show it.
		A widget receives show and hide events when its visibility status changes
		Between a hide and a show event, there is no need to waste CPU cycles preparing or displaying information to the user
		A video application, for example, might simply stop generating new frames.
		A widget that happens to be obscured by other windows on the screen is considered to be visible
		The same applies to iconified windows and windows that exist on another virtual desktop (on platforms that support this concept)
		A widget receives spontaneous show and hide events when its mapping status is changed by the window system, e.g
		a spontaneous hide event when the user minimizes the window, and a spontaneous show event when the window is restored again.
		You almost never have to reimplement the PySide.QT.QWidget.setVisible() function
		If you need to change some settings before a widget is shown, use PySide.QT.QWidget.showEvent() instead
		If you need to do some delayed initialization use the Polish event delivered to the PySide.QT.QWidget.event() function.
		"""
		res = super(Standard_QWidget,self).setVisible(visible)
		return res
	#----------------------------------------------------------------------
	def setWhatsThis(self,arg__1):
		"""
		setWhatsThis(arg__1)
			arg__1=unicode

		This property holds the widgets Whats This help text..
		By default, this property contains an empty string.
		"""
		res = super(Standard_QWidget,self).setWhatsThis(arg__1)
		return res
	#----------------------------------------------------------------------
	def setWindowFilePath(self,filePath):
		"""
		setWindowFilePath(filePath)
			filePath=unicode

		This property holds the file path associated with a widget.
		This property only makes sense for windows
		It associates a file path with a window
		If you set the file path, but have not set the window title, Qt sets the window title to contain a string created using the following components.
		On Mac OS X:
		On Windows and X11:
		If the window title is set at any point, then the window title takes precedence and will be shown instead of the file path string.
		Additionally, on Mac OS X, this has an added benefit that it sets the proxy icon for the window, assuming that the file path exists.
		If no file path is set, this property contains an empty string.
		By default, this property contains an empty string.
		"""
		res = super(Standard_QWidget,self).setWindowFilePath(filePath)
		return res
	#----------------------------------------------------------------------
	def setWindowFlags(self,type):
		"""
		setWindowFlags(type)
			type=QT.Qt.WindowFlags


		"""
		res = super(Standard_QWidget,self).setWindowFlags(type)
		return res
	#----------------------------------------------------------------------
	def setWindowIcon(self,icon):
		"""
		setWindowIcon(icon)
			icon=QT.QIcon

		This property holds the widgets icon.
		This property only makes sense for windows
		If no icon has been set, PySide.QT.QWidget.windowIcon() returns the application icon ( QApplication.windowIcon() ).
		"""
		res = super(Standard_QWidget,self).setWindowIcon(icon)
		return res
	#----------------------------------------------------------------------
	def setWindowIconText(self,arg__1):
		"""
		setWindowIconText(arg__1)
			arg__1=unicode

		This property holds the widgets icon text.
		This property only makes sense for windows
		If no icon text has been set, this functions returns an empty string.
		"""
		res = super(Standard_QWidget,self).setWindowIconText(arg__1)
		return res
	#----------------------------------------------------------------------
	def setWindowModality(self,windowModality):
		"""
		setWindowModality(windowModality)
			windowModality=QT.Qt.WindowModality

		This property holds which windows are blocked by the modal widget.
		This property only makes sense for windows
		A modal widget prevents widgets in other windows from getting input
		The value of this property controls which windows are blocked when the widget is visible
		Changing this property while the window is visible has no effect; you must PySide.QT.QWidget.hide() the widget first, then PySide.QT.QWidget.show() it again.
		By default, this property is Qt.NonModal .
		"""
		res = super(Standard_QWidget,self).setWindowModality(windowModality)
		return res
	#----------------------------------------------------------------------
	def setWindowOpacity(self,level):
		"""
		setWindowOpacity(level)
			level=QT.qreal


		"""
		res = super(Standard_QWidget,self).setWindowOpacity(level)
		return res
	#----------------------------------------------------------------------
	def setWindowRole(self,arg__1):
		"""
		setWindowRole(arg__1)
			arg__1=unicode

		Sets the windows role to role
		This only makes sense for windows on X11.
		"""
		res = super(Standard_QWidget,self).setWindowRole(arg__1)
		return res
	#----------------------------------------------------------------------
	def setWindowState(self,state):
		"""
		setWindowState(state)
			state=QT.Qt.WindowStates


		"""
		res = super(Standard_QWidget,self).setWindowState(state)
		return res
	#----------------------------------------------------------------------
	def showEvent(self,event):
		"""
		showEvent(event)
			event=QT.QShowEvent

		This event handler can be reimplemented in a subclass to receive widget show events which are passed in the event parameter.
		Non-spontaneous show events are sent to widgets immediately before they are shown
		The spontaneous show events of windows are delivered afterwards.
		Note: A widget receives spontaneous show and hide events when its mapping status is changed by the window system, e.g
		a spontaneous hide event when the user minimizes the window, and a spontaneous show event when the window is restored again
		After receiving a spontaneous hide event, a widget is still considered visible in the sense of PySide.QT.QWidget.isVisible() .
		"""
		res = super(Standard_QWidget,self).showEvent(event)
		return res
	#----------------------------------------------------------------------
	def stackUnder(self,arg__1):
		"""
		stackUnder(arg__1)
			arg__1=QT.QWidget

		Places the widget under w in the parent widgets stack.
		To make this work, the widget itself and w must be siblings.
		"""
		res = super(Standard_QWidget,self).stackUnder(arg__1)
		return res
	#----------------------------------------------------------------------
	def tabletEvent(self,event):
		"""
		tabletEvent(event)
			event=QT.QTabletEvent

		This event handler, for event event , can be reimplemented in a subclass to receive tablet events for the widget.
		If you reimplement this handler, it is very important that you ignore() the event if you do not handle it, so that the widgets parent can interpret it.
		The default implementation ignores the event.
		"""
		res = super(Standard_QWidget,self).tabletEvent(event)
		return res
	#----------------------------------------------------------------------
	def testAttribute(self,arg__1):
		"""
		testAttribute(arg__1)
			arg__1=QT.Qt.WidgetAttribute


		"""
		res = super(Standard_QWidget,self).testAttribute(arg__1)

		return res
	#----------------------------------------------------------------------
	def testAttribute_helper(self,arg__1):
		"""
		testAttribute_helper(arg__1)
			arg__1=QT.Qt.WidgetAttribute


		"""
		res = super(Standard_QWidget,self).testAttribute_helper(arg__1)

		return res
	#----------------------------------------------------------------------
	def ungrabGesture(self,type):
		"""
		ungrabGesture(type)
			type=QT.Qt.GestureType


		"""
		res = super(Standard_QWidget,self).ungrabGesture(type)
		return res
	#----------------------------------------------------------------------
	def update(self,*args,**kwargs):
		"""
		update(x,y,w,h)
			x=QT.int
			y=QT.int
			w=QT.int
			h=QT.int

		update(arg__1)
			arg__1=QT.QRegion

		update(arg__1)
			arg__1=QT.QRect

		This is an overloaded function.
		This version updates a rectangle (x , y , w , h ) inside the widget.
		"""
		res = super(Standard_QWidget,self).update(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def wheelEvent(self,event):
		"""
		wheelEvent(event)
			event=QT.QWheelEvent

		This event handler, for event event , can be reimplemented in a subclass to receive wheel events for the widget.
		If you reimplement this handler, it is very important that you ignore() the event if you do not handle it, so that the widgets parent can interpret it.
		The default implementation ignores the event.
		"""
		res = super(Standard_QWidget,self).wheelEvent(event)
		return res

	AcceptDrops           = property(acceptDrops)
	AccessibleDescription = property(accessibleDescription)
	AccessibleName        = property(accessibleName)
	Actions               = property(actions)
	ActivateWindow        = property(activateWindow)
	AdjustSize            = property(adjustSize)
	AutoFillBackground    = property(autoFillBackground)
	BackgroundRole        = property(backgroundRole)
	BaseSize              = property(baseSize)
	ChildrenRect          = property(childrenRect)
	ChildrenRegion        = property(childrenRegion)
	ClearFocus            = property(clearFocus)
	ClearMask             = property(clearMask)
	ContentsMargins       = property(contentsMargins)
	ContentsRect          = property(contentsRect)
	ContextMenuPolicy     = property(contextMenuPolicy)
	CreateWinId           = property(createWinId)
	Cursor                = property(cursor)
	EffectiveWinId        = property(effectiveWinId)
	EnsurePolished        = property(ensurePolished)
	FocusNextChild        = property(focusNextChild)
	FocusPolicy           = property(focusPolicy)
	FocusPreviousChild    = property(focusPreviousChild)
	FocusProxy            = property(focusProxy)
	FocusWidget           = property(focusWidget)
	Font                  = property(font)
	FontInfo              = property(fontInfo)
	FontMetrics           = property(fontMetrics)
	ForegroundRole        = property(foregroundRole)
	FrameGeometry         = property(frameGeometry)
	FrameSize             = property(frameSize)
	Geometry              = property(geometry)
	GetContentsMargins    = property(getContentsMargins)
	GrabKeyboard          = property(grabKeyboard)
	GrabMouse             = property(grabMouse)
	GraphicsEffect        = property(graphicsEffect)
	GraphicsProxyWidget   = property(graphicsProxyWidget)
	HasFocus              = property(hasFocus)
	HasMouseTracking      = property(hasMouseTracking)
	InputContext          = property(inputContext)
	InputMethodHints      = property(inputMethodHints)
	IsActiveWindow        = property(isActiveWindow)
	IsEnabled             = property(isEnabled)
	IsFullScreen          = property(isFullScreen)
	IsHidden              = property(isHidden)
	IsLeftToRight         = property(isLeftToRight)
	IsMaximized           = property(isMaximized)
	IsMinimized           = property(isMinimized)
	IsModal               = property(isModal)
	IsRightToLeft         = property(isRightToLeft)
	IsVisible             = property(isVisible)
	IsWindow              = property(isWindow)
	IsWindowModified      = property(isWindowModified)
	LanguageChange        = property(languageChange)
	Layout                = property(layout)
	LayoutDirection       = property(layoutDirection)
	Locale                = property(locale)
	Mask                  = property(mask)
	MaximumHeight         = property(maximumHeight)
	MaximumSize           = property(maximumSize)
	MaximumWidth          = property(maximumWidth)
	MinimumHeight         = property(minimumHeight)
	MinimumSize           = property(minimumSize)
	MinimumSizeHint       = property(minimumSizeHint)
	MinimumWidth          = property(minimumWidth)
	NativeParentWidget    = property(nativeParentWidget)
	NextInFocusChain      = property(nextInFocusChain)
	NormalGeometry        = property(normalGeometry)
	Palette               = property(palette)
	ParentWidget          = property(parentWidget)
	Pos                   = property(pos)
	PreviousInFocusChain  = property(previousInFocusChain)
	Rect                  = property(rect)
	ReleaseKeyboard       = property(releaseKeyboard)
	ReleaseMouse          = property(releaseMouse)
	ResetInputContext     = property(resetInputContext)
	SaveGeometry          = property(saveGeometry)
	Size                  = property(size)
	SizeHint              = property(sizeHint)
	SizeIncrement         = property(sizeIncrement)
	SizePolicy            = property(sizePolicy)
	StatusTip             = property(statusTip)
	Style                 = property(style)
	StyleSheet            = property(styleSheet)
	TakeLayout            = property(takeLayout)
	ToolTip               = property(toolTip)
	UnderMouse            = property(underMouse)
	UnsetCursor           = property(unsetCursor)
	UnsetLayoutDirection  = property(unsetLayoutDirection)
	UnsetLocale           = property(unsetLocale)
	UpdateGeometry        = property(updateGeometry)
	UpdatesEnabled        = property(updatesEnabled)
	VisibleRegion         = property(visibleRegion)
	WhatsThis             = property(whatsThis)
	WinId                 = property(winId)
	Window                = property(window)
	WindowFilePath        = property(windowFilePath)
	WindowFlags           = property(windowFlags)
	WindowIcon            = property(windowIcon)
	WindowIconText        = property(windowIconText)
	WindowModality        = property(windowModality)
	WindowOpacity         = property(windowOpacity)
	WindowRole            = property(windowRole)
	WindowState           = property(windowState)
	WindowTitle           = property(windowTitle)
	WindowType            = property(windowType)
	X                     = property(x)
	X11Info               = property(x11Info)
	X11PictureHandle      = property(x11PictureHandle)
	Y                     = property(y)