# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 16:25:25 2020

@author: Hugo
"""

f = lambda x : x**4-4*x**3+x-3
g = lambda x : (4*x**3-x+3)**(1/4)

def picard(x):
    
    for i in range(3):
        print(x)
        x = g(x)
        
        
picard(3.5)