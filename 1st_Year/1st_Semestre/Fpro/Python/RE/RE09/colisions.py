# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 11:47:17 2018

@author: Hugo
"""

def colisions(alist):
    
    di = {}
    
    for number in alist:
        total = 0
        new_number = number
        
        while new_number != 0 :
            
            last_digit = new_number % 10
            new_number = new_number // 10
            total += last_digit
            
        value = total % 8
        print(value)
        if value in di:
            di[value] += 1
        else:
            di[value] = 1
   
    return di


print(colisions([1,789,100,9807,1208,92,101]))
            