# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 12:12:17 2018

@author: Hugo
"""

def odd_range(start,stop,step):
    
    odd = [i for i in range(start,stop+1) if i % 2 != 0]
    return (odd[num] for num in range(0,len(odd),step))


    
    