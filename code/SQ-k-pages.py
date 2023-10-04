#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pysat
from pysat.formula import CNF
from pysat.solvers import Lingeling, Minisat22


# In[2]:


n = 18
pages = 5


# In[3]:


edges = [[0 for _ in range(n)] for _ in range(n)]


# In[4]:


# complete graph
for i in range(n-1):
    for j in range(i+1,n):
        edges[i][j] = 1


# In[5]:


# variables + page assignment
variables = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
iter = 1
formula = CNF()
for i in range(n-1):
    for j in range(i+1,n):
        if edges[i][j]:
            for k in range(pages):
                variables[i][j][k] = iter
                iter += 1
            formula.append([variables[i][j][k] for k in range(pages)])


# In[6]:


# check forbidden configurations
for red_s in range(n-4):
    for black_s in range(red_s+1,n-3):
        for green_s in range(black_s+1,n-2):
            for black_e in range(green_s+1,n-1):
                for green_e in range(black_e+1,n):
                    for red_e in range(black_e+1,n):
                        if edges[red_s][red_e] and edges[green_s][green_e] and edges[black_s][black_e]:
                            for k in range(pages):
                                formula.append([-variables[red_s][red_e][k],-variables[green_s][green_e][k],-variables[black_s][black_e][k]])


# In[7]:


def print_sol():
    for i in range(n-1):
        for j in range(i+1,n):
            if edges[i][j]:
                for k in range(pages):
                    if sol[variables[i][j][k]-1] > 0:
                        print("("+str(i)+","+str(j)+") -> "+str(k))
                        break


# In[11]:


len = 0
for i in formula:
    len += 1
print(str(len))


# In[ ]:


with Lingeling(bootstrap_with=formula.clauses, with_proof=False) as l:
    print(l.solve())
    sol = l.get_model()
    #print(l.get_model())
    if l.solve():
        print_sol()
    #else:
        #print(l.get_proof())


# In[ ]:




