# imprimier un bucle que va del 1 al 10 pero imprima solo los impares
current_number = 0
while current_number < 20:
    current_number += 1
    if current_number % 2 == 0:
        continue
    # el % es el modulo en la mayoria de lenguajes 
    # mientras que / es la division entera
    print(current_number) # deberia de imprimirlos aqui, solo lo realiza por dentro
