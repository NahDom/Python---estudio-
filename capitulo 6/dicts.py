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

for key, value in user_0.items(): 
    # recuerda que siempre es clave: valor 
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
        
# en este caso quiero que me devuelva una lista ordenada de elementos
# del diccionario, lo hago por medio de ordenar los valores de la clave

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, gracias por responder la encuesta")
    

# ahora solo quiero que me sea devuelto los valores de los elementos dentro del diccionario

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
# recordando a la estructura de datos tipo conjunto: SET() como una estructura de objetos la cual es mutable y no permite repetidos
# lo cual en el analisis de millones de datos puede ser muy util para hacer identificacion de elementos unicos
print("Los siguientes lenguajes fueron mencionados: \t ")
for language in set(favorite_languages.values()):
    print(f"\t {language.title()}")
    
glosario = {
    'python': 'el mejor que hay',
    'python': 'tambien de los mas especializados en OOP',
    'python': 'blah bla blah',
    'python': 'blah bla blah',
    'python': 'blah bla blah',
    'javascript': 'el mas raro de todos los que hay',
    'java':'a veces te preguntas como siguen funcionando...'
}

for lenguaje, definicion in set(glosario.items()):
    print(f"\n {lenguaje.title()}")
    print(f"\n {definicion.title()}")
    
rios = {
    'parana': 'argentina',
    'nilo': 'egipto',
    'amazonas': 'brasil'
}
for rio in rios.values():
    print(f"Los paises son {rio.title()}")
print("\t")
for rio in rios.keys():
    print(f"Los rios son {rio.title()}")
print("\t")
for rio, pais in rios.items():
    print(f"El rio {rio.title()} pasa por el pais {pais.title()}")
    
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

amigos = ['jen', 'edward', 'phil', 'eren', 'jorge']
# primero voy a tener que hacer el inverso
# recorrer la lista y despues ver si estan o no en el diccionario
for nombre in sorted(amigos):
    if nombre in favorite_languages:
        lenguaje = favorite_languages[nombre].title()
        print(f"\n Hola {nombre.title()}, Veo que te gusta {lenguaje}!!!, gracias por participar de la encuesta")
    else:
            print(f"\n {nombre.title()}, Deberias de hacer la encuesta, tu nombre no aparece entre los encuestados")
            
"""
    Anidamiento de funciones
"""

# crea una lista vacia para almacenar aliens
aliens = []

# Genero 30 aliens

for alien_numero in range(30):
    # el bucle va a iterar en un rango de 0 a 29 veces en donde en cada pasada
    # creara un nuevo alien con las caracteristicas que le dimos y lo añade a la nueva lista
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
    # ahora quiero que los primeros 3 cambien de color a amarillo y muestren una velocidad media y un valor de 10 puntos cada uno
    for alien in aliens[0:3]:
        if alien['color'] == 'green': 
            # recuerda que la asignacion solo puede ocurrir una vez
           alien['color'] = 'yellow'
           alien['points'] = 10
           alien['speed'] = 'medium'
        elif alien['color'] == 'yellow':
           alien['color'] = 'red'
           alien['points'] = 20
           alien['speed'] = 'fast'
    # muestro los primeros 5 aliens generados
    
    for alien in aliens[0:3]:
        # de esta forma corto la lista
        print(alien)
    print('...')
    
    # quiero mostrar cuandos aliens fueron creados
    
    print(f" Numero total de aliens generados {len(aliens)}")
    
# Una lista en un diccionario

# por ejemplo una pizzeria

pizza = {
    'corteza': 'crujiente',
    'ingredientes': ['queso mozzarella','aceitunas','pollo']
}

# resumen del pedido

print(f"Ordenaste una pizza {pizza['corteza']}: ")

print("A la misma puede añadirle: ")

# recorro la lista de los ingredientes extras de la pizza:
# al acceder a la clave puedo constantemente iterar sobre cada valor
# lo cual me facilita mostrarlos
for ingrediente in pizza['ingredientes']:
    print("\t"+ ingrediente)
    
# ejemplo numero 2: un diccionario de lenguajes pero cada persona tiene un listado de los lenguajes favoritos

    
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python','haskell']
}

for name, languages in favorite_languages.items():
    # la unica forma de acceder a los valores completos ya que esto es una lista de elementos en cada clave de nombres, lo que ocurre aqui
    # es que el segundo elemento que va a tener el valor de los valores, es quien va a ser recorrido en un for interno por ser una lista
    print(f"\n {name.title()} tus lenguajes favoritos son: ")
    for language in languages:
        print(f"\t {language.title()}")