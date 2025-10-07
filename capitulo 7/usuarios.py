# el siguiente programa de practica es para pasar elementos de una lista a otra por medio de un while
# empieza con usuarios que hay que verificar de una lista 
# y una lista vacia para alojar a los usuarios confirmados
unconfirmed_users = ['alicia', 'brian', 'candace']
confirmed_users = []

# verifica cada usuario hasta que ya no haya usuarios sin confirmar
# es decir que mueve cada usuario verificado a la lista de usuarios confirmados

while unconfirmed_users:
    # python permite como otros lenguajes permite operar por sobre una lista de elementos iterables
    usuarios_corrientes = unconfirmed_users.pop()
    # esto permite que el ultimo usuario de la lista, sea el primero de la siguiente por medio de una variable auxiliar
    
    print(f"Verificando a los usuarios: {usuarios_corrientes.title()}")
    
    confirmed_users.append(usuarios_corrientes) # lo añado a la nueva lista
# Muestra todos los usuarios confirmados
print("\nLos usuarios han sido confirmados: ")
for usuario_confirmado in confirmed_users:
    print(usuario_confirmado.title())