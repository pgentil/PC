#%% Ej 1
def less():
    with open('texto.txt', 'r') as f:
        for line in f:
            print(line)
    return None

#%% Ej 2

def head(filename, N):
    with open(filename, 'r') as f:
        for lines in range(0, N):
            print(f.readlines(), end= '')
    return None

#%% EJ 3

def tails(filename, num_lines):
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines[len(lines)- num_lines:]:
            print(line, end="")
    return None

#%% EJ 4

def touch(filename):
    with open(filename, 'a'):
        pass 
    return None

#%% EJ 5
def cp(filename, newfilename):
    with open(filename, 'r') as f, open(newfilename, 'w') as h:
        for lines in f.readlines():
            h.write(lines) 
        pass
    return None


#%% EJ 6
def wc(filename):
    palabras = 0
    caracteres = 0
    with open(filename, 'r') as f:
        lineas = f.readlines()
        n_lineas = len(lineas)
        for line in lineas:
            invalid = line.count(" ") + line.count("\n")
            print (len(line))
            o = line.split(" ")
            palabras = palabras + len(o)
            caracteres = caracteres + len(line) - invalid
            print("o:", o)
        return n_lineas, palabras, caracteres, filename


#%% Ej 7
def grep(string: str, filename:str):
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if string in line:
                print(line.strip("\n"))
        return None

#%%Ej 8
def cat(filename1:str, filename2:str, newfile: str = "newfile.txt"):
    with open (filename1, 'r') as f, open (filename2, 'r') as g, open (newfile, 'w') as h:
        h.write("First file\n")
        for line in f.readlines():
            h.write(line)
        h.write("\nSecond file\n")
        for line2 in g.readlines():
            h.write(line2)
        pass
    return None


#%%Ej 9

#%%Ej 10
def load_data(filename: str) -> dict:
    dictionary = {}
    with open (filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip("\n")
            if len(line.split(":")) == 2:
                key, value = line.split(":")
                dictionary[key] = value
        return dictionary

#%% Ej 11
def save_data(dictionary: dict, filename: str):
    with open(filename, 'a') as f:
        for key in dictionary.keys():
            f.write(f'{key}:{dictionary[key]}\n')
        return None

#%% Ej 12



def main():
    # dictionary = {
    #     'Pasto' : 'verde',
    #     'Cielo' : 'celeste',
    #     'Nube' : 'blanca'
    # }

    #less()
    #head('texto.txt', 3)
    #tails('texto.txt', 3)
    #touch('helo.txt')
    #cp('texto.txt', "copy.txt")
    #print(wc("texto.txt"))
    #grep('a', 'texto.txt')
    #cat("copy.txt", "texto.txt")
    #load_data("helo.txt")
    #save_data(dictionary, "save_data.txt")

    pass

if __name__ == "__main__":
    main()