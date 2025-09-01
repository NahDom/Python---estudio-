def cambiar_numero(x):
    print("Antes:", x, id(x)) # en memoria del interprete
    x = 99 # cambio en tiempo de ejecucion
    print("Después:", x, id(x)) # no cambia en tiempo de compilacion ya qu ese mantiene el valor

# python es todo un objeto porque usa un interprete que encapsula la logica de todo en un solo valor
a = 5
cambiar_numero(a)
print("Afuera:", a, id(a),type(a))
