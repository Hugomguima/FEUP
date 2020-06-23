# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:06:20 2019

@author: Hugo
"""

#Pergunta 2 MT2 2016

#Método de Simpson

h = 0.2

Ss = h/3*(0.18+4*0.91+2*0.83+4*1.23+2*0.88+4*1.37+2*0.8+4*1.34+0.43)
Ss1 = h*2/3*(0.18+4*0.83+2*0.88+4*0.8+0.43)
SS2 = h*4/3*(0.18+4*0.88+0.43)

#Resultado do Método
print(Ss)


#Erro estimado

E = (Ss-Ss1)/15

print(E)



