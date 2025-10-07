# haga una lista de postres y rellenelos con lo que mas le guste a medida 
# que vayan saliendo pongalos en una lista de terminados
postres_no_terminados = ['Flan con dulce de leche', 'helado artesanal', 'alfajores', 'churros rellenos', 'pastelitos criollos']
postres_terminados = []

while postres_no_terminados:
    postre = postres_no_terminados.pop()
    print(f"\nSu {postre.title()} aun no esta terminado")
    
    postres_terminados.append(postre)
    # lo añado a la lista de postres terminados
    
print("\n=== POSTRE LISTO ===")
for comida in postres_terminados:
    print(f"\nSu postre {comida} esta listo!")