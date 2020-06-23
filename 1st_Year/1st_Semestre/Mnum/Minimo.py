# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:21:46 2019

@author: Hugo
"""
import math
#Método de pesquisa de umminimo numa função de 1 só parametro

def pesquisa(function,guess,step):
    
    if (f(guess) < f(guess+step)):
        step *= -1
        
    x0 = guess
    x1 = guess + step
    x2 = guess + 2*step
    
    while(f(x1)>f(x2)):
        x0 = x1
        x1 = x2
        x2 = x2+step
    print(x0,x1,x2)
        
    
    return 0;

f = lambda x: math.sin(x)
guess = 2
step = 0.1

method(f,guess,step)
