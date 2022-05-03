#%%sorted(secuencia)

sorted([2,3,1])
sorted({'x', 'm', 'a'})

#sorted(secuencia, key = funcion, reversed = True/False)
#key hace que para cada elemento de la lista devuelva algun valor

def sq(x):
    return x ** 2

print(sorted([2,-3,1], key= sq))

letras=[('a',0.2), ('b', 0.01), ('c', 0.004)]

def por_valor(par):
    return par[1]

ordenada = sorted(letras, key=por_valor)
ordenada = sorted(letras, key = lambda par:par[1])
print(ordenada)
#lambda parametros : expresion
#def funcion(parametros):
#   return expresion

#%%filter()
#[x for x in seq if fn(x) is True]
#filter(secuencia, ....)
##### VER EN W3SCHOOL
