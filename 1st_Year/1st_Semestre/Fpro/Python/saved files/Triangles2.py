# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:35:46 2018

@author: Hugo
"""

n1 = int(input("Introduce the first side of the triangle: "))
n2 = int(input("Introduce the second side of the triangle: "))
n3 = int(input("Introduce the third side of the triangle: "))

if n1 + n2 <= n3 or n1 + n3 <= n2 or n2 + n3 <= n1:
    print("Not a triangle!!")
elif n1 == n2 == n3:
    print("This triangle is equilateral")
elif (n1 == n2 and n1 != n3) or (n1 == n3 and n1 != n2) or (n2 == n3 and n2 != n1):
    print("This triangle is isosceles")    
elif n1 != n2 != n3:
    print("This triangle is scalene")