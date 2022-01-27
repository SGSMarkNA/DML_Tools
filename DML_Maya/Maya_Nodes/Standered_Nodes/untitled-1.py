import csv
from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse

get_set_code = '''
	#----------------------------------------------------------------------
	def get_{command_dict[name]}(self):
		"""{command_dict[doc]}"""
		return self._query({command_dict[name]}=True)
	#----------------------------------------------------------------------
	def set_{command_dict[name]}(self,value):
		"""{command_dict[doc]}"""
		self._edit({command_dict[name]}=value)
	#----------------------------------------------------------------------
	{command_dict[name]} = property(fget=get_{command_dict[name]},fset=set_{command_dict[name]})'''

get_code = '''
	#----------------------------------------------------------------------
	def get_{command_dict[name]}(self):
		"""{command_dict[doc]}"""
		return self._query({command_dict[name]}=True)
	#----------------------------------------------------------------------
	{command_dict[name]} = property(fget=get_{command_dict[name]})'''

set_code = '''
	#----------------------------------------------------------------------
	def set_{command_dict[name]}(self,value):
		"""{command_dict[doc]}"""
		self._edit({command_dict[name]}=value)'''


website = urllib.request.urlopen("http://help.autodesk.com/cloudhelp/2018/ENU/Maya-Tech-Docs/CommandsPython/camera.html")
website_html = website.read()
soup   = BeautifulSoup(website_html, 'html.parser')
html   = soup.find(name="html", recursive=False)
body   = html.find(name="body", recursive=False)
lookup = body.find(name="th", attrs={}, recursive=True, text="Long name (short name)")
table = lookup.parent.parent
flags = table.findAll(name="tr", recursive=False)[2:]

for index in range(0,len(flags),2):
	flag_data,flag_doc = flags[index],flags[index+1]
	
	flag_items  = [item for item in flag_data.findAll(name="td", recursive=False) if not item.__next__ == "\\n"]
	
	flag_name, flag_typ, flag_modes = flag_items
	code = flag_name.find("code")
	command_name = code.text.split("(")[0]
	command_input = flag_typ.text.strip()
	can_edit        = flag_modes.find( attrs={'title': 'edit'}) != None
	can_query       = flag_modes.find( attrs={'title': 'query'}) != None
	can_create      = flag_modes.find( attrs={'title': 'create'}) != None
	command_doc = flag_doc.text.strip()
	command_doc_lines = command_doc.splitlines()
	command_doc = "\n".join(["\t\t"+line for line in command_doc_lines]).strip()+"\n\t\t"
	if can_edit and can_query:
		print((get_set_code.format(command_dict=dict(name=command_name,doc=command_doc))))
	elif can_edit and not can_query:
		print((get_code.format(command_dict=dict(name=command_name,doc=command_doc))))
	elif can_query and not can_edit:
		print((set_code.format(command_dict=dict(name=command_name,doc=command_doc))))
	