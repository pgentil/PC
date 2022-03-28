# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:46:46 2022

@author: Pedro
"""
import v2

def main2():
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
            print(f"Presione 1 si quiere que {name1} marque o presione 2 si quiere que {name2} marque: ")
            while True:
                score_sum = input()
                if score_sum in ('1', '2')
                    v2.score(score_sum, puntosp1, puntosp2, name1, name2, puntajes)
                else:
                    print("No ha elegido a nadie")
        elif mode == '2':
            break

if __name__ == "__main__":
    main2()