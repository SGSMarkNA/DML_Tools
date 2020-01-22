import os

def compile_rcc(rcc_file, dest_foulder=None, dest_name=None):
	if not os.path.exists(rcc_file):
		raise IOError("File %r Does Not Exist" % rcc_file)
	
	if dest_foulder is None:
		dest_foulder = os.path.dirname(rcc_file)
		
	if dest_name is None:
		dest_name =  os.path.splitext(os.path.basename(rcc_file))[0] + ".py"
	dest_path =  os.path.join(dest_foulder, dest_name)
	
	command = 'C:/Python27/Lib/site-packages/PySide/pyside-rcc.exe -o "%s" -py2 -name runit "%s"' % (dest_path, rcc_file)
	os.system(command)
	
if __name__ == "__main__":
	compile_rcc(os.path.join(os.path.dirname(__file__), "icons\Icons.qrc") , dest_foulder=os.path.dirname(__file__) )
