# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 21:22:37 2018

@author: utilizador
"""

def manipulator(l, cmds):
    
    total = ""
    
    for i in cmds:
        i = i.split()
        
        if i [0] == "insert":
            l.insert(int(i[1]), int(i[2]))
            
        elif i[0] == "append":
            l.append(int(i[1]))
        
        elif i[0] == "print":
            total += str(l) + " "
        
        elif i[0] == "remove":
            l.remove(int(i[1]))
        
        elif i[0] == "pop":
            l.pop()
            
        elif i[0] == "sort":
            l.sort()
        
        elif i[0] == "reverse":
            l.reverse()
    
    return total