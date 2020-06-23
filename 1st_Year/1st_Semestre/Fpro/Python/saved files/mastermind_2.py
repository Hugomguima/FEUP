# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 11:48:27 2018

@author: Hugo
"""
def mastermind(g1,g2,g3,c1,c2,c3):
    points = 0  
    if  g1 == c1:
        points += 3
    if g2 == c2:
        points += 3    
    if  g3 == c3:
        points += 3

    if g1 != c1 and (g1 == c2 or g1 == c3):
        points += 1
    if g2 != c2 and (g2 == c1 or g2 == c3):
        points += 1
    if g3 != c3 and (g3 == c2 or g3 == c1):
        points += 1
    
    return points
        

