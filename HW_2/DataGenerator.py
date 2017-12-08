import random

def generateByTree(Root,num,data_len,key_List,P_List):
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
	return Data,Data_X,Data_Y
		