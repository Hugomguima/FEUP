# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:42:03 2018

@author: Hugo
"""

r1 = int(input('Introduce the interest rate: '))
n1 = int(input('Introduce the first payment frequency: '))
r2 = int(input('Introduce the second interest rate: '))
n2 = int(input('Introduce the second payment frequency: '))

A1 = float( 1000 * ((1 + r1 / (100 * n1)) ** (n1)))
A2 = float( 1000 * ((1 +r2 /  (100 * n2)) ** (n2)))

print(A1)
print(A2)
