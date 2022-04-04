# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 14:32:45 2022

@author: Pedro
"""
def reverse_list(one_list):
    output = []
    
    for i in range(len(one_list)-1, -1, -1):
        output.append(one_list[i])
        
    return output

def reverse_optimized(one_list):
    left = 0
    right = len(one_list) - 1
    
    while left < right:
        aux = one_list[right]
        one_list[right] = one_list[left]
        one_list[left] = aux
        
        right -= 1
        left += 1 
    
    return one_list

def main():
    one_list = [1, 2, 3, 4]
    output = reverse_optimized(one_list)
    print(output)
    pass 

if __name__ == "__main__":
    main()