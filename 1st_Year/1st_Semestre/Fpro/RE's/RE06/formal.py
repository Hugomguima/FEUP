#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 12:52:04 2018

@author: up201806490
"""

def formal(name):
    split = name.split()
    names = len(split)
    result = ""
    split_2 = split[:names-1]
    
    for i in split_2 :
        result += i[0] + ". "
        
    last_name = split[names-1]
    
    result = last_name + ", " + result
     
    return(result)
        