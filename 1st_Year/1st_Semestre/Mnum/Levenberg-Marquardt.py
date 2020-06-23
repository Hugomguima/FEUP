# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 14:59:39 2019

@author: Hugo
"""

#Pesquisa Multidimensional
#Método de Levenberg-Marquardt
#Combinação dos Métodos do Gradiente e da Quárdrica


#É apenas necesário :
#-Os valores das funções gradiente (fx,fy)
#-Os valores da inversa da Hessiana (hxx,hxy,hyx,hyy)

def LevenbergMarquardt(f,fx,fy,hxx,hxy,hyx,hyy,y0,lm):
    
    xn = 1 #Valores bem diferentes
    yn = 1 #Valores bem diferentes
    
    xn1 = x0 #Atribuição do valor de x inincial
    yn1 = y0 #Atribuição do valor de y inicial
    
    #A professora pediu 4 iterações no exercicio
    for i in range(100):
        xn = xn1
        yn = yn1
        
        xn1 = xn - (hxx*fx(xn,yn) + hxy*fy(xn,yn) + lm*fx(xn,yn))
        yn1 = yn - (hyx*fx(xn,yn) + hyy*fy(xn,yn) + lm*fy(xn,yn))
        
        if(f(xn1,yn1) > f(xn,yn) ):
            lm = lm / 2
        else:
            lm = lm * 2
        print(xn1,yn1,f(xn1,yn1),lm)
        
    return xn1,yn1

#Não é necessário escrever a função, mas está aqui escrita
#para que consiga saber qual é o enunciado quando estiver a estudar
#E também para saber o valor dafunção para o resultado final
f = lambda xn,yn : yn**2-2*xn*yn-6*yn+2*xn**2+12

fx = lambda xn,yn : 4*xn-2*yn   #Derivada de f em ordem a x
fy = lambda xn,yn : 2*yn-2*xn-6 #Derivada de f em ordem a y

#Valores da inversa da Hessiana
hxx = 1/2 #Inversa da Hessiana[0][0]
hxy = 1/2 #Inversa da Hessiana[0][1]
hyx = 1/2 #Inversa da Hessiana[1][0]
hyy = 1   #Inversa da Hessiana[1][1]
#Os restantes cmoponentes da Inversa da Hessiana foram omitidos,
#porque tendo em conta a função dada, são nulos, portanto, desnecessários
    
x0 = 1  #Valor inicial de x
y0 = 1  #Valor inicial de y
lm = 1  #Valor inicial de lambda


result = LevenbergMarquardt(f,fx,fy,hxx,hxy,hyx,hyy,y0,lm)
print(result)
print(f(result[0],result[1]))