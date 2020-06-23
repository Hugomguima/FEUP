# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 21:04:11 2020

@author: Hugo
"""

from math import sqrt
#O melhor Método a utilizar é o método da secção áurea

f = lambda x : x**2+x**4

def pesquisa(x):
    h = 0.1
    
    if(f(x + h) > f(x)):
        h *=-1
    
    x0 = x
    x1 = x + h
    x2 = x + 2*h
    
    while(f(x1) > f(x2)):
        x0 += h
        x1 += h
        x2 += h
        
    return [x0,x1,x2]
    
def aurea(x1,x2):
    
    B = (sqrt(5)-1)/2
    A = B**2
    
    x3 = 0
    x4 = 100
    
    print(x1,x2)
    for i in range(10):  
        
        x3 = x1 + A*(x2-x1)
        x4 = x1 + B*(x2-x1)
        
        if (f(x3) < f(x4)):
            x2 = x4
        else:
            x1 = x3
        print(x1,x2)
            
    if(x1 == x3):
        return [x1,x4,x2]
    else:
        return [x1,x3,x2]

p = pesquisa(2)
a = aurea(-1,1)




