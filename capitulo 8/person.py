"""devolver una estructura de datos mas compleja"""

def build_person(first, last, age= None):
    # devolver un diccionario con datos de la persona mas la edad
    datos = {'Nombre': first, 'Apellido': last, 'edad': age}
    return datos

print(build_person('Nahuel', 'Dominguez', 999))
print(build_person('Nahuel', 'Dominguez', age=999))