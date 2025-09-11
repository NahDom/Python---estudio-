favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

amigos = ['jen', 'edward', 'phil', 'eren', 'jorge']
# primero voy a tener que hacer el inverso
# recorrer la lista y despues ver si estan o no en el diccionario
for nombre in sorted(amigos):
    if nombre in favorite_languages:
        lenguaje = favorite_languages[nombre].title()
        print(f"\n Hola {nombre.title()}, Veo que te gusta {lenguaje}!!!, gracias por participar de la encuesta")
    else:
            print(f"\n {nombre.title()}, Deberias de hacer la encuesta, tu nombre no aparece entre los encuestados")