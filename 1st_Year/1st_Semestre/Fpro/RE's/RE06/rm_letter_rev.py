#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 11:41:52 2018

@author: up201806490
"""


def rm_letter_rev(l, astr):
    counter = len(astr)
    s = ""
    for a in range(counter):
        if astr[a] != l:
            s = astr[a] + s        
    return(s)
    

        
    