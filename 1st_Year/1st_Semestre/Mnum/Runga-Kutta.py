# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 15:35:35 2019

@author: Hugo
"""

#Método de Runga-Kutta-2
#Método de 2ª Ordem


def rk2(funcao,x,y,h,maximo):
    
    while(x < maximo):
        
        xn = x
        yn = y
        
        x = xn + h
        y = yn + h*f(xn + h/2,yn+h/2*f(xn,yn))
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
s = rk2(f,x,y,h,maximum)
s1= rk2(f,x,y,h/2,maximum)
s2= rk2(f,x,y,h/4,maximum)

qc = (s1-s)/(s2-s1)#Formula do quociente de convergencia
erro = (s2-s1)/3#Formula do ero de convergencia de 2ª ordem

print()
print("Método de Runga-Kutta-2:")

print()
print("S =",s) #Resultado
print("S1 =",s1)#Resultado com metade da altura
print("S2 =",s2,'\n')#Resultado com um quarto da altura
print("Qc =",qc)#Quociente de Convergencia
print("Erro =",erro)#Erro de convegencia















