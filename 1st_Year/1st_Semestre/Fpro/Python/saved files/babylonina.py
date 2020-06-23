# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 15:23:31 2018

@author: Hugo
"""

number_initial = float(input("Input a number: "))

approximation = number_initial / 2
root = (approximation + number_initial/approximation ) / 2

while int(root * 100) != int(approximation * 100):
    approximation = root
    root = (approximation + number_initial/approximation ) / 2

print("%.3f" % root)
print(round(root,3))
   