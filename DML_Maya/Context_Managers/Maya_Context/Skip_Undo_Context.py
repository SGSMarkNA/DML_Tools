
import maya.cmds as cmds

########################################################################	
class MayaSkipUndoChunk(object):
	'''
	Safe way to using the 'with' command
	to create a block of commands that are not added to the undo queue.
	It will close the chunk automatically on exit from the block and
	restore the existing undo state.

	:Example:
	    cmds.polyCube()
	    with MayaSkipUndoChunk():
	        cmds.polyCube()
	        cmds.polyCube()
	    cmds.polyCube()
	'''
	#----------------------------------------------------------------------
	def __enter__(self):
		self.undoState = cmds.undoInfo(q=True, state=True)
		if self.undoState == True:
			cmds.undoInfo(stateWithoutFlush=False)
		return None
	#----------------------------------------------------------------------
	def __exit__(self, type, value, traceback):
		if self.undoState == True:
			cmds.undoInfo(stateWithoutFlush=True)
