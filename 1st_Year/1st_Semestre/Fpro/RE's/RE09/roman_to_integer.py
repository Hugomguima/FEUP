# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 12:22:30 2018

@author: Hugo
"""

def roman_to_integer(astring):
    
    dict_1 = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    total = 0
    
    for index in range(len(astring)):
        
        if index == len(astring) - 1:
            total += dict_1[astring[index]]
        
        elif dict_1[astring[index]] >= dict_1[astring[index + 1]]:
            total += dict_1[astring[index]]
        else:
            total -= dict_1[astring[index]]
    
    return total
        
        
        
        
#print(roman_to_integer('MMMCMXCIX'))
        
        
        