import queue
import graphviz 
import DataGenerator as DG
from sklearn import tree

Tree_Hash = {"Y":0,"N":1}

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
	parent_node.child[Tree_Hash[pos]] = child_node
	child_node.parent = parent_node
	child_node.pos = pos

def createBinaryTree(Node_Info_List):
	Q_tree = queue.Queue() ##used to creat tree
	I_node = 1# index of Node_Info_List
	Root = Node(Node_Info_List[0])
	Q_tree.put(Root)
	while (I_node != len(Node_Info_List)):
		current = Q_tree.get()
		left_Node = Node(Node_Info_List[I_node])
		if(left_Node.name != "x"):
			growthTree(current,left_Node,"Y")
			Q_tree.put(left_Node)
		I_node += 1
		right_Node = Node(Node_Info_List[I_node])
		if(right_Node.name != "x"):
			growthTree(current,right_Node,"N")		
			Q_tree.put(right_Node)
		I_node += 1
	return Root

if __name__ == "__main__" :
	Title_List = ["Management Math","Human Factors Engineering","Linear Algebra",
			"Cloud Mobile Applications","Computer Network","Java",
			"Psychology","Leadership","Service Management"]
	Person_List = [40,10,45,10,10,30,30,45,15]
	Person_List = [10,10,10,10,10,10,10,10,10]

	Node_Info = ["Java",
				"Human Factors Engineering","Service Management",
				"[0]Industrial","[1]Information","Management Math","[0]Industrial",
				"x","x","x","x","[0]Industrial","[1]Information","x","x"]

	Root = createBinaryTree(Node_Info)
	Root.printTree()

	P_List = [Person_List[i]/60 for i in range(9)]

	Train_Data,Train_X,Train_Y = DG.generateByTree(Root,10,9,Title_List,P_List)
	#print(DG.Data_Y)
	DT = tree.DecisionTreeClassifier()
	#print(DG.Data_Y)
	#print(DG.Data_X)
	DT = DT.fit(Train_X,Train_Y)

	#dot_data = tree.export_graphviz(DT, out_file=None, 
	#                     feature_names=Title_List,  
	#                     class_names=["[0]Industrial","[1]Information"],
	#                     filled=True, rounded=True,  
	#                     special_characters=True) 
	score = 0
	test_times = 1000
	for i in range(test_times):
		Test_Data,Test_X,Test_Y = DG.generateByTree(Root,1000,9,Title_List,P_List)
		Result = DT.score(Test_X,Test_Y)	
		#print(Result)
		score += Result
	print(score/test_times)


