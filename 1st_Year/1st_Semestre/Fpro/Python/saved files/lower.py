# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 15:32:15 2018

@author: Hugo
"""

n1 = int(input("Input the lower value: "))
n2 = int(input("Input the upper value: "))

string = ""

for i in range(n1, n2 + 1):
    divisors = 0
    for a in range(1, i + 1):
        if i % a == 0:
            divisors += 1
    if divisors == 2:
        string += str(i) + " "

print("Prime numbers between",n1,"and",n2,"are:",string)
        
        
        