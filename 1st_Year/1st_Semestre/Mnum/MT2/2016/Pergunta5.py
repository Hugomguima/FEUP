# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:38:28 2019

@author: Hugo
"""

#Pergunta 5 MT2 2016

#Metodo de Gauss-Seidel

g1 = lambda x1,x2,x3,x4 : 6*x1+0.5*x2+3*x3+0.25*x4 - 2.5
g2 = lambda x1,x2,x3,x4 : 1.2*x1+3*x2+0.25*x3+0.2*x4 - 3.8
g3 = lambda x1,x2,x3,x4 : -1*x1+0.25*x2+4*x3+2*x4 - 10
g4 = lambda x1,x2,x3,x4 : 2*x1+4*x2+1*x3+8*x4 - 7

f1 = lambda x2,x3,x4 : (-0.5*x2-3*x3-0.25*x4 + 2.5)/6
f2 = lambda x1,x3,x4 : (-1.2*x1-0.25*x3-0.2*x4 + 3.8)/3
f3 = lambda x1,x2,x4 : (+1*x1-0.25*x2-2*x4 + 10)/4
f4 = lambda x1,x2,x3 : (-2*x1-4*x2-1*x3 + 7)/8

x1 = 0
x2 = 0
x3 = 0
x4 = 0

for i in range(2):
    
    print(x1,x2,x3,x4)
    x1 = f1(x2,x3,x4)
    x2 = f2(x1,x3,x4)
    x3 = f3(x1,x2,x4)
    x4 = f4(x1,x2,x3)

    
    