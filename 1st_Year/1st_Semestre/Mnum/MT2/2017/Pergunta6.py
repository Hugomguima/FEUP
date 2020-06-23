# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:55:09 2019

@author: Hugo
"""

#Pergunta 5 MT2 2017

#EDO de grau superior

#Método de Euler

tn = 1
yn = 1
zn = 0
h = 0.25

#f = lambda z : z
g = lambda t,z : 2 + pow(t,2) + t*z


for i in range(3):
    t = tn
    y = yn
    z = zn
    
    tn = t + h
    yn = y + h*z
    zn = z + h*g(t,z)
    print(t,y)
    
print()
#Método de Runka-Kutta 4ªa ordem
    
t = 1
y = 1
z = 0
h = 0.25


for i in range (3):
    
    print(t,y)
    
    df1 = h*z
    dg1 = h*g(t,z)
    
    df2 = h*(z + dg1/2)
    dg2 = h*g(t + h/2,z + dg1 / 2)
    
    df3 = h*(z + dg2/2)
    dg3 = h*g(t + h/2, z + dg2/2 )
    
    df4 = h*(z+ dg3)
    dg4 = h*g(t + h, z + dg3 )
    
    t+= h
    y+= df1/6 + df2/3 + df3/3 + df4/6
    z+= dg1/6 + dg2/3 + dg3/3 + dg4/6
    
    
    
    








