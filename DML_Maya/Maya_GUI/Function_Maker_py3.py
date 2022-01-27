
import urllib.request
import urllib.request, urllib.parse, urllib.error
import pathlib
import lxml.html
import os
from  string import  Template
GUI_get_set_templet = Template('''
\t#----------------------------------------------------------------------
\tdef get_$name(self):
\t\t"""$doc"""
\t\treturn self.query($name=True)
\t#----------------------------------------------------------------------
\tdef set_$name(self, value):
\t\t"""$doc"""
\t\tself.edit($name=value)
\t#----------------------------------------------------------------------
\t$name = property(get_$name, set_$name)''')
GUI_get_templet = Template('''
\t#----------------------------------------------------------------------
\t@property
\tdef $name(self):
\t\t"""$doc"""
\t\treturn self.query($name=True)''')
GUI_set_templet = Template('''
\t#----------------------------------------------------------------------
\tdef $name(self,value):
\t\t"""$doc"""
\t\tself.edit($name=value)''')

GUI_class_templet = Template('''

import maya.cmds as cmds
from .. import UI_Object

########################################################################
class $class_name(UI_Object.UI):
\t"""$doc"""
\t#----------------------------------------------------------------------
\tdef __init__(self, name=None, **kwargs):
\t\tparent = None
\t\tif kwargs.has_key("qtParent"):
\t\t\tparent = kwargs.pop("qtParent")
\t\t\t
\t\tif name == None:
\t\t\tname = cmds.$command_name(**kwargs)
\t\t\tsuper($class_name, self).__init__(name, **dict(qtParent=parent))
\t\t\t
\t\telse:
\t\t\tif cmds.$command_name(name, exists=True):
\t\t\t\tsuper($class_name, self).__init__(name)
\t\t\telse:
\t\t\t\tname = cmds.$command_name(name, **kwargs)
\t\t\t\tsuper($class_name, self).__init__(name, **dict(qtParent=parent))''')


_base_foulder = pathlib.Path(__file__).parent


########################################################################
class Command_Data(object):
	#----------------------------------------------------------------------
	def __init__(self,name,input_Type,options,doc):
		self.name       = name
		self.input_type = input_Type
		self.options    = options
		self.document   = doc
		if len(self.document):
			lines = self.document.splitlines()
			self.document = "\n\t\t"+lines[0]
			if len(lines)>1:
				for line in lines[1:]:
					self.document +="\n\t\t"+line
			self.document += "\n\t\t"
	#----------------------------------------------------------------------
	def output_Code(self):
		if "edit" in self.options and "query" in self.options:
			return GUI_get_set_templet.substitute(name=self.name,doc=self.document)
		if "edit" in self.options and not "query" in self.options:
			return GUI_set_templet.substitute(name=self.name,doc=self.document)
		if not "edit" in self.options and "query" in self.options:
			return GUI_get_templet.substitute(name=self.name,doc=self.document)
		else:
			return ""

########################################################################
class Class_Data(object):
	#----------------------------------------------------------------------
	def __init__(self,name,doc):
		self.name         = name
		self.document     = doc
		self.commands     = []
	#----------------------------------------------------------------------
	def output_Code(self):
		res = GUI_class_templet.substitute(class_name=self.name[0].upper()+self.name[1:],command_name=self.name,doc=self.document)
		for cmd in self.commands:
			res += cmd.output_Code()
		return res

########################################################################
class Python_Command_Docs_Parser(object):
	""""""
	def __init__(self):
		"""Constructor"""
		self.catagory_elements          = []
		self.windows_command_catorgerized_commands   = dict()
		self.general_command_elements   = dict()
		self.language_command_elements  = dict()
		self.modeling_command_elements  = dict()
		self.animation_command_elements = dict()
		self.rendering_command_elements = dict()
		self.effects_command_elements   = dict()
		self.system_command_elements    = dict()
		
		self.GUI_command_elements    = []
		
		self.command_catagory_types = dict(General   = self.general_command_elements,
			 Language  = self.language_command_elements,
			 Modeling  = self.modeling_command_elements,
			 Animation = self.animation_command_elements,
			 Rendering = self.rendering_command_elements,
			 Effects   = self.effects_command_elements,
			 System    = self.system_command_elements,
			 Windows   = self.windows_command_catorgerized_commands)
		
		self.python_commands_element    = Url_To_Element("http://help.autodesk.com/cloudhelp/2018/ENU/Maya-Tech-Docs/CommandsPython/index.html")
		self.command_catagories_element = Url_To_Element(self.python_commands_element.find("frameset").find('frame').get('src'))
		
		for cat_top_element in self.command_catagories_element.xpath("./body/div/table/tr[3]/td[2]/table/tr/td"):
			for cat in cat_top_element.xpath("font/a[1]"):
				content = cat.text_content().strip()
				if content in self.command_catagory_types:
					if content in ["Windows"]:
						self.windows_command_catorgerized_commands = extract_Catagory_Command_Elements(cat.get("href"))
	#----------------------------------------------------------------------
	def build_GUI_Class_Commands(self):
		""""""
		for key in self.windows_command_catorgerized_commands:
			command_class_elements = self.windows_command_catorgerized_commands[key]
			package_folder = _base_foulder.joinpath(key)
			package_init   = package_folder.joinpath("__init__.py")
			
			package_init_output = []
			if not package_folder.exists():
				package_folder.mkdir()
				
			for cls_element in command_class_elements:
				cls_data = build_GUI_Command_Class(cls_element)
				cls_file = package_folder.joinpath(cls_data.name[0].upper()+cls_data.name[1:]+".py")
				cls_output_text = cls_data.output_Code()
				cls_file.write_text(cls_output_text)
				package_init_output.append("from {} import {}".format(cls_data.name[0].upper()+cls_data.name[1:],cls_data.name[0].upper()+cls_data.name[1:]))
			package_init.write_text("\n".join(package_init_output))
#----------------------------------------------------------------------
def extract_Catagory_Command_Elements(catagory_url):
	""""""
	res = dict()
	root_element = Url_To_Element(catagory_url)
	url_parent   = pathlib.Path(catagory_url).parent
	for header_element in root_element.getiterator("h2"):
		key = header_element.text_content().strip()
		if not key in res:
			res[key] = []
		for alink in header_element.getnext().xpath("./tr/td/a"):
			html_file = alink.text_content() + ".html"
			html_path = str(url_parent.joinpath(html_file))
			html_path = html_path.replace("\\","/").replace("http:/","http://")
			command_element = Url_To_Element(html_path)
			res[key].append(command_element)
	return res

#----------------------------------------------------------------------
def build_GUI_Command_Class(cls_element):
	""""""
	command_element      = cls_element.find_class("command")[0]
	command_name         = command_element.find(".//h1").text_content().strip()
	cls_doc              = "".join([line for line in command_element.xpath("./text()") if len(line.strip())>4]).strip()
	
	if len(cls_doc):
		lines = cls_doc.splitlines()
		cls_doc = "\n\t"+lines[0]
		if len(lines)>1:
			for line in lines[1:]:
				cls_doc +="\n\t"+line
		cls_doc += "\n\t"
		
	cls_data = Class_Data(command_name, cls_doc)
	
	for item_scan in cls_element.getiterator("th"):
		if item_scan.text == "Long name (short name)":
			table = item_scan.getparent().getparent()
			for i , code_item in enumerate(table.getiterator(("code"))):
				if i % 2==0 or i == 0:
					name = code_item.text_content().split("(")[0]
				else:
					arg  = code_item.text_content()
					ops  = []
					for img_item in code_item.getparent().getparent().getiterator(("img")):
						ops.append(img_item.attrib.get("alt"))
						
					command_doc = code_item.getparent().getparent().getnext().text_content().strip()
					
					if len(command_doc):
						lines = command_doc.splitlines()
						command_doc = "\n\t\t"+lines[0]
						if len(lines)>1:
							for line in lines[1:]:
								command_doc +="\n\t\t"+line
						command_doc += "\n\t\t"
						
					data = Command_Data(name, arg, ops, command_doc)
					
					cls_data.commands.append(data)
	return cls_data

#----------------------------------------------------------------------
def Url_To_Element(url):
	""""""
	url_request      = urllib.request.urlopen(url)
	url_text         = url_request.read()
	root_element     = lxml.html.fromstring(url_text)
	root_element.make_links_absolute(url)
	return root_element
#----------------------------------------------------------------------
def extract_Command_Url(command_file):
	""""""
	root_element         = root_element = Url_To_Element(command_file)
	command_element      = root_element.find_class("command")[0]
	command_Header_Elem  = command_element.find(".//h1")
	command_name         = command_Header_Elem.text_content().strip()
	command_docs         = "".join([line for line in command_element.xpath("./text()") if len(line.strip())>4]).strip()
	cls_data = Class_Data(command_name, command_docs)
	for item_scan in root_element.getiterator("th"):
		if item_scan.text == "Long name (short name)":
			maya_ui_command_attribute_table = item_scan.getparent().getparent()
			for i , code_item in enumerate(maya_ui_command_attribute_table.getiterator(("code"))):
				if i % 2==0 or i == 0:
					name = code_item.text_content().split("(")[0]
				else:
					arg  = code_item.text_content()
					ops  = []
					for img_item in code_item.getparent().getparent().getiterator(("img")):
						ops.append(img_item.attrib.get("alt"))
						
					doc = code_item.getparent().getparent().getnext().text_content().strip()
					data = Command_Data(name, arg, ops, doc)
					
					cls_data.command_data.append(data)
			return cls_data
		else:
			print(("skiping {}".format(command_name)))
			return None
#----------------------------------------------------------------------
def extract_Main_Catagory_Doc_Url(url):
	""""""
	root_element = Url_To_Element(url)
	for header_element in root_element.getiterator("h2"):
		name = header_element.text_content().strip().replace(".","").replace(" ","")
		url_parent = pathlib.Path(url).parent
		package = Package_Code(name)
		modual_classes = []
		for alink in header_element.getnext().xpath("./tr/td/a"):
			html_path=url_parent.joinpath(alink.text_content()+".html")
			class_data = extract_Command_Url(str(html_path).replace("\\","/").replace("http:/","http://"))
			if not class_data == None:
				modual_code = GUI_Modual_Code(class_data, package.folder)
				package.package_moduals.modules.append(modual_code)
		package.output_Code()
#----------------------------------------------------------------------
def extract_Overview_Docs_Url(url):
	""""""
	root_element = Url_To_Element(url)
	catagories = root_element.xpath("./body/div/table/tr[3]/td[2]/table/tr/td")
	for cat_top_element in catagories:
		for cat in cat_top_element.xpath("font/a[1]"):
			if cat.text_content() == "Windows":
				extract_Main_Catagory_Doc_Url(cat.get("href"))
	
#----------------------------------------------------------------------
def extract_Python_Command_Docs():
	""""""
	root_element = Url_To_Element("http://help.autodesk.com/cloudhelp/2018/ENU/Maya-Tech-Docs/CommandsPython/index.html")
	overviewDoc_url  = root_element.find("frameset").find('frame').get('src')
	extract_Overview_Docs_Url(overviewDoc_url)
	
parser = Python_Command_Docs_Parser()
parser.build_GUI_Class_Commands()
