import DataGenerator as DG

##Data [Management Math,Human Factors Engineering,Linear Algebra,
##		Cloud Mobile Applications,Computer Network,Java,Psychology,Leadership,Service Management]

Hash_Dict = {"Y":0,"N":1}

Title_List = ["Management Math","Human Factors Engineering","Linear Algebra",
			"Cloud Mobile Applications","Computer Network","Java",
			"Psychology","Leadership","Service Management"]
Persion_List = [40,10,45,10,10,30,30,45,15]
class Node :
	def __init__(self,node_name):
		self.name = node_name
		self.parent = None
		self.child = [None,None]
		self.pos = None
	
	def printTree(self,level=0):
		print('\t'*level + '('+str(self.pos)+')'+ str(self.name) )
		for child_node in self.child:
			if child_node != None:
				child_node.printTree(level+1)

def growthTree(parent_node,child_node,pos):
	parent_node.child[Hash_Dict[pos]] = child_node
	child_node.parent = parent_node
	child_node.pos = pos

if __name__ == "__main__":
	print(__name__)

	Root = Java_node =  Node("Java")
	
	Human_node = Node("Human Factors Engineering")
	growthTree(Java_node,Human_node,"Y")

	Service_node = Node("Service Management")
	growthTree(Java_node,Service_node,"N")

	industrial_1 = Node("[0]Industrial")
	growthTree(Human_node,industrial_1,"Y")

	information_1 = Node("[1]Information")
	growthTree(Human_node,information_1,"N")

	Math_Node = Node("Management Math")
	growthTree(Service_node,Math_Node,"Y")

	industrial_2 = Node("[0]Industrial")
	growthTree(Service_node,industrial_2,"N")

	industrial_3 = Node("[0]Industrial")
	growthTree(Math_Node,industrial_3,"Y")

	information_2 = Node("[1]Information")
	growthTree(Math_Node,information_2,"N")

	Root.printTree()
	P_List = [Persion_List[i]/60 for i in range(9)]
	
	#print(P_List)


	DG.generateByTree(Root,100,9,Title_List,P_List)

	print(DG.Data)








