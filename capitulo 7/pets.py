# eliminar todas las iterancias de "cat"
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

# en realidad lo que debo hacer es ver la existencia del elemento, es decir que tantas veces aparece

while 'cat' in pets:
    pets.remove('cat')

print(pets)