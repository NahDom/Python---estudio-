iterables = list(range(11))
iterables[len(iterables):] = "hola como estas"
iterables.extend("HOLA")
print(iterables)