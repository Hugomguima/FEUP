# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 12:55:01 2018

@author: You're mom gay
"""

import datetime

now = datetime.datetime.now()

print()
print("Current date and time using str method of datetime object:")
print()
print(str(now))

print()
print("Current date and time using instance attributes:")
print()
print("Current year: %d" % now.year)
print("Current month: %d" % now.month)
print("Current day: %d" % now.day)
print("Current hour: %d" % now.hour)
print("Current minute: %d" % now.minute)
print("Current second: %d" % now.second)
print("Current microsecond: %d" % now.microsecond)

print()
print("Current date and time using strftime:")
print(now.strftime("%Y-%m-%d %H:%M"))