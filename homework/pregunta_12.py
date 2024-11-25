"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open("files/input/data.csv", "r") as file:
        data = file.readlines()
    
    result = {}
    for line in data:
        columns = line.strip().split()
        letter = columns[0]
        col5_values = columns[4].split(',')
        
        col5_sum = sum(int(item.split(':')[1]) for item in col5_values)
        
        if letter in result:
            result[letter] += col5_sum
        else:
            result[letter] = col5_sum
    
    return dict(sorted(result.items()))

if __name__ == '__main__':
    print(pregunta_12())
