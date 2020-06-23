# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 21:36:19 2020

@author: Hugo
"""

import math


f = lambda x: x**3 -10*math.sin(x)+2.8


#Método da Bisseção

def bissecao(a,b):
    
    for i in range(3):
    
        result = (a+b)/2
        print(a,result,b)
        
        if(f(a) * f(result) < 0):
            b = result
        else:
            a = result
        
    return result

print(bissecao(1.5,4.2))