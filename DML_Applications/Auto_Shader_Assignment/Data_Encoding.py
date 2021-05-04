from __future__ import print_function
import csv

__Column_1_Key = 'Name'
__Column_2_Key = 'Name_Associations'

#---------------------------------------
def Read_CSV(fp=r'D:\AW_Env_System\Code\Global_Systems\DML_Tools\DML_Applications\Auto_Shader_Assignment\TestData.csv'):
	"""Reads CSV File And Returns a list"""	
	res = []
	with open(fp) as csvfile:
		reader = csv.DictReader(csvfile)
		buffer_data = {}
		for row in reader:
			buffer_data[row[__Column_1_Key]] = sorted(row[__Column_2_Key].split(":"))
		for name in sorted(buffer_data.keys()):
			res.append( [name, buffer_data[name]])
	return res

#---------------------------------------
def Write_CSV(data,fp=r'D:\AW_Env_System\Code\Global_Systems\DML_Tools\DML_Applications\Auto_Shader_Assignment\TestData_Out.csv'):
	""""""
	with open(fp, 'w') as csvfile:
		csvfile.write("{},{}\n".format(__Column_1_Key, __Column_2_Key))
		for name in sorted(data.keys()):
			csvfile.write("{},{}\n".format(name, ":".join(data[name])))