chicos = ['juan', 'paco', 'paco']
chicas = ['romina', 'denise', 'pilar']

# no hace correctamente la mezcla
for x in chicas:
    for j in chicos:
        parejas = (x,j)
print(parejas)

# la realiza por medio de funciones lambda
parejas = {(x,j) for x in chicas for j in chicos}
print(parejas)
