aliens = []

# Genero 30 aliens

for alien_numero in range(30):
    # el bucle va a iterar en un rango de 0 a 29 veces en donde en cada pasada
    # creara un nuevo alien con las caracteristicas que le dimos y lo añade a la nueva lista
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
    # ahora quiero que los primeros 3 cambien de color a amarillo y muestren una velocidad media y un valor de 10 puntos cada uno
    for alien in aliens[0:3]:
        if alien['color'] == 'green': 
            # recuerda que la asignacion solo puede ocurrir una vez
           alien['color'] = 'yellow'
           alien['points'] = 10
           alien['speed'] = 'medium'
        elif alien['color'] == 'yellow':
           alien['color'] = 'red'
           alien['points'] = 20
           alien['speed'] = 'fast'
    # muestro los primeros 5 aliens generados
    
    for alien in aliens[0:3]:
        # de esta forma corto la lista
        print(alien)
    print('...')
    
    # quiero mostrar cuandos aliens fueron creados
    
    print(f" Numero total de aliens generados {len(aliens)}")