# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 14:38:23 2022

@author: Pedro
"""

# =============================================================================
# def get_diet(dinosaur, names, diets, species):
#     names.index(dinosaur)
#     return diets[i]
# 
# def set_diet(dinosaur, diet, names, diets, species):
#     i = name.index(dinosaur)
#     names.remove(dinosaur)
#     diets.pop(i)
#     species.pop(i)
# =============================================================================
    
def get_diet (dinosaur, dinosaurs):
	return dinosaurs[dinosaur][0]

    
dinosaurs = {
    'aardonyx' : ('herbivorous', 'celestae'),
	'zephyrosaurus' : ('herbivorous', 'schaffi'),

}

#Arreglado:
dinosaurs = {
    'aardonyx' : {'diet' : 'herbivorous', 'species' : 'celestae'},
	'zephyrosaurus' : {'diet' : 'herbivorous', 'species' : 'schaffi'},
}
#como agregar un elemento al diccionario
dinosaurs["velociraptor"] = {
    "diet" : "carnivorous",
    "species" : 'memphis',
}

print (dinosaurs)

#para chequear clave
print ("deinonychus" in dinosaurs) #me devuelve false
print ("aardonyx" in dinosaurs) #me devuelve True