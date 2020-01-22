from . import Qt,QAbstractItemView,QStyle,QFileDialog,QFont
#import QT

# ########################################################################
# class AnchorAttribute:
	# AnchorName = Qt.AnchorName
	# AnchorHref = Qt.AnchorHref
########################################################################
class AnchorPoint:
	AnchorBottom                      = Qt.AnchorBottom
	AnchorRight                       = Qt.AnchorRight
	AnchorLeft                        = Qt.AnchorLeft
	AnchorHorizontalCenter            = Qt.AnchorHorizontalCenter
	AnchorTop                         = Qt.AnchorTop
	AnchorVerticalCenter              = Qt.AnchorVerticalCenter
########################################################################
class ApplicationAttribute:
	AA_DontShowIconsInMenus           = Qt.AA_DontShowIconsInMenus
	AA_DontUseNativeMenuBar           = Qt.AA_DontUseNativeMenuBar
	AA_NativeWindows                  = Qt.AA_NativeWindows
	AA_ImmediateWidgetCreation        = Qt.AA_ImmediateWidgetCreation
	AA_MSWindowsUseDirect3DByDefault  = Qt.AA_MSWindowsUseDirect3DByDefault
	# AA_S60DontConstructApplicationPanes = Qt.AA_DontConstructApplicationPanes
	AA_DontCreateNativeWidgetSiblings = Qt.AA_DontCreateNativeWidgetSiblings
	AA_MacDontSwapCtrlAndMeta         = Qt.AA_MacDontSwapCtrlAndMeta
	AA_MacPluginApplication           = Qt.AA_MacPluginApplication
########################################################################
class ArrowType:
	RightArrow                        = Qt.RightArrow
	NoArrow                           = Qt.NoArrow
	UpArrow                           = Qt.UpArrow
	DownArrow                         = Qt.DownArrow
	LeftArrow                         = Qt.LeftArrow
########################################################################
class AspectRatioMode:
	IgnoreAspectRatio                 = Qt.IgnoreAspectRatio
	KeepAspectRatio                   = Qt.KeepAspectRatio
	KeepAspectRatioByExpanding        = Qt.KeepAspectRatioByExpanding
########################################################################
class Axis:
	ZAxis                             = Qt.ZAxis
	XAxis                             = Qt.XAxis
	YAxis                             = Qt.YAxis
########################################################################
class BGMode:
	TransparentMode                   = Qt.TransparentMode
	OpaqueMode                        = Qt.OpaqueMode
########################################################################
class CaseSensitivity:
	CaseSensitive                     = Qt.CaseSensitive
	CaseInsensitive                   = Qt.CaseInsensitive
########################################################################
class ClipOperation:
	# UniteClip     = Qt.UniteClip
	ReplaceClip                       = Qt.ReplaceClip
	IntersectClip                     = Qt.IntersectClip
	NoClip                            = Qt.NoClip
########################################################################
class ConnectionType:
	UniqueConnection                  = Qt.UniqueConnection
	AutoConnection                    = Qt.AutoConnection
	BlockingQueuedConnection          = Qt.BlockingQueuedConnection
	QueuedConnection                  = Qt.QueuedConnection
	# AutoCompatConnection     = Qt.AutoCompatConnection
	DirectConnection                  = Qt.DirectConnection
########################################################################
class ContextMenuPolicy:
	DefaultContextMenu                = Qt.DefaultContextMenu
	PreventContextMenu                = Qt.PreventContextMenu
	ActionsContextMenu                = Qt.ActionsContextMenu
	NoContextMenu                     = Qt.NoContextMenu
	CustomContextMenu                 = Qt.CustomContextMenu
########################################################################
class CoordinateSystem:
	LogicalCoordinates                = Qt.LogicalCoordinates
	DeviceCoordinates                 = Qt.DeviceCoordinates
########################################################################
class Corner:
	TopRightCorner                    = Qt.TopRightCorner
	BottomRightCorner                 = Qt.BottomRightCorner
	TopLeftCorner                     = Qt.TopLeftCorner
	BottomLeftCorner                  = Qt.BottomLeftCorner
########################################################################
class CursorShape:
	DragCopyCursor                    = Qt.DragCopyCursor
	CrossCursor                       = Qt.CrossCursor
	SizeFDiagCursor                   = Qt.SizeFDiagCursor
	SizeAllCursor                     = Qt.SizeAllCursor
	SizeHorCursor                     = Qt.SizeHorCursor
	UpArrowCursor                     = Qt.UpArrowCursor
	CustomCursor                      = Qt.CustomCursor
	LastCursor                        = Qt.LastCursor
	BusyCursor                        = Qt.BusyCursor
	OpenHandCursor                    = Qt.OpenHandCursor
	SizeVerCursor                     = Qt.SizeVerCursor
	WhatsThisCursor                   = Qt.WhatsThisCursor
	BitmapCursor                      = Qt.BitmapCursor
	DragMoveCursor                    = Qt.DragMoveCursor
	DragLinkCursor                    = Qt.DragLinkCursor
	IBeamCursor                       = Qt.IBeamCursor
	ArrowCursor                       = Qt.ArrowCursor
	SplitVCursor                      = Qt.SplitVCursor
	WaitCursor                        = Qt.WaitCursor
	BlankCursor                       = Qt.BlankCursor
	PointingHandCursor                = Qt.PointingHandCursor
	ForbiddenCursor                   = Qt.ForbiddenCursor
	SizeBDiagCursor                   = Qt.SizeBDiagCursor
	SplitHCursor                      = Qt.SplitHCursor
	ClosedHandCursor                  = Qt.ClosedHandCursor
########################################################################
class DateFormat:
	DefaultLocaleLongDate             = Qt.DefaultLocaleLongDate
	TextDate                          = Qt.TextDate
	LocaleDate                        = Qt.LocaleDate
	ISODate                           = Qt.ISODate
	DefaultLocaleShortDate            = Qt.DefaultLocaleShortDate
	SystemLocaleShortDate             = Qt.SystemLocaleShortDate
	LocalDate                         = Qt.LocalDate
	SystemLocaleDate                  = Qt.SystemLocaleDate
	SystemLocaleLongDate              = Qt.SystemLocaleLongDate
########################################################################
class DockWidgetArea:
	AllDockWidgetAreas                = Qt.AllDockWidgetAreas
	LeftDockWidgetArea                = Qt.LeftDockWidgetArea
	DockWidgetArea_Mask               = Qt.DockWidgetArea_Mask
	NoDockWidgetArea                  = Qt.NoDockWidgetArea
	TopDockWidgetArea                 = Qt.TopDockWidgetArea
	RightDockWidgetArea               = Qt.RightDockWidgetArea
	BottomDockWidgetArea              = Qt.BottomDockWidgetArea
########################################################################
class DropAction:
	LinkAction                        = Qt.LinkAction
	CopyAction                        = Qt.CopyAction
	IgnoreAction                      = Qt.IgnoreAction
	TargetMoveAction                  = Qt.TargetMoveAction
	MoveAction                        = Qt.MoveAction
	ActionMask                        = Qt.ActionMask
########################################################################
class EventPriority:
	NormalEventPriority               = Qt.NormalEventPriority
	HighEventPriority                 = Qt.HighEventPriority
	LowEventPriority                  = Qt.LowEventPriority
########################################################################
class FillRule:
	WindingFill                       = Qt.WindingFill
	OddEvenFill                       = Qt.OddEvenFill
########################################################################
class FocusPolicy:
	StrongFocus                       = Qt.StrongFocus
	WheelFocus                        = Qt.WheelFocus
	ClickFocus                        = Qt.ClickFocus
	TabFocus                          = Qt.TabFocus
	NoFocus                           = Qt.NoFocus
########################################################################
class FocusReason:
	NoFocusReason                     = Qt.NoFocusReason
	BacktabFocusReason                = Qt.BacktabFocusReason
	ShortcutFocusReason               = Qt.ShortcutFocusReason
	PopupFocusReason                  = Qt.PopupFocusReason
	MouseFocusReason                  = Qt.MouseFocusReason
	ActiveWindowFocusReason           = Qt.ActiveWindowFocusReason
	MenuBarFocusReason                = Qt.MenuBarFocusReason
	TabFocusReason                    = Qt.TabFocusReason
	OtherFocusReason                  = Qt.OtherFocusReason
########################################################################
class GestureFlag:
	DontStartGestureOnChildren        = Qt.DontStartGestureOnChildren
	ReceivePartialGestures            = Qt.ReceivePartialGestures
	IgnoredGesturesPropagateToParent  = Qt.IgnoredGesturesPropagateToParent
########################################################################
class GestureState:
	GestureUpdated                    = Qt.GestureUpdated
	GestureFinished                   = Qt.GestureFinished
	GestureCanceled                   = Qt.GestureCanceled
	GestureStarted                    = Qt.GestureStarted
########################################################################
class GestureType:
	SwipeGesture                      = Qt.SwipeGesture
	CustomGesture                     = Qt.CustomGesture
	PinchGesture                      = Qt.PinchGesture
	TapAndHoldGesture                 = Qt.TapAndHoldGesture
	TapGesture                        = Qt.TapGesture
	PanGesture                        = Qt.PanGesture
########################################################################
class GlobalColor:
	lightGray                         = Qt.lightGray
	gray                              = Qt.gray
	darkGreen                         = Qt.darkGreen
	darkMagenta                       = Qt.darkMagenta
	darkCyan                          = Qt.darkCyan
	darkBlue                          = Qt.darkBlue
	darkGray                          = Qt.darkGray
	blue                              = Qt.blue
	yellow                            = Qt.yellow
	darkYellow                        = Qt.darkYellow
	color1                            = Qt.color1
	color0                            = Qt.color0
	transparent                       = Qt.transparent
	black                             = Qt.black
	darkRed                           = Qt.darkRed
	cyan                              = Qt.cyan
	green                             = Qt.green
	white                             = Qt.white
	magenta                           = Qt.magenta
	red                               = Qt.red
########################################################################
class HitTestAccuracy:
	FuzzyHit                          = Qt.FuzzyHit
	ExactHit                          = Qt.ExactHit
########################################################################
class ImageConversionFlag:
	AvoidDither                       = Qt.AvoidDither
	AutoColor                         = Qt.AutoColor
	OrderedDither                     = Qt.OrderedDither
	PreferDither                      = Qt.PreferDither
	OrderedAlphaDither                = Qt.OrderedAlphaDither
	ThresholdAlphaDither              = Qt.ThresholdAlphaDither
	DiffuseAlphaDither                = Qt.DiffuseAlphaDither
	DiffuseDither                     = Qt.DiffuseDither
	AutoDither                        = Qt.AutoDither
	ColorOnly                         = Qt.ColorOnly
	MonoOnly                          = Qt.MonoOnly
	ThresholdDither                   = Qt.ThresholdDither
########################################################################
class InputMethodHint:
	ImhPreferNumbers                  = Qt.ImhPreferNumbers
	ImhDialableCharactersOnly         = Qt.ImhDialableCharactersOnly
	ImhNoAutoUppercase                = Qt.ImhNoAutoUppercase
	ImhLowercaseOnly                  = Qt.ImhLowercaseOnly
	ImhEmailCharactersOnly            = Qt.ImhEmailCharactersOnly
	ImhNoPredictiveText               = Qt.ImhNoPredictiveText
	ImhUrlCharactersOnly              = Qt.ImhUrlCharactersOnly
	ImhUppercaseOnly                  = Qt.ImhUppercaseOnly
	ImhPreferUppercase                = Qt.ImhPreferUppercase
	ImhDigitsOnly                     = Qt.ImhDigitsOnly
	ImhFormattedNumbersOnly           = Qt.ImhFormattedNumbersOnly
	ImhPreferLowercase                = Qt.ImhPreferLowercase
	ImhHiddenText                     = Qt.ImhHiddenText
	ImhNone                           = Qt.ImhNone
	ImhExclusiveInputMask             = Qt.ImhExclusiveInputMask
########################################################################
class InputMethodQuery:
	ImCursorPosition                  = Qt.ImCursorPosition
	ImFont                            = Qt.ImFont
	ImAnchorPosition                  = Qt.ImAnchorPosition
	ImMicroFocus                      = Qt.ImMicroFocus
	ImMaximumTextLength               = Qt.ImMaximumTextLength
	ImSurroundingText                 = Qt.ImSurroundingText
	ImCurrentSelection                = Qt.ImCurrentSelection
########################################################################
class ItemSelectionMode:
	ContainsItemBoundingRect          = Qt.ContainsItemBoundingRect
	IntersectsItemBoundingRect        = Qt.IntersectsItemBoundingRect
	ContainsItemShape                 = Qt.ContainsItemShape
	IntersectsItemShape               = Qt.IntersectsItemShape
########################################################################
class Key:
	Excel                             = Qt.Key_Excel
	hyphen                            = Qt.Key_hyphen
	Space                             = Qt.Key_Space
	Pause                             = Qt.Key_Pause
	F27                               = Qt.Key_F27
	F26                               = Qt.Key_F26
	F25                               = Qt.Key_F25
	F24                               = Qt.Key_F24
	F23                               = Qt.Key_F23
	F22                               = Qt.Key_F22
	F21                               = Qt.Key_F21
	F20                               = Qt.Key_F20
	DOS                               = Qt.Key_DOS
	F29                               = Qt.Key_F29
	F28                               = Qt.Key_F28
	OpenUrl                           = Qt.Key_OpenUrl
	Launch8                           = Qt.Key_Launch8
	Launch9                           = Qt.Key_Launch9
	Dead_Belowdot                     = Qt.Key_Dead_Belowdot
	onequarter                        = Qt.Key_onequarter
	HomePage                          = Qt.Key_HomePage
	Launch1                           = Qt.Key_Launch1
	Launch2                           = Qt.Key_Launch2
	Launch3                           = Qt.Key_Launch3
	Launch4                           = Qt.Key_Launch4
	Launch5                           = Qt.Key_Launch5
	Launch6                           = Qt.Key_Launch6
	Launch7                           = Qt.Key_Launch7
	LaunchH                           = Qt.Key_LaunchH
	Ediaeresis                        = Qt.Key_Ediaeresis
	Shift                             = Qt.Key_Shift
	LaunchA                           = Qt.Key_LaunchA
	LaunchB                           = Qt.Key_LaunchB
	LaunchC                           = Qt.Key_LaunchC
	LaunchD                           = Qt.Key_LaunchD
	LaunchE                           = Qt.Key_LaunchE
	LaunchF                           = Qt.Key_LaunchF
	LaunchG                           = Qt.Key_LaunchG
	Left                              = Qt.Key_Left
	Dead_Caron                        = Qt.Key_Dead_Caron
	Hangul_Special                    = Qt.Key_Hangul_Special
	Hangul_Jamo                       = Qt.Key_Hangul_Jamo
	Period                            = Qt.Key_Period
	Dead_Voiced_Sound                 = Qt.Key_Dead_Voiced_Sound
	Ooblique                          = Qt.Key_Ooblique
	OfficeHome                        = Qt.Key_OfficeHome
	Colon                             = Qt.Key_Colon
	Forward                           = Qt.Key_Forward
	UWB                               = Qt.Key_UWB
	Katakana                          = Qt.Key_Katakana
	Eisu_toggle                       = Qt.Key_Eisu_toggle
	Zoom                              = Qt.Key_Zoom
	Zenkaku                           = Qt.Key_Zenkaku
	Save                              = Qt.Key_Save
	Greater                           = Qt.Key_Greater
	WebCam                            = Qt.Key_WebCam
	VolumeMute                        = Qt.Key_VolumeMute
	ParenRight                        = Qt.Key_ParenRight
	MenuKB                            = Qt.Key_MenuKB
	Video                             = Qt.Key_Video
	Oacute                            = Qt.Key_Oacute
	NumLock                           = Qt.Key_NumLock
	Multi_key                         = Qt.Key_Multi_key
	Ugrave                            = Qt.Key_Ugrave
	Ccedilla                          = Qt.Key_Ccedilla
	Dead_Horn                         = Qt.Key_Dead_Horn
	Hangul_Hanja                      = Qt.Key_Hangul_Hanja
	Call                              = Qt.Key_Call
	AudioForward                      = Qt.Key_AudioForward
	macron                            = Qt.Key_macron
	section                           = Qt.Key_section
	Away                              = Qt.Key_Away
	MenuPB                            = Qt.Key_MenuPB
	Hangul_Jeonja                     = Qt.Key_Hangul_Jeonja
	Equal                             = Qt.Key_Equal
	Standby                           = Qt.Key_Standby
	TrebleDown                        = Qt.Key_TrebleDown
	Launch0                           = Qt.Key_Launch0
	Hankaku                           = Qt.Key_Hankaku
	Enter                             = Qt.Key_Enter
	Dead_Semivoiced_Sound             = Qt.Key_Dead_Semivoiced_Sound
	Dead_Tilde                        = Qt.Key_Dead_Tilde
	ScreenSaver                       = Qt.Key_ScreenSaver
	Less                              = Qt.Key_Less
	Game                              = Qt.Key_Game
	Alt                               = Qt.Key_Alt
	yen                               = Qt.Key_yen
	NumberSign                        = Qt.Key_NumberSign
	AudioRewind                       = Qt.Key_AudioRewind
	Hangul_Banja                      = Qt.Key_Hangul_Banja
	Printer                           = Qt.Key_Printer
	twosuperior                       = Qt.Key_twosuperior
	Favorites                         = Qt.Key_Favorites
	Exclam                            = Qt.Key_Exclam
	Xfer                              = Qt.Key_Xfer
	AltGr                             = Qt.Key_AltGr
	Kana_Lock                         = Qt.Key_Kana_Lock
	Insert                            = Qt.Key_Insert
	guillemotright                    = Qt.Key_guillemotright
	Subtitle                          = Qt.Key_Subtitle
	KeyboardBrightnessUp              = Qt.Key_KeyboardBrightnessUp
	Market                            = Qt.Key_Market
	MediaPause                        = Qt.Key_MediaPause
	Suspend                           = Qt.Key_Suspend
	VolumeDown                        = Qt.Key_VolumeDown
	Send                              = Qt.Key_Send
	ScrollLock                        = Qt.Key_ScrollLock
	Travel                            = Qt.Key_Travel
	BassDown                          = Qt.Key_BassDown
	ApplicationLeft                   = Qt.Key_ApplicationLeft
	BassBoost                         = Qt.Key_BassBoost
	Hiragana                          = Qt.Key_Hiragana
	TaskPane                          = Qt.Key_TaskPane
	MediaTogglePlayPause              = Qt.Key_MediaTogglePlayPause
	LastNumberRedial                  = Qt.Key_LastNumberRedial
	Muhenkan                          = Qt.Key_Muhenkan
	Option                            = Qt.Key_Option
	masculine                         = Qt.Key_masculine
	H                                 = Qt.Key_H
	Phone                             = Qt.Key_Phone
	AE                                = Qt.Key_AE
	Refresh                           = Qt.Key_Refresh
	MailForward                       = Qt.Key_MailForward
	Super_R                           = Qt.Key_Super_R
	F34                               = Qt.Key_F34
	F35                               = Qt.Key_F35
	F30                               = Qt.Key_F30
	F31                               = Qt.Key_F31
	F32                               = Qt.Key_F32
	F33                               = Qt.Key_F33
	Super_L                           = Qt.Key_Super_L
	Dollar                            = Qt.Key_Dollar
	ApplicationRight                  = Qt.Key_ApplicationRight
	Backslash                         = Qt.Key_Backslash
	Community                         = Qt.Key_Community
	At                                = Qt.Key_At
	Comma                             = Qt.Key_Comma
	notsign                           = Qt.Key_notsign
	LightBulb                         = Qt.Key_LightBulb
	questiondown                      = Qt.Key_questiondown
	QuoteLeft                         = Qt.Key_QuoteLeft
	Hangul_PreHanja                   = Qt.Key_Hangul_PreHanja
	Hangul_Romaja                     = Qt.Key_Hangul_Romaja
	Calculator                        = Qt.Key_Calculator
	ClearGrab                         = Qt.Key_ClearGrab
	Eisu_Shift                        = Qt.Key_Eisu_Shift
	cent                              = Qt.Key_cent
	Messenger                         = Qt.Key_Messenger
	Paste                             = Qt.Key_Paste
	BraceRight                        = Qt.Key_BraceRight
	Stop                              = Qt.Key_Stop
	Sleep                             = Qt.Key_Sleep
	KeyboardLightOnOff                = Qt.Key_KeyboardLightOnOff
	VolumeUp                          = Qt.Key_VolumeUp
	Ograve                            = Qt.Key_Ograve
	Hangul_Start                      = Qt.Key_Hangul_Start
	Codeinput                         = Qt.Key_Codeinput
	Yes                               = Qt.Key_Yes
	LaunchMedia                       = Qt.Key_LaunchMedia
	exclamdown                        = Qt.Key_exclamdown
	plusminus                         = Qt.Key_plusminus
	Question                          = Qt.Key_Question
	Context4                          = Qt.Key_Context4
	Context3                          = Qt.Key_Context3
	Context2                          = Qt.Key_Context2
	Context1                          = Qt.Key_Context1
	AsciiTilde                        = Qt.Key_AsciiTilde
	BrightnessAdjust                  = Qt.Key_BrightnessAdjust
	SingleCandidate                   = Qt.Key_SingleCandidate
	Dead_Abovering                    = Qt.Key_Dead_Abovering
	Finance                           = Qt.Key_Finance
	Underscore                        = Qt.Key_Underscore
	KeyboardBrightnessDown            = Qt.Key_KeyboardBrightnessDown
	Dead_Breve                        = Qt.Key_Dead_Breve
	Kanji                             = Qt.Key_Kanji
	sterling                          = Qt.Key_sterling
	Eject                             = Qt.Key_Eject
	Copy                              = Qt.Key_Copy
	Display                           = Qt.Key_Display
	WWW                               = Qt.Key_WWW
	HotLinks                          = Qt.Key_HotLinks
	Agrave                            = Qt.Key_Agrave
	Cut                               = Qt.Key_Cut
	Idiaeresis                        = Qt.Key_Idiaeresis
	acute                             = Qt.Key_acute
	CameraFocus                       = Qt.Key_CameraFocus
	Dead_Macron                       = Qt.Key_Dead_Macron
	RotationPB                        = Qt.Key_RotationPB
	Hibernate                         = Qt.Key_Hibernate
	Return                            = Qt.Key_Return
	Select                            = Qt.Key_Select
	Dead_Diaeresis                    = Qt.Key_Dead_Diaeresis
	PowerDown                         = Qt.Key_PowerDown
	BracketLeft                       = Qt.Key_BracketLeft
	Minus                             = Qt.Key_Minus
	Apostrophe                        = Qt.Key_Apostrophe
	Adiaeresis                        = Qt.Key_Adiaeresis
	Shop                              = Qt.Key_Shop
	WakeUp                            = Qt.Key_WakeUp
	LaunchMail                        = Qt.Key_LaunchMail
	End                               = Qt.Key_End
	Otilde                            = Qt.Key_Otilde
	TrebleUp                          = Qt.Key_TrebleUp
	Pictures                          = Qt.Key_Pictures
	BassUp                            = Qt.Key_BassUp
	Ntilde                            = Qt.Key_Ntilde
	Uacute                            = Qt.Key_Uacute
	Zenkaku_Hankaku                   = Qt.Key_Zenkaku_Hankaku
	Play                              = Qt.Key_Play
	MySites                           = Qt.Key_MySites
	Icircumflex                       = Qt.Key_Icircumflex
	VoiceDial                         = Qt.Key_VoiceDial
	Acircumflex                       = Qt.Key_Acircumflex
	Dead_Grave                        = Qt.Key_Dead_Grave
	Bar                               = Qt.Key_Bar
	Backtab                           = Qt.Key_Backtab
	History                           = Qt.Key_History
	multiply                          = Qt.Key_multiply
	Dead_Acute                        = Qt.Key_Dead_Acute
	AudioRepeat                       = Qt.Key_AudioRepeat
	CapsLock                          = Qt.Key_CapsLock
	Aring                             = Qt.Key_Aring
	PageDown                          = Qt.Key_PageDown
	Calendar                          = Qt.Key_Calendar
	ContrastAdjust                    = Qt.Key_ContrastAdjust
	AudioCycleTrack                   = Qt.Key_AudioCycleTrack
	Meeting                           = Qt.Key_Meeting
	Terminal                          = Qt.Key_Terminal
	threequarters                     = Qt.Key_threequarters
	copyright                         = Qt.Key_copyright
	unknown                           = Qt.Key_unknown
	Asterisk                          = Qt.Key_Asterisk
	iTouch                            = Qt.Key_iTouch
	Eacute                            = Qt.Key_Eacute
	periodcentered                    = Qt.Key_periodcentered
	Camera                            = Qt.Key_Camera
	Flip                              = Qt.Key_Flip
	MediaNext                         = Qt.Key_MediaNext
	Search                            = Qt.Key_Search
	Kana_Shift                        = Qt.Key_Kana_Shift
	Igrave                            = Qt.Key_Igrave
	Battery                           = Qt.Key_Battery
	Henkan                            = Qt.Key_Henkan
	Tools                             = Qt.Key_Tools
	Cancel                            = Qt.Key_Cancel
	Hangul_PostHanja                  = Qt.Key_Hangul_PostHanja
	Any                               = Qt.Key_Any
	Hangul                            = Qt.Key_Hangul
	Ucircumflex                       = Qt.Key_Ucircumflex
	Hangup                            = Qt.Key_Hangup
	ZoomOut                           = Qt.Key_ZoomOut
	AddFavorite                       = Qt.Key_AddFavorite
	Num_5                             = Qt.Key_5
	Num_4                             = Qt.Key_4
	Num_7                             = Qt.Key_7
	Num_6                             = Qt.Key_6
	Num_1                             = Qt.Key_1
	Num_0                             = Qt.Key_0
	Num_3                             = Qt.Key_3
	Num_2                             = Qt.Key_2
	Dead_Iota                         = Qt.Key_Dead_Iota
	Num_9                             = Qt.Key_9
	Num_8                             = Qt.Key_8
	E                                 = Qt.Key_E
	D                                 = Qt.Key_D
	G                                 = Qt.Key_G
	F                                 = Qt.Key_F
	A                                 = Qt.Key_A
	division                          = Qt.Key_division
	C                                 = Qt.Key_C
	B                                 = Qt.Key_B
	M                                 = Qt.Key_M
	L                                 = Qt.Key_L
	O                                 = Qt.Key_O
	N                                 = Qt.Key_N
	I                                 = Qt.Key_I
	Semicolon                         = Qt.Key_Semicolon
	K                                 = Qt.Key_K
	J                                 = Qt.Key_J
	U                                 = Qt.Key_U
	T                                 = Qt.Key_T
	W                                 = Qt.Key_W
	V                                 = Qt.Key_V
	MediaRecord                       = Qt.Key_MediaRecord
	P                                 = Qt.Key_P
	S                                 = Qt.Key_S
	R                                 = Qt.Key_R
	Y                                 = Qt.Key_Y
	X                                 = Qt.Key_X
	Z                                 = Qt.Key_Z
	F4                                = Qt.Key_F4
	F5                                = Qt.Key_F5
	F6                                = Qt.Key_F6
	F7                                = Qt.Key_F7
	F1                                = Qt.Key_F1
	F2                                = Qt.Key_F2
	F3                                = Qt.Key_F3
	F8                                = Qt.Key_F8
	F9                                = Qt.Key_F9
	Odiaeresis                        = Qt.Key_Odiaeresis
	Escape                            = Qt.Key_Escape
	ydiaeresis                        = Qt.Key_ydiaeresis
	Meta                              = Qt.Key_Meta
	Support                           = Qt.Key_Support
	Documents                         = Qt.Key_Documents
	Egrave                            = Qt.Key_Egrave
	nobreakspace                      = Qt.Key_nobreakspace
	PowerOff                          = Qt.Key_PowerOff
	Explorer                          = Qt.Key_Explorer
	RotateWindows                     = Qt.Key_RotateWindows
	MonBrightnessDown                 = Qt.Key_MonBrightnessDown
	degree                            = Qt.Key_degree
	View                              = Qt.Key_View
	BraceLeft                         = Qt.Key_BraceLeft
	Reload                            = Qt.Key_Reload
	threesuperior                     = Qt.Key_threesuperior
	mu                                = Qt.Key_mu
	SysReq                            = Qt.Key_SysReq
	Menu                              = Qt.Key_Menu
	WLAN                              = Qt.Key_WLAN
	Dead_Hook                         = Qt.Key_Dead_Hook
	Slash                             = Qt.Key_Slash
	ParenLeft                         = Qt.Key_ParenLeft
	Iacute                            = Qt.Key_Iacute
	News                              = Qt.Key_News
	LogOff                            = Qt.Key_LogOff
	onehalf                           = Qt.Key_onehalf
	Clear                             = Qt.Key_Clear
	Word                              = Qt.Key_Word
	Udiaeresis                        = Qt.Key_Udiaeresis
	Romaji                            = Qt.Key_Romaji
	Time                              = Qt.Key_Time
	onesuperior                       = Qt.Key_onesuperior
	MediaStop                         = Qt.Key_MediaStop
	Bluetooth                         = Qt.Key_Bluetooth
	Ocircumflex                       = Qt.Key_Ocircumflex
	Right                             = Qt.Key_Right
	paragraph                         = Qt.Key_paragraph
	Down                              = Qt.Key_Down
	Dead_Cedilla                      = Qt.Key_Dead_Cedilla
	QuoteDbl                          = Qt.Key_QuoteDbl
	Backspace                         = Qt.Key_Backspace
	ZoomIn                            = Qt.Key_ZoomIn
	Reply                             = Qt.Key_Reply
	Dead_Ogonek                       = Qt.Key_Dead_Ogonek
	Music                             = Qt.Key_Music
	Yacute                            = Qt.Key_Yacute
	Atilde                            = Qt.Key_Atilde
	ETH                               = Qt.Key_ETH
	Ecircumflex                       = Qt.Key_Ecircumflex
	PageUp                            = Qt.Key_PageUp
	Hiragana_Katakana                 = Qt.Key_Hiragana_Katakana
	CD                                = Qt.Key_CD
	cedilla                           = Qt.Key_cedilla
	Execute                           = Qt.Key_Execute
	F18                               = Qt.Key_F18
	F19                               = Qt.Key_F19
	F16                               = Qt.Key_F16
	F17                               = Qt.Key_F17
	F14                               = Qt.Key_F14
	F15                               = Qt.Key_F15
	F12                               = Qt.Key_F12
	F13                               = Qt.Key_F13
	F10                               = Qt.Key_F10
	F11                               = Qt.Key_F11
	Back                              = Qt.Key_Back
	Memo                              = Qt.Key_Memo
	Control                           = Qt.Key_Control
	No                                = Qt.Key_No
	ordfeminine                       = Qt.Key_ordfeminine
	Ampersand                         = Qt.Key_Ampersand
	currency                          = Qt.Key_currency
	Book                              = Qt.Key_Book
	BracketRight                      = Qt.Key_BracketRight
	MonBrightnessUp                   = Qt.Key_MonBrightnessUp
	Dead_Doubleacute                  = Qt.Key_Dead_Doubleacute
	MultipleCandidate                 = Qt.Key_MultipleCandidate
	TopMenu                           = Qt.Key_TopMenu
	Touroku                           = Qt.Key_Touroku
	Massyo                            = Qt.Key_Massyo
	Up                                = Qt.Key_Up
	MediaLast                         = Qt.Key_MediaLast
	Hangul_End                        = Qt.Key_Hangul_End
	Plus                              = Qt.Key_Plus
	AsciiCircum                       = Qt.Key_AsciiCircum
	MediaPlay                         = Qt.Key_MediaPlay
	Help                              = Qt.Key_Help
	Tab                               = Qt.Key_Tab
	Percent                           = Qt.Key_Percent
	brokenbar                         = Qt.Key_brokenbar
	Direction_R                       = Qt.Key_Direction_R
	Print                             = Qt.Key_Print
	Direction_L                       = Qt.Key_Direction_L
	RotationKB                        = Qt.Key_RotationKB
	Aacute                            = Qt.Key_Aacute
	Spell                             = Qt.Key_Spell
	ToDoList                          = Qt.Key_ToDoList
	SplitScreen                       = Qt.Key_SplitScreen
	diaeresis                         = Qt.Key_diaeresis
	PreviousCandidate                 = Qt.Key_PreviousCandidate
	Home                              = Qt.Key_Home
	Hyper_L                           = Qt.Key_Hyper_L
	Dead_Abovedot                     = Qt.Key_Dead_Abovedot
	THORN                             = Qt.Key_THORN
	BackForward                       = Qt.Key_BackForward
	Delete                            = Qt.Key_Delete
	registered                        = Qt.Key_registered
	Hyper_R                           = Qt.Key_Hyper_R
	Dead_Circumflex                   = Qt.Key_Dead_Circumflex
	MediaPrevious                     = Qt.Key_MediaPrevious
	ToggleCallHangup                  = Qt.Key_ToggleCallHangup
	ssharp                            = Qt.Key_ssharp
	AudioRandomPlay                   = Qt.Key_AudioRandomPlay
	Mode_switch                       = Qt.Key_Mode_switch
	Close                             = Qt.Key_Close
	guillemotleft                     = Qt.Key_guillemotleft
	Q                                 = Qt.Key_Q
	Go                                = Qt.Key_Go
########################################################################
class LayoutDirection:
	RightToLeft                       = Qt.RightToLeft
	LayoutDirectionAuto               = Qt.LayoutDirectionAuto
	LeftToRight                       = Qt.LeftToRight
########################################################################
class MouseButton:
	RightButton                       = Qt.RightButton
	MiddleButton                      = Qt.MiddleButton
	NoButton                          = Qt.NoButton
	LeftButton                        = Qt.LeftButton
	MouseButtonMask                   = Qt.MouseButtonMask
	XButton1                          = Qt.XButton1
	XButton2                          = Qt.XButton2
	MidButton                         = Qt.MidButton
########################################################################
class Orientation:
	Horizontal                        = Qt.Horizontal
	Vertical                          = Qt.Vertical
########################################################################
class PenCapStyle:
	FlatCap                           = Qt.FlatCap
	RoundCap                          = Qt.RoundCap
	SquareCap                         = Qt.SquareCap
	MPenCapStyle                      = Qt.MPenCapStyle
########################################################################
class PenJoinStyle:
	RoundJoin                         = Qt.RoundJoin
	MiterJoin                         = Qt.MiterJoin
	MPenJoinStyle                     = Qt.MPenJoinStyle
	BevelJoin                         = Qt.BevelJoin
	SvgMiterJoin                      = Qt.SvgMiterJoin
########################################################################
class ScrollBarPolicy:
	AsNeeded                          = Qt.ScrollBarAsNeeded
	AlwaysOff                         = Qt.ScrollBarAlwaysOff
	AlwaysOn                          = Qt.ScrollBarAlwaysOn
########################################################################
class SizeHint:
	MinimumDescent                    = Qt.MinimumDescent
	PreferredSize                     = Qt.PreferredSize
	MinimumSize                       = Qt.MinimumSize
	MaximumSize                       = Qt.MaximumSize
########################################################################
class SizeMode:
	AbsoluteSize                      = Qt.AbsoluteSize
	RelativeSize                      = Qt.RelativeSize
########################################################################
class SortOrder:
	Ascending                         = Qt.AscendingOrder
	Descending                        = Qt.DescendingOrder
########################################################################
class TextFormat:
	PlainText                         = Qt.PlainText
	AutoText                          = Qt.AutoText
	# LogText   = Qt.LogText
	RichText                          = Qt.RichText
########################################################################
class TextInteractionFlag:
	TextEditable                      = Qt.TextEditable
	TextSelectableByKeyboard          = Qt.TextSelectableByKeyboard
	NoTextInteraction                 = Qt.NoTextInteraction
	TextSelectableByMouse             = Qt.TextSelectableByMouse
	TextBrowserInteraction            = Qt.TextBrowserInteraction
	LinksAccessibleByKeyboard         = Qt.LinksAccessibleByKeyboard
	LinksAccessibleByMouse            = Qt.LinksAccessibleByMouse
	TextEditorInteraction             = Qt.TextEditorInteraction
########################################################################
class TileRule:
	StretchTile                       = Qt.StretchTile
	RepeatTile                        = Qt.RepeatTile
	RoundTile                         = Qt.RoundTile
########################################################################
class TimeSpec:
	OffsetFromUTC                     = Qt.OffsetFromUTC
	UTC                               = Qt.UTC
	LocalTime                         = Qt.LocalTime
########################################################################
class ToolBarArea:
	RightToolBarArea                  = Qt.RightToolBarArea
	TopToolBarArea                    = Qt.TopToolBarArea
	ToolBarArea_Mask                  = Qt.ToolBarArea_Mask
	NoToolBarArea                     = Qt.NoToolBarArea
	LeftToolBarArea                   = Qt.LeftToolBarArea
	AllToolBarAreas                   = Qt.AllToolBarAreas
	BottomToolBarArea                 = Qt.BottomToolBarArea
########################################################################
class ToolButtonStyle:
	ToolButtonIconOnly                = Qt.ToolButtonIconOnly
	ToolButtonTextBesideIcon          = Qt.ToolButtonTextBesideIcon
	ToolButtonTextOnly                = Qt.ToolButtonTextOnly
	ToolButtonFollowStyle             = Qt.ToolButtonFollowStyle
	ToolButtonTextUnderIcon           = Qt.ToolButtonTextUnderIcon
########################################################################
class TouchPointState:
	TouchPointReleased                = Qt.TouchPointReleased
	TouchPointPressed                 = Qt.TouchPointPressed
	TouchPointMoved                   = Qt.TouchPointMoved
	TouchPointStationary              = Qt.TouchPointStationary
########################################################################
class UIEffect:
	AnimateCombo                      = Qt.UI_AnimateCombo
	FadeMenu                          = Qt.UI_FadeMenu
	AnimateTooltip                    = Qt.UI_AnimateTooltip
	AnimateMenu                       = Qt.UI_AnimateMenu
	FadeTooltip                       = Qt.UI_FadeTooltip
	General                           = Qt.UI_General
	AnimateToolBox                    = Qt.UI_AnimateToolBox
########################################################################
class WhiteSpaceMode:
	WhiteSpaceNoWrap                  = Qt.WhiteSpaceNoWrap
	WhiteSpaceModeUndefined           = Qt.WhiteSpaceModeUndefined
	WhiteSpaceNormal                  = Qt.WhiteSpaceNormal
	WhiteSpacePre                     = Qt.WhiteSpacePre
########################################################################
class WidgetAttribute:
	CustomWhatsThis                   = Qt.WA_CustomWhatsThis
	SetFont                           = Qt.WA_SetFont
	NoChildEventsForParent            = Qt.WA_NoChildEventsForParent
	AlwaysShowToolTips                = Qt.WA_AlwaysShowToolTips
	MacBrushedMetal                   = Qt.WA_MacBrushedMetal
	AcceptTouchEvents                 = Qt.WA_AcceptTouchEvents
	X11NetWmWindowTypeUtility         = Qt.WA_X11NetWmWindowTypeUtility
	Hover                             = Qt.WA_Hover
	TransparentForMouseEvents         = Qt.WA_TransparentForMouseEvents
	PendingUpdate                     = Qt.WA_PendingUpdate
	PaintUnclipped                    = Qt.WA_PaintUnclipped
	MacMiniSize                       = Qt.WA_MacMiniSize
	MacOpaqueSizeGrip                 = Qt.WA_MacOpaqueSizeGrip
	X11NetWmWindowTypeDropDownMenu    = Qt.WA_X11NetWmWindowTypeDropDownMenu
	SetLayoutDirection                = Qt.WA_SetLayoutDirection
	NoMousePropagation                = Qt.WA_NoMousePropagation
	SetLocale                         = Qt.WA_SetLocale
	QuitOnClose                       = Qt.WA_QuitOnClose
	MacSmallSize                      = Qt.WA_MacSmallSize
	MSWindowsUseDirect3D              = Qt.WA_MSWindowsUseDirect3D
	TouchPadAcceptSingleTouchEvents   = Qt.WA_TouchPadAcceptSingleTouchEvents
	WState_Reparented                 = Qt.WA_WState_Reparented
	ForceUpdatesDisabled              = Qt.WA_ForceUpdatesDisabled
	X11NetWmWindowTypeDND             = Qt.WA_X11NetWmWindowTypeDND
	MacVariableSize                   = Qt.WA_MacVariableSize
	LayoutUsesWidgetRect              = Qt.WA_LayoutUsesWidgetRect
	SetStyle                          = Qt.WA_SetStyle
	WState_ConfigPending              = Qt.WA_WState_ConfigPending
	X11NetWmWindowTypeDesktop         = Qt.WA_X11NetWmWindowTypeDesktop
	X11NetWmWindowTypeMenu            = Qt.WA_X11NetWmWindowTypeMenu
	MacShowFocusRect                  = Qt.WA_MacShowFocusRect
	NoMouseReplay                     = Qt.WA_NoMouseReplay
	X11NetWmWindowTypeDock            = Qt.WA_X11NetWmWindowTypeDock
	SetPalette                        = Qt.WA_SetPalette
	OpaquePaintEvent                  = Qt.WA_OpaquePaintEvent
	UpdatesDisabled                   = Qt.WA_UpdatesDisabled
	MouseTracking                     = Qt.WA_MouseTracking
	WState_Created                    = Qt.WA_WState_Created
	NoSystemBackground                = Qt.WA_NoSystemBackground
	Disabled                          = Qt.WA_Disabled
	InvalidSize                       = Qt.WA_InvalidSize
	WState_InPaintEvent               = Qt.WA_WState_InPaintEvent
	MacMetalStyle                     = Qt.WA_MacMetalStyle
	X11NetWmWindowTypePopupMenu       = Qt.WA_X11NetWmWindowTypePopupMenu
	NativeWindow                      = Qt.WA_NativeWindow
	WState_ExplicitShowHide           = Qt.WA_WState_ExplicitShowHide
	OutsideWSRange                    = Qt.WA_OutsideWSRange
	SetCursor                         = Qt.WA_SetCursor
	# MergeSoftkeys                   = Qt.WA_MergeSoftkeys
	SetWindowIcon                     = Qt.WA_SetWindowIcon
	X11DoNotAcceptFocus               = Qt.WA_X11DoNotAcceptFocus
	StyledBackground                  = Qt.WA_StyledBackground
	X11NetWmWindowTypeToolBar         = Qt.WA_X11NetWmWindowTypeToolBar
	KeyCompression                    = Qt.WA_KeyCompression
	InputMethodTransparent            = Qt.WA_InputMethodTransparent
	X11NetWmWindowTypeToolTip         = Qt.WA_X11NetWmWindowTypeToolTip
	X11NetWmWindowTypeSplash          = Qt.WA_X11NetWmWindowTypeSplash
	InputMethodEnabled                = Qt.WA_InputMethodEnabled
	StaticContents                    = Qt.WA_StaticContents
	NoX11EventCompression             = Qt.WA_NoX11EventCompression
	AcceptDrops                       = Qt.WA_AcceptDrops
	TintedBackground                  = Qt.WA_TintedBackground
	Mapped                            = Qt.WA_Mapped
	MouseNoMask                       = Qt.WA_MouseNoMask
	TranslucentBackground             = Qt.WA_TranslucentBackground
	KeyboardFocusChange               = Qt.WA_KeyboardFocusChange
	X11NetWmWindowTypeNotification    = Qt.WA_X11NetWmWindowTypeNotification
	LaidOut                           = Qt.WA_LaidOut
	WState_OwnSizePolicy              = Qt.WA_WState_OwnSizePolicy
	MacFrameworkScaled                = Qt.WA_MacFrameworkScaled
	MacNoClickThrough                 = Qt.WA_MacNoClickThrough
	X11OpenGLOverlay                  = Qt.WA_X11OpenGLOverlay
	AttributeCount                    = Qt.WA_AttributeCount
	PaintOnScreen                     = Qt.WA_PaintOnScreen
	X11NetWmWindowTypeCombo           = Qt.WA_X11NetWmWindowTypeCombo
	PendingResizeEvent                = Qt.WA_PendingResizeEvent
	MacAlwaysShowToolWindow           = Qt.WA_MacAlwaysShowToolWindow
	ShowWithoutActivating             = Qt.WA_ShowWithoutActivating
	# MergeSoftkeysRecursively        = Qt.WA_MergeSoftkeysRecursively
	WState_CompressKeys               = Qt.WA_WState_CompressKeys
	UnderMouse                        = Qt.WA_UnderMouse
	WState_Visible                    = Qt.WA_WState_Visible
	GroupLeader                       = Qt.WA_GroupLeader
	MacNormalSize                     = Qt.WA_MacNormalSize
	LayoutOnEntireRect                = Qt.WA_LayoutOnEntireRect
	DeleteOnClose                     = Qt.WA_DeleteOnClose
	WindowPropagation                 = Qt.WA_WindowPropagation
	Moved                             = Qt.WA_Moved
	# PaintOutsidePaintEvent          = Qt.WA_PaintOutsidePaintEvent
	DontCreateNativeAncestors         = Qt.WA_DontCreateNativeAncestors
	Resized                           = Qt.WA_Resized
	PendingMoveEvent                  = Qt.WA_PendingMoveEvent
	StyleSheet                        = Qt.WA_StyleSheet
	WState_Hidden                     = Qt.WA_WState_Hidden
	X11NetWmWindowTypeDialog          = Qt.WA_X11NetWmWindowTypeDialog
	ForceDisabled                     = Qt.WA_ForceDisabled
	NoChildEventsFromChildren         = Qt.WA_NoChildEventsFromChildren
	WState_Polished                   = Qt.WA_WState_Polished
	WindowModified                    = Qt.WA_WindowModified
########################################################################
class WindowFrameSection:
	TopRightSection                   = Qt.TopRightSection
	BottomRightSection                = Qt.BottomRightSection
	NoSection                         = Qt.NoSection
	TopSection                        = Qt.TopSection
	TopLeftSection                    = Qt.TopLeftSection
	RightSection                      = Qt.RightSection
	BottomLeftSection                 = Qt.BottomLeftSection
	TitleBarArea                      = Qt.TitleBarArea
	LeftSection                       = Qt.LeftSection
	BottomSection                     = Qt.BottomSection
########################################################################
class WindowState:
	WindowNoState                     = Qt.WindowNoState
	WindowFullScreen                  = Qt.WindowFullScreen
	WindowMaximized                   = Qt.WindowMaximized
	WindowActive                      = Qt.WindowActive
	WindowMinimized                   = Qt.WindowMinimized
########################################################################
class WindowType:
	SubWindow                         = Qt.SubWindow
	Sheet                             = Qt.Sheet
	Desktop                           = Qt.Desktop
	WindowType_Mask                   = Qt.WindowType_Mask
	WindowShadeButtonHint             = Qt.WindowShadeButtonHint
	Window                            = Qt.Window
	WindowMinimizeButtonHint          = Qt.WindowMinimizeButtonHint
	# WindowSoftkeysVisibleHint    = Qt.WindowSoftkeysVisibleHint
	CustomizeWindowHint               = Qt.CustomizeWindowHint
	WindowCancelButtonHint            = Qt.WindowCancelButtonHint
	WindowMaximizeButtonHint          = Qt.WindowMaximizeButtonHint
	Widget                            = Qt.Widget
	Popup                             = Qt.Popup
	WindowStaysOnTopHint              = Qt.WindowStaysOnTopHint
	BypassGraphicsProxyWidget         = Qt.BypassGraphicsProxyWidget
	Tool                              = Qt.Tool
	WindowTitleHint                   = Qt.WindowTitleHint
	X11BypassWindowManagerHint        = Qt.X11BypassWindowManagerHint
	MSWindowsFixedSizeDialogHint      = Qt.MSWindowsFixedSizeDialogHint
	WindowMinMaxButtonsHint           = Qt.WindowMinMaxButtonsHint
	MacWindowToolBarButtonHint        = Qt.MacWindowToolBarButtonHint
	FramelessWindowHint               = Qt.FramelessWindowHint
	WindowOkButtonHint                = Qt.WindowOkButtonHint
	MSWindowsOwnDC                    = Qt.MSWindowsOwnDC
	WindowCloseButtonHint             = Qt.WindowCloseButtonHint
	Dialog                            = Qt.Dialog
	# WindowSoftkeysRespondHint    = Qt.WindowSoftkeysRespondHint
	WindowSystemMenuHint              = Qt.WindowSystemMenuHint
	ToolTip                           = Qt.ToolTip
	WindowContextHelpButtonHint       = Qt.WindowContextHelpButtonHint
	Drawer                            = Qt.Drawer
	WindowStaysOnBottomHint           = Qt.WindowStaysOnBottomHint
	SplashScreen                      = Qt.SplashScreen

########################################################################
class Font:
	""""""
	class SpacingType:
		PercentageSpacing = QFont.PercentageSpacing # A value of 100 will keep the spacing unchanged; a value of 200 will enlarge the spacing after a character by the width of the character itself.
		AbsoluteSpacing   = QFont.AbsoluteSpacing   # A positive value increases the letter spacing by the corresponding pixels; a negative value decreases the spacing.
	class StyleHint:
		AnyStyle   = QFont.AnyStyle    # leaves the font matching algorithm to choose the family. This is the default.
		SansSerif  = QFont.SansSerif   # the font matcher prefer sans serif fonts.
		Helvetica  = QFont.Helvetica   # is a synonym for SansSerif.
		Serif      = QFont.Serif       # the font matcher prefers serif fonts.
		Times      = QFont.Times       # is a synonym for Serif.
		TypeWriter = QFont.TypeWriter  # the font matcher prefers fixed pitch fonts.
		Courier    = QFont.Courier     # a synonym for TypeWriter.
		OldEnglish = QFont.OldEnglish  # the font matcher prefers decorative fonts.
		Decorative = QFont.Decorative  # is a synonym for OldEnglish.
		Monospace  = QFont.Monospace   # the font matcher prefers fonts that map to the CSS generic font-family monospace.
		Fantasy    = QFont.Fantasy     # the font matcher prefers fonts that map to the CSS generic font-family fantasy.
		Cursive    = QFont.Cursive     # the font matcher prefers fonts that map to the CSS generic font-family cursive.
		System     = QFont.System      # the font matcher prefers system fonts.
	class Weight:
		Light    = QFont.Light    # 25
		Normal   = QFont.Normal   # 50
		DemiBold = QFont.DemiBold # 63
		Bold     = QFont.Bold     # 75
		Black    = QFont.Black    # 87

	class Capitalization:
		MixedCase    = QFont.MixedCase    # This is the normal text rendering option where no capitalization change is applied.
		AllUppercase = QFont.AllUppercase # This alters the text to be rendered in all uppercase type.
		AllLowercase = QFont.AllLowercase # This alters the text to be rendered in all lowercase type.
		SmallCaps    = QFont.SmallCaps    # This alters the text to be rendered in small-caps type.
		Capitalize   = QFont.Capitalize   # This alters the text to be rendered with the first character of each word as an uppercase character.
		
	class Stretch:
		UltraCondensed = QFont.UltraCondensed # 50
		ExtraCondensed = QFont.ExtraCondensed # 62
		Condensed      = QFont.Condensed      # 75
		SemiCondensed  = QFont.SemiCondensed  # 87
		Unstretched    = QFont.Unstretched    # 100
		SemiExpanded   = QFont.SemiExpanded   # 112
		Expanded       = QFont.Expanded       # 125
		ExtraExpanded  = QFont.ExtraExpanded  # 150
		UltraExpanded  = QFont.UltraExpanded  # 200
########################################################################
class AbstractItemView:
	########################################################################
	class Drag_Drop_Mode:
		DragDrop     = QAbstractItemView.DragDrop
		DragOnly     = QAbstractItemView.DragOnly
		DropOnly     = QAbstractItemView.DropOnly
		InternalMove = QAbstractItemView.InternalMove
		NoDragDrop   = QAbstractItemView.NoDragDrop
	########################################################################
	class CursorAction:
		Down     = QAbstractItemView.MoveDown
		Up       = QAbstractItemView.MoveUp
		Left     = QAbstractItemView.MoveLeft
		Right    = QAbstractItemView.MoveRight
		Home     = QAbstractItemView.MoveHome
		End      = QAbstractItemView.MoveEnd
		Next     = QAbstractItemView.MoveNext
		Previous = QAbstractItemView.MovePrevious
		PageUp   = QAbstractItemView.MovePageUp
		PageDown = QAbstractItemView.MovePageDown
	########################################################################
	class DropIndicatorPosition:
		AboveItem  = QAbstractItemView.AboveItem
		BelowItem  = QAbstractItemView.BelowItem
		OnItem     = QAbstractItemView.OnItem
		OnViewport = QAbstractItemView.OnViewport
	########################################################################
	class EditTrigger:
		AllEditTriggers = QAbstractItemView.AllEditTriggers
		AnyKeyPressed   = QAbstractItemView.AnyKeyPressed
		CurrentChanged  = QAbstractItemView.CurrentChanged
		DoubleClicked   = QAbstractItemView.DoubleClicked
		EditKeyPressed  = QAbstractItemView.EditKeyPressed
		NoEditTriggers  = QAbstractItemView.NoEditTriggers
		SelectedClicked = QAbstractItemView.SelectedClicked
	########################################################################
	class ScrollHint:
		EnsureVisible    = QAbstractItemView.EnsureVisible
		PositionAtBottom = QAbstractItemView.PositionAtBottom
		PositionAtCenter = QAbstractItemView.PositionAtCenter
		PositionAtTop    = QAbstractItemView.PositionAtTop
	########################################################################
	class ScrollMode:
		PerItem  = QAbstractItemView.ScrollPerItem
		PerPixel = QAbstractItemView.ScrollPerPixel
	########################################################################
	class SelectionBehavior:
		Columns = QAbstractItemView.SelectColumns
		Items   = QAbstractItemView.SelectItems
		Rows    = QAbstractItemView.SelectRows
	########################################################################
	class SelectionMode:
		Contiguous = QAbstractItemView.ContiguousSelection
		Extended   = QAbstractItemView.ExtendedSelection
		Multi      = QAbstractItemView.MultiSelection
		No         = QAbstractItemView.NoSelection
		Single     = QAbstractItemView.SingleSelection
	########################################################################
	class Shadow:
		Plain  = QAbstractItemView.Plain
		Raised = QAbstractItemView.Raised
		Sunken = QAbstractItemView.Sunken
	########################################################################	
	class Shape:
		Box         = QAbstractItemView.Box
		HLine       = QAbstractItemView.HLine
		NoFrame     = QAbstractItemView.NoFrame
		Panel       = QAbstractItemView.Panel
		StyledPanel = QAbstractItemView.StyledPanel
		VLine       = QAbstractItemView.VLine
		WinPanel    = QAbstractItemView.WinPanel
	########################################################################
	class State:
		Animating     = QAbstractItemView.AnimatingState
		Collapsing    = QAbstractItemView.CollapsingState
		DragSelecting = QAbstractItemView.DragSelectingState
		Dragging      = QAbstractItemView.DraggingState
		Editing       = QAbstractItemView.EditingState
		Expanding     = QAbstractItemView.ExpandingState
		No            = QAbstractItemView.NoState

########################################################################
class PenStyles:
	NoPen                        = Qt.NoPen          # no line at all. For example, QPainter.drawRect() fills but does not draw any boundary line.
	SolidLine                    = Qt.SolidLine      # A plain line.
	DashLine                     = Qt.DashLine       # Dashes separated by a few pixels.
	DotLine                      = Qt.DotLine        # Dots separated by a few pixels.
	DashDotLine                  = Qt.DashDotLine    # Alternate dots and dashes.
	DashDotDotLine               = Qt.DashDotDotLine # One dash, two dots, one dash, two dots.
	CustomDashLine               = Qt.CustomDashLine # A custom pattern defined using QPainterPathStroker.setDashPattern() .
########################################################################
class BrushStyles:
	NoBrush                      = Qt.NoBrush                # No brush pattern.
	SolidPattern                 = Qt.SolidPattern           # Uniform color.
	Dense1Pattern                = Qt.Dense1Pattern          # Extremely dense brush pattern.
	Dense2Pattern                = Qt.Dense2Pattern          # Very dense brush pattern.
	Dense3Pattern                = Qt.Dense3Pattern          # Somewhat dense brush pattern.
	Dense4Pattern                = Qt.Dense4Pattern          # Half dense brush pattern.
	Dense5Pattern                = Qt.Dense5Pattern          # Somewhat sparse brush pattern.
	Dense6Pattern                = Qt.Dense6Pattern          # Very sparse brush pattern.
	Dense7Pattern                = Qt.Dense7Pattern          # Extremely sparse brush pattern.
	HorPattern                   = Qt.HorPattern             # Horizontal lines.
	VerPattern                   = Qt.VerPattern             # Vertical lines.
	CrossPattern                 = Qt.CrossPattern           # Crossing horizontal and vertical lines.
	BDiagPattern                 = Qt.BDiagPattern           # Backward diagonal lines.
	FDiagPattern                 = Qt.FDiagPattern           # Forward diagonal lines.
	DiagCrossPattern             = Qt.DiagCrossPattern       # Crossing diagonal lines.
	LinearGradientPattern        = Qt.LinearGradientPattern  # Linear gradient (set using a dedicated PySide.QtGui.QBrush constructor).
	ConicalGradientPattern       = Qt.ConicalGradientPattern # Conical gradient (set using a dedicated PySide.QtGui.QBrush constructor).
	RadialGradientPattern        = Qt.RadialGradientPattern  # Radial gradient (set using a dedicated PySide.QtGui.QBrush constructor).
	TexturePattern               = Qt.TexturePattern         # Custom pattern (see QBrush.setTexture() ).
########################################################################
class DropActions:
	CopyAction                   = Qt.CopyAction       # Copy the data to the target.
	MoveAction                   = Qt.MoveAction       # Move the data from the source to the target.
	LinkAction                   = Qt.LinkAction       # Create a link from the source to the target.
	ActionMask                   = Qt.ActionMask       #
	IgnoreAction                 = Qt.IgnoreAction     # Ignore the action (do nothing with the data).
	TargetMoveAction             = Qt.TargetMoveAction # On Windows, this value is used when the ownership of the D&D data should be taken over by the target application, i.e., the source application should not delete the data. .. raw:: html <br /> On X11 this value is used to do a move. .. raw:: html <br /> TargetMoveAction is not used on the Mac.
########################################################################
class GestureTypes:
	TapGesture                   = Qt.TapGesture           # A Tap gesture.
	TapAndHoldGesture            = Qt.TapAndHoldGesture    # A Tap-And-Hold (Long-Tap) gesture.
	PanGesture                   = Qt.PanGesture           # A Pan gesture.
	PinchGesture                 = Qt.PinchGesture         # A Pinch gesture.
	SwipeGesture                 = Qt.SwipeGesture         # A Swipe gesture.
	CustomGesture                = Qt.CustomGesture        # A flag that can be used to test if the gesture is a user-defined gesture ID.
########################################################################
class CheckStates:
	Unchecked                    = Qt.Unchecked           # The item is unchecked.
	PartiallyChecked             = Qt.PartiallyChecked    # The item is partially checked. Items in hierarchical models may be partially checked if some, but not all, of their children are checked
	Checked                      = Qt.Checked             # The item is checked.
########################################################################
class ItemFlag:
	NoItemFlags                  = Qt.NoItemFlags         # It does not have any properties set.
	IsSelectable                 = Qt.ItemIsSelectable    # It can be selected.
	IsEditable                   = Qt.ItemIsEditable      # It can be edited.
	IsDragEnabled                = Qt.ItemIsDragEnabled   # It can be dragged.
	IsDropEnabled                = Qt.ItemIsDropEnabled   # It can be used as a drop target.
	IsUserCheckable              = Qt.ItemIsUserCheckable # It can be checked or unchecked by the user.
	IsEnabled                    = Qt.ItemIsEnabled       # The user can interact with the item.
	IsTristate                   = Qt.ItemIsTristate      # The item is checkable with three separate states.
########################################################################
class AlignmentFlag:
	class Horizontal:
		Left    = Qt.AlignmentFlag.AlignLeft     # Aligns with the left edge.
		Right   = Qt.AlignmentFlag.AlignRight    # Aligns with the right edge.
		Center  = Qt.AlignmentFlag.AlignHCenter  # Centers horizontally in the available space.
		Justify = Qt.AlignmentFlag.AlignJustify  # Justifies the text in the available space.
		Values  = {'Center' : Center , Center : Center  , Center.name : Center, 
		           'Left'   : Left   , Left   : Left    , Left.name   : Left, 
		           'Justify': Justify, Justify: Justify , Justify.name: Justify, 
		           'Right'  : Right  , Right  : Right   , Right.name  : Right}
	class Vertical:
		Top     = Qt.AlignmentFlag.AlignTop     # Aligns with the top.
		Bottom  = Qt.AlignmentFlag.AlignBottom  # Aligns with the bottom.
		Center  = Qt.AlignmentFlag.AlignVCenter # Centers vertically in the available space.
		Values  = {'Top'    : Top   , Top     : Top   , Top.name     : Top, 
		           'Bottom' : Bottom, Bottom  : Bottom, Bottom.name  : Bottom, 
		           'Center' : Center, Center  : Center, Center.name  : Center}
	class Masks:
		Horizontal = Qt.AlignmentFlag.AlignHorizontal_Mask
		Vertical   = Qt.AlignmentFlag.AlignVertical_Mask
		Values     = {'Horizontal': Horizontal, Horizontal : "Horizontal",
		              'Vertical'  : Vertical  , Vertical   : "Vertical"}
	Center = Qt.AlignmentFlag.AlignCenter # Centers in both dimensions.
########################################################################
class MatchFlag:
	CaseSensitive                = Qt.MatchCaseSensitive
	Contains                     = Qt.MatchContains
	EndsWith                     = Qt.MatchEndsWith
	Exactly                      = Qt.MatchExactly
	FixedString                  = Qt.MatchFixedString
	Recursive                    = Qt.MatchRecursive
	RegExp                       = Qt.MatchRegExp
	StartsWith                   = Qt.MatchStartsWith
	Wildcard                     = Qt.MatchWildcard
	Wrap                         = Qt.MatchWrap
########################################################################
class DayOfWeek:
	Friday                       = Qt.Friday
	Monday                       = Qt.Monday
	Saturday                     = Qt.Saturday
	Sunday                       = Qt.Sunday
	Thursday                     = Qt.Thursday
	Tuesday                      = Qt.Tuesday
	Wednesday                    = Qt.Wednesday
########################################################################
class MouseButton:
	RightButton                  = Qt.RightButton
	MiddleButton                 = Qt.MiddleButton
	NoButton                     = Qt.NoButton
	LeftButton                   = Qt.LeftButton
	MouseButtonMask              = Qt.MouseButtonMask
	XButton1                     = Qt.XButton1
	XButton2                     = Qt.XButton2
	MidButton                    = Qt.MidButton
########################################################################
class Modifier:
	CTRL                         = Qt.CTRL
	SHIFT                        = Qt.SHIFT
	UNICODE_ACCEL                = Qt.UNICODE_ACCEL
	MODIFIER_MASK                = Qt.MODIFIER_MASK
	META                         = Qt.META
	ALT                          = Qt.ALT
########################################################################
class SizeHint:
	MinimumDescent               = Qt.MinimumDescent
	PreferredSize                = Qt.PreferredSize
	MinimumSize                  = Qt.MinimumSize
	MaximumSize                  = Qt.MaximumSize
########################################################################
class TextFlag:
	TextShowMnemonic             = Qt.TextShowMnemonic
	TextHideMnemonic             = Qt.TextHideMnemonic
	TextJustificationForced      = Qt.TextJustificationForced
	TextDontClip                 = Qt.TextDontClip
	TextIncludeTrailingSpaces    = Qt.TextIncludeTrailingSpaces
	TextDontPrint                = Qt.TextDontPrint
	TextSingleLine               = Qt.TextSingleLine
	TextWrapAnywhere             = Qt.TextWrapAnywhere
	TextExpandTabs               = Qt.TextExpandTabs
	TextWordWrap                 = Qt.TextWordWrap
########################################################################
class Colors:
	""""""
	WHITE        = Qt.white       #ffffff
	BLACK        = Qt.black       #000000
	RED          = Qt.red         #ff0000
	DARK_RED     = Qt.darkRed     #800000
	GREEN        = Qt.green       #00ff00
	DARK_GREEN   = Qt.darkGreen	  #008000
	BLUE         = Qt.blue        #0000ff
	DARK_BLUE    = Qt.darkBlue    #000080
	CYAN         = Qt.cyan        #00ffff
	DARK_CYAN    = Qt.darkCyan    #008080
	MAGENTA      = Qt.magenta     #ff00ff
	DARK_MAGENTA = Qt.darkMagenta #800080
	YELLOW       = Qt.yellow      #ffff00
	DARK_YELLOW  = Qt.darkYellow  #808000
	GRAY         = Qt.gray        #a0a0a4
	DARK_GRAY    = Qt.darkGray    #808080
	LIGHT_GRAY   = Qt.lightGray   #c0c0c0
	TRANSPARENT  = Qt.transparent # a transparent black value (i.e., PySide.QtGui.QColor (0, 0, 0, 0))
########################################################################
class QSTYLE:
	########################################################################
	class PrimitiveElement:
		FrameStatusBar                  = QStyle.PE_FrameStatusBar #Frame
		PanelButtonCommand              = QStyle.PE_PanelButtonCommand #Button used to initiate an action, for example, a PySide.QtGui.QPushButton .
		FrameDefaultButton              = QStyle.PE_FrameDefaultButton #This frame around a default button, e.g. in a dialog.
		PanelButtonBevel                = QStyle.PE_PanelButtonBevel #Generic panel with a button bevel.
		PanelButtonTool                 = QStyle.PE_PanelButtonTool #Panel for a Tool button, used with PySide.QtGui.QToolButton .
		PanelLineEdit                   = QStyle.PE_PanelLineEdit #Panel for a PySide.QtGui.QLineEdit .
		IndicatorButtonDropDown         = QStyle.PE_IndicatorButtonDropDown #Indicator for a drop down button, for example, a tool button that displays a menu.
		FrameFocusRect                  = QStyle.PE_FrameFocusRect #Generic focus indicator.
		IndicatorArrowUp                = QStyle.PE_IndicatorArrowUp #Generic Up arrow.
		IndicatorArrowDown              = QStyle.PE_IndicatorArrowDown #Generic Down arrow.
		IndicatorArrowRight             = QStyle.PE_IndicatorArrowRight #Generic Right arrow.
		IndicatorArrowLeft              = QStyle.PE_IndicatorArrowLeft #Generic Left arrow.
		IndicatorSpinUp                 = QStyle.PE_IndicatorSpinUp #Up symbol for a spin widget, for example a PySide.QtGui.QSpinBox .
		IndicatorSpinDown               = QStyle.PE_IndicatorSpinDown #Down symbol for a spin widget.
		IndicatorSpinPlus               = QStyle.PE_IndicatorSpinPlus #Increase symbol for a spin widget.
		IndicatorSpinMinus              = QStyle.PE_IndicatorSpinMinus #Decrease symbol for a spin widget.
		IndicatorItemViewItemCheck      = QStyle.PE_IndicatorItemViewItemCheck #On/off indicator for a view item.
		IndicatorCheckBox               = QStyle.PE_IndicatorCheckBox #On/off indicator, for example, a PySide.QtGui.QCheckBox .
		IndicatorRadioButton            = QStyle.PE_IndicatorRadioButton #Exclusive on/off indicator, for example, a PySide.QtGui.QRadioButton .
		IndicatorDockWidgetResizeHandle = QStyle.PE_IndicatorDockWidgetResizeHandle #Resize handle for dock windows.
		Frame                           = QStyle.PE_Frame #Generic frame
		FrameMenu                       = QStyle.PE_FrameMenu #Frame for popup windows/menus; see also PySide.QtGui.QMenu .
		PanelMenuBar                    = QStyle.PE_PanelMenuBar #Panel for menu bars.
		PanelScrollAreaCorner           = QStyle.PE_PanelScrollAreaCorner #Panel at the bottom-right (or bottom-left) corner of a scroll area.
		FrameDockWidget                 = QStyle.PE_FrameDockWidget #Panel frame for dock windows and toolbars.
		FrameTabWidget                  = QStyle.PE_FrameTabWidget #Frame for tab widgets.
		FrameLineEdit                   = QStyle.PE_FrameLineEdit #Panel frame for line edits.
		FrameGroupBox                   = QStyle.PE_FrameGroupBox #Panel frame around group boxes.
		FrameButtonBevel                = QStyle.PE_FrameButtonBevel #Panel frame for a button bevel.
		FrameButtonTool                 = QStyle.PE_FrameButtonTool #Panel frame for a tool button.
		IndicatorHeaderArrow            = QStyle.PE_IndicatorHeaderArrow #Arrow used to indicate sorting on a list or table header.
		FrameStatusBarItem              = QStyle.PE_FrameStatusBarItem #Frame for an item of a status bar; see also PySide.QtGui.QStatusBar .
		FrameWindow                     = QStyle.PE_FrameWindow #Frame around a MDI window or a docking window.
		IndicatorMenuCheckMark          = QStyle.PE_IndicatorMenuCheckMark #Check mark used in a menu.
		IndicatorProgressChunk          = QStyle.PE_IndicatorProgressChunk #Section of a progress bar indicator; see also PySide.QtGui.QProgressBar .
		IndicatorBranch                 = QStyle.PE_IndicatorBranch #Lines used to represent the branch of a tree in a tree view.
		IndicatorToolBarHandle          = QStyle.PE_IndicatorToolBarHandle #The handle of a toolbar.
		IndicatorToolBarSeparator       = QStyle.PE_IndicatorToolBarSeparator #The separator in a toolbar.
		PanelToolBar                    = QStyle.PE_PanelToolBar #The panel for a toolbar.
		PanelTipLabel                   = QStyle.PE_PanelTipLabel #The panel for a tip label.
		FrameTabBarBase                 = QStyle.PE_FrameTabBarBase
		IndicatorTabTear                = QStyle.PE_IndicatorTabTear #An indicator that a tab is partially scrolled out of the visible tab bar when there are many tabs.
		IndicatorColumnViewArrow        = QStyle.PE_IndicatorColumnViewArrow #An arrow in a PySide.QtGui.QColumnView .
		Widget                          = QStyle.PE_Widget #A plain PySide.QtGui.QWidget .
		CustomBase                      = QStyle.PE_CustomBase #Base value for custom primitive elements. All values above this are reserved for custom use. Custom values must be greater than this value.
		IndicatorItemViewItemDrop       = QStyle.PE_IndicatorItemViewItemDrop #An indicator that is drawn to show where an item in an item view is about to be dropped during a drag-and-drop operation in an item view.
		PanelItemViewItem               = QStyle.PE_PanelItemViewItem #The background for an item in an item view.
		PanelItemViewRow                = QStyle.PE_PanelItemViewRow #The background of a row in an item view.
		PanelStatusBar                  = QStyle.PE_PanelStatusBar #The panel for a status bar.
		IndicatorTabClose               = QStyle.PE_IndicatorTabClose #The close button on a tab bar.
		PanelMenu                       = QStyle.PE_PanelMenu #The panel for a menu.
	########################################################################
	class StyleHint:
		EtchDisabledText                               = QStyle.SH_EtchDisabledText #Disabled text is etched as it is on Windows.
		DitherDisabledText                             = QStyle.SH_DitherDisabledText #Disabled text is dithered as it is on Motif.
		ScrollBar_ContextMenu                          = QStyle.SH_ScrollBar_ContextMenu #Whether or not a scroll bar has a context menu.
		ScrollBar_MiddleClickAbsolutePosition          = QStyle.SH_ScrollBar_MiddleClickAbsolutePosition #A boolean value. If true, middle clicking on a scroll bar causes the slider to jump to that position. If false, middle clicking is ignored.
		ScrollBar_LeftClickAbsolutePosition            = QStyle.SH_ScrollBar_LeftClickAbsolutePosition #A boolean value. If true, left clicking on a scroll bar causes the slider to jump to that position. If false, left clicking will behave as appropriate for each control.
		ScrollBar_ScrollWhenPointerLeavesControl       = QStyle.SH_ScrollBar_ScrollWhenPointerLeavesControl #A boolean value. If true, when clicking a scroll bar QStyle.SubControl , holding the mouse button down and moving the pointer outside the QStyle.SubControl , the scroll bar continues to scroll. If false, the scollbar stops scrolling when the pointer leaves the QStyle.SubControl .
		ScrollBar_RollBetweenButtons                   = QStyle.SH_ScrollBar_RollBetweenButtons #A boolean value. If true, when clicking a scroll bar button ( SC_ScrollBarAddLine or SC_ScrollBarSubLine ) and dragging over to the opposite button (rolling) will press the new button and release the old one. When it is false, the original button is released and nothing happens (like a push button).
		TabBar_Alignment                               = QStyle.SH_TabBar_Alignment #The alignment for tabs in a PySide.QtGui.QTabWidget . Possible values are Qt.AlignLeft , Qt.AlignCenter and Qt.AlignRight .
		Header_ArrowAlignment                          = QStyle.SH_Header_ArrowAlignment #The placement of the sorting indicator may appear in list or table headers. Possible values are Qt.Left or Qt.Right .
		Slider_SnapToValue                             = QStyle.SH_Slider_SnapToValue #Sliders snap to values while moving, as they do on Windows.
		Slider_SloppyKeyEvents                         = QStyle.SH_Slider_SloppyKeyEvents #Key presses handled in a sloppy manner, i.e., left on a vertical slider subtracts a line.
		ProgressDialog_CenterCancelButton              = QStyle.SH_ProgressDialog_CenterCancelButton #Center button on progress dialogs, like Motif, otherwise right aligned.
		ProgressDialog_TextLabelAlignment              = QStyle.SH_ProgressDialog_TextLabelAlignment #The alignment for text labels in progress dialogs; Qt.AlignCenter on Windows, Qt.AlignVCenter otherwise.
		PrintDialog_RightAlignButtons                  = QStyle.SH_PrintDialog_RightAlignButtons #Right align buttons in the print dialog, as done on Windows.
		MainWindow_SpaceBelowMenuBar                   = QStyle.SH_MainWindow_SpaceBelowMenuBar #One or two pixel space between the menu bar and the dockarea, as done on Windows.
		FontDialog_SelectAssociatedText                = QStyle.SH_FontDialog_SelectAssociatedText #Select the text in the line edit, or when selecting an item from the listbox, or when the line edit receives focus, as done on Windows.
		Menu_KeyboardSearch                            = QStyle.SH_Menu_KeyboardSearch #Typing causes a menu to be search for relevant items, otherwise only mnemnonic is considered.
		Menu_AllowActiveAndDisabled                    = QStyle.SH_Menu_AllowActiveAndDisabled #Allows disabled menu items to be active.
		Menu_SpaceActivatesItem                        = QStyle.SH_Menu_SpaceActivatesItem #Pressing the space bar activates the item, as done on Motif.
		Menu_SubMenuPopupDelay                         = QStyle.SH_Menu_SubMenuPopupDelay #The number of milliseconds to wait before opening a submenu (256 on Windows, 96 on Motif).
		Menu_Scrollable                                = QStyle.SH_Menu_Scrollable #Whether popup menus must support scrolling.
		Menu_SloppySubMenus                            = QStyle.SH_Menu_SloppySubMenus #Whether popupmenus must support sloppy submenu; as implemented on Mac OS.
		ScrollView_FrameOnlyAroundContents             = QStyle.SH_ScrollView_FrameOnlyAroundContents #Whether scrollviews draw their frame only around contents (like Motif), or around contents, scroll bars and corner widgets (like Windows).
		MenuBar_AltKeyNavigation                       = QStyle.SH_MenuBar_AltKeyNavigation #Menu bars items are navigable by pressing Alt, followed by using the arrow keys to select the desired item.
		ComboBox_ListMouseTracking                     = QStyle.SH_ComboBox_ListMouseTracking #Mouse tracking in combobox drop-down lists.
		Menu_MouseTracking                             = QStyle.SH_Menu_MouseTracking #Mouse tracking in popup menus.
		MenuBar_MouseTracking                          = QStyle.SH_MenuBar_MouseTracking #Mouse tracking in menu bars.
		Menu_FillScreenWithScroll                      = QStyle.SH_Menu_FillScreenWithScroll #Whether scrolling popups should fill the screen as they are scrolled.
		Menu_SelectionWrap                             = QStyle.SH_Menu_SelectionWrap #Whether popups should allow the selections to wrap, that is when selection should the next item be the first item.
		ItemView_ChangeHighlightOnFocus                = QStyle.SH_ItemView_ChangeHighlightOnFocus #Gray out selected items when losing focus.
		Widget_ShareActivation                         = QStyle.SH_Widget_ShareActivation #Turn on sharing activation with floating modeless dialogs.
		TabBar_SelectMouseType                         = QStyle.SH_TabBar_SelectMouseType #Which type of mouse event should cause a tab to be selected.
		TabBar_PreferNoArrows                          = QStyle.SH_TabBar_PreferNoArrows #Whether a tab bar should suggest a size to prevent scoll arrows.
		ComboBox_Popup                                 = QStyle.SH_ComboBox_Popup #Allows popups as a combobox drop-down menu.
		Workspace_FillSpaceOnMaximize                  = QStyle.SH_Workspace_FillSpaceOnMaximize #The workspace should maximize the client area.
		TitleBar_NoBorder                              = QStyle.SH_TitleBar_NoBorder #The title bar has no border.
		ScrollBar_StopMouseOverSlider                  = QStyle.SH_ScrollBar_StopMouseOverSlider #Obsolete. Use SH_Slider_StopMouseOverSlider instead.
		Slider_StopMouseOverSlider                     = QStyle.SH_Slider_StopMouseOverSlider #Stops auto-repeat when the slider reaches the mouse position.
		BlinkCursorWhenTextSelected                    = QStyle.SH_BlinkCursorWhenTextSelected #Whether cursor should blink when text is selected.
		RichText_FullWidthSelection                    = QStyle.SH_RichText_FullWidthSelection #Whether richtext selections should extend to the full width of the document.
		GroupBox_TextLabelVerticalAlignment            = QStyle.SH_GroupBox_TextLabelVerticalAlignment #How to vertically align a group boxs text label.
		GroupBox_TextLabelColor                        = QStyle.SH_GroupBox_TextLabelColor #How to paint a group boxs text label.
		DialogButtons_DefaultButton                    = QStyle.SH_DialogButtons_DefaultButton #Which button gets the default status in a dialogs button widget.
		ToolBox_SelectedPageTitleBold                  = QStyle.SH_ToolBox_SelectedPageTitleBold #Boldness of the selected page title in a PySide.QtGui.QToolBox .
		LineEdit_PasswordCharacter                     = QStyle.SH_LineEdit_PasswordCharacter #The Unicode character to be used for passwords.
		Table_GridLineColor                            = QStyle.SH_Table_GridLineColor #The RGB value of the grid for a table.
		UnderlineShortcut                              = QStyle.SH_UnderlineShortcut #Whether shortcuts are underlined.
		SpellCheckUnderlineStyle                       = QStyle.SH_SpellCheckUnderlineStyle #A QTextCharFormat.UnderlineStyle value that specifies the way misspelled words should be underlined.
		SpinBox_AnimateButton                          = QStyle.SH_SpinBox_AnimateButton #Animate a click when up or down is pressed in a spin box.
		SpinBox_KeyPressAutoRepeatRate                 = QStyle.SH_SpinBox_KeyPressAutoRepeatRate #Auto-repeat interval for spinbox key presses.
		SpinBox_ClickAutoRepeatRate                    = QStyle.SH_SpinBox_ClickAutoRepeatRate #Auto-repeat interval for spinbox mouse clicks.
		SpinBox_ClickAutoRepeatThreshold               = QStyle.SH_SpinBox_ClickAutoRepeatThreshold #Auto-repeat threshold for spinbox mouse clicks.
		ToolTipLabel_Opacity                           = QStyle.SH_ToolTipLabel_Opacity #An integer indicating the opacity for the tip label, 0 is completely transparent, 255 is completely opaque.
		DrawMenuBarSeparator                           = QStyle.SH_DrawMenuBarSeparator #Indicates whether or not the menu bar draws separators.
		TitleBar_ModifyNotification                    = QStyle.SH_TitleBar_ModifyNotification #Indicates if the title bar should show a * for windows that are modified.
		Button_FocusPolicy                             = QStyle.SH_Button_FocusPolicy #The default focus policy for buttons.
		CustomBase                                     = QStyle.SH_CustomBase #Base value for custom style hints. Custom values must be greater than this value.
		MessageBox_UseBorderForButtonSpacing           = QStyle.SH_MessageBox_UseBorderForButtonSpacing #A boolean indicating what the to use the border of the buttons (computed as half the button height) for the spacing of the button in a message box.
		MessageBox_CenterButtons                       = QStyle.SH_MessageBox_CenterButtons #A boolean indicating whether the buttons in the message box should be centered or not (see QDialogButtonBox::setCentered()).
		MessageBox_TextInteractionFlags                = QStyle.SH_MessageBox_TextInteractionFlags #A boolean indicating if the text in a message box should allow user interfactions (e.g. selection) or not.
		TitleBar_AutoRaise                             = QStyle.SH_TitleBar_AutoRaise #A boolean indicating whether controls on a title bar ought to update when the mouse is over them.
		ToolButton_PopupDelay                          = QStyle.SH_ToolButton_PopupDelay #An int indicating the popup delay in milliseconds for menus attached to tool buttons.
		FocusFrame_Mask                                = QStyle.SH_FocusFrame_Mask #The mask of the focus frame.
		RubberBand_Mask                                = QStyle.SH_RubberBand_Mask #The mask of the rubber band.
		WindowFrame_Mask                               = QStyle.SH_WindowFrame_Mask #The mask of the window frame.
		SpinControls_DisableOnBounds                   = QStyle.SH_SpinControls_DisableOnBounds #Determines if the spin controls will shown as disabled when reaching the spin range boundary.
		Dial_BackgroundRole                            = QStyle.SH_Dial_BackgroundRole #Defines the styles preferred background role (as QPalette.ColorRole ) for a dial widget.
		ComboBox_LayoutDirection                       = QStyle.SH_ComboBox_LayoutDirection #The layout direction for the combo box. By default it should be the same as indicated by the QStyleOption.direction variable.
		ItemView_EllipsisLocation                      = QStyle.SH_ItemView_EllipsisLocation #The location where ellipses should be added for item text that is too long to fit in an view item.
		ItemView_ShowDecorationSelected                = QStyle.SH_ItemView_ShowDecorationSelected #When an item in an item view is selected, also highlight the branch or other decoration.
		ItemView_ActivateItemOnSingleClick             = QStyle.SH_ItemView_ActivateItemOnSingleClick #Emit the activated signal when the user single clicks on an item in an item in an item view. Otherwise the signal is emitted when the user double clicks on an item.
		Slider_AbsoluteSetButtons                      = QStyle.SH_Slider_AbsoluteSetButtons #Which mouse buttons cause a slider to set the value to the position clicked on.
		Slider_PageSetButtons                          = QStyle.SH_Slider_PageSetButtons #Which mouse buttons cause a slider to page step the value.
		TabBar_ElideMode                               = QStyle.SH_TabBar_ElideMode #The default eliding style for a tab bar.
		DialogButtonLayout                             = QStyle.SH_DialogButtonLayout #Controls how buttons are laid out in a PySide.QtGui.QDialogButtonBox , returns a QDialogButtonBox.ButtonLayout enum.
		WizardStyle                                    = QStyle.SH_WizardStyle #Controls the look and feel of a PySide.QtGui.QWizard . Returns a QWizard.WizardStyle enum.
		FormLayoutWrapPolicy                           = QStyle.SH_FormLayoutWrapPolicy #Provides a default for how rows are wrapped in a PySide.QtGui.QFormLayout . Returns a QFormLayout.RowWrapPolicy enum.
		FormLayoutFieldGrowthPolicy                    = QStyle.SH_FormLayoutFieldGrowthPolicy #Provides a default for how fields can grow in a PySide.QtGui.QFormLayout . Returns a QFormLayout.FieldGrowthPolicy enum.
		FormLayoutFormAlignment                        = QStyle.SH_FormLayoutFormAlignment #Provides a default for how a PySide.QtGui.QFormLayout aligns its contents within the available space. Returns a Qt.Alignment enum.
		FormLayoutLabelAlignment                       = QStyle.SH_FormLayoutLabelAlignment #Provides a default for how a PySide.QtGui.QFormLayout aligns labels within the available space. Returns a Qt.Alignment enum.
		ItemView_ArrowKeysNavigateIntoChildren         = QStyle.SH_ItemView_ArrowKeysNavigateIntoChildren #Controls whether the tree view will select the first child when it is exapanded and the right arrow key is pressed.
		ComboBox_PopupFrameStyle                       = QStyle.SH_ComboBox_PopupFrameStyle #The frame style used when drawing a combobox popup menu.
		DialogButtonBox_ButtonsHaveIcons               = QStyle.SH_DialogButtonBox_ButtonsHaveIcons #Indicates whether or not StandardButtons in PySide.QtGui.QDialogButtonBox should have icons or not.
		ItemView_MovementWithoutUpdatingSelection      = QStyle.SH_ItemView_MovementWithoutUpdatingSelection #The item view is able to indicate a current item without changing the selection.
		ToolTip_Mask                                   = QStyle.SH_ToolTip_Mask #The mask of a tool tip.
		FocusFrame_AboveWidget                         = QStyle.SH_FocusFrame_AboveWidget #The FocusFrame is stacked above the widget that it is focusing on.
		TextControl_FocusIndicatorTextCharFormat       = QStyle.SH_TextControl_FocusIndicatorTextCharFormat #Specifies the text format used to highlight focused anchors in rich text documents displayed for example in PySide.QtGui.QTextBrowser . The format has to be a PySide.QtGui.QTextCharFormat returned in the variant of the PySide.QtGui.QStyleHintReturnVariant return value. The QTextFormat.OutlinePen property is used for the outline and QTextFormat.BackgroundBrush for the background of the highlighted area.
		Menu_FlashTriggeredItem                        = QStyle.SH_Menu_FlashTriggeredItem #Flash triggered item.
		Menu_FadeOutOnHide                             = QStyle.SH_Menu_FadeOutOnHide #Fade out the menu instead of hiding it immediately.
		TabWidget_DefaultTabPosition                   = QStyle.SH_TabWidget_DefaultTabPosition #Default position of the tab bar in a tab widget.
		ToolBar_Movable                                = QStyle.SH_ToolBar_Movable #Determines if the tool bar is movable by default.
		ItemView_PaintAlternatingRowColorsForEmptyArea = QStyle.SH_ItemView_PaintAlternatingRowColorsForEmptyArea #Whether PySide.QtGui.QTreeView paints alternating row colors for the area that does not have any items.
		Menu_Mask                                      = QStyle.SH_Menu_Mask #The mask for a popup menu.
		ItemView_DrawDelegateFrame                     = QStyle.SH_ItemView_DrawDelegateFrame #Determines if there should be a frame for a delegate widget.
		TabBar_CloseButtonPosition                     = QStyle.SH_TabBar_CloseButtonPosition #Determines the position of the close button on a tab in a tab bar.
		DockWidget_ButtonsHaveFrame                    = QStyle.SH_DockWidget_ButtonsHaveFrame #Determines if dockwidget buttons should have frames. Default is true.
		ToolButtonStyle                                = QStyle.SH_ToolButtonStyle #Determines the default system style for tool buttons that uses Qt.ToolButtonFollowStyle .
		RequestSoftwareInputPanel                      = QStyle.SH_RequestSoftwareInputPanel #Determines when a software input panel should be requested by input widgets. Returns an enum of type QStyle.RequestSoftwareInputPanel .
	########################################################################
	class PixelMetric:
		ButtonMargin                   = QStyle.PM_ButtonMargin #Amount of whitespace between push button labels and the frame.
		DockWidgetTitleBarButtonMargin = QStyle.PM_DockWidgetTitleBarButtonMargin #Amount of whitespace between dock widgets title bar button labels and the frame.
		ButtonDefaultIndicator         = QStyle.PM_ButtonDefaultIndicator #Width of the default-button indicator frame.
		MenuButtonIndicator            = QStyle.PM_MenuButtonIndicator #Width of the menu button indicator proportional to the widget height.
		ButtonShiftHorizontal          = QStyle.PM_ButtonShiftHorizontal #Horizontal contents shift of a button when the button is down.
		ButtonShiftVertical            = QStyle.PM_ButtonShiftVertical #Vertical contents shift of a button when the button is down.
		DefaultFrameWidth              = QStyle.PM_DefaultFrameWidth #Default frame width (usually 2).
		SpinBoxFrameWidth              = QStyle.PM_SpinBoxFrameWidth #Frame width of a spin box, defaults to PM_DefaultFrameWidth .
		ComboBoxFrameWidth             = QStyle.PM_ComboBoxFrameWidth #Frame width of a combo box, defaults to PM_DefaultFrameWidth .
		MDIFrameWidth                  = QStyle.PM_MDIFrameWidth #Obsolete. Use PM_MdiSubWindowFrameWidth instead.
		MdiSubWindowFrameWidth         = QStyle.PM_MdiSubWindowFrameWidth #Frame width of an MDI window.
		MDIMinimizedWidth              = QStyle.PM_MDIMinimizedWidth #Obsolete. Use PM_MdiSubWindowMinimizedWidth instead.
		MdiSubWindowMinimizedWidth     = QStyle.PM_MdiSubWindowMinimizedWidth #Width of a minimized MDI window.
		LayoutLeftMargin               = QStyle.PM_LayoutLeftMargin #Default left margin for a PySide.QtGui.QLayout .
		LayoutTopMargin                = QStyle.PM_LayoutTopMargin #Default top margin for a PySide.QtGui.QLayout .
		LayoutRightMargin              = QStyle.PM_LayoutRightMargin #Default right margin for a PySide.QtGui.QLayout .
		LayoutBottomMargin             = QStyle.PM_LayoutBottomMargin #Default bottom margin for a PySide.QtGui.QLayout .
		LayoutHorizontalSpacing        = QStyle.PM_LayoutHorizontalSpacing #Default horizontal spacing for a PySide.QtGui.QLayout .
		LayoutVerticalSpacing          = QStyle.PM_LayoutVerticalSpacing #Default vertical spacing for a PySide.QtGui.QLayout .
		MaximumDragDistance            = QStyle.PM_MaximumDragDistance #The maximum allowed distance between the mouse and a scrollbar when dragging. Exceeding the specified distance will cause the slider to jump back to the original position; a value of -1 disables this behavior.
		ScrollBarExtent                = QStyle.PM_ScrollBarExtent #Width of a vertical scroll bar and the height of a horizontal scroll bar.
		ScrollBarSliderMin             = QStyle.PM_ScrollBarSliderMin #The minimum height of a vertical scroll bars slider and the minimum width of a horizontal scroll bars slider.
		SliderThickness                = QStyle.PM_SliderThickness #Total slider thickness.
		SliderControlThickness         = QStyle.PM_SliderControlThickness #Thickness of the slider handle.
		SliderLength                   = QStyle.PM_SliderLength #Length of the slider.
		SliderTickmarkOffset           = QStyle.PM_SliderTickmarkOffset #The offset between the tickmarks and the slider.
		SliderSpaceAvailable           = QStyle.PM_SliderSpaceAvailable #The available space for the slider to move.
		DockWidgetSeparatorExtent      = QStyle.PM_DockWidgetSeparatorExtent #Width of a separator in a horizontal dock window and the height of a separator in a vertical dock window.
		DockWidgetHandleExtent         = QStyle.PM_DockWidgetHandleExtent #Width of the handle in a horizontal dock window and the height of the handle in a vertical dock window.
		DockWidgetFrameWidth           = QStyle.PM_DockWidgetFrameWidth #Frame width of a dock window.
		DockWidgetTitleMargin          = QStyle.PM_DockWidgetTitleMargin #Margin of the dock window title.
		MenuBarPanelWidth              = QStyle.PM_MenuBarPanelWidth #Frame width of a menu bar, defaults to PM_DefaultFrameWidth .
		MenuBarItemSpacing             = QStyle.PM_MenuBarItemSpacing #Spacing between menu bar items.
		MenuBarHMargin                 = QStyle.PM_MenuBarHMargin #Spacing between menu bar items and left/right of bar.
		MenuBarVMargin                 = QStyle.PM_MenuBarVMargin #Spacing between menu bar items and top/bottom of bar.
		ToolBarFrameWidth              = QStyle.PM_ToolBarFrameWidth #Width of the frame around toolbars.
		ToolBarHandleExtent            = QStyle.PM_ToolBarHandleExtent #Width of a toolbar handle in a horizontal toolbar and the height of the handle in a vertical toolbar.
		ToolBarItemMargin              = QStyle.PM_ToolBarItemMargin #Spacing between the toolbar frame and the items.
		ToolBarItemSpacing             = QStyle.PM_ToolBarItemSpacing #Spacing between toolbar items.
		ToolBarSeparatorExtent         = QStyle.PM_ToolBarSeparatorExtent #Width of a toolbar separator in a horizontal toolbar and the height of a separator in a vertical toolbar.
		ToolBarExtensionExtent         = QStyle.PM_ToolBarExtensionExtent #Width of a toolbar extension button in a horizontal toolbar and the height of the button in a vertical toolbar.
		TabBarTabOverlap               = QStyle.PM_TabBarTabOverlap #Number of pixels the tabs should overlap. (Currently only used in styles, not inside of PySide.QtGui.QTabBar )
		TabBarTabHSpace                = QStyle.PM_TabBarTabHSpace #Extra space added to the tab width.
		TabBarTabVSpace                = QStyle.PM_TabBarTabVSpace #Extra space added to the tab height.
		TabBarBaseHeight               = QStyle.PM_TabBarBaseHeight #Height of the area between the tab bar and the tab pages.
		TabBarBaseOverlap              = QStyle.PM_TabBarBaseOverlap #Number of pixels the tab bar overlaps the tab bar base.
		TabBarScrollButtonWidt         = QStyle.PM_TabBarScrollButtonWidth #
		TabBarTabShiftHorizontal       = QStyle.PM_TabBarTabShiftHorizontal #Horizontal pixel shift when a tab is selected.
		TabBarTabShiftVertical         = QStyle.PM_TabBarTabShiftVertical #Vertical pixel shift when a tab is selected.
		ProgressBarChunkWidth          = QStyle.PM_ProgressBarChunkWidth #Width of a chunk in a progress bar indicator.
		SplitterWidth                  = QStyle.PM_SplitterWidth #Width of a splitter.
		TitleBarHeight                 = QStyle.PM_TitleBarHeight #Height of the title bar.
		IndicatorWidth                 = QStyle.PM_IndicatorWidth #Width of a check box indicator.
		IndicatorHeight                = QStyle.PM_IndicatorHeight #Height of a checkbox indicator.
		ExclusiveIndicatorWidth        = QStyle.PM_ExclusiveIndicatorWidth #Width of a radio button indicator.
		ExclusiveIndicatorHeight       = QStyle.PM_ExclusiveIndicatorHeight #Height of a radio button indicator.
		MenuPanelWidth                 = QStyle.PM_MenuPanelWidth #Border width (applied on all sides) for a PySide.QtGui.QMenu .
		MenuHMargin                    = QStyle.PM_MenuHMargin #Additional border (used on left and right) for a PySide.QtGui.QMenu .
		MenuVMargin                    = QStyle.PM_MenuVMargin #Additional border (used for bottom and top) for a PySide.QtGui.QMenu .
		MenuScrollerHeight             = QStyle.PM_MenuScrollerHeight #Height of the scroller area in a PySide.QtGui.QMenu .
		MenuTearoffHeight              = QStyle.PM_MenuTearoffHeight #Height of a tear off area in a PySide.QtGui.QMenu .
		MenuDesktopFrameWidth          = QStyle.PM_MenuDesktopFrameWidth #The frame width for the menu on the desktop.
		HeaderMarkSize                 = QStyle.PM_HeaderMarkSize #The size of the sort indicator in a header.
		HeaderGripMargin               = QStyle.PM_HeaderGripMargin #The size of the resize grip in a header.
		HeaderMargin                   = QStyle.PM_HeaderMargin #The size of the margin between the sort indicator and the text.
		SpinBoxSliderHeight            = QStyle.PM_SpinBoxSliderHeight #The height of the optional spin box slider.
		ToolBarIconSize                = QStyle.PM_ToolBarIconSize #Default tool bar icon size
		SmallIconSize                  = QStyle.PM_SmallIconSize #Default small icon size
		LargeIconSize                  = QStyle.PM_LargeIconSize #Default large icon size
		FocusFrameHMargin              = QStyle.PM_FocusFrameHMargin #Horizontal margin that the focus frame will outset the widget by.
		FocusFrameVMargin              = QStyle.PM_FocusFrameVMargin #Vertical margin that the focus frame will outset the widget by.
		IconViewIconSize               = QStyle.PM_IconViewIconSize #The default size for icons in an icon view.
		ListViewIconSize               = QStyle.PM_ListViewIconSize #The default size for icons in a list view.
		ToolTipLabelFrameWidth         = QStyle.PM_ToolTipLabelFrameWidth #The frame width for a tool tip label.
		CheckBoxLabelSpacing           = QStyle.PM_CheckBoxLabelSpacing #The spacing between a check box indicator and its label.
		RadioButtonLabelSpacing        = QStyle.PM_RadioButtonLabelSpacing #The spacing between a radio button indicator and its label.
		TabBarIconSize                 = QStyle.PM_TabBarIconSize #The default icon size for a tab bar.
		SizeGripSize                   = QStyle.PM_SizeGripSize #The size of a size grip.
		MessageBoxIconSize             = QStyle.PM_MessageBoxIconSize #The size of the standard icons in a message box
		ButtonIconSize                 = QStyle.PM_ButtonIconSize #The default size of button icons
		TextCursorWidth                = QStyle.PM_TextCursorWidth #The width of the cursor in a line edit or text edit
		TabBar_ScrollButtonOverlap     = QStyle.PM_TabBar_ScrollButtonOverlap #The distance between the left and right buttons in a tab bar.
		TabCloseIndicatorWidth         = QStyle.PM_TabCloseIndicatorWidth #The default width of a close button on a tab in a tab bar.
		TabCloseIndicatorHeight        = QStyle.PM_TabCloseIndicatorHeight #The default height of a close button on a tab in a tab bar.
		CustomBase                     = QStyle.PM_CustomBase #Base value for custom pixel metrics. Custom values must be greater than this value.
	########################################################################
	class StandardPixmap:
		TitleBarMinButton                = QStyle.SP_TitleBarMinButton #Minimize button on title bars (e.g., in PySide.QtGui.QMdiSubWindow ).
		TitleBarMenuButton               = QStyle.SP_TitleBarMenuButton #Menu button on a title bar.
		TitleBarMaxButton                = QStyle.SP_TitleBarMaxButton #Maximize button on title bars.
		TitleBarCloseButton              = QStyle.SP_TitleBarCloseButton #Close button on title bars.
		TitleBarNormalButton             = QStyle.SP_TitleBarNormalButton #Normal (restore) button on title bars.
		TitleBarShadeButton              = QStyle.SP_TitleBarShadeButton #Shade button on title bars.
		TitleBarUnshadeButton            = QStyle.SP_TitleBarUnshadeButton #Unshade button on title bars.
		TitleBarContextHelpButton        = QStyle.SP_TitleBarContextHelpButton #The Context help button on title bars.
		MessageBoxInformation            = QStyle.SP_MessageBoxInformation #The information icon.
		MessageBoxWarning                = QStyle.SP_MessageBoxWarning #The warning icon.
		MessageBoxCritical               = QStyle.SP_MessageBoxCritical #The critical icon.
		MessageBoxQuestion               = QStyle.SP_MessageBoxQuestion #The question icon.
		DesktopIcon                      = QStyle.SP_DesktopIcon #The desktop icon.
		TrashIcon                        = QStyle.SP_TrashIcon #The trash icon.
		ComputerIcon                     = QStyle.SP_ComputerIcon #The My computer icon.
		DriveFDIcon                      = QStyle.SP_DriveFDIcon #The floppy icon.
		DriveHDIcon                      = QStyle.SP_DriveHDIcon #The harddrive icon.
		DriveCDIcon                      = QStyle.SP_DriveCDIcon #The CD icon.
		DriveDVDIcon                     = QStyle.SP_DriveDVDIcon #The DVD icon.
		DriveNetIcon                     = QStyle.SP_DriveNetIcon #The network icon.
		DirHomeIcon                      = QStyle.SP_DirHomeIcon #The home directory icon.
		DirOpenIcon                      = QStyle.SP_DirOpenIcon #The open directory icon.
		DirClosedIcon                    = QStyle.SP_DirClosedIcon #The closed directory icon.
		DirIcon                          = QStyle.SP_DirIcon #The directory icon.
		DirLinkIcon                      = QStyle.SP_DirLinkIcon #The link to directory icon.
		FileIcon                         = QStyle.SP_FileIcon #The file icon.
		FileLinkIcon                     = QStyle.SP_FileLinkIcon #The link to file icon.
		FileDialogStart                  = QStyle.SP_FileDialogStart #The start icon in a file dialog.
		FileDialogEnd                    = QStyle.SP_FileDialogEnd #The end icon in a file dialog.
		FileDialogToParent               = QStyle.SP_FileDialogToParent #The parent directory icon in a file dialog.
		FileDialogNewFolder              = QStyle.SP_FileDialogNewFolder #The create new folder icon in a file dialog.
		FileDialogDetailedView           = QStyle.SP_FileDialogDetailedView #The detailed view icon in a file dialog.
		FileDialogInfoView               = QStyle.SP_FileDialogInfoView #The file info icon in a file dialog.
		FileDialogContentsView           = QStyle.SP_FileDialogContentsView #The contents view icon in a file dialog.
		FileDialogListView               = QStyle.SP_FileDialogListView #The list view icon in a file dialog.
		FileDialogBack                   = QStyle.SP_FileDialogBack #The back arrow in a file dialog.
		DockWidgetCloseButton            = QStyle.SP_DockWidgetCloseButton #Close button on dock windows (see also PySide.QtGui.QDockWidget ).
		ToolBarHorizontalExtensionButton = QStyle.SP_ToolBarHorizontalExtensionButton #Extension button for horizontal toolbars.
		ToolBarVerticalExtensionButton   = QStyle.SP_ToolBarVerticalExtensionButton #Extension button for vertical toolbars.
		DialogOkButton                   = QStyle.SP_DialogOkButton #Icon for a standard OK button in a PySide.QtGui.QDialogButtonBox .
		DialogCancelButton               = QStyle.SP_DialogCancelButton #Icon for a standard Cancel button in a PySide.QtGui.QDialogButtonBox .
		DialogHelpButton                 = QStyle.SP_DialogHelpButton #Icon for a standard Help button in a PySide.QtGui.QDialogButtonBox .
		DialogOpenButton                 = QStyle.SP_DialogOpenButton #Icon for a standard Open button in a PySide.QtGui.QDialogButtonBox .
		DialogSaveButton                 = QStyle.SP_DialogSaveButton #Icon for a standard Save button in a PySide.QtGui.QDialogButtonBox .
		DialogCloseButton                = QStyle.SP_DialogCloseButton #Icon for a standard Close button in a PySide.QtGui.QDialogButtonBox .
		DialogApplyButton                = QStyle.SP_DialogApplyButton #Icon for a standard Apply button in a PySide.QtGui.QDialogButtonBox .
		DialogResetButton                = QStyle.SP_DialogResetButton #Icon for a standard Reset button in a PySide.QtGui.QDialogButtonBox .
		DialogDiscardButton              = QStyle.SP_DialogDiscardButton #Icon for a standard Discard button in a PySide.QtGui.QDialogButtonBox .
		DialogYesButton                  = QStyle.SP_DialogYesButton #Icon for a standard Yes button in a PySide.QtGui.QDialogButtonBox .
		DialogNoButton                   = QStyle.SP_DialogNoButton #Icon for a standard No button in a PySide.QtGui.QDialogButtonBox .
		ArrowUp                          = QStyle.SP_ArrowUp #Icon arrow pointing up.
		ArrowDown                        = QStyle.SP_ArrowDown #Icon arrow pointing down.
		ArrowLeft                        = QStyle.SP_ArrowLeft #Icon arrow pointing left.
		ArrowRight                       = QStyle.SP_ArrowRight #Icon arrow pointing right.
		ArrowBack                        = QStyle.SP_ArrowBack #Equivalent to SP_ArrowLeft when the current layout direction is Qt.LeftToRight , otherwise SP_ArrowRight .
		ArrowForward                     = QStyle.SP_ArrowForward #Equivalent to SP_ArrowRight when the current layout direction is Qt.LeftToRight , otherwise SP_ArrowLeft .
		CommandLink                      = QStyle.SP_CommandLink #Icon used to indicate a Vista style command link glyph.
		VistaShield                      = QStyle.SP_VistaShield #Icon used to indicate UAC prompts on Windows Vista. This will return a null pixmap or icon on all other platforms.
		BrowserReload                    = QStyle.SP_BrowserReload #Icon indicating that the current page should be reloaded.
		BrowserStop                      = QStyle.SP_BrowserStop #Icon indicating that the page loading should stop.
		MediaPlay                        = QStyle.SP_MediaPlay #Icon indicating that media should begin playback.
		MediaStop                        = QStyle.SP_MediaStop #Icon indicating that media should stop playback.
		MediaPause                       = QStyle.SP_MediaPause #Icon indicating that media should pause playback.
		MediaSkipForward                 = QStyle.SP_MediaSkipForward #Icon indicating that media should skip forward.
		MediaSkipBackward                = QStyle.SP_MediaSkipBackward #Icon indicating that media should skip backward.
		MediaSeekForward                 = QStyle.SP_MediaSeekForward #Icon indicating that media should seek forward.
		MediaSeekBackward                = QStyle.SP_MediaSeekBackward #Icon indicating that media should seek backward.
		MediaVolume                      = QStyle.SP_MediaVolume #Icon indicating a volume control.
		MediaVolumeMuted                 = QStyle.SP_MediaVolumeMuted #Icon indicating a muted volume control.
		CustomBase                       = QStyle.SP_CustomBase #Base value for custom standard pixmaps; custom values must be greater than this value.
	########################################################################
	class ControlElement:
		PushButton            = QStyle.CE_PushButton #A PySide.QtGui.QPushButton , draws CE_PushButtonBevel , CE_PushButtonLabel and PE_FrameFocusRect .
		PushButtonBevel       = QStyle.CE_PushButtonBevel #The bevel and default indicator of a PySide.QtGui.QPushButton .
		PushButtonLabel       = QStyle.CE_PushButtonLabel #The label (an icon with text or pixmap) of a PySide.QtGui.QPushButton .
		DockWidgetTitle       = QStyle.CE_DockWidgetTitle #Dock window title.
		Splitter              = QStyle.CE_Splitter #Splitter handle; see also PySide.QtGui.QSplitter .
		CheckBox              = QStyle.CE_CheckBox #A PySide.QtGui.QCheckBox , draws a PE_IndicatorCheckBox , a CE_CheckBoxLabel and a PE_FrameFocusRect .
		CheckBoxLabel         = QStyle.CE_CheckBoxLabel #The label (text or pixmap) of a PySide.QtGui.QCheckBox .
		RadioButton           = QStyle.CE_RadioButton #A PySide.QtGui.QRadioButton , draws a PE_IndicatorRadioButton , a CE_RadioButtonLabel and a PE_FrameFocusRect .
		RadioButtonLabel      = QStyle.CE_RadioButtonLabel #The label (text or pixmap) of a PySide.QtGui.QRadioButton .
		TabBarTab             = QStyle.CE_TabBarTab #The tab and label within a PySide.QtGui.QTabBar .
		TabBarTabShape        = QStyle.CE_TabBarTabShape #The tab shape within a tab bar.
		TabBarTabLabel        = QStyle.CE_TabBarTabLabel #The label within a tab.
		ProgressBar           = QStyle.CE_ProgressBar #A PySide.QtGui.QProgressBar , draws CE_ProgressBarGroove , CE_ProgressBarContents and CE_ProgressBarLabel .
		ProgressBarGroove     = QStyle.CE_ProgressBarGroove #The groove where the progress indicator is drawn in a PySide.QtGui.QProgressBar .
		ProgressBarContents   = QStyle.CE_ProgressBarContents #The progress indicator of a PySide.QtGui.QProgressBar .
		ProgressBarLabel      = QStyle.CE_ProgressBarLabel #The text label of a PySide.QtGui.QProgressBar .
		ToolButtonLabel       = QStyle.CE_ToolButtonLabel #A tool buttons label.
		MenuBarItem           = QStyle.CE_MenuBarItem #A menu item in a PySide.QtGui.QMenuBar .
		MenuBarEmptyArea      = QStyle.CE_MenuBarEmptyArea #The empty area of a PySide.QtGui.QMenuBar .
		MenuItem              = QStyle.CE_MenuItem #A menu item in a PySide.QtGui.QMenu .
		MenuScroller          = QStyle.CE_MenuScroller #Scrolling areas in a PySide.QtGui.QMenu when the style supports scrolling.
		MenuTearoff           = QStyle.CE_MenuTearoff #A menu item representing the tear off section of a PySide.QtGui.QMenu .
		MenuEmptyArea         = QStyle.CE_MenuEmptyArea #The area in a menu without menu items.
		MenuHMargin           = QStyle.CE_MenuHMargin #The horizontal extra space on the left/right of a menu.
		MenuVMargin           = QStyle.CE_MenuVMargin #The vertical extra space on the top/bottom of a menu.
		ToolBoxTab            = QStyle.CE_ToolBoxTab #The toolboxs tab and label within a PySide.QtGui.QToolBox .
		SizeGrip              = QStyle.CE_SizeGrip #Window resize handle; see also PySide.QtGui.QSizeGrip .
		Header                = QStyle.CE_Header #A header.
		HeaderSection         = QStyle.CE_HeaderSection #A header section.
		HeaderLabel           = QStyle.CE_HeaderLabel #The headers label.
		ScrollBarAddLine      = QStyle.CE_ScrollBarAddLine #Scroll bar line increase indicator. (i.e., scroll down); see also PySide.QtGui.QScrollBar .
		ScrollBarSubLine      = QStyle.CE_ScrollBarSubLine #Scroll bar line decrease indicator (i.e., scroll up).
		ScrollBarAddPage      = QStyle.CE_ScrollBarAddPage #Scolllbar page increase indicator (i.e., page down).
		ScrollBarSubPage      = QStyle.CE_ScrollBarSubPage #Scroll bar page decrease indicator (i.e., page up).
		ScrollBarSlider       = QStyle.CE_ScrollBarSlider #Scroll bar slider.
		ScrollBarFirst        = QStyle.CE_ScrollBarFirst #Scroll bar first line indicator (i.e., home).
		ScrollBarLast         = QStyle.CE_ScrollBarLast #Scroll bar last line indicator (i.e., end).
		RubberBand            = QStyle.CE_RubberBand #Rubber band used in for example an icon view.
		FocusFrame            = QStyle.CE_FocusFrame #Focus frame that is style controlled.
		ItemViewItem          = QStyle.CE_ItemViewItem #An item inside an item view.
		CustomBase            = QStyle.CE_CustomBase #Base value for custom control elements; custom values must be greater than this value.
		ComboBoxLabel         = QStyle.CE_ComboBoxLabel #The label of a non-editable PySide.QtGui.QComboBox .
		ToolBar               = QStyle.CE_ToolBar #A toolbar like PySide.QtGui.QToolBar .
		ToolBoxTabShape       = QStyle.CE_ToolBoxTabShape #The toolboxs tab shape.
		ToolBoxTabLabel       = QStyle.CE_ToolBoxTabLabel #The toolboxs tab label.
		HeaderEmptyArea       = QStyle.CE_HeaderEmptyArea #The area of a header view where there are no header sections.
		ShapedFrame           = QStyle.CE_ShapedFrame #The frame with the shape specified in the PySide.QtGui.QStyleOptionFrameV3 ; see
	########################################################################
	class SubControl:
		NONE                      = QStyle.SC_None #Special value that matches no other sub control.
		ScrollBarAddLine          = QStyle.SC_ScrollBarAddLine #Scroll bar add line (i.e., down/right arrow); see also PySide.QtGui.QScrollBar .
		ScrollBarSubLine          = QStyle.SC_ScrollBarSubLine #Scroll bar sub line (i.e., up/left arrow).
		ScrollBarAddPage          = QStyle.SC_ScrollBarAddPage #Scroll bar add page (i.e., page down).
		ScrollBarSubPage          = QStyle.SC_ScrollBarSubPage #Scroll bar sub page (i.e., page up).
		ScrollBarFirst            = QStyle.SC_ScrollBarFirst #Scroll bar first line (i.e., home).
		ScrollBarLast             = QStyle.SC_ScrollBarLast #Scroll bar last line (i.e., end).
		ScrollBarSlider           = QStyle.SC_ScrollBarSlider #Scroll bar slider handle.
		ScrollBarGroove           = QStyle.SC_ScrollBarGroove #Special sub-control which contains the area in which the slider handle may move.
		SpinBoxUp                 = QStyle.SC_SpinBoxUp #Spin widget up/increase; see also PySide.QtGui.QSpinBox .
		SpinBoxDown               = QStyle.SC_SpinBoxDown #Spin widget down/decrease.
		SpinBoxFrame              = QStyle.SC_SpinBoxFrame #Spin widget frame.
		SpinBoxEditField          = QStyle.SC_SpinBoxEditField #Spin widget edit field.
		ComboBoxEditField         = QStyle.SC_ComboBoxEditField #Combobox edit field; see also PySide.QtGui.QComboBox .
		ComboBoxArrow             = QStyle.SC_ComboBoxArrow #Combobox arrow button.
		ComboBoxFrame             = QStyle.SC_ComboBoxFrame #Combobox frame.
		ComboBoxListBoxPopup      = QStyle.SC_ComboBoxListBoxPopup #The reference rectangle for the combobox popup. Used to calculate the position of the popup.
		SliderGroove              = QStyle.SC_SliderGroove #Special sub-control which contains the area in which the slider handle may move.
		SliderHandle              = QStyle.SC_SliderHandle #Slider handle.
		SliderTickmarks           = QStyle.SC_SliderTickmarks #Slider tickmarks.
		ToolButton                = QStyle.SC_ToolButton #Tool button (see also PySide.QtGui.QToolButton ).
		ToolButtonMenu            = QStyle.SC_ToolButtonMenu #Sub-control for opening a popup menu in a tool button; see also Q3PopupMenu .
		TitleBarSysMenu           = QStyle.SC_TitleBarSysMenu #System menu button (i.e., restore, close, etc.).
		TitleBarMinButton         = QStyle.SC_TitleBarMinButton #Minimize button.
		TitleBarMaxButton         = QStyle.SC_TitleBarMaxButton #Maximize button.
		TitleBarCloseButton       = QStyle.SC_TitleBarCloseButton #Close button.
		TitleBarLabel             = QStyle.SC_TitleBarLabel #Window title label.
		TitleBarNormalButton      = QStyle.SC_TitleBarNormalButton #Normal (restore) button.
		TitleBarShadeButton       = QStyle.SC_TitleBarShadeButton #Shade button.
		TitleBarUnshadeButton     = QStyle.SC_TitleBarUnshadeButton #Unshade button.
		TitleBarContextHelpButton = QStyle.SC_TitleBarContextHelpButton #Context Help button.
		DialHandle                = QStyle.SC_DialHandle #The handle of the dial (i.e. what you use to control the dial).
		DialGroove                = QStyle.SC_DialGroove #The groove for the dial.
		DialTickmarks             = QStyle.SC_DialTickmarks #The tickmarks for the dial.
		GroupBoxFrame             = QStyle.SC_GroupBoxFrame #The frame of a group box.
		GroupBoxLabel             = QStyle.SC_GroupBoxLabel #The title of a group box.
		GroupBoxCheckBox          = QStyle.SC_GroupBoxCheckBox #The optional check box of a group box.
		GroupBoxContents          = QStyle.SC_GroupBoxContents #The group box contents.
		MdiNormalButton           = QStyle.SC_MdiNormalButton #The normal button for a MDI subwindow in the menu bar.
		MdiMinButton              = QStyle.SC_MdiMinButton #The minimize button for a MDI subwindow in the menu bar.
		MdiCloseButton            = QStyle.SC_MdiCloseButton #The close button for a MDI subwindow in the menu bar.
		All                       = QStyle.SC_All #Special value that matches all sub-controls.
	########################################################################
	class ContentsType:
		CheckBox      = QStyle.CT_CheckBox #A check box, like PySide.QtGui.QCheckBox .
		ComboBox      = QStyle.CT_ComboBox #A combo box, like PySide.QtGui.QComboBox .
		HeaderSection = QStyle.CT_HeaderSection #A header section, like QHeader .
		LineEdit      = QStyle.CT_LineEdit #A line edit, like PySide.QtGui.QLineEdit .
		Menu          = QStyle.CT_Menu #A menu, like PySide.QtGui.QMenu .
		MenuBar       = QStyle.CT_MenuBar #A menu bar, like PySide.QtGui.QMenuBar .
		MenuBarItem   = QStyle.CT_MenuBarItem #A menu bar item, like the buttons in a PySide.QtGui.QMenuBar .
		MenuItem      = QStyle.CT_MenuItem #A menu item, like QMenuItem .
		ProgressBar   = QStyle.CT_ProgressBar #A progress bar, like PySide.QtGui.QProgressBar .
		PushButton    = QStyle.CT_PushButton #A push button, like PySide.QtGui.QPushButton .
		RadioButton   = QStyle.CT_RadioButton #A radio button, like PySide.QtGui.QRadioButton .
		SizeGrip      = QStyle.CT_SizeGrip #A size grip, like PySide.QtGui.QSizeGrip .
		Slider        = QStyle.CT_Slider #A slider, like PySide.QtGui.QSlider .
		ScrollBar     = QStyle.CT_ScrollBar #A scroll bar, like PySide.QtGui.QScrollBar .
		SpinBox       = QStyle.CT_SpinBox #A spin box, like PySide.QtGui.QSpinBox .
		Splitter      = QStyle.CT_Splitter #A splitter, like PySide.QtGui.QSplitter .
		TabBarTab     = QStyle.CT_TabBarTab #A tab on a tab bar, like PySide.QtGui.QTabBar .
		TabWidget     = QStyle.CT_TabWidget #A tab widget, like PySide.QtGui.QTabWidget .
		ToolButton    = QStyle.CT_ToolButton #A tool button, like PySide.QtGui.QToolButton .
		GroupBox      = QStyle.CT_GroupBox #A group box, like PySide.QtGui.QGroupBox .
		ItemViewItem  = QStyle.CT_ItemViewItem #An item inside an item view.
		CustomBase    = QStyle.CT_CustomBase #Base value for custom contents types. Custom values must be greater than this value.
		MdiControls   = QStyle.CT_MdiControls #The minimize, normal, and close button in the menu bar for a maximized MDI subwindow.
	########################################################################
	class StateFlag:
		State_None                = QStyle.State_None #Indicates that the widget does not have a state.
		State_Active              = QStyle.State_Active #Indicates that the widget is active.
		State_AutoRaise           = QStyle.State_AutoRaise #Used to indicate if auto-raise appearance should be usd on a tool button.
		State_Children            = QStyle.State_Children #Used to indicate if an item view branch has children.
		State_DownArrow           = QStyle.State_DownArrow #Used to indicate if a down arrow should be visible on the widget.
		State_Editing             = QStyle.State_Editing #Used to indicate if an editor is opened on the widget.
		State_Enabled             = QStyle.State_Enabled #Used to indicate if the widget is enabled.
		State_HasFocus            = QStyle.State_HasFocus #Used to indicate if the widget has focus.
		State_Horizontal          = QStyle.State_Horizontal #Used to indicate if the widget is laid out horizontally, for example. a tool bar.
		State_KeyboardFocusChange = QStyle.State_KeyboardFocusChange #Used to indicate if the focus was changed with the keyboard, e.g., tab, backtab or shortcut.
		State_MouseOver           = QStyle.State_MouseOver #Used to indicate if the widget is under the mouse.
		State_NoChange            = QStyle.State_NoChange #Used to indicate a tri-state checkbox.
		State_Off                 = QStyle.State_Off #Used to indicate if the widget is not checked.
		State_On                  = QStyle.State_On #Used to indicate if the widget is checked.
		State_Raised              = QStyle.State_Raised #Used to indicate if a button is raised.
		State_ReadOnly            = QStyle.State_ReadOnly #Used to indicate if a widget is read-only.
		State_Selected            = QStyle.State_Selected #Used to indicate if a widget is selected.
		State_Item                = QStyle.State_Item #Used by item views to indicate if a horizontal branch should be drawn.
		State_Open                = QStyle.State_Open #Used by item views to indicate if the tree branch is open.
		State_Sibling             = QStyle.State_Sibling #Used by item views to indicate if a vertical line needs to be drawn (for siblings).
		State_Sunken              = QStyle.State_Sunken #Used to indicate if the widget is sunken or pressed.
		State_UpArrow             = QStyle.State_UpArrow #Used to indicate if an up arrow should be visible on the widget.
		State_Mini                = QStyle.State_Mini #Used to indicate a mini style Mac widget or button.
		State_Small               = QStyle.State_Small #Used to indicate a small style Mac widget or button.
	########################################################################
	class ComplexControl:
		SpinBox     = QStyle.CC_SpinBox #A spinbox, like PySide.QtGui.QSpinBox .
		ComboBox    = QStyle.CC_ComboBox #A combobox, like PySide.QtGui.QComboBox .
		ScrollBar   = QStyle.CC_ScrollBar #A scroll bar, like PySide.QtGui.QScrollBar .
		Slider      = QStyle.CC_Slider #A slider, like PySide.QtGui.QSlider .
		ToolButton  = QStyle.CC_ToolButton #A tool button, like PySide.QtGui.QToolButton .
		TitleBar    = QStyle.CC_TitleBar #A Title bar, like those used in PySide.QtGui.QMdiSubWindow .
		GroupBox    = QStyle.CC_GroupBox #A group box, like PySide.QtGui.QGroupBox .
		Dial        = QStyle.CC_Dial #A dial, like PySide.QtGui.QDial .
		MdiControls = QStyle.CC_MdiControls #The minimize, close, and normal button in the menu bar for a maximized MDI subwindow.
		CustomBase  = QStyle.CC_CustomBase #Base value for custom complex controls. Custom values must be greater than this value.
	########################################################################
	class SubElement:
		PushButtonContents         = QStyle.SE_PushButtonContents #Area containing the label (icon with text or pixmap).
		PushButtonFocusRect        = QStyle.SE_PushButtonFocusRect #Area for the focus rect (usually larger than the contents rect).
		PushButtonLayoutItem       = QStyle.SE_PushButtonLayoutItem #Area that counts for the parent layout.
		CheckBoxIndicator          = QStyle.SE_CheckBoxIndicator #Area for the state indicator (e.g., check mark).
		CheckBoxContents           = QStyle.SE_CheckBoxContents #Area for the label (text or pixmap).
		CheckBoxFocusRect          = QStyle.SE_CheckBoxFocusRect #Area for the focus indicator.
		CheckBoxClickRect          = QStyle.SE_CheckBoxClickRect #Clickable area, defaults to SE_CheckBoxFocusRect .
		CheckBoxLayoutItem         = QStyle.SE_CheckBoxLayoutItem #Area that counts for the parent layout.
		DateTimeEditLayoutItem     = QStyle.SE_DateTimeEditLayoutItem #Area that counts for the parent layout.
		RadioButtonIndicator       = QStyle.SE_RadioButtonIndicator #Area for the state indicator.
		RadioButtonContents        = QStyle.SE_RadioButtonContents #Area for the label.
		RadioButtonFocusRect       = QStyle.SE_RadioButtonFocusRect #Area for the focus indicator.
		RadioButtonClickRect       = QStyle.SE_RadioButtonClickRect #Clickable area, defaults to SE_RadioButtonFocusRect .
		RadioButtonLayoutItem      = QStyle.SE_RadioButtonLayoutItem #Area that counts for the parent layout.
		ComboBoxFocusRect          = QStyle.SE_ComboBoxFocusRect #Area for the focus indicator.
		SliderFocusRect            = QStyle.SE_SliderFocusRect #Area for the focus indicator.
		SliderLayoutItem           = QStyle.SE_SliderLayoutItem #Area that counts for the parent layout.
		SpinBoxLayoutItem          = QStyle.SE_SpinBoxLayoutItem #Area that counts for the parent layout.
		ProgressBarGroove          = QStyle.SE_ProgressBarGroove #Area for the groove.
		ProgressBarContents        = QStyle.SE_ProgressBarContents #Area for the progress indicator.
		ProgressBarLabel           = QStyle.SE_ProgressBarLabel #Area for the text label.
		ProgressBarLayoutItem      = QStyle.SE_ProgressBarLayoutItem #Area that counts for the parent layout.
		FrameContents              = QStyle.SE_FrameContents #Area for a frames contents.
		ShapedFrameContents        = QStyle.SE_ShapedFrameContents #Area for a frames contents using the shape in PySide.QtGui.QStyleOptionFrameV3 ; see PySide.QtGui.QFrame
		FrameLayoutItem            = QStyle.SE_FrameLayoutItem #Area that counts for the parent layout.
		HeaderArrow                = QStyle.SE_HeaderArrow #Area for the sort indicator for a header.
		HeaderLabel                = QStyle.SE_HeaderLabel #Area for the label in a header.
		LabelLayoutItem            = QStyle.SE_LabelLayoutItem #Area that counts for the parent layout.
		LineEditContents           = QStyle.SE_LineEditContents #Area for a line edits contents.
		TabWidgetLeftCorner        = QStyle.SE_TabWidgetLeftCorner #Area for the left corner widget in a tab widget.
		TabWidgetRightCorner       = QStyle.SE_TabWidgetRightCorner #Area for the right corner widget in a tab widget.
		TabWidgetTabBar            = QStyle.SE_TabWidgetTabBar #Area for the tab bar widget in a tab widget.
		TabWidgetTabContents       = QStyle.SE_TabWidgetTabContents #Area for the contents of the tab widget.
		TabWidgetTabPane           = QStyle.SE_TabWidgetTabPane #Area for the pane of a tab widget.
		TabWidgetLayoutItem        = QStyle.SE_TabWidgetLayoutItem #Area that counts for the parent layout.
		ToolBoxTabContents         = QStyle.SE_ToolBoxTabContents #Area for a toolbox tabs icon and label.
		ToolButtonLayoutItem       = QStyle.SE_ToolButtonLayoutItem #Area that counts for the parent layout.
		ItemViewItemCheckIndicator = QStyle.SE_ItemViewItemCheckIndicator #Area for a view items check mark.
		TabBarTearIndicator        = QStyle.SE_TabBarTearIndicator #Area for the tear indicator on a tab bar with scroll arrows.
		TreeViewDisclosureItem     = QStyle.SE_TreeViewDisclosureItem #Area for the actual disclosure item in a tree branch.
		DialogButtonBoxLayoutItem  = QStyle.SE_DialogButtonBoxLayoutItem #Area that counts for the parent layout.
		GroupBoxLayoutItem         = QStyle.SE_GroupBoxLayoutItem #Area that counts for the parent layout.
		CustomBase                 = QStyle.SE_CustomBase #Base value for custom sub-elements. Custom values must be greater than this value.
		DockWidgetFloatButton      = QStyle.SE_DockWidgetFloatButton #The float button of a dock widget.
		DockWidgetTitleBarText     = QStyle.SE_DockWidgetTitleBarText #The text bounds of the dock widgets title.
		DockWidgetCloseButton      = QStyle.SE_DockWidgetCloseButton #The close button of a dock widget.
		DockWidgetIcon             = QStyle.SE_DockWidgetIcon #The icon of a dock widget.
		ComboBoxLayoutItem         = QStyle.SE_ComboBoxLayoutItem #Area that counts for the parent layout.
		ItemViewItemDecoration     = QStyle.SE_ItemViewItemDecoration #Area for a view items decoration (icon).
		ItemViewItemText           = QStyle.SE_ItemViewItemText #Area for a view items text.
		ItemViewItemFocusRect      = QStyle.SE_ItemViewItemFocusRect #Area for a view items focus rect.
		TabBarTabLeftButton        = QStyle.SE_TabBarTabLeftButton #Area for a widget on the left side of a tab in a tab bar.
		TabBarTabRightButton       = QStyle.SE_TabBarTabRightButton #Area for a widget on the right side of a tab in a tab bar.
		TabBarTabText              = QStyle.SE_TabBarTabText #Area for the text on a tab in a tab bar.
		ToolBarHandle              = QStyle.SE_ToolBarHandle #Area for the handle of a tool bar.

########################################################################
class File_Dialog_Options:
	ShowDirsOnly                 = QFileDialog.ShowDirsOnly          # Only show directories in the file dialog. By default both files and directories are shown. (Valid only in the Directory file mode.)
	DontResolveSymlinks          = QFileDialog.DontResolveSymlinks   # Don't resolve symlinks in the file dialog. By default symlinks are resolved.
	DontConfirmOverwrite         = QFileDialog.DontConfirmOverwrite  # Don't ask for confirmation if an existing file is selected. By default confirmation is requested.
	DontUseNativeDialog          = QFileDialog.DontUseNativeDialog   # Don't use the native file dialog. By default, the native file dialog is used unless you use a subclass of PySide.QFileDialog that contains the Q_OBJECT() macro.
	ReadOnly                     = QFileDialog.ReadOnly              # Indicates that the model is readonly.
	HideNameFilterDetails        = QFileDialog.HideNameFilterDetails # Indicates if the file name filter details are hidden or not.
	DontUseSheet                 = QFileDialog.DontUseSheet          # In previous versions of Qt, the static functions would create a sheet by default if the static function was given a parent. This is no longer supported and does nothing in Qt 4.5, The static functions will always be an application modal dialog. If you want to use sheets, use QFileDialog.open() instead.

########################################################################
class ItemDataRole:
	""""""
	## The general purpose roles (and the associated types):
	DISPLAY        = Qt.DisplayRole       ## The key data to be rendered in the form of text.                                                :: QtCore.QString
	DECORATION     = Qt.DecorationRole    ## The data to be rendered as a decoration in the form of an icon.                                 :: QColor | QIcon | QtGui.QPixmap
	EDIT           = Qt.EditRole          ## The data in a form suitable for editing in an editor.                                           :: QString
	TOOLTIP        = Qt.ToolTipRole       ## The data displayed in the item's tooltip.                                                       :: QtCore.QString
	STATUSTIP      = Qt.StatusTipRole     ## The data displayed in the status bar.                                                           :: QtCore.QString
	WHATSTHIS      = Qt.WhatsThisRole     ## The data displayed for the item in What's This? mode.                                           :: QtCore.QString
	SIZEHINT       = Qt.SizeHintRole      ## The size hint for the item that will be supplied to views.                                      :: QtCore.QSize
	DP_ED          = [DISPLAY,EDIT]

	##Roles describing appearance and meta data (with associated types):

	FONT           = Qt.FontRole          ## The font used for items rendered with the default delegate.                                     :: QtGui.QFont
	TEXT_ALIGNMENT = Qt.TextAlignmentRole ## The alignment of the text for items rendered with the default delegate.                         :: Qt.AlignmentFlag
	BACKGROUND     = Qt.BackgroundRole    ## The background brush used for items rendered with the default delegate.                         :: QtGui.QBrush
	FOREGROUND     = Qt.ForegroundRole    ## The foreground brush (text color, typically) used for items rendered with the default delegate. :: QtGui.QBrush
	CHECKSTATE     = Qt.CheckStateRole    ## This role is used to obtain the checked state of an item.                                       :: Qt.CheckState