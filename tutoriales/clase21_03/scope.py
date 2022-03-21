# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 16:37:56 2022

@author: Pedro
"""

"""
Scope
"""

name = "John"

def func1():
    print(name)
    
def greet(name: str) -> str:
    last_name = "Johnson"
    return f"Hello, {name}"

def main():
    name = "Mike"
    return (greet(name))

if __name__ == "__main__":
    main()
    