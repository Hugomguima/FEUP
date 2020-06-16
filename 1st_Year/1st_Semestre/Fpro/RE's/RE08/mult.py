# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 21:16:33 2018

@author: utilizador
"""

def mult(M,N):
    
    maximum_result = []
    if (len(M[0]) != len(N)) or len(M[0]) == 0:
        result = []
    else:
        for line in M:
            maximum_result.append([])
            
        for i, line in enumerate(M):
            for j in range(len(N[0])):
                sum = 0
                
                for k in range(len(N)):
                    sum += line[k] * N[k][j]
                maximum_result[i].append(sum)
        result = maximum_result
    
    return result
        