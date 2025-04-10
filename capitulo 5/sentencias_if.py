# Ejercicios con IF ELIF ELSE
import random 
cars = ['toyota', 'bmw', 'bbw', 'honda']
for car in cars:
    if car == 'bbw':
        print(car.upper())
    else:
        print(car.title())
    
var = 'ACM1PT'
print(var[::-1].lower()) 

edad = 19
if edad != 21:
    print("tienes 19 buen intento kjj")
    
# not in

baneados = ['elvio', 'lado']

user = 'maria'

if user not in baneados:
    print(f"La usuaria {user.title()} puede postear kjj")

edad = 18
if edad < 18:
    print("puedes pasar al carrusel")
else:
    print("tas viejo kjj")
    
parque = 4

if parque <= 4:
    print("Entrada gratis!")
elif parque <= 18:
    print("paga perro")
    
color_alien = 'amarillo'

if color_alien == 'verde':
    print("Has ganado 5 peronios")
elif color_alien == 'amarillo':
    print("has ganao 10 pelonios")
else:
    print("Ahora si ganaste 15 peronios")
    
fruta = ['manzana', 'durazno', 'pera']

if 'manzana' not in fruta:
    print('me gusta ese')
elif 'banana' not in fruta:
    print('tambien xD')