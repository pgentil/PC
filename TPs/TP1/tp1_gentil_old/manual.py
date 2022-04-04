# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 13:00:49 2022

@author: Pedro
"""

def manual(name1: str,
           name2: str,
           puntosp1: int,
           puntosp2: int,
           puntajes: tuple):
    """Funcion que ejecuta el modo manual del TeniSim
    Argumentos:
    name1 -- nombre del jugador 1
    name2 -- nombre del jugador 2
    puntosp1 -- puntos del jugador 1
    puntosp2 -- puntos del jugador 2
    puntajes -- tupla que indica los puntajes reglamentarios del tennis"""
    print ("Ha elegido el modo manual")
    print("El game empieza 0-0")
    print(f"""Presione 1 si quiere que {name1} marque o presione 2 si quiere que {name2} marque: """)
    u = input ()
    while True:
        int(u)
        if u == '1':
            puntosp1 += 1
            print (f"{name1} ha marcado un punto")
            if puntosp1 == 4 and puntosp2 < 3:
                print (f"{name1} ha ganado el game")
                break
            if puntosp1 == 5 and puntosp2 == 3:
                print(f"{name1} ha ganado el game")
                break
            if puntosp1 == 4 and puntosp2 == 4:
                puntosp1 -= 1
                puntosp2 -= 1
                print (f"""El game ahora va 
                {name1}: {puntajes[puntosp1]} - {name2}: {puntajes[puntosp2]}""")
                u = input ("¿Ahora quién marca? ")
            else:
                print (f"""El game ahora va 
                {name1}: {puntajes[puntosp1]} - {name2}: {puntajes[puntosp2]}""")
                u = input ("¿Ahora quién marca? ")
        elif u == '2':
            puntosp2 += 1
            print (f"{name2} ha marcado un punto")
            if puntosp2 == 4 and puntosp1 < 3:
                print (f"{name2} ha ganado el game")
                break
            if puntosp2 == 5 and puntosp1 == 3:
                print(f"{name2} ha ganado el game")
                break
            if puntosp1 == 4 and puntosp2 == 4:
                puntosp1 -= 1
                puntosp2 -= 1
                print (f"""El game ahora va 
                {name1}: {puntajes[puntosp1]} - {name2}: {puntajes[puntosp2]}""")
                u = input ("¿Ahora quién marca? ")
            else:
                print (f"""El game ahora va 
                {name1}: {puntajes[puntosp1]} - {name2}: {puntajes[puntosp2]}""")
                u = input ("¿Ahora quién marca? ")
        else: 
            u = input ("No ha seleccionado a ningun jugador para que marque. Porfavor intentelo de nuevo:")