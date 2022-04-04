# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 16:50:39 2022

@author: Pedro
"""
import simulado
import manual

def main():
    print ("TeniSim")
    while True:
        while True:
            mode = int(input("""Elija en que modo quiere jugar: \n- Ingrese '1' si quiere jugar el modo manual\n- Ingrese '2' si quiere jugar el modo simulado\n> """))     
            if mode in (1, 2):
                break
            else:
                print("No ha seleccionado ningun modo de juego.")
        name1 = input("Nombre del jugador 1: ")
        name2 = input("Nombre del jugador 2: ")
        puntosp1 = 0
        puntosp2 = 0
        puntajes = (0, 15, 30, 40, "Adv.", "Win")
        if mode == 1:
            manual.manual(name1, name2, puntosp1, puntosp2, puntajes)
            break
        if mode == 2:
            simulado.simulado(name1, name2, puntosp1, puntosp2, puntajes)
            break
            
            

if __name__ == "__main__":
    main()
    