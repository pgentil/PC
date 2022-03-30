# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 11:06:15 2022

@author: Pedro
"""

#from dinosaurs import *

import dinosaurs 

print (dinosaurs.dinosaurs)

from dinosaurs import cantidad_de_dinos

print (cantidad_de_dinos)




import subdirectorio.dinos2 #archivo adentro de carpeta

print (subdirectorio.dinos2.dinosaurs2)

import subdirectorio.dinos2 as dinos2 #puedo usar el nombre dinos2 para directamente llamar lo que tiene adentro

print (dinos2.dinosaurs2)






