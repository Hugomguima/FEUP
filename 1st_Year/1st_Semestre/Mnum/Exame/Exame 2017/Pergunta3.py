# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 17:19:15 2020

@author: Hugo
"""
import math

#Alinea 1.
#A equação tem 2 raizes:
#Uma situada no intervalo [-6,-4]
#Outra situada no intevalo [1,3]


f = lambda x: math.e**x - x - 5 
g = lambda x: math.e**x - 5 
h = lambda x: math.log(5 + x)

df = lambda x: math.e**x - 1
dg = lambda x: math.e**x
dh = lambda x: 1/(x+5)

#Alinea 2.
#dg tem modulo menor que 1 no intervalo [-4,6], portanto pertence á regiao de convergencia
#dh tem modulo menor que 1 no intervalo [1,3], portanto pertence á regiao de convergencia

#Alinea 3.
#Metodo de Newton


x = 100
xn = 2
n = 0
while(abs(xn-x) > 10**-5):
    x = xn
    xn -= f(x)/df(x)
    n+=1
print(xn,n)   

#Método de Picard-Peano
x = 100
xn = 1.5
n = 0
while(abs(xn-x) > 10**-5):
    x = xn
    xn = g(x)
    n+=1

print(xn,n)

x = 100
xn = 2
n = 0
while(abs(xn-x) > 10**-5):
    x = xn
    xn = h(x)
    n+=1
    
print(xn,n)
    

