import itertools
from . import Qt,QStandardItem
__all__ = ["userRole_generator","userType_generator"]
########################################################################
class Counter(itertools.count):
	##----------------------------------------------------------------------
	#def __init__(self,start=1,step=1):
		#super(Counter,self).__init__(start=start,step=step)
	#----------------------------------------------------------------------
	def __call__(self):
		return next(self)
	
userRole_generator = Counter(Qt.UserRole)
userType_generator = Counter(QStandardItem.UserType)