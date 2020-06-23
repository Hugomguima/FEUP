# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 15:05:01 2018

@author: Hugo
"""

number_initial = int(input("Input the palyndrome: "))

number = number_initial
inverse = 0

if number < 0:
    print("Input error!!")
    
else:
    while number / 10 > 0:
        digit = number % 10
        number = number // 10
        inverse = inverse * 10 + digit
    
    if number_initial == inverse:
        print(number_initial,"is a palyndrome!!")
    else:
        print(number_initial,"is not a palyndrome!!")
        
        

