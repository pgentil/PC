# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:07:32 2022

@author: Pedro
"""
import random
lista1 = list(range(1, 41))


def falta_una (lista1):
    carta_X = random.choice(range(1, 41))
    lista1.remove(carta_X)
    return lista1
    
 
def busqueda(lista1):
    print (len (lista1))
    falta_una(lista1)
    print(len (lista1))
    while True:
        if lista1[19] != 10:
            
    
    
if __name__ == "__main__":
    busqueda(lista1)