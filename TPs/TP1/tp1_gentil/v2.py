# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:35:56 2022

@author: Pedro
"""

def score(mode: str, puntosp1: int, puntosp2: int, name1: str, name2: str, puntajes: tuple, auto_ch: str)->str:
    """Funcion que simula un game de Tenis, ya sea de forma manual, es decir
    con intervencion del usuario en los puntos, o de forma automatica, dejando 
    a eleccion del usuario si mostrar o no los puntajes en todas las jugadas
    
    Argumentos:
    mode -- Variable que decide que modo de juego se ejecutara. Tomara el valor 
    '1' para ejecutar el modo de juego manual y el '2' para ejecutar el 
    automatico.
    
    puntosp1 -- Variable que guarda el puntaje del primer jugador
    
    puntosp2 -- Variable que guarda el puntaje del segundo jugador
    
    name1 -- Variable que guarda el nombre del primer jugador
    
    name2 -- Variable que guarda el nombre del segundo jugador
    
    puntajes -- Variable de tipo tupla que guarda los puntajes reglamentarios
    del tenis, usados para llamarlos usando a puntosp1 y puntosp2 como numeros
    de indice
    
    auto_ch -- Variable que decide si se imprimen las jugadas del game o solo
    el resultado en caso de que se ejecute el modo automatico. 
    """
    import random
    import time
    while True:
        if mode == '1':
            score_sum = input("¿Quién marca? ")
        if mode == '2':
            score_sum = random.choice('1' '2')
        if score_sum == "1":
            puntosp1 += 1 
            if auto_ch == "1":
                print (f"\n{name1} ha marcado un punto")
            if puntosp1 == 4 and puntosp2 < 3:
                print (f"\n{name1} ha ganado el game")
                break
            if puntosp1 == 5 and puntosp2 == 3:
                print(f"\n{name1} ha ganado el game")
                break
            if puntosp1 == 4 and puntosp2 == 4 and auto_ch == "1":
                puntosp1 -= 1
                puntosp2 -= 1
                print (f"\nEl game ahora va:\n{name1}: {puntajes[puntosp1]} - {name2}: {puntajes[puntosp2]}")
                if mode == "2" and auto_ch == "1":
                    time.sleep(2)
            elif auto_ch == "1":
                print (f"\nEl game ahora va:\n{name1}: {puntajes[puntosp1]} - {name2}: {puntajes[puntosp2]}")
                if mode == "2" and auto_ch == "1":
                    time.sleep(2)
        elif score_sum == "2":
            puntosp2 += 1
            if auto_ch == "1":
                print (f"\n{name2} ha marcado un punto")
            if puntosp2 == 4 and puntosp1 < 3:
                print (f"\n{name2} ha ganado el game")
                break
            if puntosp2 == 5 and puntosp1 == 3:
                print(f"\n{name2} ha ganado el game")
                break
            if puntosp1 == 4 and puntosp2 == 4 and auto_ch == "1":
                puntosp1 -= 1
                puntosp2 -= 1
                print (f"\nEl game ahora va:\n{name1}: {puntajes[puntosp1]} - {name2}: {puntajes[puntosp2]}")
                if mode == "2" and auto_ch == "1":
                    time.sleep(2)
            elif auto_ch == "1":
                print (f"\nEl game ahora va:\n{name1}: {puntajes[puntosp1]} - {name2}: {puntajes[puntosp2]}")
                if mode == "2" and auto_ch == "1":
                    time.sleep(2)
    return "Partido Terminado"

