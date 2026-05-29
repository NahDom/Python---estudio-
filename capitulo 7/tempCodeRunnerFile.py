print("\n===== VENTA DE ENTRADAS =====")
print("\nIngrese las edades de los que quieren ver la pelicula.")

edades = []
total = 0
while True:
    #debo de actualizar la variable de la salida para que cada vez que termine la ejecucion, esto lo puedo hacer siempre con variables locales para la ejecucion del programa, al menos mientras no realize un main()
    entrada = input("Ingrese una edad (o 'salir' para terminar el programa): ")
    # aqui se actualiza la edad de la persona para que cuando ingrese salir salga directamente
    if entrada.lower() == 'salir':
        break
    # aqui lo que ocurre es que obligo a que salga CUANDO SEA SALIR no al revez como cuando lo pongo como una condicion booleana aparte
    """ 
    Debo de tener cuidado mucho cuidado cuando sea un ingreso invertido, si yo tengo que la entrada es DISTINTA A LO QUE DEBE HACER SALIR estare saliendo de la ejecucion eternamente.
    siempre debe ser un Si condicion = salida Entonces Fin, porque al hacerlo al revez la salida de mi condicion es distinta a la que obliga que ingrese
    """
    try:
        # le pido que ingrese su edad en numeros
        # le asigno a la variable edad la entrada para que sea convertida a numerico
        edad = int(entrada)
        edades.append(edad) # añado las edades a una lista de edades
        if edad == 3:
            print(f"\n Entrada de menor de {edad} su ingreso es gratuito")
        elif edad > 3 and edad < 12:
            print(f"\nMenor de 12, tiene {edad}, paga 8 dolares")
            total += 8
        elif edad >= 12:
            print(f"\nMayor de 12 años, edad: {edad} , debe de pagar 12 dolares")
            total += 12
    except ValueError: # para evitar ingresos invalidos solo numeros no caracteres en este punto
        print("\n¡Porfavor, ingrese solamente la edad en numeros!")

# por si quiero mostrar las edades que fueron ingresadas al final
if edades:
    print(f"La cantidad de personas fueron: {len(edades)} personas, de: " + ", ".join(map(str,edades))) 
    #convierto los elementos de la lista para que se muestren como string 
    # porque no hay una forma logica de momento que me ayude a mostrar la lista separa por comas  
    print(f"\nTotal a pagar $ {total}")
else:
    print("\nNo hay edades ingresadas")