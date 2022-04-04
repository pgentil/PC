# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 11:08:35 2022

@author: Pedro
"""
def simulado(name1: str,
             name2: str,
             puntosp1: int,
             puntosp2: int,
             puntajes: tuple):
    """Funcion que ejecuta el modo simulado del TeniSim
    Argumentos:
    name1 -- nombre del jugador 1
    name2 -- nombre del jugador 2
    puntosp1 -- puntos del jugador 1
    puntosp2 -- puntos del jugador s2
    puntajes -- tupla que indica los puntajes reglamentarios del tennis
    """
    import random
    import time
    print ("Ha elegido el modo simulado\n")
    
    choice = input("Ingrese '1' si quiere que se muestren los resultados directamente o \ningrese '2' si quiere que se muestren las jugadas tambien: ")
    while True:
        if choice == '1':
            u = random.random()
            if u > 0.5:
                print(f"{name1} ha ganado el game.")
                break
            else: 
                print(f"{name2} ha ganado el game.")
                break
        if choice == '2':
            print("El game empieza 0-0")
            while True:
                u = random.random() #valores que van del 0 al 1
                time.sleep(2)
                if u > 0.5:
                    puntosp1 += 1
                    print (f"{name1} ha marcado un punto\n")
                    if puntosp1 == 4 and puntosp2 < 3:
                        print (f"{name1} ha ganado el game")
                        break
                    if puntosp1 == 5 and puntosp2 == 3:
                        print(f"{name1} ha ganado el game")
                        break
                    if puntosp1 == 4 and puntosp2 == 4:
                        puntosp1 -= 1
                        puntosp2 -= 1
                        print (f"""El game ahora va:\n{name1}: {puntajes[puntosp1]} - {name2}: {puntajes[puntosp2]}\n""")
                    else:
                        print (f"""El game ahora va:\n{name1}: {puntajes[puntosp1]} - {name2}: {puntajes[puntosp2]}\n""")
                else:
                    puntosp2 += 1
                    print (f"{name2} ha marcado un punto\n")
                    if puntosp2 == 4 and puntosp1 < 3:
                        print (f"{name2} ha ganado el game")
                        break
                    if puntosp2 == 5 and puntosp1 == 3:
                        print(f"{name2} ha ganado el game")
                        break
                    if puntosp1 == 4 and puntosp2 == 4:
                        puntosp1 -= 1
                        puntosp2 -= 1
                        print (f"""El game ahora va:\n{name1}: {puntajes[puntosp1]} - {name2}: {puntajes[puntosp2]}\n""")
                    else:
                        print (f"""El game ahora va:\n{name1}: {puntajes[puntosp1]} - {name2}: {puntajes[puntosp2]}\n""")
            break
        else:
            choice = input("Porfavor intentelo de nuevo: ")  