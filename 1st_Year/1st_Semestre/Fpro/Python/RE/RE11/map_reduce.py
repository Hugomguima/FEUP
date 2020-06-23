# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 11:53:19 2018

@author: Hugo
"""
from functools import reduce

def map_reduce(n1, n2):
    
    odd = [i for i in range(n1,n2+1) if i % 2 != 0]
    
    function = map(lambda x: x**2,odd)
    
    return reduce(lambda x,y :x*y if x*y < 50 else x + y, function)

#print(map_reduce(5, 100))