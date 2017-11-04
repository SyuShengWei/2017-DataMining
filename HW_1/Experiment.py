import Apriori
import FPG
import HT_Apriori
def if_same_result(result_a , result_b):
	if_same = 1
	for item_a in result_a :
		if_find = 0
		for item_b in result_b:
			#print(set(item_b))
			if set(item_a) == set(item_b):
				if_find = 1 
		if if_find == 0 :
			if_same =  0
			break
	if if_same == 1:
		return True
	else:
		return False

def readInfile(filename):
	Return_Data_List = []
	with open(filename,'r') as Infile:
		Data_List = Infile.readlines()
		for the_Line in Data_List:
			the_Line = the_Line.replace('\n','')
			the_data = the_Line.split(',')
			Return_Data_List.append(the_data)
	return Return_Data_List

if __name__ == '__main__' :	
	'''
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
	Test_Data_List = readInfile('Py_IBM_1_1_0.01.csv')

	ms = 0.01

	#print(Test_Data_List[0])
	#print("a")
	a = FPG.FP_Growth(Test_Data_List,ms)
	FPG.FP_Growth(Test_Data_List,ms,1)

	#b = Apriori.Apriori(Test_Data_List,ms)
	#Apriori.Apriori(Test_Data_List,ms,1)

	c = HT_Apriori.HT_Apriori(Test_Data_List,ms)
	HT_Apriori.HT_Apriori(Test_Data_List,ms,1)

	
	#print(if_same_result(a,b))
	print(if_same_result(a,c))


