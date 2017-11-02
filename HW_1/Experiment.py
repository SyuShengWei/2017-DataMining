import Apriori
import FPG
def if_same_result(result_a , result_b):
	if_same = 1
	for item_a in result_a :
		if_find = 0
		for item_b in result_b:
			if set(item_a) == set(item_b):
				if_find = 1 
		if if_find == 0 :
			if_same =  0
			break
	if if_same == 1:
		return True
	else:
		return False



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
	

	a = FPG.FP_Growth(Test_Data_List,0.5)
	b = Apriori.Apriori(Test_Data_List,0.5)
	#a= [['a','b'],['a','b','c']]
	#b= [['b','a'],['a','c','b']]
	print(if_same_result(a,b))
