"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    with open("files/input/data.csv", "r") as file:
        data = file.readlines()

    dict_values = {}

    for line in data:
        columns = line.strip().split()
        dict_column = columns[4]
        items = dict_column.split(',')
        for item in items:
            key, value = item.split(':')
            value = int(value)
            if key not in dict_values:
                dict_values[key] = [value]
            else:
                dict_values[key].append(value)

    result = []
    for key in sorted(dict_values.keys()):
        min_value = min(dict_values[key])
        max_value = max(dict_values[key])
        result.append((key, min_value, max_value))

    return result

if __name__ == '__main__':
    print(pregunta_06())