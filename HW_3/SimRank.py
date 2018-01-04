import csv
import numpy as np
import numpy.linalg as npl
import math

class Node :
    def __init__ (self,name):
        self.name = name
        self.in_node = []
        self.out_node = []
        self.authority = 0
        self.hub = 0

    def __repr__(self):
        return self.name

def findNode(name,list_node):
    if_find = 0
    the_node = None
    for node in list_node:
        if node.name == name:
            if_find = 1
            the_node = node
    if if_find == 0 :return None
    else:            return the_node


def growGraphByInfile(filename):
    List_Node = []
    with open(filename,'r') as infile:
        CSV_reader = csv.reader(infile,delimiter = ',')
        for row in CSV_reader :
            the_node_1 = findNode(row[0],List_Node)
            the_node_2 = findNode(row[1],List_Node)
            if the_node_1 == None :
                the_node_1 = Node(row[0])
                List_Node.append(the_node_1)
            if the_node_2 == None :
                the_node_2 = Node(row[1])
                List_Node.append(the_node_2)
            the_node_1.out_node.append(the_node_2)
            the_node_2.in_node.append(the_node_1)
    List_Node.sort(key = lambda node: int(node.name)) 
    return List_Node

def copyNode (Graph):
    New_List = [] 
    for node in Graph:
        new_Node = Node(node.name)
        new_Node.in_node = node.in_node[:]
        new_Node.out_node = node.out_node[:]
        new_Node.authority = node.authority
        new_Node.hub = node.hub
        New_List.append(new_Node)
    return New_List

def graphToMatrix(Graph):
    Num_Node = len(Graph)
    Matrix_Graph = [[0 for i in range(Num_Node)] for j in range(Num_Node)]

    for node in Graph:
        for out_node in node.out_node:
            Matrix_Graph[int(node.name)-1][int(out_node.name)-1] = 1
        for in_node in node.in_node:
            Matrix_Graph[int(in_node.name)-1][int(node.name)-1] = 1

    #for line in Matrix_Graph:
    #   print(line)
    return Matrix_Graph

def SimRank(node_M, C = 0.5,e = 0.01,print_iter = 0):
    Num_Node = len(node_M)   

    A_node_M = [[0 for i in range(Num_Node)] for j in range(Num_Node)]
    for i in range(Num_Node):
        for j in range(Num_Node):
            if node_M[i][j] == 1:
                norm = 0
                for z in range(Num_Node):
                    norm += node_M[z][j]
                A_node_M[i][j] = 1/norm

    W = np.mat(A_node_M)
    I = np.eye(Num_Node,Num_Node)
    M = np.mat(node_M)
    Et_1 = np.eye(Num_Node,Num_Node)
    t = 0 
    while True :
        t+=1
        Et = C*(W.T * Et_1 * W) 
        for i in range(Num_Node):
            Et[i,i] = 1
        Ee =  Et - Et_1    
        error = np.sum(Ee)

        if print_iter == 1 :
            print(t,error)

        if error < e :
            break
        else:
            print(Et)
            Et_1 = Et
    return Et


    #print(np.mat(Sim_Matrix))

if __name__ == '__main__' :

    filename = 'graph_3.txt'
    Node_Graph = growGraphByInfile(filename)
    for node in Node_Graph :
        print(node,"Out:",node.out_node,"In:",node.in_node) 

    Node_Matrix = graphToMatrix(Node_Graph)
    SR = SimRank(Node_Matrix,print_iter =1)
    print(SR)