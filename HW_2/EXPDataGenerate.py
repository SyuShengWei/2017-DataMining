import csv
import queue

import graphviz 
from sklearn import tree
from sklearn import svm

import DataGenerator as DG
import Decision_Tree as DT

def readCSV(filename,num = 0):
	Data_X = []
	Data_Y = []
	infile = open(filename,'r')
	infile.readline()
	CSV_reader = csv.reader(infile,delimiter = ',', quotechar='|')
	for row in CSV_reader:
		Data_X.append(row[:-1])
		Data_Y.append(row[-1])
	if num == 0:
		return Data_X ,Data_Y 
	else :
		return Data_X[:num], Data_Y[:num]
if __name__ == "__main__":
###Generate Data Prepare
	Title_List = ["Management Math","Human Factors Engineering","Linear Algebra",
			"Cloud Mobile Applications","Computer Network","Java",
			"Psychology","Leadership","Service Management"]
	Person_List = [30,6,36,24,12,30,24,42,12]
	P_List = [Person_List[i]/60 for i in range(9)]


	Node_Info = ["Java",
				"Human Factors Engineering","Service Management",
				"[0]Industrial","[1]Information","Management Math","[0]Industrial",
				"x","x","x","x","[0]Industrial","[1]Information","x","x"]

	Root = DT.createBinaryTree(Node_Info)
	Root.printTree()
	#DG.generateByTree(Root,100000,9,Title_List,P_List,"Test.csv")
###Generate Train Data
	#for i in range(10):
	#	DG.generateByTree(Root,10000,9,Title_List,P_List,"Train"+str(i)+".csv")
	

	#test_X, test_Y = readCSV('Test.csv')


	#train_X, train_Y = readCSV('Train.csv',10000)

	#SVM = svm.SVC()
	#SVM.fit(train_X,train_Y)
	#result = SVM.score(test_X,test_Y)
	#print(result)
	'''
	Title_Plus_1 = ["Introduction to Simulation","Information Security","Psychology"]
	P_Plus_1 = [42,52,24]
	P_List_1 = [P_Plus_1[i]/60 for i in range(len(P_Plus_1))]
	Title_Plus_2 = ["Engineering Economy","APP Design","HR Management"]
	P_Plus_2 = [30,48,12]
	P_List_2 = [P_Plus_2[i]/60 for i in range(len(P_Plus_2))]
	Title_Plus_3 = ["Management Accounting","Computer Network","Decision Method"]
	P_Plus_3 = [54,12,48]
	P_List_3 = [P_Plus_3[i]/60 for i in range(len(P_Plus_3))]

	for i in range(10):
		DG.generateByTree(Root,100000,9,Title_List,P_List,"Test_9_"+str(i)+".csv")
		break

	for i in range(10):
		DG.generateByTree(Root,100000,12,Title_List+Title_Plus_1,P_List+P_List_1,"Test_12_"+str(i)+".csv")
		break
	for i in range(10):
		DG.generateByTree(Root,100000,15,Title_List+Title_Plus_1+Title_Plus_2,P_List+P_List_1+P_List_2,"Test_15_"+str(i)+".csv")
		break
	for i in range(10):
		DG.generateByTree(Root,100000,18,Title_List+Title_Plus_1+Title_Plus_2+Title_Plus_3,P_List+P_List_1+P_List_2+P_List_3,"Test_18_"+str(i)+".csv")
		break

	Title_Plus_1 = ["Introduction to Simulation","Engineering Economy","Management accounting"]
	P_Plus_1 = [42,30,54]
	Title_Plus_2 = ["Information Security","APP Design","Computer Network"]
	P_Plus_2 = [52,48,12]
	Title_Plus_3 = ["Psychology","HR Management","Decision Method"]
	P_Plus_3 = [24,12,48]
	P_List_1 = [P_Plus_1[i]/60 for i in range(len(P_Plus_1))]
	P_List_2 = [P_Plus_2[i]/60 for i in range(len(P_Plus_2))]
	P_List_3 = [P_Plus_3[i]/60 for i in range(len(P_Plus_3))]

	for i in range(10):
		DG.generateByTree(Root,100000,12,Title_List+Title_Plus_1,P_List+P_List_1,"Test_Ind_"+str(i)+".csv")
		break
	for i in range(10):
		DG.generateByTree(Root,100000,12,Title_List+Title_Plus_2,P_List+P_List_2,"Test_Inf_"+str(i)+".csv")
		break
	for i in range(10):
		DG.generateByTree(Root,100000,12,Title_List+Title_Plus_3,P_List+P_List_3,"Test_M_"+str(i)+".csv")
		break
	'''
	for i in range(11):
		DG.generateByTreeError(Root,10000,9,Title_List,P_List,"Train_Error_S_"+str(i)+".csv",0.01*i)
