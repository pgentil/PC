# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 10:57:30 2022

@author: Pedro
"""
#%% Try y except
# =============================================================================
# print ("vamos a dividir x por y")
# try:
#     x = int(input(" ingrese x: "))
#     y = int(input(" ingrese y: "))
#     print (x / y)
# except:
#     print ("algo no salio bien revise los datos de entrada")
#     print("nada mas que hacer")
#     
# =============================================================================
#%% Se pueden especificar los errores en except
# =============================================================================
# 
# print ("vamos a dividir x por y")
# try:
#     x = int(input(" ingrese x: "))
#     y = int(input(" ingrese y: "))
#     print (x / y)
# except ValueError:
#     print ("La entrada no se pudo convertir a entero")
# except ZeroDivisionError:
#     print("No se puede dividir por cero")
# except:
#     print("no se que paso xd")
#     print("nada mas que hacer")
# =============================================================================
    
#%% Se le pueden poner nombres

# =============================================================================
# print ("vamos a dividir x por y")
# try:
#     x = int(input(" ingrese x: "))
#     y = int(input(" ingrese y: "))
#     z = (x / y)
#     print (z)
# except ValueError:
#     print ("La entrada no se pudo convertir a entero")
# except ZeroDivisionError as e:
#     print(f"{e}: No se puede dividir por cero")
# except KeyboardInterrupt:
#     print ("apretaste CTRL + C")
# except:
#     print("no se que paso xd")
#     print("nada mas que hacer")
# =============================================================================

#%%
