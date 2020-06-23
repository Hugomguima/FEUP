# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 08:59:21 2018

@author: Hugo
"""

n = int(input("Input an integer number: "))

string = ""

if n <= 0 :
        print("Input error")

for i in range(1, n + 1):
    if i % 5 == 0 and i % 3 == 0:
        string += ""
    elif i % 3 == 0 and i % 5 != 0:
        string += "Fizz "
    elif i % 5 == 0 and i % 3 != 0:
        string += "Buzz "
    else:
        string += str(i) + " "
        
print(string)

        