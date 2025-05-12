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