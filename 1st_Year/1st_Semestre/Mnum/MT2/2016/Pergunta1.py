# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 17:16:43 2019

@author: Hugo
"""

import math
#Pergunta 1 MT2 2016

#Metodo de Euler

f = lambda T,C : -pow(math.e,-0.5/(T+273))*C
g = lambda T,C : 20*pow(math.e,-0.5/(T+273))*C - 0.5*(T-20)



def euler(t,C,T,h):

    for i in range(3):
        
#        print(t,C,T)
        
        t += h
        C += h*f(T,C)
        T += h*g(T,C)
    
    return C

#Pergunta 2

#Método de RK4

t = 0
T = 15
C = 1
h = 0.25

for i in range(3):
    print(t,C,T)
    
    df1 = h*f(T,C)
    dg1 = h*g(T,C)
    
    df2 = h*f(T+dg1/2,C+df1/2)
    dg2 = h*g(T+dg1/2,C+df1/2)
    
    df3 = h*f(T+dg2/2,C+df2/2)
    dg3 = h*g(T+dg2/2,C+df2/2)
    
    df4 = h*f(T+dg3,C+df3)
    dg4 = h*g(T+dg3,C+df3)
    
    
    t += h
    C += df1/6 + df2/3 + df3/3 + df4/6
    T += dg1/6 + dg2/3 + dg3/3 + dg4/6
print()


#Quocientes de convergência

h = 0.25
t = 0
T = 15
C = 1

S = euler(t,C,T,h)
S1 = euler(t,C,T,h/2)
S2 = euler(t,C,T,h/4)

Qc = (S1-S)/(S2-S1)
E = (S2-S1)/1

print(S1)
print(S2)
print(Qc)
print(E)    







    
    
    