
import csv

__Column_1_Key = 'Name'
__Column_2_Key = 'Name_Associations'

#---------------------------------------
def Read_CSV(fp=r'D:\aw_config\Git_Live_Code\Global_Systems\DML_Tools\DML_Applications\Auto_Shader_Assignment\TestData_Out.csv'):
	"""Reads CSV File And Returns a list"""	
	res = []
	with open(fp) as csvfile:
		reader = csv.DictReader(csvfile)
		buffer_data = {}
		for row in reader:
			__Column_1_value  = row[__Column_1_Key]
			__Column_2_values = [value for value in row[__Column_2_Key].split(":") if len(value)]
			__Column_2_values.sort()
			
			buffer_data[__Column_1_value] = __Column_2_values
		for name in sorted(buffer_data.keys()):
			res.append( [name, buffer_data[name]])
	res.insert(0, ["None", []])
	return res

#---------------------------------------
def Write_CSV(data,fp=r'D:\aw_config\Git_Live_Code\Global_Systems\DML_Tools\DML_Applications\Auto_Shader_Assignment\TestData_Out.csv'):
	""""""
	with open(fp, 'w') as csvfile:
		csvfile.write("{},{}\n".format(__Column_1_Key, __Column_2_Key))
		for name in sorted(data.names):
			if not name == "None":
				csvfile.write("{},{}\n".format(name, ":".join(data[name])))