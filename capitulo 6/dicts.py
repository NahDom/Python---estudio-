mydict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd':4
    }
# obtener los elementos del diccionario con get
# pudiendo obtener los elementos por medio de la clave o el valor

print(mydict.get('a'))

# para retornar una lista de los items dentro del diccionario
# se usa .items()
# en databricks lo usaria para la obtencion de los elementos de la BD en la cual necesito depositar en batch los datos

# dict.values() devuelve una lista de los valores del diccionario
print(mydict.values())

# dict.keys() retorna una lista de las claves del diccionario
print(mydict.keys())

# en un diccionario los elementos solo pueden ser borrados a partir de su clave y no de su valor, por lo que existen metodos
# pop(), popitem(), .update()
# pop elimina la clave que se le de si es que esta existe en el diccionario
# pop(clave)
# popitem() elimina el ultimo elemento del diccionario
# dict.update(<obj>) --> en este caso update(diccionario_nombre)
# este metodo lo que hace es hacer MERGE de un diccionario con otro, primeramente debe verificar que la clave del primer diccionario se encuentre en el segundo si esta presente solamente actualiza el valor del primero por el valor que tenga el segundo y de no encontrarse un valor en alguno, todo valor es actualizado en el diccionario de salida 

# d2 = {'b': 300, 'z': 40}
# print(mydict.update(d2))
# print(mydict)


frutas = ["manzana", "banana", "cereza"]
# por medio de enumerate(lista) puedo obtener el indice de cada elemento
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")

# pero si quiero todos los valores puedo usar la funcion values()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in sorted(favorite_languages):
    print(f"{name.title()}, gracias por participar")


for valor in favorite_languages.values():
    print(valor.title())

# para omitir un conjunto repetido puedo convertirlo a set por medio de la funcion set en un iterable de tipo diccionario, porque python identifica los valores unicos de una coleccion

for language in set(favorite_languages.values()):
    print(language.title())

language_1 = favorite_languages['sarah'].title() #realmente lo que estamos haciendo es el acceso al valor por medio de la clave
print(f"El lenguaje de Sarah es : {language_1}")

""" Ejercicios """
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for rico in user_0.values():
    print(rico) 

for rico in user_0.keys():
    print(rico)

"""
    La forma de crear un diccionario vacío en Python puede ser con dict() o con {}.
    Un diccionario almacena pares clave:valor. Por ejemplo: {"a": 1, "b": 2}.
    Un diccionario vacío no contiene nada, pero podemos llenarlo con asignaciones,
    ya sea manualmente o dentro de un bucle, como for x in range(...).
"""

b = dict()
#otra forma es con el elemento --> {}
for x in range(1, 20):
    # accedo al valor posicional del elemento del valor por medio del b[]
    b[x] = x ** 2 

print(b)

""" y si quiero ver todo lo que hay en un diccionario? """
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

"""
    Los siguientes bloques de codigo tienen el mismo comportamiento
    lo unico que los hace unicos por decirlo de alguna manera
"""
for name in user_0:
    print(name.title())
for name in user_0.keys():
    print(name.title())

for key, value in user_0.items(): # recuerda que siempre es clave: valor
                                  # Por lo que la forma de recorrido siempre sera la misma en caso de necesitar dichos valores
    print(f"\nkey: {key}")
    print(f"\nvalue: {value}")

""" siempre usar un nombre descriptivo para las variables"""

data = {
    'nombre': 'nahuel'
}

for clave, valor in data.items():
    print(f"\nclave: {clave}")
    print(f"\nvalor: {valor}")
    

# Por ejemplo ahora quiero ver una clave concreta siempre que coincida 
# con una condicion que yo le entrego previamente

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

amigos = ['jen', 'edward']
for nombre in favorite_languages.keys():
    print(f"Hi {nombre.title()}")
    if nombre in amigos:
        lenguaje = favorite_languages[nombre].title()
        # lo que hace es por medio de la clave acceder al valor
        # por medio de la sentencia dict[key] la cual accede al valor
        # de la clave en este caso los lenguajes favoritos de cada persona
        print(f"\n{nombre.title()}, Veo que te gusta {lenguaje}!!!")