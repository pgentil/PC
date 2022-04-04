# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:46:46 2022

@author: Pedro
"""
import v2


def main2():
    """Funcion principal del programa, que ejecuta un partido de tenis simulado.
    El usuario debe elegir los nombres, el modo de juego (manual o automatico)
    y en caso de elegir el modo automatico si quiere imprimir las jugadas del
    game o solo el resultado. Establece los argumentos para la funcion score
    en el archivo v2.py."""
    print ("TeniSim")
    while True:
        while True:
            mode = input("Elija en que modo quiere jugar: \n- Ingrese '1' si quiere jugar el modo manual\n- Ingrese '2' si quiere jugar el modo simulado\n> ")     
            if mode in ('1','2'):
                break
            else:
                print("No ha seleccionado ningun modo de juego. Vuelva a intentar: ")
        name1 = input("Nombre del jugador 1: ")
        name2 = input("Nombre del jugador 2: ")
        puntosp1 = 0
        puntosp2 = 0
        puntajes = (0, 15, 30, 40, "Adv.", "Win")
        if mode == '1':
            print ("Ha elegido el modo manual")
            print("El game empieza 0-0")
            print(f"\nInstrucciones: Presione 1 si quiere que {name1} marque o presione 2 si quiere que {name2} marque.")
            auto_ch = "1"
            v2.score(mode, puntosp1, puntosp2, name1, name2, puntajes, auto_ch)
            break
        elif mode == '2':
            print ("Ha elegido el modo automatico")
            while True:
                auto_ch = input("Ingrese '1' si quiere que se muestren los resultados de cada jugada e ingrese '2' si quiere que se muestre el resultado final directamente: ")
                if  auto_ch in ('1','2'):
                    break
                else: 
                    print ("No ha seleccionado nada. Vuelve a intentarlo")
            while True:
                v2.score(mode, puntosp1, puntosp2, name1, name2, puntajes, auto_ch)
                break
            break

if __name__ == "__main__":
    main2()