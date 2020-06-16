# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 17:40:39 2018

@author: utilizador
"""

def dot_product(vec1,vec2):
    
    total = 0
    
    for i in range(len(vec1)):
        total += vec1[i] * vec2[i]
        
    return total

print(dot_product([1, 2, 1], [1, 4, 3]))