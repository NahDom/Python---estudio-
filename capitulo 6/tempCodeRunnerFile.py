favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

amigos = ['jen', 'edward']
for nombre in favorite_languages.keys():
    print(f"Hi {nombre.title()}")
    if nombre in amigos:
        lenguaje = favorite_languages[nombre].title()
        # lo que hace es por medio de la clave acceder al valor
        # por medio de la sentencia dict[key] la cual accede al valor
        # de la clave en este caso los lenguajes favoritos de cada persona
        print(f"\n{nombre.title()}, Veo que te gusta {lenguaje}!!!")