# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 17:24:46 2022

@author: Pedro
"""

def usd_to_cny(dollars: float) -> float:
    return dollars * 6.75


def usd_to_ars(dollars: float) -> float:
    return dollars * 200


def usd_to_chf(dollars: float) -> float:
    return dollars * 0.94


def main(): #es una buena practica
    coin = input("Ingrese moneda (codigo ISO): ")
    dollars = float(input("Ingrese USD: "))
    while True:
        if coin.upper() == 'CNY':
             cny = usd_to_cny(dollars)
             #  print(cny, "Chinese Yuan")
             # f-strings
             print(f"{cny:.2f} Chinese Yuan") # el . es cant. de decimales, el 2 es la cantidad explicita y la f representa al tipo float
             break
        if coin.upper() == 'ARS':
             ars = usd_to_ars(dollars)
             print(f"{ars:.2f} Pesos")
             break
        if coin.upper() == 'CHF':
             chf = usd_to_chf(dollars)
             print(f"{chf:.2f} Francos Suizos")
             break
        else:
            print("Ninguna moneda fue seleccionada")
    
    
        # .lower() o .upper() para poner variables str en mayusculas o minusculas
   
    
    
if __name__== '__main__': #HAY QUE HACER ESTO PARA TODO CODIGO QUE EJECUTAMOS
    main()
    
    
