"""funcion que tome un nombre y un apellido y devuelva el mismo en formato completo y limpio"""

def nombre_formateado(first, last):
    #devuelve el nombre formateado
    full = f"{first} {last}"
    return full

nombre_completo = nombre_formateado('Armando', 'Paredes')
print(nombre_completo)

"""practica recomendada aquellos valores que yo defina como variables que pueden pasar como clave en pyton
puedo hacer que directamente esten posicionalmente al final de los parametros, de modo que no se contamine mucho
el codigo, de dicha forma haciendolo mas flexible al cambio"""


def nombre_formateado(first, last, middle=''):
    if middle:
        full = f"{first} {middle} {last}"
    #devuelve el nombre formateado
    else:
        full = f"{first} {last}"
    
    return full.title()

nombre_completo = nombre_formateado('Armando','el paraguayo de', 'Paredes')
print(nombre_completo)