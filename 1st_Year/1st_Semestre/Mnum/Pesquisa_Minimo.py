# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:21:46 2019

@author: Hugo
"""
import math
pi = math.pi

#Método de pesquisa de um minimo numa função de 1 só parametro
#É necessário usar estas 3 funções para se arranjar um valor concreto

#Método para a pesquisa de 3 pontos que contém o minimo,
#De acordo com uma guess e um step
def pesquisa(f,guess,step):
    
    if (f(guess) < f(guess+step)):
        step *= -1
        
    x0 = guess
    x1 = guess + step
    x2 = guess + 2*step
    
    while(f(x1)>f(x2)):
        x0 += step
        x1 += step
        x2 += step
    print(x0,x1,x2)
    return (x0,x1,x2)

#Função para se encontrar 3 pontos proximos com uma certa precisão
def terços(f,a,b,precision):
    
    while(abs(b-a) > precision):
        prop = (b-a)/3
        c = a + prop
        d = b - prop
        
        if( f(c) > f(d)):
            a = c
        else:
            b = d
    #Caso a ultima alteração seja no b, o ponto a vai ser igual ao c,
    #logo, retornam-se os 3 pontos não iguais
    if (a == c):
        return [c,d,b]
    #Caso a ultima alteração seja no a, o ponto b vai ser igual ao d,
    #logo, retornam-se os 3 pontos não iguais
    else:
        return [a,c,d]
    
#função para se obter o resultado
def quadrica(f,x1,x2,x3):
    f1 = f(x1) #Reduzir parentesis para o uso de f(x1)
    f2 = f(x2) #Reduzir parentesis para o uso de f(x2)
    f3 = f(x3) #Reduzir parentesis para o uso de f(x3)
    h = x2-x1  
    return x2+(h*(f1-f3))/(2*(f3-2*f2+f1))

#Dados
f = lambda x: math.sin(x) #Função em que se quer procurar o minimo
guess = 2  #Valor proximo do minimo local
step = 0.1 #Step de incremento usada na pesquisa
precision = 10**(-5) #Precisão de pesquisa entre os intervalos dos terços

p = pesquisa(f,guess,step)
t = terços(f,p[0],p[2],step,precision)

print(t[0],t[1],t[2])
print(quadrica(f,t[0],t[1],t[2]))




