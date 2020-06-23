# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 13:05:05 2018

@author: Hugo
"""

print('This program is used to calculate the sum of the divisiors of a certain number')
n = int(input('Introduce that number: '))

divisors = 0

for i in range(1,n + 1):
    if n % i == 0:
        divisors += i
print(divisors)