# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 12:47:31 2018

@author: Hugo
"""

def override(l1, l2):
    
    lista = []
    
    for i in l2:
        if i[0] not in lista:
            lista.append(i)
    
    for j in l1:
        if j[0] not in lista:
            lista.append(j)
            
    return sorted(lista)
    
print(override([('c','d'),('c','e'),('a','b'),('a', 'd')],
[('a','c'),('b','d')]))
    