# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 13:31:14 2018

@author: Hugo
"""
def rm_letter_rev(l,astr):
    
    result = ""
    
    for i in astr:
        if i != l:
            result += i
    
    result = result[::-1]
            
    
    return result
            
