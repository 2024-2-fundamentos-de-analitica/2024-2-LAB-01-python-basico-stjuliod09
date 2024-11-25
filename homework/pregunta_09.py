"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}
    """
    with open("files/input/data.csv", "r") as file:
        data = file.readlines()
    
    count_dict = {}
    
    for line in data:
        columns = line.strip().split()
        dict_column = columns[4]
        items = dict_column.split(',')
        
        for item in items:
            key = item.split(':')[0]
            if key in count_dict:
                count_dict[key] += 1
            else:
                count_dict[key] = 1
    
    return dict(sorted(count_dict.items()))

if __name__ == '__main__':
    print(pregunta_09())