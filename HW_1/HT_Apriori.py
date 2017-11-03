class Hash:

	def __init__(self,one_item_List):
		self.one_item_List = one_item_List
		self.Hash_Dict = {}
		for i in range(len(self.one_item_List)):
			if i%3 == 0:
				self.Hash_Dict[one_item_List[i]] = 0
			elif i%3 == 1 :
				self.Hash_Dict[one_item_List[i]] = 1
			elif i%3 == 2 :
				self.Hash_Dict[one_item_List[i]] = 2
		#print(self.Hash_Dict)
	def print_HasH_Dict(self):
		print(self.Hash_Dict)

	def search(self,item):
		return self.Hash_Dict[item]

class H_Node :

	def __init__(self , name, prev):
		self.name = name
		self.value = [0,0,0]
		self.prev = prev
		self.next = [None,None,None]
		self.Data = []

	def print_Tree(self, level=0):
		print ('\t' * level + repr(self.name) + ":" + repr(self.Data))
		for child in self.next:
			if child != None:
				child.print_Tree(level+1)


def createHT(Hash,Candidata_List,level):
	Root = H_Node('root',None)
	Node_Dict = {}
##create_tree 
	for candidate_set in Candidata_List :
		#print(candidate_set)
		Ptr_Node = Root
		HV_List = []
		lay = 1
		for item in candidate_set:
			HV_List.append(Hash.search(item))
		for i in range(len(HV_List)):
			#print(i)
			if Ptr_Node.next[HV_List[i]] == None:
				new_Node = H_Node(str(HV_List[i]),Ptr_Node)
				Ptr_Node.next[HV_List[i]] = new_Node
				if i == level-1 :
					new_Node.Data.append(candidate_set)
					Node_Dict[tuple(candidate_set)] = 0
				else:
					Ptr_Node = new_Node
					lay+=1
			else:
				if i == level-1 :
					Ptr_Node.next[HV_List[i]].Data.append(candidate_set)
					Node_Dict[tuple(candidate_set)] = 0
				else:
					Ptr_Node = Ptr_Node.next[HV_List[i]]
					lay+=1
		
	return Root , Node_Dict
#				12356.  root 3.    [].     
def traceTree(data_line,node,level,preset,the_hash,Node_Dict):
	if level == len(preset)+1 :
		for i in range(len(data_line)):
			the_sub_set = preset+[data_line[i]]
			if node.next[the_hash.search(data_line[i])] != None:
				Data_of_next = node.next[the_hash.search(data_line[i])].Data
				for item_set in Data_of_next:
					#print(item_set,node.next[the_hash.search(data_line[i])].name)
					if(the_sub_set == item_set):
						Node_Dict[tuple(the_sub_set)] +=1
	else:
		if len(data_line) > 3:
			for i in range(0,3):
				hash_value = the_hash.search(data_line[i])
				if node.next[hash_value] != None:
					next_node = node.next[hash_value]
					preset_next = preset+[data_line[i]]
					if len(data_line) > i+1:	
						line_next = data_line[i+1:]
						if(len(preset_next) + len(line_next)) >= level :
							traceTree(line_next,next_node,level,preset_next,the_hash,Node_Dict)
				
		else:
			for i in range(0,len(data_line)):
				hash_value = the_hash.search(data_line[i])
				if node.next[hash_value] != None:
					next_node = node.next[hash_value]
					preset_next = preset+[data_line[i]]
					try:	
						line_next = data_line[i+1:]
						if(len(preset_next) + len(line_next)) >= level :
							traceTree(line_next,next_node,level,preset_next,the_hash,Node_Dict)
					except:
						return



def HT_Apriori(Data_List , min_sup,result_type = 0):
	Result = []

	total_data_num = 0
##Prepare one item frequence
	One_Item_Dict = {}
	for data_line in Data_List :
		total_data_num += 1
		for item in data_line :
			One_Item_Dict[item] = One_Item_Dict.get(item,0) + 1

	msv = min_sup * total_data_num
	
	Frequency_One_Item_Dict = {}
	for item in One_Item_Dict:
		if One_Item_Dict[item] >= msv :
			Frequency_One_Item_Dict[item] = One_Item_Dict[item]
	Sorted_Frequency_One_Item = sorted(Frequency_One_Item_Dict,key =Frequency_One_Item_Dict.get,reverse = True)
	#print('Sorted',Sorted_Frequency_One_Item)
	for item in Sorted_Frequency_One_Item:
		Result.append([[item],Frequency_One_Item_Dict[item]])
#rebuild data in sorted
	Sorted_Data = []
	for data_line in Data_List :
		sorted_line = []
		for item in Sorted_Frequency_One_Item :
			if item in data_line:
				sorted_line.append(item)
		Sorted_Data.append(sorted_line)
# create Has Table 
	the_hash = Hash(Sorted_Frequency_One_Item)
	#the_hash.print_HasH_Dict()

	level = 2
	Two_Item = []
	for i in range(len(Sorted_Frequency_One_Item)-1):
		for j in range(i+1,len(Sorted_Frequency_One_Item)):
			Two_Item.append([Sorted_Frequency_One_Item[i],Sorted_Frequency_One_Item[j]])
	#print(Two_Item)
	ItemSet_Array_Next = []
	ItemSet_Array_Next.append(Two_Item)

	for ItemSet_Array in ItemSet_Array_Next:

		HT_Root ,Node_Dict = createHT(the_hash,ItemSet_Array,level)
		#HT_Root.print_Tree()
		for data_line in Sorted_Data:
			traceTree(data_line,HT_Root,level,[],the_hash,Node_Dict)	
		#print(Node_Dict)
		Remain_Item = []
		Remove_Item = []
		for itemset in ItemSet_Array:
			if Node_Dict[tuple(itemset)] < msv:
				Remove_Item.append(set(itemset))
			else:
				Result.append([itemset,Node_Dict[tuple(itemset)]])
				Remain_Item.append(set(itemset))

		Item_Set_Next = []
		for i in range(0,len(Remain_Item)-1):
			for j in range(i+1,len(Remain_Item)):
				if_get = 1
				sub_set = Remain_Item[i].union(Remain_Item[j])
				for removed in Remove_Item:
					if removed.issubset(sub_set):
						if_get = 0
				if len(sub_set) != len(Remain_Item[0]) +1:
					if_get = 0
				if if_get==1 and sub_set not in Item_Set_Next:
					Item_Set_Next.append(sub_set)
		Item_Array_Next = []
		for the_set in Item_Set_Next :
			Item_Array_Next.append(list(the_set))
		if (len(Item_Array_Next) )!= 0 :
			ItemSet_Array_Next.append(Item_Array_Next)
##========Result=======================================##
	if result_type == 0 :
		Result_Return = []
		for remain in Result :
			Result_Return.append(remain[0])
		return Result_Return
	elif result_type == 1:
		print(Result)
		print(len(Result))
	elif result_type == 2 :
		ctr = 0 
		for remain in Remain_Array_List :
			print(remain[0])
		print(len(Result))

def readInfile(filename):
	Return_Data_List = []
	with open(filename,'r') as Infile:
		Data_List = Infile.readlines()
		for the_Line in Data_List:
			the_Line = the_Line.replace('\n','')
			the_data = the_Line.split(',')
			Return_Data_List.append(the_data)
	return Return_Data_List

if __name__ == "__main__" :
	Test_Data_List = [
				['a','c','d','f','g','i','m','p'],
				['a','b','c','f','i','m','o'],
				['b','f','h','j','o'],
				['b','c','k','s','p'],
				['a','c','e','f','l','m','n','p']
				]
	Test_Data_List = readInfile('Book_ranking1.csv')
	(HT_Apriori(Test_Data_List,0.001,1))