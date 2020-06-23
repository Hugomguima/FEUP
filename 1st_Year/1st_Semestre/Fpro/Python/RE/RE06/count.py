#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 12:24:26 2018

@author: up201806490
"""

def count(word,phrase):
    words = phrase.split()
    counter = 0
    word = word.lower()
    phrase = phrase.lower()
    for i in words:
        if i == word:
            counter += 1
    return(counter)
