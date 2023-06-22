# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 18:27:59 2022

@author: HP
"""
'''
# 1 st Model
import networkx as nx
import random
import matplotlib.pyplot as plt
G=nx.gnp_random_graph(10,0.5,directed=True)
nx.draw(G,with_labels=True)
plt.show()
#x is the random source node
x=random.choice([i for i in range(G.number_of_nodes())])
dict_counter={}
for i in range(G.number_of_nodes()):
    dict_counter[i]=0
dict_counter[x]=dict_counter[x]+1
for i in range(10000000):
    list_n=list(G.neighbors(x))
    if(len(list_n)==0):#If x is a sink
        x=random.choice([i for i in range(G.number_of_nodes())])
        dict_counter[x]=dict_counter[x]+1
    else:
        x=random.choice(list_n)#Choose a node randomly from the given set of nodes
        dict_counter[x]=dict_counter[x]+1

p=nx.pagerank(G)
print(p)
print(dict_counter)
 '''

#Model 2

import networkx as nx
import random
import matplotlib.pyplot as plt



def add_edges():
    nodes=list(G.nodes)
    for s in nodes:
        for t in nodes:
            if s!=t:
                ran=random.random()
                if ran<=0.5:
                    G.add_edge(s,t)
                    
    return G

def assign_points(G):
    nodes=list(G.nodes())
    p=[]
    for each in nodes:
        p.append(100)
    return p

def distribute_points(G,points):
    nodes=list(G.nodes())
    new_point=[]
    for i in range(len(nodes)):
        new_point.append(0)
    for n in nodes:
        out=list(G.out_edges(n))
        if len(out)==0:
            new_point[n]=new_point[n]+points[n]
        else:
            share=points[n]/len(out)
            for (source,target) in out:
                new_point[target]=new_point[target]+share
    return new_point
              
def keep_distributing(points,G):
    while True:
        new_points=distribute_points(G,points)
        print(new_points)
        points=new_points
        stop=input("Press # to stop or any other key to continue")
        if stop=='#':
            break
    return new_points

    
G=nx.DiGraph()
G.add_nodes_from([i for i in range(1,11)])
G=add_edges()

#Visualise the graph
nx.draw(G,with_labels=True)
plt.show()

#Assign Initial points
points=assign_points(G)

#KEEP DISTRIBUTING
final_pointd=keep_distributing(points,G)














   