
data = {
    'alumno': ['nahuel','juliana','romina','enrqiue'],
    'edad':[25,18,22,35]
}

print("RECORRIDO INCORRECTO")
print("====================")
for key, value in data.items():
    print(f"el nombre del alumno es {key.title()}")
    print(f"la edad del alumno es {value}")
    