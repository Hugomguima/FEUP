# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 17:55:41 2018

@author: utilizador
"""

def replace(s, old, new):
    
    b = list(s)
    
    for i in range(len(b)):
        
        if old in b:
            index = b.index(old)
            b[index] = new
    
    b = "".join(b)
    
    return b

print(replace("I love spom! Spom is my favorite food. Spom, spom, yum!", "o", "a"))