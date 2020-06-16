# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 21:37:18 2018

@author: utilizador
"""

def anagrams(alist):
    
    total = []
    m = 0
    
    for i in alist:
        total.append([])
        total[m].append(i)
        total_1 = []
        
        for j in alist:
            if i != j:
                f = list(i.lower().replace(" ",""))
                f.sort()
                g = list(j.lower().replace(" ",""))
                g.sort()
                
                if f == g:
                    total_1.append(i)
                    total_1.append(j)
                    alist.remove(j)
        
        for p in total_1:
            if p not in total[m]:
                total[m].append(p)
        total[m] = sorted(total[m])
        m += 1
    total = sorted(total, key = lambda x:x[0].lower())
    return total