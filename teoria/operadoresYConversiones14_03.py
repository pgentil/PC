# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 14:49:45 2022

@author: Pedro
"""

# float()
# bool()
# int()
# str()

# bool(0) #False
# bool("") #False
# bool(0.0) #False
# bool(1) #True
# bool("X") #True
# bool(0.01) #True

# #%% conversion implicita
# if 0: #se convierte en un booleano
#     print ("a")
    
# if "hola": #se convierte en un booleano
#     print("a")

# #%% 
# def is_positive(number): #forma larga de hacerlo
#     """docstring"""
#     answer = False
#     if number > 0:
#         answer = True
#     return answer

# def is_positive2(number): #forma corta
#     """docstring"""
#     return number > 0

#%%Condicionales
    # <sentencias>
    # if <condicion1>:
    #     <sentencias1>
    # elif <condicion2>:
    #     <sentencias2>
    # else:
    #     <sentencias3>
        
#%% Logica binaria
#operaciones logicas
#se define A={F, T} - F es falso T es verdadero - con p, q que son elementos de A:
    #operaciones unarias: not
    #operaciones binarias: and y or
    # False and <expresion> --> va a ser falso
    # True or <expresion> --> va a ser verdadero

#%% Paradigmas
## programa (se pueden escribir codigos en forma de programa o funciones)
# valor_inicial = input("Valor de compra: ")
# valor_inicial = float(valor_inicial)
# valor_actual = float(input("Valor actual: "))
# volumen = float(input("Volumen: "))
# capital_objetivo = 50000

# def calcular_capital(volumen: float, valor_actual: float, captial_objetivo: float):
#     """Calcular volumen de transaccion
    
#     Argumentos
#     volumen -- ...
#     """
#     capital = volumen * valor_actual
#     if capital > capital_objetivo:
#         return -0.1 * volumen
#     if capital < capital_objetivo:
#         return 0.1 * volumen

##Paradigma: fail fast, return early
    ## Prueba errores al inicio
    ##Muchos puntos de salida
    ## Facil de leer
    ## Facil de depurar

def get_name(first_name, last_name, reverse=False):
    if not (last_name and first_name):
        return ""    
    if reverse:
        name = last_name + ", " + first_name
    else:
        name =  first_name + " " + last_name
    return name
##Paradigma: single entry, single exit
    # Un unico punto de entrada
    # Un unico punto de salida
    # Prueba errores encadenados
    # Genera mucha identacion
    # Facil determinar donde sale la funcion (al final y no otro lado)
    
def make_merengue(huevos, azucar, batidora, bowl):
    if huevos == 4:
        if azucar == 170:
            if electrodomestico_funciona(batidora):
                etc...