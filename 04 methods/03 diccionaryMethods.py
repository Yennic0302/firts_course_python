diccionary = {
    "nombre": "yender",
    "apellido": "rodriguez",
    "edad": 20
}

print(diccionary.keys())
print(diccionary.get("nombre")) #sin exepcion
#       o
print(diccionary["nombre"]) # con exepcion

diccionary.pop('edad')

print(diccionary.items())

print(diccionary)
diccionary.clear()