#%%Ej 1
"El sort"

#%%Ej 2
from tkinter import EXCEPTION


def printkeys(dictionary: dict):
    print (list(dictionary.keys()))

#%%Ej 3
def printvalues(dictionary:dict):
    print (list(dictionary.values()))


#%%Ej 4
def squared(number:int) -> dict:
    dictionary = {}
    if number == 0:
        return dictionary
    elif number < 0:
        for i in range(-1, number - 1, -1):
            dictionary[i] = i ** 2
    else:
        for j in range(1, number + 1):
            dictionary[j] = j ** 2
    return dictionary

#%%Ej5
def dictcount(string:str) -> dict:
    dictionary = {}
    for i in string:
        if i in dictionary.keys():
            pass
        elif i == " ":
            pass
        else:
            dictionary[i.lower()] = string.count(i)
    return dictionary

#%%Ej 6

def currency(inputuser:str, error_msg: str = "The currency you are looking for was not found."):
    dictionary = {
        'euro':'€',
        'dollar':'$',
        'yen':'¥'
    }
    if inputuser not in dictionary.keys():
        raise Exception (error_msg)
    else:
        print (dictionary[inputuser])

#%%Ej 7

def tuple_to_dict(list1: list) -> dict:
    dictionary = {}
    for i in list1:
        if type(i) != tuple or len(i) != 2:
            pass
        else:
            dictionary[i[0]] = i[1]
    return dictionary

#%%Ej8

def tuple_to_dict2(list1: list) -> dict:
    dictionary = {}
    for i in list1:
        if type(i) != tuple or len(i) != 2:
            pass
        elif i[0] in dictionary.keys():
            dictionary[i[0]].append(i[1])
        else:
            dictionary[i[0]] = [i[1]]
    return dictionary

#%%Ej 9

def dados(number: int) -> dict:
    dictionary = {}
    from random import choice
    for i in range(0, number):
        dado1 = choice(list(range(1,7)))
        dado2 = choice(list(range(1,7)))
        suma = dado1 + dado2
        if suma in dictionary.keys():
            dictionary[suma] += 1
        else: 
            dictionary[suma] = 1
    dictionary_ordered = {}
    a = list(dictionary.keys())
    a.sort()
    for i in a:
        dictionary_ordered[i] = dictionary[i]
    return dictionary_ordered
        
#%%Ej 10


def main():
    dictionary = {
        'cielo' : 'celeste',
        'pasto' : 'verde',
        'clifford': 'rojo'
    }

    list_tuple = [('Hernan', 47), ('Ramiro', 65), ('Juan', 20)]
    list_tuple2 = list_tuple + [('Juan', 54)]

    # printkeys(dictionary)
    # printvalues(dictionary)
    #print(squared(8))
    # print(dictcount("Hello World!"))

    # inputuser = input("Please insert a currency: ")
    # currency(inputuser)
    #print(tuple_to_dict(list_tuple))
    # print(tuple_to_dict2(list_tuple2))
    print(dados(10000))



    pass

if __name__ == "__main__":
    main()