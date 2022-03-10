# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 11:08:46 2022

@author: Pedro
"""

def greet(name):
    """Return a string to greet someone.
 	Arguments:
 	Name – name of the person to greet
	""" #es una buena practica usar el docstring#
    return "Hello, " + name + "."

print ("el archivo fue ejecutado")
msg = greet ("674")
print (greet ("63"))

#"Una computadora responde en 0,000000001 segundos (1 nanosegundo)"#

nombre = input("como te llamas? ")
msg = greet(nombre) #se sobreescribe la variable msg por orden de precedencia#

#Con CRTL + 1 se comentan todas las líneas seleccionadas#

x = 2
y = 3

#%% 

def multiply(x, y):
    """Multiply x and y"""
    y += 1
    print (x, y)
    z = x * y
    print (z)
    return z #Las variables que declaras adentro de las funciones no estan declaradas por fuera de las mismas#

print ("x =", x)
print ("y =", y)

multiply (2, 3)
print ("x =", x)
print ("y =", y)
#print ("z =", z)

def multiply(a, b):
    """Multiply x and y"""
    b += 1
    print (a, b)
    pepe = a * b
    print (pepe)
    return pepe #no pongas variables globales en el scope local (como y o x) a menos que entren en los parametros#

def multiply(t, p, n=6):
    """Multiply x and y"""
    p += 1
    print (t, p, n)
    pepe = t * p * n
    print (pepe)
    return pepe

print (multiply(2, 2))

#%% Type hints / Annotations

def geometric_sum(a, r, n=7):
    """Compute a geometric sum of n terms
    Arguments:
    a --- coefficient
    r --- ratio
    n --- terms to sum (default: 7)
    """
    total = 0
    for i in range (0, n):
        total = total + a *r ** i
    return total

