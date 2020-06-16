# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 17:48:29 2018

@author: utilizador
"""

def cross_product(vec_1,vec_2):
    
    
    i = vec_1[1] * vec_2[2] - vec_2[1] * vec_1[2]
    
    j = vec_1[0] * vec_2[2] - vec_2[0] * vec_1[2]
    
    j = -j
    
    k = vec_1[0] * vec_2[1] - vec_2[0] * vec_1[1]
    
    
    vec_3 = [i,j,k]
    
    return vec_3

print(cross_product([1,2,0],[-1,1,2]))
    
    