# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 18:30:38 2020

@author: Hugo
"""

f = lambda z : z
g = lambda t,z:0.+t**2+t*z

def euler(t,y,z,h):
    
    yn = y
    zn = z
    
    print(t,y)
    for i in range(2):
        
        y = yn
        z = zn
        
        t += h
        yn += h*f(z)
        zn += h*g(t,z)
        print(t,y)

def rk4(t,y,z,h):
    yn = y
    zn = z
    
    print(t,y)
    for i in range(2):
        
        y = yn
        z = zn
        
        dy1 = h*f(z)
        dz1 = h*g(t,z)
        
        dy2 = h*f(z + dz1/2)
        dz2 = h*g(t + h/2,z + dz1/2)
        
        dy3 = h*f(z + dz2/2)
        dz3 = h*g(t + h/2,z + dz2/2)
        
        dy4 = h*f(z + dz3)
        dz4 = h*g(t + h,z + dz3)
        
        t += h
        yn += 1/6*(dy1 + 2*dy2 + 2*dy3 + dy4)
        zn += 1/6*(dz1 + 2*dz2 + 2*dz3 + dz4)
        
        print(t,y)
        
        
        
        
t = 0
y = 0
z = 1
h = 0.25

euler(t,y,z,h)
print()
rk4(t,y,z,h)
