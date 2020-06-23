# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 15:32:25 2019

@author: Hugo
"""

import math
#Pesquisa de minimo pela Regra Áurea

#Método para a pesquisa de 3 pontos que contém o minimo,
#De acordo com uma guess e um step
def pesquisa(f,guess,step):
    
    if (f(guess) < f(guess+step)):
        step *= -1
        
    x0 = guess
    x1 = guess + step
    x2 = guess + 2*step
    
    while(f(x1)>f(x2)):
        x0 = x1
        x1 = x2
        x2 = x2+step
    print(x0,x1,x2)
    return (x0,x1,x2)

def aurea(f,x1,x2,precision):
    #f é a função dada no enunciado
    #x1 é o valor inferior do intevalo de pesquisa
    #x2 é o valor superior do intervalo de pesquisa
    
    B = (5**(1/2)-1)/2 #Constante de secçao aurea
    A = B**2
    x3 = 0 #Valor novo obtido como aproximação ao extremo pelo lado esquerdo
    x4 = 0 #Valor novo obtido como aproximação do extremo do lado direito
    first = True
    
    while(abs(x2-x1) >= precision):
        x3 = x1 + A*(x2-x1) #calculo de nova aproximação de x3
        x4 = x1 + B*(x2-x1) #caluclo de nova aproximação de x4
        
        #Alteração dos valores de x1 e x2 conforme o menor valor
        #...na novas aproximações de x3 e x4
        #if( f(x3) > f(x4)):#Usar este para calcular o maximo
        if( f(x3) < f(x4)): #Usar este para calcular o minimo
            x2 = x4
            first = True
        else:
            x1 = x3
            first = False
            
    if (first):
        return x2
    else:
        return x4
    
#Dados
f = lambda x: (2*x+1)**2 - 5 * math.cos(10*x) #Função em que se quer procurar o minimo
precision = 10**(-3) #Precisão da procura
minimum = -1         #Valor que se sabe estar á esquerda do minimo
maximum = 0          #Valor que se sabe estar á direita do minimo
au = aurea(f,minimum,maximum,precision) #Passar os resultados para um vetor

print(au) #Dar print aos valore de x obtidos
print(f(au))#Dar print aos valores de f(x) obtidos
    
    
    
    
    