prompt = "\nDime algo, y yo te lo repetire: "
prompt += "\nIngresa 'salida' para terminar la ejecucion del programa: "

# message = ""
# utilizando una condicion booleana
active = True
while active:
    # en python los bucles while son una completa abstraccion del bucle while de C/C++ que controlan siempre la condicion, aunque aqui es mejor controlado por el recolector de basura
    # al menos una vez que la condicion sea igual a la requerida para terminar solo se efectua la salida del bucle de ejecucion en forma directa
    message = input(prompt)
    if message != 'salida': 
        print(message)
    else:
        active = False