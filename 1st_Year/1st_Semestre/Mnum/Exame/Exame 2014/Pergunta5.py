# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 16:10:03 2020

@author: Hugo
"""

from math import sqrt as sqrt
from math import cos as cos
from math import sin as sin
#Secção aurea

f = lambda x : 5*cos(x) - sin(x)

def aurea(x1,x2):
    
    B = (sqrt(5)-1)/2
    A = B**2
    
    x3 = 0
    x4 = 0
    
    for i in range(3):
        
        x3 = x1 + A*(x2-x1)
        x4 = x1 + B*(x2-x1)
        print(x1,x2,x3,x4)
        print(f(x1),f(x2),f(x3),f(x4))
        print()
        
        if(f(x3) < f(x4)):
            x2 = x4
        else:
            x1 = x3
    print()
    if(x1 == x3):
        return x1,x2,x4
    else:
        return x1,x3,x4
    
        

a = aurea(2,4)
print(a[1]-a[0])
    
