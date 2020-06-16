# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:49:35 2019

@author: Hugo
"""

def exception_str(f):
    
    try:
        f()
    except Exception as ex:
        return str(ex)
    else:    
        return "No exception was raised"
    
print(exception_str(lambda: 1/0))