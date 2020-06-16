# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 17:38:04 2018

@author: utilizador
"""

def scalar_mult(scalar, vector):
    
    new_vector= []
    
    for i in range(len(vector)):
        total = vector[i] * scalar
        new_vector.append(total)
    
    return new_vector

print(scalar_mult(7, [3, 0, 5, 11, 2]))