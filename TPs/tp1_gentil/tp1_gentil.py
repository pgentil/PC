# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 16:50:39 2022

@author: Pedro
"""


def main():
    print ("TeniSim")
    in_choice = input("""Elija en que modo quiere jugar:
                      - Ingrese '1' si quiere jugar el modo manual
                      - Ingrese '2' si quiere jugar el modo simulado""")
    if in_choice == 1:
        n = 2 + 2
        return n
    if in_choice == 2:
        n = 3 + 3