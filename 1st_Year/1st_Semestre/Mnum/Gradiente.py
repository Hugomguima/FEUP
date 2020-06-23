# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 14:58:30 2019

@author: Hugo
"""

#Pesquisa Multidimensioanal
#Método do Gradiente


def gradiente(f,fx,fy,x0,y0,h):
    
    xn = 100 #Valores bem difernetes
    yn = 100
    xn1 = x0
    yn1 = y0
    
    while((abs(xn1 - xn) > 10**-3) and (abs(yn1 - yn) > 10**-3) ):

        xn = xn1
        yn = yn1
        xn1 = xn - h*fx(xn,yn)
        yn1 = yn - h*fy(xn,yn)
        
        if(f(xn1,yn1) < f(xn,yn)): #good
            h = h*2
            continue
            
        else:#bad
            h = h / 2
            xn1 = xn - h*fx(xn,yn)
            yn1 = yn - h*fy(xn,yn)
            
    return xn1,yn1

f = lambda x,y : y**2 - 2*x*y - 6*y + 2*(x**2) + 12
fx = lambda x,y : 4*x - 2*y
fy = lambda x,y : 2*y - 2*x - 6
x0 = 1
y0 = 1
h =1

result = gradiente(f,fx,fy,x0,y0,h)
print(result)
print(f(result[0],result[1]))



