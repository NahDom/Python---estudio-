pizza = {
    'corteza': 'crujiente',
    'ingredientes': ['queso mozzarella','aceitunas','pollo']
}

# resumen del pedido

print(f"Ordenaste una pizza {pizza['corteza']}")
print("A la misma puede añadirle: ")
for ingrediente in pizza['ingredientes']:
    print(f"\t"+ ingrediente)