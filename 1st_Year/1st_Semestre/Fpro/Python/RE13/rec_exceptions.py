# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 13:02:09 2019

@author: Hugo
"""

def rec_exceptions(l):
    
    result = []
    for function in l:
        try:
            function()
        
        except Exception:
            my_error = ZeroDivisionError("division by zero",)
            result.append(my_error)
    return result
    
print(rec_exceptions([lambda: 1/0]))
#rec_exceptions([lambda: 1/0])