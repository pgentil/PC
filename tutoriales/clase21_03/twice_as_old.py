# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:19:00 2022

@author: Pedro
"""

def twice_as_old(father_age: int, son_age: int) -> int:
    """Se calcula hace cuantos años el padre tuvo el doble de la del hijo actualmente o cuanto le falta para tener el doble
    
    Argumentos:
    father_age -- la edad actual del padre
    son_age -- la edad actual del hijo
    """
    a = abs(father_age - son_age * 2)
    return a

#%% AREA PERIMETER

def area_or_perimeter(length: float, width: float):
    if length == width:
        return length ** 2
    else:
        return length * 2 + width * 2
    
    
#%% DOT CALCULATOR

def dot_calc (text):
    counter_first = 0
    counter_second = 0
    op = None
    
    for character in text:
        print (character)
        if character == "." and op is None:
            counter_first += 1
        if character != "." and character != " ":
            op = character
        if character == "." and op is not None:
            counter_second += 1
    if op == "+":
        return (counter_first + counter_second) * "."
    if op == "-":
        return (counter_first - counter_second) * "."
    if op == "*":
        return (counter_first * counter_second) * "."
    if op == "/":
        return (counter_first // counter_second) * "."
            
    
print (len(calc) )

## oooo...

def calc(text):
    a, b, c = text.split (" ")
    
    return len(a) + len(b) * '.'