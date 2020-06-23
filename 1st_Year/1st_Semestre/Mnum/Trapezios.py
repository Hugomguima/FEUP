# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:18:07 2019

@author: Hugo
"""
import math



def trapezio(f,a,b,n):
    
    St = f(a)
    
    h = (b-a)/n
    
    for i in range (1,n):
        St += 2*f(a+i*h)
    St += f(a+n*h)
    St = (h/2)*St
    return St;
    
    
def simpson(f,a,b,n):
    Ss = f(a)
    
    h = (b-a)/n
    
    for i in range (1,n):
        if(i % 2 == 0):
            Ss += 2*f(a+i*h)
        else:
            Ss += 4*f(a+i*h)
  
    Ss += f(a+n*h)
    Ss = (h/3)*Ss
    return Ss


#Metodo dos trapezios

#funcao
f = lambda x: (math.sin(x))/(x**2)
def g(x):
    return pow(1+1.5*pow(math.e,1.5*x),1/2)

print("St =",trapezio(f,math.pi / 2 ,math.pi,4))
print("Ss =",simpson(f,math.pi/2 ,math.pi,4))


#Quociente de convergencia dos trapezios (QCt)

St0 = trapezio(f,math.pi / 2 ,math.pi,4)
St1 = trapezio(f,math.pi / 2 ,math.pi,4*2)
St2 = trapezio(f,math.pi / 2 ,math.pi,4*2*2)

QCt = (St1 - St0) / (St2 - St1)

print("QQt =",QCt)

#Quociente de convergencia dos simpsons (QCs)

Ss0 = simpson(f,math.pi / 2 ,math.pi,4)
Ss1 = simpson(f,math.pi / 2 ,math.pi,4*2)
Ss2 = simpson(f,math.pi / 2 ,math.pi,4*2*2)

QCs = (Ss1 - Ss0) / (Ss2 - Ss1)

print("QQs =",QCs)








