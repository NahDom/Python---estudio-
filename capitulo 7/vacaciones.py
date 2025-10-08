# Imprimir una encuesta con las vacaciones soñadas de una persona

lugares = {} # empty dict of places

encuesta = True

while encuesta:
    nombre = input("\nCual es tu nombre?: ")
    respuesta = input("\nA que lugar te encantaria viajar?: ")
    
    lugares[nombre] = respuesta
    
    question = input("\nDesea continuar ('s' o 'n')")
    if question == 'n':
        encuesta = False

for nombre, respuesta in lugares.items():
    print(f"\nA {nombre.title()} le encantaria viajar a {respuesta.title()}")