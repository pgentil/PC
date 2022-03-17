# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 12:45:23 2022

@author: Pedro
"""

for i in range (1, 13):
    print (i)

def main():
    month = int(input('Indica en que mes naciste, con un numero del 1 al 12: '))
    if 1 <= month <= 3:
        quarter = '1st quarter'
    if 4 <= month <= 6:
        quarter = '2nd quarter'
    if 7 <= month <= 9:
        quarter = '3rd quarter'
    if 10 <= month <= 12:
        quarter = '4th quarter'
    else:
        "Numero equivocado"
    print (quarter)
    
if __name__== '__main__':
    main()