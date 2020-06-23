# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:44:20 2018

@author: Hugo
"""

n1 = int(input("Input the first number: "))
n2 = int(input("Input the second number: "))

n3 = n2 
counter = 0

while n3 > 0:
    n3 = n3 // 10
    counter += 1

print(counter)

result = n1 * 10 ** counter + n2

print(result)
