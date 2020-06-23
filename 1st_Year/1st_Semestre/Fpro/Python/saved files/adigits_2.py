# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 11:01:27 2018

@author: Hugo
"""

def adigits(a,b,c):

    
    d = [str(a) , str(b) , str(c)]
    e = sorted(d)
    h = list(reversed(e))
    f = "".join(h)
    f = int(f)
    
    
    
    return f
print(adigits(1,2,3))
    