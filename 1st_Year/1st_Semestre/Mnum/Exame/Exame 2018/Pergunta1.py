# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 19:34:08 2020

@author: Hugo
"""
#import math
from math import sin
from math import cos
from math import e

f = lambda x,y : sin(y+x)-e**(x-y)
g = lambda x,y : cos(y+x)-x**2*y**2

fx = lambda x,y: cos(y+x)-e**(x-y)
fy = lambda x,y: cos(y+x)+e**(x-y)

gx = lambda x,y: -sin(y+x)-2*x*y**2
gy = lambda x,y: -sin(y+x)-2*x**2*y

J = lambda x,y: fx(x,y)*gy(x,y) - fy(x,y)*gx(x,y)
hn = lambda x,y: f(x,y)*gy(x,y) - g(x,y)*fy(x,y)
kn = lambda x,y : fx(x,y)*g(x,y) - gx(x,y)*f(x,y)

def newton(x,y):
    
    xn = x
    yn = y
    
    print(x,y)
    for i in range(2):
        x = xn
        y = yn
        
        xn -= hn(x,y)/J(x,y)
        yn -= kn(x,y)/J(x,y)
        print(xn,yn)
    


newton(0.5,0.25)