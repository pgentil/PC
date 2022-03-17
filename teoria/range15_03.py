# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 10:55:32 2022

@author: Pedro
"""

import time

#%% RANGE

range(8)
# range(start: int, stop: int, step: int): #-> <secuencia>#
    #comienza en start
    #avanza de a step
    #para antes de stop
    
range (10)#= range (0, 10) = range (0, 10, 1) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    # range(10, 0, -1) #10, 9, 8, 7, 6, 5, 4, 3, 2, 1
    
for i in range (10):
    print (i, end="->\n")
    
nombre = "Pedro"
print("hola", nombre, "!", sep="-")

n_maximo = int(input("n maximo?"))

suma = 0

for n in range (n_maximo):
    suma += n
    time.sleep(0)
print("La suma de 0 a", n_maximo, "es", suma, sep=" ")

def factorial(n: int) -> int:
    """Computes n!"""
    result = 1
    for i in range (1, n + 1):
        result *= i
    return result


n = int(input("n?"))
print ("El factorial es", factorial(n))


#%% WHILE LOOP (CICLO INDEFINIDO)

## Un centinela es una condicion de corte:

#variable = valor
# while variable != centinela:
    #hacer_cosas()

def heron(x, guess):
    if not guess:
        return -1.0
    while abs(guess ** 2 - x) >1e-7: # depende del numero en el 1e-n la precision va ser mejor o peor
        print ("guess: ", guess)
        guess = (guess + x / guess) / 2
    return guess
        
def heron2(x: float, guess: float, tol: float = 1e-4):
    if not guess: # es lo mismo que decir if guess == 0
        return -1.0
    while abs(guess ** 2 - x) > tol: # depende del numero en el 1e-n la precision va ser mejor o peor
        print ("guess: ", guess)
        guess = (guess + x / guess) / 2
    return guess

def es_nota_valida(nota:float, minimo:float = 0.0, maximo:float = 10.0):
	return minimo <= nota <= maximo


prompt = "Ingresar una nota valida para continuar:"
suma = 0.0
cantidad = 0
nota = float(input(prompt)) #leer valor
while es_nota_valida(nota): #leer valor
    suma += nota #hacer algo
    cantidad += 1#hacer algo
    nota = float(input(prompt))#leer valor
print("El promedio es: ", suma / cantidad)



