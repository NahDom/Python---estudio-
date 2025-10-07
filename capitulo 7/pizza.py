prompt = "\nEscriba aqui que ingredientes quiere introducir a su pizza"
prompt += "\nSi desea salir solo diga 'salir': "

condition = True
ingrediente = []
while condition:
    ingredientes = input(prompt)
    # solicito los ingredientes de la pizza al cliente
    if ingredientes.lower() != 'salir':
        ingrediente.append(ingredientes)
        #print(f"\nExcelente a seleccionado los ingredientes {ingredientes.title()}, ")
        #print(f"\nLos ingredientes que ah elegido son: {ingrediente}")
    else:
       break
    print("\nLos ingredientes son: ")
    print(", ".join(ingrediente))
    #mejor usar una funcion de string que tome los elementos de la lista y los convierta a una salida por renglon mas sencilla, en este caso usando .join(lista)
    print(", ".join([i.title() for i in ingrediente]))
    # esta segunda hace algo un poco mas estilizado si se quiere toma la entrada del usuario y la convierte en lo mismo una salida por coma pero en este caso toma dentro del join un indice ordinal de la lista en i que por medio de list comprehension hace que cada elemento tenga la primer letra en mayuscula