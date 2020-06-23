# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 13:36:33 2018

@author: Hugo
"""

def count(word, phrase):
    
    words = phrase.upper()
    words = words.split()
    result = 0
    
    
    for i in words:
        if i == word.upper():
            result += 1
    
    return result

print(count("shells","Sally sells sea shells by the sea shore. But if Sally sells sea shells by the sea shore then where are the sea shells Sally sells?"))