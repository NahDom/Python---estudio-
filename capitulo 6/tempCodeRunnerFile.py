favorite_numbers = {
    'jen': [1,2],
    'sarah': [3],
    'edward': [4,5],
    'phil': [6,7]
}

for name, numbers in favorite_numbers.items():
    if len(numbers) > 1:
    # la unica forma de acceder a los valores completos ya que esto es una lista de elementos en cada clave de nombres, lo que ocurre aqui
    # es que el segundo elemento que va a tener el valor de los valores, es quien va a ser recorrido en un for interno por ser una lista
        print(f"\n {name.title()} tus numeros favoritos son: ")
        for number in numbers:
            print(f"\t {number}")
    else:
        print(f"\n {name.title()} tu numero favorito es: ")
        for number in numbers:
            print(f"\t {number}")