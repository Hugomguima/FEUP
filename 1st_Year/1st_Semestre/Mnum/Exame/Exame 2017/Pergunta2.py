# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:03:15 2020

@author: Hugo
"""
import math


f = lambda x: (1 +(2.5*math.e**(2.5*x))**2 )**(1/2)
g = lambda x: math.sqrt(1 + pow(2.5 * pow(math.e, 2.5 * x), 2))


def trapezios(f,a,b,h):
    
    n = int((b-a)/h)
    St = f(a) + f(b)
    
    for i in range (1,n):
#        print(St)
        St += 2 * f(a + i*h)
    
    return St * h/2

def simpson(f,a,b,h):
    
    n = int((b-a)/h)
    Ss = f(a) + f(b)
    
    for i in range(1,n):
        if(i % 2 == 0):
            Ss += 2 * f(a + i*h)
        else:
            Ss += 4 * f(a + i*h)
          
    return Ss * h/3

a = 0
b = 1
h = 0.125

St = trapezios(f,a,b,h)
St1 = trapezios(f,a,b,h/2)
St2 = trapezios(f,a,b,h/4)
Qct = (St1-St)/(St2-St1)
Et = (St2-St1)/3

Ss = simpson(f,a,b,h)
Ss1 = simpson(f,a,b,h/2)
Ss2 = simpson(f,a,b,h/4)
Qcs = (Ss1-Ss)/(Ss2-Ss1)
Es = (Ss2-Ss1)/15


print(h,h)
print(h/2,h/2)
print(h/4,h/4)
print(St,Ss)
print(St1,Ss1)
print(St2,Ss2)
print(Qct,Qcs)
print(Et,Es)

















