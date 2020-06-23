# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 14:12:43 2018

@author: Hugo
"""

def uppercase(astring):
    counter = 0
    
    for i in range(3):
        if astring[i].isupper():
            counter += 1
            print (counter)
            
    if counter != 0:
        result = astring.upper()
        return result
    
    return astring

print(uppercase("...tonic..."))
            