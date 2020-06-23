# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 13:13:12 2020

@author: Hugo
"""

f = lambda y : y
g = lambda x,y : (-y*-20*x)/20

def euler(t,x,y,h):
    
    tn = t
    xn = x
    yn = y
    
    for i in range(100):
        
        t = tn
        x = xn
        y = yn
        
        tn += h
        xn += h*f(y)
        yn += h*g(x,y)
    
    return (t,x,y)


t=0
x=1
y=0
h=0.1

print(euler(t,x,y,h))