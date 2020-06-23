# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 19:26:35 2019

@author: Hugo
"""

#Pergunta 2 MT2 2015

#Metodo de Gauss Jacobi

f1 = lambda x2,x3,x4:(1+x2+x3-x4)/4.5
f2 = lambda x1,x3,x4:(-1+x1-x3+x4)/4.5
f3 = lambda x1,x2,x4:(-1+x1-2*x2+x4)/4.5
f4 = lambda x1,x2,x3:(-2*x1+x2+x3)/4.5


x1n = 0.25
x2n = 0.25
x3n = 0.25
x4n = 0.25

for i in range(2):
    
    x1 = x1n
    x2 = x2n
    x3 = x3n
    x4 = x4n
    
    x1n = f1(x2,x3,x4)
    x2n = f2(x1,x3,x4)
    x3n = f3(x1,x2,x4)
    x4n = f4(x1,x2,x3)
    
    print(x1n,x2n,x3n,x4n)
    

