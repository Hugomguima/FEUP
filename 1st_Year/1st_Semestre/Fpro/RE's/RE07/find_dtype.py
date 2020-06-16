#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 12:12:47 2018

@author: up201806490
"""

def find_dtype(atuple, data_type):
    length = len(atuple)
    result = ()
    
        
    for i in range(length):
        typ = type(atuple[i]).__name__
        if typ == data_type:
            result += (atuple[i], )
    
    
    return result