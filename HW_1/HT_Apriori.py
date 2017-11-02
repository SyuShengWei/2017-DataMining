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
		print(self.Hash_Dict)
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
	Node_Ptr = H_Node('root',None)
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
				else:
					Ptr_Node = new_Node
					lay+=1
			else:
				if i == level-1 :
					Ptr_Node.next[HV_List[i]].Data.append(candidate_set)
				else:
					Ptr_Node = Ptr_Node.next[HV_List[i]]
					lay+=1
		
	return Root


def HT_Apriori(Data_List , min_sup):

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
# create Has Table 
	Two_Item = []
	for i in range(len(Sorted_Frequency_One_Item)-1):
		for j in range(i+1,len(Sorted_Frequency_One_Item)):
			Two_Item.append([Sorted_Frequency_One_Item[i],Sorted_Frequency_One_Item[j]])
	#print(Two_Item)

	the_hash = Hash(Sorted_Frequency_One_Item)
	HT_Root = createHT(the_hash,Two_Item,2)
	HT_Root.print_Tree()








if __name__ == "__main__" :
	Test_Data_List = [
				['a','c','d','f','g','i','m','p'],
				['a','b','c','f','i','m','o'],
				['b','f','h','j','o'],
				['b','c','k','s','p'],
				['a','c','e','f','l','m','n','p']
				]

	HT_Apriori(Test_Data_List,0.5)