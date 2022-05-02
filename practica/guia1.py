# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 16:55:24 2022

@author: Pedro
"""
#%% Ej 11
def greet_msg(name: str):
    return f"Hello {name}" 
def greet():
    name = input()
    msg = greet_msg(name)
    return msg

