import functools
import maya.cmds as cmds
import sys
#----------------------------------------------------------------------
def locked_Plug_Management(func):
	'''
	This decorator is used to manage the unlocking of self for all calls that
	require change access rights to the plug itself once changed returns it to its orig state.
	'''
	@functools.wraps(func)
	def wrapper(*args, **kws):
		# Stores return value of the orig function
		res = None
		# store the error if one is cought
		err = None
		# store the orig lock state of the node
		locked=False
		try:
			# get the current lock state
			locked = cmds.getAttr(args[0], lock=True )
			# force the node to be unlocked
			cmds.setAttr(args[0],lock=False)
			# run the orig function
			res=func(*args, **kws)
		except StandardError, error:
			# store the error
			err=error
		finally:
			# restore the orig lock state
			cmds.setAttr(args[0],lock=locked)
			# check if an error was cough
			if err:
				# get the error info and raise a new StandardError
				traceback = sys.exc_info()[2]  # get the full traceback
				raise StandardError(StandardError(err), traceback)
			return res
	return wrapper
