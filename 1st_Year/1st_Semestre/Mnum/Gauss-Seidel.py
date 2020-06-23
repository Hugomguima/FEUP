# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 14:59:09 2019

@author: Hugo
"""

#Metodo de Gauss-Seidel

#Equacoes do sistema
g1 = lambda x1,x2,x3 : 3*x1 + x2 + x3 - 7
g2 = lambda x1,x2,x3 : x1 + 4*x2 +2*x3 - 4
g3 = lambda x2,x3 : 2*x2 +5*x3 - 5

#Equações por Recorrencia
f1 = lambda x2,x3 : (7-x2- x3) / 3
f2 = lambda x1,x3 : (4-x1- 2*x3) / 4
f3 = lambda x2 : (5-2*x2) / 5

#anteriores
x1n = 0
x2n = 0
x3n = 0

#novos
x1 = f1(x2n,x3n)
x2 = f2(x1n,x3n)
x3 = f3(x2n)

n = 1

while((abs(x1-x1n) > 10**-3) and (abs(x2-x2n) > 10**-3) and (abs(x3-x3n) > 10**-3)):
    #novos
    x1 = f1(x2,x3)
    x2 = f2(x1,x3)
    x3 = f3(x2)
    #Residuos
    print("R1 =",g1(x1,x2,x3),"R2=",g2(x1,x2,x3),"R3=",g3(x2,x3))
    #iteracoes
    n +=1
    

print(n)
print("x1 =",x1,"x2=",x2,"x3=",x3)