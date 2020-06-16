# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 00:15:43 2019

@author: utilizador
"""

def rec_exceptions(l):
    
    resul = []
    
    for cons in l:
        
        try:
            
           type(cons()) == type([])
        except Exception as r:
            
                resul.append(r)
                
        else:
            resul += rec_exceptions(cons())
            
    return resul