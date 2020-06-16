# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 12:23:55 2019

@author: Hugo
"""

def compatible(A, B):
    
    col_A = len(A[0])
    rows_B = len(B)
    
    try:        
        assert col_A == rows_B , "A and B cannot be multiplied"
    
    except Exception as ex:
        
        return ex       
    else:
        return "A and B can be multiplied" 
    
#    if cols_A != rows_B:
#        return "A and B cannot be multiplied"
#    else:
#        return "A and B can be multiplied"
        
print(compatible([[2,2], [1,1]], [[5,5,5,5], [5,5,5,5]]))
print(compatible([[1,2,2], [1,2,2]], [[1,2,3,4], [1,2,3,4]]))

