# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 19:17:07 2018

@author: utilizador
"""

def soup(matrix,word):
    for row in range(len(matrix)):
        for letter in range(len(matrix[row])):
            if matrix[row-1][letter-1] == word[0]:
                if checksoup(matrix,row-1,letter-1,word[1:]):
                    return "{0}{1}".format(chr(ord("A")+row-1),letter)


def checksoup(matrix,row,letter,word):
    if word == "":
        return True
    else:
        for s in range(row-1,row+2):
            for l in range(letter-1,letter+2):
                if s >= 0 and l >= 0 and s < len(matrix) and l < len(matrix) and word[0] == matrix[s][l]:
                    matrix[s][l] == ""
                    if checksoup(matrix,s,l,word[1:]):
                        return checksoup(matrix,s,l,word[1:])
                    else:
                        continue


print(soup((('X', 'A', 'B', 'N', 'T', 'O'),
('Y', 'T', 'N', 'R', 'I', 'T'),
('U', 'P', 'O', 'M', 'D', 'S'),
('I', 'O', 'H', 'U', 'O', 'O'),
('R', 'T', 'E', 'L', 'Q', 'X'),
('I', 'W', 'J', 'K', 'P', 'Z')), 'PORTO'))