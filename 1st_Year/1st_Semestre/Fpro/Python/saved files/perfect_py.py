# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 10:58:05 2018

@author: Hugo
"""

def is_perfect(n):
    
    total= 0
    
    for i in range(1,n):
        if n % i == 0:
            total += i
            
    if total == n:
        return True
    
    return False
    