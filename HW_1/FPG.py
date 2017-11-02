def readInfile(filename):
	Return_Data_List = []
	with open(filename,'r') as Infile:
		Data_List = Infile.readlines()
		for the_Line in Data_List:
			the_Line = the_Line.replace('\n','')
			the_data = the_Line.split(',')
			Return_Data_List.append(the_data)
	return Return_Data_List


class node :

	def __init__(self , i_name, i_value, prev):
		self.item_name = i_name
		self.item_value = i_value
		self.prev = prev
		self.next = []

	def __str__(self):
		return "i_name : {},i_value : {} , i_next = {}".format(self.item_name,self.item_value,self.next)

	def print_Tree(self, level=0):
		print ('\t' * level + repr(self.item_name) + ":" + repr(self.item_value))
		for child in self.next:
			child.print_Tree(level+1)

def update_Header(Header_Pointer_Dic,item,new_node):
	if len(Header_Pointer_Dic) != 0: 
		if item in Header_Pointer_Dic:
			the_List = Header_Pointer_Dic[item]
			the_List.append(new_node)
		else :
			new_dict = {item:[new_node]}
			Header_Pointer_Dic.update(new_dict)

	else:
		new_dict = {item:[new_node]}
		Header_Pointer_Dic.update(new_dict)

def createTree(Refinded_Data):
	Root = node('root',None,None)
	Header_Pointer_Dic = {}#[ [ item_name , [pointer] ] ]
	
	for data in Refinded_Data :
		index_now = Root 
		for item in data :
			if index_now.next == []:
				new_node = node(item,1,index_now)
				index_now.next.append(new_node)
				index_now = new_node
				update_Header(Header_Pointer_Dic,item,new_node)
			else:
				if_find = 0
				for child in index_now.next:
					if child.item_name == item:
						child.item_value += 1
						if_find = 1
						index_now = child

				if if_find == 0:
					new_node = node(item,1,index_now)
					index_now.next.append(new_node)
					index_now = new_node
					update_Header(Header_Pointer_Dic,item,new_node)
	return Root,Header_Pointer_Dic

def trace(node,path):
	if node.item_name != 'root' and node.item_name != 'C_root':
		#path.append([node.item_name,node.item_value])
		path.append(node.item_name)
		trace(node.prev,path)

def trace_PatternBase(node):
	Node_Path = []
	if node.prev != "root":
		trace(node.prev,Node_Path)
	Node_Path.reverse()
	return Node_Path


def findFrequencyOneItem(Data_List,min_sup , test = 0):
	Items_Dict = {}
	total_data_num = 0
	Remain_Item = []

	for transaction in Data_List:
		total_data_num += 1
		for item in transaction :
			Items_Dict[item] = Items_Dict.get(item,0) + 1

	min_sup_value = min_sup * total_data_num
	Sorted_Item_by_fre = sorted(Items_Dict , key = Items_Dict.get,reverse = True)	
	for item in Sorted_Item_by_fre :
		if Items_Dict[item] >= min_sup_value:
			Remain_Item.append(item)
	#del Sorted_Item_by_fre
	#print('Remain' , Remain_Item)
	if test == 1 :Remain_Item = ['B','D','A','E','C']
	return min_sup_value , Remain_Item

def rebuildData(Data_List,min_sup):
	msv , Remain_Item = findFrequencyOneItem(Data_List,min_sup)
	Ordered_Date = []
	for transaction in Data_List:
		data_line = []
		for item in Remain_Item:
			if item in transaction:
				data_line.append(item)
		Ordered_Date.append(data_line)
	return msv, Remain_Item,Ordered_Date

def findFrequency(Traced_Path,msv):
	Items_Dict = {} 
	Remain_Item_Dict = {}

	for transaction in Traced_Path:
		for item in transaction :
			Items_Dict[item] = Items_Dict.get(item,0) + 1

	Sorted_Item_by_fre = sorted(Items_Dict , key = Items_Dict.get,reverse = True)	
	#print(Sorted_Item_by_fre)
	for item in Sorted_Item_by_fre :
		if Items_Dict[item] >= msv:
			Remain_Item_Dict[item] = Items_Dict[item]

	return Remain_Item_Dict 

def searchTree(Root,Header_Pointer_Dic,item,sub_set,msv,FPG_Result):
#Search node path from HPD , one kind of node have one Path_List 
	Traced_Path = []
	#print()
	#print("Item now : ",item,", sub_set : " , sub_set)
	for node in Header_Pointer_Dic[item]: #one kind of node share a list of pointer
		path_of_one_node = trace_PatternBase(node)
		if path_of_one_node != [] :
			for i in range(node.item_value):
				Traced_Path.append(path_of_one_node)
	#print("Trace Path",Traced_Path)
#Create Cond FPTree
	S_Root , S_HPD = createTree(Traced_Path)
	#S_Root.print_Tree()
#find frequency
	FID = findFrequency(Traced_Path,msv)
	#print(FID)
	if len(FID) != 0:
		for the_item in FID:
			new_set = [the_item]+sub_set
			#print(new_set)
			FPG_Result[tuple(new_set)] = FID[the_item]
		#For each frequence item ,Create
		for sub_item in S_HPD:
			new_set = [sub_item]+sub_set
			searchTree(S_Root,S_HPD,sub_item,new_set,msv,FPG_Result)





def FP_Growth (Data_List,min_sup,result_type = 0):
	FP_Result_Dict = {}

	msv , Remain_Item , Rebuilded_Data = rebuildData(Data_List,min_sup)
	#print(msv , sorted(Remain_Item))
	Root , HPD = createTree(Rebuilded_Data)
	#Root.print_Tree()
	FID = findFrequency(Rebuilded_Data,msv)
	for the_item in FID:
		#print(tuple([the_item]))
		FP_Result_Dict[tuple([the_item])] = FID[the_item]
##Scan Pattern Base in Reverse Order of frequency
	for item in HPD:
		searchTree(Root,HPD,item,[item],msv,FP_Result_Dict)

	#print((FP_Result_Dict))
##decide result type---------------------------------------------------------------
	Result_Return = []
	if result_type == 0 :
		for item in FP_Result_Dict.keys():
			Result_Return.append(list(item))
		#print(len(Result_Return))
		return Result_Return

	elif result_type == 1:				
		for i in range(0,len(Remain_Item)):
			for item in FP_Result_Dict:
				if len(item) == i :
					print([item,FP_Result_Dict[item]])
		print("len of result : ",len(FP_Result_Dict))	

	elif result_type == 2 :	
		for i in range(0,len(Remain_Item)):
			for item in FP_Result_Dict:
				if len(item) == i :
					print(set(item))
		print("len of result : ",len(FP_Result_Dict))	

if __name__ == '__main__' :	
	
	Test_Data_List = [
				['a','c','d','f','g','i','m','p'],
				['a','b','c','f','i','m','o'],
				['b','f','h','j','o'],
				['b','c','k','s','p'],
				['a','c','e','f','l','m','n','p']
				]
	'''
	Test_Data_List = [
				['E','A','D','B'],
				['D','A','C','E','B'],
				['C','A','B','E'],
				['B','A','D'],
				['D'],
				['D','B'],
				['A','D','E'],
				['B','C']
				]
	'''
	Test_Data_List = readInfile('Book_ranking1.csv')

	print(FP_Growth(Test_Data_List,0.001))