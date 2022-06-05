#%%
class Animal:
    def __init__(self, nombre):
        print("llamamos al __init__ del animal") #si sacamos el super del Perro esto se va a aimprimir solo 1 vez
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre}"

    def __repr__(self):
        return f"Animal('{self.nombre}')"


class Perro(Animal):
    def __init__(self, nombre):
        print("llamamos al __init__ del perro")
        super().__init__(nombre) ##super se encarga de mandar el comportamiento de una clase 'hija' a la clase 'madre'

    def __repr__(self):
        return f"Perro('{self.nombre}')"

montoto = Animal("montoto")
lolo = Perro("Lolo") ##Estoy modelando la raza o el nombre de perro? 

if isinstance(lolo, Perro): #me permite ver si un objeto es instancia de la clase Perro
    print(f"{lolo} es instancia de Perro")

if isinstance(lolo, Animal): #me permite ver si un objeto es instancia de la clase Animal
    print(f"{lolo} es instancia de Animal")

#%%
class Animal:
    def __init__(self, nombre):
        print("llamamos al __init__ del animal") #si sacamos el super del Perro esto se va a aimprimir solo 1 vez
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre}"

    def __repr__(self):
        return f"Animal('{self.nombre}')"


class Perro(Animal):
    def __init__(self, nombre):
        self.animal = Animal(nombre) #meti un objeto adentro de una clase, y cuando inicializo el objeto con esta clase hay un objeto adentro de otro
        self.patas = 4 #en este caso el 4 tambien es un objeto, aunque hasta ahora no nos hayamos dado cuenta

    def __repr__(self):
        return f"Perro('{self.nombre}')"
#%%
class Planeta:
    def __init__(self, nombre, tipo):
        self.nommbre = nombre

class SistemaSolar:
    def __init__(self, *nombres):
        self.planetas = [Planeta(n) for n in nombres]


    def __repr__(self):
        return f"SistemaSolar('{self.nombres}')"




#%%
def ejemplo (a1, a2, *args, **kwargs): ##el asterico funciona como un argumento que puede contener un monton de argumentos PROBAR
    print(f"a1: {a1}")
    print(f"a2: {a2}")
    print (args)
    for arg in args:
        print(arg)

ejemplo(*(1, 2, 3, 4, 5, 6, 7, 8)) #poner un asterisco adentro de esta funcion al lado de una tupla hace que se printeen sus elementos
# %%
