class node :

	def __init__(self , i_name, i_value, prev):
		self.item_name = i_name
		self.item_value = i_value
		self.prev = prev
		self.next = []

	def __str__(self):
		return "i_name : {},i_value : {} , i_next = {}".format(self.item_name,self.item_value,self.next)

	def print_tree(self, level=0):
		print ('\t' * level + repr(self.item_name) + ":" + repr(self.item_value))
		for child in self.next:
			child.print_tree(level+1)

root = node('root','root',None)
Data_List =[['a','b','c'],['a','c','e'],['b','c'],['c']]


for data in Data_List :
	index_now = root
	for item in data:
		if index_now.next == []:
			new_node = node(item,1,index_now)
			index_now.next.append(new_node)
			index_now = new_node
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

def find_sub_all(Super_List):
	ALL_Sub = []
	mask = [ 0 for i in range(len(Super_List))]
	find_sub(Super_List,mask,0,ALL_Sub)
	return ALL_Sub
	

def find_sub (Super_List,mask,index,ALL_Sub) :
	if index == len(Super_List) -1  :
		elements = []
		for i in range(0,len(Super_List)):
			if mask[i] == 1:
				elements.append(Super_List[i])
		ALL_Sub.append(set(elements))
	else:
		mask[index] = 0 
		find_sub(Super_List,mask,index+1,ALL_Sub)
		mask[index] = 1
		find_sub(Super_List,mask,index+1,ALL_Sub)	


root.print_tree()
'''
mask = []
set_List = [0,1,2,3,4,5]
print(find_sub_all(set_List))
print(len(find_sub_all(set_List)))


set1 = {'a','b'}
st = {'c'}
print(set1|st)
'''