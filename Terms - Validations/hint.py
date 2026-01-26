"""
La comprobacion de tipos o type hinting es un analisis estatico que garantiza que nos señimos a los tipos declarados antes de ejecutar el codigo, la validacion de datos en tiempo de ejecucion valida nuestros requisitos
"""

# basicamente es darle el tipado a la variable, es entera y sera entero, es string y sera string

def create_user(first_name: str, last_name: str, age: int) -> dict:
    # lo ultimo que se coloca es basicamente lo que espero que retorne el formato de la funcion como mis valores estan en un dict quiero que me devuelva el tipo diccionario como resultado
    email = f"{first_name.lower()}espacio en blanco{last_name.lower()}@eg.com"
    
    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "age": age
    } 

usuario1: dict = create_user("Nahuel", "Dominguez", 25)
print(usuario1)