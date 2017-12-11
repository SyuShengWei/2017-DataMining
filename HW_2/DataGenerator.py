import random
import csv

def generateByTree(Root,num,data_len,key_List,P_List,outfile_name = ''):
	Data = []
	Data_X = []
	Data_Y = []
	#print(key_List)
	for i in range(num):
		data_line = []
		for att in range(data_len):
			if random.random() >= P_List[att]:
				data_line.append('1')
			else:
				data_line.append('0')
		current = Root
		Data_X.append(list(data_line))
		while(current.child[0] != None or current.child[1] != None):
			#print( data_line[(key_List.index(current.name))],end=" ")
			if data_line[ (key_List.index(current.name)) ] == '1' :
				#print(current.name,end =' -> ')
				current = current.child[0]
			else:
				#print(current.name,end =' -> ')
				current = current.child[1]
		data_line.append(current.name)
		Data_Y.append(current.name) 
		#print(int(current.name[1]))
		Data.append(data_line)
		if outfile_name != '' : 
			CSV_Writer = csv.writer(open(outfile_name,'w',newline=''),delimiter=',',quotechar='|')
			CSV_Writer.writerow(key_List+['Class'])
			for line in Data:
				CSV_Writer.writerow(line)
	return Data,Data_X,Data_Y

def generateByTreeError(Root,num,data_len,key_List,P_List,outfile_name = '', error_rate = 0):
	Data = []
	Data_X = []
	Data_Y = []
	#print(key_List)
	for i in range(num):
		data_line = []
		for att in range(data_len):
			if random.random() >= P_List[att]:
				data_line.append('1')
			else:
				data_line.append('0')
		current = Root
		Data_X.append(list(data_line))
		while(current.child[0] != None or current.child[1] != None):
			#print( data_line[(key_List.index(current.name))],end=" ")
			if data_line[ (key_List.index(current.name)) ] == '1' :
				#print(current.name,end =' -> ')
				current = current.child[0]
			else:
				#print(current.name,end =' -> ')
				current = current.child[1]
		if_error = random.random()
		if current.name == "[0]Industrial" and if_error < error_rate:
			data_line.append("[1]Information")
			Data_Y.append("[1]Information")
		elif current.name == "[0]Industrial" and if_error >= error_rate: 
			data_line.append(current.name)
			Data_Y.append(current.name) 
		elif current.name == "[1]Information" and if_error < error_rate:
			data_line.append("[0]Industrial")
			Data_Y.append("[0]Industrial")
		elif current.name == "[1]Information" and if_error >= error_rate: 
			data_line.append(current.name)
			Data_Y.append(current.name) 
		#print(int(current.name[1]))
		Data.append(data_line)
		if outfile_name != '' : 
			CSV_Writer = csv.writer(open(outfile_name,'w',newline=''),delimiter=',',quotechar='|')
			CSV_Writer.writerow(key_List+['Class'])
			for line in Data:
				CSV_Writer.writerow(line)
	return Data,Data_X,Data_Y