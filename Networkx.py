# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:50:04 2022

@author: HP
"""
"""
# Draw a simple graph
import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()

G.add_node(1)

G.add_node(2)

G.add_node(3)

G.add_edge(1,2)

G.add_edge(2,3)

G.add_edge(1,3)

nx.draw(G)

plt.show()

#Using list to create the same graph
import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()

l=[1,2,3]
G.add_nodes_from(l)
G.add_edge(1,2)

G.add_edge(2,3)

G.add_edge(1,3)

nx.draw(G)

plt.show()
"""

# Complete Graph with multiple nodes 
import networkx as nx
import matplotlib.pyplot as plt
G=nx.complete_graph(10)



nx.draw(G)

plt.show()
