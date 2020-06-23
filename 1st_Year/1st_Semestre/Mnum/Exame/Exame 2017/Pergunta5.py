# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 18:16:06 2020

@author: Hugo
"""

f = lambda x,y : -1.1*x*y+12*y+7*x**2-8*x
fx = lambda x,y : -1.1*y+14*x-8
fy = lambda x : 12-1.1*x

def gradiente(x,y,h):
    xn = x
    yn = y
    for i in range(1):
        
        x = xn
        y = yn
        
        xn = x -h*fx(x,y)
        yn = y -h*fy(x)
        
        if(f(xn,yn) < f(x,y)):
            h *= 2
            print("k")
        else:
            print("l")
            h/= 2
            xn = x -h*fx(x,y)
            yn = y -h*fy(x)
        
        
    return xn,yn

x0 = 3
y0 = 1
h = 0.1

gra = gradiente(x0,y0,h)
print(f(gra[0],gra[1]))
print(f(x0,y0))



