# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 21:28:02 2018

@author: utilizador
"""

def local_minima(alist,n):
    
    total = []
    
    if n % 2 == 0:
        window_low = n / 2
        window_high = window_low - 1
        
    else:
        window_low = n // 2
        window_high = n // 2
        
    count = 0
    
    for ch in alist:
        
        low = count - window_low
        up = count + window_high + 1
        
        if low < 0:
            low = 0
            
        if up > (len(alist) - 1):
            up = len(alist)
            
        
        minimum_local = min(alist[low:up])
        
        counter = 0
        
        for i in alist[low:up]:
            if i == minimum_local:
                counter += 1
                
        if counter > 1:
            index = alist.index(minimum_local)
            
        else:
            index = count
            
        if ch == minimum_local and (minimum_local, index) not in total:
            total.append((minimum_local,count))
        
        count += 1
        
    return total
        