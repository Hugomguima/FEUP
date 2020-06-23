# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 18:45:30 2020

@author: Hugo
"""

f = lambda x,y : y**2-x*y+11*y+3*x**2-8*x
fx = lambda x,y : -y+6*x-8
fy = lambda x,y : 2*y-x+11

def gradiente(x,y):
    h = 0.5
    
    xn = x
    yn = y
    
    
    for i in range(2):
        
        x = xn
        y = yn
        
        xn = x - h*fx(x,y)
        yn = y - h*fy(x,y)
        
        if(f(xn,yn) < f(x,y)):
            h*=2
        else:
            h/=2
            xn = x - h*fx(x,y)
            yn = y - h*fy(x,y)
            
        print(x,f(x,y))
        print(y)
        print()



gradiente(2,2)


