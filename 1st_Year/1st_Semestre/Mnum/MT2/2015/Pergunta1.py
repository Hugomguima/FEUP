# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 19:26:33 2019

@author: Hugo
"""

#Pergunta 1 MT2 2015


h = 0.25

Ss = h/3*(0.36+ 4*1.19+ 2*1.32+ 4*0.21+ 2*1.15+ 4*1.39+ 2*0.12+ 4*1.22+ 0.6)
Ss1 = h*2/3*(0.36+ 4*1.32+ 2*1.15+ 4*0.12+ 0.6)

E = (Ss-Ss1)/15

print(Ss)
print(E)