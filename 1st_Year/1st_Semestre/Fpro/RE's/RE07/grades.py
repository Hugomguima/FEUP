# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 11:20:17 2018

@author: Rita Silva
"""

def sort_grades(records):
    
    from statistics import mean as media
    total_result = tuple(sorted(sorted(sorted(records, key = lambda x : x[1]), key = lambda y : y[0]), key = lambda z : media(z[2]), reverse = True))
    
    return total_result

