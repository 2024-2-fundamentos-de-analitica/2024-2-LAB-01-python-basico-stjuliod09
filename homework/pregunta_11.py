"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """
    with open("files/input/data.csv", "r") as file:
        data = file.readlines()
    
    sum_dict = {}
    for line in data:
        columns = line.strip().split()
        col2 = int(columns[1])
        col4 = columns[3]
        
        for letter in col4.split(','):
            if letter in sum_dict:
                sum_dict[letter] += col2
            else:
                sum_dict[letter] = col2
    
    return dict(sorted(sum_dict.items()))

if __name__ == '__main__':
    print(pregunta_11())
