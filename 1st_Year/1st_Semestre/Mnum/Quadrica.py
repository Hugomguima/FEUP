# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 15:50:32 2019

@author: Hugo
"""

#Pesquisa Multidimensioana
#Método da Qúadrica
from math import cos
from math import sin

#É apenas necesário :
#-Os valores das funções gradiente (fx,fy)
#-Os valores da inversa da Hessiana (hxx,hxy,hyx,hyy)

def quadrica(f,fx,fy,x0,y0):
    
    xn = 100 #Valores bem diferentes
    yn = 100 #Valores bem diferentes
    
    xn1 = x0 #Atribuição do valor de x inincial
    yn1 = y0 #Atribuição do valor de y inicial
    
    #A professora pediu 4 iterações no exercicio
    for i in range(4):
        xn = xn1
        yn = yn1
        xn1 = xn - hxx(xn)*fx(xn)
        yn1 = yn - hyy(yn)*fy(yn)
        
    return xn1,yn1

#Não é necessário escrever a função, mas está aqui escrita
#para que consiga saber qual é o enunciado quando estiver a estudar
f = lambda xn,yn : sin(yn)+yn**2/4+cos(xn)+xn**2/4-1

fx = lambda xn : xn/2-sin(xn) #Derivada de f em ordem a x
fy = lambda yn : cos(yn)+yn/2 #Derivada de f em ordem a y

#Valores da inversa da Hessiana
hxx = lambda xn :1/(1/2-cos(xn)) #Inversa da Hessiana[0][0]
hyy = lambda yn: 1/(1/2-sin(yn)) #Inversa da Hessiana[1][1]
#Os restantes cmoponentes da Inversa da Hessiana foram omitidos,
#porque tendo em conta a função dada, são nulos, portanto, desnecessários
    
x0 = 0  #Valor inicial de x
y0 = 0  #Valor inicial de y


result = quadrica(f,fx,fy,x0,y0)
print(result)
print(f(result[0],result[1]))