# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 11:22:49 2022

@author: Pedro
"""

# =============================================================================
# def sq(seq):
#     for i in range(len(seq)):
#         seq[i] = seq[i] * seq[i]
#     return seq
# 
# if __name__ == "__main__":
#     lista = list(range(10))
#     nueva_lista = sq(lista[:])
#     
# =============================================================================
#%% Shallow copy and deep copy

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]    
]

nueva_matriz = matriz[:]

boolean = (nueva_matriz == matriz)

print(boolean)

nueva_matriz.append("hola")

print(boolean)

nueva_matriz[0].append(4)
print(matriz)
print(boolean)

#como se ve las dos matrices son iguales
#%% mi version

# =============================================================================
# opciones = [
# 	["Play", "See words list", "Quit"],
# 	["Human hangman", "Computer hangman", "Go back"],
# ]
# 
# def menu(prompt: str, opciones: list[str], retries: int = 3, error_msg: str = "Esa opcion no es valida") -> int:
#     
# 	if prompt == "Menu":
# 		print (ennumerate.opciones[0])
# 	elif prompt == "Play":
# 		print (ennumerate.opciones[1])
# 		
# 	while retries > 0:
# 		user_choice = input("Elija la opcion que guste (1, 2 o 3)")
# 		if user_choice in ("1", "2", "3"):
# 			return user_choice
# 		else:
# 			print(error_msg)
# 			retries -= 1
# 
# 
# =============================================================================
	
#%% correcion
def menu(prompt: str, opciones: list[str], retries: int = 3, error_msg: str = "Esa opcion no es valida") -> int:
    print (prompt)
    for i, opcion in enumerate(opciones):
        print(f"{i + 1}. {opcion}")
    
    return opciones[int(input("> ")) - 1]

def ir_izquierda ():
    print("voy izquierda")
def ir_derecha ():
    print("voy derecha")
def ir_arriba ():
    print("voy arriba")
def ir_abajo ():
    print("voy abajo")
    
def menu(prompt: str, opciones: list[str]) -> int:
    print (prompt)
    for i, opcion in enumerate(opciones):
        print(f"{i + 1}. {opcion}")
    
    return opciones[int(input("> ")) - 1]
    
movimientos = {
    'izquierda' : ir_izquierda,
    'derecha' : ir_derecha,
    'arriba' : ir_arriba,
    'abajo' : ir_abajo,
}

move = menu("Hacia donde quieres ir?", list(movimientos.keys()))
movimientos[move]()