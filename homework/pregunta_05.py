"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open('files/input/data.csv', 'r') as file:
        data = file.readlines()

    result = {}
    for line in data:
        columns = line.strip().split()
        letter = columns[0]
        value = int(columns[1])
        if letter not in result:
            result[letter] = [value, value]
        else:
            result[letter][0] = max(result[letter][0], value)
            result[letter][1] = min(result[letter][1], value)

    return [(letter, values[0], values[1]) for letter, values in sorted(result.items())]

if __name__ == '__main__':
    print(pregunta_05())