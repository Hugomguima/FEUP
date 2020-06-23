# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 13:11:23 2018

@author: Hugo
"""
number = int(input('Introduce a number: '))

if number == 0 :
    print('The square root of 0 is 0')
else:    
    g = number/2.0
    g2 = g + 1
    while(g != g2):
        n = number/ g
        g2 = g;
        g = (g + n)/2
    
    print(g)
