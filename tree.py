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

root.print_tree()