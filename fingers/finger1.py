# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 14:59:19 2022

@author: Pedro Gentil
"""

def partido_tenis(horas, minutos, segundos):
    """Devuelve la cantidad de segundos de un partido de tenis
   
    Argumentos:
    
    horas -- la cantidad de horas transcurridas mostrada en numeros enteros (descartar la cantidad de minutos y segundos que no puedan representarse como horas enteras).
    
    minutos -- La cantidad de minutos que transcurrieron restando la cantidad de horas representadas en numeros enteros, descartar la cantidad de segundos que no puedan ser representados como minutos enteros.
    
    segundos -- la cantidad de segundos transcurridos restando la cantidad de horas y minutos representados en numeros enteros
    
    """
    minutos = minutos * 60
    horas = horas * (60**2)
    return horas + minutos + segundos
