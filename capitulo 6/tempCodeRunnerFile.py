rios = {
    'parana': 'argentina',
    'nilo': 'egipto',
    'amazonas': 'brasil'
}
for rio in rios.values():
    print(f"Los paises son {rio.title()}")
print("\t")
for rio in rios.keys():
    print(f"Los rios son {rio.title()}")
print("\t")
for rio, pais in rios.items():
    print(f"El rio {rio.title()} pasa por el pais {pais.title()}")