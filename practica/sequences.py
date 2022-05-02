# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 17:23:47 2022

@author: Pedro
"""

#%% Ej 3
# =============================================================================
# def count(s: str, character: str) -> int:
#     counter = 0
#     for i in s:
#         if i == character:
#             counter += 1
#     return counter
# =============================================================================

#%% Ej 3.1
# =============================================================================
# counter = 0
# texto = input("Ingrese la cadena de texto que quiera:\n")
# character = input("Ingrese el caracter que quiera contar en su cadena de texto:\n")
# for i in texto:
#     if i == character:
#         counter += 1
# print(f"El caracter {character} esta {counter} veces repetido en la cadena de texto")
#         
# =============================================================================

#%% Ej 3.2
# =============================================================================
# counter1 = 0
# counter2 = 0
# texto = input("Ingrese la cadena de texto que quiera:\n")
# character1 = input("Ingrese el primer caracter que quiera contar en su cadena de texto:\n")
# character2 = input("Ingrese el segundo caracter que quiera contar en su cadena de texto:\n")
# for i in texto:
#      if i == character1:
#          counter1 += 1
#      if i == character2:
#          counter2 += 1
# 
# if counter1 > counter2:
#     print(f"El caracter '{character1}' tiene mas ocurrencias en el texto que '{character2}'")
# elif counter2 > counter1:
#     print(f"El caracter '{character2}' tiene mas ocurrencias en el texto que '{character1}'")
# else:
#     print("Los dos caracteres tienen la misma cantidad de ocurrencias")
# =============================================================================

#%% Ej 4
# =============================================================================
# def shorten(s: str) -> str:
#     ss = s[0] + s[int(len(s)/2)] + s[-1]
#     return ss
# 
# =============================================================================
#%% Ej 7
# =============================================================================
# def shorten_message(message: str, n: int) -> str:
#     new_msg = []    
#     for i in range(0, n):
#         if i == len(message):
#             return "".join(new_msg)
#         elif i not in (n-1, n-2, n-3):
#             new_msg.append(message[i])
#         else: 
#             new_msg.append(".")
#     return "".join(new_msg)
# 
# =============================================================================
#%% Ej 8

# =============================================================================
# def enable_password(password: str) -> bool:
#     if password.isalnum() == False and password.isalpha() == False and password.islower() == False and password.isupper() == False and password.isnumeric() == False and 8 <= len(password) <= 31:
#         return True
#     else:
#         return False
# 
# =============================================================================


#%% Ej 9

# =============================================================================
# def sagitarius(birthdate: str) -> bool:
#     bd = birthdate.split("-")
#     month = int(bd[1])
#     date = int(bd[2])
#     if (month == 11 and date >= 22) or (month == 12 and date <= 21):
#         return True
#     else: 
#         return False
# =============================================================================

#%%Ej 10

# def number_control(number):
#     while number not in list(range(0, 27)):
#         if number < 0 :
#             number += 26
#         elif number >= 26:
#             number -=26
#     return number
    
        
# def encryption(message: str, n: int, asciilower: tuple = tuple(range(ord("a"), ord("z") + 1)),asciiupper: tuple = tuple(range(ord("A"), ord("Z") + 1))) -> str:
#     number_control(n)
#     encryptionL = []
#     for i in message:
#         if ord(i) == 32:
#             encryptionL.append(i)
#         elif i.isupper() == True:
#             encrypted_letter = asciiupper.index(ord(i)) + n
#             number_control(encrypted_letter)
#             encryptionL.append(chr(asciiupper[encrypted_letter]))
#         elif i.islower() == True:
#             encrypted_letter = asciilower.index(ord(i)) + n
#             encrypted_letter = number_control(encrypted_letter)
#             encryptionL.append(chr(asciilower[encrypted_letter]))
#     return "".join(encryptionL)


# def desencryption(encr_message: str, n: int, asciilower: tuple = tuple(range(ord("a"), ord("z") + 1)),asciiupper: tuple = tuple(range(ord("A"), ord("Z") + 1))) -> str:
#     desencryptionL = []
#     for i in encr_message:
#         number_control(n)
#         if ord(i) == 32:
#             desencryptionL.append(i)
#         if i.isupper() == True:
#             desencrypted_letter = asciiupper.index(ord(i)) - n
#             number_control(desencrypted_letter)
#             desencryptionL.append(chr(asciiupper[desencrypted_letter]))
#         elif i.islower() == True:
#             desencrypted_letter = asciilower.index(ord(i)) - n
#             desencrypted_letter = number_control(desencrypted_letter)
#             desencryptionL.append(chr(asciilower[desencrypted_letter]))
#     return "".join(desencryptionL)

# if __name__ == "__main__":
#     print(encryption("pepe es un topo asqueroso", 14))
#     print(desencryption(encryption("pepe es un topo asqueroso", 14), 14))

#%%Ej 11

def matches(base: str, word: str) -> bool:
    """Function that takes into account a string and a word and returns True if
    the string can become the word if the '?' signs on it are replaced by letters
    The string has 1 or more '?' sign in it, which indicates a variable having
    the whole alphabet as its domain. The word can be any word.
    Arguments:
    base -- The string containing the '?' signs on it
    word -- The string that takes the role of the word which will determine if the
    base can become the word if the '?' signs are replaced
    """
    if '*' not in base:
        if len(word) != len(base):
            return False
        else:
            for i in range(0, len(word)):
                if base[i] != '?':
                    if base[i] != word[i]:
                        return False
                    else:
                        continue
                else:
                    continue
            
            return True
    else:
        base_list = split.base('*')
        for i in base_list:
            if i not in word:
                if '?' in i:
            else:
                
        for i in range(0, len(base)):
            if base[i] not in ('?', '*'):
                base_list.append(base[i])
            elif base[i] == '*':
                string = 
                base_list.append()
        base_list = base.split('*')
        for 
        
        
        
    
    



if __name__ == "__main__":
