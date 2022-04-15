# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 16:55:11 2022

@author: Pedro
"""

import numpy as np
def db(p):
 '''
 Recibe un valor de potencia p [watts] y lo devuelve en decibeles [dB]
 precondiciones: p>0.
 '''
 try:
     assert p > 0, "Entrada invalida, no puede elegir un valor igual o menor a 0"
     pdb = 10 * np.log10(p)
 except AssertionError as msg:
     print(msg)
 else:
     return pdb
 finally:
     print("Programa terminado")
     
def db2(p):
    '''
    Recibe un valor de potencia p [watts] y lo devuelve en decibeles [dB]
    precondiciones: p>0.
    '''
    try:
        pdb = 10 * np.log10(p)
    except RuntimeWarning:
        print("El valor que elige debe ser mayor a 0")
    else:
        return pdb


if __name__ == "__main__":
# casos de prueba
    a = db(1)
    b = db2(0)
    c = db2(-3)
    d = db(0.5)
    e = db(36954)
