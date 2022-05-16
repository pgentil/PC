
from inspect import formatargvalues


def bubble_sort(lista: list) -> list:
    aux = 0
    ord = 1
    while ord != 0:
        ord = 0
        for i in range(len(lista)):
            if lista[i] == lista[-1]:
                pass
            elif lista[i] > lista[i+1]:
                ord = 1
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
            else:
                pass
    return lista
        

def bubble_sort2(lista): #ordenamiento in place
    ordenada = True
    for i in range(len(lista)-1):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
            ordenada = False
    return ordenada, lista

def bubble_sort3(lista): #ordenamiento in place
    ordenada = True
    j = 0
    for i in range(len(lista)-j-1):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
            ordenada = False
            j =+ 1
    return ordenada, lista

def selection_sort(lista: list) -> list: #algoritmo de ordenamiento de seleccion
    idx = 0
    value = lista[idx]
    while idx != len(lista) - 1:
        for i in range(idx + 1, len(lista)):
            if value < lista[i]:
                lista[idx], lista[i] = lista[i], lista[idx]


def merge(seq1, seq2):
    r = []
    i = 0
    j = 0
    while i < len(seq1) and j < len(seq2):
        if seq1[i] < seq2[j]:
            r.append(seq1[i])
            i+= 1
        else:
            r.append(seq2[j])
            j += 1

    while i < len(seq1):
        r.append(seq1[i])
        i += 1
    
    while j < len(seq2):
        r.append(seq2[j])
        j += 1
    
    return r


def sort(seq):
    if len(seq) == 1:
        return seq
    if len(seq) == 2:
        if seq[1] < seq[0]:
            seq[0], seq[1] = seq[1], seq[0]
        return seq

def main():   
    lista = [2, 3, 5, 3, 4, 2, 5, 6, 2, 3, 6, 9, 9, 100, 2, 4]
    print(bubble_sort2(lista))

if __name__ == "__main__":
    main()
