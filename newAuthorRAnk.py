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
#tuples={}
#m=defaultdict(list)
for line in lines1:
    node=line.strip().split(' ')
    t1=node[0]
    t2=node[1]
    ##print(line)
    #uples=(line)
    #m[t1].append(t2)
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
for i in x:
    dif=dif+abs(xlast[i]-x[i])
eps=.000001
while (dif>eps):
    dif = 0
    for i in x:
        xlast[i] = x[i]

    sum = 0
    for n in x:
        count=0
        for i in W[n]:
            count+=1
            if(inDegree[i]>0):
                x[n]=x[n]+(xlast[i]/inDegree[i])
        if (count > 0):
            x[n] = (x[n] / (math.sqrt(count)))
        sum=sum+x[n]
    for n in x:
        x[n]=(x[n]/sum)*N
        dif= dif+abs(xlast[n]-x[n])
print(x)

items=x.items()
print(sorted(items, key = lambda kv:(kv[1], kv[0])))

