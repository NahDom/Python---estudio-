nombres =  ['trek', 'cannondale', 'redline', 'specialized']
# Listas o arreglos de python
print(nombres[0] + ' y ' + nombres[1])
print(nombres[0].title() + ' y ' + nombres[1].title())
print(nombres[-1])
# usando cadenas f string

mensaje = f'Mi primer bicicleta fue una {nombres[1].title()}'
print(mensaje)

# Ejercicio 1

amigos = ['negro', 'foco', 'mas negro']

print(amigos[0])
print(amigos[1])
print(amigos[2])

saludos = ['Te odio', 'que trolo eres', 'marik on']

print(saludos[0],amigos[0])
print(saludos[1],amigos[1])
print(saludos[2],amigos[2])

amigos.append('drogadicto')
print(amigos)

# metodo insert -> inserta elementos en la lista al principio de todo, mas no reemplaza el primero original


amigos.insert(0, 'ferra')
print(amigos)
# del borra por completo de la lista el elemento al cual se accedio y ya no puede ser utilizado 
del amigos[1]
print(amigos)

# El final de una lista en python corresponde al principio de una pila, por lo tanto las acciones con el metodo pop(), por defecto lo quitan del final, pero nos permite eliminar cualquier elemento cuya posicion sea conocida, este metodo corresponden a metodos FIFO, primero en entrar y el primero en salir, de igual manera con pop el elemento puede ser reutilizado si es almacenado en una variable o si se lo llama de otro medio ya que solo esta en memoria

print(nombres)
popped_nombres = nombres.pop()
print(nombres)
print(popped_nombres)

# luego esta remove, el cual si bien no conocemos la posicion pero sabemos CUAL es el elemento que queremos eliminar solo basta con llamar a dicho elemento con metodo remove(elemento de lista)

# Consejo: VARAIBLES CON COMILLAS SIMPLES Y TEXTO DE SALIDA CON DOBLES
motos = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motos)
muy_caro = 'suzuki'
motos.remove(muy_caro)
print(f"\n Una {muy_caro.title()} me es demasiado cara.")
print(motos)

# EJERCICIOS

invitados = ['juliana', 'denise', 'mauri', 'ferra', 'lautaro']

message = 'Te invito a mi primera hiperinflacion :D'

print(f"{message}, {invitados[0].title()}")
print(f"{message}, {invitados[1].title()}")
print(f"{message}, {invitados[2].title()}")
print(f"{message}, {invitados[3].title()}")
print(f"{message}, {invitados[4].title()}")
print(f"\n lastimosamente el invitado {invitados[2].title()}, no podra asistir a la hiper, asi que en su lugar invito a otro negro.")
print(f"\n")
invitados.remove('mauri')
# meto a otra persona la lista con el metodo insert
invitados.insert(2, 'Carlos')
message = 'Te invito a mi primera hiperinflacion :D'

print(f"{message}, {invitados[0].title()}")
print(f"{message}, {invitados[1].title()}")
print(f"{message}, {invitados[2].title()}")
print(f"{message}, {invitados[3].title()}")
print(f"{message}, {invitados[4].title()}")
print(f"encontre una mesa mas grande, por lo tanto puedo invitar mas gente a la hiperinflacion de venezuela.")
invitados.insert(0,'tralalero tralala')
invitados.insert(3,'vaca saturna saturnita')
invitados.append('tung tung tung shakur')

print(invitados)

print(f"{message}, {invitados[0].title()}")
print(f"{message}, {invitados[1].title()}")
print(f"{message}, {invitados[2].title()}")
print(f"{message}, {invitados[3].title()}")
print(f"{message}, {invitados[4].title()}")
print(f"{message}, {invitados[5].title()}")
print(f"{message}, {invitados[6].title()}")
print(f"{message}, {invitados[7].title()}")

# reducir la lista de invitados
print(invitados)

print(f"Lo siento pero solo podre invitar a dos personas")
print(f"\n")

invitados.pop()
invitados.pop()
invitados.pop()
invitados.pop()
invitados.pop()
invitados.pop()
print(invitados)

print(f"\n")
print(f"Pero si hay lugar para ustedes dos {invitados[1].title()} y {invitados[0].title()}")

print(f"\n")
print(f"Me enoje los odio asi que los borro")
del invitados[0]
# Como es en tiempo de compilacion el metodo del lista[], convierte los elementos de la lista en concurrentes, de modo que si borraste el primero el segundo se convierte en el primero y asi sucesivamente
del invitados[0]
print(invitados)


