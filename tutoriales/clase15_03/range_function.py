# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 13:29:51 2022

@author: Pedro
"""

def generate_range(min: int, max: int, step: int) -> None:
    maximrange = max + 1
    for i in range(min, maximrange, step):
        print (i)
        
        
def generate_while(num: int, max: int, step: int):
    while num <= max:
        print (num)
        num += step    
        
def fibo(a, b, c):
    a = 1
    b = 1
    

def main():
    generate_range(2, 21, 2)
    generate_while(2, 600, 3)
    
    
if __name__== '__main__':
    main()
    

