##
archivo = open("archivo.txt", "rt")
i = 1
for linea in archivo:
    linea = linea.rstrip("\n")
    print(f"{i}: {linea}")
    i+= 1
archivo.close()
##
with open("archivo.txt", "rt") as archivo:
    for i in enumerate(archivo, 1):
        linea = linea.rstrip("\n")
        print(f"{i}: {linea}")
##
with open("archivo.txt", "rt") as archivo:
    for i in enumerate(archivo, 1):
        print(f"{i}: {linea}", end="") ##LE ESTOY DICIENDO AL PRINT QUE NO PONGA EL \N AL FINAL COMO SUELE HACER USUALMENTE

# ESTAS TRES COSAS HACEN LO MISMO ||||||

with open ("prueba.txt", "wt") as archivo:
    while True:
        try:
            linea = input("> ")
            archivo.write(linea + "\n")
        except KeyboardInterrupt:
            break


