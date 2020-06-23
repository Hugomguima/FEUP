# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:08:48 2018

@author: Hugo
"""

def inner(u,v):
    
    result = 0
    counter = 0
    
    for i in u:
        product = i * v[counter]
        result += product
        print(product)
        counter += 1
    
    return result
        
        
    