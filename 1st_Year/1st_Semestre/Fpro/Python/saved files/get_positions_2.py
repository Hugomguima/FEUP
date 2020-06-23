# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 12:04:09 2018

@author: Hugo
"""

def get_positions(word_list,sentences):
      
    b = sentences.split()
    counter  = 0
    result = ""
    
    
    for i in b:
        counter = 0
        for j in word_list:
           
            if j == i:
                result += str(counter) + " "
            counter += 1
        if b[0] == b[1]:
            return result  
    return result
            
            
        