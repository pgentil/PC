# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:35:56 2022

@author: Pedro
"""

def score(score_sum: str, puntosp1: int, puntosp2: int, name1: str, name2: str, puntajes: tuple):
    if score_sum == '1':
        puntosp1 += 1  
        if puntosp1 == 4 and puntosp2 < 3:
            print (f"\n{name1} ha ganado el game")
        if puntosp1 == 5 and puntosp2 == 3:
            print(f"\n{name1} ha ganado el game")
        if puntosp1 == 4 and puntosp2 == 4:
            puntosp1 -= 1
            puntosp2 -= 1
            print (f"\nEl game ahora va:\n{name1}: {puntajes[puntosp1]} - {name2}: {puntajes[puntosp2]}")
            else:
                print (f"\nEl game ahora va:\n{name1}: {puntajes[puntosp1]} - {name2}: {puntajes[puntosp2]}")
        elif score_sum == '2':
            puntosp2 += 1
        print (f"\n{name1} ha marcado un punto")
    if score_sum == '2':
        
    