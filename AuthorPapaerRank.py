import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from numpy import linalg as LA
from collections import defaultdict
import math
import pandas as pd


G = nx.DiGraph()
fh1=open(r"C:\Users\Asus\OneDrive\Desktop\p25.txt")
lines1=fh1.readlines()
fh2=open(r"C:\Users\Asus\OneDrive\Desktop\P2A.txt")
lines2=fh2.readlines()

for line in lines1:
    node=line.strip().split(' ')
    t1=node[0]
    t2=node[1]
    G.add_edge(t1,t2)



"""for line in lines2:
    node=line.strip().split(' ')
    t1=node[0]
    t2=node[1]
    #print(line)
    #tuples=((line))
    #m[t1].append(t2)
    #m[t2].append(t1)
    G.add_edge(t1, t2)
    G.add_edge(t2, t1)"""

#print(G)
#r=(("p1","p2"),('p1','p3'),('p2','p3'),('p3','a3'),('a3','p3'),('a1','p3'),('p3','a1'),("p1","a1"),("a1","p1"),("p1","a2"),("a2","p1"),("p2","a2"),("a2","p2"),("p2","a3"),("a3","p2"))
#y=(("p1","p2"),("p1","a1"),("a1","p1"),("p1","a2"),("a2","p1"),("p2","a2"),("a2","p2"),("p2","a3"),("a3","p2"))
#y=(('p1','p2'),('p1','p3'),('p2','p3'))
#m=((2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(6,2),(7,3),(7,4),(8,5),(3,9),(8,7),(11,9),(13,9),(1,9),(1,10),(13,10),(6,11),(13,11),(7,12),(8,12),(13,12),(8,13))
#t=(('p1','p2'),('p1','p3'),('p2','p3'))
#print(y)
#G.add_edges_from(y)

W = nx.stochastic_graph(G, weight="weight")


N = W.number_of_nodes()
alpha=0.85




inDegree=G.in_degree
outDegree=G.out_degree
x = dict.fromkeys(W, 1)
dangling_weights = x
dangling_nodes = [n for n in W if W.in_degree(n, weight='weight') == 0.0]
print("Dangling Nodes",dangling_nodes)
p = dict.fromkeys(W, 1.0 / N)



xlast=dict.fromkeys(W,0)
dif=0
final=dict.fromkeys(W,0)
for i in x:
    dif=dif+abs(xlast[i]-x[i])
eps=.0000001
while (dif>eps):
    for i in x:
        xlast[i] = x[i]
    sum=0
    for n in x:
        for i in W[n]:
            if(inDegree[i]>0):
                x[n]+=(xlast[i]/inDegree[i])
        sum=sum+x[n]
    dif = 0
    for n in x:
        if(sum>0):
            x[n]=(x[n]/sum)*N
        dif = dif + abs(xlast[n] - x[n])

items=x.items()

print("Rank",sorted(items, key = lambda kv:(kv[1], kv[0])))

