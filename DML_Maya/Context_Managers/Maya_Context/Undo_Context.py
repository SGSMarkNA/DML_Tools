
import maya.cmds as cmds


########################################################################
class MayaUndoChunk(object):
	'''
	Safe way to manage group undo chunks using the 'with' command.
	It will close the chunk automatically on exit from the block
	:Example:
		cmds.polyCube()
		with MayaUndoChunk():
			cmds.polyCube()
			cmds.polyCube()
		cmds.undo()
	'''
	#----------------------------------------------------------------------
	def __enter__(self,chunkName="DML_Undo_Chunk"):
		cmds.undoInfo(openChunk=True,chunkName=chunkName)
		return None
	#----------------------------------------------------------------------
	def __exit__(self, type, value, traceback):
		cmds.undoInfo(closeChunk=True)