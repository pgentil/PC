# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 14:56:14 2022

@author: Pedro
"""

def geometric_sum (a, r, n):
    total = 0
    for k in range(0, n):
        total = total + a * r ** k 
    return total
print ("geometric sum(0.5, 0.5, 5) =", geometric_sum (0.5, 0.5, 5))

print ("""esta es un string de multiples lineas
m
m""") #tres comillas de cada lado representan tres lineas#

print ("n/", 7/8)

for i in range (0, 10): #en matematicas seria un conjunto de Z definido como C= [0, 10)#
    print (i) 