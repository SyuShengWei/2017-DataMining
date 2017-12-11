import csv
import queue
import numpy as np
import graphviz 
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn import linear_model

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

import DataGenerator as DG
import Decision_Tree as DT
def readCSV(filename,num = 0):
    Data_X = []
    Data_Y = []
    NUM_X = []
    NUM_Y = []
    infile = open(filename,'r')
    infile.readline()
    CSV_reader = csv.reader(infile,delimiter = ',', quotechar='|')
    for row in CSV_reader:
        Data_X.append(row[:-1])
        Data_Y.append(row[-1])
    for line in Data_X:
        num_line = []
        for element in line :
            num_line.append(int(element))
        NUM_X.append(num_line)
    for element in Data_Y:
        NUM_Y.append(int(element[1]))
    if num == 0:
        return Data_X, Data_Y, NUM_X, NUM_Y 
    else :
        return Data_X[:num], Data_Y[:num], NUM_X[:num], NUM_Y[:num]

def readResult (infile):
    Data_List = []
    CSV_reader = csv.reader(open(infile,'r'),delimiter = ',', quotechar='|')
    for row in CSV_reader:
        Data_List.append([float(element) for element in row])
    return Data_List
if __name__ == "__main__":
    Title_List = ["Management Math","Human Factors Engineering","Linear Algebra",
                "Cloud Mobile Applications","Computer Network","Java",
                "Psychology","Leadership","Service Management"]
    '''
    DT_result = []
    RF_result = []
    NB_result = []
    SVM_result = []
    LR_result = []
    Result = [DT_result,RF_result,NB_result,SVM_result,LR_result]
    NUM_List = [10,100,1000,10000]
    test_X, test_Y , test_NX, test_NY= readCSV('Test.csv')
    for num in NUM_List :
        DT_i_result = []
        RF_i_result = []
        NB_i_result = [] 
        SVM_i_result = [] 
        LR_i_result = []
        for i in range(10):
            train_X, train_Y, train_NX, train_NY = readCSV("Train"+str(i)+".csv",num)

            DT = tree.DecisionTreeClassifier()
            DT.fit(train_X,train_Y)
            tree.export_graphviz(DT, out_file="EXP2_"+str(num)+"_"+str(i)+".txt", 
                         feature_names=Title_List,  
                         class_names=["[0]Industrial","[1]Information"],
                         filled=True, rounded=True,  
                         special_characters=True) 
            RF = RandomForestClassifier()
            RF.fit(train_X,train_Y)
            NB = GaussianNB()
            NB.fit(train_NX,train_NY)
            SVM = svm.SVC()
            SVM.fit(train_X,train_Y)
            LR = linear_model.LogisticRegression()
            LR.fit(train_NX,train_NY)

            DT_i_result.append(DT.score(test_X, test_Y))
            RF_i_result.append(RF.score(test_X, test_Y))
            NB_i_result.append(NB.score(test_NX, test_NY))
            SVM_i_result.append(SVM.score(test_X, test_Y))
            LR_i_result.append(LR.score(test_NX, test_NY))
        DT_result.append(DT_i_result)
        print(DT_result)
        RF_result.append(RF_i_result)
        print(RF_result)
        NB_result.append(NB_i_result) 
        print(NB_result)
        SVM_result.append(SVM_i_result) 
        print(SVM_result)
        LR_result.append(LR_i_result)
        print(LR_result)

    Classifier_List = ['DT','RF','NB','SVM','LR']
    for i in range(len(Result)):
        result_list = Result[i]
        outfile_name = "EXP2_"+Classifier_List[i]+".csv"
        CSV_Writer = csv.writer(open(outfile_name,'w',newline=''),delimiter=',',quotechar='|')
        for line in result_list:
            CSV_Writer.writerow(line)
    
    DT_result = readResult("EXP2_DT.csv")
    RF_result = readResult("EXP2_RF.csv")
    NB_result = readResult("EXP2_NB.csv")
    SVM_result = readResult("EXP2_SVM.csv")
    LR_result = readResult("EXP2_LR.csv")
    Result = [DT_result,RF_result,NB_result,SVM_result,LR_result]
    plot_result = []
    for i in range(len(DT_result)):
        for j in range(len(Result)):
            plot_result.append(Result[j][i])
            #print(i,j)
    for line in plot_result:
        print(line)   
    
    DT_result = []
    RF_result = []
    NB_result = []
    SVM_result = []
    LR_result = []
    Result = [DT_result,RF_result,NB_result,SVM_result,LR_result]

    Train_File = ["Train_9_0.csv","Train_12_0.csv","Train_15_0.csv","Train_18_0.csv"]
    #Train_File = ["Train_Ind_0.csv","Train_Inf_0.csv","Train_M_0.csv"]
    #Test_File = ["Test_9_0.csv","Test_12_0.csv","Test_18_0.csv"]

    Title_ALL = [Title_List,Title_List+["Introduction to Simulation","Information Security","Psychology"],
                Title_List+["Introduction to Simulation","Information Security","Psychology"]+["Engineering Economy","APP Design","HR Management"],
                Title_List+["Introduction to Simulation","Information Security","Psychology"]+["Engineering Economy","APP Design","HR Management"]+  ["Management Accounting","Computer Network","Decision Method"]]

    for i in range(len(Train_File)):
        #test_X, test_Y , test_NX, test_NY= readCSV(Test_File[i])
        train_X, train_Y, train_NX, train_NY = readCSV(Train_File[i])
        
        DT_i_result = []
        RF_i_result = []
        NB_i_result = [] 
        SVM_i_result = [] 
        LR_i_result = []

        for j in range(10):
            this_train_X = train_X[0+j*1000:1000+j*1000]
            this_train_Y = train_Y[0+j*1000:1000+j*1000]
            this_train_NX = train_NX[0+j*1000:1000+j*1000]
            this_train_NY = train_NY[0+j*1000:1000+j*1000]

            this_test_X = train_X[:0+j*1000]  + train_X[1000+j*1000:]
            this_test_Y = train_Y[:0+j*1000]  + train_Y[1000+j*1000:]
            this_test_NX = train_NX[:0+j*1000]  + train_NX[1000+j*1000:]
            this_test_NY = train_NY[:0+j*1000]  + train_NY[1000+j*1000:]

            this_train_X = this_train_X[:100]
            this_train_Y = this_train_Y[:100]
            this_train_NX = this_train_NX[:100]
            this_train_NY = this_train_NY[:100]



            DT = tree.DecisionTreeClassifier()
            DT.fit(this_train_X,this_train_Y)
            tree.export_graphviz(DT, out_file="EXP3_Num_helf_"+str(9+3*i)+"_"+str(j)+".txt", 
                         feature_names=Title_ALL[i],  
                         class_names=["[0]Industrial","[1]Information"],
                         filled=True, rounded=True,  
                         special_characters=True) 
            RF = RandomForestClassifier()
            RF.fit(this_train_X,this_train_Y)
            NB = GaussianNB()
            NB.fit(this_train_NX,this_train_NY)
            SVM = svm.SVC()
            SVM.fit(this_train_X,this_train_Y)
            LR = linear_model.LogisticRegression()
            LR.fit(this_train_NX,this_train_NY)

            DT_i_result.append(DT.score(this_test_X, this_test_Y))
            RF_i_result.append(RF.score(this_test_X, this_test_Y))
            NB_i_result.append(NB.score(this_test_NX, this_test_NY))
            SVM_i_result.append(SVM.score(this_test_X, this_test_Y))
            LR_i_result.append(LR.score(this_test_NX, this_test_NY))
        DT_result.append(DT_i_result)
        print(DT_result)
        RF_result.append(RF_i_result)
        print(RF_result)
        NB_result.append(NB_i_result) 
        print(NB_result)
        SVM_result.append(SVM_i_result) 
        print(SVM_result)
        LR_result.append(LR_i_result)
        print(LR_result)
    Classifier_List = ['DT','RF','NB','SVM','LR']
    for i in range(len(Result)):
        result_list = Result[i]
        outfile_name = "EXP3_Num_helf_"+Classifier_List[i]+".csv"
        CSV_Writer = csv.writer(open(outfile_name,'w',newline=''),delimiter=',',quotechar='|')
        for line in result_list:
            CSV_Writer.writerow(line)

    '''
## EXP 4
    DT_result = []
    RF_result = []
    NB_result = []
    SVM_result = []
    LR_result = []
    Result = [DT_result,RF_result,NB_result,SVM_result,LR_result]

    
    test_X, test_Y , test_NX, test_NY= readCSV("Test.csv")

    if_small = 1
    for i in range(11):
        Training_File = "Train_Error"+str(i)
        train_X, train_Y, train_NX, train_NY = readCSV(Training_File+".csv")
        
        DT_i_result = []
        RF_i_result = []
        NB_i_result = [] 
        SVM_i_result = [] 
        LR_i_result = []

        for j in range(10):
            this_train_X = train_X[0+j*1000:1000+j*1000]
            this_train_Y = train_Y[0+j*1000:1000+j*1000]
            this_train_NX = train_NX[0+j*1000:1000+j*1000]
            this_train_NY = train_NY[0+j*1000:1000+j*1000]

            if if_small != 0 :
                this_train_X = this_train_X[:100]
                this_train_Y = this_train_Y[:100]
                this_train_NX = this_train_NX[:100]
                this_train_NY = this_train_NY[:100]



            DT = tree.DecisionTreeClassifier()
            DT.fit(this_train_X,this_train_Y)
            tree.export_graphviz(DT, out_file=Training_File+"_"+str(if_small)+"_"+str(j)+".txt", 
                         feature_names=Title_List,  
                         class_names=["[0]Industrial","[1]Information"],
                         filled=True, rounded=True,  
                         special_characters=True) 
            RF = RandomForestClassifier()
            RF.fit(this_train_X,this_train_Y)
            NB = GaussianNB()
            NB.fit(this_train_NX,this_train_NY)
            SVM = svm.SVC()
            SVM.fit(this_train_X,this_train_Y)
            LR = linear_model.LogisticRegression()
            LR.fit(this_train_NX,this_train_NY)

            DT_i_result.append(DT.score(test_X, test_Y))
            RF_i_result.append(RF.score(test_X, test_Y))
            NB_i_result.append(NB.score(test_NX, test_NY))
            SVM_i_result.append(SVM.score(test_X, test_Y))
            LR_i_result.append(LR.score(test_NX, test_NY))
        DT_result.append(DT_i_result)
        print(DT_result)
        RF_result.append(RF_i_result)
        print(RF_result)
        NB_result.append(NB_i_result) 
        print(NB_result)
        SVM_result.append(SVM_i_result) 
        print(SVM_result)
        LR_result.append(LR_i_result)
        print(LR_result)
    Classifier_List = ['DT','RF','NB','SVM','LR']
    for i in range(len(Result)):
        result_list = Result[i]
        outfile_name = "Training_File_"+str(if_small)+"_"+Classifier_List[i]+".csv"
        CSV_Writer = csv.writer(open(outfile_name,'w',newline=''),delimiter=',',quotechar='|')
        for line in result_list:
            CSV_Writer.writerow(line)