def readInfile(filename):
	Return_Data_List = []
	with open(filename,'r') as Infile:
		Data_List = Infile.readlines()
		for the_Line in Data_List:
			the_Line = the_Line.replace('\n','')
			the_data = the_Line.split(',')
			Return_Data_List.append(the_data)
	return Return_Data_List


def Apriori(Data_List , min_support ,result_type = 0):
	print("In A")
	Data_In_Set = []
	Item_Array_List = []
	Remain_Array_List = [] #this is the result

	total_data_num = 0 
	min_support_value = 0
#find all possibal items
	Total_Item = []
	for one_date in Data_List :
		Data_In_Set.append(set(one_date))
		#print(set(one_date))
		total_data_num += 1
		for item in one_date:
			if item not in Total_Item:
				Total_Item.append(item)
	min_support_value = (min_support*total_data_num)
	print('min',min_support_value)
	#print(Total_Item)
	#print(Data_In_Set)
#create the 2D arr for counting the frequence
	Item_Array0 = []
	#print(Total_Item)
	for item in Total_Item:
		Item_Array0.append([set([item]),0])
	#print(Item_Array[0][0])
	Item_Array_List.append(Item_Array0)
#start recursive find the relation
	for Item_Array in Item_Array_List:
#scan the frequence
		for data in Data_In_Set :
			for item in Item_Array:
				if item[0].issubset(data):
					item[1] +=1
#compare with min_sup
		Remain_Array = []
		Remove_Array = []
		for item in Item_Array:
			if item[1] < min_support_value:
				Remove_Array.append(item)
			else:
				Remain_Array.append(item)
		Remain_Array_List.append(Remain_Array)
#create sub sets next intection
		#print(Remain_Array)
		Item_Set_Next = []
		for i in range(0,len(Remain_Array)-1):
			for j in range(i+1,len(Remain_Array)):
				if_get = 1
				sub_set = Remain_Array[i][0].union(Remain_Array[j][0])
				#print(Remain_Array[i][0].union(Remain_Array[j][0]))
				for removed in Remove_Array:
					if removed[0].issubset(sub_set):
						if_get = 0 
				if len(sub_set) != len(Remain_Array[0][0])+1:
					if_get = 0
				if if_get == 1 and sub_set not in Item_Set_Next:
					Item_Set_Next.append(sub_set)
##create 2D array next
		Item_Array_Next = []
		for the_set in Item_Set_Next :
			Item_Array_Next.append([the_set,0])
		if (len(Item_Array_Next)) != 0:
			Item_Array_List.append(Item_Array_Next)
		#print(Item_Array_Next)
##return type	
	if result_type == 0 :
		Result_Return = []
		for remain in Remain_Array_List :
			for item in remain :
				Result_Return.append(list(item[0]))
		return Result_Return

	elif result_type == 1:
		ctr = 0 
		for remain in Remain_Array_List :
			for item in remain :
				print(item)
			ctr+=len(remain)
		print(ctr)
	elif result_type == 2 :
		ctr = 0 
		for remain in Remain_Array_List :
			for item in remain :
				print(item[0])
			ctr+=len(remain)
		print(ctr)

if __name__ == '__main__' : 
	#Test_Data_List = [['A','C','D'],['B','C','E'],['A','B','C','E'],['B','E']]
	Test_Data_List = [
					['a','c','d','f','g','i','m','p'],
					['a','b','c','f','i','m','o'],
					['b','f','h','j','o'],
					['b','c','k','s','p'],
					['a','c','e','f','l','m','n','p']
					]
	Test_Data_List = readInfile('Book_ranking1.csv')

	print(Apriori(Test_Data_List,0.001))
