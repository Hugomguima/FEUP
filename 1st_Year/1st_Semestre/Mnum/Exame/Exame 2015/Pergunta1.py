# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 19:24:44 2020

@author: Hugo
"""

#Método de Euler

f = lambda T : -0.25*(T-37)


def euler(t,T,h):
    
    for i in range(2):
        
        t += h
        T += h*f(T)

    return t,T

t = 5
T = 3
h= 0.4
e = euler(t,T,h)
print(e)