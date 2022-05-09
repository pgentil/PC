#%% Ej 1
def less():
    with open('texto.txt', 'r') as f:
        for line in f:
            print(line)


#%% Ej 2

def head(filename, N):
    with open(filename, 'r') as f:
        for lines in range(0, N):
            print(f.readlines(), end= '')

#%% EJ 3

def tails(filename, num_lines):
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines[len(lines)- num_lines:]:
            print(line, end="")

#%% EJ 4

def touch(filename):
    with open(filename, 'a'):
        pass 

#%% EJ 5
def cp(filename, newfilename):
    with open(filename, 'r') as f, open(newfilename, 'w') as h:
        for lines in f.readlines():
            h.write(lines) 
        pass
    pass


#%% EJ 6
def wc(filename):
    lineas = 0
    palabras = 0
    caracteres = 0
    with open(filename, 'r') as f:
        print(f.readlines())
        for lines in f.readlines():
            lineas =+ 1
            lista = lines.split(" ")
            palabras =+ len(lista)
            for palabra in lista:
                caracteres =+ len(palabra)
        return lineas, palabras, caracteres, filename

def main():
    #less()
    head('texto.txt', 3)
    tails('texto.txt', 3)
    touch('helo.txt')
    cp('texto.txt', "copy.txt")
    print(wc("texto.txt"))

if __name__ == "__main__":
    main()