# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:35:27 2019

@author: Hugo
"""

#Pergunta 4 MT2 2016

f = lambda T : -0.25*(T-42)

h = 0.4
T = 10
t = 5


for i in range(3):
    
    print(t,T)
    t+= h
    T+= h*f(T)
    
    