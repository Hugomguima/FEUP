# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 18:05:02 2020

@author: Hugo
"""
import math

f = lambda C,T: -pow(math.e,(-0.5/(T+273)))*C 
g = lambda C,T: 30 * pow(math.e,(-0.5/(T+273)))*C - 0.5*(T-20)

#Metodo de Euler

def euler(t,C,T,h):
    
    Cn = C
    Tn = T
    for i in range(3):
        C = Cn
        T = Tn
        print(t,C,T)
        t += h
        Cn = C + h*f(C,T)
        Tn = T + h*g(C,T)
    return C,T

#Não dá print, este
def euler2(t,C,T,h):
    
    Cn = C
    Tn = T
    for i in range(400):
        C = Cn
        T = Tn
        t += h
        Cn = C + h*f(C,T)
        Tn = T + h*g(C,T)
    return C,T


def rk4(t,C,T,h):
    
    Cn = C
    Tn = T
    for i in range(3):
        C = Cn
        T = Tn
        
        print(t,C,T)

        dc1 = h*f(C,T)
        dt1 = h*g(C,T)
        
        dc2 = h*f(C + dc1/2,T + dt1/2)
        dt2 = h*g(C + dc1/2,T + dt1/2)
        
        dc3 = h*f(C + dc2/2,T + dt2/2)
        dt3 = h*g(C + dc2/2,T + dt2/2)
        
        dc4 = h*f(C + dc3,T + dt3)
        dt4 = h*g(C + dc3,T + dt3)
        
        t += h
        Cn = Cn + 1/6*(dc1 + 2*dc2 + 2*dc3 + dc4)
        Tn = Tn + 1/6*(dt1 + 2*dt2 + 2*dt3 + dt4)
        
    
    
t = 0
C = 2.5
T = 25
h = 0.25

print("Alinea a)")
e = euler(t,C,T,h)
e1 = euler2(t,C,T,h/2)
e2 = euler2(t,C,T,h/4)

Qc = (e1[0]-e[0])/(e2[0]-e1[0])
E = e2[0]-e1[0]

print()
print("Alinea b)")
rk4(t,C,T,h)

print()
print("Alinea c)")
print(h/2,e1[1])
print(h/4,e2[1])
print(Qc)
print(E)









