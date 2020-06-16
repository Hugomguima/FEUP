#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 12:46:14 2018

@author: up201806490

for astring="Hello world!" and table=(('a', 1), ('e', 2), ('i', 3),
('o', 4), ('u', 5), ('!', ' :)')), the function returns the string "H2ll4
w4rld :)" (without quotes)
● for astring="Testing this string..." and table=((' ', '--'), ('.',
'!'), ('i', 'o'), ('t', 'tt')), the function returns the string
"Testtong--tthos--sttrong!!!" (without quotes)
"""


def translate(astring, table):
    
    result =''
    length_astring = len(astring)
    length_table = len(table)
    
    for i in range(length_astring):
        for a in range(length_table):
            if astring[i] == table[a][0]:
                result += str(table[a][1])
                break
        else:
            result += astring[i]
        
    
    return result
            
        
    