"""
    En lo que respecta al uso de las pilas o el uso de las colas en python
    muchas veces el append. es costoso por terminos de tiempo y de desarrollo, esto de la mano
    al interprete 
    Lo que se hace en muchos casos es FIFO
    y se usa la libreria collections que realiza el deque de la lista
    de otra forma python haria insert(elemento, pos) y pop() y seria costoso 
"""

# aplicando la libreria collections
from collections import deque

# inicia la cola de operaciones

cola = deque()

# llegan cinco clientes a comprar al supermercado y van a la cola

for i in range(5):
    # al string que marca al cliente le sumo en la cola posicional un numero como argumento pero como string
    # por ejemplo al 1 le sumo 1 y da el 2, al 2 le sumo 1 y 3 y asi  
    cliente = 'cliente ' + str(i+1)
    print('llega', cliente)
    cola.append(cliente) # insertamos al cliente en la cola
    print('Cola:', cola) # muestro el estado de la cola
    
# salen todos los clientes de la cola
while len(cola) > 0:
    print('sale: ', cola.popleft()) # el popleft hace lo mismo que el pop pero remueve el primero de la cola
                                    # lo hace en forma consecutiva
    print("quedan: ", cola)