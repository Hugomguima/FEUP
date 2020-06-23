# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:25:09 2019

@author: Hugo
"""

#Pergunta 3 MT2 2017

#Metodo de Simpson


h = 0.25
St = h/3*(1.04 + 4*0.37+ 2*0.38 + 4*1.49 + 2*1.08 + 4*0.13 + 2*0.64 +4*0.84 + 0.12)

h = 0.5
St1 = h/3*(1.04 + 4*0.38 + 2*1.08 + 4*0.64 + 0.12)

E = (St - St1)/15

print(St)
print(E)