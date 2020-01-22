from itertools import count

########################################################################
class Counter(count):
	#----------------------------------------------------------------------
	def __init__(self,start=1,step=1):
		super(Counter,self).__init__(start,step)
	#----------------------------------------------------------------------
	def __call__(self):
		return self.next()