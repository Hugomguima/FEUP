# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 21:16:07 2018

@author: utilizador
"""

def palindrome(astring):
    a = 2
    b = len(astring) - 1
    counting = 0
    
    while a <= len(astring):
        for b in range(0,len(astring) - a + 1):
            if astring [b:b + a] == astring[b:b + a][::-1]:
                counting = counting + 1
    
        a += 1
        result = "For string '{0}': {1} palindrome substrings".format(astring,counting)
    return result