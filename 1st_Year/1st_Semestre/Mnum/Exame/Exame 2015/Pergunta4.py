# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 19:45:58 2020

@author: Hugo
"""
import math
#Picard Peano

f = lambda x : math.e**x-4*x**2
g = lambda x : 2*math.log(2*x)

def picardPeano(x):
    
    x  = g(x)
    return x

x=1.1
print(x)
print(picardPeano(x))
print(g(x)-x)

