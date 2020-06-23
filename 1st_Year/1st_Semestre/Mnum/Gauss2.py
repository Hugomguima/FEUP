# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 17:09:40 2019

@author: Hugo
"""

#Metodo de Gauss


def solve(A,B):
    
    rows,cols = len(A),len(A[0])
    
    for i in range(rows):
        pivot = A[i][i]
        
        for j in range (cols):
            A[i][j] /= pivot
            
        B[i] /= pivot
        
        for i2 in range(i+1,rows):
            
            coef = A[i2][i]
            
            for j in range (cols):
                A[i2][j] -= coef * A[i][j]
            
            B[i2] -= coef * B[i]
    
    sols = []
    
    for i in range(rows-1,-1,-1):
        
        sol = B[i]
        for j in range(cols-1,i,-1):
            sol -= A[i][j] * sols[cols-1-j]
        
        sols.append(sol)
    sols.reverse()
    
    return sols
        
        
        
            