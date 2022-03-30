# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 17:34:10 2022

@author: Pedro
"""

def compress(strand: str):
    new_strand = []
    for i in strand:
        indexi = strand.index(i)
        valor_ant = indexi - 1
        valor_post = indexi + 1
        elem_ant = strand[valor_ant]
        elem_post = strand[valor_post]
        if indexi >= 0:
            if i != elem_ant or i == strand[0]:
                num_case = 1
            if i == elem_ant and i != strand[0]:
                num_case += 1
            if i != elem_post or strand.index(i) == -1:
                element = str(num_case) + i
                new_strand.append(element)
            if indexi == -1:
                return new_strand
            
if __name__ == "__main__":
    print(compress('AIIIHHHOOJJJDDD'))