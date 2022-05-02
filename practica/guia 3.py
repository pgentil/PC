# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 17:46:09 2022

@author: Pedro
"""

#%% Ej 8
# def number_control(number: int, lista: list):
#     while number not in lista:
#         if number < 0 :
#             number += len(lista)
#         elif number >= len(lista):
#             number -= len(lista)
#     return number
    

# def dia_de_semana(dia_start: str, dias_anuales: int, dias_semanales: list = ["lunes", "martes", 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo'], index_list: list = list(range(0, 7))) -> str:
#     dias_anuales += dias_semanales.index(dia_start)
#     dias_anuales -= 1
#     dia_end = number_control(dias_anuales, index_list)
#     return dias_semanales[dia_end]

#%%ej 9

# def abcisa(listaRecta1: list, listaRecta2: list) -> float:
#     """Funcion que devuelve el valor de la abcisa en el que intersecan dos rectas
#     Argumentos:
#     listaRecta1 -- Lista que contiene dos elementos, el primero la pendiente de la recta 1, y el segundo la ordenada al origen de la recta 1.
#     listaRecta2 -- Lista que contiene dos elementos, el primero la pendiente de la recta 2, y el segundo la ordenada al origen de la recta 2.
#     """
#     if listaRecta1[0] == listaRecta2[0]:
#         return None
#     elif listaRecta1[1] == listaRecta2[1]:
#         return 0
#     else:
#         x = (listaRecta2[1] - listaRecta1[1])/(listaRecta1[0]-listaRecta2[0])
#         return x


#     l1 = [2, 1]
#     l2 = [3, 1]
#     print(abcisa(l1, l2))
    
#%% EJ 10

def bisiesto(year: int) -> bool:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
        

if __name__ == "__main__":
    # print(bisiesto(2100))
    