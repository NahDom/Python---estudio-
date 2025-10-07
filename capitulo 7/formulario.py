# pedir informacion a los usuarios en forma de encuesta en cada paso del while

responses = {}

# configuramos un booleano que nos indique que esta activa la encuesta

polling_active = True

while polling_active:
    # Pedimos el nombre y la respuesta de la persona
    nombre = input("\nCual es su nombre: ")
    respuesta = input("Cual montaña te gustaria escalar? ")
    
    # guardo la respuesta en el diccionario
    
    responses[nombre] = respuesta
    # asi es como puedo asignar a cada diccionario la clave y el valor que contendra
    # averigua si otra persona va a realizar la encuesta
    repito = input("Quiere dejar otra respuesta? (si o no) ")
    # aqui es donde se actualizaria la variable booleana para terminar la ejecucion, de modo que si siempre esta en ejecucion con True pasa a false con la peticion al usuario y de esta forma sale del bucle
    if repito == 'no':
        polling_active = False
    
# la encuesta esta terminada, mostramos los resultados de la misma
print("\n==== RESULTADOS ====")
# muestro los resultados de la encuesta en la salida
for nombre, respuesta in responses.items():
    print(f"{nombre} quiere escalar la montaña {respuesta}")