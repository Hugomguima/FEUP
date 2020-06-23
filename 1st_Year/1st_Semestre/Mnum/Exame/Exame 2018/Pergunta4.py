# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 20:59:03 2020

@author: Hugo
"""

#Não connsegui perceber qual era o step nem o valor inicial de x
#Talvez seja por causa de a pergunta ser por caixinhas, e teria que se escolher

f = lambda z : z
g = lambda y,z : -7*z - 4*y


def euler(x,y,z,h):
    
    yn = y
    zn = z
    print(x,y,z)
    
    for i in range(3):
        y = yn
        z = zn
        
        x += h
        yn = y + h*f(z)
        zn = z + h*g(y,z)
        
        print(x,yn,zn)

euler(0.4,2,1,0.2)
        

