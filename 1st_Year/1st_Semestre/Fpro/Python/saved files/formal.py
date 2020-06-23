# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 13:50:42 2018

@author: Hugo
"""

def formal(name):
    
    name_list = name.split()
    length = len(name_list)
    last_name = name_list[-1]
    result = ""
    
    for i in range(length-1):
        
        result += name_list[i][0] + "."
    
    result = last_name + "," + result
    
    return result
    
print(formal("Aníbal António Cavaco Silva"))
    