# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 12:48:08 2018

@author: Hugo
"""

def isomorphic(astring1,astring2):
    
    dict_1 = {}
    alist = []
    
    for i in range(len(astring1)):
        if astring1[i] in dict_1:
            if dict_1[astring1[i]] != astring2[i]:
                
                return "'{}' and '{}' are not isomorphic".format(astring1,astring2)
        
        else:
            dict_1.update({astring1[i]:astring2[i]})
    for a in dict_1:
        for b in dict_1:
            
            if dict_1[a] == dict_1[b] and a != b:
                
                return "'{}' and '{}' are not isomorphic".format(astring1,astring2)
    for j in dict_1:
        alist.append((j,dict_1[j])) 
    return "'{}' and '{}' are isomorphic because we can map: {}".format(astring1,astring2,alist)