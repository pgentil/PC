#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt


class Alumno:
    def __init__(self, nombre, legajo):
        self.nombre = nombre
        self.legajo = legajo
        self.notas = []
        
    def nota_de_cursada(self):
        if len(self.notas) == 0:
            return 0
        return np.mean(self.notas)
    
    def obtener_notas(self):
        return np.array(self.notas)
    
    def cargar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
            
    def __lt__(self, other):
        return self.nota_de_cursada() < other.nota_de_cursada()
    
    def __eq__(self, other):
        return self.nota_de_cursada() == other.nota_de_cursada()
    
    def __repr__(self):
        return f"Alumno('{self.nombre}', {self.legajo})"
            
tomas = Alumno("Tomás", 45345)
joaquin = Alumno("Joaquín", 96832)
lolo = Alumno("Mateo", 92842)

tomas.cargar_nota(8)
tomas.cargar_nota(7)
tomas.cargar_nota(9)
tomas.cargar_nota(5)
tomas.cargar_nota(5)
tomas.cargar_nota(5)


joaquin.cargar_nota(10)
joaquin.cargar_nota(7.5)
joaquin.cargar_nota(5)
joaquin.cargar_nota(9)

lolo.cargar_nota(2)
lolo.cargar_nota(3.5)
lolo.cargar_nota(6)
lolo.cargar_nota(10)

alumnos = [tomas, joaquin, lolo]
plt.plot(tomas.notas, label="Notas de Tomás")

plt.figure()
notas = [0]* 11
for nota in tomas.notas:
    notas[nota] += 1
plt.bar(range(0, 11), notas, label="Notas de Tomás")
plt.legend()


plt.figure()
t = np.linspace(0.1, 100, 1000)
r = t ** 2/np.sqrt(t)
plt.plot(t, r, label="Función t² - sqrt(t)")
plt.title("Graficos")
plt.legend()