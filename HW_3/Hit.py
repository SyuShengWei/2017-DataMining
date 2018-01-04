import csv
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
    
    #def __cmp__(self,other):
    #    return cmp(int(self.name),int(other.name))

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

def Hit(Graph,e = 0.01) :
    iteration = 0
    for node in Graph:
        node.authority = 1
        node.hub = 1
    Graph_Old = copyNode(Graph)
    while True:
    ##calculate authority
        iteration+=1
        #print(iteration)
        norm = 0 #num for normalization
        for node in Graph:
            node.authority = 0
            for in_node in node.in_node :
                node.authority += in_node.hub
            norm += math.pow(node.authority,2)
        norm = math.sqrt(norm)
        ##normalize
        for node in Graph:
            node.authority = node.authority/norm
    ##calculate hub
        norm = 0
        for node in Graph :
            node.hub = 0 
            for out_node in node.out_node:
                node.hub += out_node.authority
            norm += math.pow(node.hub,2)
        norm = math.sqrt(norm)
        for node in Graph:
            node.hub = node.hub/norm
    ##break condiction        
        e_auth = 0
        e_hub = 0
        for i in range( len(Graph) ):
            e_auth += abs( Graph[i].authority - Graph_Old[i].authority)
            e_hub  += abs( Graph[i].hub - Graph_Old[i].hub)
        if (e_auth+e_hub) < e :
            #print(e_auth+e_hub)
            print(iteration)
            break
        else:
            #print(e_auth+e_hub)
            Graph_Old = copyNode(Graph)

if __name__ == '__main__' :

    filename = 'graph_3.txt'
    Node_Graph = growGraphByInfile(filename)
    for node in Node_Graph :
        print(node,"Out:",node.out_node,"In:",node.in_node) 
    

    Hit(Node_Graph)
    for node in Node_Graph :
        print(node,"Auth:",node.authority,"Hub:",node.hub)


