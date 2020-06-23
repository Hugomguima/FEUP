# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 11:50:35 2018

@author: Hugo
"""

def sparse_dot_product(dict1,dict2):
    
    inner = 0
    
    for key in dict1:
        if key in dict2:
            inner += dict1[key] * dict2[key]
    
    return inner

#print(sparse_dot_product({0: 1, 1: 1},{2: 1, 3: 1}))