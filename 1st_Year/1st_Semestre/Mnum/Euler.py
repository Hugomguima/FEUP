# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 15:13:25 2019

@author: Hugo
"""

#Método de Euler
#Método de 1ª Ordem


def euler(funcao,x,y,h,maximo):
    
    while(x < 1.3999):
        
        xn = x
        yn = y
        
        x = xn + h
        y = yn + h*f(xn,yn)
#        print("x =",x,"y =",y)
    return y

#Dados
#Funcao
f = lambda x,y : x**2 + y**2
#Altura
h = 0.1
#Ponto inicial
x = 0
y = 0
#Intervalo superior do integral
maximum = 1.39
#Quocientes de convergencia
#Por definição, divide-se a meio a altura de Sn para Sn+1
s = euler(f,x,y,h,maximum)
s1= euler(f,x,y,h/2,maximum)
s2= euler(f,x,y,h/4,maximum)

qc = (s1-s)/(s2-s1)#Formula do quociente de convergencia
erro = (s2-s1)/1#Formula do ero de convergencia de 1ª Ordem

print()
print("Método de Euler:")

print()
print("S =",s) #Resultado
print("S1 =",s1)#Resultado com metade da altura
print("S2 =",s2)#Resultado com um quarto da altura

print()
print("Qc =",qc)#Quociente de Convergencia
print("Erro =",erro)#Erro de convegencia



