# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 11:45:59 2018

@author: Hugo
"""

def sort_by_f(l):
    
    return sorted(l,key = lambda x: x if x < 5 else 5-x)

#print(sort_by_f([-1, -2, 2, 15, 99]))