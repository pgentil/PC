# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 13:11:03 2022

@author: Pedro
"""
def removal(array1, array2):
    for i in array2:
        if i in array1:
            for j in array1:
                if i == j:
                    array1.remove(j)
        else:
            continue
   
    return array1

if __name__ == "__main__":
    removal([1, 2, 3, 4, 5, 2, 3, 4, 7, 6 ,7 ,2, 4, 9, 99, 3, 2 ,4], [2, 4, 3])