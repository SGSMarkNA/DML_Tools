import itertools
from . import Qt,QStandardItem
__all__ = ["userRole_generator","userType_generator"]
########################################################################
class Counter(itertools.count):
	#----------------------------------------------------------------------
	def __init__(self,start=1,step=1):
		super(Counter,self).__init__(start,step)
	#----------------------------------------------------------------------
	def __call__(self):
		return self.next()
	
userRole_generator = Counter(Qt.UserRole)
userType_generator = Counter(QStandardItem.UserType)