# los diccionarios, una estructura que almacena sus elementos, en estructuras de tipo clave:valor,  El valor de una clave puede ser un número, una cadena, una lista o incluso otro diccionario.
# diccionario = {clave:valor}

alien = {'color': 'verde', 'speed': 5}
print(alien)

"""

    el metodo del permite borrar el elemento dentro del diccionario, pero debe acceder a una clave conocida
    nada mas que de ese diccionario se borra ese dato internamente, ya que aunque yo ejecute una instancia del
    mismo llamado a la funcion, voy a crear en memoria OTRO diccionario

"""

# del alien['points']
# print(alien)
# Metodo para llamar a los valores del diccionario para que el get nos devuelva la clave, como primer argumento siempre debe recibir el valor de la clave pero segundo argumento puede ir un mensaje que diga que no se encuentra la clave

point_value = alien.get('points','No points values rescued')
print(point_value)
# acceder al valor del diccionario, se accede por medio de la clave entre corchetes --> diccionario[clave]
# print(alien['color'],alien['points'])
# new_color = alien['color']
# para añadir un elemento
# =========================

# si quiero definir el diccionario vacio 
# diccionario_nombre = {}
# el elemento es accedido por medio del --> []
# print(f"disparaste al alien de color {new_color}")
# dictionary[clave] = valor
# alien['x_position'] = 0
# alien['y_position'] = 25
color = alien['color']
print(f"The color of the alien is {color}")
color_1 = alien['color'] = 'morado'
print(f"Now the color is {color_1}")

estudiante = {}

estudiante['nombre'] = 'nahuel'
estudiante['nota'] = 10
print(estudiante)

# ================================
# Pequeño programa que calcula las posiciones de un alien en pantalla

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

print((f"Posicion original del alien: {alien_0['x_position']}"))

# Mueve el alien a la derecha
# determina cuanto se va a mover el alien basandose en su velocidad actual

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'fast':
    x_increment = 2
else:
    # Debe ser un alien n...
    x_increment = 3

# la posicion nueva es la antigua mas el incremento de velocidad

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"Nueva posicion en pantalla: {alien_0['x_position']}")


