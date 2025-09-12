    
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python','haskell']
}

for name, languages in favorite_languages.items():
    if len(languages) >= 1:
    # la unica forma de acceder a los valores completos ya que esto es una lista de elementos en cada clave de nombres, lo que ocurre aqui
    # es que el segundo elemento que va a tener el valor de los valores, es quien va a ser recorrido en un for interno por ser una lista
        print(f"\n {name.title()} tus lenguajes favoritos son: ")
        for language in languages:
            print(f"\t {language.title()}")
    else:
        print(f"\n {name.title()} tu lenguaje favorito es: ")
        for language in languages:
            print(f"\t {language.title()}")