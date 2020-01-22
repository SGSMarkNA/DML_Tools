
import functools
from .. import General_Utils
import sys


#----------------------------------------------------------------------
def flatten_Input_Args(func):
	''''''
	@functools.wraps(func)
	def wrapper(*args, **kws):
		err = None
		try:
			args = General_Utils.flatten(args)
			if len(args)>=1:
				res = func(args[0], **kws)
			else:
				res = func(args, **kws)
		except Exception, error:
			err=error
		finally:
			if err:
				traceback = sys.exc_info()[2]  # get the full traceback
				raise Exception(err, traceback)
			return res
	return wrapper