# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 12:49:31 2019

@author: Hugo
"""

def raise_exception(alist, value):
    result = []
    
    for i in alist:
        if i <= value:
            my_error = ValueError("{0} is not greater than {1}".format(i,value))
            result.append(my_error)
            
    return result
    
print(raise_exception([1, -2, 3, 0], 3))
print(raise_exception([3], 2))

