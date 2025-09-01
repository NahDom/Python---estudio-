def cambiar_numero(x):
    print("Antes:", x, id(x)) # en memoria del interprete
    x = 99 # cambio en tiempo de ejecucion
    print("Después:", x, id(x)) # no cambia en tiempo de compilacion ya qu ese mantiene el valor

""" 

En python es todo un objeto porque usa un interprete que encapsula la logica conviritiendo todo en una instancia de una clase, lo que produce cosas tan interesantes como que la instancia de una clase entero sea un valor, o la instancia de un string un texto determinado por la instancia del objeto

"""
a = 5
cambiar_numero(a)
print("Afuera:", a, id(a),type(a))
