# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 13:43:26 2020

@author: Hugo
"""
from math import cos as cos
from math import sqrt as sqrt
from math import sin as sin
#A função tem 3 zeros, ecnontrados no maxima

f = lambda x: -x+40*cos(sqrt(x))+3
df = lambda x:-(20*sin(sqrt(x)))/sqrt(x)-1

def newton(x):
    print(x,f(x))
    for i in range(2):
        x -= f(x)/df(x)
        print(x,f(x))

newton(1.7)