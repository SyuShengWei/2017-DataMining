import operator

def FP_Growth(Data_List ,min_sup):
#count frequence of each item in evey data 
	Items_Dict = {}
	total_data_num = 0

	for transaction in Data_List:
		total_data_num += 1
		for item in transaction :
			Items_Dict[item] = Items_Dict.get(item,0) + 1
	min_sup_value = total_data_num * min_sup 

	Sorted_Item_by_fre = sorted(Items_Dict , key = Items_Dict.get,reverse = True)


##	


Test_Data_List = [
				['a','c','d','f','g','i','m','p'],
				['a','b','c','f','i','m','o'],
				['b','f','h','j','o'],
				['b','c','k','s','p'],
				['a','c','e','f','l','m','n','p']
				]

FP_Growth(Test_Data_List,0.5)