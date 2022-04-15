# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 13:06:05 2022

@author: Pedro
"""

#%% ejercicio 2
def a_count(string1: str) -> int:
    counter = 0
    for i in string1:
        t = i.lower()
        if t == "a":
            counter += 1
    return counter
            


    

#%%ejercicio 5

def ip_colmillos(ip: str) -> str:
    ip = ip.split(".")
    return "[.]".join(ip)
  
    
#%%ejercicio 6 

def finding_joyas(piedras: str, joyas: str) -> int:
    counter = 0
    for i in joyas:
        if i in piedras:
            counter += 1
    return counter

#%% ejercicio 10
a = ord('a')
print (a)

