#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:28:11 2018

@author: up201806490
"""

def file_finder(dirs,file_name):
    if dirs == file_name:
        return file_name
    for sub in dirs[1:]:
        total = file_finder(sub,file_name)
        if total != None:
            return dirs[0] + "/" + total
    