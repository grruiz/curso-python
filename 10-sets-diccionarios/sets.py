"""
SET es un tipo de datos, para tener una coleccion de valores, 
pero no tiene ni indice ni orden
"""

personas = {
    "Victor",
    "Manolo",
    "Antonio"
}

personas.add("Paco")
personas.remove("Manolo")
print(type(personas))
print(personas)