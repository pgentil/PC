# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 14:33:16 2022

@author: Pedro
"""

def contar_letras (cadena: str, letras: str):
    """Cuenta la cantidad de letras especificas en la cadena
    
    Argumentos:
        cadena (str) -- cadena sobre la que contar
        letra (str) -- letra que quiero contar
    """
    cuenta = 0
    for caracter in cadena:
        if caracter == letras:
            cuenta += 1
            
    return cuenta 


def contar_elementos(lista: list, elemento) -> int:
    """Cuenta la cantidad de letras especificas en un elemento
    
    Argumentos:
        lista (list) -- ...
        elemento -- ...
    """
    cuenta = 0
    for e in lista:
        if e == elemento:
            cuenta += 1
            
    return cuenta

n = 'Patricio'

print(n[0]) #'p'
print(n[1]) #'a'
print(n[2]) #'t'
print(n[3]) #'r'
print(n[4]) #'i'
print(n[-1]) #'o'
print(n[-2]) #'i'
print(n[-8]) #'p'
print(n[-7]) #'a'

#en un tuple no puedo modificar nada pero en la lista si:

m = ['hola', False, 1]

m[0] = 'chau'
m[1] = True
m[2] = 2

print (m)
s = 'hola'
print (s)
print (id(s))
s += " python"
print (s)
print (id(s))

def sq_list(lista: list) -> list:
    lista2 = lista
    for i in range(len(lista2)):
        lista2[i] = lista[i] ** 2
    return lista2


def generar_lista(n: int) -> list:
    return list(range(n))

def probar_desempaquetado():
    meses = (("enero", 31), ("febrero", 28), ("diciembre", 31))
    for mes, dias in meses:
        print (mes, "tiene", dias, "dias.")
        

def probar_desempaquetado2():
    db = (("Cuantos estudiantes hay en PC-IA?", (50, 100, 150, 200)),
             ("Cuantos estudiantes hay en el aula", (15, 30, 45, 60)))
    for pregunta, opciones in db:
        print (pregunta)
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")
        rta = input("> ")