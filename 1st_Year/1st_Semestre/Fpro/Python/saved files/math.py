# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 19:58:40 2018
@author: jlopes
"""


def squareit(n):
    return n * n


def cubeit(n):
    return n*n*n


def main():
    anum = int(input("Please enter a number: "))
    print(squareit(anum))
    print(cubeit(anum))


if __name__ == "__main__":
    main()