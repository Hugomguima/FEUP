# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:32:24 2019

@author: Hugo
"""

#Metodo de RUnka-Kutta-4
#Metodo de Ordem 4

def rk4(funcao,x,y,h,maximo):
    
    while(x < maximo):
        
        xn = x
        yn = y
        
        dy1 = h*f(x,y);
        dy2 = h*f(x + h/2, y + dy1/2)
        dy3 = h*f(x + h/2, y + dy2/2)
        dy4 = h*f(x + h, y + dy3)
        
        x = xn + h
        y = yn + dy1/6 + dy2/3 + dy3/3 + dy4/6
#        print("x =",x,"y =",y)
    
    return y

#Dados
#Funcao
f = lambda x,y : x**2 + y**2
#Altura
h = 0.0125
#Ponto inicial
x = 0
y = 0
#Intervalo superior do integral
maximum = 1.39999999999

s = rk4(f,x,y,h,maximum)
s1= rk4(f,x,y,h/2,maximum)
s2= rk4(f,x,y,h/4,maximum)

qc = (s1-s)/(s2-s1)#Formula do quociente de convergencia
erro = (s2-s1)/15#Formula do ero de convergencia de 4ª ordem

print()
print("Método de Runga-Kutta-4:")

print()
print("S =",s) #Resultado
print("S1 =",s1)#Resultado com metade da altura
print("S2 =",s2,'\n')#Resultado com um quarto da altura
print("Qc =",qc)#Quociente de Convergencia
print("Erro =",erro)#Erro de convegencia


