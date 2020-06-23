# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:52:13 2020

@author: Hugo
"""

#import math

#Método da Secção Aurea

def pesquisa(f,x,h):
    
    if(f(x+h) > f(x)):
        h *= -1
    x0 = x
    x1 = x + h
    x2 = x + 2*h
    
    while(f(x1) > f(x2)):
        
        x0 += h
        x1 += h
        x2 += h
    
    return [x0,x2]
    
def tercos(x1,x2):
    
    
    x3 = 0
    x4 = 0
    
    for i in range(100):
        prop = (x2-x1)/3
        x3 = x1 + prop
        x4 = x2 - prop
        
        if(f(x3) < f(x4)):
            x2 = x4
        else:
            x1 = x3
    
    if(x1 == x3):
       return [x1,x4,x2]
    else:
       return [x1,x3,x2]
    
    
def aurea(x1,x2):
    
    B = (5**0.5 - 1) / 2
    A = B**2
    x3 = 100
    x4 = 200
    for i in range(100):
        x3 = x1 + A*(x2-x1)
        x4 = x1 + B*(x2-x1)
        
        if(f(x3) < f(x4)):
            x2 = x4
        else:
            x1 = x3
        
    if(x1 == x3):
        return [x1,x4,x2]
    else:
        return [x1,x3,x2]


f = lambda x : (x-6)**2+x**4

pes = pesquisa(f,0.5,0.01)
au = aurea(1,30)
ter = tercos(1,30)

#print(pes)
print(au)
print(ter)



