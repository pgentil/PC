# Para testear cada funcion especifica hay que poner un NUEVO ARCHIVO PYTHON
# hay que poner 'test_nombre_de_funcion'

def reverse_list(one_list):
    output = []
    
    for i in range(len(one_list)-1, -1, -1):
        output.append(one_list[i])
        
    return output


def usd_to_chf(dollars: float) -> float:
    return dollars * 0.94

if __name__ == "__main__":
    reverse_list([1,2,3,4])