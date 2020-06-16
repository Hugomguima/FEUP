#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:42:37 2018

@author: up201806490
"""

def unique(atuple):
    order = sorted(atuple)
    result = (order[0], )
    length = len(atuple)
    
    for i in range(1,length):
        if order[i] != order[i-1]:
            result += (order[i], )
        
        
    return result