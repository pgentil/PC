# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 17:00:01 2022

@author: Pedro
"""
#%%Ej 8

# =============================================================================
# def interes_simple(Cn: float, k: int, i:int) -> float:
#     Cnk = Cn + Cn * (k * (i/100))
#     return Cnk
# 
# Cn = float(input("Ingrese el capital incial: "))
# k = float(input("Ingrese el periodo de tiempo que transcurrirá: "))
# i = float(input("Ingrese el procentaje de la tasa de interes: "))
# Cnk = interes_simple(Cn, k, i)
# print(f"El capital final del interes simple es: {Cnk}$")
# =============================================================================


#%%Ej 9 


def interes_compuesto(Cn: float, k: int, i:int) -> float:
    Cnk = Cn * (1 + (i/100))**k
    return Cnk

Cn = float(input("Ingrese el capital incial: "))
k = float(input("Ingrese el periodo de tiempo que transcurrirá: "))
i = float(input("Ingrese el procentaje de la tasa de interes: "))
Cnk = interes_compuesto(Cn, k, i)
print(f"El capital final del interes compuesto es: {Cnk}$")



#%% Ej 13

# =============================================================================
# def ten_mult(number: int) -> int:
#     """Function that returns the closest multiple of ten equal or inferior to
#     the number entered as arguement
#     Arguments:
#     number -- number in which the function will start searching for the closest
#     multiple of ten, which cannot be bigger than the number. 
#     """
#     resto = number % 10
#     return number - resto
# 
# 
# =============================================================================
#%% Ej 14
# =============================================================================
# def reversedSec(seconds: int) -> str:
#     """Functions that returns time measured in hours, minutes and seconds when entering
#     only the same time lapse in seconds
#     Arguments:
#     seconds -- Seconds that will be passed into hours, munites and seconds, in the form of an integer"""
#     hours = int(seconds/3600)
#     minutes = int((seconds%3600)/60)
#     seconds = (seconds%3600)%60
#     
#     return hours, minutes, seconds
# 
# =============================================================================
