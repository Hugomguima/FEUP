# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 20:45:53 2020

@author: Hugo
"""


#Funções para o método de Gauss Seide
#a)
#Deve ser utilizada a equação I, porque o valor na diagonal é maior que os outros
#b)
#Deve ser utilizada a equação III, porque o pivot na posicação [1,1] é 1

f = lambda y,z: (1.2-61*y-41*z)/103   #Em ordem a x
g = lambda x,z: (-x-3*z)              #Em ordem a y
h = lambda x,y: (-13 - 2*x -10*y)/13  #Em ordem a z


