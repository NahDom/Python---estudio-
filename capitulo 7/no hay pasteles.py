postres_no_terminados = ['pastrami','Flan con dulce de leche','pastrami', 'helado artesanal', 'alfajores', 'churros rellenos', 'pastelitos criollos','pastrami','pastrami','pastrami','pastrami']

print("\nYa no nos queda pastrami")

while 'pastrami' in postres_no_terminados:
    # el mientras esta contando y comparando cada elemento en el bucle
    postres_no_terminados.remove('pastrami')

print(postres_no_terminados)