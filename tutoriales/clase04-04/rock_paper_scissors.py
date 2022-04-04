# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 17:34:30 2022

@author: Pedro
"""

def rps() -> str:
    """Simula una partida de piedra, papel o tijeras y devuelve el ganador"""

    score1 = 0
    score2 = 0
    
    while score1 < 2 and score2 < 2:
        hand1 = input('Que eligio el primer jugador: ')
        hand2 = input('Que eligio el segundo jugador: ')
        if (hand1 == "scissors" and hand2 == "paper" or
            hand1 == "paper" and hand2 == "rock" or
            hand1 == "rock" and hand2 == "scissors"):
            print ("Marco el jugador 1")
            score1 += 1
        elif hand1 == hand2:
            print("Empate")
            continue
        else:
            print ("Marco el jugador 2")
            score2 += 1
    
    if score1 == 2:
        return 'Gano el jugador 1'
    elif score2 == 2:
        return 'Gano el jugador 2'
    
    
def main():
    rps()
    
if __name__ == "__main__":
    main()