prompt = "\nIngresa las ciudades que te gustaria ir"
prompt += "\nIngresa 'salida' para salir del programa: "

while True:
    city = input(prompt)
    #le pido al usuario la ciudad que desearia visitar
    # de momento solo es para testear el hecho de que el break permita salir
    #generalmente soy mas de entrar por la condicion opuesta ya que eso ayuda mas a entender el codigo
    if city != 'salida':
        print(f"Me encantaria visitar: {city.title()}")
    else:
        break